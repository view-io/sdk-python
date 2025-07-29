from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class EmbeddingsMap(BaseModel):
    """Embeddings map."""

    content: Optional[str] = Field(default=None, alias="Content", description="Content")

    embeddings: List[float] = Field(
        default_factory=list, alias="Embeddings", description="Embeddings"
    )

    model_config = ConfigDict(populate_by_name=True)

    @field_validator("embeddings", mode="before")
    def validate_embeddings(cls, v: Optional[List[float]]) -> List[float]:
        """Ensure embeddings is never None."""
        return v or []
