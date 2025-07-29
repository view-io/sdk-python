from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from ..models.embeddings_rule import EmbeddingsRuleModel


class GenerateEmbeddingsRequestModel(BaseModel):
    """Generate embeddings request."""

    embeddings_rule: Optional[EmbeddingsRuleModel] = Field(None, alias="EmbeddingsRule")
    model: Optional[str] = Field(default="all-MiniLM-L6-v2", alias="Model")
    api_key: Optional[str] = Field(None, alias="ApiKey")
    contents: List[str] = Field(default_factory=list, alias="Contents")
    embeddings: Optional[List[List[float]]] = Field(default=None, alias="Embeddings")

    model_config = ConfigDict(populate_by_name=True)
