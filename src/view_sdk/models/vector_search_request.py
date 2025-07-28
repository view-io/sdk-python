from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enums.vector_search_type_enum import VectorSearchTypeEnum


class VectorSearchRequestModel(BaseModel):
    search_type: Optional[VectorSearchTypeEnum] = Field(
        default=VectorSearchTypeEnum.InnerProduct, alias="searchType"
    )
    tenant_guid: Optional[str] = Field(default=None, alias="TenantGUID")
    vector_repository_guid: Optional[str] = Field(..., alias="VectorRepositoryGUID")
    start_index: Optional[int] = Field(
        default=0, ge=0, alias="StartIndex"
    )  # Ensure non-negative values
    max_results: Optional[int] = Field(
        default=100, ge=1, alias="MaxResults"
    )  # Ensure values are >= 1
    embeddings: Optional[List[float]] = Field(default_factory=list, alias="Embeddings")

    model_config = ConfigDict(populate_by_name=True)
