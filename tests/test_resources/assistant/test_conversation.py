import pytest
from unittest.mock import Mock, patch
from uuid import uuid4
from datetime import datetime

from view_sdk.resources.assistant.conversation import Conversation
from view_sdk.models.conversation_request import ConversationRequestModel
from view_sdk.models.list_conversations import ListConversationsModel


@pytest.fixture
def mock_client():
    """Mock client fixture for testing."""
    with (
        patch(
            "view_sdk.resources.assistant.conversation.get_client"
        ) as mock_get_client,
        patch("view_sdk.mixins.get_client") as mock_mixin_client,
    ):
        client = Mock()
        client.tenant_guid = "test-tenant-guid"
        mock_get_client.return_value = client
        mock_mixin_client.return_value = client
        yield client


@pytest.fixture
def sample_conversation_data():
    """Sample conversation data for testing."""
    return {
        "conversation_id": uuid4(),
        "tenant_guid": uuid4(),
        "user_guid": uuid4(),
        "session_id": "test-session",
        "config_guid": uuid4(),
        "title": "Test Conversation",
        "message_count": 2,
        "last_message_at": datetime.now(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "metadata": {"source": "test"},
    }


@pytest.fixture
def sample_message_data():
    """Sample message data for testing."""
    return {
        "message_id": uuid4(),
        "conversation_id": uuid4(),
        "role": "user",
        "content": "Hello, world!",
        "sources": None,
        "metadata": None,
        "created_at": datetime.now(),
        "is_superseded": False,
        "superseded_at": None,
        "superseded_by_message_id": None,
        "edited_at": None,
        "original_content": None,
    }


class TestConversationCreate:
    """Test cases for Conversation.create method."""

    def test_create_success_streaming(self, mock_client, sample_conversation_data):
        """Test successful conversation creation with streaming."""
        # Setup
        conversation_id = sample_conversation_data["conversation_id"]
        mock_events = [
            {
                "conversation_id": str(conversation_id),
                "tenant_guid": str(sample_conversation_data["tenant_guid"]),
                "title": "Test Conversation",
            },
            {"message_id": str(uuid4()), "role": "user"},
            {"token": "Hello"},
            {"token": " World"},
            {"total_time_ms": 1500.0},
        ]
        mock_client.sse_request.return_value = iter(mock_events)

        # Execute
        request_data = {
            "config_guid": sample_conversation_data["config_guid"],
            "title": "Test Conversation",
            "message": "Hello, world!",
            "metadata": {"source": "test"},
            "documents": None,
        }

        result = list(Conversation.create(**request_data))

        # Assert
        assert len(result) == 5
        assert result[0]["conversation_id"] == str(conversation_id)
        assert result[1]["role"] == "user"
        assert result[2]["token"] == "Hello"
        assert result[3]["token"] == " World"
        assert result[4]["total_time_ms"] == 1500.0

        # Verify the request was made correctly
        mock_client.sse_request.assert_called_once()
        call_args = mock_client.sse_request.call_args
        assert call_args[0][0] == "POST"  # method
        assert (
            "assistant/conversations" in call_args[0][1]
        )  # URL contains resource name
        assert "json" in call_args[1]  # JSON data provided

    def test_create_validation_error(self, mock_client):
        """Test conversation creation with invalid data."""
        # Execute & Assert
        with pytest.raises(Exception):  # Pydantic validation error
            list(
                Conversation.create(
                    # Missing required fields
                    title="Test"
                    # config_guid and message are required
                )
            )

    def test_create_missing_tenant_guid(self, mock_client):
        """Test conversation creation when tenant GUID is missing."""
        # Setup
        mock_client.tenant_guid = None

        # Execute & Assert
        with pytest.raises(ValueError, match="Tenant GUID is required"):
            list(
                Conversation.create(
                    config_guid=uuid4(), title="Test Conversation", message="Hello"
                )
            )

    def test_create_client_error(self, mock_client):
        """Test conversation creation when client raises an error."""
        # Setup
        mock_client.sse_request.side_effect = Exception("Connection error")

        # Execute & Assert
        with pytest.raises(Exception, match="Connection error"):
            list(
                Conversation.create(
                    config_guid=uuid4(), title="Test Conversation", message="Hello"
                )
            )


class TestConversationRetrieve:
    """Test cases for Conversation.retrieve method."""

    def test_retrieve_success(
        self, mock_client, sample_conversation_data, sample_message_data
    ):
        """Test successful conversation retrieval."""
        # Setup
        conversation_id = sample_conversation_data["conversation_id"]
        mock_response = {
            "conversation": sample_conversation_data,
            "messages": [sample_message_data],
        }

        with patch("view_sdk.resources.assistant.conversation.super") as mock_super:
            mock_super().retrieve.return_value = mock_response

            # Execute
            result = Conversation.retrieve(conversation_id)

            # Assert
            assert isinstance(result, dict)  # Returns raw response that gets validated
            mock_super().retrieve.assert_called_once_with(conversation_id)

    def test_retrieve_nonexistent_conversation(self, mock_client):
        """Test retrieving a non-existent conversation."""
        # Setup
        conversation_id = uuid4()

        with patch("view_sdk.resources.assistant.conversation.super") as mock_super:
            mock_super().retrieve.side_effect = Exception("Not found")

            # Execute & Assert
            with pytest.raises(Exception, match="Not found"):
                Conversation.retrieve(conversation_id)


class TestConversationRetrieveAll:
    """Test cases for Conversation.retrieve_all method."""

    def test_retrieve_all_success(self, mock_client, sample_conversation_data):
        """Test successful retrieval of all conversations."""
        # Setup
        mock_response = {
            "conversations": [sample_conversation_data],
            "total": 1,
            "limit": 10,
            "offset": 0,
        }

        with patch("view_sdk.resources.assistant.conversation.super") as mock_super:
            mock_super().retrieve_all.return_value = mock_response

            # Execute
            result = Conversation.retrieve_all(limit=10, offset=0)

            # Assert
            assert isinstance(result, ListConversationsModel)
            assert len(result.conversations) == 1
            assert result.total == 1
            assert result.limit == 10
            assert result.offset == 0
            mock_super().retrieve_all.assert_called_once_with(limit=10, offset=0)

    def test_retrieve_all_with_pagination(self, mock_client, sample_conversation_data):
        """Test retrieve_all with pagination parameters."""
        # Setup
        mock_response = {
            "conversations": [sample_conversation_data] * 5,
            "total": 25,
            "limit": 5,
            "offset": 10,
        }

        with patch("view_sdk.resources.assistant.conversation.super") as mock_super:
            mock_super().retrieve_all.return_value = mock_response

            # Execute
            result = Conversation.retrieve_all(limit=5, offset=10)

            # Assert
            assert isinstance(result, ListConversationsModel)
            assert len(result.conversations) == 5
            assert result.total == 25
            assert result.limit == 5
            assert result.offset == 10

    def test_retrieve_all_empty_result(self, mock_client):
        """Test retrieve_all when no conversations exist."""
        # Setup
        mock_response = {"conversations": [], "total": 0, "limit": 10, "offset": 0}

        with patch("view_sdk.resources.assistant.conversation.super") as mock_super:
            mock_super().retrieve_all.return_value = mock_response

            # Execute
            result = Conversation.retrieve_all()

            # Assert
            assert isinstance(result, ListConversationsModel)
            assert len(result.conversations) == 0
            assert result.total == 0


class TestConversationAddMessage:
    """Test cases for Conversation.add_message method."""

    def test_add_message_success_streaming(self, mock_client):
        """Test successful message addition with streaming."""
        # Setup
        conversation_id = uuid4()
        message_id = uuid4()
        mock_events = [
            {"message_id": str(message_id), "role": "user"},
            {"query": "test query", "model": "test-model", "provider": "test-provider"},
            {"token": "Response"},
            {"token": " token"},
            {"total_time_ms": 800.0},
        ]
        mock_client.sse_request.return_value = iter(mock_events)

        # Execute
        result = list(
            Conversation.add_message(
                conversation_id=conversation_id, message="What is AI?", documents=None
            )
        )

        # Assert
        assert len(result) == 5
        assert result[0]["message_id"] == str(message_id)
        assert result[1]["query"] == "test query"
        assert result[2]["token"] == "Response"
        assert result[3]["token"] == " token"
        assert result[4]["total_time_ms"] == 800.0

        # Verify the request was made correctly
        mock_client.sse_request.assert_called_once()
        call_args = mock_client.sse_request.call_args
        assert call_args[0][0] == "POST"  # method
        assert str(conversation_id) in call_args[0][1]  # conversation ID in URL
        assert "messages" in call_args[0][1]  # messages endpoint
        assert "json" in call_args[1]  # JSON data provided

    def test_add_message_validation_error(self, mock_client):
        """Test add_message with invalid data."""
        # Execute & Assert
        with pytest.raises(Exception):  # Pydantic validation error
            list(
                Conversation.add_message(
                    conversation_id=uuid4()
                    # Missing required 'message' field
                )
            )

    def test_add_message_missing_tenant_guid(self, mock_client):
        """Test add_message when tenant GUID is missing."""
        # Setup
        mock_client.tenant_guid = None

        # Execute & Assert
        with pytest.raises(ValueError, match="Tenant GUID is required"):
            list(Conversation.add_message(conversation_id=uuid4(), message="Hello"))

    def test_add_message_with_documents(self, mock_client):
        """Test add_message with documents."""
        # Setup
        conversation_id = uuid4()
        documents = [{"title": "Doc1", "content": "Content1"}]
        mock_events = [{"message_id": str(uuid4()), "role": "user"}]
        mock_client.sse_request.return_value = iter(mock_events)

        # Execute
        result = list(
            Conversation.add_message(
                conversation_id=conversation_id,
                message="Analyze these documents",
                documents=documents,
            )
        )

        # Assert
        assert len(result) == 1
        mock_client.sse_request.assert_called_once()

        # Verify documents were included in the request
        call_args = mock_client.sse_request.call_args
        json_data = call_args[1]["json"]
        assert json_data["documents"] == documents

    def test_add_message_client_error(self, mock_client):
        """Test add_message when client raises an error."""
        # Setup
        mock_client.sse_request.side_effect = Exception("Server error")

        # Execute & Assert
        with pytest.raises(Exception, match="Server error"):
            list(Conversation.add_message(conversation_id=uuid4(), message="Hello"))


class TestConversationGetWithMessages:
    """Test cases for Conversation.get_with_messages method."""

    def test_get_with_messages_success(
        self, mock_client, sample_conversation_data, sample_message_data
    ):
        """Test successful retrieval of conversation with messages."""
        # Setup
        conversation_id = sample_conversation_data["conversation_id"]
        mock_response = {
            "conversation": sample_conversation_data,
            "messages": [sample_message_data],
        }

        with patch("view_sdk.resources.assistant.conversation.super") as mock_super:
            mock_super().retrieve.return_value = mock_response

            # Execute
            result = Conversation.get_with_messages(conversation_id)

            # Assert
            assert isinstance(result, dict)  # Returns raw response
            mock_super().retrieve.assert_called_once_with(conversation_id)

    def test_get_with_messages_multiple_messages(
        self, mock_client, sample_conversation_data, sample_message_data
    ):
        """Test get_with_messages with multiple messages."""
        # Setup
        conversation_id = sample_conversation_data["conversation_id"]
        message1 = sample_message_data.copy()
        message2 = sample_message_data.copy()
        message2["message_id"] = uuid4()
        message2["role"] = "assistant"
        message2["content"] = "Hello! How can I help you?"

        mock_response = {
            "conversation": sample_conversation_data,
            "messages": [message1, message2],
        }

        with patch("view_sdk.resources.assistant.conversation.super") as mock_super:
            mock_super().retrieve.return_value = mock_response

            # Execute
            result = Conversation.get_with_messages(conversation_id)

            # Assert
            assert isinstance(result, dict)
            assert len(result["messages"]) == 2

    def test_get_with_messages_nonexistent_conversation(self, mock_client):
        """Test get_with_messages for non-existent conversation."""
        # Setup
        conversation_id = uuid4()

        with patch("view_sdk.resources.assistant.conversation.super") as mock_super:
            mock_super().retrieve.side_effect = Exception("Not found")

            # Execute & Assert
            with pytest.raises(Exception, match="Not found"):
                Conversation.get_with_messages(conversation_id)


class TestConversationDelete:
    """Test cases for Conversation.delete method."""

    def test_delete_success(self, mock_client):
        """Test successful conversation deletion."""
        # Setup
        conversation_id = uuid4()
        mock_client.request.return_value = None

        # Execute
        result = Conversation.delete(conversation_id)

        # Assert
        assert result is True
        mock_client.request.assert_called_once()

    def test_delete_nonexistent_conversation(self, mock_client):
        """Test deleting a non-existent conversation."""
        # Setup
        conversation_id = uuid4()
        mock_client.request.side_effect = Exception("Not found")

        # Execute
        result = Conversation.delete(conversation_id)

        # Assert
        assert result is False


class TestConversationResourceConfiguration:
    """Test cases for Conversation resource configuration."""

    def test_resource_configuration(self):
        """Test that the Conversation resource is configured correctly."""
        assert Conversation.RESOURCE_NAME == "assistant/conversations"
        assert Conversation.REQUEST_MODEL == ConversationRequestModel
        assert Conversation.SERVICE.value == "assistant"  # Assuming Service is an enum
        assert Conversation.REQUIRES_TENANT is True
        assert Conversation.CREATE_METHOD == "POST"

    def test_inheritance(self):
        """Test that Conversation inherits from the correct mixins."""
        from view_sdk.mixins import (
            CreateableAPIResource,
            RetrievableAPIResource,
            AllRetrievableAPIResource,
            DeletableAPIResource,
        )

        assert issubclass(Conversation, CreateableAPIResource)
        assert issubclass(Conversation, RetrievableAPIResource)
        assert issubclass(Conversation, AllRetrievableAPIResource)
        assert issubclass(Conversation, DeletableAPIResource)


class TestConversationErrorHandling:
    """Test cases for error handling in Conversation methods."""

    def test_create_with_custom_headers(self, mock_client):
        """Test conversation creation with custom headers."""
        # Setup
        mock_events = [{"conversation_id": str(uuid4())}]
        mock_client.sse_request.return_value = iter(mock_events)
        custom_headers = {"X-Custom-Header": "test-value"}

        # Execute
        result = list(
            Conversation.create(
                config_guid=uuid4(),
                title="Test",
                message="Hello",
                headers=custom_headers,
            )
        )

        # Assert
        assert len(result) == 1
        mock_client.sse_request.assert_called_once()
        call_args = mock_client.sse_request.call_args
        assert call_args[1]["headers"] == custom_headers

    def test_add_message_with_custom_headers(self, mock_client):
        """Test add_message with custom headers."""
        # Setup
        mock_events = [{"message_id": str(uuid4())}]
        mock_client.sse_request.return_value = iter(mock_events)
        custom_headers = {"X-Custom-Header": "test-value"}

        # Execute
        result = list(
            Conversation.add_message(
                conversation_id=uuid4(), message="Hello", headers=custom_headers
            )
        )

        # Assert
        assert len(result) == 1
        mock_client.sse_request.assert_called_once()
        call_args = mock_client.sse_request.call_args
        assert call_args[1]["headers"] == custom_headers

    def test_streaming_event_types(self, mock_client):
        """Test handling of different streaming event types."""
        # Setup
        conversation_id = uuid4()
        message_id = uuid4()
        mock_events = [
            # Conversation creation event
            {
                "conversation_id": str(conversation_id),
                "tenant_guid": "test-tenant",
                "title": "Test",
            },
            # Message creation event
            {"message_id": str(message_id), "role": "user"},
            # Pipeline start event
            {"config_guid": str(uuid4()), "message_id": str(message_id)},
            # Embedding event
            {"query": "test", "model": "test-model", "provider": "test-provider"},
            # Error event
            {"error": "Test error", "error_type": "ValidationError"},
            # Completion events
            {"embedding_time_ms": 100.5},
            {"source_count": 5, "retrieval_time_ms": 200.0},
            {
                "token_count": 50,
                "generation_time_ms": 500.0,
                "tokens_per_second": 100.0,
            },
            {"total_time_ms": 800.5},
        ]
        mock_client.sse_request.return_value = iter(mock_events)

        # Execute
        result = list(
            Conversation.create(config_guid=uuid4(), title="Test", message="Hello")
        )

        # Assert
        assert len(result) == 9
        # Verify different event types are preserved
        assert result[0]["conversation_id"] == str(conversation_id)
        assert result[1]["message_id"] == str(message_id)
        assert result[4]["error"] == "Test error"
        assert result[5]["embedding_time_ms"] == 100.5
        assert result[8]["total_time_ms"] == 800.5
