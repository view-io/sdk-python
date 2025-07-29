from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict


class ContentEmbeddingModel(BaseModel):
    content: Optional[str] = Field(default=None, alias="Content")
    embeddings: List[float] = Field(default_factory=list, alias="Embeddings")

    model_config = ConfigDict(populate_by_name=True)
