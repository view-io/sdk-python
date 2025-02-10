"""
    View.IO SDK

    This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

"""  # noqa: E501

import json
from unittest.mock import patch

from uuid import uuid4

import pytest
from viewio_sdk.models.api_error_enum import ApiErrorEnum
from viewio_sdk.models.bucket_metadata import BucketMetadata
from viewio_sdk.rest import ApiException
from ..conftest import _get_success_mock_response, _get_failure_mock_response


# Test for successful exists_bucket using mocked API
def test_exists_bucket_success(config_api, guid):
    mock_response = _get_success_mock_response(status=200)
    # Mocked API call
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_bucket:
        mock_bucket.return_value = mock_response

        # Perform the exists_bucket call
        exists = config_api.exists_bucket_with_http_info(guid, guid)

        # Assert the result is as expected
        assert exists.status_code == 200


# Test for exists_bucket when the bucket does not exist (mocked API)
@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_exists_bucket_not_found(config_api, guid, error_code, expected_status):
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_bucket:
        mock_create_bucket.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.exists_bucket_with_http_info(guid, guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful create bucket using mocked API
def test_create_bucket_success(config_api, guid):
    new_bucket = BucketMetadata(guid=str(uuid4()), name="Test Bucket")
    # Mock the RESTResponse
    mock_response = _get_success_mock_response(
        status=200, data=new_bucket.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create:
        mock_create.return_value = mock_response

        # Call the actual function
        bucket = config_api.create_bucket_with_http_info(guid, new_bucket)

        assert bucket.data == new_bucket


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_create_bucket_api_errors(config_api, guid, error_code, expected_status):
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)
    bucket_data = {"GUID": str(uuid4()), "Name": "Test Bucket"}

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_create_bucket:
        mock_create_bucket.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.create_bucket_with_http_info(guid, BucketMetadata(**bucket_data))

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful delete bucket by GUID using mocked API
def test_delete_bucket_by_guid_success(config_api, guid):
    bucket_guid = "guid1"
    new_bucket = BucketMetadata(guid=bucket_guid, name="Test Bucket")
    mock_response = _get_success_mock_response(
        status=200, data=new_bucket.to_json().encode("utf-8")
    )

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete:
        mock_delete.return_value = mock_response

        response = config_api.delete_bucket_with_http_info(guid, bucket_guid)

        assert response.data == new_bucket


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_delete_bucket_api_errors(config_api, guid, error_code, expected_status):
    bucket_guid = "invalid-guid"
    # Mock the ApiException
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_delete_bucket:
        mock_delete_bucket.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.delete_bucket_with_http_info(guid, bucket_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve all buckets using mocked API
def test_retrieve_buckets_success(config_api, guid):
    buckets = [
        BucketMetadata(guid=str(uuid4()), name="Bucket 1"),
        BucketMetadata(guid=str(uuid4()), name="Bucket 2"),
    ]
    # Convert the list of BucketMetadata objects to JSON
    buckets_json = [bucket.to_dict() for bucket in buckets]
    mock_response = _get_success_mock_response(
        status=200, data=json.dumps(buckets_json).encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_buckets_with_http_info(guid)

        assert response.data == buckets


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_buckets_api_errors(config_api, guid, error_code, expected_status):
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_buckets_with_http_info(guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for retrieve bucket using mocked API
def test_retrieve_bucket_success(config_api, guid):
    bucket = BucketMetadata(guid=str(uuid4()), name="Test Bucket")
    # Mocked API response
    mock_response = _get_success_mock_response(
        status=200, data=bucket.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve:
        mock_retrieve.return_value = mock_response

        response = config_api.retrieve_bucket_with_http_info(guid, bucket.guid)

        assert response.data == bucket


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_retrieve_bucket_api_errors(config_api, guid, error_code, expected_status):
    bucket_guid = str(uuid4())
    # Mocked API response
    mock_response = _get_failure_mock_response(expected_status, error_code)

    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_retrieve_bucket:
        mock_retrieve_bucket.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.retrieve_bucket_with_http_info(guid, bucket_guid)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")


# Test for successful update bucket using mocked API
def test_update_bucket_success(config_api, guid):
    bucket = BucketMetadata(guid=str(uuid4()), name="Updated Bucket")
    mock_response = _get_success_mock_response(
        status=200, data=bucket.to_json().encode("utf-8")
    )
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update:
        mock_update.return_value = mock_response

        response = config_api.update_bucket_with_http_info(guid, bucket.guid, bucket)

        assert response.data == bucket


@pytest.mark.parametrize(
    "error_code, expected_status",
    [
        (ApiErrorEnum.NOTFOUND, 404),
        (ApiErrorEnum.BADREQUEST, 400),
        (ApiErrorEnum.CONFLICT, 409),
        (ApiErrorEnum.INTERNALERROR, 500),
    ],
)
def test_update_bucket_api_errors(config_api, guid, error_code, expected_status):
    bucket_data = {"GUID": str(uuid4()), "Name": "Updated Bucket"}

    bucket = BucketMetadata(**bucket_data)
    mock_response = _get_failure_mock_response(expected_status, error_code)
    with patch("viewio_sdk.api_client.ApiClient.call_api") as mock_update_bucket:
        mock_update_bucket.side_effect = ApiException(http_resp=mock_response)

        with pytest.raises(ApiException) as exc_info:
            config_api.update_bucket_with_http_info(guid, bucket.guid, bucket)

        assert exc_info.value.status == expected_status
        assert exc_info.value.reason == error_code.name
        assert exc_info.value.body == mock_response.data.decode("utf-8")
