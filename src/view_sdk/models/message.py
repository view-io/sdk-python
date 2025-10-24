from datetime import datetime
from typing import Dict, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class MessageModel(BaseModel):
    message_id: UUID = Field(..., alias="message_id")
    conversation_id: UUID = Field(..., alias="conversation_id")
    role: str = Field(..., alias="role")
    content: str = Field(..., alias="content")
    sources: Optional[list] = Field(default=None, alias="sources")
    metadata: Dict[str, float] | None = Field(default=None, alias="metadata")
    created_at: datetime = Field(..., alias="created_at")
    is_superseded: bool = Field(default=False, alias="is_superseded")
    superseded_at: Optional[datetime] = Field(default=None, alias="superseded_at")
    superseded_by_message_id: Optional[UUID] = Field(default=None, alias="superseded_by_message_id")
    edited_at: Optional[datetime] = Field(default=None, alias="edited_at")
    original_content: Optional[str] = Field(default=None, alias="original_content")

    model_config = ConfigDict(populate_by_name=True)
