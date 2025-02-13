import uuid
from datetime import datetime, timezone
from typing import ClassVar, List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..enums.http_method_enum import HttpMethodEnum  # This needs to be provided
from ..enums.trigger_type_enum import TriggerTypeEnum


class TriggerModel(BaseModel):
    """Data flow trigger, i.e. the event that invokes a data flow."""

    # Define reserved prefixes as a ClassVar
    _reserved_url_prefixes: ClassVar[List[str]] = ["/v1.0"]

    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    trigger_type: TriggerTypeEnum = Field(
        default=TriggerTypeEnum.HTTP, alias="TriggerType"
    )
    name: str = Field(default="My trigger", alias="Name")
    http_method: Optional[HttpMethodEnum] = Field(default=None, alias="HttpMethod")
    http_url_prefix: Optional[str] = Field(default=None, alias="HttpUrlPrefix")
    notes: Optional[str] = Field(default=None, alias="Notes")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)

    @field_validator("http_url_prefix")
    def validate_http_url_prefix(cls, v: Optional[str]) -> Optional[str]:
        if v:
            if not v.startswith("/"):
                v = f"/{v}"

            if v in cls._reserved_url_prefixes:
                raise ValueError(
                    "Supplied HttpUrlPrefix is reserved and cannot be used."
                )

        return v
