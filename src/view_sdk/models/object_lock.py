import uuid
from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict, Field, field_validator


class ObjectLockModel(BaseModel):
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    node_guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="NodeGUID")
    bucket_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="BucketGUID"
    )
    owner_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="OwnerGUID"
    )
    object_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="ObjectGUID"
    )

    key: str = Field(default="", alias="Key")
    version: str = Field(default="", alias="Version")
    is_read_lock: bool = Field(default=False, alias="IsReadLock")
    is_write_lock: bool = Field(default=False, alias="IsWriteLock")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)

    @field_validator("key")
    def validate_key(cls, v):
        if v is None:
            raise ValueError("Key must not be None.")
        return v

    @field_validator("version")
    def validate_version(cls, v):
        if v is None:
            raise ValueError("Version must not be None.")
        return v
