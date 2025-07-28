import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import Base64Bytes, BaseModel, ConfigDict, Field


class BlobModel(BaseModel):
    id: Optional[int] = Field(None, ge=1, exclude=True, alias="ID")  # JSON ignored
    guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        alias="GUID",
    )
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    content_type: Optional[str] = Field(None, alias="ContentType")
    name: Optional[str] = Field(None, alias="Name")
    description: Optional[str] = Field(None, alias="Description")
    url: Optional[str] = Field(None, alias="URL")
    length: int = Field(0, ge=0, alias="Length")
    ref_obj_type: Optional[str] = Field(None, alias="RefObjType")
    ref_obj_guid: Optional[str] = Field(None, alias="RefObjGUID")
    is_public: bool = Field(default=False, alias="IsPublic")
    md5_hash: str = Field(default="", alias="MD5Hash")
    sha1_hash: Optional[str] = Field(None, alias="SHA1Hash")
    sha256_hash: Optional[str] = Field(None, alias="SHA256Hash")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        alias="CreatedUTC",
    )
    data: Optional[Base64Bytes] = Field(None, alias="Data")

    model_config = ConfigDict(populate_by_name=True)
