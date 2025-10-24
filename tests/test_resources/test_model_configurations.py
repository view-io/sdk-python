import pytest
from unittest.mock import patch, MagicMock
from view_sdk.resources.configuration.model_configurations import ModelConfiguration
from view_sdk.models.model_configuration_model import ModelConfigurationModel


@patch("view_sdk.mixins.get_client")
@patch(
    "view_sdk.models.model_configuration_model.ModelConfigurationModel.model_validate"
)
def test_create_model_configuration(mock_model_validate, mock_get_client):
    """Test creating a model configuration."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {"GUID": "test-guid", "ModelName": "test/model"}
    mock_model_validate.return_value = ModelConfigurationModel(
        guid="test-guid", model_name="test/model"
    )

    result = ModelConfiguration.create(
        model_name="test/model", temperature=0.5, context_size=2048
    )

    assert result.guid == "test-guid"
    assert result.model_name == "test/model"
    mock_client.request.assert_called_once()
    mock_model_validate.assert_called_once()


@patch("view_sdk.mixins.get_client")
@patch(
    "view_sdk.models.model_configuration_model.ModelConfigurationModel.model_validate"
)
def test_retrieve_model_configuration(mock_model_validate, mock_get_client):
    """Test retrieving a model configuration by GUID."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {"GUID": "test-guid", "ModelName": "test/model"}
    mock_model_validate.return_value = ModelConfigurationModel(
        guid="test-guid", model_name="test/model"
    )

    result = ModelConfiguration.retrieve("test-guid")

    assert result.guid == "test-guid"
    assert result.model_name == "test/model"
    mock_client.request.assert_called_once()
    mock_model_validate.assert_called_once()


@patch("view_sdk.mixins.get_client")
@patch(
    "view_sdk.models.model_configuration_model.ModelConfigurationModel.model_validate"
)
def test_retrieve_all_model_configurations(mock_model_validate, mock_get_client):
    """Test retrieving all model configurations."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = [
        {"GUID": "guid1", "ModelName": "model1"},
        {"GUID": "guid2", "ModelName": "model2"},
    ]
    mock_model_validate.side_effect = lambda data: ModelConfigurationModel(**data)

    result = ModelConfiguration.retrieve_all()

    assert len(result) == 2
    assert result[0].guid == "guid1"
    assert result[1].guid == "guid2"
    mock_client.request.assert_called_once()
    assert mock_model_validate.call_count == 2


@patch("view_sdk.mixins.get_client")
@patch(
    "view_sdk.models.model_configuration_model.ModelConfigurationModel.model_validate"
)
def test_update_model_configuration(mock_model_validate, mock_get_client):
    """Test updating a model configuration."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {
        "GUID": "test-guid",
        "ModelName": "updated/model",
    }
    mock_model_validate.return_value = ModelConfigurationModel(
        guid="test-guid", model_name="updated/model"
    )

    result = ModelConfiguration.update(
        "test-guid", model_name="updated/model", temperature=0.8
    )

    assert result.guid == "test-guid"
    assert result.model_name == "updated/model"
    mock_client.request.assert_called_once()
    mock_model_validate.assert_called_once()


@patch("view_sdk.mixins.get_client")
def test_delete_model_configuration(mock_get_client):
    """Test deleting a model configuration."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = None

    result = ModelConfiguration.delete("test-guid")

    assert result is True
    mock_client.request.assert_called_once()


@patch("view_sdk.mixins.get_client")
def test_exists_model_configuration(mock_get_client):
    """Test checking if a model configuration exists."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = True

    result = ModelConfiguration.exists("test-guid")

    assert result is True
    mock_client.request.assert_called_once()


@patch("view_sdk.mixins.get_client")
@patch(
    "view_sdk.models.model_configuration_model.ModelConfigurationModel.model_validate"
)
def test_enumerate_model_configurations(mock_model_validate, mock_get_client):
    """Test enumerating model configurations with pagination."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {
        "Objects": [
            {"GUID": "guid1", "ModelName": "model1"},
            {"GUID": "guid2", "ModelName": "model2"},
        ],
        "TotalRecords": 2,
        "Skip": 0,
        "MaxResults": 10,
    }
    mock_model_validate.side_effect = lambda data: ModelConfigurationModel(**data)

    result = ModelConfiguration.enumerate(page=1, page_size=10)

    assert len(result.objects) == 2
    assert result.total_records == 2
    assert result.skip == 0
    assert result.max_results == 10
    mock_client.request.assert_called_once()


@patch("view_sdk.mixins.get_client")
@patch(
    "view_sdk.models.model_configuration_model.ModelConfigurationModel.model_validate"
)
def test_create_model_configuration_with_validation(
    mock_model_validate, mock_get_client
):
    """Test creating a model configuration with field validation."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {"GUID": "test-guid"}

    # Test with invalid temperature (should raise validation error)
    with patch.object(
        ModelConfigurationModel,
        "__init__",
        side_effect=ValueError("Temperature must be between 0.0 and 2.0"),
    ):
        with pytest.raises(ValueError, match="Temperature must be between 0.0 and 2.0"):
            ModelConfiguration.create(temperature=3.0)

    # Test with valid data
    mock_model_validate.return_value = ModelConfigurationModel(
        guid="test-guid", model_name="test/model", temperature=0.5
    )

    result = ModelConfiguration.create(
        model_name="test/model",
        temperature=0.5,
        context_size=2048,
        max_output_tokens=1024,
    )

    assert result.guid == "test-guid"
    assert result.model_name == "test/model"
    assert result.temperature == 0.5


@patch("view_sdk.mixins.get_client")
@patch(
    "view_sdk.models.model_configuration_model.ModelConfigurationModel.model_validate"
)
def test_retrieve_model_configuration_with_alias(mock_model_validate, mock_get_client):
    """Test retrieving a model configuration using alias fields."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {
        "GUID": "test-guid",
        "ModelName": "test/model",
        "Temperature": 0.7,
        "ContextSize": 4096,
        "MaxOutputTokens": 2048,
    }
    mock_model_validate.return_value = ModelConfigurationModel(
        guid="test-guid",
        model_name="test/model",
        temperature=0.7,
        context_size=4096,
        max_output_tokens=2048,
    )

    result = ModelConfiguration.retrieve("test-guid")

    assert result.guid == "test-guid"
    assert result.model_name == "test/model"
    assert result.temperature == 0.7
    assert result.context_size == 4096
    assert result.max_output_tokens == 2048
    mock_client.request.assert_called_once()
    mock_model_validate.assert_called_once()


@patch("view_sdk.mixins.get_client")
@patch(
    "view_sdk.models.model_configuration_model.ModelConfigurationModel.model_validate"
)
def test_update_model_configuration_partial(mock_model_validate, mock_get_client):
    """Test partial update of a model configuration."""
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.request.return_value = {
        "GUID": "test-guid",
        "ModelName": "test/model",
        "Temperature": 0.9,  # Updated
        "ContextSize": 4096,  # Unchanged
    }
    mock_model_validate.return_value = ModelConfigurationModel(
        guid="test-guid", model_name="test/model", temperature=0.9, context_size=4096
    )

    result = ModelConfiguration.update(
        "test-guid",
        temperature=0.9,  # Only update temperature
    )

    assert result.guid == "test-guid"
    assert result.model_name == "test/model"
    assert result.temperature == 0.9
    assert result.context_size == 4096
    mock_client.request.assert_called_once()
    mock_model_validate.assert_called_once()


def test_model_configuration_resource_name():
    """Test that the resource name is correct."""
    assert ModelConfiguration.RESOURCE_NAME == "modelconfigs"


def test_model_configuration_model_class():
    """Test that the model class is correct."""
    assert ModelConfiguration.MODEL == ModelConfigurationModel
