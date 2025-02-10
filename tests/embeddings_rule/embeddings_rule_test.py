"""
    View.IO SDK

    This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

"""  # noqa: E501

import json
from unittest.mock import patch

from uuid import uuid4

import pytest
from viewio_sdk.models.api_error_enum import ApiErrorEnum
from viewio_sdk.models.embeddings_rule import EmbeddingsRule
from viewio_sdk.rest import ApiException
from ..conftest import _get_success_mock_response, _get_failure_mock_response


# Test for successful exists_embeddings_rule using mocked API
def test_exists_embeddings_rule_success(config_api, guid):
    embeddings_rule_id = "test_embeddings_rule_id"
    mock_response = _get_success_mock_response(status=200)
    # Mocked API call
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_embeddings_rule:
        mock_embeddings_rule.return_value = mock_response

        # Perform the exists_embeddings_rule call
        exists = config_api.exists_embeddings_rule(guid, embeddings_rule_id)

        # Assert the result is as expected
        assert exists is True


# Test for exists_embeddings_rule when the embeddings_rule does not exist (mocked API)
@pytest.mark.parametrize("error_code", [404, 500])
def test_exists_embeddings_rule_not_found(config_api, guid, error_code):
    # Mock the ApiException
    mock_response = _get_success_mock_response(status=error_code)

    embeddings_rule_id = "invalid_embeddings_rule_id"
    # Mocked API call that raises an exception when the embeddings_rule is not found
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_embeddings_rule:
        mock_embeddings_rule.return_value = mock_response

        exists = config_api.exists_embeddings_rule(guid, embeddings_rule_id)

        # Assert the result is as expected
        assert exists is False


# Test for successful create embeddings_rule using mocked API
def test_create_embeddings_rule_success(config_api, guid):
    new_embeddings_rule = EmbeddingsRule(guid=str(uuid4()), name="Test EmbeddingsRule")
    # Mock the RESTResponse
    mock_response = _get_success_mock_response(
        status=200, data=new_embeddings_rule.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create:
        mock_create.return_value = mock_response

        embeddings_rule = config_api.create_embeddings_rule(
            guid, new_embeddings_rule
        )

        assert embeddings_rule == new_embeddings_rule


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_create_embeddings_rule_api_errors(config_api, guid, error_code, expected_status):
    mock_response = _get_failure_mock_response(expected_status, error_code)
    embeddings_rule_data = {"GUID": str(uuid4()), "Name": "Test EmbeddingsRule"}

    with patch(
        "viewio_sdk.api_client.ApiClient.call_api"
    ) as mock_create_embeddings_rule:
        mock_create_embeddings_rule.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.create_embeddings_rule(
                guid, EmbeddingsRule(**embeddings_rule_data)
            )

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful delete embeddings_rule by GUID using mocked API
def test_delete_embeddings_rule_by_guid_success(config_api, guid):
    embeddings_rule_guid = "guid1"
    new_embeddings_rule = EmbeddingsRule(
        guid=embeddings_rule_guid, name="Test EmbeddingsRule"
    )
    mock_response = _get_success_mock_response(
        status=200, data=new_embeddings_rule.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete:
        mock_delete.return_value = mock_response

        response = config_api.delete_embeddings_rule(guid, embeddings_rule_guid)

        assert response == new_embeddings_rule


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_delete_embeddings_rule_api_errors(config_api, guid, error_code, expected_status):
    embeddings_rule_guid = "invalid-guid"
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch(
        "viewio_sdk.api_client.ApiClient.call_api"
    ) as mock_delete_embeddings_rule:
        mock_delete_embeddings_rule.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.delete_embeddings_rule(guid, embeddings_rule_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve all embedding rules using mocked API
def test_retrieve_embeddings_rules_success(config_api, guid):
    embeddings_rules = [
        EmbeddingsRule(guid=str(uuid4()), name="Embeddings Rule 1"),
        EmbeddingsRule(guid=str(uuid4()), name="Embeddings Rule 2"),
    ]
    # Convert the list of EmbeddingsRule objects to JSON
    embeddings_rules_json = [rule.to_dict() for rule in embeddings_rules]
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(embeddings_rules_json).encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_embeddings_rules(guid)

        assert response == embeddings_rules


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_embeddings_rules_api_errors(config_api, guid, error_code, expected_status):
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_embeddings_rules(guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve embeddings rule using mocked API
def test_retrieve_embeddings_rule_success(config_api, guid):
    rule = EmbeddingsRule(guid=str(uuid4()), name="Test Embeddings Rule")
    # Mocked API response
    mock_response = _get_success_mock_response(
        status=200, data=rule.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_embeddings_rule(guid, rule.guid)

        assert response == rule


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_embeddings_rule_api_errors(config_api, guid, error_code, expected_status):
    rule_guid = str(uuid4())
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve_rule:
        mock_retrieve_rule.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_embeddings_rule(guid, rule_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful update embedding_rule using mocked API
def test_update_embeddings_rule_success(config_api, guid):
    embedding_rule = EmbeddingsRule(guid=str(uuid4()), name="Updated EmbeddingsRule")
    mock_response = _get_success_mock_response(
        status=200, data=embedding_rule.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update:
        mock_update.return_value = mock_response

        response = config_api.update_embeddings_rule(
            guid, embedding_rule.guid, embedding_rule
        )

        assert response == embedding_rule


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_update_embeddings_rule_api_errors(config_api, guid, error_code, expected_status):
    embedding_rule_data = {"GUID": str(uuid4()), "Name": "Updated EmbeddingsRule"}

    embedding_rule = EmbeddingsRule(**embedding_rule_data)
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch(
        "viewio_sdk.api_client.ApiClient.call_api"
    ) as mock_update_embeddings_rule:
        mock_update_embeddings_rule.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.update_embeddings_rule(
                guid, embedding_rule.guid, embedding_rule
            )

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")
