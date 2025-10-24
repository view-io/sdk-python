import pytest
from datetime import datetime
from uuid import UUID, uuid4
from typing import Dict

from view_sdk.models.conversation import ConversationModel
from view_sdk.models.conversation_request import ConversationRequestModel
from view_sdk.models.conversation_with_messages import ConversationWithMessagesModel
from view_sdk.models.list_conversations import ListConversationsModel
from view_sdk.models.message import MessageModel
from view_sdk.models.message_request import MessageRequestModel


class TestConversationModel:
    """Test cases for ConversationModel."""

    def test_conversation_model_creation_with_all_fields(self):
        """Test creating a ConversationModel with all fields."""
        # Setup
        conversation_id = uuid4()
        tenant_guid = uuid4()
        user_guid = uuid4()
        config_guid = uuid4()
        now = datetime.now()
        
        data = {
            "conversation_id": conversation_id,
            "tenant_guid": tenant_guid,
            "user_guid": user_guid,
            "session_id": "test-session-123",
            "config_guid": config_guid,
            "title": "Test Conversation",
            "message_count": 5,
            "last_message_at": now,
            "created_at": now,
            "updated_at": now,
            "metadata": {"source": "api", "priority": "high"}
        }

        # Execute
        conversation = ConversationModel(**data)

        # Assert
        assert conversation.conversation_id == conversation_id
        assert conversation.tenant_guid == tenant_guid
        assert conversation.user_guid == user_guid
        assert conversation.session_id == "test-session-123"
        assert conversation.config_guid == config_guid
        assert conversation.title == "Test Conversation"
        assert conversation.message_count == 5
        assert conversation.last_message_at == now
        assert conversation.created_at == now
        assert conversation.updated_at == now
        assert conversation.metadata == {"source": "api", "priority": "high"}

    def test_conversation_model_creation_with_minimal_fields(self):
        """Test creating a ConversationModel with minimal required fields."""
        # Setup
        conversation_id = uuid4()
        tenant_guid = uuid4()
        user_guid = uuid4()
        config_guid = uuid4()
        now = datetime.now()
        
        data = {
            "conversation_id": conversation_id,
            "tenant_guid": tenant_guid,
            "user_guid": user_guid,
            "config_guid": config_guid,
            "title": "Minimal Conversation",
            "message_count": 0,
            "last_message_at": now,
            "created_at": now,
            "updated_at": now
        }

        # Execute
        conversation = ConversationModel(**data)

        # Assert
        assert conversation.conversation_id == conversation_id
        assert conversation.session_id is None
        assert conversation.metadata == {}  # Default empty dict

    def test_conversation_model_with_aliases(self):
        """Test ConversationModel creation using field aliases."""
        # Setup
        conversation_id = uuid4()
        tenant_guid = uuid4()
        user_guid = uuid4()
        config_guid = uuid4()
        now = datetime.now()
        
        # Using aliases (same as field names in this case, but testing the alias functionality)
        data = {
            "conversation_id": conversation_id,
            "tenant_guid": tenant_guid,
            "user_guid": user_guid,
            "config_guid": config_guid,
            "title": "Alias Test",
            "message_count": 1,
            "last_message_at": now,
            "created_at": now,
            "updated_at": now,
            "metadata": {"test": "alias"}
        }

        # Execute
        conversation = ConversationModel(**data)

        # Assert
        assert conversation.conversation_id == conversation_id
        assert conversation.metadata == {"test": "alias"}

    def test_conversation_model_serialization(self):
        """Test ConversationModel serialization to dict."""
        # Setup
        conversation_id = uuid4()
        tenant_guid = uuid4()
        user_guid = uuid4()
        config_guid = uuid4()
        now = datetime.now()
        
        conversation = ConversationModel(
            conversation_id=conversation_id,
            tenant_guid=tenant_guid,
            user_guid=user_guid,
            config_guid=config_guid,
            title="Serialization Test",
            message_count=3,
            last_message_at=now,
            created_at=now,
            updated_at=now,
            metadata={"key": "value"}
        )

        # Execute
        data = conversation.model_dump()

        # Assert
        assert data["conversation_id"] == conversation_id
        assert data["tenant_guid"] == tenant_guid
        assert data["title"] == "Serialization Test"
        assert data["message_count"] == 3
        assert data["metadata"] == {"key": "value"}

    def test_conversation_model_validation_errors(self):
        """Test ConversationModel validation with invalid data."""
        # Test missing required field
        with pytest.raises(Exception):  # Pydantic validation error
            ConversationModel(
                conversation_id=uuid4(),
                # Missing other required fields
            )

        # Test invalid UUID
        with pytest.raises(Exception):  # Pydantic validation error
            ConversationModel(
                conversation_id="invalid-uuid",
                tenant_guid=uuid4(),
                user_guid=uuid4(),
                config_guid=uuid4(),
                title="Test",
                message_count=1,
                last_message_at=datetime.now(),
                created_at=datetime.now(),
                updated_at=datetime.now()
            )

        # Test invalid message_count type
        with pytest.raises(Exception):  # Pydantic validation error
            ConversationModel(
                conversation_id=uuid4(),
                tenant_guid=uuid4(),
                user_guid=uuid4(),
                config_guid=uuid4(),
                title="Test",
                message_count="invalid",  # Should be int
                last_message_at=datetime.now(),
                created_at=datetime.now(),
                updated_at=datetime.now()
            )


class TestConversationRequestModel:
    """Test cases for ConversationRequestModel."""

    def test_conversation_request_model_creation_with_all_fields(self):
        """Test creating a ConversationRequestModel with all fields."""
        # Setup
        config_guid = uuid4()
        documents = [{"title": "Doc1", "content": "Content1"}]
        
        data = {
            "config_guid": config_guid,
            "title": "New Conversation",
            "message": "Hello, how can you help me?",
            "metadata": {"source": "web", "user_type": "premium"},
            "documents": documents
        }

        # Execute
        request = ConversationRequestModel(**data)

        # Assert
        assert request.config_guid == config_guid
        assert request.title == "New Conversation"
        assert request.message == "Hello, how can you help me?"
        assert request.metadata == {"source": "web", "user_type": "premium"}
        assert request.documents == documents

    def test_conversation_request_model_creation_with_minimal_fields(self):
        """Test creating a ConversationRequestModel with minimal required fields."""
        # Setup
        config_guid = uuid4()
        
        data = {
            "config_guid": config_guid,
            "title": "Minimal Request",
            "message": "Simple message"
        }

        # Execute
        request = ConversationRequestModel(**data)

        # Assert
        assert request.config_guid == config_guid
        assert request.title == "Minimal Request"
        assert request.message == "Simple message"
        assert request.metadata == {}  # Default empty dict
        assert request.documents is None  # Default None

    def test_conversation_request_model_serialization(self):
        """Test ConversationRequestModel serialization."""
        # Setup
        config_guid = uuid4()
        request = ConversationRequestModel(
            config_guid=config_guid,
            title="Serialization Test",
            message="Test message",
            metadata={"test": "data"},
            documents=[{"doc": "test"}]
        )

        # Execute
        data = request.model_dump()

        # Assert
        assert data["config_guid"] == config_guid
        assert data["title"] == "Serialization Test"
        assert data["message"] == "Test message"
        assert data["metadata"] == {"test": "data"}
        assert data["documents"] == [{"doc": "test"}]

    def test_conversation_request_model_with_aliases(self):
        """Test ConversationRequestModel serialization with aliases."""
        # Setup
        config_guid = uuid4()
        request = ConversationRequestModel(
            config_guid=config_guid,
            title="Alias Test",
            message="Test message"
        )

        # Execute - serialize with aliases
        data = request.model_dump(by_alias=True)

        # Assert - aliases should be used (same as field names in this case)
        assert "config_guid" in data
        assert "title" in data
        assert "message" in data

    def test_conversation_request_model_validation_errors(self):
        """Test ConversationRequestModel validation with invalid data."""
        # Test missing required fields
        with pytest.raises(Exception):  # Pydantic validation error
            ConversationRequestModel(
                config_guid=uuid4(),
                title="Test"
                # Missing required 'message' field
            )

        with pytest.raises(Exception):  # Pydantic validation error
            ConversationRequestModel(
                title="Test",
                message="Test message"
                # Missing required 'config_guid' field
            )

        # Test invalid UUID
        with pytest.raises(Exception):  # Pydantic validation error
            ConversationRequestModel(
                config_guid="invalid-uuid",
                title="Test",
                message="Test message"
            )


class TestMessageRequestModel:
    """Test cases for MessageRequestModel."""

    def test_message_request_model_creation_with_all_fields(self):
        """Test creating a MessageRequestModel with all fields."""
        # Setup
        documents = [{"title": "Doc1", "content": "Content1"}]
        
        data = {
            "message": "What is machine learning?",
            "documents": documents
        }

        # Execute
        request = MessageRequestModel(**data)

        # Assert
        assert request.message == "What is machine learning?"
        assert request.documents == documents

    def test_message_request_model_creation_with_minimal_fields(self):
        """Test creating a MessageRequestModel with minimal required fields."""
        # Setup
        data = {
            "message": "Simple question"
        }

        # Execute
        request = MessageRequestModel(**data)

        # Assert
        assert request.message == "Simple question"
        assert request.documents is None  # Default None

    def test_message_request_model_serialization(self):
        """Test MessageRequestModel serialization."""
        # Setup
        request = MessageRequestModel(
            message="Test message",
            documents=[{"doc": "test"}]
        )

        # Execute
        data = request.model_dump()

        # Assert
        assert data["message"] == "Test message"
        assert data["documents"] == [{"doc": "test"}]

    def test_message_request_model_validation_errors(self):
        """Test MessageRequestModel validation with invalid data."""
        # Test missing required field
        with pytest.raises(Exception):  # Pydantic validation error
            MessageRequestModel(
                # Missing required 'message' field
                documents=[]
            )


class TestConversationWithMessagesModel:
    """Test cases for ConversationWithMessagesModel."""

    def test_conversation_with_messages_model_creation(self):
        """Test creating a ConversationWithMessagesModel."""
        # Setup
        conversation_id = uuid4()
        tenant_guid = uuid4()
        user_guid = uuid4()
        config_guid = uuid4()
        message_id = uuid4()
        now = datetime.now()
        
        conversation_data = {
            "conversation_id": conversation_id,
            "tenant_guid": tenant_guid,
            "user_guid": user_guid,
            "config_guid": config_guid,
            "title": "Test Conversation",
            "message_count": 1,
            "last_message_at": now,
            "created_at": now,
            "updated_at": now,
            "metadata": {}
        }
        
        message_data = {
            "message_id": message_id,
            "conversation_id": conversation_id,
            "role": "user",
            "content": "Hello!",
            "created_at": now
        }
        
        conversation = ConversationModel(**conversation_data)
        message = MessageModel(**message_data)
        
        data = {
            "conversation": conversation,
            "messages": [message]
        }

        # Execute
        result = ConversationWithMessagesModel(**data)

        # Assert
        assert isinstance(result.conversation, ConversationModel)
        assert len(result.messages) == 1
        assert isinstance(result.messages[0], MessageModel)
        assert result.conversation.conversation_id == conversation_id
        assert result.messages[0].message_id == message_id

    def test_conversation_with_messages_model_multiple_messages(self):
        """Test ConversationWithMessagesModel with multiple messages."""
        # Setup
        conversation_id = uuid4()
        tenant_guid = uuid4()
        user_guid = uuid4()
        config_guid = uuid4()
        now = datetime.now()
        
        conversation_data = {
            "conversation_id": conversation_id,
            "tenant_guid": tenant_guid,
            "user_guid": user_guid,
            "config_guid": config_guid,
            "title": "Multi-message Conversation",
            "message_count": 2,
            "last_message_at": now,
            "created_at": now,
            "updated_at": now,
            "metadata": {}
        }
        
        message1_data = {
            "message_id": uuid4(),
            "conversation_id": conversation_id,
            "role": "user",
            "content": "Hello!",
            "created_at": now
        }
        
        message2_data = {
            "message_id": uuid4(),
            "conversation_id": conversation_id,
            "role": "assistant",
            "content": "Hi there! How can I help you?",
            "created_at": now
        }
        
        conversation = ConversationModel(**conversation_data)
        message1 = MessageModel(**message1_data)
        message2 = MessageModel(**message2_data)
        
        data = {
            "conversation": conversation,
            "messages": [message1, message2]
        }

        # Execute
        result = ConversationWithMessagesModel(**data)

        # Assert
        assert len(result.messages) == 2
        assert result.messages[0].role == "user"
        assert result.messages[1].role == "assistant"

    def test_conversation_with_messages_model_serialization(self):
        """Test ConversationWithMessagesModel serialization."""
        # Setup
        conversation_id = uuid4()
        tenant_guid = uuid4()
        user_guid = uuid4()
        config_guid = uuid4()
        message_id = uuid4()
        now = datetime.now()
        
        conversation = ConversationModel(
            conversation_id=conversation_id,
            tenant_guid=tenant_guid,
            user_guid=user_guid,
            config_guid=config_guid,
            title="Serialization Test",
            message_count=1,
            last_message_at=now,
            created_at=now,
            updated_at=now
        )
        
        message = MessageModel(
            message_id=message_id,
            conversation_id=conversation_id,
            role="user",
            content="Test message",
            created_at=now
        )
        
        result = ConversationWithMessagesModel(
            conversation=conversation,
            messages=[message]
        )

        # Execute
        data = result.model_dump()

        # Assert
        assert "conversation" in data
        assert "messages" in data
        assert data["conversation"]["conversation_id"] == conversation_id
        assert len(data["messages"]) == 1
        assert data["messages"][0]["message_id"] == message_id


class TestListConversationsModel:
    """Test cases for ListConversationsModel."""

    def test_list_conversations_model_creation(self):
        """Test creating a ListConversationsModel."""
        # Setup
        conversation_id = uuid4()
        tenant_guid = uuid4()
        user_guid = uuid4()
        config_guid = uuid4()
        now = datetime.now()
        
        conversation_data = {
            "conversation_id": conversation_id,
            "tenant_guid": tenant_guid,
            "user_guid": user_guid,
            "config_guid": config_guid,
            "title": "Test Conversation",
            "message_count": 1,
            "last_message_at": now,
            "created_at": now,
            "updated_at": now,
            "metadata": {}
        }
        
        conversation = ConversationModel(**conversation_data)
        
        data = {
            "conversations": [conversation],
            "total": 1,
            "limit": 10,
            "offset": 0
        }

        # Execute
        result = ListConversationsModel(**data)

        # Assert
        assert len(result.conversations) == 1
        assert isinstance(result.conversations[0], ConversationModel)
        assert result.total == 1
        assert result.limit == 10
        assert result.offset == 0

    def test_list_conversations_model_empty_list(self):
        """Test ListConversationsModel with empty conversations list."""
        # Setup
        data = {
            "conversations": [],
            "total": 0,
            "limit": 10,
            "offset": 0
        }

        # Execute
        result = ListConversationsModel(**data)

        # Assert
        assert len(result.conversations) == 0
        assert result.total == 0

    def test_list_conversations_model_pagination(self):
        """Test ListConversationsModel with pagination data."""
        # Setup
        conversations = []
        for i in range(5):
            conversation_data = {
                "conversation_id": uuid4(),
                "tenant_guid": uuid4(),
                "user_guid": uuid4(),
                "config_guid": uuid4(),
                "title": f"Conversation {i+1}",
                "message_count": i + 1,
                "last_message_at": datetime.now(),
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
                "metadata": {}
            }
            conversations.append(ConversationModel(**conversation_data))
        
        data = {
            "conversations": conversations,
            "total": 25,
            "limit": 5,
            "offset": 10
        }

        # Execute
        result = ListConversationsModel(**data)

        # Assert
        assert len(result.conversations) == 5
        assert result.total == 25
        assert result.limit == 5
        assert result.offset == 10

    def test_list_conversations_model_serialization(self):
        """Test ListConversationsModel serialization."""
        # Setup
        conversation = ConversationModel(
            conversation_id=uuid4(),
            tenant_guid=uuid4(),
            user_guid=uuid4(),
            config_guid=uuid4(),
            title="Serialization Test",
            message_count=1,
            last_message_at=datetime.now(),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        
        result = ListConversationsModel(
            conversations=[conversation],
            total=1,
            limit=10,
            offset=0
        )

        # Execute
        data = result.model_dump()

        # Assert
        assert "conversations" in data
        assert "total" in data
        assert "limit" in data
        assert "offset" in data
        assert len(data["conversations"]) == 1
        assert data["total"] == 1

    def test_list_conversations_model_validation_errors(self):
        """Test ListConversationsModel validation with invalid data."""
        # Test missing required fields
        with pytest.raises(Exception):  # Pydantic validation error
            ListConversationsModel(
                conversations=[],
                total=0
                # Missing limit and offset
            )

        # Test invalid total type
        with pytest.raises(Exception):  # Pydantic validation error
            ListConversationsModel(
                conversations=[],
                total="invalid",  # Should be int
                limit=10,
                offset=0
            )


class TestModelIntegration:
    """Integration tests for conversation models."""

    def test_full_conversation_workflow_models(self):
        """Test a complete workflow using all conversation models."""
        # Setup - Create a conversation request
        config_guid = uuid4()
        request = ConversationRequestModel(
            config_guid=config_guid,
            title="Integration Test Conversation",
            message="Hello, this is a test!",
            metadata={"test": "integration"},
            documents=[{"title": "Test Doc", "content": "Test content"}]
        )

        # Simulate conversation creation response
        conversation_id = uuid4()
        tenant_guid = uuid4()
        user_guid = uuid4()
        now = datetime.now()
        
        conversation = ConversationModel(
            conversation_id=conversation_id,
            tenant_guid=tenant_guid,
            user_guid=user_guid,
            config_guid=config_guid,
            title=request.title,
            message_count=1,
            last_message_at=now,
            created_at=now,
            updated_at=now,
            metadata=request.metadata
        )

        # Create initial message
        message = MessageModel(
            message_id=uuid4(),
            conversation_id=conversation_id,
            role="user",
            content=request.message,
            created_at=now
        )

        # Create conversation with messages
        conversation_with_messages = ConversationWithMessagesModel(
            conversation=conversation,
            messages=[message]
        )

        # Create list response
        list_response = ListConversationsModel(
            conversations=[conversation],
            total=1,
            limit=10,
            offset=0
        )

        # Assert all models work together
        assert conversation_with_messages.conversation.conversation_id == conversation_id
        assert len(conversation_with_messages.messages) == 1
        assert conversation_with_messages.messages[0].content == request.message
        assert list_response.conversations[0].conversation_id == conversation_id
        assert list_response.total == 1

        # Test serialization of the complete workflow
        request_data = request.model_dump()
        conversation_data = conversation.model_dump()
        message_data = message.model_dump()
        full_data = conversation_with_messages.model_dump()
        list_data = list_response.model_dump()

        # Verify serialized data integrity
        assert request_data["config_guid"] == config_guid
        assert conversation_data["conversation_id"] == conversation_id
        assert message_data["message_id"] == message.message_id
        assert full_data["conversation"]["conversation_id"] == conversation_id
        assert list_data["conversations"][0]["conversation_id"] == conversation_id

