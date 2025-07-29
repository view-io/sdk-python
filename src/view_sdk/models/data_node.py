import contextlib
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..enums.data_type_enum import DataTypeEnum


class DataNodeModel(BaseModel):
    """A node of data from a parsed document."""

    key: Optional[str] = Field(None, alias="Key", description="The key")
    type_: DataTypeEnum = Field(
        default=DataTypeEnum.String,
        alias="Type",
        description="The DataType associated with the key-value pair",
    )
    data: Any = Field(
        None, alias="Data", description="The data associated with the key"
    )

    model_config = ConfigDict(
        use_enum_values=True,
        populate_by_name=True,
        validate_assignment=True,
        json_schema_extra={
            "properties": {
                "Key": {"order": 1},
                "Type": {"order": 2},
                "Data": {"order": 3},
            }
        },
    )

    @field_validator("key")
    def validate_key(cls, v: Optional[str]) -> str:
        """Validate that key is not empty when provided."""
        if v is not None and not v.strip():
            raise ValueError("Key must not be empty when provided")
        return v

    def __init__(
        self,
        key: Optional[str] = None,
        data: Any = None,
        type_: Optional[DataTypeEnum] = None,
        **kwargs,
    ):
        """
        Initialize DataNode with optional key, data, and type.

        Args:
            key: The key
            data: The data associated with the key
            type: The DataType associated with the key-value pair
        """
        if type_ is None:
            type_ = DataNodeModel.type_from_value(data)

        super().__init__(key=key, data=data, type_=type_, **kwargs)

    @staticmethod
    def type_from_value(val: Any) -> DataTypeEnum:
        """
        Retrieve the DataType of the supplied value.

        Args:
            val: The object to evaluate

        Returns:
            DataType
        """
        if val is None:
            return DataTypeEnum.Null

        # Convert to string for consistent handling
        val_str = str(val)

        # Check for decimal numbers
        if "." in val_str:
            with contextlib.suppress(ValueError):
                float(val_str)  # Use float instead of Decimal for simplicity
                return DataTypeEnum.Decimal
        # Check for integers
        with contextlib.suppress(ValueError):
            num = int(val_str)
            if -2147483648 <= num <= 2147483647:  # int32 range
                return DataTypeEnum.Integer
            return DataTypeEnum.Long
        # Check for booleans
        if val_str.lower() in {"true", "false"}:
            return DataTypeEnum.Boolean

        # Default to string
        return DataTypeEnum.String
