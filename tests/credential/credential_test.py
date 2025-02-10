"""
    View.IO SDK

    This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

"""  # noqa: E501

import json
from datetime import datetime, timezone
from unittest.mock import patch

from uuid import uuid4

import pytest
from viewio_sdk.models.api_error_enum import ApiErrorEnum
from viewio_sdk.models.credential import Credential
from viewio_sdk.rest import ApiException
from ..conftest import _get_success_mock_response, _get_failure_mock_response

# Test for successful exists_credential using mocked API
def test_exists_credential_success(config_api, guid):
    credential_id = "test_credential_id"
    mock_response = _get_success_mock_response(status=200)
    # Mocked API call
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_credential:
        mock_credential.return_value = mock_response

        # Perform the exists_credential call
        exists = config_api.exists_credential(guid, credential_id)

        # Assert the result is as expected
        assert exists is True


# Test for exists_credential when the credential does not exist (mocked API)
@pytest.mark.parametrize("error_code", [404, 500])
def test_exists_credential_not_found(config_api, guid, error_code):
    # Mock the ApiException
    mock_response = _get_success_mock_response(status=error_code)

    credential_id = "invalid_credential_id"
    # Mocked API call that raises an exception when the credential is not found
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_credential:
        mock_credential.return_value = mock_response

        exists = config_api.exists_credential(guid, credential_id)

        # Assert the result is as expected
        assert exists is False


# Test for successful create credential using mocked API
def test_create_credential_success(config_api, guid):
    new_credential = Credential(
        guid=str(uuid4()),
        tenant_guid=str(uuid4()),
        user_guid=str(uuid4()),
        access_key="test_access_key",
        secret_key="test_secret_key",
        active=True,
        created_utc=datetime.now(timezone.utc),
    )

    # Mock the RESTResponse
    mock_response = _get_success_mock_response(
        status=200, data=new_credential.to_json().encode("utf-8")
    )
    mock_response.data = new_credential.to_json().encode(
        "utf-8"
    )  # Mocked response data in bytes

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create:
        mock_create.return_value = mock_response

        credential = config_api.create_credential(guid, new_credential)

        assert credential == new_credential


# Parametrized test for various API error scenarios for creating a credential
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_create_credential_api_errors(config_api, guid, error_code, expected_status):
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)
    credential_data = {
        "GUID": str(uuid4()),
        "TenantGuid": str(uuid4()),
        "user_guid": str(uuid4()),
        "access_key": "test_access_key",
        "secret_key": "test_secret_key",
        "active": True,
    }

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create:
        mock_create.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.create_credential(guid, Credential(**credential_data))

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successfully retrieving all credentials
def test_retrieve_credentials_success(config_api, guid):
    credentials = [
        Credential(
            guid=str(uuid4()),
            tenant_guid=str(uuid4()),
            user_guid=str(uuid4()),
            access_key="test_access_key_1",
            secret_key="test_secret_key_1",
            active=True,
            created_utc=datetime.now(timezone.utc),
        ),
        Credential(
            guid=str(uuid4()),
            tenant_guid=str(uuid4()),
            user_guid=str(uuid4()),
            access_key="test_access_key_2",
            secret_key="test_secret_key_2",
            active=True,
            created_utc=datetime.now(timezone.utc),
        ),
    ]
    # Convert the list of Credential objects to JSON
    credentials_json = [json.loads(credential.to_json()) for credential in credentials]
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(credentials_json).encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_get:
        mock_get.return_value = mock_response

        retrieved_credentials = config_api.retrieve_credentials(guid)

        assert retrieved_credentials == credentials


# Test for retrieving all credentials with API errors
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.INTERNALERROR, 500),
        (ApiErrorEnum.BADREQUEST, 400),
    ],
)
def test_retrieve_credentials_api_errors(config_api, guid, error_code, expected_status):
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_credentials(guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieving a credential successfully
def test_retrieve_credential_success(config_api, guid):
    credential_guid = str(uuid4())
    existing_credential = Credential(
        guid=credential_guid,
        tenant_guid=str(uuid4()),
        user_guid=str(uuid4()),
        access_key="test_access_key",
        secret_key="test_secret_key",
        active=True,
        created_utc=datetime.now(timezone.utc),
    )

    mock_response = _get_success_mock_response(
        status=200, data=existing_credential.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_get:
        mock_get.return_value = mock_response
        credential = config_api.retrieve_credential(guid, credential_guid)

        assert credential == existing_credential


# Parametrized test for various API error scenarios for retrieving a credential
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_credential_api_errors(config_api, guid, error_code, expected_status):
    credential_guid = str(uuid4())

    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_get:
        mock_get.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_credential(guid, credential_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successfully updating a credential
def test_update_credential_success(config_api, guid):
    credential_guid = str(uuid4())
    updated_credential = Credential(
        guid=credential_guid,
        tenant_guid=str(uuid4()),
        user_guid=str(uuid4()),
        access_key="updated_access_key",
        secret_key="updated_secret_key",
        active=False,
        created_utc=datetime.now(timezone.utc),
    )
    mock_response = _get_success_mock_response(
        status=200, data=updated_credential.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update:
        mock_update.return_value = mock_response

        credential = config_api.update_credential(
            guid, credential_guid, updated_credential
        )

        assert credential == updated_credential


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_update_credential_api_errors(config_api, guid, error_code, expected_status):
    # Mocked credential data to be updated
    credential_data = {
        "GUID": str(uuid4()),
        "TenantGuid": str(uuid4()),
        "user_guid": str(uuid4()),
        "access_key": "new_access_key",
        "secret_key": "new_secret_key",
        "active": True,
        "created_utc": datetime.now(timezone.utc),
    }
    # Mock the response based on the error_code
    mock_response = _get_failure_mock_response(expected_status, error_code)
    # Convert dictionary to Credential model
    credential = Credential(**credential_data)

    # Mock the update_credential API call and raise ApiException based on error_code
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update_credential:
        mock_update_credential.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.update_credential(guid, credential.guid, credential)

        # Assertions
        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")
