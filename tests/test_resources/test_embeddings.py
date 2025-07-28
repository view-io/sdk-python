import pytest
from unittest.mock import patch, Mock
from view_sdk.resources.embeddings.generate_embeddings import GenerateEmbeddings
from view_sdk.resources.embeddings.healthcheck import HealthCheck


@pytest.fixture
def mock_client():
    with patch("view_sdk.mixins.get_client") as mock:
        client = Mock()
        mock.return_value = client
        yield client


def test_generate_embeddings(mock_client):
    """Test generating embeddings."""
    test_data = {"text": "test text", "model": "text-embedding-ada-002"}
    expected_response = {
        "embedding": [0.1, 0.2, 0.3],
        "text": "test text",
        "model": "text-embedding-ada-002",
    }

    mock_client.request.return_value = expected_response

    result = GenerateEmbeddings.generate(**test_data)

    mock_client.request.assert_called_once()
    assert result == expected_response


def test_embeddings_healthcheck_success(mock_client):
    """Test successful health check for embeddings service."""
    mock_client.request.return_value = None

    result = HealthCheck.check()

    assert result is True
    mock_client.request.assert_called_once()


def test_embeddings_healthcheck_failure(mock_client):
    """Test failed health check for embeddings service."""
    mock_client.request.side_effect = Exception("Service unavailable")

    result = HealthCheck.check()

    assert result is False
    mock_client.request.assert_called_once()


def test_preload_models(mock_client):
    """Test preloading models."""
    from view_sdk.resources.embeddings.preload_models import PreloadModels

    test_data = {"models": ["text-embedding-ada-002"]}
    expected_response = {
        "status": "success",
        "loaded_models": ["text-embedding-ada-002"],
    }

    mock_client.request.return_value = expected_response

    result = PreloadModels.load(**test_data)

    mock_client.request.assert_called_once()
    assert result == expected_response
