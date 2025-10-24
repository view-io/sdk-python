from typing import List

from pydantic import BaseModel, ConfigDict, Field

from .conversation import ConversationModel
from .message import MessageModel


class ConversationWithMessagesModel(BaseModel):
    conversation: ConversationModel = Field(..., alias="conversation")
    messages: List[MessageModel] = Field(..., alias="messages")

    model_config = ConfigDict(populate_by_name=True)
