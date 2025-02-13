from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AdministratorModel(BaseModel):
    """Administrator model."""

    account_guid: Optional[str] = Field(default=None, alias="AccountGUID")
    guid: Optional[str] = Field(default=None, alias="GUID")
    first_name: Optional[str] = Field(default=None, alias="FirstName")
    last_name: Optional[str] = Field(default=None, alias="LastName")
    full_name: Optional[str] = Field(default=None, alias="FullName")
    email: Optional[str] = Field(default=None, alias="Email")
    password_sha256: Optional[str] = Field(default=None, alias="PasswordSha256")
    telephone: Optional[str] = Field(default=None, alias="Telephone")
    additional_data: Optional[str] = Field(default=None, alias="AdditionalData")
    active: bool = Field(default=True, alias="Active")
    is_protected: bool = Field(default=False, alias="IsProtected")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(populate_by_name=True)
