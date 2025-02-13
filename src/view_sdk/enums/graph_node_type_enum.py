from enum import Enum


class GraphNodeTypeEnum(str, Enum):
    """Graph node type."""

    Unknown = "Unknown"
    Tenant = "Tenant"
    StoragePool = "StoragePool"
    Bucket = "Bucket"
    Object = "Object"
    Collection = "Collection"
    SourceDocument = "SourceDocument"
    VectorRepository = "VectorRepository"
    SemanticCell = "SemanticCell"
    SemanticChunk = "SemanticChunk"
    DataRepository = "DataRepository"
