import uuid
from pydantic import BaseModel, ConfigDict, Field


class CrawlOperationRequestModel(BaseModel):
    name: str = Field(..., alias="Name")
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")

    model_config = ConfigDict(populate_by_name=True)
