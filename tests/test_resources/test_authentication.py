from unittest.mock import patch, MagicMock
from view_sdk.resources.configuration.authentication import Authentication


@patch("view_sdk.resources.configuration.authentication.get_client")
@patch("view_sdk.models.tenant_metadata.TenantMetadataModel.model_validate")
def test_retrieve_tenants_for_email(mock_model_validate, mock_get_client):
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = [{"foo": "bar"}]
    mock_model_validate.side_effect = lambda *args, **kwargs: args[0] if args else kwargs
    result = Authentication.retrieve_tenants_for_email("test@example.com")
    assert result == [{"foo": "bar"}]
    mock_client.request.assert_called()
    mock_model_validate.assert_called()


@patch("view_sdk.resources.configuration.authentication.get_client")
@patch("view_sdk.models.authentication_token.AuthenticationTokenModel.model_validate")
def test_generate_authentication_token(mock_model_validate, mock_get_client):
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {"token": "abc"}
    mock_model_validate.return_value = {"token": "abc"}
    result = Authentication.generate_authentication_token("email", "pw", "tenant")
    assert result == {"token": "abc"}
    mock_client.request.assert_called()
    mock_model_validate.assert_called()


@patch("view_sdk.resources.configuration.authentication.get_client")
@patch("view_sdk.models.authentication_token.AuthenticationTokenModel.model_validate")
def test_generate_authentication_token_sha_256(mock_model_validate, mock_get_client):
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {"token": "abc"}
    mock_model_validate.return_value = {"token": "abc"}
    result = Authentication.generate_authentication_token_sha_256(
        "email", "sha256", "tenant"
    )
    assert result == {"token": "abc"}
    mock_client.request.assert_called()
    mock_model_validate.assert_called()


@patch("view_sdk.resources.configuration.authentication.get_client")
@patch("view_sdk.models.authentication_token.AuthenticationTokenModel.model_validate")
def test_validate_authentication_token(mock_model_validate, mock_get_client):
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {"token": "abc"}
    mock_model_validate.return_value = {"token": "abc"}
    result = Authentication.validate_authentication_token("token")
    assert result == {"token": "abc"}
    mock_client.request.assert_called()
    mock_model_validate.assert_called()


@patch("view_sdk.resources.configuration.authentication.get_client")
@patch("view_sdk.models.authentication_token.AuthenticationTokenModel.model_validate")
def test_retrieve_token_details(mock_model_validate, mock_get_client):
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {"token": "abc"}
    mock_model_validate.return_value = {"token": "abc"}
    result = Authentication.retrieve_token_details("token")
    assert result == {"token": "abc"}
    mock_client.request.assert_called()
    mock_model_validate.assert_called()


@patch("view_sdk.resources.configuration.authentication.get_client")
@patch("view_sdk.models.authentication_token.AuthenticationTokenModel.model_validate")
def test_retrieve_administrator_token(mock_model_validate, mock_get_client):
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {"token": "abc"}
    mock_model_validate.return_value = {"token": "abc"}
    result = Authentication.retrieve_administrator_token("email", "pw")
    assert result == {"token": "abc"}
    mock_client.request.assert_called()
    mock_model_validate.assert_called()


@patch("view_sdk.resources.configuration.authentication.get_client")
@patch("view_sdk.models.authentication_token.AuthenticationTokenModel.model_validate")
def test_retrieve_administrator_token_sha_256(mock_model_validate, mock_get_client):
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {"token": "abc"}
    mock_model_validate.return_value = {"token": "abc"}
    result = Authentication.retrieve_administrator_token_sha_256("email", "sha256")
    assert result == {"token": "abc"}
    mock_client.request.assert_called()
    mock_model_validate.assert_called()
