import uuid
from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, field_validator


class WebhookTargetModel(BaseModel):
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    name: str = Field(default="My webhook target", alias="Name")

    url: HttpUrl = Field(alias="Url")
    content_type: str = Field(default="application/json", alias="ContentType")
    expect_status: int = Field(default=200, ge=100, le=599, alias="ExpectStatus")

    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)

    @field_validator("content_type")
    def validate_content_type(cls, v):
        if not v.strip():
            raise ValueError("Content type must not be empty.")
        return v
