import uuid
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from .bucket import BucketMetadataModel
from .collection import CollectionModel
from .data_repository import DataRepositoryModel
from .embeddings_rule import EmbeddingsRuleModel
from .graph_repository import GraphRepositoryModel
from .metadata_rule import MetadataRuleModel
from .object_metadata import ObjectMetadataModel
from .pool import StoragePool
from .tenant_metadata import TenantMetadataModel
from .vector_repository import VectorRepositoryModel


class ProcessorRequest(BaseModel):
    """Processor request model."""

    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant: Optional[TenantMetadataModel] = Field(None, alias="Tenant")
    pool: Optional[StoragePool] = Field(None, alias="Pool")
    bucket: Optional[BucketMetadataModel] = Field(None, alias="Bucket")
    data_repository: Optional[DataRepositoryModel] = Field(None, alias="DataRepository")
    collection: Optional[CollectionModel] = Field(None, alias="Collection")
    object: Optional[ObjectMetadataModel] = Field(None, alias="Object")
    metadata_rule: Optional[MetadataRuleModel] = Field(None, alias="MetadataRule")
    embeddings_rule: Optional[EmbeddingsRuleModel] = Field(None, alias="EmbeddingsRule")
    vector_repository: Optional[VectorRepositoryModel] = Field(
        None, alias="VectorRepository"
    )
    graph_repository: Optional[GraphRepositoryModel] = Field(
        None, alias="GraphRepository"
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
