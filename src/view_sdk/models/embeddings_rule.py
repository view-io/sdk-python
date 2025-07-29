import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..enums.embeddings_generator_enum import EmbeddingsGeneratorEnum


class EmbeddingsRuleModel(BaseModel):
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: Optional[str] = Field(None, alias="TenantGUID")
    bucket_guid: Optional[str] = Field(None, alias="BucketGUID")
    owner_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="OwnerGUID"
    )
    name: Optional[str] = Field(None, alias="Name")
    content_type: str = Field(default="text/plain", alias="ContentType")
    prefix: Optional[str] = Field(None, alias="Prefix")
    suffix: Optional[str] = Field(None, alias="Suffix")
    graph_repository_guid: Optional[str] = Field(None, alias="GraphRepositoryGUID")
    vector_repository_guid: Optional[str] = Field(None, alias="VectorRepositoryGUID")
    processing_endpoint: str = Field(
        default="http://localhost:8000/v1.0/tenants/default/processing",
        alias="ProcessingEndpoint",
    )
    processing_access_key: str = Field(default="default", alias="ProcessingAccessKey")
    chunking_server_url: str = Field(
        default="http://localhost:8000/v1.0/tenants/default/chunking",
        alias="ChunkingServerUrl",
    )
    chunking_server_api_key: str = Field(
        default="default", alias="ChunkingServerApiKey"
    )
    tokenization_model: str = Field(
        default="sentence-transformers/all-MiniLM-L6-v2", alias="TokenizationModel"
    )

    hugging_face_api_key: str = Field(default="default", alias="HuggingFaceApiKey")

    max_chunking_tasks: int = Field(default=0, ge=1, alias="MaxChunkingTasks")

    min_chunk_content_length: int = Field(
        default=0, ge=1, alias="MinChunkContentLength"
    )

    max_chunk_content_length: int = Field(
        default=0, ge=1, alias="MaxChunkContentLength"
    )

    max_tokens_per_chunk: int = Field(default=0, ge=1, alias="MaxTokensPerChunk")

    token_overlap: int = Field(default=0, ge=1, alias="TokenOverlap")

    embedding_server_url: str = Field(
        default="http://localhost:8000/", alias="EmbeddingsServerUrl"
    )
    embedding_server_api_key: str = Field(
        default="default", alias="EmbeddingsServerApiKey"
    )

    embeddings_generator: EmbeddingsGeneratorEnum = Field(
        default=EmbeddingsGeneratorEnum.LCProxy, alias="EmbeddingsGenerator"
    )
    embeddings_generator_url: str = Field(
        default="http://localhost:8000/v1.0/tenants/default/embeddings",
        alias="EmbeddingsGeneratorUrl",
    )
    embeddings_generator_api_key: str = Field(
        default="default", alias="EmbeddingsGeneratorApiKey"
    )
    embeddings_batch_size: int = Field(default=16, ge=1, alias="EmbeddingsBatchSize")
    max_embeddings_tasks: int = Field(default=16, ge=1, alias="MaxEmbeddingsTasks")
    max_embeddings_retries: int = Field(default=3, ge=1, alias="MaxEmbeddingsRetries")
    max_embeddings_failures: int = Field(default=3, ge=1, alias="MaxEmbeddingsFailures")
    vector_store_url: str = Field(
        default="http://localhost:8000/", alias="VectorStoreUrl"
    )
    vector_store_access_key: str = Field(
        default="default", alias="VectorStoreAccessKey"
    )
    max_content_length: int = Field(
        default=16 * 1024 * 1024, ge=1, alias="MaxContentLength"
    )
    retention_minutes: Optional[int] = Field(None, ge=1, alias="RetentionMinutes")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)

    @field_validator("max_chunk_content_length")
    @classmethod
    def validate_max_chunk_content_length(cls, v):
        if v < 256 or v > 16384:
            raise ValueError("MaxChunkContentLength must be between 256 and 16384.")
        return v
