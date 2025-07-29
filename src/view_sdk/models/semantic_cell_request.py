from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enums.document_type_enum import DocumentTypeEnum


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

    data_: Optional[bytes] = Field(
        default=None, alias="Data", description="Binary data to process"
    )

    model_config = ConfigDict(
        populate_by_name=True, use_enum_values=True, validate_assignment=True
    )
