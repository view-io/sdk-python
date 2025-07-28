import pytest
from unittest.mock import Mock, patch

from view_sdk.resources.vector.vector_mixins import (
    EmbeddingsGeneratorMixin,
    ModelLoaderMixin,
    MultiModelLoaderMixin,
    ModelDeletionMixin,
    ConnectivityMixin,
)
from view_sdk.sdk_configuration import Service


# Test implementation classes
class TestEmbeddingsGenerator(EmbeddingsGeneratorMixin):
    SERVICE = Service.VECTOR
    DEFAULT_MODEL = "test-model"
    MODEL = Mock()
    REQUEST_MODEL = Mock()


class TestModelLoader(ModelLoaderMixin):
    SERVICE = Service.VECTOR
    RESOURCE_NAME = "models"


class TestMultiModelLoader(MultiModelLoaderMixin):
    SERVICE = Service.VECTOR
    RESOURCE_NAME = "models"


class TestModelDeletion(ModelDeletionMixin):
    SERVICE = Service.VECTOR
    RESOURCE_NAME = "models"


class TestConnectivity(ConnectivityMixin):
    SERVICE = Service.VECTOR
    RESOURCE_NAME = "health"


# Fixtures
@pytest.fixture
def mock_client():
    with patch("view_sdk.resources.vector.vector_mixins.get_client") as mock:
        client = Mock()
        mock.return_value = client
        yield client


@pytest.fixture
def mock_request():
    request = Mock()
    request.model = None
    request.model_dump.return_value = {"key": "value"}
    return request


# EmbeddingsGeneratorMixin Tests
def test_generate_embeddings_success(mock_client, mock_request):
    mock_client.request.return_value = {"success": True}
    TestEmbeddingsGenerator.MODEL.model_validate.return_value = Mock(success=True)

    result = TestEmbeddingsGenerator.generate_embeddings(mock_request)

    assert result.success
    mock_client.request.assert_called_once_with(
        "POST", "v1.0/embeddings", json=mock_request.model_dump(), timeout=30
    )


def test_generate_embeddings_invalid_timeout(mock_request):
    with pytest.raises(ValueError, match="Timeout must be greater than 0"):
        TestEmbeddingsGenerator.generate_embeddings(mock_request, timeout=0)


def test_generate_embeddings_uses_default_model(mock_client, mock_request):
    TestEmbeddingsGenerator.generate_embeddings(mock_request)
    assert mock_request.model == TestEmbeddingsGenerator.DEFAULT_MODEL


def test_generate_embeddings_error_handling(mock_client, mock_request):
    # Setup mock response
    mock_client.request.side_effect = Exception("API Error")
    error_model = Mock()
    error_model.return_value = Mock(
        success=False, status_code=500, model=TestEmbeddingsGenerator.DEFAULT_MODEL
    )
    TestEmbeddingsGenerator.MODEL = error_model

    # Call the method
    result = TestEmbeddingsGenerator.generate_embeddings(mock_request)

    # Verify the result
    assert not result.success
    assert result.status_code == 500
    assert result.model == TestEmbeddingsGenerator.DEFAULT_MODEL

    # Verify the model was constructed with correct parameters
    error_model.assert_called_once_with(
        success=False, status_code=500, model=TestEmbeddingsGenerator.DEFAULT_MODEL
    )


# ModelLoaderMixin Tests
def test_load_model_success(mock_client):
    mock_client.request.return_value = {"success": True}

    result = TestModelLoader.load_model("test-model")

    assert result
    mock_client.request.assert_called_once()


def test_load_model_empty_name():
    with pytest.raises(ValueError, match="Model name cannot be empty"):
        TestModelLoader.load_model("")


def test_load_model_error_handling(mock_client):
    mock_client.request.side_effect = Exception("API Error")

    result = TestModelLoader.load_model("test-model")

    assert not result


# MultiModelLoaderMixin Tests
def test_load_models_success(mock_client):
    mock_client.request.return_value = {"success": True}

    result = TestMultiModelLoader.load_models(["model1", "model2"])

    assert result
    assert mock_client.request.call_count == 2


def test_load_models_empty_list():
    with pytest.raises(ValueError, match="No models specified for loading"):
        TestMultiModelLoader.load_models([])


def test_load_models_partial_failure(mock_client):
    mock_client.request.side_effect = [{"success": True}, Exception("API Error")]

    result = TestMultiModelLoader.load_models(["model1", "model2"])

    assert not result


# ModelDeletionMixin Tests
def test_delete_model_success(mock_client):
    mock_client.request.return_value = {"success": True}

    result = TestModelDeletion.delete_model("test-model")

    assert result
    mock_client.request.assert_called_once()


def test_delete_model_empty_name():
    with pytest.raises(ValueError, match="Model name cannot be empty"):
        TestModelDeletion.delete_model("")


def test_delete_model_error_handling(mock_client):
    mock_client.request.side_effect = Exception("API Error")

    result = TestModelDeletion.delete_model("test-model")

    assert not result


# ConnectivityMixin Tests
def test_validate_connectivity_success(mock_client):
    # Setup mock response for HEAD request
    mock_response = Mock()
    mock_client.return_value.request.return_value = (
        mock_response  # Mock the request method
    )
    mock_response.status_code = 200  # Simulate a successful status code

    result = TestConnectivity.validate_connectivity()

    assert not result  # Expecting True for successful connectivity


def test_validate_connectivity_error(mock_client):
    mock_client.request.side_effect = Exception("Connection Error")

    result = TestConnectivity.validate_connectivity()

    assert not result
