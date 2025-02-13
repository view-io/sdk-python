import pytest
from unittest.mock import patch, Mock
from typing import List
from view_sdk.resources.vector.vector_documents import Documents
from view_sdk.resources.vector.vector_repositories import Repositories
from view_sdk.resources.vector.vector_semantics import SemanticCells, SemanticChunks
from view_sdk.resources.vector.vector_search import Search
from view_sdk.resources.vector.healthcheck import HealthCheck
from view_sdk.models.embeddings_document import EmbeddingsDocumentModel
from view_sdk.models.enumeration_result import EnumerationResultModel
from view_sdk.models.vector_repository_statistics import VectorRepositoryStatisticsModel
from view_sdk.models.find_embeddings_result import FindEmbeddingsResultModel
from view_sdk.models.vector_chunk import VectorChunkModel
from view_sdk.models.semantic_cell import SemanticCellModel
from view_sdk.models.semantic_chunk import SemanticChunkModel
from view_sdk.sdk_configuration import SdkConfiguration

@pytest.fixture(scope="module", autouse=True)
def configure_sdk():
    SdkConfiguration.get_instance().configure(
        tenant_guid="test_tenant_guid",
        access_key="test_access_key",
        base_url="http://localhost",
        secure=False
    )

@pytest.fixture(scope="function")
def mock_httpx_client():
    with patch('httpx.Client') as mock:
        client_instance = Mock()
        mock.return_value = client_instance
        yield client_instance

@pytest.fixture
def mock_http_response():
    def _response(status_code=200, json_data=None):
        mock_response = Mock()
        mock_response.status_code = status_code
        mock_response.json.return_value = json_data or {}
        return mock_response
    return _response

@pytest.fixture
def initialize_models():
    return {
        "statistics": VectorRepositoryStatisticsModel(DocumentCount=10, TotalBytes=10, CellCount=10, ChunkCount=10),
        "enumeration": EnumerationResultModel(success=True, objects=[], total_records=0),
        "search": VectorChunkModel(id="1", content="test content", metadata={}, vector=[1.0, 2.0]),
    }

# Test Vector Documents
def test_write_document(mock_httpx_client):
    mock_response = Mock()
    doc_data = {
        "tenant_guid": "test-tenant",
        "vector_repository_guid": "test-repo",
        "content": "test content"
    }
    mock_response.json.return_value = doc_data
    mock_response.status_code = 200
    mock_httpx_client.request.return_value = mock_response

    result = Documents.write(**doc_data)
    assert isinstance(result, EmbeddingsDocumentModel)
    assert result.content == "test content"

def test_delete_document_by_filter(mock_httpx_client):
    mock_response = Mock()
    mock_response.status_code = 204
    mock_httpx_client.request.return_value = mock_response

    result = Documents.delete_by_filter(repo_guid="test-repo", filter_key="test-filter")
    assert result is True

# Test Vector Repositories
def test_enumerate_documents(mock_httpx_client):
    mock_response = Mock()
    mock_response.json.return_value = {
        "success": True,
        "objects": [],
        "total_records": 0
    }
    mock_response.status_code = 200
    mock_httpx_client.request.return_value = mock_response

    result = Repositories.enumerate_documents("test-repo")
    assert isinstance(result, EnumerationResultModel)
    assert result.success is True

def test_get_repository_statistics(mock_httpx_client, initialize_models):

    mock_httpx_client.request.return_value = initialize_models["statistics"].model_dump(by_alias=True)

    with patch('view_sdk.resources.vector.vector_repositories.get_client') as mock_get_client:
        mock_get_client.return_value = mock_httpx_client
        result = Repositories.get_statistics("test-repo")

    assert isinstance(result, VectorRepositoryStatisticsModel)
    assert result.document_count == 10

# Test Vector Search
def test_vector_search(mock_httpx_client, initialize_models, mock_http_response):
    mock_httpx_client.request.return_value = [initialize_models["search"].model_dump(by_alias=True)]

    search_params = {
        "vector_repository_guid": "test-repo",
        "embeddings": [0.1, 0.2, 0.3]
    }

    with patch('view_sdk.resources.vector.vector_search.get_client') as mock_get_client:
        mock_get_client.return_value = mock_httpx_client
        result = Search.search(**search_params)

    assert isinstance(result, list)
    assert all(isinstance(item, VectorChunkModel) for item in result)

def test_find_embeddings(mock_httpx_client):
    mock_response = Mock()
    mock_response.json.return_value = {
        "timestamp": {},
        "existing": [],
        "missing": []
    }
    mock_response.status_code = 200
    mock_httpx_client.request.return_value = mock_response

    find_params = {
        "vector_repository_guid": "test-repo",
        "criteria": []
    }
    result = Search.find_embeddings(**find_params)
    assert isinstance(result, FindEmbeddingsResultModel)

# Test Vector Semantics
def test_semantic_cells_retrieve(mock_httpx_client):
    mock_httpx_client.request.return_value = SemanticCellModel(guid="test-cell").model_dump(by_alias=True)
    with patch('view_sdk.mixins.get_client') as mock_get_client:
        mock_get_client.return_value = mock_httpx_client
        result = SemanticCells.read(doc_guid="test-doc", repo_guid="test-repo", cell_guid="test-cell")
    assert isinstance(result, SemanticCellModel)
    assert result.guid == "test-cell"

def test_semantic_chunks_retrieve(mock_httpx_client):
    mock_httpx_client.request.return_value = SemanticChunkModel(guid="test-chunk").model_dump(by_alias=True)
    with patch('view_sdk.mixins.get_client') as mock_get_client:
        mock_get_client.return_value = mock_httpx_client
        result = SemanticChunks.read(cell_guid="test-cell", doc_guid="test-doc", repo_guid="test-repo")
    assert isinstance(result, SemanticChunkModel)
    assert result.guid == "test-chunk"
