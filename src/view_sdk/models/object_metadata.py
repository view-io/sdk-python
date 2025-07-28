import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..enums.document_type_enum import DocumentTypeEnum


class ObjectMetadataModel(BaseModel):
    """Object metadata."""

    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    parent_guid: Optional[str] = Field(default=None, alias="ParentGUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    tenant_name: Optional[str] = Field(default=None, alias="TenantName")
    node_guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="NodeGUID")
    pool_guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="PoolGUID")
    bucket_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="BucketGUID"
    )
    bucket_name: Optional[str] = Field(default=None, alias="BucketName")
    owner_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="OwnerGUID"
    )
    encryption_key_guid: Optional[str] = Field(default=None, alias="EncryptionKeyGUID")
    data_catalog_document_guid: Optional[str] = Field(
        default=None, alias="DataCatalogDocumentGUID"
    )
    data_repository_guid: Optional[str] = Field(
        default=None, alias="DataRepositoryGUID"
    )
    crawl_operation_guid: Optional[str] = Field(
        default=None, alias="CrawlOperationGUID"
    )
    graph_repository_guid: Optional[str] = Field(
        default=None, alias="GraphRepositoryGUID"
    )
    graph_node_identifier: Optional[str] = Field(
        default=None, alias="GraphNodeIdentifier"
    )
    processing_success: Optional[bool] = Field(default=None, alias="ProcessingSuccess")
    key: str = Field(default="", alias="Key")
    version: str = Field(default="", alias="Version")
    is_latest: bool = Field(default=True, alias="IsLatest")
    is_delete_marker: bool = Field(default=False, alias="IsDeleteMarker")
    is_local: bool = Field(default=True, alias="IsLocal")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    document_type: DocumentTypeEnum = Field(
        default=DocumentTypeEnum.Unknown, alias="DocumentType"
    )
    content_length: int = Field(
        default=0,
        ge=0,  # Ensures non-negative value
        alias="ContentLength",
    )
    source_url: Optional[str] = Field(default=None, alias="SourceUrl")
    md5_hash: str = Field(default="", alias="MD5Hash")
    sha1_hash: Optional[str] = Field(default=None, alias="SHA1Hash")
    sha256_hash: Optional[str] = Field(default=None, alias="SHA256Hash")
    expiration_utc: Optional[datetime] = Field(default=None, alias="ExpirationUtc")
    last_access_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="LastAccessUtc"
    )
    last_modified_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="LastModifiedUtc"
    )
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )
    data: Optional[bytes] = Field(default=None, alias="Data")

    @field_validator("content_length")
    def validate_content_length(cls, v: int) -> int:
        """Ensure content_length is non-negative."""
        if v < 0:
            raise ValueError("ContentLength must be non-negative")
        return v

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
