"""
    View.IO SDK

    This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

"""  # noqa: E501

import json
from unittest.mock import patch

from uuid import uuid4

import pytest
from viewio_sdk.models.api_error_enum import ApiErrorEnum
from viewio_sdk.models.webhook_rule import WebhookRule
from viewio_sdk.rest import ApiException
from ..conftest import _get_success_mock_response, _get_failure_mock_response


# Test for successful exists_webhook_rule using mocked API
def test_exists_webhook_rule_success(config_api, guid):
    mock_response = _get_success_mock_response(status=200)
    # Mocked API call
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_webhook_rule:
        mock_webhook_rule.return_value = mock_response

        # Perform the exists_webhook_rule call
        exists = config_api.exists_webhook_rule_with_http_info(guid, guid)

        # Assert the result is as expected
        assert exists.status_code == 200


# Test for exists_webhook_rule when the webhook_rule does not exist (mocked API)
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_exists_webhook_rule_not_found(config_api, guid, error_code, expected_status):
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_webhook_rule:
        mock_create_webhook_rule.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.exists_webhook_rule_with_http_info(guid, guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful create webhook_rule using mocked API
def test_create_webhook_rule_success(config_api, guid):
    new_webhook_rule = WebhookRule(guid=str(uuid4()), name="Test WebhookRule")
    # Mock the RESTResponse
    mock_response = _get_success_mock_response(
        status=200, data=new_webhook_rule.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create:
        mock_create.return_value = mock_response

        webhook_rule = config_api.create_webhook_rule_with_http_info(guid, new_webhook_rule)

        assert webhook_rule.data == new_webhook_rule


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_create_webhook_rule_api_errors(config_api, guid, error_code, expected_status):
    mock_response = _get_failure_mock_response(expected_status, error_code)
    webhook_rule_data = {"GUID": str(uuid4()), "Name": "Test WebhookRule"}

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_webhook_rule:
        mock_create_webhook_rule.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.create_webhook_rule_with_http_info(
                guid, WebhookRule(**webhook_rule_data)
            )

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful delete webhook_rule by GUID using mocked API
def test_delete_webhook_rule_by_guid_success(config_api, guid):
    webhook_rule_guid = "guid1"
    new_webhook_rule = WebhookRule(
        id=1, guid=webhook_rule_guid, name="Test Webhook Rule"
    )
    mock_response = _get_success_mock_response(
        status=200, data=new_webhook_rule.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete:
        mock_delete.return_value = mock_response

        response = config_api.delete_webhook_rule_with_http_info(guid, webhook_rule_guid)

        assert response.data == new_webhook_rule


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_delete_webhook_rule_api_errors(config_api, guid, error_code, expected_status):
    webhook_rule_guid = "invalid-guid"
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete_webhook_rule:
        mock_delete_webhook_rule.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.delete_webhook_rule_with_http_info(guid, webhook_rule_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve all webhook rules using mocked API
def test_retrieve_webhook_rules_success(config_api, guid):
    webhook_rules = [
        WebhookRule(guid=str(uuid4()), name="Webhook Rule 1"),
        WebhookRule(guid=str(uuid4()), name="Webhook Rule 2"),
    ]
    # Convert the list of WebhookRule objects to JSON
    webhook_rules_json = [webhook_rule.to_dict() for webhook_rule in webhook_rules]
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(webhook_rules_json).encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_webhook_rules_with_http_info(guid)

        assert response.data == webhook_rules


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_webhook_rules_api_errors(config_api, guid, error_code, expected_status):
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_webhook_rules_with_http_info(guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve webhook rule using mocked API
def test_retrieve_webhook_rule_success(config_api, guid):
    rule = WebhookRule(guid=str(uuid4()), name="Test Webhook Rule")
    mock_response = _get_success_mock_response(
        status=200, data=rule.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_webhook_rule_with_http_info(guid, rule.guid)

        assert response.data == rule


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_webhook_rule_api_errors(config_api, guid, error_code, expected_status):
    rule_guid = str(uuid4())
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve_rule:
        mock_retrieve_rule.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_webhook_rule_with_http_info(guid, rule_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful update webhook_rule using mocked API
def test_update_webhook_rule_success(config_api, guid):
    webhook_rule = WebhookRule(guid=str(uuid4()), name="Updated WebhookRule")
    mock_response = _get_success_mock_response(
        status=200, data=webhook_rule.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update:
        mock_update.return_value = mock_response

        response = config_api.update_webhook_rule_with_http_info(
            guid, webhook_rule.guid, webhook_rule
        )

        assert response.data == webhook_rule


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_update_webhook_rule_api_errors(config_api, guid, error_code, expected_status):
    webhook_rule_data = {"GUID": str(uuid4()), "Name": "Updated WebhookRule"}

    webhook_rule = WebhookRule(**webhook_rule_data)
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update_webhook_rule:
        mock_update_webhook_rule.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.update_webhook_rule_with_http_info(guid, webhook_rule.guid, webhook_rule)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")
