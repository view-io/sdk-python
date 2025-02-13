import uuid
from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..enums.database_type_enum import DatabaseTypeEnum


class UdrDataTableRequest(BaseModel):
    """UDR data table processing request."""

    guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="GUID", description="GUID"
    )

    database_type: DatabaseTypeEnum = Field(
        default=DatabaseTypeEnum.SQLITE,
        alias="DatabaseType",
        description="Database type",
    )

    hostname: Optional[str] = Field(
        default=None, alias="Hostname", description="Hostname"
    )

    port: int = Field(default=0, alias="Port", description="Port", ge=0, le=65535)

    username: Optional[str] = Field(
        default=None, alias="Username", description="Username"
    )

    password: Optional[str] = Field(
        default=None, alias="Password", description="Password"
    )

    database_name: Optional[str] = Field(
        default=None, alias="DatabaseName", description="Database name"
    )

    query: Optional[str] = Field(default=None, alias="Query", description="Query")

    include_flattened: bool = Field(
        default=True,
        alias="IncludeFlattened",
        description="True to include a flattened representation of the source document",
    )

    case_insensitive: bool = Field(
        default=True,
        alias="CaseInsensitive",
        description="True to enable case insensitive processing",
    )

    top_terms: int = Field(
        default=10, alias="TopTerms", description="Number of top terms to include", ge=0
    )

    additional_data: Optional[str] = Field(
        default=None,
        alias="AdditionalData",
        description="Additional data, not used by the service",
    )

    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        alias="Metadata",
        description="Metadata, attached to the result",
    )

    sqlite_file_data: bytes = Field(
        default=b"", alias="SqliteFileData", description="Sqlite file data"
    )

    model_config = ConfigDict(
        populate_by_name=True, use_enum_values=True, validate_assignment=True
    )

    @field_validator("database_type")
    def validate_database_type(cls, v: str) -> str:
        if not v:
            raise ValueError("DatabaseType cannot be empty")
        return v
