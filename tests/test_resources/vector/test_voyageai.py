# tests/test_resources/vector/test_voyageai.py
import pytest
from unittest.mock import Mock, patch
from view_sdk.resources.vector.voyageai import VoyageAI
from view_sdk.models.voyageai_embeddings_request import VoyageAiEmbeddingsRequest


@pytest.fixture
def mock_client():
    with patch("view_sdk.sdk_configuration.get_client") as mock:
        client = Mock()
        mock.return_value = client
        yield client


@pytest.fixture
def embed_request():
    return VoyageAiEmbeddingsRequest(model="test-model", data=["sample data"])


# # Test cases
# @patch('view_sdk.sdk_configuration.get_client')
# def test_validate_connectivity_success(mock_get_client, mock_client):
#     # Ensure get_client returns the mock client
#     mock_get_client.return_value = mock_client

#     # Set up the mock response for the request method
#     mock_client.request.return_value = Mock(status_code=200)

#     # Call the method under test
#     result = VoyageAI.validate_connectivity()

#     # Assert that the result is True (indicating successful connectivity)
#     assert result is False

#     # Ensure that request was called with the correct parameters
#     mock_client.request.assert_called_once_with("GET", "healthz")


def test_validate_connectivity_failure(mock_client):
    # Set up the mock client to raise an exception
    mock_client.return_value.request.side_effect = Exception("Connection Error")

    # Call the method under test
    result = VoyageAI.validate_connectivity()

    # Assert that the result is False
    assert result is False


def test_generate_embeddings_timeout_error(embed_request):
    # Test for ValueError when timeout is less than 1
    with pytest.raises(ValueError, match="Timeout must be greater than 0"):
        VoyageAI.generate_embeddings(embed_request, timeout=0)


def test_generate_embeddings_uses_default_model(mock_client, embed_request):
    embed_request.model = None  # Simulate no model specified
    VoyageAI.generate_embeddings(embed_request)
    assert embed_request.model == VoyageAI.DEFAULT_MODEL


def test_generate_embeddings_error_handling(mock_client, embed_request):
    # Set up the mock client to raise an exception
    mock_client.return_value.request.side_effect = Exception("API Error")

    # Call the method under test
    result = VoyageAI.generate_embeddings(embed_request)

    # Assert that the result indicates failure
    assert result.success is False
    assert result.status_code == 500
    assert result.model == embed_request.model
