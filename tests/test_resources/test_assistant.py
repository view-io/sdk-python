import pytest
from unittest.mock import Mock, patch

from view_sdk.resources.assistant.assistant import Assistant
from view_sdk.models.assistant_chat_request import AssistantChatRequest
from view_sdk.models.assistant_rag_request import AssistantRagRequest
from view_sdk.resources.assistant.healthcheck import HealthCheck

@pytest.fixture
def mock_client():
    with patch('view_sdk.resources.assistant.assistant.get_client') as mock:
        client = Mock()
        mock.return_value = client
        yield client


class TestAssistant:
    def test_process_rag_success(self, mock_client):
        # Setup
        mock_events = [
            {"token": "Hello"},
            {"token": " World"},
            {"other": "data"}  # Changed: use dict without token instead of string
        ]
        mock_client.sse_request.return_value = mock_events

        # Execute
        rag_request = {
            "query": "test query",
            "context": "test context"
        }
        result = list(Assistant.process_rag(**rag_request))

        # Assert
        assert result == ["Hello", " World"]
        mock_client.sse_request.assert_called_once()

    def test_process_chat_success(self, mock_client):
        # Setup
        mock_events = [
            {"token": "Hello"},
            {"token": " Chat"},
            {"other": "data"}  # Changed: use dict without token instead of string
        ]
        mock_client.sse_request.return_value = mock_events

        # Execute
        chat_request = {
            "messages": [{"role": "user", "content": "Hello"}]
        }
        result = list(Assistant.process_chat(**chat_request))

        # Assert
        assert result == ["Hello", " Chat"]
        mock_client.sse_request.assert_called_once()

    def test_process_chat_error_handling(self, mock_client):
        # Setup
        mock_client.sse_request.side_effect = Exception("Test error")

        # Execute
        chat_request = {
            "messages": [{"role": "user", "content": "Hello"}]
        }
        result = list(Assistant.process_chat(**chat_request))

        # Assert
        assert result == []

    def test_extract_token_valid_json(self):
        # Test with valid JSON
        json_data = '{"token": "test_token", "other": "data"}'
        result = Assistant._extract_token(json_data)
        assert result == "test_token"

    def test_extract_token_invalid_json(self):
        # Test with invalid JSON
        json_data = 'invalid json'
        result = Assistant._extract_token(json_data)
        assert result is None

    def test_extract_token_missing_token(self):
        # Test with JSON missing token
        json_data = '{"other": "data"}'
        result = Assistant._extract_token(json_data)
        assert result is None
