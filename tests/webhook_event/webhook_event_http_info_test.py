"""
    View.IO SDK

    This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

"""  # noqa: E501

import json
from unittest.mock import patch

from uuid import uuid4

import pytest
from viewio_sdk.models.api_error_enum import ApiErrorEnum
from viewio_sdk.models.webhook_event import WebhookEvent
from viewio_sdk.rest import ApiException
from ..conftest import _get_success_mock_response, _get_failure_mock_response


# Test for successful exists_webhook_event using mocked API
def test_exists_webhook_event_success(config_api, guid):
    mock_response = _get_success_mock_response(status=200)
    # Mocked API call
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_webhook_event:
        mock_webhook_event.return_value = mock_response

        # Perform the exists_webhook_event call
        exists = config_api.exists_webhook_event_with_http_info(guid, guid)

        # Assert the result is as expected
        assert exists.status_code == 200


# Test for exists_webhook_event when the webhook_event does not exist (mocked API)
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_exists_webhook_event_not_found(config_api, guid, error_code, expected_status):
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_webhook_event:
        mock_create_webhook_event.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.exists_webhook_event_with_http_info(guid, guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve all webhook events using mocked API
def test_retrieve_webhook_events_success(config_api, guid):
    webhook_events = [
        WebhookEvent(guid=str(uuid4()), url="http://example.com"),
        WebhookEvent(guid=str(uuid4()), url="http://example2.com"),
    ]
    # Convert the list of WebhookEvent objects to JSON
    webhook_events_json = [webhook_event.to_dict() for webhook_event in webhook_events]
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(webhook_events_json).encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_webhook_events_with_http_info(guid)

        assert response.data == webhook_events


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_webhook_events_api_errors(config_api, guid, error_code, expected_status):
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_webhook_events_with_http_info(guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve webhook event using mocked API
def test_retrieve_webhook_event_success(config_api, guid):
    event = WebhookEvent(guid=str(uuid4()), url="http://example.com")
    mock_response = _get_success_mock_response(
        status=200, data=event.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_webhook_event_with_http_info(guid, event.guid)

        assert response.data == event


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_webhook_event_api_errors(config_api, guid, error_code, expected_status):
    event_guid = str(uuid4())
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve_event:
        mock_retrieve_event.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_webhook_event_with_http_info(guid, event_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")
