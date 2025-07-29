import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enums.document_type_enum import DocumentTypeEnum
from .document_score import DocumentScoreModel
from .udr_document import UdrDocumentModel


class SourceDocumentModel(BaseModel):
    guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="GUID", description="GUID"
    )
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        alias="TenantGUID",
        description="Tenant GUID",
    )
    bucket_guid: Optional[str] = Field(
        None, alias="BucketGUID", description="Bucket GUID"
    )
    collection_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        alias="CollectionGUID",
        description="Collection GUID",
    )
    object_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        alias="ObjectGUID",
        description="Object GUID",
    )
    graph_repository_guid: Optional[str] = Field(
        None, alias="GraphRepositoryGUID", description="Graph repository GUID"
    )
    graph_node_identifier: Optional[str] = Field(
        None, alias="GraphNodeIdentifier", description="Graph node identifier"
    )
    data_repository_guid: Optional[str] = Field(
        None, alias="DataRepositoryGUID", description="Data repository GUID"
    )
    processing_success: Optional[bool] = Field(
        None,
        alias="ProcessingSuccess",
        description="Boolean indicating if the processing was successful",
    )
    object_key: Optional[str] = Field(None, alias="ObjectKey", description="Key")
    object_version: str = Field(
        default="1", alias="ObjectVersion", description="Version"
    )
    content_type: str = Field(
        default="application/octet-stream",
        alias="ContentType",
        description="Content-type",
    )
    document_type: DocumentTypeEnum = Field(
        default=DocumentTypeEnum.Unknown,
        alias="DocumentType",
        description="Document type",
    )
    source_url: Optional[str] = Field(None, alias="SourceUrl", description="Source URL")
    content_length: int = Field(
        default=0, ge=0, alias="ContentLength", description="Content length"
    )
    md5_hash: str = Field(default="", alias="MD5Hash", description="MD5")
    sha1_hash: Optional[str] = Field(None, alias="SHA1Hash", description="SHA1")
    sha256_hash: Optional[str] = Field(None, alias="SHA256Hash", description="SHA256")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        alias="CreatedUtc",
        description="Creation timestamp, in UTC time",
    )
    expiration_utc: Optional[datetime] = Field(
        None,
        alias="ExpirationUtc",
        description="Expiration timestamp, if any, in UTC time",
    )
    score: Optional[DocumentScoreModel] = Field(
        None, alias="Score", description="Document score"
    )
    udr_document: Optional[UdrDocumentModel] = Field(
        None, alias="UdrDocument", description="UDR document"
    )

    model_config = ConfigDict(
        use_enum_values=True, populate_by_name=True, validate_assignment=True
    )
