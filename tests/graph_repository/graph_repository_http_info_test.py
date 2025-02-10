"""
    View.IO SDK

    This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

"""  # noqa: E501

import json
from unittest.mock import patch

from uuid import uuid4

import pytest
from viewio_sdk.models.api_error_enum import ApiErrorEnum
from viewio_sdk.models.graph_repository import GraphRepository
from viewio_sdk.rest import ApiException
from ..conftest import _get_success_mock_response, _get_failure_mock_response


# Test for successful exists_graph_repository using mocked API
def test_exists_graph_repository_success(config_api, guid):
    mock_response = _get_success_mock_response(status=200)
    # Mocked API call
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_graph_repository:
        mock_graph_repository.return_value = mock_response

        # Perform the exists_graph_repository call
        exists = config_api.exists_graph_repository_with_http_info(guid, guid)

        # Assert the result is as expected
        assert exists.status_code == 200


# Test for exists_graph_repository when the graph_repository does not exist (mocked API)
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_exists_graph_repository_not_found(config_api, guid, error_code, expected_status):
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_graph_repository:
        mock_create_graph_repository.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.exists_graph_repository_with_http_info(guid, guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful create graph_repository using mocked API
def test_create_graph_repository_success(config_api, guid):
    new_graph_repository = GraphRepository(
        guid=str(uuid4()), name="Test GraphRepository"
    )
    # Mock the RESTResponse
    mock_response = _get_success_mock_response(
        status=200, data=new_graph_repository.to_json().encode("utf-8")
    )
    mock_response.data = new_graph_repository.to_json().encode(
        "utf-8"
    )  # Mocked response data in bytes

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create:
        mock_create.return_value = mock_response

        graph_repository = config_api.create_graph_repository_with_http_info(
            guid, new_graph_repository
        )

        assert graph_repository.data == new_graph_repository


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_create_graph_repository_api_errors(config_api, guid, error_code, expected_status):
    mock_response = _get_failure_mock_response(expected_status, error_code)
    graph_repository_data = {"GUID": str(uuid4()), "Name": "Test GraphRepository"}

    with patch(
        "viewio_sdk.api_client.ApiClient.call_api"
    ) as mock_create_graph_repository:
        mock_create_graph_repository.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.create_graph_repository_with_http_info(
                guid, GraphRepository(**graph_repository_data)
            )

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful delete graph_repository by GUID using mocked API
def test_delete_graph_repository_by_guid_success(config_api, guid):
    graph_repository_guid = "guid1"
    new_graph_repository = GraphRepository(
        guid=graph_repository_guid, name="Test GraphRepository"
    )
    mock_response = _get_success_mock_response(
        status=200, data=new_graph_repository.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete:
        mock_delete.return_value = mock_response

        response = config_api.delete_graph_repository_with_http_info(
            guid, graph_repository_guid
        )

        assert response.data == new_graph_repository


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_delete_graph_repository_api_errors(config_api, guid, error_code, expected_status):
    graph_repository_guid = "invalid-guid"
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch(
        "viewio_sdk.api_client.ApiClient.call_api"
    ) as mock_delete_graph_repository:
        mock_delete_graph_repository.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.delete_graph_repository_with_http_info(guid, graph_repository_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve all graph repositories using mocked API
def test_retrieve_graph_repositories_success(config_api, guid):
    graph_repos = [
        GraphRepository(guid=str(uuid4()), name="Graph Repo 1"),
        GraphRepository(guid=str(uuid4()), name="Graph Repo 2"),
    ]
    # Convert the list of GraphRepository objects to JSON
    graph_repos_json = [repo.to_dict() for repo in graph_repos]
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(graph_repos_json).encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_graph_repositories_with_http_info(guid)

        assert response.data == graph_repos


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_graph_repositories_api_errors(
    config_api, guid, error_code, expected_status
):
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_graph_repositories_with_http_info(guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve graph repository using mocked API
def test_retrieve_graph_repository_success(config_api, guid):
    repo = GraphRepository(guid=str(uuid4()), name="Test Graph Repo")
    # Mocked API response
    mock_response = _get_success_mock_response(
        status=200, data=repo.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_graph_repository_with_http_info(guid, repo.guid)

        assert response.data == repo


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_graph_repository_api_errors(config_api, guid, error_code, expected_status):
    repo_guid = str(uuid4())
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve_repo:
        mock_retrieve_repo.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_graph_repository_with_http_info(guid, repo_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful update graph_repository using mocked API
def test_update_graph_repository_success(config_api, guid):
    graph_repository = GraphRepository(
        guid=str(uuid4()), name="Updated GraphRepository"
    )
    mock_response = _get_success_mock_response(
        status=200, data=graph_repository.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update:
        mock_update.return_value = mock_response

        response = config_api.update_graph_repository_with_http_info(
            guid, graph_repository.guid, graph_repository
        )

        assert response.data == graph_repository


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_update_graph_repository_api_errors(config_api, guid, error_code, expected_status):
    graph_repository_data = {"GUID": str(uuid4()), "Name": "Updated GraphRepository"}

    graph_repository = GraphRepository(**graph_repository_data)
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch(
        "viewio_sdk.api_client.ApiClient.call_api"
    ) as mock_update_graph_repository:
        mock_update_graph_repository.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.update_graph_repository_with_http_info(
                guid, graph_repository.guid, graph_repository
            )

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


