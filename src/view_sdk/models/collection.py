import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CollectionModel(BaseModel):
    id: int = Field(default=0, ge=1, alias="Id")
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    name: Optional[str] = Field(None, alias="Name")
    allow_overwrites: bool = Field(default=True, alias="AllowOverwrites")
    additional_data: Optional[str] = Field(None, alias="AdditionalData")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
