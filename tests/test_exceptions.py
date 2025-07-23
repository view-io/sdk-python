import pytest
import httpx
from unittest.mock import Mock

from view_sdk.exceptions import (
    get_exception_for_error_code,
    SdkException,
    AuthenticationError,
    AuthorizationError,
    BadRequestError,
    ResourceNotFoundError,
    ServerError,
)
from view_sdk.enums.api_error_enum import ApiErrorEnum, ERROR_DESCRIPTIONS


@pytest.mark.parametrize("error_code,expected_exception", [
    (ApiErrorEnum.authentication_failed, AuthenticationError),
    (ApiErrorEnum.authorization_failed, AuthorizationError),
    (ApiErrorEnum.bad_request, BadRequestError),
    (ApiErrorEnum.not_found, ResourceNotFoundError),
    (ApiErrorEnum.internal_error, ServerError),
])
def test_get_exception_for_error_code_basic_mapping(error_code, expected_exception):
    """Test basic error code to exception mapping without verbosity or original exception."""
    with pytest.raises(expected_exception) as exc_info:
        get_exception_for_error_code(error_code)
    assert str(exc_info.value) == ERROR_DESCRIPTIONS[error_code]


@pytest.mark.parametrize("verbose", [True, False])
def test_get_exception_for_error_code_with_original_exception(verbose):
    """Test exception mapping with original exception and verbosity."""
    original_error = ValueError("Original error")

    with pytest.raises(AuthenticationError) as exc_info:
        get_exception_for_error_code(
            ApiErrorEnum.authentication_failed,
            verbose=verbose,
            original_exception=original_error
        )

    if verbose:
        assert exc_info.value.__cause__ is original_error
    else:
        assert exc_info.value.__cause__ is None


@pytest.mark.parametrize("invalid_code,expected_message", [
    (None, "Invalid error code type"),
    ("InvalidError", "Invalid error code type - InvalidError"),
    (404, "Invalid error code type - 404"),
    ("", "Invalid error code type"),
])
def test_invalid_error_codes(invalid_code, expected_message):
    """Test handling of invalid error codes."""
    with pytest.raises(SdkException) as exc_info:
        get_exception_for_error_code(invalid_code)
    assert expected_message in str(exc_info.value)


@pytest.mark.parametrize("error_enum", list(ApiErrorEnum))
def test_all_error_enums(error_enum):
    """Test that all defined error enums have corresponding descriptions and can be mapped."""
    with pytest.raises(SdkException) as exc_info:
        get_exception_for_error_code(error_enum)
    assert str(exc_info.value) == ERROR_DESCRIPTIONS[error_enum]


def test_exception_with_httpx_error():
    """Test exception handling with httpx errors."""
    # Create a mock HTTP response
    mock_response = Mock(spec=httpx.Response)
    mock_response.status_code = 401

    # Create an HTTPStatusError
    http_error = httpx.HTTPStatusError(
        "401 Unauthorized",
        request=Mock(spec=httpx.Request),
        response=mock_response
    )

    with pytest.raises(AuthenticationError) as exc_info:
        get_exception_for_error_code(
            ApiErrorEnum.authentication_failed,
            verbose=True,
            original_exception=http_error
        )
    assert exc_info.value.__cause__ is http_error
    assert ERROR_DESCRIPTIONS[ApiErrorEnum.authentication_failed] in str(exc_info.value)
