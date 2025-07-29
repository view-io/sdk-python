from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from ..models.find_embeddings_object import FindEmbeddingsObjectModel
from ..models.embeddings_rule import EmbeddingsRuleModel
from ..models.vector_repository import VectorRepositoryModel


class FindEmbeddingsRequestModel(BaseModel):
    tenant_guid: str = Field(None, alias="TenantGUID")
    embeddings_rule_guid: str = Field(None, alias="EmbeddingsRuleGUID")
    embeddings_rule: Optional[EmbeddingsRuleModel] = Field(None, alias="EmbeddingsRule")
    vector_repository_guid: str = Field(None, alias="VectorRepositoryGUID")
    vector_repository: Optional[VectorRepositoryModel] = Field(
        None, alias="VectorRepository"
    )
    criteria: List[FindEmbeddingsObjectModel] = Field(
        default_factory=list, alias="Criteria"
    )

    model_config = ConfigDict(populate_by_name=True)
