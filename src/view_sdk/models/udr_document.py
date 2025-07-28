import uuid
from collections import Counter
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..enums.document_type_enum import DocumentTypeEnum
from .api_error_response import ApiErrorResponseModel
from .posting import PostingModel
from .schema_result import SchemaResultModel
from .semantic_cell import SemanticCellModel
from .timestamp import TimestampModel


class UdrDocumentModel(BaseModel):
    """UDR document."""

    guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="GUID", description="GUID"
    )
    success: bool = Field(
        default=False,
        alias="Success",
        description="Indicates if the parser was successful",
    )
    timestamp: TimestampModel = Field(
        default_factory=TimestampModel,
        alias="Timestamp",
        description="Start and end timestamps",
    )
    error: Optional[ApiErrorResponseModel] = Field(
        None, alias="Error", description="Error response, if any"
    )
    additional_data: Optional[str] = Field(
        None,
        alias="AdditionalData",
        description="Additional data, not used by the service",
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        alias="Metadata",
        description="Metadata, attached to the result",
    )
    key: Optional[str] = Field(None, alias="Key", description="Key")
    type: DocumentTypeEnum = Field(alias="Type", description="Document type")
    terms: List[str] = Field(
        default_factory=list,
        alias="Terms",
        description="Terms identified through text extraction",
    )
    schema_: Optional[SchemaResultModel] = Field(
        None, alias="Schema", description="Schema"
    )
    postings: List[PostingModel] = Field(
        default_factory=list, alias="Postings", description="Postings"
    )
    semantic_cells: List[SemanticCellModel] = Field(
        default_factory=list, alias="SemanticCells", description="Semantic cells"
    )

    model_config = ConfigDict(
        use_enum_values=True, populate_by_name=True, validate_assignment=True
    )

    @property
    def top_terms(self) -> Dict[str, int]:
        """Get top terms and their count."""
        return self.get_top_terms()

    def get_top_terms(self, count: int = 10) -> Dict[str, int]:
        """
        Retrieve top terms.

        Args:
            count: Number of top terms to retrieve.

        Returns:
            Dictionary containing terms and their counts.
        """
        if count < 1:
            raise ValueError("count must be greater than 0")

        # Filter out empty terms and count occurrences
        term_counts = Counter(term for term in self.terms if term)

        # Get top N terms
        return dict(term_counts.most_common(count))

    @field_validator("metadata", mode="before")
    def validate_metadata(cls, v: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """Ensure metadata is never None."""
        return v or {}

    @field_validator("terms", mode="before")
    def validate_terms(cls, v: Optional[List[str]]) -> List[str]:
        """Ensure terms is never None."""
        return v or []

    @field_validator("postings", mode="before")
    def validate_postings(cls, v: Optional[List[PostingModel]]) -> List[PostingModel]:
        """Ensure postings is never None."""
        return v or []

    @field_validator("semantic_cells", mode="before")
    def validate_semantic_cells(
        cls, v: Optional[List[SemanticCellModel]]
    ) -> List[SemanticCellModel]:
        """Ensure semantic_cells is never None."""
        return v or []
