from pydantic import BaseModel, ConfigDict, Field

from ..enums.enumeration_order_enum import EnumerationOrderEnum


class GraphSearchRequest(BaseModel):
    """Search request model for graph operations."""

    graph_guid: str = Field(
        default="00000000-0000-0000-0000-000000000000",
        alias="GraphGUID",
        description="Graph GUID",
    )

    ordering: EnumerationOrderEnum = Field(
        default=EnumerationOrderEnum.CreatedDescending,
        alias="Ordering",
        description="Ordering of results",
    )

    expression: dict | None = Field(
        default=None, alias="Expr", description="Search expression"
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
