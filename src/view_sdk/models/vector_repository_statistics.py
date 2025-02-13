from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from .vector_repository import VectorRepositoryModel


class VectorRepositoryStatisticsModel(BaseModel):
    vector_repository: Optional[VectorRepositoryModel] = Field(
        default=None, alias="VectorRepository"
    )
    document_count: int = Field(ge=0, alias="DocumentCount")
    total_bytes: int = Field(ge=0, alias="TotalBytes")
    cell_count: int = Field(ge=0, alias="CellCount")
    chunk_count: int = Field(ge=0, alias="ChunkCount")

    model_config = ConfigDict(populate_by_name=True)

    @classmethod
    def from_data_row(cls, row: dict) -> "VectorRepositoryStatisticsModel":
        if not row:
            return None

        return cls(
            document_count=row.get("document_count", 0),
            total_bytes=row.get("total_bytes", 0),
            cell_count=row.get("num_cells", 0),
            chunk_count=row.get("num_chunks", 0),
        )
