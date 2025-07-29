import uuid
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ..models.bucket import BucketMetadataModel
from ..models.collection import CollectionModel
from ..models.data_repository import DataRepositoryModel
from ..models.embeddings_rule import EmbeddingsRuleModel
from ..models.graph_repository import GraphRepositoryModel
from ..models.metadata_rule import MetadataRuleModel
from ..models.object_metadata import ObjectMetadataModel
from ..models.pool import StoragePool
from ..models.tenant_metadata import TenantMetadataModel
from ..models.vector_repository import VectorRepositoryModel


class CleanupRequest(BaseModel):
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    async_: bool = Field(default=True, alias="Async")
    tenant: Optional[TenantMetadataModel] = Field(None, alias="Tenant")
    collection: Optional[CollectionModel] = Field(None, alias="Collection")
    pool: Optional[StoragePool] = Field(None, alias="Pool")
    bucket: Optional[BucketMetadataModel] = Field(None, alias="Bucket")
    data_repository: Optional[DataRepositoryModel] = Field(None, alias="DataRepository")
    object: ObjectMetadataModel = Field(None, alias="Object")
    metadata_rule: MetadataRuleModel = Field(None, alias="MetadataRule")
    embeddings_rule: Optional[EmbeddingsRuleModel] = Field(None, alias="EmbeddingsRule")
    vector_repository: Optional[VectorRepositoryModel] = Field(
        None, alias="VectorRepository"
    )
    graph_repository: Optional[GraphRepositoryModel] = Field(
        None, alias="GraphRepository"
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
