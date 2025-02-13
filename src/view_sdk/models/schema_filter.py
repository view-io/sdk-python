import decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..enums.schema_condition_enum import SchemaConditionEnum


class SchemaFilterModel(BaseModel):
    Property: str = Field(..., alias="Property")
    Condition: SchemaConditionEnum = Field(..., alias="Condition")
    Value: Optional[str] = Field(default=None, alias="Value")

    model_config = ConfigDict(populate_by_name=True)

    @field_validator("Property")
    def property_must_not_be_empty(cls, v):
        if not v:
            raise ValueError("Property must not be empty")
        return v

    @field_validator("Value")
    def value_must_be_valid_for_condition(cls, v, values):
        condition = values.get("Condition")
        if condition in {
            SchemaConditionEnum.GreaterThan,
            SchemaConditionEnum.GreaterThanOrEqualTo,
            SchemaConditionEnum.LessThan,
            SchemaConditionEnum.LessThanOrEqualTo,
        }:
            if v is None:
                raise ValueError("Value must not be empty for the specified condition")
            try:
                decimal.Decimal(v)
            except decimal.InvalidOperation as e:
                raise ValueError(
                    "Value must be convertible to decimal for the specified condition"
                ) from e
        return v
