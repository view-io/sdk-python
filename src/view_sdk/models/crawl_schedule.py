from pydantic import BaseModel, ConfigDict, Field


class CrawlScheduleModel(BaseModel):
    name: str = Field(..., alias="Name")
    schedule: str = Field(default="DaysInterval", alias="Schedule")
    interval: int = Field(default=1, alias="Interval")

    model_config = ConfigDict(populate_by_name=True)
