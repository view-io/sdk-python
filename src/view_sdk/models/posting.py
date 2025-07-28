from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, computed_field, field_validator


class PostingModel(BaseModel):
    """A posting from a parsed document."""

    term: str = Field(
        ...,  # Required field
        alias="Term",
        description="The token",
    )
    absolute_positions: List[int] = Field(
        default_factory=list,
        alias="AbsolutePositions",
        description="The absolute positions in the token list where the token appears",
    )
    relative_positions: List[int] = Field(
        default_factory=list,
        alias="RelativePositions",
        description="The relative positions in the token list where the token appears",
    )

    model_config = ConfigDict(
        use_enum_values=True,
        populate_by_name=True,
        validate_assignment=True,
        json_schema_extra={
            "properties": {
                "Term": {"order": 1},
                "Count": {"order": 2},
                "AbsolutePositions": {"order": 3},
                "RelativePositions": {"order": 4},
            }
        },
    )

    @computed_field
    def count(self) -> int:
        """The frequency with which the token occurs."""
        return len(self.absolute_positions) + len(self.relative_positions)

    def __init__(self, term: Optional[str] = None, **data):
        """
        Initialize Posting with optional term.

        Args:
            term: The token
        """
        if term is not None and not term.strip():
            raise ValueError("term must not be empty when provided")
        super().__init__(term=term, **data)

    @field_validator("absolute_positions", "relative_positions", mode="before")
    def validate_positions(cls, v: Optional[List[int]]) -> List[int]:
        """Ensure position lists are never None."""
        return v or []
