from enum import Enum


class BucketCategoryEnum(str, Enum):
    Data = "Data"
    Metadata = "Metadata"
    Embeddings = "Embeddings"
