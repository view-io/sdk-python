from pydantic import BaseModel, ConfigDict, Field

from .collection import CollectionModel


class CollectionStatisticsModel(BaseModel):
    collection: CollectionModel = Field(alias="Collection")
    document_count: int = Field(0, ge=0, alias="DocumentCount")
    total_bytes: int = Field(0, ge=0, alias="TotalBytes")
    term_count: int = Field(0, ge=0, alias="TermCount")
    key_value_count: int = Field(0, ge=0, alias="KeyValueCount")

    model_config = ConfigDict(populate_by_name=True)
