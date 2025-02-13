import uuid
from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict, Field

from .user_master import UserMasterModel


class MultipartUploadPartModel(BaseModel):
    guid: str = Field(default=None, alias="GUID")
    tenant_guid: str = Field(default=None, alias="TenantGUID")
    bucket_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="BucketGUID"
    )
    pool_guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="PoolGUID")
    node_guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="NodeGUID")
    owner_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="OwnerGUID"
    )
    upload_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="UploadGUID"
    )
    key: str = Field(..., alias="Key")
    started_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="StartedUtc"
    )
    last_access_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="LastAccessUtc"
    )
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )
    expiration_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="ExpirationUtc"
    )
    owner: UserMasterModel = Field(alias="Owner")
    parts: list = Field(default=[], alias="Parts")

    model_config = ConfigDict(populate_by_name=True)
