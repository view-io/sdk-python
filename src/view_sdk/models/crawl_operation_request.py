from pydantic import BaseModel, ConfigDict, Field


class CrawlOperationRequestModel(BaseModel):
    name: str = Field(..., alias="Name")

    model_config = ConfigDict(populate_by_name=True)
