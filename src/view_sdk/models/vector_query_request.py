from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class VectorQueryRequestModel(BaseModel):
    query: Optional[str] = Field(None, alias="Query")
    vector_repository_guid: str = Field(..., alias="VectorRepositoryGUID")

    model_config = ConfigDict(populate_by_name=True)
