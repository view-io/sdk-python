"""
    View.IO SDK

    This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

"""  # noqa: E501

import json
from unittest.mock import patch

from uuid import uuid4

import pytest
from viewio_sdk.models.api_error_enum import ApiErrorEnum
from viewio_sdk.models.data_repository import DataRepository
from viewio_sdk.rest import ApiException
from ..conftest import _get_success_mock_response, _get_failure_mock_response


# Test for successful create data_repository using mocked API
def test_create_data_repository_success(config_api, guid):
    new_data_repository = DataRepository(
        id=1, guid=str(uuid4()), name="Test DataRepository"
    )
    # Mock the RESTResponse
    mock_response = _get_success_mock_response(
        status=200, data=new_data_repository.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create:
        mock_create.return_value = mock_response

        data_repository = config_api.create_data_repository_with_http_info(
            guid, new_data_repository
        )

        assert data_repository.data == new_data_repository


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_create_data_repository_api_errors(config_api, guid, error_code, expected_status):
    mock_response = _get_failure_mock_response(expected_status, error_code)
    data_repository_data = {"GUID": str(uuid4()), "Name": "Test DataRepository"}

    with patch(
        "viewio_sdk.api_client.ApiClient.call_api"
    ) as mock_create_data_repository:
        mock_create_data_repository.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.create_data_repository_with_http_info(
                guid, DataRepository(**data_repository_data)
            )

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful delete data_repository by GUID using mocked API
def test_delete_data_repository_by_guid_success(config_api, guid):
    data_repository_guid = "guid1"
    new_data_repository = DataRepository(
        id=1, guid=data_repository_guid, name="Test Data Repository"
    )
    mock_response = _get_success_mock_response(
        status=200, data=new_data_repository.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete:
        mock_delete.return_value = mock_response

        response = config_api.delete_data_repository_with_http_info(guid, data_repository_guid)

        assert response.data == new_data_repository


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_delete_data_repository_api_errors(config_api, guid, error_code, expected_status):
    data_repository_guid = "invalid-guid"
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch(
        "viewio_sdk.api_client.ApiClient.call_api"
    ) as mock_delete_data_repository:
        mock_delete_data_repository.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.delete_data_repository_with_http_info(guid, data_repository_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve all data repositories using mocked API
def test_retrieve_data_repositories_success(config_api, guid):
    data_repos = [
        DataRepository(id=1, guid=str(uuid4()), name="Data Repo 1"),
        DataRepository(id=2, guid=str(uuid4()), name="Data Repo 2"),
    ]
    # Convert the list of DataRepository objects to JSON
    data_repos_json = [data_repo.to_dict() for data_repo in data_repos]
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(data_repos_json).encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_data_repositories_with_http_info(guid)

        assert response.data == data_repos


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_data_repositories_api_errors(config_api, guid, error_code, expected_status):
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_data_repositories_with_http_info(guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve data repository using mocked API
def test_retrieve_data_repository_success(config_api, guid):
    repo = DataRepository(id=1, guid=str(uuid4()), name="Test Data Repo")
    mock_response = _get_success_mock_response(
        status=200, data=repo.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_data_repository_with_http_info(guid, repo.guid)

        assert response.data == repo


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_data_repository_api_errors(config_api, guid, error_code, expected_status):
    repo_guid = str(uuid4())

    mock_response = _get_failure_mock_response(
        expected_status=expected_status, error_code=error_code
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve_repo:
        mock_retrieve_repo.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_data_repository_with_http_info(guid, repo_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")
