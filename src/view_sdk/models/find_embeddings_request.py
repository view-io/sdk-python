from typing import List

from pydantic import BaseModel, ConfigDict, Field

from ..models.find_embeddings_object import FindEmbeddingsObjectModel


class FindEmbeddingsRequestModel(BaseModel):
    tenant_guid: str = Field(None, alias="TenantGUID")
    vector_repository_guid: str = Field(None, alias="VectorRepositoryGUID")
    criteria: List[FindEmbeddingsObjectModel] = Field(
        default_factory=list, alias="Criteria"
    )

    model_config = ConfigDict(populate_by_name=True)
