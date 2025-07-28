import uuid
from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict, Field


class CredentialModel(BaseModel):
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    user_guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="UserGUID")
    access_key: str = Field(default="", alias="AccessKey")
    secret_key: str = Field(default="", alias="SecretKey")
    active: bool = Field(default=True, alias="Active")
    is_protected: bool = Field(default=False, alias="IsProtected")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
