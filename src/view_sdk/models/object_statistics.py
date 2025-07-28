from pydantic import BaseModel, ConfigDict, Field


class ObjectStatistics(BaseModel):
    objects: int = Field(default=0, alias="Objects", ge=0)
    bytes: int = Field(default=0, alias="Bytes", ge=0)

    model_config = ConfigDict(populate_by_name=True)
