from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..enums.document_type_enum import DocumentTypeEnum
from .metadata_rule import MetadataRuleModel
from .pdf_options import PdfOptionsModel


class SemanticCellRequest(BaseModel):
    """Semantic cell request model."""

    document_type: DocumentTypeEnum = Field(
        default=DocumentTypeEnum.Unknown,
        alias="DocumentType",
        description="Document type",
    )

    min_chunk_content_length: int = Field(
        default=2,
        alias="MinChunkContentLength",
        description="Minimum chunk content length. Minimum is 1",
        ge=1,
    )

    max_chunk_content_length: int = Field(
        default=512,
        alias="MaxChunkContentLength",
        description="Maximum chunk content length. Minimum is 256 and maximum is 16384",
        ge=256,
        le=16384,
    )

    shift_size: int = Field(
        default=512,
        alias="ShiftSize",
        description="Shift size, used to determine overlap amongst neighboring chunks",
    )

    pdf: Optional[PdfOptionsModel] = Field(
        default=PdfOptionsModel(), alias="Pdf", description="PDF options"
    )

    metadata_rule: Optional[MetadataRuleModel] = Field(
        default=None, alias="MetadataRule", description="Metadata rule"
    )

    data_: Optional[bytes] = Field(
        default=None, alias="Data", description="Binary data to process"
    )

    model_config = ConfigDict(
        populate_by_name=True, use_enum_values=True, validate_assignment=True
    )

    @field_validator("shift_size")
    def validate_shift_size(cls, v: int, values) -> int:
        max_length = values.data.get("max_chunk_content_length", 512)
        if v > max_length:
            raise ValueError(
                "ShiftSize must be equal to or less than MaxChunkContentLength"
            )
        return v

    @field_validator("pdf")
    def validate_pdf(cls, v: Optional[PdfOptionsModel]) -> PdfOptionsModel:
        return PdfOptionsModel() if v is None else v
