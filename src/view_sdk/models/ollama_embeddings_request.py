from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class OllamaEmbeddingsRequest(BaseModel):
    """Ollama embeddings request."""

    model: Optional[str] = Field(
        default=None,
        alias="model",  # Note: Using lowercase to match JSON property name
        description="Model used to generate embeddings",
    )

    contents: List[str] = Field(
        default_factory=list,
        alias="input",  # Note: Using 'input' to match JSON property name
        description="Contents",
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)

    @field_validator("contents", mode="before")
    def validate_contents(cls, v: Optional[List[str]]) -> List[str]:
        """Ensure contents is never None."""
        return v or []
