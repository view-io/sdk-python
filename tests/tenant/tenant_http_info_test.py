"""
    View.IO SDK

    This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

"""  # noqa: E501

import json
from unittest.mock import patch


import pytest
from viewio_sdk.models.api_error_enum import ApiErrorEnum
from viewio_sdk.models.tenant_metadata import TenantMetadata
from viewio_sdk.rest import ApiException
from ..conftest import _get_success_mock_response, _get_failure_mock_response


def test_retrieve_tenant_success(config_api, guid):
    new_tenant = TenantMetadata(
        guid=guid,
        name="Test Tenant",
    )
    # Mocked API response
    mock_response = _get_success_mock_response(
        status=200, data=new_tenant.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve_tenant:
        mock_retrieve_tenant.return_value = mock_response

        result = config_api.retrieve_tenant_with_http_info(guid)

        assert result.data == new_tenant


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_tenant_api_errors(config_api, guid, error_code, expected_status):
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve_tenant:
        mock_retrieve_tenant.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_tenant_with_http_info(guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


def test_update_tenant_success(config_api, guid):
    updated_data = {"Name": "Updated Tenant"}
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(updated_data).encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update_tenant:
        mock_update_tenant.return_value = mock_response

        result = config_api.update_tenant_with_http_info(guid, TenantMetadata(**updated_data))

        assert result.data.name == "Updated Tenant"


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_update_tenant_api_errors(config_api, guid, error_code, expected_status):
    update_data = {"Name": "Updated Tenant"}
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update_tenant:
        mock_update_tenant.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.update_tenant_with_http_info(guid, TenantMetadata(**update_data))

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")
