from enum import Enum


class VectorSearchTypeEnum(Enum):
    InnerProduct = "InnerProduct"
    CosineDistance = "CosineDistance"
    L2Distance = "L2Distance"
