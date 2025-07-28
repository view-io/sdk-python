from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class LangchainEmbeddingsResult(BaseModel):
    """Langchain embeddings result."""

    success: bool = Field(
        default=False,
        alias="Success",
        description="Boolean indicating whether or not the operation was successful",
    )

    status_code: int = Field(
        default=0, alias="StatusCode", description="HTTP status code"
    )

    model: Optional[str] = Field(
        default=None, alias="Model", description="Model used to generate embeddings"
    )

    contents: List[str] = Field(
        default_factory=list, alias="Contents", description="Contents"
    )

    embeddings: List[List[float]] = Field(
        default_factory=list, alias="Embeddings", description="List of embeddings"
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)

    @field_validator("contents", mode="before")
    def validate_contents(cls, v: Optional[List[str]]) -> List[str]:
        """Ensure contents is never None."""
        return v or []

    @field_validator("embeddings", mode="before")
    def validate_embeddings(cls, v: Optional[List[List[float]]]) -> List[List[float]]:
        """Ensure embeddings is never None."""
        return v or []
