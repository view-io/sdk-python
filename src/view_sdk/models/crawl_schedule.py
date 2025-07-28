import uuid
from datetime import datetime, timezone
from pydantic import BaseModel, ConfigDict, Field

from ..enums.schedule_interval_enum import ScheduleIntervalEnum


class CrawlScheduleModel(BaseModel):
    id: int = Field(default=0, exclude=True, alias="Id")
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    name: str = Field(..., alias="Name")
    schedule: ScheduleIntervalEnum = Field(
        default=ScheduleIntervalEnum.DaysInterval, alias="Schedule"
    )
    interval: int = Field(default=1, alias="Interval")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(populate_by_name=True)
