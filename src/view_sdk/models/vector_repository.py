import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enums.vector_repository_type_enum import VectorRepositoryTypeEnum


class VectorRepositoryModel(BaseModel):
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    name: str = Field(default="My vector repository", alias="Name")
    repository_type: VectorRepositoryTypeEnum = Field(
        default=VectorRepositoryTypeEnum.Pgvector, alias="RepositoryType"
    )
    endpoint_url: Optional[str] = Field(None, alias="EndpointUrl")
    api_key: Optional[str] = Field(None, alias="ApiKey")
    model: str = Field(default="all-MiniLM-L6-v2", alias="Model")
    dimensionality: int = Field(default=384, ge=1, alias="Dimensionality")
    database_hostname: Optional[str] = Field(None, alias="DatabaseHostname")
    database_name: Optional[str] = Field(None, alias="DatabaseName")
    database_table: Optional[str] = Field(None, alias="DatabaseTable")
    database_port: int = Field(default=0, ge=0, le=65535, alias="DatabasePort")
    database_user: Optional[str] = Field(None, alias="DatabaseUser")
    database_password: Optional[str] = Field(None, alias="DatabasePassword")
    prompt_prefix: str = Field(
        default=(
            "Use the following pieces of context to answer the question at the end. "
            "Documents are sorted by similarity to the question. "
            "If the context is not enough for you to answer the question, "
            "politely explain that you don't have relevant context. "
            "Do not try to make up an answer."
        ),
        alias="PromptPrefix",
    )
    prompt_suffix: Optional[str] = Field(None, alias="PromptSuffix")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
