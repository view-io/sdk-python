import uuid
from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class ModelProfileModel(BaseModel):
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    model_configuration_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="ModelConfigurationGUID"
    )
    model_endpoint_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="ModelEndpointGUID"
    )
    name: str = Field(default="My model profile", alias="Name")
    additional_data: Optional[str] = Field(default=None, alias="AdditionalData")
    active: bool = Field(default=True, alias="Active")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(populate_by_name=True)
