from datetime import datetime, timezone
from typing import List, Optional
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field

from ..enums.semantic_cell_type_enum import SemanticCellTypeEnum


class VectorChunkModel(BaseModel):
    document_guid: str = Field(
        default_factory=lambda: str(uuid4()), alias="DocumentGUID"
    )
    tenant_guid: Optional[str] = Field(None, alias="TenantGUID")
    collection_guid: Optional[str] = Field(None, alias="CollectionGUID")
    source_document_guid: Optional[str] = Field(None, alias="SourceDocumentGUID")
    bucket_guid: Optional[str] = Field(None, alias="BucketGUID")
    vector_repository_guid: Optional[str] = Field(None, alias="VectorRepositoryGUID")
    graph_repository_guid: Optional[str] = Field(None, alias="GraphRepositoryGUID")
    graph_node_identifier: Optional[str] = Field(None, alias="GraphNodeIdentifier")
    object_guid: Optional[str] = Field(None, alias="ObjectGUID")
    object_key: Optional[str] = Field(None, alias="ObjectKey")
    object_version: Optional[str] = Field(None, alias="ObjectVersion")
    model: Optional[str] = Field(None, alias="Model")
    cell_guid: str = Field(default_factory=lambda: str(uuid4()), alias="CellGUID")
    cell_type: SemanticCellTypeEnum = Field(SemanticCellTypeEnum.Text, alias="CellType")
    cell_md5_hash: str = Field("", alias="CellMD5Hash")
    cell_sha1_hash: Optional[str] = Field(None, alias="CellSHA1Hash")
    cell_sha256_hash: Optional[str] = Field(None, alias="CellSHA256Hash")
    cell_position: int = Field(default=0, ge=0, alias="CellPosition")
    chunk_guid: str = Field(default_factory=lambda: str(uuid4()), alias="ChunkGUID")
    chunk_md5_hash: Optional[str] = Field(None, alias="ChunkMD5Hash")
    chunk_sha1_hash: Optional[str] = Field(None, alias="ChunkSHA1Hash")
    chunk_sha256_hash: Optional[str] = Field(None, alias="ChunkSHA256Hash")
    chunk_position: int = Field(default=0, ge=0, alias="ChunkPosition")
    chunk_length: int = Field(default=0, ge=0, alias="ChunkLength")
    content: Optional[str] = Field(None, alias="Content")
    score: Optional[float] = Field(None, alias="Score")
    distance: Optional[float] = Field(None, alias="Distance")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUTC"
    )
    embeddings: List[float] = Field(default_factory=list, alias="Embeddings")

    model_config = ConfigDict(populate_by_name=True)
