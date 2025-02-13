import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class UserMasterModel(BaseModel):
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    first_name: str = Field(default="", alias="FirstName")
    last_name: str = Field(default="", alias="LastName")
    full_name: Optional[str] = Field(default=None, alias="FullName")
    notes: Optional[str] = Field(default="", alias="Notes")
    email: str = Field(default="", alias="Email")
    password_sha256: str = Field(default="", alias="PasswordSha256", exclude=True)
    active: bool = Field(default=True, alias="Active")
    is_protected: bool = Field(default=False, alias="IsProtected")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    # Custom behavior to auto-fill full_name based on first_name and last_name
    @staticmethod
    def full_name_fn(first_name: str, last_name: str) -> str:
        return f"{first_name} {last_name}".strip()

    def __init__(self, **data):
        super().__init__(**data)
        # Automatically compute full_name
        self.full_name = self.full_name_fn(self.first_name, self.last_name)

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
