import pytest
import json
from unittest.mock import Mock
from viewio_sdk.api.configuration_api import ConfigurationApi
from viewio_sdk.rest import RESTResponse

@pytest.fixture
def guid():
    return "default"

@pytest.fixture
def config_api():
    """Fixture to return a mocked ConfigurationApi instance."""
    return ConfigurationApi()


def _get_success_mock_response(
    status=200,
    reason="OK",
    data=None,
    headers=None,
    content_type="application/json; charset=utf-8",
):
    mock_response = Mock(spec=RESTResponse)
    mock_response.status = status
    mock_response.reason = reason
    mock_response.data = data or b"{}"
    mock_response.getheader.return_value = content_type
    mock_response.getheaders.return_value = headers or {"Content-Type": content_type}
    mock_response.response = mock_response
    return mock_response


def _get_failure_mock_response(expected_status, error_code):
    # Mock the ApiException
    mock_response = Mock(spec=RESTResponse)
    mock_response.status = expected_status
    mock_response.reason = error_code.name
    mock_response.data = json.dumps(
        {
            "Error": error_code.value,
            "Message": "Dummy message",
            "StatusCode": expected_status,
        }
    ).encode(
        "utf-8"
    )  # Mocked error message in bytes
    mock_response.getheaders.return_value = mock_response
    mock_response.response = mock_response
    return mock_response
