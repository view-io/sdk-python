import uuid
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..enums.step_result_enum import StepResultEnum


class DataFlowLogModel(BaseModel):
    """Data flow log."""

    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    data_flow_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="DataFlowGUID"
    )
    request_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="RequestGUID"
    )
    trigger_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TriggerGUID"
    )
    step_guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="StepGUID")
    start_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="StartUtc"
    )
    end_utc: Optional[datetime] = Field(default=None, alias="EndUtc")
    total_ms: Decimal = Field(
        default=Decimal("0"),
        ge=0,  # Ensures non-negative value
        alias="TotalMs",
    )
    result: StepResultEnum = Field(default=StepResultEnum.Success, alias="Result")
    next_step_guid: Optional[str] = Field(default=None, alias="NextStepGUID")
    notes: Optional[str] = Field(default=None, alias="Notes")
    log_expiration_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc) + timedelta(days=7),
        alias="LogExpirationUtc",
    )
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    @field_validator("total_ms")
    def validate_total_ms(cls, v: Decimal) -> Decimal:
        """Ensure total_ms is non-negative."""
        return Decimal("0") if v < 0 else v

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
