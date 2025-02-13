from enum import Enum


class PdfModeEnum(str, Enum):
    """PDF processing mode."""

    FLAT_TEXT_EXTRACTION = "FlatTextExtraction"
    BOUNDING_BOX_EXTRACTION = "BoundingBoxExtraction"
