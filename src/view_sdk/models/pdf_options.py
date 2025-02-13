from pydantic import BaseModel, ConfigDict, Field

from ..enums.pdf_mode_enum import PdfModeEnum


class PdfOptionsModel(BaseModel):
    """PDF processing options model."""

    mode: PdfModeEnum = Field(
        default=PdfModeEnum.BOUNDING_BOX_EXTRACTION,
        alias="Mode",
        description="PDF processing mode",
    )

    return_markup: bool = Field(
        default=False,
        alias="ReturnMarkup",
        description="True to indicate that the marked-up PDF including bounding boxes should be returned. "
        "Only applicable when Mode is set to BoundingBoxExtraction",
    )

    retain_artifact: bool = Field(
        default=False,
        alias="RetainArtifact",
        description="True to indicate that the marked-up PDF file should be preserved in the temporary directory. "
        "Only applicable when Mode is set to BoundingBoxExtraction",
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
