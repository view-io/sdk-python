from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class TenantMetadataModel(BaseModel):
    id: Optional[int] = Field(default=None, ge=1, exclude=True)  # ID with validation
    guid: Optional[str] = Field(alias="GUID")
    account_guid: Optional[str] = Field(default=None, alias="AccountGUID")
    parent_guid: Optional[str] = Field(default=None, alias="ParentGUID")
    name: Optional[str] = Field(default="", alias="Name")
    region: Optional[str] = Field(default="us-west-1", alias="Region")
    s3_base_domain: Optional[str] = Field(default="", alias="S3BaseDomain")
    rest_base_domain: Optional[str] = Field(default="", alias="RestBaseDomain")
    default_pool_guid: Optional[str] = Field(default="", alias="DefaultPoolGUID")
    active: bool = Field(default=True, alias="Active")
    is_protected: bool = Field(default=False, alias="IsProtected")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
