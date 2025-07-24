from unittest.mock import patch
from view_sdk.resources.assistant.models import Models


@patch("view_sdk.resources.assistant.models.super")
def test_retrieve_all(mock_super):
    mock_super().create.return_value = "all_models"
    result = Models.retrieve_all(foo="bar")
    assert result == "all_models"
    assert Models.CREATE_METHOD == "POST"
    mock_super().create.assert_called()


@patch("view_sdk.resources.assistant.models.super")
def test_retrieve(mock_super):
    mock_super().create.return_value = "one_model"
    result = Models.retrieve(id="model1")
    assert result == "one_model"
    assert Models.CREATE_METHOD == "POST"
    assert Models.RESOURCE_NAME == "assistant/models/pull"
    mock_super().create.assert_called()


@patch("view_sdk.resources.assistant.models.super")
def test_delete(mock_super):
    mock_super().create.return_value = "deleted_model"
    result = Models.delete(id="model1")
    assert result == "deleted_model"
    assert Models.CREATE_METHOD == "POST"
    assert Models.RESOURCE_NAME == "assistant/models/delete"
    mock_super().create.assert_called()


@patch("view_sdk.resources.assistant.models.super")
def test_load_unload(mock_super):
    mock_super().create.return_value = "loaded_model"
    result = Models.load_unload(id="model1")
    assert result == "loaded_model"
    assert Models.CREATE_METHOD == "POST"
    assert Models.RESOURCE_NAME == "assistant/models/load"
    mock_super().create.assert_called()
