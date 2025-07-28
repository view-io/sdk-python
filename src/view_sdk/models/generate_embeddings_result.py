from typing import List, Optional
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..models.api_error_response import ApiErrorResponseModel  # Adjust import if needed
from ..models.semantic_cell import SemanticCellModel  # Adjust import if needed
from ..models.content_embedding import ContentEmbeddingModel  # Placeholder for ContentEmbedding

class GenerateEmbeddingsResultModel(BaseModel):
    success: bool = Field(default=False, alias="Success")
    status_code: int = Field(default=200, alias="StatusCode")
    error: Optional[ApiErrorResponseModel] = Field(default=None, alias="Error")
    batch_count: int = Field(default=0, alias="BatchCount")
    semantic_cells: List[SemanticCellModel] = Field(default_factory=list, alias="SemanticCells")
    content_embeddings: List[ContentEmbeddingModel] = Field(default_factory=list, alias="ContentEmbeddings")

    model_config = ConfigDict(populate_by_name=True)

    @field_validator("batch_count")
    @classmethod
    def validate_batch_count(cls, v):
        if v < 0:
            raise ValueError("BatchCount must be >= 0.")
        return v 