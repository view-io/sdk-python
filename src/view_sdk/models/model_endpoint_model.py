from pydantic import BaseModel, ConfigDict, Field, field_validator
import uuid
from datetime import datetime, timezone
from typing import Optional
from ..enums.model_api_type_enum import ModelApiTypeEnum


class ModelEndpointModel(BaseModel):
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    name: str = Field(default="My model endpoint", alias="Name")
    endpoint_url: str = Field(default="http://localhost:11434/", alias="EndpointUrl")
    bearer_token: Optional[str] = Field(default=None, alias="BearerToken")
    api_type: ModelApiTypeEnum = Field(default=ModelApiTypeEnum.Ollama, alias="ApiType")
    timeout_ms: int = Field(default=30000, alias="TimeoutMs")
    additional_data: Optional[str] = Field(default=None, alias="AdditionalData")
    active: bool = Field(default=True, alias="Active")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(populate_by_name=True)

    @classmethod
    def normalize_url(cls, v: str) -> str:
        if v:
            v = v.replace("\\", "/")
            if not v.endswith("/"):
                v += "/"
        return v

    @field_validator("timeout_ms")
    def validate_timeout(cls, v: int) -> int:
        if v <= 1000:
            raise ValueError("TimeoutMs must be greater than 1000")
        return v
