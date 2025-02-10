"""
    View.IO SDK

    This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

"""  # noqa: E501

import pytest
from unittest.mock import patch
from viewio_sdk.api.auth_api import AuthApi
from viewio_sdk.models.token import Token
from viewio_sdk.models.api_error_enum import ApiErrorEnum
from viewio_sdk.models.api_error_response import ApiErrorResponse
from viewio_sdk.rest import ApiException


@pytest.fixture
def auth_api():
    """Fixture to return a mocked AuthApi instance."""
    return AuthApi()


# Test for successful login using mocked API
def test_login_for_access_token(auth_api):
    username = "johndoe"
    password = "secret"

    # Mocked API call
    with patch("viewio_sdk.api.auth_api.AuthApi.login_for_access_token") as mock_login:
        # Create a mock token
        mock_token = Token(access_token="mock_access_token", token_type="bearer")
        mock_login.return_value = mock_token

        # Perform the login call
        token = auth_api.login_for_access_token(username, password)

        # Assert the token returned is the mock token
        assert token.access_token == "mock_access_token"
        assert token.token_type == "bearer"
        mock_login.assert_called_once_with(username, password)


# Test for handling login failure (invalid credentials) using mocked API
def test_login_for_access_token_invalid_credentials(auth_api):
    username = "invalid_user"
    password = "wrong_password"

    # Mocked API call that raises an exception for invalid credentials
    with patch("viewio_sdk.api.auth_api.AuthApi.login_for_access_token") as mock_login:
        mock_login.side_effect = ApiException(
            status=401,
            reason="Unauthorized",
            data=ApiErrorResponse(
                Error=ApiErrorEnum.AUTHENTICATIONFAILED,
                Description=""
            )
        )

        # Perform the login call and assert the exception is raised
        with pytest.raises(ApiException) as exc_info:
            auth_api.login_for_access_token(username, password)

        # Assert that the exception has the expected status and reason
        assert exc_info.value.status == 401
        assert exc_info.value.reason == "Unauthorized"
        assert exc_info.value.data.error == ApiErrorEnum.AUTHENTICATIONFAILED
        assert exc_info.value.data.description == ""
        mock_login.assert_called_once_with(username, password)
