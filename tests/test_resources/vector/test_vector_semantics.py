import pytest
from unittest.mock import patch, Mock
from view_sdk.resources.vector.vector_semantics import SemanticCells, SemanticChunks
from view_sdk.models.semantic_cell import SemanticCellModel
from view_sdk.models.semantic_chunk import SemanticChunkModel
from view_sdk.resources.vector import vector_semantics


@pytest.fixture
def mock_get_client():
    with patch("view_sdk.mixins.get_client") as mock_get_client:
        client = Mock()
        mock_get_client.return_value = client
        yield mock_get_client, client


def test_semantic_cells_retrieve(mock_get_client):
    _, client = mock_get_client
    client.request.return_value = {"guid": "cell1"}
    result = SemanticCells.retrieve("repo1", "doc1", "cell1")
    assert isinstance(result, SemanticCellModel)
    assert result.guid == "cell1"


def test_semantic_cells_exists(mock_get_client):
    _, client = mock_get_client
    client.exists.return_value = True
    result = SemanticCells.exists("repo1", "doc1", "cell1")
    assert result is True


def test_semantic_cells_retrieve_all(mock_get_client):
    _, client = mock_get_client
    client.request.return_value = [{"guid": "cell1"}]
    result = SemanticCells.retrieve_all("repo1", "doc1")
    assert isinstance(result, list)
    assert result[0].guid == "cell1"


def test_semantic_chunks_retrieve(mock_get_client):
    _, client = mock_get_client
    client.request.return_value = {"guid": "chunk1"}
    result = SemanticChunks.retrieve("repo1", "doc1", "cell1", "chunk1")
    assert isinstance(result, SemanticChunkModel)
    assert result.guid == "chunk1"


def test_semantic_chunks_exists(mock_get_client):
    _, client = mock_get_client
    client.exists.return_value = True
    result = SemanticChunks.exists("repo1", "doc1", "cell1", "chunk1")
    assert result is True


def test_semantic_chunks_retrieve_all():
    with patch.object(
        vector_semantics.AllRetrievableAPIResource,
        "retrieve_all",
        return_value=[{"guid": "chunk1"}],
    ):
        result = vector_semantics.SemanticChunks.retrieve_all("repo1", "doc1", "cell1")
        assert isinstance(result, list)
        assert result[0]["guid"] == "chunk1"
