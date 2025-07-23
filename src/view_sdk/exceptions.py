from .enums.api_error_enum import ERROR_DESCRIPTIONS, ApiErrorEnum


class SdkException(Exception):
    """Base class for all SDK exceptions."""


class AuthenticationError(SdkException):
    """Raised when authentication fails."""


class AuthorizationError(SdkException):
    """Raised when authorization fails."""


class BadRequestError(SdkException):
    """Raised when the request is malformed."""


class ResourceNotFoundError(SdkException):
    """Raised when the requested resource is not found."""


class ServerError(SdkException):
    """Raised when the server encounters an error."""


class TimeoutError(SdkException):
    """Raised when the request times out."""


class ConflictError(SdkException):
    """Raised when a conflict occurs, such as resource already existing."""


class InactiveError(SdkException):
    """Raised when the resource or account is inactive."""


class InvalidRangeError(SdkException):
    """Raised when an invalid range is supplied."""


class InUseError(SdkException):
    """Raised when the resource is in use."""


class NotEmptyError(SdkException):
    """Raised when the resource is not empty."""


class DeserializationError(SdkException):
    """Raised when there is an error in deserialization."""


class NoConnectivityError(SdkException):
    """Raised when there is no connectivity to a required service."""


class OperationFailedError(SdkException):
    """Raised when an operation against a service fails."""


class UnknownTypeError(SdkException):
    """Raised when an unknown type is detected or encountered."""


def get_exception_for_error_code(
    error_code: ApiErrorEnum | None,
    verbose: bool = False,
    original_exception: Exception = None,
) -> SdkException:
    """
    Maps API error codes to specific exception types with optional verbosity for tracebacks.

    Args:
        error_code: The API error code to map to an exception.
        verbose: Whether to include the original exception traceback.
        original_exception: The original exception, if any, to include based on verbosity.

    Returns:
        An instance of the appropriate exception type.

    Raises:
        SdkException: With appropriate error message for invalid error codes.
    """
    # Handle invalid error code types
    if not isinstance(error_code, ApiErrorEnum):
        error_message = (
            f"Invalid error code type - {error_code}"
            if error_code is not None and error_code != ""
            else "Invalid error code type"
        )
        exception_instance = SdkException(error_message)
        if verbose and original_exception:
            raise exception_instance from original_exception
        raise exception_instance from None

    error_mapping = {
        ApiErrorEnum.authentication_failed: AuthenticationError,
        ApiErrorEnum.authorization_failed: AuthorizationError,
        ApiErrorEnum.bad_request: BadRequestError,
        ApiErrorEnum.not_found: ResourceNotFoundError,
        ApiErrorEnum.internal_error: ServerError,
        ApiErrorEnum.too_large: BadRequestError,
        ApiErrorEnum.conflict: ConflictError,
        ApiErrorEnum.inactive: InactiveError,
        ApiErrorEnum.invalid_range: InvalidRangeError,
        ApiErrorEnum.in_use: InUseError,
        ApiErrorEnum.not_empty: NotEmptyError,
        ApiErrorEnum.deserialization_error: DeserializationError,
        ApiErrorEnum.no_type_detector_connectivity: NoConnectivityError,
        ApiErrorEnum.unknown_type_detected: UnknownTypeError,
        ApiErrorEnum.no_graph_connectivity: NoConnectivityError,
        ApiErrorEnum.graph_operation_failed: OperationFailedError,
        ApiErrorEnum.no_udr_connectivity: NoConnectivityError,
        ApiErrorEnum.udr_generation_failed: OperationFailedError,
        ApiErrorEnum.no_semantic_cell_connectivity: NoConnectivityError,
        ApiErrorEnum.semantic_cell_extraction_failed: OperationFailedError,
        ApiErrorEnum.no_data_catalog_connectivity: NoConnectivityError,
        ApiErrorEnum.data_catalog_persist_failed: OperationFailedError,
        ApiErrorEnum.unknown_data_catalog_type: UnknownTypeError,
        ApiErrorEnum.unknown_embeddings_generator_type: UnknownTypeError,
        ApiErrorEnum.embeddings_generation_failed: OperationFailedError,
        ApiErrorEnum.embeddings_persist_failed: OperationFailedError,
        ApiErrorEnum.no_object_metadata: BadRequestError,
        ApiErrorEnum.no_object_data: BadRequestError,
        ApiErrorEnum.no_metadata_rule: BadRequestError,
        ApiErrorEnum.required_properties_missing: BadRequestError,
    }

    # Get the exception class from the mapping, default to SdkException if not found
    exception_class = error_mapping.get(error_code, SdkException)

    # Get the error description from the ERROR_DESCRIPTIONS mapping
    error_description = ERROR_DESCRIPTIONS.get(error_code, "An unknown error occurred.")

    # Instantiate the exception with the description
    exception_instance = exception_class(error_description)

    # Conditionally attach original exception traceback based on verbosity
    if verbose and original_exception:
        raise exception_instance from original_exception  # Includes full traceback
    else:
        raise exception_instance from None
