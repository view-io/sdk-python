"""
    View.IO SDK

    This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

"""  # noqa: E501

import json
from unittest.mock import patch


import pytest
from viewio_sdk.models.api_error_enum import ApiErrorEnum
from viewio_sdk.models.user_master import UserMaster
from viewio_sdk.rest import ApiException
from ..conftest import _get_success_mock_response, _get_failure_mock_response


# Test for successful exists_user using mocked API
def test_exists_user_success(config_api, guid):
    mock_response = _get_success_mock_response(status=200)
    # Mocked API call
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_user:
        mock_user.return_value = mock_response

        # Perform the exists_user call
        exists = config_api.exists_user_with_http_info(guid, guid)

        # Assert the result is as expected
        assert exists.status_code == 200


# Test for exists_user when the user does not exist (mocked API)
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_exists_user_not_found(config_api, guid, error_code, expected_status):
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_user:
        mock_create_user.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.exists_user_with_http_info(guid, guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for creating a user successfully
def test_create_user_success(config_api, guid):
    user_data = {
        "FirstName": "John",
        "LastName": "Doe",
        "Email": "john.doe@example.com",
        "TenantGuid": "tenant-guid",
    }

    # Mock the RESTResponse
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(user_data).encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_user:
        mock_create_user.return_value = mock_response

        response = config_api.create_user_with_http_info(guid, UserMaster(**user_data))

        assert response.data == UserMaster(**user_data)


# Test for creating a user with API errors
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_create_user_api_errors(config_api, guid, error_code, expected_status):
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)
    mock_response.getheaders.return_value = mock_response
    user_data = {
        "FirstName": "John",
        "LastName": "Doe",
        "Email": "john.doe@example.com",
        "TenantGuid": "tenant-guid",
    }

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_user:
        mock_create_user.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.create_user_with_http_info(guid, UserMaster(**user_data))

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for deleting a user successfully
def test_delete_user_success(config_api, guid):
    user_data = {
        "FirstName": "John",
        "LastName": "Doe",
        "Email": "john.doe@example.com",
        "TenantGuid": "tenant-guid",
    }
    user_guid = "valid-guid"
    # Mock the RESTResponse
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(user_data).encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete_user:
        mock_delete_user.return_value = mock_response

        response = config_api.delete_user_with_http_info(guid, user_guid)

        assert response.data == UserMaster(**user_data)


# Test for deleting a user with API errors
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_delete_user_api_errors(config_api, guid, error_code, expected_status):
    user_guid = "invalid-guid"
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete_user:
        mock_delete_user.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.delete_user_with_http_info(guid, user_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieving all users successfully
def test_retrieve_users_success(config_api, guid):
    user_list = [
        UserMaster(guid="guid1", first_name="John", last_name="Doe"),
        UserMaster(guid="guid2", first_name="Jane", last_name="Doe"),
    ]
    # Convert the list of UserMaster objects to JSON
    user_list_json = [user.to_dict() for user in user_list]
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(user_list_json).encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        users = config_api.retrieve_users_with_http_info(guid)

        assert users.data == user_list


# Test for retrieving all users with API errors
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.INTERNALERROR, 500),
        (ApiErrorEnum.BADREQUEST, 400),
    ],
)
def test_retrieve_users_api_errors(config_api, guid, error_code, expected_status):
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_users_with_http_info(guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieving a user successfully
def test_retrieve_user_success(config_api, guid):
    user_guid = "valid-guid"
    new_user = UserMaster(
        guid=user_guid,
        email="test@example.com",
    )
    # Mocked API response
    mock_response = _get_success_mock_response(
        status=200, data=new_user.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve_user:
        mock_retrieve_user.return_value = mock_response

        user = config_api.retrieve_user_with_http_info(guid, user_guid)

        assert user.data == new_user


# Test for retrieving a user with API errors
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_user_api_errors(config_api, guid, error_code, expected_status):
    user_guid = "invalid-guid"
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve_user:
        mock_retrieve_user.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_user_with_http_info(guid, user_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for updating a user successfully
def test_update_user_success(config_api, guid):
    user_guid = "valid-guid"
    update_data = {"FirstName": "Jane"}
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(update_data).encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update_user:
        mock_update_user.return_value = mock_response

        response = config_api.update_user_with_http_info(
            guid, user_guid, UserMaster(**update_data)
        )

        assert response.data == UserMaster(**update_data)


# Test for updating a user with API errors
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_update_user_api_errors(config_api, guid, error_code, expected_status):
    user_guid = "test-guid"
    update_data = {"FirstName": "Jane"}
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update_user:
        mock_update_user.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.update_user_with_http_info(guid, user_guid, UserMaster(**update_data))

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")
