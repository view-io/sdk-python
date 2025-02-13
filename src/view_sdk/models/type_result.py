from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ..enums.document_type_enum import DocumentTypeEnum


class TypeResultModel(BaseModel):
    """Type detection results."""

    mime_type: Optional[str] = Field(
        default=None, alias="MimeType", description="MIME type"
    )

    extension: Optional[str] = Field(
        default=None, alias="Extension", description="Extension"
    )

    type_: DocumentTypeEnum = Field(
        default=DocumentTypeEnum.Unknown, alias="Type", description="Data type"
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
