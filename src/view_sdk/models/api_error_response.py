from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enums.api_error_enum import ApiErrorEnum


class ApiErrorResponseModel(BaseModel):
    error: ApiErrorEnum = Field(alias="Error")
    context: Optional[str] = Field(default=None, alias="Context")
    description: Optional[str] = Field(default=None, alias="Description")

    model_config = ConfigDict(populate_by_name=True)
