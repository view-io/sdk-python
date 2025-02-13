import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, field_validator

from ..enums.webhook_event_type_enum import WebhookEventTypeEnum


class WebhookEventModel(BaseModel):
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    target_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TargetGUID"
    )
    rule_guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="RuleGUID")
    event_type: WebhookEventTypeEnum = Field(
        default=WebhookEventTypeEnum.Unknown, alias="EventType"
    )

    content_length: int = Field(default=0, ge=0, alias="ContentLength")
    timeout_ms: int = Field(default=60000, ge=1, alias="TimeoutMs")
    url: HttpUrl = Field(alias="Url")  # Validates as a proper URL
    content_type: str = Field(default="application/json", alias="ContentType")
    expect_status: int = Field(default=200, ge=100, le=599, alias="ExpectStatus")
    retry_interval_ms: int = Field(default=10000, ge=1, alias="RetryIntervalMs")
    attempt: int = Field(default=0, ge=0, alias="Attempt")
    max_attempts: int = Field(default=5, ge=1, alias="MaxAttempts")
    http_status: int = Field(default=0, ge=0, le=599, alias="HttpStatus")

    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )
    added_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="AddedUtc"
    )
    last_attempt_utc: Optional[datetime] = Field(None, alias="LastAttemptUtc")
    next_attempt_utc: Optional[datetime] = Field(None, alias="NextAttemptUtc")
    last_failure_utc: Optional[datetime] = Field(None, alias="LastFailureUtc")
    success_utc: Optional[datetime] = Field(None, alias="SuccessUtc")
    failed_utc: Optional[datetime] = Field(None, alias="FailedUtc")

    @field_validator("url")
    def validate_url(cls, v):
        if not v:
            raise ValueError("Url must not be empty.")
        return v

    @field_validator("content_type")
    def validate_content_type(cls, v):
        if not v:
            raise ValueError("ContentType must not be empty.")
        return v

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
