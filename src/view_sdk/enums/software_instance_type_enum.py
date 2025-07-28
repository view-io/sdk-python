from enum import Enum


# Define the SoftwareInstanceTypeEnum based on the C# enum
class SoftwareInstanceTypeEnum(str, Enum):
    config_server = "ConfigServer"
    data_connector_server = "DataConnectorServer"
    document_processor_server = "DocumentProcessorServer"
    processor_server = "ProcessorServer"
    lexi_server = "LexiServer"
    vector_server = "VectorServer"
    storage_server = "StorageServer"
    semantic_cell_extractor_server = "SemanticCellExtractorServer"
    director_server = "DirectorServer"
    embeddings_server = "EmbeddingsServer"
