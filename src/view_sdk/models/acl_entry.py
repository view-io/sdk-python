from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ACLEntryModel(BaseModel):
    guid: str = Field(alias="GUID")
    tenant_guid: str = Field(alias="TenantGUID")
    bucket_guid: str = Field(alias="BucketGUID")
    owner_guid: str = Field(alias="OwnerGUID")
    user_guid: str = Field(alias="UserGUID")
    canonical_user: str = Field(alias="CanonicalUser")
    enable_read: bool = Field(alias="EnableRead")
    enable_read_acp: bool = Field(alias="EnableReadAcp")
    enable_write: bool = Field(alias="EnableWrite")
    enable_write_acp: bool = Field(alias="EnableWriteAcp")
    full_control: bool = Field(alias="FullControl")
    created_utc: datetime = Field(alias="CreatedUtc")

    model_config = ConfigDict(populate_by_name=True)
