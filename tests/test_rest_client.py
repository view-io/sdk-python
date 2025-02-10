import pytest
import json
import urllib3
from unittest.mock import Mock, patch
from viewio_sdk.rest import RESTClientObject, RESTResponse, is_socks_proxy_url
from viewio_sdk.exceptions import ApiException

@pytest.fixture
def mock_configuration():
    config = Mock()
    config.verify_ssl = True
    config.ssl_ca_cert = None
    config.cert_file = None
    config.key_file = None
    config.assert_hostname = None
    config.retries = None
    config.tls_server_name = None
    config.socket_options = None
    config.connection_pool_maxsize = None
    config.proxy = None
    config.proxy_headers = None
    return config

@pytest.fixture
def rest_client(mock_configuration):
    return RESTClientObject(mock_configuration)

def test_is_socks_proxy_url():
    assert is_socks_proxy_url("socks5://127.0.0.1:1080")
    assert is_socks_proxy_url("socks4://127.0.0.1:1080")
    assert not is_socks_proxy_url("http://127.0.0.1:1080")
    assert not is_socks_proxy_url(None)

def test_rest_response():
    mock_resp = Mock()
    mock_resp.status = 200
    mock_resp.reason = "OK"
    mock_resp.data = b"test data"
    mock_resp.headers = {"Content-Type": "application/json"}

    response = RESTResponse(mock_resp)
    assert response.status == 200
    assert response.reason == "OK"
    assert response.read() == b"test data"
    assert response.getheaders() == {"Content-Type": "application/json"}
    assert response.getheader("Content-Type") == "application/json"
    assert response.getheader("Non-Existent", "default") == "default"

@patch("viewio_sdk.rest.urllib3.PoolManager")
def test_rest_client_init(mock_pool_manager, mock_configuration):
    RESTClientObject(mock_configuration)
    mock_pool_manager.assert_called_once()

@patch("viewio_sdk.rest.urllib3.ProxyManager")
def test_rest_client_init_with_proxy(mock_proxy_manager, mock_configuration):
    mock_configuration.proxy = "http://proxy.example.com:8080"
    RESTClientObject(mock_configuration)
    mock_proxy_manager.assert_called_once()

@patch("urllib3.contrib.socks.SOCKSProxyManager")
def test_rest_client_init_with_socks_proxy(mock_socks_proxy_manager, mock_configuration):
    mock_configuration.proxy = "socks5://127.0.0.1:1080"
    RESTClientObject(mock_configuration)
    mock_socks_proxy_manager.assert_called_once()

@pytest.mark.parametrize("method", ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"])
def test_request_methods(rest_client, method):
    with patch.object(rest_client.pool_manager, "request") as mock_request:
        mock_response = Mock()
        mock_request.return_value = mock_response

        rest_client.request(method, "http://example.com")
        mock_request.assert_called_once()

def test_request_with_json_body(rest_client):
    with patch.object(rest_client.pool_manager, "request") as mock_request:
        mock_response = Mock()
        mock_request.return_value = mock_response

        body = {"key": "value"}
        rest_client.request("POST", "http://example.com", body=body)
        mock_request.assert_called_once()
        assert json.loads(mock_request.call_args[1]["body"]) == body

def test_request_with_form_urlencoded(rest_client):
    with patch.object(rest_client.pool_manager, "request") as mock_request:
        mock_response = Mock()
        mock_request.return_value = mock_response

        post_params = {"key": "value"}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        rest_client.request("POST", "http://example.com", headers=headers, post_params=post_params)
        mock_request.assert_called_once()
        assert mock_request.call_args[1]["fields"] == post_params

def test_request_with_multipart_form_data(rest_client):
    with patch.object(rest_client.pool_manager, "request") as mock_request:
        mock_response = Mock()
        mock_request.return_value = mock_response

        post_params = [("key", "value"), ("dict_key", {"nested": "data"})]
        headers = {"Content-Type": "multipart/form-data"}
        rest_client.request("POST", "http://example.com", headers=headers, post_params=post_params)
        mock_request.assert_called_once()
        assert mock_request.call_args[1]["fields"] == [("key", "value"), ("dict_key", '{"nested": "data"}')]

def test_request_with_string_body(rest_client):
    with patch.object(rest_client.pool_manager, "request") as mock_request:
        mock_response = Mock()
        mock_request.return_value = mock_response

        body = "test string body"
        rest_client.request("POST", "http://example.com", body=body)
        mock_request.assert_called_once()
        assert mock_request.call_args[1]["body"] == json.dumps(body)


def test_request_with_boolean_body(rest_client):
    with patch.object(rest_client.pool_manager, "request") as mock_request:
        mock_response = Mock()
        mock_request.return_value = mock_response

        headers = {"Content-Type": "text/plain"}
        rest_client.request("POST", "http://example.com", headers=headers, body=True)
        mock_request.assert_called_once()
        assert mock_request.call_args[1]["body"] == "true"

def test_request_with_invalid_params(rest_client):
    with pytest.raises(ApiException):
        headers = {"Content-Type": "invalid/content-type"}
        body = {"key": "value"}
        rest_client.request("POST", "http://example.com", headers=headers, body=body)


def test_request_with_ssl_error(rest_client):
    with patch.object(rest_client.pool_manager, "request") as mock_request:
        mock_request.side_effect = urllib3.exceptions.SSLError("SSL Error")

        with pytest.raises(ApiException):
            rest_client.request("GET", "https://example.com")

def test_request_with_timeout(rest_client):
    with patch.object(rest_client.pool_manager, "request") as mock_request:
        mock_response = Mock()
        mock_request.return_value = mock_response

        rest_client.request("GET", "http://example.com", _request_timeout=5)
        mock_request.assert_called_once()
        assert mock_request.call_args[1]["timeout"].total == 5

def test_request_with_connection_and_read_timeout(rest_client):
    with patch.object(rest_client.pool_manager, "request") as mock_request:
        mock_response = Mock()
        mock_request.return_value = mock_response

        rest_client.request("GET", "http://example.com", _request_timeout=(3, 7))
        mock_request.assert_called_once()
        assert mock_request.call_args[1]["timeout"]._connect == 3
        assert mock_request.call_args[1]["timeout"]._read == 7
