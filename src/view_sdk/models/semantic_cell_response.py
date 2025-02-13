from datetime import datetime, timezone
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from .api_error_response import ApiErrorResponseModel
from .semantic_cell import SemanticCellModel


class SemanticCellResponse(BaseModel):
    """Semantic cell response model."""

    data_flow_request_guid: Optional[str] = Field(
        default=None, alias="DataFlowRequestGUID", description="Data flow request GUID"
    )

    success: bool = Field(
        default=True, alias="Success", description="Boolean indicating success"
    )

    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        alias="Timestamp",
        description="Timestamp",
    )

    error: Optional[ApiErrorResponseModel] = Field(
        default=None, alias="Error", description="Error response, if any"
    )

    semantic_cells: Optional[List[SemanticCellModel]] = Field(
        default=None, alias="SemanticCells", description="Semantic cells"
    )

    data_: Optional[bytes] = Field(
        default=None, alias="Data", description="Additional data, if requested"
    )

    @field_validator("semantic_cells", mode="before")
    def validate_semantic_cells(
        cls, v: Optional[List[SemanticCellModel]]
    ) -> Optional[List[SemanticCellModel]]:
        """Ensure semantic_cells is never None when accessed."""
        return v or []

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
