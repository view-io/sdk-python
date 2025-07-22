import pytest
import httpx
from unittest.mock import Mock, patch
from view_sdk.base import BaseClient
from view_sdk.exceptions import SdkException, BadRequestError


@pytest.fixture
def base_client():
    return BaseClient(
        base_url="https://api.example.com",
        access_key="test-key",
        tenant_guid="test-tenant",
        timeout=10,
        retries=3,
    )


def test_init():
    client = BaseClient(
        base_url="https://api.example.com",
        access_key="test-key",
        tenant_guid="test-tenant",
    )
    assert client.base_url == "https://api.example.com"
    assert client.access_key == "test-key"
    assert client.tenant_guid == "test-tenant"
    assert client.timeout == 10  # default value
    assert client.retries == 3  # default value


def test_get_headers(base_client):
    headers = base_client._get_headers()
    assert headers["Authorization"] == "Bearer test-key"
    assert headers["Content-Type"] == "application/json"


# @pytest.mark.asyncio
def test_request_success(base_client):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = b'{"data": "test"}'
    mock_response.json.return_value = {"data": "test"}

    with patch.object(httpx.Client, "request", return_value=mock_response):
        result = base_client.request("GET", "/test")
        assert result == {"data": "test"}


# @pytest.mark.asyncio
def test_request_retry_success(base_client):
    mock_success = Mock()
    mock_success.status_code = 200
    mock_success.content = b'{"data": "test"}'
    mock_success.json.return_value = {"data": "test"}

    mock_error = Mock()
    mock_error.raise_for_status.side_effect = httpx.RequestError("Connection error")

    with patch.object(httpx.Client, "request") as mock_request:
        mock_request.side_effect = [mock_error, mock_success]
        result = base_client.request("GET", "/test")
        assert result == {"data": "test"}
        assert mock_request.call_count == 2


# @pytest.mark.asyncio
def test_request_http_error(base_client):
    """Test handling of HTTP error with proper error response structure"""
    error_response = {
        "Error": "BadRequest",
        "Description": "We were unable to discern your request. Please check your URL, query, and request body.",
        "Context": None,
    }

    mock_response = Mock(spec=httpx.Response)
    mock_response.status_code = 400
    mock_response.json.return_value = error_response
    mock_response.content = b'{"Error": "BadRequest", "Description": "We were unable to discern your request. Please check your URL, query, and request body.", "Context": null}'
    mock_response.headers = {"Content-Type": "application/json"}

    mock_error = httpx.HTTPStatusError(
        "400 Bad Request", request=Mock(), response=mock_response
    )

    with patch.object(httpx.Client, "request") as mock_request:
        mock_request.side_effect = mock_error
        with pytest.raises(BadRequestError) as exc_info:
            base_client.request("GET", "/test")

        assert (
            str(exc_info.value)
            == "We were unable to discern your request. Please check your URL, query, and request body."
        )


# @pytest.mark.asyncio
def test_request_max_retries_exceeded(base_client):
    """Test handling of max retries with proper error message"""
    mock_error = httpx.RequestError("Connection error")

    with patch.object(httpx.Client, "request") as mock_request:
        mock_request.side_effect = [
            mock_error
        ] * 3  # Ensure consistent error for all attempts
        with pytest.raises(SdkException) as exc_info:
            base_client.request("GET", "/test")

        assert "Request failed after 3 attempts:" in str(exc_info.value)
        assert mock_request.call_count == 3  # Verify retry count


def test_close(base_client):
    with patch.object(httpx.Client, "close") as mock_close:
        base_client.close()
        mock_close.assert_called_once()


def test_request_non_json_error_response(base_client):
    """Test handling of non-JSON error response"""
    mock_response = Mock(spec=httpx.Response)
    mock_response.status_code = 500
    mock_response.content = b"Internal Server Error"
    mock_response.headers = {"Content-Type": "text/plain"}

    mock_error = httpx.HTTPStatusError(
        "500 Internal Server Error", request=Mock(), response=mock_response
    )

    with patch.object(httpx.Client, "request") as mock_request:
        mock_request.side_effect = mock_error
        with pytest.raises(SdkException):
            base_client.request("GET", "/test")


def test_request_invalid_json_error_response(base_client):
    """Test handling of invalid JSON error response"""
    mock_response = Mock(spec=httpx.Response)
    mock_response.status_code = 500
    mock_response.json.side_effect = ValueError("Invalid JSON")
    mock_response.content = b'{"invalid": json'
    mock_response.headers = {"Content-Type": "application/json"}

    mock_error = httpx.HTTPStatusError(
        "500 Internal Server Error", request=Mock(), response=mock_response
    )

    with patch.object(httpx.Client, "request") as mock_request:
        mock_request.side_effect = mock_error
        with pytest.raises(SdkException):
            base_client.request("GET", "/test")


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (b'data: {"message": "test"}\n\n', {"message": "test"}),
        (b"data: invalid json\n\n", "invalid json\n\n"),
        (b"\n", None),  # Empty line case
    ],
)
def test_sse_request_success(base_client, test_input, expected):
    """Test SSE request with different response formats"""
    mock_response = Mock(spec=httpx.Response)
    mock_response.iter_lines.return_value = [test_input]
    mock_response.headers = {"Content-Type": "text/event-stream"}

    with (
        patch.object(httpx.Client, "build_request") as mock_build_request,
        patch.object(httpx.Client, "send", return_value=mock_response),
    ):
        events = list(base_client.sse_request("GET", "/test"))

        if expected is None:
            assert len(events) == 0
        else:
            assert len(events) == 1
            assert events[0] == expected


def test_sse_request_http_error(base_client):
    """Test SSE request with HTTP error"""
    error_response = {
        "Error": "BadRequest",
        "Description": "Invalid request",
        "Context": None,
    }

    mock_response = Mock(spec=httpx.Response)
    mock_response.status_code = 400
    mock_response.json.return_value = error_response
    mock_response.headers = {"Content-Type": "application/json"}
    mock_response.read = Mock()  # Add read method

    mock_error = httpx.HTTPStatusError(
        "400 Bad Request", request=Mock(), response=mock_response
    )

    with (
        patch.object(httpx.Client, "build_request"),
        patch.object(httpx.Client, "send") as mock_send,
    ):
        mock_send.side_effect = mock_error

        with pytest.raises(BadRequestError):
            list(base_client.sse_request("GET", "/test"))


def test_sse_request_connection_error(base_client):
    """Test SSE request with connection error"""
    mock_error = httpx.RequestError("Connection failed")

    with (
        patch.object(httpx.Client, "build_request"),
        patch.object(httpx.Client, "send") as mock_send,
    ):
        mock_send.side_effect = mock_error

        with pytest.raises(SdkException):
            list(base_client.sse_request("GET", "/test"))
