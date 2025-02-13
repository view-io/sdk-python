from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class GenerateEmbeddingsRequestModel(BaseModel):
    """Generate embeddings request."""

    model: Optional[str] = Field(default="all-MiniLM-L6-v2", alias="Model")
    api_key: Optional[str] = Field(None, alias="ApiKey")
    contents: List[str] = Field(default_factory=list, alias="Contents")

    model_config = ConfigDict(populate_by_name=True)
