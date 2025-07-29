from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enums.search_condition_enum import SearchCondition


class SearchFilterModel(BaseModel):
    field: str = Field(..., alias="Field")
    condition: SearchCondition = Field(
        default=SearchCondition.Equals, alias="Condition"
    )
    value: Optional[str] = Field(None, alias="Value")

    @classmethod
    def validate_value(
        cls, condition: SearchCondition, value: Optional[str]
    ) -> Optional[str]:
        if condition in {
            SearchCondition.GreaterThan,
            SearchCondition.GreaterThanOrEqualTo,
            SearchCondition.LessThan,
            SearchCondition.LessThanOrEqualTo,
        } and (value is None or not value.isdigit()):
            raise ValueError(
                "Value must be convertible to decimal when using comparison conditions."
            )
        return value

    model_config = ConfigDict(populate_by_name=True)
