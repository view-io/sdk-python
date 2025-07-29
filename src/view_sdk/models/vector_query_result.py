from typing import Optional, Any
from pydantic import BaseModel, Field, ConfigDict, field_validator
from .timestamp import TimestampModel  # Adjust import if needed


class VectorQueryResultModel(BaseModel):
    success: bool = Field(default=False, alias="Success")
    timestamp: Optional[TimestampModel] = Field(
        default_factory=TimestampModel, alias="Timestamp"
    )
    status_code: int = Field(default=200, alias="StatusCode")
    query: Optional[str] = Field(default=None, alias="Query")
    result: Optional[Any] = Field(default=None, alias="Result")

    model_config = ConfigDict(populate_by_name=True)

    @field_validator("status_code")
    @classmethod
    def validate_status_code(cls, v):
        if v < 0 or v > 599:
            raise ValueError("StatusCode must be between 0 and 599.")
        return v
