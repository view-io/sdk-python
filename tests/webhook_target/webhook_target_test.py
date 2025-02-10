"""
    View.IO SDK

    This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

"""  # noqa: E501

import json
from unittest.mock import patch

from uuid import uuid4

import pytest
from viewio_sdk.models.api_error_enum import ApiErrorEnum
from viewio_sdk.models.webhook_target import WebhookTarget
from viewio_sdk.rest import ApiException
from ..conftest import _get_success_mock_response, _get_failure_mock_response


# Test for successful exists_webhook_target using mocked API
def test_exists_webhook_target_success(config_api, guid):
    webhook_target_id = "test_webhook_target_id"
    mock_response = _get_success_mock_response(status=200)
    # Mocked API call
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_webhook_target:
        mock_webhook_target.return_value = mock_response

        # Perform the exists_webhook_target call
        exists = config_api.exists_webhook_target(guid, webhook_target_id)

        # Assert the result is as expected
        assert exists is True


# Test for exists_webhook_target when the webhook_target does not exist (mocked API)
@pytest.mark.parametrize("error_code", [404, 500])
def test_exists_webhook_target_not_found(config_api, guid, error_code):
    # Mock the ApiException
    mock_response = _get_success_mock_response(status=error_code)

    webhook_target_id = "invalid_webhook_target_id"
    # Mocked API call that raises an exception when the webhook_target is not found
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_webhook_target:
        mock_webhook_target.return_value = mock_response

        exists = config_api.exists_webhook_target(guid, webhook_target_id)

        # Assert the result is as expected
        assert exists is False


# Test for successful create webhook_target using mocked API
def test_create_webhook_target_success(config_api, guid):
    new_webhook_target = WebhookTarget(guid=str(uuid4()), name="Test WebhookTarget")
    # Mock the RESTResponse
    mock_response = _get_success_mock_response(
        status=200, data=new_webhook_target.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create:
        mock_create.return_value = mock_response

        webhook_target = config_api.create_webhook_target(
            guid, new_webhook_target
        )

        assert webhook_target == new_webhook_target


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_create_webhook_target_api_errors(config_api, guid, error_code, expected_status):
    mock_response = _get_failure_mock_response(expected_status, error_code)
    webhook_target_data = {"GUID": str(uuid4()), "Name": "Test WebhookTarget"}

    with patch(
        "viewio_sdk.api_client.ApiClient.call_api"
    ) as mock_create_webhook_target:
        mock_create_webhook_target.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.create_webhook_target(
                guid, WebhookTarget(**webhook_target_data)
            )

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful delete webhook_target by GUID using mocked API
def test_delete_webhook_target_by_guid_success(config_api, guid):
    webhook_target_guid = "guid1"
    new_webhook_target = WebhookTarget(
        id=1, guid=str(uuid4()), name="Test WebhookTarget", url="http://example.com"
    )
    mock_response = _get_success_mock_response(
        status=200, data=new_webhook_target.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete:
        mock_delete.return_value = mock_response

        response = config_api.delete_webhook_target(guid, webhook_target_guid)

        assert response == new_webhook_target


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_delete_webhook_target_api_errors(config_api, guid, error_code, expected_status):
    webhook_target_guid = "invalid-guid"
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch(
        "viewio_sdk.api_client.ApiClient.call_api"
    ) as mock_delete_webhook_target:
        mock_delete_webhook_target.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.delete_webhook_target(guid, webhook_target_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve all webhook targets using mocked API
def test_retrieve_webhook_targets_success(config_api, guid):
    webhook_targets = [
        WebhookTarget(guid=str(uuid4()), name="Webhook Target 1"),
        WebhookTarget(guid=str(uuid4()), name="Webhook Target 2"),
    ]
    # Convert the list of WebhookTarget objects to JSON
    webhook_targets_json = [
        webhook_target.to_dict() for webhook_target in webhook_targets
    ]
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(webhook_targets_json).encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_webhook_targets(guid)

        assert response == webhook_targets


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_webhook_targets_api_errors(config_api, guid, error_code, expected_status):
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_webhook_targets(guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve webhook target using mocked API
def test_retrieve_webhook_target_success(config_api, guid):
    target = WebhookTarget(guid=str(uuid4()), name="Test Webhook Target")
    mock_response = _get_success_mock_response(
        status=200, data=target.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_webhook_target(guid, target.guid)

        assert response == target


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_webhook_target_api_errors(config_api, guid, error_code, expected_status):
    target_guid = str(uuid4())
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve_target:
        mock_retrieve_target.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_webhook_target(guid, target_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful update webhook_target using mocked API
def test_update_webhook_target_success(config_api, guid):
    webhook_target = WebhookTarget(guid=str(uuid4()), name="Updated WebhookTarget")
    mock_response = _get_success_mock_response(
        status=200, data=webhook_target.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update:
        mock_update.return_value = mock_response

        response = config_api.update_webhook_target(
            guid, webhook_target.guid, webhook_target
        )

        assert response == webhook_target


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_update_webhook_target_api_errors(config_api, guid, error_code, expected_status):
    webhook_target_data = {"GUID": str(uuid4()), "Name": "Updated WebhookTarget"}

    webhook_target = WebhookTarget(**webhook_target_data)
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch(
        "viewio_sdk.api_client.ApiClient.call_api"
    ) as mock_update_webhook_target:
        mock_update_webhook_target.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.update_webhook_target(
                guid, webhook_target.guid, webhook_target
            )

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")
