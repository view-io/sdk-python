from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from .embeddings_map import EmbeddingsMap


class EmbeddingsResult(BaseModel):
    """Embeddings result."""

    success: bool = Field(
        default=False,
        alias="Success",
        description="Boolean indicating whether or not the operation was successful",
    )

    status_code: int = Field(
        default=200, alias="StatusCode", description="HTTP status code", ge=0, le=599
    )

    model: Optional[str] = Field(
        default=None, alias="Model", description="Model used to generate embeddings"
    )

    result: List[EmbeddingsMap] = Field(
        default_factory=list,
        alias="Result",
        description="Result containing embeddings maps",
    )

    @field_validator("result", mode="before")
    def validate_result(cls, v: Optional[List[EmbeddingsMap]]) -> List[EmbeddingsMap]:
        """Ensure result is never None."""
        return v or []

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
