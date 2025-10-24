from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class MessageRequestModel(BaseModel):
    message: str = Field(..., description="The message to add")
    documents: Optional[list] = Field(default=None, description="The documents to add")

    model_config = ConfigDict(populate_by_name=True)
