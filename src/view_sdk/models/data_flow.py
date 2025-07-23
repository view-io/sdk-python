import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from .step_metadata import StepMetadataModel


class DataFlowModel(BaseModel):
    """Data flow, i.e. a collection of steps and paths."""

    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    trigger_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TriggerGUID"
    )
    step_guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="StepGUID")
    name: str = Field(default="My data flow", alias="Name")
    notes: Optional[str] = Field(default=None, alias="Notes")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )
    log_retention_days: int = Field(
        default=7,
        ge=0,  # Validation for non-negative values
        alias="LogRetentionDays",
    )
    step: Optional[StepMetadataModel] = Field(default=None, alias="Step")

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
