from typing import Optional
import uuid
from datetime import datetime, timezone
from pydantic import BaseModel, ConfigDict, Field


class CrawlFilterModel(BaseModel):
    id: int = Field(default=0, exclude=True, alias="Id")
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    suffix: Optional[str] = Field(default=None, alias="Suffix")
    name: str = Field(..., alias="Name")
    minimum_size: int = Field(default=1, ge=1, alias="MinimumSize")
    maximum_size: int = Field(default=134217728, le=134217728, alias="MaximumSize")
    include_subdirectories: bool = Field(default=True, alias="IncludeSubdirectories")
    content_type: str = Field(default="*", alias="ContentType")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(populate_by_name=True)
