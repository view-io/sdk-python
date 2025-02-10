"""
    View.IO SDK

    This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

"""  # noqa: E501

import json
from unittest.mock import patch

from uuid import uuid4

import pytest
from viewio_sdk.models.api_error_enum import ApiErrorEnum
from viewio_sdk.models.storage_pool import StoragePool
from viewio_sdk.rest import ApiException
from ..conftest import _get_success_mock_response, _get_failure_mock_response


# Test for successful exists_pool using mocked API
def test_exists_pool_success(config_api, guid):
    mock_response = _get_success_mock_response(status=200)
    # Mocked API call
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_pool:
        mock_pool.return_value = mock_response

        # Perform the exists_pool call
        exists = config_api.exists_pool_without_preload_content(guid, guid)

        # Assert the result is as expected
        assert exists.status == 200


# Test for exists_pool when the pool does not exist (mocked API)
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_exists_pool_not_found(config_api, guid, error_code, expected_status):
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_pool:
        mock_create_pool.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.exists_pool_without_preload_content(guid, guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful create storage pool using mocked API
def test_create_pool_success(config_api, guid):
    new_pool = StoragePool(guid=str(uuid4()), name="Test Storage Pool")
    # Mock the RESTResponse
    mock_response = _get_success_mock_response(
        status=200, data=new_pool.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create:
        mock_create.return_value = mock_response

        pool = config_api.create_pool_without_preload_content(guid, new_pool)

        assert pool.data == new_pool.to_json().encode("utf-8")


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_create_pool_api_errors(config_api, guid, error_code, expected_status):
    mock_response = _get_failure_mock_response(expected_status, error_code)
    pool_data = {"GUID": str(uuid4()), "Name": "Test Storage Pool"}

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_pool:
        mock_create_pool.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.create_pool_without_preload_content(guid, StoragePool(**pool_data))

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful delete storage pool using mocked API
def test_delete_pool_success(config_api, guid):
    pool_guid = str(uuid4())
    new_pool = StoragePool(guid=pool_guid, name="Test Storage Pool")
    mock_response = _get_success_mock_response(
        status=200, data=new_pool.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete:
        mock_delete.return_value = mock_response

        response = config_api.delete_pool_without_preload_content(guid, pool_guid)

        assert response.data == new_pool.to_json().encode("utf-8")


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_delete_pool_api_errors(config_api, guid, error_code, expected_status):
    pool_guid = str(uuid4())
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete_pool:
        mock_delete_pool.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.delete_pool_without_preload_content(guid, pool_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve all storage pools using mocked API
def test_retrieve_pools_success(config_api, guid):
    storage_pools = [
        StoragePool(guid=str(uuid4()), name="Storage Pool 1"),
        StoragePool(guid=str(uuid4()), name="Storage Pool 2"),
    ]
    # Convert the list of StoragePool objects to JSON
    storage_pools_json = [pool.to_dict() for pool in storage_pools]
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(storage_pools_json).encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_pools_without_preload_content(guid)

        assert response.data == json.dumps(storage_pools_json).encode("utf-8")


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_pools_api_errors(config_api, guid, error_code, expected_status):
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_pools_without_preload_content(guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve storage pool using mocked API
def test_retrieve_pool_success(config_api, guid):
    pool = StoragePool(guid=str(uuid4()), name="Test Storage Pool")
    # Mocked API response
    mock_response = _get_success_mock_response(
        status=200, data=pool.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_pool_without_preload_content(guid, pool.guid)

        assert response.data == pool.to_json().encode("utf-8")


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_pool_api_errors(config_api, guid, error_code, expected_status):
    pool_guid = str(uuid4())
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve_pool:
        mock_retrieve_pool.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_pool_without_preload_content(guid, pool_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful update storage pool using mocked API
def test_update_pool_success(config_api, guid):
    pool = StoragePool(guid=str(uuid4()), name="Updated Storage Pool")
    mock_response = _get_success_mock_response(
        status=200, data=pool.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update:
        mock_update.return_value = mock_response

        response = config_api.update_pool_without_preload_content(guid, pool.guid, pool)

        assert response.data == pool.to_json().encode("utf-8")


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_update_pool_api_errors(config_api, guid, error_code, expected_status):
    pool_data = {"GUID": str(uuid4()), "Name": "Updated Storage Pool"}
    mock_response = _get_failure_mock_response(expected_status, error_code)
    pool = StoragePool(**pool_data)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update_pool:
        mock_update_pool.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.update_pool_without_preload_content(guid, pool.guid, pool)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


