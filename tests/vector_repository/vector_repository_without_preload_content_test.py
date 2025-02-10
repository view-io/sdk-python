"""
    View.IO SDK

    This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

"""  # noqa: E501

import json
from unittest.mock import patch

from uuid import uuid4

import pytest
from viewio_sdk.models.api_error_enum import ApiErrorEnum
from viewio_sdk.models.vector_repository import VectorRepository
from viewio_sdk.rest import ApiException
from ..conftest import _get_success_mock_response, _get_failure_mock_response


# Test for successful exists_vector_repository using mocked API
def test_exists_vector_repository_success(config_api, guid):
    mock_response = _get_success_mock_response(status=200)
    # Mocked API call
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_vector_repository:
        mock_vector_repository.return_value = mock_response

        # Perform the exists_vector_repository call
        exists = config_api.exists_vector_repository_without_preload_content(guid, guid)

        # Assert the result is as expected
        assert exists.status == 200


# Test for exists_vector_repository when the vector_repository does not exist (mocked API)
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_exists_vector_repository_not_found(config_api, guid, error_code, expected_status):
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_vector_repository:
        mock_create_vector_repository.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.exists_vector_repository_without_preload_content(guid, guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful create vector_repository using mocked API
def test_create_vector_repository_success(config_api, guid):
    new_vector_repository = VectorRepository(
        guid=str(uuid4()), name="Test VectorRepository"
    )
    # Mock the RESTResponse
    mock_response = _get_success_mock_response(
        status=200, data=new_vector_repository.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create:
        mock_create.return_value = mock_response

        vector_repository = config_api.create_vector_repository_without_preload_content(
            guid, new_vector_repository
        )

        assert vector_repository.data == new_vector_repository.to_json().encode("utf-8")


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_create_vector_repository_api_errors(config_api, guid, error_code, expected_status):
    mock_response = _get_failure_mock_response(expected_status, error_code)
    vector_repository_data = {"GUID": str(uuid4()), "Name": "Test VectorRepository"}

    with patch(
        "viewio_sdk.api_client.ApiClient.call_api"
    ) as mock_create_vector_repository:
        mock_create_vector_repository.side_effect = ApiException(
            http_resp=mock_response
        )

        with pytest.raises(ApiException) as exc_info:
            config_api.create_vector_repository_without_preload_content(
                guid, VectorRepository(**vector_repository_data)
            )

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful delete vector_repository by GUID using mocked API
def test_delete_vector_repository_by_guid_success(config_api, guid):
    vector_repository_guid = "guid1"
    new_vector_repository = VectorRepository(
        guid=vector_repository_guid, name="Test VectorRepository"
    )
    mock_response = _get_success_mock_response(
        status=200, data=new_vector_repository.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete:
        mock_delete.return_value = mock_response

        response = config_api.delete_vector_repository_without_preload_content(
            guid, vector_repository_guid
        )

        assert response.data == new_vector_repository.to_json().encode("utf-8")


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_delete_vector_repository_api_errors(config_api, guid, error_code, expected_status):
    vector_repository_guid = "invalid-guid"
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch(
        "viewio_sdk.api_client.ApiClient.call_api"
    ) as mock_delete_vector_repository:
        mock_delete_vector_repository.side_effect = ApiException(
            http_resp=mock_response
        )

        with pytest.raises(ApiException) as exc_info:
            config_api.delete_vector_repository_without_preload_content(guid, vector_repository_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve all vector repositories using mocked API
def test_retrieve_vector_repositories_success(config_api, guid):
    vector_repos = [
        VectorRepository(guid=str(uuid4()), name="Repo 1"),
        VectorRepository(guid=str(uuid4()), name="Repo 2"),
    ]
    # Convert the list of VectorRepository objects to JSON
    vector_repos_json = [repo.to_dict() for repo in vector_repos]
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(vector_repos_json).encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_vector_repositories_without_preload_content(guid)

        assert response.data == json.dumps(vector_repos_json).encode("utf-8")


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_vector_repositories_api_errors(
    config_api, guid, error_code, expected_status
):
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_vector_repositories_without_preload_content(guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve vector repository using mocked API
def test_retrieve_vector_repository_success(config_api, guid):
    repo = VectorRepository(guid=str(uuid4()), name="Test Repo")
    # Mocked API response
    mock_response = _get_success_mock_response(
        status=200, data=repo.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_vector_repository_without_preload_content(guid, repo.guid)

        assert response.data == repo.to_json().encode("utf-8")


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_vector_repository_api_errors(config_api, guid, error_code, expected_status):
    repo_guid = str(uuid4())
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve_repo:
        mock_retrieve_repo.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_vector_repository_without_preload_content(guid, repo_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful update vector_repository using mocked API
def test_update_vector_repository_success(config_api, guid):
    vector_repository = VectorRepository(
        guid=str(uuid4()), name="Updated VectorRepository"
    )
    mock_response = _get_success_mock_response(
        status=200, data=vector_repository.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update:
        mock_update.return_value = mock_response

        response = config_api.update_vector_repository_without_preload_content(
            guid, vector_repository.guid, vector_repository
        )

        assert response.data == vector_repository.to_json().encode("utf-8")


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_update_vector_repository_api_errors(config_api, guid, error_code, expected_status):
    vector_repository_data = {"GUID": str(uuid4()), "Name": "Updated VectorRepository"}

    vector_repository = VectorRepository(**vector_repository_data)
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch(
        "viewio_sdk.api_client.ApiClient.call_api"
    ) as mock_update_vector_repository:
        mock_update_vector_repository.side_effect = ApiException(
            http_resp=mock_response
        )

        with pytest.raises(ApiException) as exc_info:
            config_api.update_vector_repository_without_preload_content(
                guid, vector_repository.guid, vector_repository
            )

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")
