from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from .embeddings_document import EmbeddingsDocumentModel
from .source_document import SourceDocumentModel
from .timestamp import TimestampModel


class SearchResultModel(BaseModel):
    """Search result model."""

    success: bool = Field(
        default=False,
        alias="Success",
        description="Indicates if the parser was successful",
    )

    timestamp: TimestampModel = Field(
        ...,
        alias="Timestamp",
        description="Timestamp",
    )

    max_results: int = Field(
        alias="MaxResults", description="Maximum number of results to retrieve"
    )

    processing_request_guid: Optional[str] = Field(
        default=None,
        alias="ProcessingRequestGUID",
        description="Processing request GUID",
    )

    end_of_results: bool = Field(
        default=True,
        alias="EndOfResults",
        description="Boolean indicating end of results",
    )

    continuation_token: Optional[str] = Field(
        default=None,
        alias="ContinuationToken",
        description="Continuation token to use when continuing the search",
    )

    records_remaining: int = Field(
        default=0,
        ge=0,  # Ensures non-negative value
        alias="RecordsRemaining",
        description="Number of candidate records remaining in the search",
    )

    documents: Optional[List[SourceDocumentModel]] = Field(
        default=None, alias="Documents", description="Documents that matched the query"
    )

    embeddings: Optional[List[EmbeddingsDocumentModel]] = Field(
        default=None,
        alias="Embeddings",
        description="Embeddings documents generated from matched documents",
    )

    model_config = ConfigDict(populate_by_name=True)

    @field_validator("documents", mode="before")
    def validate_documents(
        cls, v: Optional[List[SourceDocumentModel]]
    ) -> List[SourceDocumentModel]:
        """Ensure documents is never None."""
        return v or []

    @field_validator("embeddings", mode="before")
    def validate_embeddings(
        cls, v: Optional[List[EmbeddingsDocumentModel]]
    ) -> List[EmbeddingsDocumentModel]:
        """Ensure embeddings is never None."""
        return v or []
