from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..enums.document_type_enum import DocumentTypeEnum


class IngestionQueueEntryModel(BaseModel):
    """Ingestion queue entry."""

    guid: str = Field(default_factory=lambda: str(uuid4()), alias="GUID")
    tenant_guid: str = Field(default_factory=lambda: str(uuid4()), alias="TenantGUID")
    collection_guid: str = Field(
        default_factory=lambda: str(uuid4()), alias="CollectionGUID"
    )
    source_document_guid: str = Field(
        default_factory=lambda: str(uuid4()), alias="SourceDocumentGUID"
    )
    document_type: DocumentTypeEnum = Field(
        default=DocumentTypeEnum.Unknown, alias="DocumentType"
    )
    object_key: Optional[str] = Field(default=None, alias="ObjectKey")
    object_version: str = Field(default="1", alias="ObjectVersion")
    content_length: int = Field(default=0, alias="ContentLength", ge=0)
    message: Optional[str] = Field(default=None, alias="Message")
    start_utc: Optional[datetime] = Field(default=None, alias="StartUtc")
    success_utc: Optional[datetime] = Field(default=None, alias="SuccessUtc")
    failure_utc: Optional[datetime] = Field(default=None, alias="FailureUtc")
    total_ms: Optional[Decimal] = Field(default=None, alias="TotalMs")
    term_processing_ms: Optional[Decimal] = Field(
        default=None, alias="TermProcessingMs"
    )
    schema_processing_ms: Optional[Decimal] = Field(
        default=None, alias="SchemaProcessingMs"
    )
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)

    @field_validator("content_length")
    def validate_content_length(cls, v):
        if v < 0:
            raise ValueError("ContentLength must be greater than or equal to 0")
        return v
