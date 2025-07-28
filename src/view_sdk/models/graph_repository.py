import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enums.graph_repository_type_enum import GraphRepositoryTypeEnum


class GraphRepositoryModel(BaseModel):
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    name: str = Field(default="My vector repository", alias="Name")
    repository_type: GraphRepositoryTypeEnum = Field(
        default=GraphRepositoryTypeEnum.LiteGraph, alias="RepositoryType"
    )
    endpoint_url: Optional[str] = Field(None, alias="EndpointUrl")
    api_key: Optional[str] = Field(None, alias="ApiKey")
    username: Optional[str] = Field(None, alias="Username")
    password: Optional[str] = Field(None, alias="Password")
    hostname: Optional[str] = Field(None, alias="Hostname")
    port: int = Field(default=0, ge=0, le=65535, alias="Port")
    ssl: bool = Field(default=False, alias="Ssl")
    graph_identifier: Optional[str] = Field(None, alias="GraphIdentifier")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
