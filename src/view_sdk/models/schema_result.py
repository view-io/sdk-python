from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..enums.data_type_enum import DataTypeEnum
from ..enums.document_type_enum import DocumentTypeEnum
from .data_node import DataNodeModel


class SchemaResultModel(BaseModel):
    """Schema result."""

    type: DocumentTypeEnum = Field(
        default=DocumentTypeEnum.Unknown, alias="Type", description="Data type"
    )
    rows: Optional[int] = Field(None, alias="Rows", description="Number of rows", ge=0)
    columns: Optional[int] = Field(
        None, alias="Columns", description="Number of columns", ge=0
    )
    irregular: Optional[bool] = Field(
        None,
        alias="Irregular",
        description="Flag to indicate if the geometry of the object is irregular",
    )
    max_depth: Optional[int] = Field(
        None, alias="MaxDepth", description="Maximum depth observed in the object", ge=0
    )
    num_objects: Optional[int] = Field(
        None, alias="NumObjects", description="Number of objects", ge=0
    )
    num_arrays: Optional[int] = Field(
        None, alias="NumArrays", description="Number of arrays", ge=0
    )
    num_key_values: Optional[int] = Field(
        None, alias="NumKeyValues", description="Number of key values", ge=0
    )
    schema_: Dict[str, DataTypeEnum] = Field(
        default_factory=dict, alias="Schema", description="Schema of the document"
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict, alias="Metadata", description="Metadata"
    )
    flattened: List[DataNodeModel] = Field(
        default_factory=list,
        alias="Flattened",
        description="Flattened representation of the object",
    )

    model_config = ConfigDict(
        use_enum_values=True,
        populate_by_name=True,
        validate_assignment=True,
        json_schema_extra={
            "properties": {
                "Schema": {"order": 10},
                "Metadata": {"order": 11},
                "Flattened": {"order": 12},
            }
        },
    )

    @field_validator("schema_", mode="before")
    def validate_schema(
        cls, v: Optional[Dict[str, DataTypeEnum]]
    ) -> Dict[str, DataTypeEnum]:
        """Ensure schema is never None."""
        return v or {}

    @field_validator("metadata", mode="before")
    def validate_metadata(cls, v: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """Ensure metadata is never None."""
        return v or {}

    @field_validator("flattened", mode="before")
    def validate_flattened(
        cls, v: Optional[List[DataNodeModel]]
    ) -> List[DataNodeModel]:
        """Ensure flattened is never None."""
        return v or []

    @field_validator(
        "rows",
        "columns",
        "max_depth",
        "num_objects",
        "num_arrays",
        "num_key_values",
        mode="before",
    )
    def validate_non_negative(cls, v: Optional[int], field: Field) -> Optional[int]:
        """Ensure numeric fields are non-negative when provided."""
        if v is not None and v < 0:
            raise ValueError(f"{field.alias} must be non-negative")
        return v
