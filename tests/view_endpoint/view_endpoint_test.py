"""
    View.IO SDK

    This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

"""  # noqa: E501

import json
from unittest.mock import patch

from uuid import uuid4

import pytest
from viewio_sdk.models.api_error_enum import ApiErrorEnum
from viewio_sdk.models.view_endpoint import ViewEndpoint
from viewio_sdk.rest import ApiException
from ..conftest import _get_success_mock_response, _get_failure_mock_response


# Test for successful exists_view_endpoint using mocked API
def test_exists_view_endpoint_success(config_api, guid):
    view_endpoint_id = "test_view_endpoint_id"
    mock_response = _get_success_mock_response(status=200)
    # Mocked API call
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_view_endpoint:
        mock_view_endpoint.return_value = mock_response

        # Perform the exists_view_endpoint call
        exists = config_api.exists_view_endpoint(guid, view_endpoint_id)

        # Assert the result is as expected
        assert exists is True


# Test for exists_view_endpoint when the view_endpoint does not exist (mocked API)
@pytest.mark.parametrize("error_code", [404, 500])
def test_exists_view_endpoint_not_found(config_api, guid, error_code):
    # Mock the ApiException
    mock_response = _get_success_mock_response(status=error_code)

    view_endpoint_id = "invalid_view_endpoint_id"
    # Mocked API call that raises an exception when the view_endpoint is not found
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_view_endpoint:
        mock_view_endpoint.return_value = mock_response

        exists = config_api.exists_view_endpoint(guid, view_endpoint_id)

        # Assert the result is as expected
        assert exists is False


# Test for successful create view_endpoint using mocked API
def test_create_view_endpoint_success(config_api, guid):
    new_view_endpoint = ViewEndpoint(guid=str(uuid4()), name="Test ViewEndpoint")
    # Mock the RESTResponse
    mock_response = _get_success_mock_response(
        status=200, data=new_view_endpoint.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create:
        mock_create.return_value = mock_response

        view_endpoint = config_api.create_view_endpoint(guid, new_view_endpoint)

        assert view_endpoint == new_view_endpoint


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_create_view_endpoint_api_errors(config_api, guid, error_code, expected_status):
    mock_response = _get_failure_mock_response(expected_status, error_code)
    view_endpoint_data = {"GUID": str(uuid4()), "Name": "Test ViewEndpoint"}

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_view_endpoint:
        mock_create_view_endpoint.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.create_view_endpoint(
                guid, ViewEndpoint(**view_endpoint_data)
            )

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful delete view_endpoint by GUID using mocked API
def test_delete_view_endpoint_by_guid_success(config_api, guid):
    view_endpoint_guid = "guid1"
    new_view_endpoint = ViewEndpoint(guid=str(uuid4()), name="Test ViewEndpoint")
    mock_response = _get_success_mock_response(
        status=200, data=new_view_endpoint.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete:
        mock_delete.return_value = mock_response

        response = config_api.delete_view_endpoint(guid, view_endpoint_guid)

        assert response == new_view_endpoint


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_delete_view_endpoint_api_errors(config_api, guid, error_code, expected_status):
    view_endpoint_guid = "invalid-guid"
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete_view_endpoint:
        mock_delete_view_endpoint.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.delete_view_endpoint(guid, view_endpoint_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve all view endpoints using mocked API
def test_retrieve_view_endpoints_success(config_api, guid):
    view_endpoints = [
        ViewEndpoint(guid=str(uuid4()), name="View Endpoint 1"),
        ViewEndpoint(guid=str(uuid4()), name="View Endpoint 2"),
    ]
    # Convert the list of ViewEndpoint objects to JSON
    view_endpoints_json = [view_endpoint.to_dict() for view_endpoint in view_endpoints]
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(view_endpoints_json).encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_view_endpoints(guid)

        assert response == view_endpoints


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_view_endpoints_api_errors(config_api, guid, error_code, expected_status):
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_view_endpoints(guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve view endpoint using mocked API
def test_retrieve_view_endpoint_success(config_api, guid):
    endpoint = ViewEndpoint(guid=str(uuid4()), name="Test View Endpoint")
    mock_response = _get_success_mock_response(
        status=200, data=endpoint.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_view_endpoint(guid, endpoint.guid)

        assert response == endpoint


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_view_endpoint_api_errors(config_api, guid, error_code, expected_status):
    endpoint_guid = str(uuid4())
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve_endpoint:
        mock_retrieve_endpoint.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_view_endpoint(guid, endpoint_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful update view_endpoint using mocked API
def test_update_view_endpoint_success(config_api, guid):
    view_endpoint = ViewEndpoint(guid=str(uuid4()), name="Updated ViewEndpoint")
    mock_response = _get_success_mock_response(
        status=200, data=view_endpoint.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update:
        mock_update.return_value = mock_response

        response = config_api.update_view_endpoint(
            guid, view_endpoint.guid, view_endpoint
        )

        assert response == view_endpoint


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_update_view_endpoint_api_errors(config_api, guid, error_code, expected_status):
    view_endpoint_data = {"GUID": str(uuid4()), "Name": "Updated ViewEndpoint"}

    view_endpoint = ViewEndpoint(**view_endpoint_data)
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update_view_endpoint:
        mock_update_view_endpoint.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.update_view_endpoint(
                guid, view_endpoint.guid, view_endpoint
            )

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")
