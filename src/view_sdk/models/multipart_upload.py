import uuid
from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

from .user_master import UserMasterModel


class MultipartUploadPartModel(BaseModel):
    guid: Optional[str] = Field(default=None, alias="GUID")
    tenant_guid: Optional[str] = Field(default=None, alias="TenantGUID")
    bucket_guid: Optional[str] = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="BucketGUID"
    )
    pool_guid: Optional[str] = Field(default=None, alias="PoolGUID")
    node_guid: Optional[str] = Field(default=None, alias="NodeGUID")
    owner_guid: Optional[str] = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="OwnerGUID"
    )
    upload_guid: Optional[str] = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="UploadGUID"
    )
    key: str = Field(..., alias="Key")
    started_utc: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="StartedUtc"
    )
    last_access_utc: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="LastAccessUtc"
    )
    created_utc: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )
    expiration_utc: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="ExpirationUtc"
    )
    owner: Optional[UserMasterModel] = Field(alias="Owner")
    parts: Optional[list] = Field(default=[], alias="Parts")

    model_config = ConfigDict(populate_by_name=True)
