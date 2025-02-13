from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from .api_error_response import ApiErrorResponseModel
from .embeddings_document import EmbeddingsDocumentModel
from .source_document import SourceDocumentModel
from .type_result import TypeResultModel
from .udr_document import UdrDocumentModel


class ProcessorResponse(BaseModel):
    """Processor response model."""

    guid: Optional[str] = Field(
        default=None, alias="GUID", description="Processor request GUID"
    )

    success: bool = Field(
        default=True, alias="Success", description="Boolean indicating success"
    )

    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        alias="Timestamp",
        description="Timestamps",
    )

    error: Optional[ApiErrorResponseModel] = Field(
        default=None, alias="Error", description="Error response, if any"
    )

    type: Optional[TypeResultModel] = Field(
        default=None, alias="Type", description="Type result"
    )

    udr: Optional[UdrDocumentModel] = Field(
        default=None, alias="Udr", description="UDR document"
    )

    source: Optional[SourceDocumentModel] = Field(
        default=None, alias="Source", description="Source document in data catalog"
    )

    vector: Optional[EmbeddingsDocumentModel] = Field(
        default=None, alias="Vector", description="Embeddings document"
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
