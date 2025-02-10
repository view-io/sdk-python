"""
    View.IO SDK

    This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

"""  # noqa: E501

import json
from unittest.mock import patch

from uuid import uuid4

import pytest
from viewio_sdk.models.api_error_enum import ApiErrorEnum
from viewio_sdk.models.metadata_rule import MetadataRule
from viewio_sdk.rest import ApiException
from ..conftest import _get_success_mock_response, _get_failure_mock_response


# Test for successful exists_metadata_rule using mocked API
def test_exists_metadata_rule_success(config_api, guid):
    metadata_rule_id = "test_metadata_rule_id"
    mock_response = _get_success_mock_response(status=200)
    # Mocked API call
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_metadata_rule:
        mock_metadata_rule.return_value = mock_response

        # Perform the exists_metadata_rule call
        exists = config_api.exists_metadata_rule(guid, metadata_rule_id)

        # Assert the result is as expected
        assert exists is True


# Test for exists_metadata_rule when the metadata_rule does not exist (mocked API)
@pytest.mark.parametrize("error_code", [404, 500])
def test_exists_metadata_rule_not_found(config_api, guid, error_code):
    # Mock the ApiException
    mock_response = _get_success_mock_response(status=error_code)

    metadata_rule_id = "invalid_metadata_rule_id"
    # Mocked API call that raises an exception when the metadata_rule is not found
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_metadata_rule:
        mock_metadata_rule.return_value = mock_response

        exists = config_api.exists_metadata_rule(guid, metadata_rule_id)

        # Assert the result is as expected
        assert exists is False


# Test for successful create metadata_rule using mocked API
def test_create_metadata_rule_success(config_api, guid):
    new_metadata_rule = MetadataRule(guid=str(uuid4()), name="Test MetadataRule")
    mock_response = _get_success_mock_response(
        status=200, data=new_metadata_rule.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create:
        mock_create.return_value = mock_response

        metadata_rule = config_api.create_metadata_rule(guid, new_metadata_rule)

        assert metadata_rule == new_metadata_rule


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_create_metadata_rule_api_errors(config_api, guid, error_code, expected_status):
    mock_response = _get_failure_mock_response(expected_status, error_code)
    metadata_rule_data = {"GUID": str(uuid4()), "Name": "Test MetadataRule"}

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_metadata_rule:
        mock_create_metadata_rule.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.create_metadata_rule(
                guid, MetadataRule(**metadata_rule_data)
            )

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful delete metadata_rule by GUID using mocked API
def test_delete_metadata_rule_by_guid_success(config_api, guid):
    metadata_rule_guid = "guid1"
    new_metadata_rule = MetadataRule(guid=metadata_rule_guid, name="Test MetadataRule")
    mock_response = _get_success_mock_response(
        status=200, data=new_metadata_rule.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete:
        mock_delete.return_value = mock_response

        response = config_api.delete_metadata_rule(guid, metadata_rule_guid)

        assert response == new_metadata_rule


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_delete_metadata_rule_api_errors(config_api, guid, error_code, expected_status):
    metadata_rule_guid = "invalid-guid"
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete_metadata_rule:
        mock_delete_metadata_rule.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.delete_metadata_rule(guid, metadata_rule_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve all metadata rules using mocked API
def test_retrieve_metadata_rules_success(config_api, guid):
    metadata_rules = [
        MetadataRule(guid=str(uuid4()), name="Rule 1"),
        MetadataRule(guid=str(uuid4()), name="Rule 2"),
    ]
    # Convert the list of MetadataRule objects to JSON
    metadata_rules_json = [rule.to_dict() for rule in metadata_rules]
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(metadata_rules_json).encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_metadata_rules(guid)

        assert response == metadata_rules


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_metadata_rules_api_errors(config_api, guid, error_code, expected_status):
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_metadata_rules(guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve metadata_rule using mocked API
def test_retrieve_metadata_rule_success(config_api, guid):
    rule = MetadataRule(guid=str(uuid4()), name="Test Rule")
    # Mocked API response
    mock_response = _get_success_mock_response(
        status=200, data=rule.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_metadata_rule(guid, rule.guid)

        assert response == rule


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_metadata_rule_api_errors(config_api, guid, error_code, expected_status):
    rule_guid = str(uuid4())
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve_rule:
        mock_retrieve_rule.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_metadata_rule(guid, rule_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful update metadata_rule using mocked API
def test_update_metadata_rule_success(config_api, guid):
    metadata_rule = MetadataRule(guid=str(uuid4()), name="Updated MetadataRule")
    mock_response = _get_success_mock_response(
        status=200, data=metadata_rule.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update:
        mock_update.return_value = mock_response

        response = config_api.update_metadata_rule(
            guid, metadata_rule.guid, metadata_rule
        )

        assert response == metadata_rule


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_update_metadata_rule_api_errors(config_api, guid, error_code, expected_status):
    metadata_rule_data = {"GUID": str(uuid4()), "Name": "Updated MetadataRule"}

    metadata_rule = MetadataRule(**metadata_rule_data)
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update_metadata_rule:
        mock_update_metadata_rule.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.update_metadata_rule(
                guid, metadata_rule.guid, metadata_rule
            )

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")
