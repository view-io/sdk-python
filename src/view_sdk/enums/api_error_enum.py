from enum import Enum


class ApiErrorEnum(str, Enum):
    authentication_failed = "AuthenticationFailed"
    authorization_failed = "AuthorizationFailed"
    bad_request = "BadRequest"
    conflict = "Conflict"
    deserialization_error = "DeserializationError"
    inactive = "Inactive"
    internal_error = "InternalError"
    invalid_range = "InvalidRange"
    in_use = "InUse"
    not_empty = "NotEmpty"
    not_found = "NotFound"
    timeout = "Timeout"
    too_large = "TooLarge"
    no_type_detector_connectivity = "NoTypeDetectorConnectivity"
    unknown_type_detected = "UnknownTypeDetected"
    no_graph_connectivity = "NoGraphConnectivity"
    graph_operation_failed = "GraphOperationFailed"
    no_udr_connectivity = "NoUdrConnectivity"
    udr_generation_failed = "UdrGenerationFailed"
    no_semantic_cell_connectivity = "NoSemanticCellConnectivity"
    semantic_cell_extraction_failed = "SemanticCellExtractionFailed"
    no_data_catalog_connectivity = "NoDataCatalogConnectivity"
    data_catalog_persist_failed = "DataCatalogPersistFailed"
    unknown_data_catalog_type = "UnknownDataCatalogType"
    unknown_embeddings_generator_type = "UnknownEmbeddingsGeneratorType"
    embeddings_generation_failed = "EmbeddingsGenerationFailed"
    embeddings_persist_failed = "EmbeddingsPersistFailed"
    no_object_metadata = "NoObjectMetadata"
    no_object_data = "NoObjectData"
    no_metadata_rule = "NoMetadataRule"
    required_properties_missing = "RequiredPropertiesMissing"
    request_body_missing = "RequestBodyMissing"
    no_embeddings_connectivity = "NoEmbeddingsConnectivity"
    no_vector_connectivity = "NoVectorConnectivity"
    unknown_vector_repository_type = "UnknownVectorRepositoryType"
    vector_persist_failed = "VectorPersistFailed"
    token_expired = "TokenExpired"
    bad_gateway = "BadGateway"


ERROR_DESCRIPTIONS = {
    ApiErrorEnum.authentication_failed: "Your authentication material was not accepted.",
    ApiErrorEnum.authorization_failed: "Your authentication material was accepted, but you are not authorized to perform this request.",
    ApiErrorEnum.bad_request: "We were unable to discern your request. Please check your URL, query, and request body.",
    ApiErrorEnum.conflict: "Operation failed as it would create a conflict with an existing resource.",
    ApiErrorEnum.deserialization_error: "Your request body was invalid and could not be deserialized.",
    ApiErrorEnum.inactive: "Your account, credentials, or the requested resource are marked as inactive.",
    ApiErrorEnum.internal_error: "An internal error has been encountered.",
    ApiErrorEnum.invalid_range: "An invalid range has been supplied and cannot be fulfilled.",
    ApiErrorEnum.in_use: "The requested resource is in use.",
    ApiErrorEnum.not_empty: "The requested resource is not empty.",
    ApiErrorEnum.not_found: "The requested resource was not found.",
    ApiErrorEnum.timeout: "The request was not completed within the specified timeout interval.",
    ApiErrorEnum.too_large: "The size of your request exceeds the maximum allowed by this server.",
    ApiErrorEnum.no_type_detector_connectivity: "Unable to establish a connection to the type detector.",
    ApiErrorEnum.unknown_type_detected: "An unrecognizable data type was supplied.",
    ApiErrorEnum.no_graph_connectivity: "Unable to establish a connection to the graph repository.",
    ApiErrorEnum.graph_operation_failed: "An operation against the graph repository has failed.",
    ApiErrorEnum.no_udr_connectivity: "Unable to establish a connection to the UDR endpoint.",
    ApiErrorEnum.udr_generation_failed: "Unable to generate UDR document.",
    ApiErrorEnum.no_semantic_cell_connectivity: "Unable to establish a connection to the semantic cell extraction endpoint.",
    ApiErrorEnum.semantic_cell_extraction_failed: "Unable to extract semantic cells.",
    ApiErrorEnum.no_data_catalog_connectivity: "Unable to establish a connection to the data catalog endpoint.",
    ApiErrorEnum.data_catalog_persist_failed: "Unable to persist data within the data catalog.",
    ApiErrorEnum.unknown_data_catalog_type: "An unknown data catalog type was encountered.",
    ApiErrorEnum.unknown_embeddings_generator_type: "An unknown embeddings generator type was encountered.",
    ApiErrorEnum.embeddings_generation_failed: "Unable to generate embeddings.",
    ApiErrorEnum.embeddings_persist_failed: "Unable to persist embeddings within the vector store.",
    ApiErrorEnum.no_object_metadata: "No object metadata was supplied.",
    ApiErrorEnum.no_object_data: "No object data was supplied.",
    ApiErrorEnum.no_metadata_rule: "No metadata rule was supplied.",
    ApiErrorEnum.required_properties_missing: "A required property was missing from the request.",
    ApiErrorEnum.request_body_missing: "A request body is required for this operation.",
    ApiErrorEnum.no_embeddings_connectivity: "Unable to establish a connection to the embeddings generation endpoint.",
    ApiErrorEnum.no_vector_connectivity: "Unable to establish a connection to the vector repository.",
    ApiErrorEnum.unknown_vector_repository_type: "An unknown vector repository type was encountered.",
    ApiErrorEnum.vector_persist_failed: "Unable to persist embeddings within the vector store.",
    ApiErrorEnum.token_expired: "Your authentication token has expired.",
    ApiErrorEnum.bad_gateway: "Your request is unable to be serviced as there are no origin servers available.",
}
