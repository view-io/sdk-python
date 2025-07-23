import uuid
from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enums.document_type_enum import DocumentTypeEnum
from .metadata_rule import MetadataRuleModel


class UdrDocumentRequest(BaseModel):
    """UDR document request model."""

    guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="GUID", description="GUID"
    )

    type_: DocumentTypeEnum = Field(
        default=DocumentTypeEnum.Unknown, alias="Type", description="Document type"
    )

    key: Optional[str] = Field(default=None, alias="Key", description="Key")

    content_type: Optional[str] = Field(
        default=None, alias="ContentType", description="Content-type"
    )

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

    data: bytes = Field(default=b"", alias="Data", description="Data")

    metadata_rule: Optional[MetadataRuleModel] = Field(
        default=None, alias="MetadataRule", description="Metadata rule"
    )

    model_config = ConfigDict(
        populate_by_name=True, use_enum_values=True, validate_assignment=True
    )

