import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from ..enums.data_catalog_type_enum import DataCatalogTypeEnum


class MetadataRuleModel(BaseModel):
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: Optional[str] = Field(None, alias="TenantGUID")
    bucket_guid: Optional[str] = Field(None, alias="BucketGUID")
    owner_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="OwnerGUID"
    )
    name: Optional[str] = Field(None, alias="Name")
    content_type: str = Field(default="text/plain", alias="ContentType")
    prefix: Optional[str] = Field(None, alias="Prefix")
    suffix: Optional[str] = Field(None, alias="Suffix")
    processing_endpoint: HttpUrl = Field(
        default=HttpUrl("http://localhost:8000/v1.0/tenants/default/processing"),
        alias="ProcessingEndpoint",
    )
    processing_access_key: str = Field(default="default", alias="ProcessingAccessKey")
    cleanup_endpoint: HttpUrl = Field(
        default=HttpUrl(
            "http://localhost:8000/v1.0/tenants/default/processing/cleanup"
        ),
        alias="CleanupEndpoint",
    )
    cleanup_access_key: str = Field(default="default", alias="CleanupAccessKey")
    min_chunk_content_length: int = Field(
        default=2, ge=1, alias="MinChunkContentLength"
    )
    max_chunk_content_length: int = Field(
        default=512, ge=256, le=16384, alias="MaxChunkContentLength"
    )
    max_tokens_per_chunk: int = Field(default=256, ge=1, alias="MaxTokensPerChunk")
    shift_size: int = Field(default=512, ge=1, le=16384, alias="ShiftSize")
    top_terms: int = Field(default=25, ge=1, alias="TopTerms")
    case_insensitive: bool = Field(default=True, alias="CaseInsensitive")
    include_flattened: bool = Field(default=True, alias="IncludeFlattened")
    data_catalog_type: DataCatalogTypeEnum = Field(
        default=DataCatalogTypeEnum.Lexi, alias="DataCatalogType"
    )
    data_catalog_endpoint: HttpUrl = Field(
        default=HttpUrl("http://localhost:8000/"), alias="DataCatalogEndpoint"
    )
    data_catalog_access_key: str = Field(
        default="default", alias="DataCatalogAccessKey"
    )
    data_catalog_collection: Optional[str] = Field(None, alias="DataCatalogCollection")
    graph_repository_guid: Optional[str] = Field(None, alias="GraphRepositoryGUID")
    max_content_length: int = Field(
        default=16 * 1024 * 1024, ge=1, alias="MaxContentLength"
    )
    retention_minutes: Optional[int] = Field(None, ge=1, alias="RetentionMinutes")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
