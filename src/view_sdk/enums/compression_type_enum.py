from enum import Enum


class CompressionTypeEnum(str, Enum):
    # Using lower case "none" because it causes issues with python's Enum
    none = "None"
    Gzip = "Gzip"
    Deflate = "Deflate"
    Adaptive = "Adaptive"
