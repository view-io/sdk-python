from unittest.mock import patch, MagicMock
import pytest
from view_sdk.resources.configuration.model_endpoints import ModelEndpoint
from view_sdk.models.model_endpoint_model import ModelEndpointModel
from view_sdk.enums.model_api_type_enum import ModelApiTypeEnum


@patch("view_sdk.mixins.get_client")
@patch("view_sdk.models.model_endpoint_model.ModelEndpointModel.model_validate")
def test_create_model_endpoint(mock_model_validate, mock_get_client):
    """Test creating a model endpoint."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {"GUID": "test-guid", "Name": "Test Endpoint"}
    mock_model_validate.return_value = ModelEndpointModel(guid="test-guid", name="Test Endpoint")
    
    result = ModelEndpoint.create(
        name="Test Endpoint",
        endpoint_url="https://api.example.com/",
        api_type=ModelApiTypeEnum.OpenAi
    )
    
    assert result.guid == "test-guid"
    assert result.name == "Test Endpoint"
    mock_client.request.assert_called_once()
    mock_model_validate.assert_called_once()


@patch("view_sdk.mixins.get_client")
@patch("view_sdk.models.model_endpoint_model.ModelEndpointModel.model_validate")
def test_retrieve_model_endpoint(mock_model_validate, mock_get_client):
    """Test retrieving a model endpoint by GUID."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {"GUID": "test-guid", "Name": "Test Endpoint"}
    mock_model_validate.return_value = ModelEndpointModel(guid="test-guid", name="Test Endpoint")
    
    result = ModelEndpoint.retrieve("test-guid")
    
    assert result.guid == "test-guid"
    assert result.name == "Test Endpoint"
    mock_client.request.assert_called_once()
    mock_model_validate.assert_called_once()


@patch("view_sdk.mixins.get_client")
@patch("view_sdk.models.model_endpoint_model.ModelEndpointModel.model_validate")
def test_retrieve_all_model_endpoints(mock_model_validate, mock_get_client):
    """Test retrieving all model endpoints."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = [
        {"GUID": "guid1", "Name": "Endpoint 1"},
        {"GUID": "guid2", "Name": "Endpoint 2"}
    ]
    mock_model_validate.side_effect = lambda data: ModelEndpointModel(**data)
    
    result = ModelEndpoint.retrieve_all()
    
    assert len(result) == 2
    assert result[0].guid == "guid1"
    assert result[1].guid == "guid2"
    mock_client.request.assert_called_once()
    assert mock_model_validate.call_count == 2


@patch("view_sdk.mixins.get_client")
@patch("view_sdk.models.model_endpoint_model.ModelEndpointModel.model_validate")
def test_update_model_endpoint(mock_model_validate, mock_get_client):
    """Test updating a model endpoint."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {"GUID": "test-guid", "Name": "Updated Endpoint"}
    mock_model_validate.return_value = ModelEndpointModel(guid="test-guid", name="Updated Endpoint")
    
    result = ModelEndpoint.update(
        "test-guid",
        name="Updated Endpoint",
        timeout_ms=60000
    )
    
    assert result.guid == "test-guid"
    assert result.name == "Updated Endpoint"
    mock_client.request.assert_called_once()
    mock_model_validate.assert_called_once()


@patch("view_sdk.mixins.get_client")
def test_delete_model_endpoint(mock_get_client):
    """Test deleting a model endpoint."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = None
    
    result = ModelEndpoint.delete("test-guid")
    
    assert result is True
    mock_client.request.assert_called_once()


@patch("view_sdk.mixins.get_client")
def test_exists_model_endpoint(mock_get_client):
    """Test checking if a model endpoint exists."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = True
    
    result = ModelEndpoint.exists("test-guid")
    
    assert result is True
    mock_client.request.assert_called_once()


@patch("view_sdk.mixins.get_client")
@patch("view_sdk.models.model_endpoint_model.ModelEndpointModel.model_validate")
def test_enumerate_model_endpoints(mock_model_validate, mock_get_client):
    """Test enumerating model endpoints with pagination."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {
        "Objects": [
            {"GUID": "guid1", "Name": "Endpoint 1"},
            {"GUID": "guid2", "Name": "Endpoint 2"}
        ],
        "TotalRecords": 2,
        "Skip": 0,
        "MaxResults": 10
    }
    mock_model_validate.side_effect = lambda data: ModelEndpointModel(**data)
    
    result = ModelEndpoint.enumerate(page=1, page_size=10)
    
    assert len(result.objects) == 2
    assert result.total_records == 2
    assert result.skip == 0
    assert result.max_results == 10
    mock_client.request.assert_called_once()


@patch("view_sdk.mixins.get_client")
@patch("view_sdk.models.model_endpoint_model.ModelEndpointModel.model_validate")
def test_create_model_endpoint_with_validation(mock_model_validate, mock_get_client):
    """Test creating a model endpoint with field validation."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {"GUID": "test-guid"}
    
    # Test with invalid timeout (should raise validation error)
    with patch.object(ModelEndpointModel, '__init__', side_effect=ValueError("TimeoutMs must be greater than 1000")):
        with pytest.raises(ValueError, match="TimeoutMs must be greater than 1000"):
            ModelEndpoint.create(timeout_ms=500)
    
    # Test with valid data
    mock_model_validate.return_value = ModelEndpointModel(
        guid="test-guid",
        name="Test Endpoint",
        endpoint_url="https://api.example.com/",
        api_type=ModelApiTypeEnum.OpenAi,
        timeout_ms=30000
    )
    
    result = ModelEndpoint.create(
        name="Test Endpoint",
        endpoint_url="https://api.example.com/",
        api_type=ModelApiTypeEnum.OpenAi,
        timeout_ms=30000
    )
    
    assert result.guid == "test-guid"
    assert result.name == "Test Endpoint"
    assert result.endpoint_url == "https://api.example.com/"
    assert result.api_type == ModelApiTypeEnum.OpenAi
    assert result.timeout_ms == 30000


@patch("view_sdk.mixins.get_client")
@patch("view_sdk.models.model_endpoint_model.ModelEndpointModel.model_validate")
def test_retrieve_model_endpoint_with_alias(mock_model_validate, mock_get_client):
    """Test retrieving a model endpoint using alias fields."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {
        "GUID": "test-guid",
        "Name": "Test Endpoint",
        "EndpointUrl": "https://api.example.com/",
        "ApiType": "OpenAi",
        "TimeoutMs": 45000,
        "BearerToken": "test-token"
    }
    mock_model_validate.return_value = ModelEndpointModel(
        guid="test-guid",
        name="Test Endpoint",
        endpoint_url="https://api.example.com/",
        api_type=ModelApiTypeEnum.OpenAi,
        timeout_ms=45000,
        bearer_token="test-token"
    )
    
    result = ModelEndpoint.retrieve("test-guid")
    
    assert result.guid == "test-guid"
    assert result.name == "Test Endpoint"
    assert result.endpoint_url == "https://api.example.com/"
    assert result.api_type == ModelApiTypeEnum.OpenAi
    assert result.timeout_ms == 45000
    assert result.bearer_token == "test-token"
    mock_client.request.assert_called_once()
    mock_model_validate.assert_called_once()


@patch("view_sdk.mixins.get_client")
@patch("view_sdk.models.model_endpoint_model.ModelEndpointModel.model_validate")
def test_update_model_endpoint_partial(mock_model_validate, mock_get_client):
    """Test partial update of a model endpoint."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {
        "GUID": "test-guid",
        "Name": "Test Endpoint",
        "EndpointUrl": "https://api.example.com/",
        "TimeoutMs": 60000,  # Updated
        "ApiType": "Ollama"  # Unchanged
    }
    mock_model_validate.return_value = ModelEndpointModel(
        guid="test-guid",
        name="Test Endpoint",
        endpoint_url="https://api.example.com/",
        timeout_ms=60000,
        api_type=ModelApiTypeEnum.Ollama
    )
    
    result = ModelEndpoint.update(
        "test-guid",
        timeout_ms=60000  # Only update timeout
    )
    
    assert result.guid == "test-guid"
    assert result.name == "Test Endpoint"
    assert result.endpoint_url == "https://api.example.com/"
    assert result.timeout_ms == 60000
    assert result.api_type == ModelApiTypeEnum.Ollama
    mock_client.request.assert_called_once()
    mock_model_validate.assert_called_once()


@patch("view_sdk.mixins.get_client")
@patch("view_sdk.models.model_endpoint_model.ModelEndpointModel.model_validate")
def test_create_model_endpoint_with_bearer_token(mock_model_validate, mock_get_client):
    """Test creating a model endpoint with bearer token."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {"GUID": "test-guid"}
    mock_model_validate.return_value = ModelEndpointModel(
        guid="test-guid",
        name="Test Endpoint",
        endpoint_url="https://api.openai.com/v1/",
        bearer_token="sk-test-token",
        api_type=ModelApiTypeEnum.OpenAi
    )
    
    result = ModelEndpoint.create(
        name="Test Endpoint",
        endpoint_url="https://api.openai.com/v1/",
        bearer_token="sk-test-token",
        api_type=ModelApiTypeEnum.OpenAi
    )
    
    assert result.guid == "test-guid"
    assert result.name == "Test Endpoint"
    assert result.endpoint_url == "https://api.openai.com/v1/"
    assert result.bearer_token == "sk-test-token"
    assert result.api_type == ModelApiTypeEnum.OpenAi
    mock_client.request.assert_called_once()
    mock_model_validate.assert_called_once()


@patch("view_sdk.mixins.get_client")
@patch("view_sdk.models.model_endpoint_model.ModelEndpointModel.model_validate")
def test_create_model_endpoint_ollama(mock_model_validate, mock_get_client):
    """Test creating an Ollama model endpoint."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {"GUID": "test-guid"}
    mock_model_validate.return_value = ModelEndpointModel(
        guid="test-guid",
        name="Ollama Endpoint",
        endpoint_url="http://localhost:11434/",
        api_type=ModelApiTypeEnum.Ollama
    )
    
    result = ModelEndpoint.create(
        name="Ollama Endpoint",
        endpoint_url="http://localhost:11434/",
        api_type=ModelApiTypeEnum.Ollama
    )
    
    assert result.guid == "test-guid"
    assert result.name == "Ollama Endpoint"
    assert result.endpoint_url == "http://localhost:11434/"
    assert result.api_type == ModelApiTypeEnum.Ollama
    assert result.bearer_token is None  # Ollama typically doesn't use bearer tokens
    mock_client.request.assert_called_once()
    mock_model_validate.assert_called_once()


def test_model_endpoint_resource_name():
    """Test that the resource name is correct."""
    assert ModelEndpoint.RESOURCE_NAME == "modelendpoints"


def test_model_endpoint_model_class():
    """Test that the model class is correct."""
    assert ModelEndpoint.MODEL == ModelEndpointModel


@patch("view_sdk.mixins.get_client")
@patch("view_sdk.models.model_endpoint_model.ModelEndpointModel.model_validate")
def test_retrieve_model_endpoint_with_additional_data(mock_model_validate, mock_get_client):
    """Test retrieving a model endpoint with additional data."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {
        "GUID": "test-guid",
        "Name": "Test Endpoint",
        "AdditionalData": '{"custom": "data"}'
    }
    mock_model_validate.return_value = ModelEndpointModel(
        guid="test-guid",
        name="Test Endpoint",
        additional_data='{"custom": "data"}'
    )
    
    result = ModelEndpoint.retrieve("test-guid")
    
    assert result.guid == "test-guid"
    assert result.name == "Test Endpoint"
    assert result.additional_data == '{"custom": "data"}'
    mock_client.request.assert_called_once()
    mock_model_validate.assert_called_once()
