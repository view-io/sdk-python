from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enums.graph_node_type_enum import GraphNodeTypeEnum
from .bucket import BucketMetadataModel
from .collection import CollectionModel
from .data_repository import DataRepositoryModel
from .object_metadata import ObjectMetadataModel
from .pool import StoragePool
from .semantic_cell import SemanticCellModel
from .semantic_chunk import SemanticChunkModel
from .source_document import SourceDocumentModel
from .tenant_metadata import TenantMetadataModel
from .vector_repository import VectorRepositoryModel


class GraphDataModel(BaseModel):
    """Graph data model."""

    type_: GraphNodeTypeEnum = Field(
        default=GraphNodeTypeEnum.Unknown, alias="Type", description="Node type"
    )

    tenant: Optional[TenantMetadataModel] = Field(
        default=None, alias="Tenant", description="Tenant metadata"
    )

    storage_pool: Optional[StoragePool] = Field(
        default=None, alias="StoragePool", description="Storage pool"
    )

    bucket: Optional[BucketMetadataModel] = Field(
        default=None, alias="Bucket", description="Bucket metadata"
    )

    object_: Optional[ObjectMetadataModel] = Field(
        default=None, alias="Object", description="Object metadata"
    )

    collection: Optional[CollectionModel] = Field(
        default=None, alias="Collection", description="Collection"
    )

    source_document: Optional[SourceDocumentModel] = Field(
        default=None, alias="SourceDocument", description="Source document"
    )

    vector_repository: Optional[VectorRepositoryModel] = Field(
        default=None, alias="VectorRepository", description="Vector repository"
    )

    semantic_cell: Optional[SemanticCellModel] = Field(
        default=None, alias="SemanticCell", description="Semantic cell"
    )

    semantic_chunk: Optional[SemanticChunkModel] = Field(
        default=None, alias="SemanticChunk", description="Semantic chunk"
    )

    data_repository: Optional[DataRepositoryModel] = Field(
        default=None, alias="DataRepository", description="Data repository"
    )

    model_config = ConfigDict(populate_by_name=True)
