from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class EmbeddingsRequest(BaseModel):
    """Embeddings request."""

    model: Optional[str] = Field(
        default=None, alias="Model", description="Model used to generate embeddings"
    )

    api_key: Optional[str] = Field(default=None, alias="ApiKey", description="API key")

    contents: List[str] = Field(
        default_factory=list, alias="Contents", description="Contents"
    )

    @field_validator("contents", mode="before")
    def validate_contents(cls, v: Optional[List[str]]) -> List[str]:
        """Ensure contents is never None."""
        return v or []

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
