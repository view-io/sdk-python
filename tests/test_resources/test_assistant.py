import pytest
from unittest.mock import Mock, patch

from view_sdk.resources.assistant.assistant import Assistant


@pytest.fixture
def mock_client():
    with patch("view_sdk.resources.assistant.assistant.get_client") as mock:
        client = Mock()
        client.tenant_guid = "test-tenant-guid"
        mock.return_value = client
        yield client


@pytest.fixture
def mock_super():
    with patch(
        "view_sdk.resources.assistant.assistant.CreateableAPIResource.create"
    ) as mock:
        yield mock


class TestAssistant:
    def test_rag_legacy_streaming_success(self, mock_client):
        """Test rag_LEGACY method with streaming."""
        # Setup
        mock_events = [
            {"token": "Hello"},
            {"token": " World"},
            {"other": "data"},  # Event without token should be skipped
        ]
        mock_client.sse_request.return_value = mock_events

        # Execute
        rag_request = {"query": "test query", "context": "test context"}
        result = list(Assistant.rag_LEGACY(**rag_request))

        # Assert
        assert result == ["Hello", " World"]
        mock_client.sse_request.assert_called_once()
        call_args = mock_client.sse_request.call_args
        assert call_args[0][0] == "POST"
        assert call_args[0][1] == "v1.0/assistant/rag/"

    def test_chat_rag_messages_streaming_success(self, mock_client):
        """Test chat_rag_messages method with streaming enabled."""
        # Setup
        mock_events = [
            {"token": "Hello"},
            {"token": " Chat"},
            {"other": "data"},  # Event without token should be skipped
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
        call_args = mock_client.sse_request.call_args
        assert call_args[0][0] == "POST"
        assert call_args[0][1] == "v1.0/tenants/test-tenant-guid/assistant/rag/chat"

    def test_chat_rag_messages_non_streaming(self, mock_super):
        """Test chat_rag_messages method with streaming disabled."""
        # Setup
        mock_super.return_value = {"response": "test"}

        # Execute
        chat_request = {
            "messages": [{"role": "user", "content": "Hello"}],
            "Stream": False,
        }
        generator = Assistant.chat_rag_messages(**chat_request)

        # Assert - method returns a generator that raises StopIteration with the result
        assert hasattr(generator, "__iter__")  # It's a generator
        try:
            next(generator)
            assert False, "Expected StopIteration"
        except StopIteration as e:
            result = e.value
            assert result == {"response": "test"}

        mock_super.assert_called_once_with(**chat_request)
        assert Assistant.RESOURCE_NAME == "assistant/rag/chat"

    def test_chat_config_streaming_success(self, mock_client):
        """Test chat_config method with streaming enabled."""
        # Setup
        mock_events = [
            {"token": "Config"},
            {"token": " Response"},
        ]
        mock_client.sse_request.return_value = mock_events

        # Execute
        config_id = "test-config-123"
        chat_request = {
            "messages": [{"role": "user", "content": "Hello"}],
            "Stream": True,
        }
        result = list(Assistant.chat_config(config_id, **chat_request))

        # Assert
        assert result == ["Config", " Response"]
        mock_client.sse_request.assert_called_once()
        call_args = mock_client.sse_request.call_args
        assert call_args[0][0] == "POST"
        assert call_args[0][1] == "v1.0/assistant/chat/test-config-123"

    def test_chat_only_streaming_success(self, mock_client):
        """Test chat_only method with streaming enabled."""
        # Setup
        mock_events = [
            {"token": "Only"},
            {"token": " Chat"},
        ]
        mock_client.sse_request.return_value = mock_events

        # Execute
        chat_request = {
            "messages": [{"role": "user", "content": "Hello"}],
            "Stream": True,
        }
        result = list(Assistant.chat_only(**chat_request))

        # Assert
        assert result == ["Only", " Chat"]
        mock_client.sse_request.assert_called_once()
        call_args = mock_client.sse_request.call_args
        assert call_args[0][0] == "POST"
        assert call_args[0][1] == "v1.0/assistant/chat/completions"

    def test_chat_only_non_streaming(self, mock_super):
        """Test chat_only method with streaming disabled."""
        # Setup
        mock_super.return_value = {"response": "only test"}

        # Execute
        chat_request = {
            "messages": [{"role": "user", "content": "Hello"}],
            "Stream": False,
        }
        generator = Assistant.chat_only(**chat_request)

        # Assert - method returns a generator that raises StopIteration with the result
        assert hasattr(generator, "__iter__")  # It's a generator
        try:
            next(generator)
            assert False, "Expected StopIteration"
        except StopIteration as e:
            result = e.value
            assert result == {"response": "only test"}

        mock_super.assert_called_once_with(**chat_request)
        assert Assistant.RESOURCE_NAME == "assistant/chat/completions"

    def test_chat_rag_messages_error_handling(self, mock_client):
        """Test chat_rag_messages error handling."""
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

    def test_chat_config_error_handling(self, mock_client):
        """Test chat_config error handling."""
        # Setup
        mock_client.sse_request.side_effect = Exception("Test error")

        # Execute
        config_id = "test-config"
        chat_request = {
            "messages": [{"role": "user", "content": "Hello"}],
            "Stream": True,
        }
        result = list(Assistant.chat_config(config_id, **chat_request))

        # Assert
        assert result == []

    def test_chat_only_error_handling(self, mock_client):
        """Test chat_only error handling."""
        # Setup
        mock_client.sse_request.side_effect = Exception("Test error")

        # Execute
        chat_request = {
            "messages": [{"role": "user", "content": "Hello"}],
            "Stream": True,
        }
        result = list(Assistant.chat_only(**chat_request))

        # Assert
        assert result == []

    def test_extract_token_valid_json(self):
        """Test _extract_token with valid JSON."""
        json_data = '{"token": "test_token", "other": "data"}'
        result = Assistant._extract_token(json_data)
        assert result == "test_token"

    def test_extract_token_invalid_json(self):
        """Test _extract_token with invalid JSON."""
        json_data = "invalid json"
        result = Assistant._extract_token(json_data)
        assert result is None

    def test_extract_token_missing_token(self):
        """Test _extract_token with JSON missing token."""
        json_data = '{"other": "data"}'
        result = Assistant._extract_token(json_data)
        assert result is None

    def test_extract_token_none_input(self):
        """Test _extract_token with None input."""
        result = Assistant._extract_token(None)
        assert result is None

    def test_string_token_events(self, mock_client):
        """Test handling of string events (non-dict events)."""
        # Setup - mix of dict and string events
        mock_events = [
            {"token": "Hello"},
            "String Event",  # This should be yielded as-is
            {"token": " World"},
        ]
        mock_client.sse_request.return_value = mock_events

        # Execute
        chat_request = {
            "messages": [{"role": "user", "content": "Hello"}],
            "Stream": True,
        }
        result = list(Assistant.chat_rag_messages(**chat_request))

        # Assert - string events should be yielded as-is
        assert result == ["Hello", "String Event", " World"]
