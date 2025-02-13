import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enums.bucket_category_enum import BucketCategoryEnum
from .user_master import UserMasterModel


class BucketMetadataModel(BaseModel):
    id: Optional[int] = Field(None, ge=1, alias="Id", exclude=True)
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    pool_guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="PoolGUID")
    owner_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="OwnerGUID"
    )
    category: BucketCategoryEnum = Field(
        default=BucketCategoryEnum.Data, alias="Category"
    )
    name: str = Field(default="", alias="Name")
    region_string: str = Field(default="us-west-1", alias="RegionString")
    versioning: bool = Field(default=True, alias="Versioning")
    retention_minutes: Optional[int] = Field(
        None, ge=1, alias="RetentionMinutes", exclude=True
    )
    max_upload_size: Optional[int] = Field(None, alias="MaxUploadSize")
    max_multipart_upload_seconds: int = Field(
        default=60 * 60 * 24 * 7, alias="MaxMultipartUploadSeconds"
    )
    last_access_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="LastAccessUtc"
    )
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )
    owner: Optional[UserMasterModel] = Field(None, alias="Owner")

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
