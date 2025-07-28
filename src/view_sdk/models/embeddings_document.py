import uuid
from datetime import datetime, timezone
from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from .embeddings_rule import EmbeddingsRuleModel
from .semantic_cell import SemanticCellModel


class EmbeddingsDocumentModel(BaseModel):
    """Embeddings document."""

    success: Optional[bool] = Field(
        default=True,
        alias="Success",
        description="Indicates if the parser was successful",
    )

    id: int = Field(default=0, exclude=True, alias="Id")
    guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="GUID", description="GUID"
    )

    document_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        alias="DocumentGUID",
        description="Document GUID",
    )

    tenant_guid: Optional[str] = Field(
        default=None, alias="TenantGUID", description="Tenant GUID"
    )

    collection_guid: Optional[str] = Field(
        default=None, alias="CollectionGUID", description="Collection GUID"
    )

    source_document_guid: Optional[str] = Field(
        default=None, alias="SourceDocumentGUID", description="Source document GUID"
    )

    crawl_plan_guid: Optional[str] = Field(
        default=None, alias="CrawlPlanGUID", description="Crawl plan GUID"
    )
    data_repository_guid: Optional[str] = Field(
        default=None, alias="DataRepositoryGUID", description="Data repository GUID"
    )
    crawl_operation_guid: Optional[str] = Field(
        default=None, alias="CrawlOperationGUID", description="Crawl operation GUID"
    )
    bucket_guid: Optional[str] = Field(
        default=None, alias="BucketGUID", description="Bucket GUID"
    )

    vector_repository_guid: Optional[str] = Field(
        default=None, alias="VectorRepositoryGUID", description="Vector repository GUID"
    )

    graph_repository_guid: Optional[str] = Field(
        default=None, alias="GraphRepositoryGUID", description="Graph repository GUID"
    )

    graph_node_identifier: Optional[str] = Field(
        default=None, alias="GraphNodeIdentifier", description="Graph node identifier"
    )

    object_guid: Optional[str] = Field(
        default=None, alias="ObjectGUID", description="Object GUID"
    )

    object_key: Optional[str] = Field(
        default=None, alias="ObjectKey", description="Object key"
    )

    object_version: Optional[str] = Field(
        default=None, alias="ObjectVersion", description="Object version"
    )

    model: Optional[str] = Field(default=None, alias="Model", description="Model")

    embeddings_rule: Optional[EmbeddingsRuleModel] = Field(
        default=None, alias="EmbeddingsRule", description="Embeddings rule"
    )

    content: Optional[str] = Field(default=None, alias="Content", description="Content")

    score: Optional[Decimal] = Field(default=None, alias="Score", description="Score")

    distance: Optional[Decimal] = Field(
        default=None, alias="Distance", description="Distance"
    )

    semantic_cells: List[SemanticCellModel] = Field(
        default_factory=list, alias="SemanticCells", description="Semantic cells"
    )

    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        alias="CreatedUtc",
        description="Creation timestamp in UTC",
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
