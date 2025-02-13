import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

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
    batch_size: int = Field(default=16, ge=1, alias="BatchSize")
    max_generator_tasks: int = Field(default=16, ge=1, alias="MaxGeneratorTasks")
    max_retries: int = Field(default=3, ge=1, alias="MaxRetries")
    max_failures: int = Field(default=3, ge=1, alias="MaxFailures")
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
