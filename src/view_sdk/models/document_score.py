from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class DocumentScoreModel(BaseModel):
    """Document score."""

    score: Optional[Decimal] = Field(
        None,
        alias="Score",
        description="The score of the document, between 0 and 1, over both terms and filters. Only relevant when optional terms or filters are supplied in the search.",
        ge=0,
        le=1,
    )
    terms_score: Optional[Decimal] = Field(
        None,
        alias="TermsScore",
        description="The terms score of the document, between 0 and 1, when optional terms are supplied.",
        ge=0,
        le=1,
    )
    filters_score: Optional[Decimal] = Field(
        None,
        alias="FiltersScore",
        description="The filters score of the document, between 0 and 1, when optional filters are supplied.",
        ge=0,
        le=1,
    )

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
