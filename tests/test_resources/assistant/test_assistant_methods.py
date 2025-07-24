import pytest
from unittest.mock import Mock, patch

from view_sdk.resources.assistant.assistant import Assistant


@pytest.fixture
def mock_client():
    with (
        patch("view_sdk.resources.assistant.assistant.get_client") as mock1,
        patch("view_sdk.mixins.get_client") as mock2,
    ):
        client = Mock()
        mock1.return_value = client
        mock2.return_value = client
        yield client


class TestAssistant:
    def test_process_rag_success(self, mock_client):
        # Setup
        mock_events = [
            {"token": "Hello"},
            {"token": " World"},
            {"other": "data"},  # Changed: use dict without token instead of string
        ]
        mock_client.sse_request.return_value = mock_events

        # Execute
        rag_request = {"query": "test query", "context": "test context"}
        result = list(Assistant.rag_LEGACY(**rag_request))

        # Assert
        assert result == ["Hello", " World"]
        mock_client.sse_request.assert_called_once()

    def test_process_chat_success(self, mock_client):
        # Setup
        mock_events = [
            {"token": "Hello"},
            {"token": " Chat"},
            {"other": "data"},  # Changed: use dict without token instead of string
        ]
        mock_client.sse_request.return_value = mock_events

        # Execute
        chat_request = {
            "messages": [{"role": "user", "content": "Hello"}],
            "Stream": True,
        }
        result = list(Assistant.chat_rag_messages(**chat_request))

        # Assert
        assert result == ["Hello", " Chat"]
        mock_client.sse_request.assert_called_once()

    def test_process_chat_error_handling(self, mock_client):
        # Setup
        mock_client.sse_request.side_effect = Exception("Test error")

        # Execute
        chat_request = {
            "messages": [{"role": "user", "content": "Hello"}],
            "Stream": True,
        }
        result = list(Assistant.chat_rag_messages(**chat_request))

        # Assert
        assert result == []

    def test_extract_token_valid_json(self):
        # Test with valid JSON
        json_data = '{"token": "test_token", "other": "data"}'
        result = Assistant._extract_token(json_data)
        assert result == "test_token"

    def test_extract_token_invalid_json(self):
        # Test with invalid JSON
        json_data = "invalid json"
        result = Assistant._extract_token(json_data)
        assert result is None

    def test_extract_token_missing_token(self):
        # Test with JSON missing token
        json_data = '{"other": "data"}'
        result = Assistant._extract_token(json_data)
        assert result is None


# Move these outside the class for pytest discovery
@patch("view_sdk.resources.assistant.assistant.super")
def test_chat_rag_messages_non_stream(mock_super):
    mock_super().create.return_value = "created"
    result = Assistant.chat_rag_messages(Stream=False, foo="bar")
    # Exhaust the generator to get the return value
    try:
        next(result)
    except StopIteration as e:
        assert e.value == "created"
    assert Assistant.RESOURCE_NAME == "assistant/rag/chat"
    mock_super().create.assert_called()


@patch("view_sdk.resources.assistant.assistant.super")
def test_chat_config_non_stream(mock_super):
    mock_super().update.return_value = "updated"
    result = Assistant.chat_config("config123", Stream=False, foo="bar")
    try:
        next(result)
    except StopIteration as e:
        assert e.value == "updated"
    assert Assistant.RESOURCE_NAME == "assistant/chat"
    assert Assistant.UPDATE_METHOD == "POST"
    mock_super().update.assert_called()


@patch("view_sdk.resources.assistant.assistant.super")
def test_chat_only_non_stream(mock_super):
    mock_super().create.return_value = "created"
    result = Assistant.chat_only(Stream=False, foo="bar")
    try:
        next(result)
    except StopIteration as e:
        assert e.value == "created"
    assert Assistant.RESOURCE_NAME == "assistant/chat/completions"
    mock_super().create.assert_called()
