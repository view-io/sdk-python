import pytest
from datetime import datetime, timezone
from unittest.mock import Mock, patch

from view_sdk import models
from view_sdk.models.api_error_response import ApiErrorResponseModel
from view_sdk.models.bucket import BucketMetadataModel
from view_sdk.models.cleanup_request import CleanupRequest
from view_sdk.models.cleanup_response import CleanupResponse
from view_sdk.models.timestamp import TimestampModel
from view_sdk.models.collection import CollectionModel
from view_sdk.models.data_repository import DataRepositoryModel
from view_sdk.models.embeddings_rule import EmbeddingsRuleModel
from view_sdk.models.graph_repository import GraphRepositoryModel
from view_sdk.models.metadata_rule import MetadataRuleModel
from view_sdk.models.object_metadata import ObjectMetadataModel
from view_sdk.models.pool import StoragePool
from view_sdk.models.tenant_metadata import TenantMetadataModel
from view_sdk.models.vector_repository import VectorRepositoryModel
from view_sdk.resources.processor.cleanup import Cleanup
from view_sdk.resources.processor.healthcheck import HealthCheck
from view_sdk.sdk_configuration import SdkConfiguration


@pytest.fixture(scope="module", autouse=True)
def configure_sdk():
    SdkConfiguration.get_instance().configure(
        tenant_guid="test_tenant_guid",
        access_key="test_access_key",
        base_url="http://localhost:8501",  # Using the processor port
        secure=False,
    )


@pytest.fixture(scope="function")
def mock_http_client():
    with patch('httpx.Client') as mock:
        client_instance = Mock()
        mock.return_value = client_instance
        yield client_instance


# @pytest.fixture(scope="function", autouse=True)
# def reset_mocks(mock_http_client):
#     # Reset the mock client before each test
#     mock_http_client.reset_mock()
#     # Reset SdkConfiguration clients
#     SdkConfiguration.get_instance()._clients = {}


@pytest.fixture(scope="function")
def sample_cleanup_response():
    return CleanupResponse(
        success=True,
        guid="test-guid",
        timestamp=TimestampModel(
            created_at=datetime(2023, 1, 1, tzinfo=timezone.utc),
            updated_at=datetime(2023, 1, 1, tzinfo=timezone.utc),
        )
    ).model_dump(mode="json", by_alias=True)


@pytest.fixture(scope="function")
def sample_storage_request():
    return CleanupRequest(
        Object=ObjectMetadataModel(guid="test-object"),
        MetadataRule=MetadataRuleModel(guid="test-rule"),
        Tenant=None,
        Collection=None,
        Pool=None,
        Bucket=None,
        EmbeddingsRule=None,
        VectorRepository=None,
        GraphRepository=None,
    )


@pytest.fixture(scope="function")
def sample_crawler_request():
    return CleanupRequest(
        Object=ObjectMetadataModel(guid="test-object"),
        MetadataRule=MetadataRuleModel(guid="test-rule"),
        Tenant=None,
        Collection=None,
        DataRepository=DataRepositoryModel(guid="test-repo"),
        EmbeddingsRule=None,
        VectorRepository=None,
        GraphRepository=None,
    )


@patch('view_sdk.mixins.get_client')
def test_process_storage_success(mock_get_client, mock_http_client, sample_cleanup_response, sample_storage_request):
    # Configure the mock to return the mock_http_client
    mock_get_client.return_value = mock_http_client

    # Setup mock response
    # mock_response = Mock()
    # mock_response.json.return_value = sample_cleanup_response
    mock_http_client.request.return_value = sample_cleanup_response

    # Call the method
    response = Cleanup.process_storage(
        guid="test-guid",
        tenant=sample_storage_request.tenant,
        collection=sample_storage_request.collection,
        pool=sample_storage_request.pool,
        bucket=sample_storage_request.bucket,
        obj=sample_storage_request.object,
        metadata_rule=sample_storage_request.metadata_rule,
        embeddings_rule=sample_storage_request.embeddings_rule,
        vector_repo=sample_storage_request.vector_repository,
        graph_repo=sample_storage_request.graph_repository,
    )

    # Verify the response
    assert isinstance(response, CleanupResponse)
    assert response.success is True
    assert response.guid == "test-guid"

    # Verify the request
    mock_http_client.request.assert_called_once()
    call_args = mock_http_client.request.call_args
    assert call_args[0][0] == "POST"
    assert "/cleanup" in call_args[0][1]


@patch('view_sdk.mixins.get_client')
def test_process_crawler_success(mock_get_client, mock_http_client, sample_cleanup_response, sample_crawler_request):
    # Configure the mock to return the mock_http_client
    mock_get_client.return_value = mock_http_client

    # Setup mock response
    # mock_response = Mock()
    # mock_response.json.return_value = sample_cleanup_response
    mock_http_client.request.return_value = sample_cleanup_response

    # Call the method
    response = Cleanup.process_crawler(
        guid="test-guid",
        tenant=sample_crawler_request.tenant,
        collection=sample_crawler_request.collection,
        data_repository=sample_crawler_request.data_repository,
        obj=sample_crawler_request.object,
        metadata_rule=sample_crawler_request.metadata_rule,
        embeddings_rule=sample_crawler_request.embeddings_rule,
        vector_repo=sample_crawler_request.vector_repository,
        graph_repo=sample_crawler_request.graph_repository,
    )

    # Verify the response
    assert isinstance(response, CleanupResponse)
    assert response.success is True
    assert response.guid == "test-guid"

    # Verify the request
    mock_http_client.request.assert_called_once()
    call_args = mock_http_client.request.call_args
    assert call_args[0][0] == "POST"
    assert "/cleanup" in call_args[0][1]


@patch('view_sdk.mixins.get_client')
def test_process_storage_with_all_fields(mock_get_client, mock_http_client, sample_cleanup_response):
    # Configure the mock to return the mock_http_client
    mock_get_client.return_value = mock_http_client

    # Setup mock response
    mock_http_client.request.return_value = sample_cleanup_response

    # Create test data with all fields populated
    tenant = TenantMetadataModel(guid="test-tenant")
    collection = CollectionModel(guid="test-collection")
    pool = StoragePool(guid="test-pool")
    bucket = BucketMetadataModel(guid="test-bucket")
    obj = ObjectMetadataModel(guid="test-object")
    metadata_rule = MetadataRuleModel(guid="test-metadata-rule")
    embeddings_rule = EmbeddingsRuleModel(guid="test-embeddings-rule")
    vector_repo = VectorRepositoryModel(guid="test-vector-repo")
    graph_repo = GraphRepositoryModel(guid="test-graph-repo")

    # Call the method
    response = Cleanup.process_storage(
        guid="test-guid",
        tenant=tenant,
        collection=collection,
        pool=pool,
        bucket=bucket,
        obj=obj,
        metadata_rule=metadata_rule,
        embeddings_rule=embeddings_rule,
        vector_repo=vector_repo,
        graph_repo=graph_repo,
    )

    # Verify the response
    assert isinstance(response, CleanupResponse)
    assert response.success is True
    assert response.guid == "test-guid"

    # Verify the request
    mock_http_client.request.assert_called_once()
    call_args = mock_http_client.request.call_args
    assert call_args[0][0] == "POST"
    assert "/cleanup" in call_args[0][1]


@patch('view_sdk.mixins.get_client')
def test_error_handling(mock_get_client, mock_http_client, sample_storage_request):
    # Configure the mock to return the mock_http_client
    mock_get_client.return_value = mock_http_client

    # Setup mock error response
    error_response = {
        "Success": False,
        "StatusCode": 400,
        "Error": {
            "Error": "BadRequest",
            "Context": "Invalid request parameters",
            "Description": "Missing required field"
        }
    }
    mock_http_client.request.return_value = error_response

    # Call the method and verify error handling
    response = Cleanup.process_storage(
        guid="test-guid",
        tenant=sample_storage_request.tenant,
        collection=sample_storage_request.collection,
        pool=sample_storage_request.pool,
        bucket=sample_storage_request.bucket,
        obj=sample_storage_request.object,
        metadata_rule=sample_storage_request.metadata_rule,
        embeddings_rule=sample_storage_request.embeddings_rule,
        vector_repo=sample_storage_request.vector_repository,
        graph_repo=sample_storage_request.graph_repository,
    )

    # Verify error response
    assert isinstance(response, CleanupResponse)
    assert response.success is False
    assert response.error is not None
    assert isinstance(response.error, ApiErrorResponseModel)
    assert response.error.error == "BadRequest"
    assert response.error.context == "Invalid request parameters"
    assert response.error.description == "Missing required field"
