from datetime import datetime, timezone
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from .api_error_response import ApiErrorResponseModel
from .embeddings_document import EmbeddingsDocumentModel


class LexiEmbeddingsResponse(BaseModel):
    """Lexi embeddings response model."""

    guid: Optional[str] = Field(
        default=None, alias="GUID", description="Processor request GUID"
    )

    success: bool = Field(
        default=True, alias="Success", description="Boolean indicating success"
    )
    async_: bool = Field(default=False, alias="Async")
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        alias="Timestamp",
        description="Timestamp",
    )

    error: Optional[ApiErrorResponseModel] = Field(
        default=None, alias="Error", description="Error response, if any"
    )

    vector: List[EmbeddingsDocumentModel] = Field(
        default_factory=list, alias="Vector", description="Embeddings documents"
    )

    @field_validator("vector", mode="before")
    def validate_vector(
        cls, v: Optional[List[EmbeddingsDocumentModel]]
    ) -> List[EmbeddingsDocumentModel]:
        """Ensure vector is never None."""
        return v or []

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
