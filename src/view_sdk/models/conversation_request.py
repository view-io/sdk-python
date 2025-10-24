from typing import Dict, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ConversationRequestModel(BaseModel):
    config_guid: UUID = Field(..., alias="config_guid")
    title: str = Field(..., alias="title")
    message: str = Field(..., alias="message")
    metadata: Dict[str, str] = Field(default_factory=dict, alias="metadata")
    documents: Optional[list] = Field(default=None, alias="documents")

    model_config = ConfigDict(populate_by_name=True)
