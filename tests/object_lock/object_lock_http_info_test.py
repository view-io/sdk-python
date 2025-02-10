"""
    View.IO SDK

    This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

"""  # noqa: E501

import json
from unittest.mock import patch

from uuid import uuid4

import pytest
from viewio_sdk.models.api_error_enum import ApiErrorEnum
from viewio_sdk.models.object_lock import ObjectLock
from viewio_sdk.rest import ApiException
from ..conftest import _get_success_mock_response, _get_failure_mock_response


# Test for successful exists_object_lock using mocked API
def test_exists_object_lock_success(config_api, guid):
    mock_response = _get_success_mock_response(status=200)
    # Mocked API call
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_object_lock:
        mock_object_lock.return_value = mock_response

        # Perform the exists_object_lock call
        exists = config_api.exists_object_lock_with_http_info(guid, guid)

        # Assert the result is as expected
        assert exists.status_code == 200


# Test for exists_object_lock when the object_lock does not exist (mocked API)
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_exists_object_lock_not_found(config_api, guid, error_code, expected_status):
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_object_lock:
        mock_create_object_lock.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.exists_object_lock_with_http_info(guid, guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful create object_lock using mocked API
def test_create_object_lock_success(config_api, guid):
    new_object_lock = ObjectLock(guid=str(uuid4()), is_read_lock=True)
    # Mock the RESTResponse
    mock_response = _get_success_mock_response(
        status=200, data=new_object_lock.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create:
        mock_create.return_value = mock_response

        object_lock = config_api.create_object_lock_with_http_info(guid, new_object_lock)

        assert object_lock.data == new_object_lock


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_create_object_lock_api_errors(config_api, guid, error_code, expected_status):
    mock_response = _get_failure_mock_response(expected_status, error_code)
    object_lock_data = {"GUID": str(uuid4()), "is_read_lock": True}

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_object_lock:
        mock_create_object_lock.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.create_object_lock_with_http_info(guid, ObjectLock(**object_lock_data))

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful delete object_lock by GUID using mocked API
def test_delete_object_lock_by_guid_success(config_api, guid):
    object_lock_guid = "guid1"
    new_object_lock = ObjectLock(guid=str(uuid4()), name="Test ObjectLock")
    mock_response = _get_success_mock_response(
        status=200, data=new_object_lock.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete:
        mock_delete.return_value = mock_response

        response = config_api.delete_object_lock_with_http_info(guid, object_lock_guid)

        assert response.data == new_object_lock


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_delete_object_lock_api_errors(config_api, guid, error_code, expected_status):
    object_lock_guid = "invalid-guid"
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete_object_lock:
        mock_delete_object_lock.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.delete_object_lock_with_http_info(guid, object_lock_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve all object locks using mocked API
def test_retrieve_object_locks_success(config_api, guid):
    object_locks = [
        ObjectLock(guid=str(uuid4()), name="Object Lock 1"),
        ObjectLock(guid=str(uuid4()), name="Object Lock 2"),
    ]
    # Convert the list of ObjectLock objects to JSON
    object_locks_json = [object_lock.to_dict() for object_lock in object_locks]
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(object_locks_json).encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_object_locks_with_http_info(guid)

        assert response.data == object_locks


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_object_locks_api_errors(config_api, guid, error_code, expected_status):
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_object_locks_with_http_info(guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve object lock using mocked API
def test_retrieve_object_lock_success(config_api, guid):
    lock = ObjectLock(guid=str(uuid4()), name="Test Object Lock")
    mock_response = _get_success_mock_response(
        status=200, data=lock.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_object_lock_with_http_info(guid, lock.guid)

        assert response.data == lock


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_object_lock_api_errors(config_api, guid, error_code, expected_status):
    lock_guid = str(uuid4())
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve_lock:
        mock_retrieve_lock.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_object_lock_with_http_info(guid, lock_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful update object_lock using mocked API
def test_update_object_lock_success(config_api, guid):
    object_lock = ObjectLock(guid=str(uuid4()), is_read_lock=True)
    mock_response = _get_success_mock_response(
        status=200, data=object_lock.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update:
        mock_update.return_value = mock_response

        response = config_api.update_object_lock_with_http_info(
            guid, object_lock.guid, object_lock
        )

        assert response.data == object_lock


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_update_object_lock_api_errors(config_api, guid, error_code, expected_status):
    object_lock_data = {"GUID": str(uuid4()), "is_read_lock": True}

    object_lock = ObjectLock(**object_lock_data)
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update_object_lock:
        mock_update_object_lock.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.update_object_lock_with_http_info(guid, object_lock.guid, object_lock)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")
