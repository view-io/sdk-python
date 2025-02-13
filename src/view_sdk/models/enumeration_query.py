from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enums.enumeration_order_enum import EnumerationOrderEnum
from .bucket import BucketMetadataModel
from .collection import CollectionModel
from .graph_repository import GraphRepositoryModel
from .search_filter import SearchFilterModel
from .source_document import SourceDocumentModel
from .tenant_metadata import TenantMetadataModel
from .timestamp import TimestampModel
from .vector_repository import VectorRepositoryModel


class EnumerationQueryModel(BaseModel):
    timestamp: TimestampModel = Field(default=TimestampModel(), alias="Timestamp")
    tenant: Optional[TenantMetadataModel] = Field(None, alias="Tenant")
    tenant_guid: Optional[str] = Field(None, alias="TenantGUID")
    bucket: Optional[BucketMetadataModel] = Field(None, alias="Bucket")
    bucket_guid: Optional[str] = Field(None, alias="BucketGUID")
    collection: Optional[CollectionModel] = Field(None, alias="Collection")
    collection_guid: Optional[str] = Field(None, alias="CollectionGUID")
    source_document: Optional[SourceDocumentModel] = Field(None, alias="SourceDocument")
    source_document_guid: Optional[str] = Field(None, alias="SourceDocumentGUID")
    data_repository_guid: Optional[str] = Field(None, alias="DataRepositoryGUID")
    vector_repository: Optional[VectorRepositoryModel] = Field(
        None, alias="VectorRepository"
    )
    vector_repository_guid: Optional[str] = Field(None, alias="VectorRepositoryGUID")
    graph_repository: Optional[GraphRepositoryModel] = Field(
        None, alias="GraphRepository"
    )
    graph_repository_guid: Optional[str] = Field(None, alias="GraphRepositoryGUID")
    graph_node_identifier: Optional[str] = Field(None, alias="GraphNodeIdentifier")
    max_results: int = Field(default=1000, ge=1, le=1000, alias="MaxResults")
    skip: int = Field(default=0, ge=0, alias="Skip")
    continuation_token: Optional[str] = Field(None, alias="ContinuationToken")
    prefix: Optional[str] = Field(None, alias="Prefix")
    suffix: Optional[str] = Field(None, alias="Suffix")
    delimiter: str = Field(default="", alias="Delimiter")
    include_data: bool = Field(default=False, alias="IncludeData")
    include_owners: bool = Field(default=True, alias="IncludeOwners")
    filters: List[SearchFilterModel] = Field(default_factory=list, alias="Filters")
    ordering: EnumerationOrderEnum = Field(
        default=EnumerationOrderEnum.CreatedDescending, alias="Ordering"
    )

    model_config = ConfigDict(populate_by_name=True)
