"""
    View.IO SDK

    This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

"""  # noqa: E501

import json
from unittest.mock import patch

from uuid import uuid4

import pytest
from viewio_sdk.models.api_error_enum import ApiErrorEnum
from viewio_sdk.models.encryption_key import EncryptionKey
from viewio_sdk.rest import ApiException
from ..conftest import _get_success_mock_response, _get_failure_mock_response


# Test for successful exists_encryption_key using mocked API
def test_exists_encryption_key_success(config_api, guid):
    mock_response = _get_success_mock_response(status=200)
    # Mocked API call
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_encryption_key:
        mock_encryption_key.return_value = mock_response

        # Perform the exists_encryption_key call
        exists = config_api.exists_encryption_key_with_http_info(guid, guid)

        # Assert the result is as expected
        assert exists.status_code == 200


# Test for exists_encryption_key when the encryption_key does not exist (mocked API)
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_exists_encryption_key_not_found(config_api, guid, error_code, expected_status):
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_encryption_key:
        mock_create_encryption_key.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.exists_encryption_key_with_http_info(guid, guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful create encryption key using mocked API
def test_create_encryption_key_success(config_api, guid):
    new_encryption_key = EncryptionKey(guid=str(uuid4()), name="Test Encryption Key")
    # Mock the RESTResponse
    mock_response = _get_success_mock_response(
        status=200, data=new_encryption_key.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create:
        mock_create.return_value = mock_response

        encryption_key = config_api.create_encryption_key_with_http_info(
            guid, new_encryption_key
        )

        assert encryption_key.data == new_encryption_key


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_create_encryption_key_api_errors(config_api, guid, error_code, expected_status):
    mock_response = _get_failure_mock_response(expected_status, error_code)
    encryption_key_data = {"GUID": str(uuid4()), "Name": "Test Encryption Key"}

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_key:
        mock_create_key.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.create_encryption_key_with_http_info(
                guid, EncryptionKey(**encryption_key_data)
            )

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful delete encryption key using mocked API
def test_delete_encryption_key_success(config_api, guid):
    encryption_key_guid = str(uuid4())
    new_encryption_key = EncryptionKey(
        guid=encryption_key_guid, name="Test Encryption Key"
    )
    # Mock the RESTResponse
    mock_response = _get_success_mock_response(
        status=200, data=new_encryption_key.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete:
        mock_delete.return_value = mock_response

        response = config_api.delete_encryption_key_with_http_info(guid, encryption_key_guid)

        assert response.data == new_encryption_key


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_delete_encryption_key_api_errors(config_api, guid, error_code, expected_status):
    encryption_key_guid = str(uuid4())
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete_key:
        mock_delete_key.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.delete_encryption_key_with_http_info(guid, encryption_key_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve all encryption keys using mocked API
def test_retrieve_encryption_keys_success(config_api, guid):
    encryption_keys = [
        EncryptionKey(guid=str(uuid4()), name="Key 1"),
        EncryptionKey(guid=str(uuid4()), name="Key 2"),
    ]
    # Convert the list of EncryptionKey objects to JSON
    encryption_keys_json = [key.to_dict() for key in encryption_keys]
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(encryption_keys_json).encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_encryption_keys_with_http_info(guid)

        assert response.data == encryption_keys


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_encryption_keys_api_errors(config_api, guid, error_code, expected_status):
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_encryption_keys_with_http_info(guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve encryption key using mocked API
def test_retrieve_encryption_key_success(config_api, guid):
    encryption_key = EncryptionKey(guid=str(uuid4()), name="Test Encryption Key")
    # Mocked API response
    mock_response = _get_success_mock_response(
        status=200, data=encryption_key.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_encryption_key_with_http_info(guid, encryption_key.guid)

        assert response.data == encryption_key


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_encryption_key_api_errors(config_api, guid, error_code, expected_status):
    encryption_key_guid = str(uuid4())
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve_key:
        mock_retrieve_key.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_encryption_key_with_http_info(guid, encryption_key_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful update encryption key using mocked API
def test_update_encryption_key_success(config_api, guid):
    encryption_key = EncryptionKey(guid=str(uuid4()), name="Updated Encryption Key")
    mock_response = _get_success_mock_response(
        status=200, data=encryption_key.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update:
        mock_update.return_value = mock_response

        response = config_api.update_encryption_key_with_http_info(
            guid, encryption_key.guid, encryption_key
        )

        assert response.data == encryption_key


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_update_encryption_key_api_errors(config_api, guid, error_code, expected_status):
    encryption_key_data = {"GUID": str(uuid4()), "Name": "Updated Encryption Key"}
    mock_response = _get_failure_mock_response(expected_status, error_code)
    encryption_key = EncryptionKey(**encryption_key_data)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update_key:
        mock_update_key.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.update_encryption_key_with_http_info(
                guid, encryption_key.guid, encryption_key
            )

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")
