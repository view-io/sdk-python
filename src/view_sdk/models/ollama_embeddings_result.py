from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class OllamaEmbeddingsResult(BaseModel):
    """Ollama embeddings result."""

    model: Optional[str] = Field(
        default=None,
        alias="model",  # Note: Using lowercase to match JSON property name
        description="Model",
    )

    embeddings: List[List[float]] = Field(
        default_factory=list,
        alias="embeddings",  # Note: Using lowercase to match JSON property name
        description="List of embeddings",
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)

    @field_validator("embeddings", mode="before")
    def validate_embeddings(cls, v: Optional[List[List[float]]]) -> List[List[float]]:
        """Ensure embeddings is never None."""
        return v or []
