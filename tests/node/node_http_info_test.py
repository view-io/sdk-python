"""
    View.IO SDK

    This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

"""  # noqa: E501

import json
from unittest.mock import patch


import pytest
from viewio_sdk.models.api_error_enum import ApiErrorEnum
from viewio_sdk.models.node import Node
from viewio_sdk.rest import ApiException
from ..conftest import _get_success_mock_response, _get_failure_mock_response


# Test for successful exists_node using mocked API
def test_exists_node_success(config_api, guid):
    mock_response = _get_success_mock_response(status=200)
    # Mocked API call
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_node:
        mock_node.return_value = mock_response

        # Perform the exists_node call
        exists = config_api.exists_node_with_http_info(guid)

        # Assert the result is as expected
        assert exists.status_code == 200

# Test for exists_node when the node does not exist (mocked API)
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_exists_node_not_found(config_api, guid, error_code, expected_status):
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_node:
        mock_create_node.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.exists_node_with_http_info(guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful create node using mocked API
def test_create_node_success(config_api, guid):
    new_node = Node(id=3, guid="guid3", name="Node 3")
    # Mock the RESTResponse
    mock_response = _get_success_mock_response(
        status=200, data=new_node.to_json().encode("utf-8")
    )  # Mocked response data in bytes
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create:
        mock_create.return_value = mock_response

        node = config_api.create_node_with_http_info(new_node)

        assert node.data == new_node


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_create_node_api_errors(config_api, guid, error_code, expected_status):
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)
    node_data = {"GUID": "test-guid", "Name": "Test Node"}

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_node:
        mock_create_node.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.create_node_with_http_info(Node(**node_data))

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful delete node by GUID using mocked API
def test_delete_node_by_guid_success(config_api, guid):
    node_guid = "guid1"
    new_node = Node(id=3, guid="guid3", name="Node 3")
    # Mock the RESTResponse
    mock_response = _get_success_mock_response(
        status=200, data=new_node.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete:
        mock_delete.return_value = mock_response

        node = config_api.delete_node_with_http_info(node_guid)

        assert node.data == new_node


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_delete_node_api_errors(config_api, guid, error_code, expected_status):
    node_guid = "invalid-guid"
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete_node:
        mock_delete_node.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.delete_node_with_http_info(node_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful retrieve using mocked API
def test_retrieve_nodes_success(config_api, guid):
    # Mocked API response
    mocked_nodes = [
        Node(id=1, guid="guid1", name="Node 1"),
        Node(id=2, guid="guid2", name="Node 2"),
    ]
    # Convert the list of Node objects to JSON
    mocked_nodes_json = [node.to_dict() for node in mocked_nodes]
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(mocked_nodes_json).encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        nodes = config_api.retrieve_nodes_with_http_info()

        assert nodes.data == mocked_nodes


# Test for retrieve when there is an API error
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.INTERNALERROR, 500),
        (ApiErrorEnum.BADREQUEST, 400),
    ],
)
def test_retrieve_nodes_failure(config_api, guid, error_code, expected_status):
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_nodes_with_http_info()

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful retrieve by GUID using mocked API
def test_retrieve_node_by_guid_success(config_api, guid):
    node_guid = "guid1"
    mocked_node = Node(id=1, guid="guid1", name="Node 1")
    # Mocked API response
    mock_response = _get_success_mock_response(
        status=200, data=mocked_node.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        node = config_api.retrieve_node_with_http_info(node_guid)

        assert node.data == mocked_node


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_node_api_errors(config_api, guid, error_code, expected_status):
    node_guid = "invalid-guid"
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve_node:
        mock_retrieve_node.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_node_with_http_info(node_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful update node by GUID using mocked API
def test_update_node_by_guid_success(config_api, guid):
    updated_node = Node(id=1, guid="guid1", name="Updated Node")
    mock_response = _get_success_mock_response(
        status=200, data=updated_node.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update:
        mock_update.return_value = mock_response

        node = config_api.update_node_with_http_info(updated_node.guid, updated_node)

        assert node.data == updated_node


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_update_node_api_errors(config_api, guid, error_code, expected_status):
    node_guid = "test-guid"
    update_data = {"Name": "Updated Node"}
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update_node:
        mock_update_node.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.update_node_with_http_info(node_guid, Node(**update_data))

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


