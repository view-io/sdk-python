"""
    View.IO SDK

    This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

"""  # noqa: E501

import json
from unittest.mock import patch

from uuid import uuid4

import pytest
from viewio_sdk.models.api_error_enum import ApiErrorEnum
from viewio_sdk.models.collection import Collection
from viewio_sdk.rest import ApiException
from ..conftest import _get_success_mock_response, _get_failure_mock_response


# Test for successful exists_collection using mocked API
def test_exists_collection_success(config_api, guid):
    mock_response = _get_success_mock_response(status=200)
    # Mocked API call
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_collection:
        mock_collection.return_value = mock_response

        # Perform the exists_collection call
        exists = config_api.exists_collection_with_http_info(guid, guid)

        # Assert the result is as expected
        assert exists.status_code == 200


# Test for exists_collection when the collection does not exist (mocked API)
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_exists_collection_not_found(config_api, guid, error_code, expected_status):
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_collection:
        mock_create_collection.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.exists_collection_with_http_info(guid, guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful create collection using mocked API
def test_create_collection_success(config_api, guid):
    new_collection = Collection(id=1, guid=str(uuid4()), name="Test Collection")
    # Mock the RESTResponse
    mock_response = _get_success_mock_response(
        status=200, data=new_collection.to_json().encode("utf-8")
    )
    mock_response.data = new_collection.to_json().encode(
        "utf-8"
    )  # Mocked response data in bytes

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create:
        mock_create.return_value = mock_response

        collection = config_api.create_collection_with_http_info(guid, new_collection)

        assert collection.data == new_collection


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_create_collection_api_errors(config_api, guid, error_code, expected_status):
    mock_response = _get_failure_mock_response(expected_status, error_code)
    collection_data = {"GUID": str(uuid4()), "Name": "Test Collection"}

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_collection:
        mock_create_collection.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.create_collection_with_http_info(guid, Collection(**collection_data))

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful delete collection by GUID using mocked API
def test_delete_collection_by_guid_success(config_api, guid):
    collection_guid = "guid1"
    new_collection = Collection(id=1, guid=collection_guid, name="Test Collection")
    mock_response = _get_success_mock_response(
        status=200, data=new_collection.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete:
        mock_delete.return_value = mock_response

        response = config_api.delete_collection_with_http_info(guid, collection_guid)

        assert response.data == new_collection


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_delete_collection_api_errors(config_api, guid, error_code, expected_status):
    collection_guid = "invalid-guid"
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete_collection:
        mock_delete_collection.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.delete_collection_with_http_info(guid, collection_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve all collections using mocked API
def test_retrieve_collections_success(config_api, guid):
    collections = [
        Collection(id=1, guid=str(uuid4()), name="Collection 1"),
        Collection(id=2, guid=str(uuid4()), name="Collection 2"),
    ]
    # Convert the list of Collection objects to JSON
    collections_json = [collection.to_dict() for collection in collections]
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(collections_json).encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_collections_with_http_info(guid)

        assert response.data == collections


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_collections_api_errors(config_api, guid, error_code, expected_status):
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_collections_with_http_info(guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve collection using mocked API
def test_retrieve_collection_success(config_api, guid):
    collection = Collection(id=1, guid=str(uuid4()), name="Test Collection")
    # Mocked API response
    mock_response = _get_success_mock_response(
        status=200, data=collection.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_collection_with_http_info(guid, collection.guid)

        assert response.data == collection


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_collection_api_errors(config_api, guid, error_code, expected_status):
    collection_guid = str(uuid4())
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve_collection:
        mock_retrieve_collection.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_collection_with_http_info(guid, collection_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")
