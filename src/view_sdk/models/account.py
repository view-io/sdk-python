from datetime import datetime, timezone
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator


class AccountModel(BaseModel):
    id: int = Field(default=0, exclude=True, alias="Id")
    guid: str = Field(default_factory=lambda: str(uuid4()), alias="GUID")
    name: str = Field(default=None, alias="Name")
    additional_data: str = Field(default=None, alias="AdditionalData")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(populate_by_name=True)

    @field_validator("id")
    def validate_id(cls, value):
        if value < 0:
            raise ValueError("Id must be non-negative")
        return value
