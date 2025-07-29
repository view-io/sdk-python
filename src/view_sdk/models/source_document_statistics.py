from pydantic import BaseModel, ConfigDict, Field, computed_field

from .source_document import SourceDocumentModel


class SourceDocumentStatisticsModel(BaseModel):
    """Source document statistics."""

    source_document: SourceDocumentModel = Field(
        ...,  # Required field
        exclude=True,  # JsonIgnore equivalent
        alias="SourceDocument",
        description="Source document",
    )

    model_config = ConfigDict(populate_by_name=True)

    @computed_field
    def tenant_guid(self) -> str:
        """Tenant GUID."""
        return self.source_document.tenant_guid

    @computed_field
    def collection_guid(self) -> str:
        """Collection GUID."""
        return self.source_document.collection_guid

    @computed_field
    def source_document_guid(self) -> str:
        """Source document GUID."""
        return self.source_document.guid

    @computed_field
    def terms(self) -> int:
        """Term count."""
        if (udr := self.source_document.udr_document) and udr.terms:
            return len(udr.terms)
        return 0

    @computed_field
    def distinct_terms(self) -> int:
        """Distinct terms."""
        if (udr := self.source_document.udr_document) and udr.terms:
            return len(set(udr.terms))
        return 0

    @computed_field
    def key_value_pairs(self) -> int:
        """Key-value count."""
        if (
            (udr := self.source_document.udr_document)
            and udr.schema_
            and udr.schema_.flattened
        ):
            return len(udr.schema_.flattened)
        return 0

    @computed_field
    def semantic_cells(self) -> int:
        """Semantic cell count."""
        if (udr := self.source_document.udr_document) and udr.semantic_cells:
            return self._count_semantic_cells(udr.semantic_cells)
        return 0

    @computed_field
    def semantic_cell_bytes(self) -> int:
        """Semantic cell bytes."""
        if (udr := self.source_document.udr_document) and udr.semantic_cells:
            return self._sum_semantic_cell_bytes(udr.semantic_cells)
        return 0

    @computed_field
    def semantic_chunks(self) -> int:
        """Semantic chunk count."""
        if (udr := self.source_document.udr_document) and udr.semantic_cells:
            return self._count_semantic_chunks(udr.semantic_cells)
        return 0

    @computed_field
    def semantic_chunk_bytes(self) -> int:
        """Semantic chunk bytes."""
        if (udr := self.source_document.udr_document) and udr.semantic_cells:
            return self._sum_semantic_chunk_bytes(udr.semantic_cells)
        return 0

    def _count_semantic_cells(self, cells) -> int:
        """Count semantic cells recursively."""
        count = 0
        for cell in cells:
            count += 1
            if cell.children:
                count += self._count_semantic_cells(cell.children)
        return count

    def _sum_semantic_cell_bytes(self, cells) -> int:
        """Sum semantic cell bytes recursively."""
        bytes_sum = 0
        for cell in cells:
            if cell.length > 0:
                bytes_sum += cell.length
            if cell.children:
                bytes_sum += self._sum_semantic_cell_bytes(cell.children)
        return bytes_sum

    def _count_semantic_chunks(self, cells) -> int:
        """Count semantic chunks recursively."""
        count = 0
        for cell in cells:
            if cell.chunks:
                count += len(cell.chunks)
            if cell.children:
                count += self._count_semantic_chunks(cell.children)
        return count

    def _sum_semantic_chunk_bytes(self, cells) -> int:
        """Sum semantic chunk bytes recursively."""
        bytes_sum = 0
        for cell in cells:
            if cell.chunks:
                bytes_sum += sum(chunk.length for chunk in cell.chunks)
            if cell.children:
                bytes_sum += self._sum_semantic_chunk_bytes(cell.children)
        return bytes_sum
