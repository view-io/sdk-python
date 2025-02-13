from typing import List

from pydantic import BaseModel, ConfigDict, Field


class FindEmbeddingsObjectModel(BaseModel):
    sha256_hash: str = Field(alias="SHA256Hash")
    embeddings: List[float] = Field(default_factory=list, alias="Embeddings")

    model_config = ConfigDict(populate_by_name=True)
