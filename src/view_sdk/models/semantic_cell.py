import uuid
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..enums.semantic_cell_type_enum import SemanticCellTypeEnum
from .semantic_chunk import SemanticChunkModel


class SemanticCellModel(BaseModel):
    """Semantic cell."""

    guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="GUID", description="GUID"
    )
    cell_type: SemanticCellTypeEnum = Field(
        default=SemanticCellTypeEnum.Text,
        alias="CellType",
        description="Semantic cell type",
    )
    md5_hash: str = Field(default="", alias="MD5Hash", description="MD5")
    sha1_hash: Optional[str] = Field(None, alias="SHA1Hash", description="SHA1")
    sha256_hash: Optional[str] = Field(None, alias="SHA256Hash", description="SHA256")
    position: int = Field(default=0, ge=0, alias="Position", description="Position")
    binary: Optional[bytes] = Field(None, alias="Binary", description="Binary data")
    content: Optional[str] = Field(None, alias="Content", description="Content")
    unordered_list: List[str] = Field(
        default_factory=list, alias="UnorderedList", description="Unordered list"
    )
    ordered_list: List[str] = Field(
        default_factory=list, alias="OrderedList", description="Ordered list"
    )
    chunks: List[SemanticChunkModel] = Field(
        default_factory=list, alias="Chunks", description="Chunks"
    )
    children: List["SemanticCellModel"] = Field(
        default_factory=list, alias="Children", description="Children"
    )

    model_config = ConfigDict(
        use_enum_values=True, populate_by_name=True, validate_assignment=True
    )

    @property
    def length(self) -> int:
        """Length in bytes."""
        return self.count_bytes()

    def count_embeddings(self) -> int:
        """Count the number of embeddings contained within the semantic cell."""
        total = sum(len(chunk.embeddings) for chunk in self.chunks)
        return total + sum(child.count_embeddings() for child in self.children)

    def count_semantic_cells(self) -> int:
        """Count the number of semantic cells in this semantic cell."""
        return 1 + sum(child.count_semantic_cells() for child in self.children)

    def count_bytes(self) -> int:
        """Count the number of bytes contained within chunks within the semantic cell."""
        chunk_bytes = sum(chunk.length for chunk in self.chunks)
        return chunk_bytes + sum(child.count_bytes() for child in self.children)

    @field_validator("chunks", "children", mode="before")
    def validate_lists(cls, v: Optional[List]) -> List:
        """Ensure lists are never None."""
        return v or []

    @classmethod
    def count_embeddings_list(cls, cells: Optional[List["SemanticCellModel"]]) -> int:
        """Count the number of embeddings in a list of semantic cells."""
        return sum(cell.count_embeddings() for cell in (cells or []))

    @classmethod
    def count_semantic_cells_list(
        cls, cells: Optional[List["SemanticCellModel"]]
    ) -> int:
        """Count the number of semantic cells in a list of semantic cells."""
        if not cells:
            return 0
        return sum(1 + cls.count_semantic_cells_list(cell.children) for cell in cells)

    @classmethod
    def count_semantic_chunks_list(
        cls, cells: Optional[List["SemanticCellModel"]]
    ) -> int:
        """Count the number of semantic chunks in a list of semantic cells."""
        if not cells:
            return 0
        return sum(
            len(cell.chunks) + cls.count_semantic_chunks_list(cell.children)
            for cell in cells
        )

    @classmethod
    def count_bytes_list(cls, cells: Optional[List["SemanticCellModel"]]) -> int:
        """Count the number of bytes in chunks within a list of semantic cells."""
        return sum(cell.count_bytes() for cell in (cells or []))
