from datetime import datetime
from typing import Dict, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ConversationModel(BaseModel):
    conversation_id: UUID = Field(..., alias="conversation_id")
    tenant_guid: UUID = Field(..., alias="tenant_guid")
    user_guid: UUID = Field(..., alias="user_guid")
    session_id: Optional[str] = Field(default=None, alias="session_id")
    config_guid: UUID = Field(..., alias="config_guid")
    title: str = Field(..., alias="title")
    message_count: int = Field(..., alias="message_count")
    last_message_at: datetime = Field(..., alias="last_message_at")
    created_at: datetime = Field(..., alias="created_at")
    updated_at: datetime = Field(..., alias="updated_at")
    metadata: Dict[str, str] = Field(default_factory=dict, alias="metadata")

    model_config = ConfigDict(populate_by_name=True)
