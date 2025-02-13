from pydantic import BaseModel, ConfigDict, Field


class CrawlFilterModel(BaseModel):
    name: str = Field(..., alias="Name")
    minimum_size: int = Field(default=1, ge=1, alias="MinimumSize")
    maximum_size: int = Field(default=134217728, le=134217728, alias="MaximumSize")
    include_subdirectories: bool = Field(default=True, alias="IncludeSubdirectories")
    content_type: str = Field(default="*", alias="ContentType")

    model_config = ConfigDict(populate_by_name=True)
