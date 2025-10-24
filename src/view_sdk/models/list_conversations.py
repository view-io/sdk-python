from typing import List

from pydantic import BaseModel, ConfigDict, Field

from .conversation import ConversationModel


class ListConversationsModel(BaseModel):
    conversations: List[ConversationModel] = Field(..., alias="conversations")
    total: int = Field(..., alias="total")
    limit: int = Field(..., alias="limit")
    offset: int = Field(..., alias="offset")

    model_config = ConfigDict(populate_by_name=True)
