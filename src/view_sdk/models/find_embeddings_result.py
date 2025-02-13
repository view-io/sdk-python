from typing import List

from pydantic import BaseModel, ConfigDict, Field

from ..models.find_embeddings_object import FindEmbeddingsObjectModel
from ..models.timestamp import TimestampModel


class FindEmbeddingsResultModel(BaseModel):
    timestamp: TimestampModel = Field(default_factory=TimestampModel, alias="Timestamp")
    existing: List[FindEmbeddingsObjectModel] = Field(
        default_factory=list, alias="Existing"
    )
    missing: List[FindEmbeddingsObjectModel] = Field(
        default_factory=list, alias="Missing"
    )

    model_config = ConfigDict(populate_by_name=True)
