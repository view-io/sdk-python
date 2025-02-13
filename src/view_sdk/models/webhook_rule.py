import uuid
from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..enums.webhook_event_type_enum import WebhookEventTypeEnum


class WebhookRuleModel(BaseModel):
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    target_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TargetGUID"
    )
    name: str = Field(default=None, alias="Name")
    event_type: WebhookEventTypeEnum = Field(
        default=WebhookEventTypeEnum.Unknown, alias="EventType"
    )

    max_attempts: int = Field(default=10, ge=0, alias="MaxAttempts")
    retry_interval_ms: int = Field(
        default=30000, ge=1, alias="RetryIntervalMs"
    )  # Default is 30 seconds
    timeout_ms: int = Field(
        default=60000, ge=1, alias="TimeoutMs"
    )  # Default is 1 minute

    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)

    @field_validator("name", mode="before")
    def validate_name(cls, v):
        if v is None or v.strip() == "":
            raise ValueError("Name must not be empty.")
        return v
