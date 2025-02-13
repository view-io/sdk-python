from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class StorageTagModel(BaseModel):
    guid: Optional[str] = Field(None, alias="GUID")
    tenant_guid: Optional[str] = Field(None, alias="TenantGUID")
    bucket_guid: Optional[str] = Field(None, alias="BucketGUID")
    owner_guid: Optional[str] = Field(None, alias="OwnerGUID")
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")
    created_utc: Optional[datetime] = Field(None, alias="CreatedUtc")

    model_config = ConfigDict(populate_by_name=True)
