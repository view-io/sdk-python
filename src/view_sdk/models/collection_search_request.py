from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field

from ..enums.enumeration_order_enum import EnumerationOrderEnum
from .embeddings_rule import EmbeddingsRuleModel
from .query_filter import QueryFilterModel


class CollectionSearchRequestModel(BaseModel):
    GUID: str = Field(default_factory=lambda: str(uuid4()), alias="GUID")
    TenantGUID: str = Field(default_factory=lambda: str(uuid4()), alias="TenantGUID")
    CollectionGUID: str = Field(
        default_factory=lambda: str(uuid4()), alias="CollectionGUID"
    )
    MaxResults: int = Field(default=10, ge=1, le=100, alias="MaxResults")
    Skip: int = Field(default=0, ge=1, alias="Skip")
    ContinuationToken: Optional[str] = Field(default=None, alias="ContinuationToken")
    Ordering: EnumerationOrderEnum = Field(
        default=EnumerationOrderEnum.CreatedDescending, alias="Ordering"
    )
    Filter: QueryFilterModel = Field(default_factory=QueryFilterModel, alias="Filter")
    EmbeddingsRule: Optional[EmbeddingsRuleModel] = Field(
        default=None, alias="EmbeddingsRule"
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
