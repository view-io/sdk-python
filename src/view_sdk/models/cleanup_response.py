from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from .api_error_response import ApiErrorResponseModel
from .timestamp import TimestampModel


class CleanupResponse(BaseModel):
    """Cleanup response from processor."""

    guid: Optional[str] = Field(
        default=None, alias="GUID", description="Processor request GUID"
    )

    success: bool = Field(
        default=True, alias="Success", description="Boolean indicating success"
    )

    async_: bool = Field(
        default=True,
        alias="Async",
        description="Boolean indicating whether or not the task was executed asynchronously",
    )

    timestamp: TimestampModel = Field(
        default=TimestampModel(),
        alias="Timestamp",
        description="Timestamps",
    )

    error: Optional[ApiErrorResponseModel] = Field(
        default=None, alias="Error", description="Error response, if any"
    )

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
