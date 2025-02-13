import pytest
from unittest.mock import Mock, patch
from view_sdk.models.semantic_cell import SemanticCellModel
from view_sdk.models.semantic_chunk import SemanticChunkModel
from view_sdk.resources.vector.embeddings import Embeddings, EmbeddingsGeneratorEnum
from view_sdk.sdk_configuration import SdkConfiguration

@pytest.fixture(scope="module", autouse=True)
def configure_sdk():
    SdkConfiguration.get_instance().configure(
        tenant_guid="test_tenant_guid",
        access_key="test_access_key",
        base_url="http://localhost:8301",
        secure=False
    )

@pytest.fixture(scope="function")
def mock_http_client():
    with patch('httpx.Client') as mock:
        client_instance = Mock()
        mock.return_value = client_instance
        yield client_instance

@pytest.fixture(scope="function", autouse=True)
def reset_mocks(mock_http_client):
    # Reset the mock client before each test
    mock_http_client.reset_mock()
    # Reset Embeddings class variables
    Embeddings._generator = None
    Embeddings._api_key = None
    Embeddings._endpoint = None
    Embeddings._sdk_base = None
    Embeddings._semaphore = None
    Embeddings.BATCH_SIZE = 16
    Embeddings.MAX_PARALLEL_TASKS = 16
    Embeddings.MAX_RETRIES = 3
    Embeddings.MAX_FAILURES = 3
    Embeddings.TIMEOUT = 300
    # Reset SdkConfiguration clients
    SdkConfiguration.get_instance()._clients = {}

@pytest.fixture
def sample_semantic_cells():
    chunks = [SemanticChunkModel(
        id="chunk-1",
        text="Test content",
        content="Test content"
    )]
    return [SemanticCellModel(id="cell-1", chunks=chunks)]

def test_configure_valid_generator():
    # Test configuration with each generator type
    for generator in EmbeddingsGeneratorEnum:
        Embeddings.configure(
            generator=generator,
            endpoint="http://test-endpoint",
            api_key="test-api-key"
        )

        # Verify the SDK was initialized with correct type
        assert Embeddings._generator == generator
        assert Embeddings._api_key == "test-api-key"
        assert Embeddings._endpoint == "http://test-endpoint"

def test_configure_invalid_generator():
    with pytest.raises(ValueError, match="Unknown embeddings generator"):
        Embeddings.configure(
            generator="InvalidGenerator",
            endpoint="http://test-endpoint",
            api_key="test-api-key"
        )

def test_process_semantic_cells_empty_input():
    result = Embeddings.process_semantic_cells([], "test-model")
    assert result == []

@patch('view_sdk.sdk_configuration.get_client')
def test_process_semantic_cells(mock_get_client, mock_http_client, sample_semantic_cells):
    # Configure the mock to return the mock_http_client
    mock_get_client.return_value = mock_http_client

    # Configure embeddings
    Embeddings.configure(
        generator=EmbeddingsGeneratorEnum.LCProxy,
        endpoint="http://test-endpoint",
        api_key="test-api-key"
    )

    # Mock HTTP response
    mock_response = Mock()
    mock_response.json.return_value = {
        "Success": True,
        "StatusCode": 200,
        "Model": "test-model",
        "Contents": ["Test content"],
        "Embeddings": [[0.1, 0.2, 0.3]]
    }
    mock_http_client.request.return_value = mock_response

    # Process cells
    result = Embeddings.process_semantic_cells(sample_semantic_cells, "test-model")

    # Verify results
    assert len(result) == 1
    assert result[0].chunks[0].embeddings == [0.1, 0.2, 0.3]
    mock_http_client.request.assert_called_once()

@patch('view_sdk.sdk_configuration.get_client')
def test_process_semantic_cells_batch_handling(mock_get_client, mock_http_client):
    # Configure the mock to return the mock_http_client
    mock_get_client.return_value = mock_http_client

    # Create multiple cells to test batching
    chunks = [
        SemanticChunkModel(
            id=f"chunk-{i}",
            text=f"text-{i}",
            content=f"content-{i}"
        ) for i in range(20)
    ]
    cells = [SemanticCellModel(id="cell-1", chunks=chunks)]

    # Mock HTTP response
    def request_handler(*args, **kwargs):
        contents = kwargs.get('json', {}).get('Contents', [])
        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "Success": True,
            "StatusCode": 200,
            "Model": "test-model",
            "Contents": contents,
            "Embeddings": [[0.1, 0.2, 0.3]] * len(contents)
        }
        return response

    mock_http_client.request.side_effect = request_handler

    # Configure embeddings with batch_size=8
    Embeddings.configure(
        generator=EmbeddingsGeneratorEnum.LCProxy,
        endpoint="http://test-endpoint",
        api_key="test-api-key",
        batch_size=8
    )

    # Process cells
    result = Embeddings.process_semantic_cells(cells, "test-model")

    # Verify batching (20 chunks / 8 batch size = 3 calls)
    assert mock_http_client.request.call_count == 3
    assert all(chunk.embeddings == [0.1, 0.2, 0.3] for chunk in chunks)

@patch('view_sdk.sdk_configuration.get_client')
def test_process_semantic_cells_failure_handling(mock_get_client, mock_http_client, sample_semantic_cells):
    # Configure the mock to return the mock_http_client
    mock_get_client.return_value = mock_http_client

    # Configure embeddings with max_failures=1
    Embeddings.configure(
        generator=EmbeddingsGeneratorEnum.LCProxy,
        endpoint="http://test-endpoint",
        api_key="test-api-key",
        max_failures=1
    )

    def request_handler(*args, **kwargs):
        raise Exception("API Error")

    mock_http_client.request.side_effect = request_handler

    # Verify that it raises error after max failures
    with pytest.raises(RuntimeError, match="Too many failures encountered"):
        Embeddings.process_semantic_cells(sample_semantic_cells, "test-model")
