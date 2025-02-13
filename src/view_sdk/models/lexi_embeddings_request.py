import uuid
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from .collection import CollectionModel
from .embeddings_rule import EmbeddingsRuleModel
from .graph_repository import GraphRepositoryModel
from .search_result import SearchResultModel
from .tenant_metadata import TenantMetadataModel
from .vector_repository import VectorRepositoryModel


class LexiEmbeddingsRequest(BaseModel):
    """Lexi embeddings request model."""

    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant: Optional[TenantMetadataModel] = Field(
        default=None, alias="Tenant", description="Tenant metadata"
    )

    collection: Optional[CollectionModel] = Field(
        default=None, alias="Collection", description="Collection"
    )

    results: Optional[SearchResultModel] = Field(
        default=None, alias="Results", description="Search results"
    )

    embeddings_rule: Optional[EmbeddingsRuleModel] = Field(
        default=None, alias="EmbeddingsRule", description="Embeddings rule"
    )

    vector_repository: Optional[VectorRepositoryModel] = Field(
        default=None, alias="VectorRepository", description="Vector repository"
    )

    graph_repository: Optional[GraphRepositoryModel] = Field(
        default=None, alias="GraphRepository", description="Graph repository"
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
