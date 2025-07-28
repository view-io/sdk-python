from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from .schema_filter import SchemaFilterModel


class QueryFilterModel(BaseModel):
    CreatedAfter: Optional[datetime] = Field(default=None, alias="CreatedAfter")
    CreatedBefore: Optional[datetime] = Field(default=None, alias="CreatedBefore")
    Terms: List[str] = Field(default_factory=list, alias="Terms")
    MimeTypes: List[str] = Field(default_factory=list, alias="MimeTypes")
    Prefixes: List[str] = Field(default_factory=list, alias="Prefixes")
    Suffixes: List[str] = Field(default_factory=list, alias="Suffixes")
    SchemaFilters: List[SchemaFilterModel] = Field(
        default_factory=list, alias="SchemaFilters"
    )

    model_config = ConfigDict(populate_by_name=True)
