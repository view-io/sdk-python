import pytest
from unittest.mock import Mock, patch, MagicMock
from uuid import UUID, uuid4
from datetime import datetime
import json

from view_sdk.resources.assistant.conversation import Conversation
from view_sdk.exceptions import SdkException


@pytest.fixture
def mock_client():
    """Mock client fixture for streaming tests."""
    with (
        patch("view_sdk.resources.assistant.conversation.get_client") as mock_get_client,
        patch("view_sdk.mixins.get_client") as mock_mixin_client,
    ):
        client = Mock()
        client.tenant_guid = "test-tenant-guid"
        mock_get_client.return_value = client
        mock_mixin_client.return_value = client
        yield client


class TestConversationStreamingCreate:
    """Test cases for streaming functionality in Conversation.create."""

    def test_create_streaming_conversation_events(self, mock_client):
        """Test that create method properly handles conversation creation events."""
        # Setup
        conversation_id = str(uuid4())
        tenant_guid = str(uuid4())
        config_guid = uuid4()
        
        mock_events = [
            # Conversation created event
            {
                "conversation_id": conversation_id,
                "tenant_guid": tenant_guid,
                "title": "Test Conversation",
                "created_at": "2024-01-01T12:00:00Z"
            },
            # Message created event
            {
                "message_id": str(uuid4()),
                "role": "user",
                "content": "Hello, world!"
            },
            # Pipeline start event
            {
                "config_guid": str(config_guid),
                "message_id": str(uuid4()),
                "pipeline_started": True
            }
        ]
        mock_client.sse_request.return_value = iter(mock_events)

        # Execute
        result = list(Conversation.create(
            config_guid=config_guid,
            title="Test Conversation",
            message="Hello, world!"
        ))

        # Assert
        assert len(result) == 3
        assert result[0]["conversation_id"] == conversation_id
        assert result[1]["role"] == "user"
        assert result[2]["pipeline_started"] is True

    def test_create_streaming_embedding_events(self, mock_client):
        """Test handling of embedding-related streaming events."""
        # Setup
        config_guid = uuid4()
        mock_events = [
            # Embedding start event
            {
                "query": "Hello, world!",
                "model": "sentence-transformers/all-MiniLM-L6-v2",
                "provider": "huggingface",
                "embedding_started": True
            },
            # Embedding completion event
            {
                "embedding_time_ms": 150.5,
                "embedding_tokens": 3,
                "embedding_dimensions": 384
            }
        ]
        mock_client.sse_request.return_value = iter(mock_events)

        # Execute
        result = list(Conversation.create(
            config_guid=config_guid,
            title="Embedding Test",
            message="Hello, world!"
        ))

        # Assert
        assert len(result) == 2
        assert result[0]["query"] == "Hello, world!"
        assert result[0]["model"] == "sentence-transformers/all-MiniLM-L6-v2"
        assert result[1]["embedding_time_ms"] == 150.5

    def test_create_streaming_search_events(self, mock_client):
        """Test handling of search/retrieval streaming events."""
        # Setup
        config_guid = uuid4()
        mock_events = [
            # Search start event
            {
                "search_query": "Hello, world!",
                "vector_database": "pgvector",
                "search_started": True
            },
            # Search results event
            {
                "source_count": 5,
                "retrieval_time_ms": 75.2,
                "max_similarity": 0.85,
                "min_similarity": 0.62
            }
        ]
        mock_client.sse_request.return_value = iter(mock_events)

        # Execute
        result = list(Conversation.create(
            config_guid=config_guid,
            title="Search Test",
            message="Hello, world!"
        ))

        # Assert
        assert len(result) == 2
        assert result[0]["search_query"] == "Hello, world!"
        assert result[1]["source_count"] == 5
        assert result[1]["retrieval_time_ms"] == 75.2

    def test_create_streaming_generation_events(self, mock_client):
        """Test handling of text generation streaming events."""
        # Setup
        config_guid = uuid4()
        mock_events = [
            # Generation start event
            {
                "generation_model": "gpt-4o-mini",
                "generation_provider": "openai",
                "generation_started": True
            },
            # Token streaming events
            {"token": "Hello"},
            {"token": " there"},
            {"token": "!"},
            # Generation completion event
            {
                "token_count": 3,
                "generation_time_ms": 1200.0,
                "tokens_per_second": 2.5,
                "finish_reason": "stop"
            }
        ]
        mock_client.sse_request.return_value = iter(mock_events)

        # Execute
        result = list(Conversation.create(
            config_guid=config_guid,
            title="Generation Test",
            message="Say hello!"
        ))

        # Assert
        assert len(result) == 5
        assert result[0]["generation_model"] == "gpt-4o-mini"
        assert result[1]["token"] == "Hello"
        assert result[2]["token"] == " there"
        assert result[3]["token"] == "!"
        assert result[4]["token_count"] == 3
        assert result[4]["tokens_per_second"] == 2.5

    def test_create_streaming_error_events(self, mock_client):
        """Test handling of error events in streaming."""
        # Setup
        config_guid = uuid4()
        mock_events = [
            # Normal start
            {"conversation_id": str(uuid4()), "title": "Error Test"},
            # Error event
            {
                "error": "Model not available",
                "error_type": "ModelNotFoundError",
                "error_code": "MODEL_404"
            },
            # Recovery or continuation
            {"status": "retrying", "retry_attempt": 1}
        ]
        mock_client.sse_request.return_value = iter(mock_events)

        # Execute
        result = list(Conversation.create(
            config_guid=config_guid,
            title="Error Test",
            message="This will cause an error"
        ))

        # Assert
        assert len(result) == 3
        assert result[1]["error"] == "Model not available"
        assert result[1]["error_type"] == "ModelNotFoundError"
        assert result[2]["status"] == "retrying"

    def test_create_streaming_complete_pipeline(self, mock_client):
        """Test a complete streaming pipeline with all event types."""
        # Setup
        conversation_id = str(uuid4())
        message_id = str(uuid4())
        config_guid = uuid4()
        
        mock_events = [
            # 1. Conversation creation
            {"conversation_id": conversation_id, "tenant_guid": "test-tenant", "title": "Complete Test"},
            # 2. Message creation
            {"message_id": message_id, "role": "user", "content": "Complete test message"},
            # 3. Pipeline start
            {"config_guid": str(config_guid), "message_id": message_id, "pipeline_started": True},
            # 4. Embedding phase
            {"query": "Complete test message", "model": "all-MiniLM-L6-v2", "provider": "huggingface"},
            {"embedding_time_ms": 120.0, "embedding_tokens": 4},
            # 5. Search phase
            {"search_query": "Complete test message", "vector_database": "pgvector"},
            {"source_count": 3, "retrieval_time_ms": 85.5},
            # 6. Generation phase
            {"generation_model": "gpt-4o-mini", "generation_provider": "openai"},
            {"token": "This"},
            {"token": " is"},
            {"token": " a"},
            {"token": " complete"},
            {"token": " response"},
            {"token": "."},
            {"token_count": 6, "generation_time_ms": 800.0, "tokens_per_second": 7.5},
            # 7. Pipeline completion
            {"total_time_ms": 1005.5, "pipeline_completed": True}
        ]
        mock_client.sse_request.return_value = iter(mock_events)

        # Execute
        result = list(Conversation.create(
            config_guid=config_guid,
            title="Complete Test",
            message="Complete test message"
        ))

        # Assert
        assert len(result) == 16
        
        # Verify conversation creation
        assert result[0]["conversation_id"] == conversation_id
        
        # Verify message creation
        assert result[1]["message_id"] == message_id
        assert result[1]["role"] == "user"
        
        # Verify embedding events
        embedding_events = [e for e in result if "embedding_time_ms" in e]
        assert len(embedding_events) == 1
        assert embedding_events[0]["embedding_time_ms"] == 120.0
        
        # Verify search events
        search_events = [e for e in result if "source_count" in e]
        assert len(search_events) == 1
        assert search_events[0]["source_count"] == 3
        
        # Verify token streaming
        token_events = [e for e in result if "token" in e and "token_count" not in e]
        assert len(token_events) == 6
        tokens = [e["token"] for e in token_events]
        assert tokens == ["This", " is", " a", " complete", " response", "."]
        
        # Verify completion
        completion_events = [e for e in result if "total_time_ms" in e]
        assert len(completion_events) == 1
        assert completion_events[0]["total_time_ms"] == 1005.5


class TestConversationStreamingAddMessage:
    """Test cases for streaming functionality in Conversation.add_message."""

    def test_add_message_streaming_events(self, mock_client):
        """Test that add_message method properly handles streaming events."""
        # Setup
        conversation_id = uuid4()
        message_id = str(uuid4())
        
        mock_events = [
            # Message created event
            {"message_id": message_id, "role": "user", "content": "Follow-up question"},
            # Processing events
            {"query": "Follow-up question", "model": "all-MiniLM-L6-v2", "provider": "huggingface"},
            {"embedding_time_ms": 95.0},
            {"source_count": 2, "retrieval_time_ms": 60.0},
            # Generation events
            {"token": "Here's"},
            {"token": " the"},
            {"token": " answer"},
            {"token_count": 3, "generation_time_ms": 500.0},
            {"total_time_ms": 655.0}
        ]
        mock_client.sse_request.return_value = iter(mock_events)

        # Execute
        result = list(Conversation.add_message(
            conversation_id=conversation_id,
            message="Follow-up question"
        ))

        # Assert
        assert len(result) == 9
        assert result[0]["message_id"] == message_id
        assert result[1]["query"] == "Follow-up question"
        
        # Verify token streaming
        token_events = [e for e in result if "token" in e and "token_count" not in e]
        assert len(token_events) == 3
        tokens = [e["token"] for e in token_events]
        assert tokens == ["Here's", " the", " answer"]

    def test_add_message_streaming_with_documents(self, mock_client):
        """Test add_message streaming with document processing events."""
        # Setup
        conversation_id = uuid4()
        documents = [{"title": "Doc1", "content": "Document content"}]
        
        mock_events = [
            # Message with documents
            {"message_id": str(uuid4()), "role": "user", "documents_count": 1},
            # Document processing
            {"document_processing_started": True, "documents_count": 1},
            {"document_processed": "Doc1", "processing_time_ms": 200.0},
            # Regular pipeline continues
            {"embedding_time_ms": 110.0},
            {"source_count": 4, "retrieval_time_ms": 70.0},
            {"token_count": 5, "generation_time_ms": 600.0},
            {"total_time_ms": 980.0}
        ]
        mock_client.sse_request.return_value = iter(mock_events)

        # Execute
        result = list(Conversation.add_message(
            conversation_id=conversation_id,
            message="Analyze this document",
            documents=documents
        ))

        # Assert
        assert len(result) == 7
        assert result[0]["documents_count"] == 1
        assert result[1]["document_processing_started"] is True
        assert result[2]["document_processed"] == "Doc1"

    def test_add_message_streaming_error_handling(self, mock_client):
        """Test error handling in add_message streaming."""
        # Setup
        conversation_id = uuid4()
        mock_events = [
            {"message_id": str(uuid4()), "role": "user"},
            {"error": "Rate limit exceeded", "error_type": "RateLimitError"},
            {"retry_after_seconds": 30, "status": "rate_limited"}
        ]
        mock_client.sse_request.return_value = iter(mock_events)

        # Execute
        result = list(Conversation.add_message(
            conversation_id=conversation_id,
            message="This will hit rate limit"
        ))

        # Assert
        assert len(result) == 3
        assert result[1]["error"] == "Rate limit exceeded"
        assert result[2]["retry_after_seconds"] == 30

    def test_add_message_streaming_rerank_events(self, mock_client):
        """Test streaming events for reranking functionality."""
        # Setup
        conversation_id = uuid4()
        mock_events = [
            {"message_id": str(uuid4()), "role": "user"},
            {"embedding_time_ms": 100.0},
            {"source_count": 10, "retrieval_time_ms": 80.0},
            # Reranking events
            {"rerank_started": True, "rerank_model": "cross-encoder/ms-marco-MiniLM-L-6-v2"},
            {"rerank_time_ms": 150.0, "reranked_count": 5, "top_k": 3},
            # Generation with reranked context
            {"generation_with_reranked_context": True},
            {"token_count": 8, "generation_time_ms": 700.0},
            {"total_time_ms": 1030.0}
        ]
        mock_client.sse_request.return_value = iter(mock_events)

        # Execute
        result = list(Conversation.add_message(
            conversation_id=conversation_id,
            message="Question requiring reranking"
        ))

        # Assert
        assert len(result) == 8
        rerank_events = [e for e in result if "rerank" in str(e)]
        assert len(rerank_events) >= 2
        assert any("rerank_started" in e for e in result)
        assert any("rerank_time_ms" in e for e in result)


class TestStreamingErrorHandling:
    """Test cases for error handling in streaming scenarios."""

    def test_streaming_connection_error(self, mock_client):
        """Test handling of connection errors during streaming."""
        # Setup
        mock_client.sse_request.side_effect = ConnectionError("Connection lost")

        # Execute & Assert
        with pytest.raises(ConnectionError, match="Connection lost"):
            list(Conversation.create(
                config_guid=uuid4(),
                title="Connection Test",
                message="This will fail"
            ))

    def test_streaming_timeout_error(self, mock_client):
        """Test handling of timeout errors during streaming."""
        # Setup
        mock_client.sse_request.side_effect = TimeoutError("Request timed out")

        # Execute & Assert
        with pytest.raises(TimeoutError, match="Request timed out"):
            list(Conversation.add_message(
                conversation_id=uuid4(),
                message="This will timeout"
            ))

    def test_streaming_malformed_event(self, mock_client):
        """Test handling of malformed streaming events."""
        # Setup - Mix of valid and invalid events
        mock_events = [
            {"conversation_id": str(uuid4()), "title": "Test"},  # Valid
            "invalid_event_string",  # Invalid - should be handled gracefully
            {"token": "Hello"},  # Valid
            None,  # Invalid - should be handled gracefully
            {"token": "World"}  # Valid
        ]
        mock_client.sse_request.return_value = iter(mock_events)

        # Execute
        result = list(Conversation.create(
            config_guid=uuid4(),
            title="Malformed Test",
            message="Test message"
        ))

        # Assert - Should handle malformed events gracefully
        assert len(result) == 5  # All events should be yielded as-is
        assert result[0]["conversation_id"] is not None
        assert result[1] == "invalid_event_string"
        assert result[2]["token"] == "Hello"
        assert result[3] is None
        assert result[4]["token"] == "World"

    def test_streaming_empty_response(self, mock_client):
        """Test handling of empty streaming response."""
        # Setup
        mock_client.sse_request.return_value = iter([])

        # Execute
        result = list(Conversation.create(
            config_guid=uuid4(),
            title="Empty Test",
            message="This returns nothing"
        ))

        # Assert
        assert len(result) == 0

    def test_streaming_partial_failure(self, mock_client):
        """Test handling of partial failures in streaming."""
        # Setup - Start successfully but fail midway
        def failing_generator():
            yield {"conversation_id": str(uuid4()), "title": "Partial Test"}
            yield {"message_id": str(uuid4()), "role": "user"}
            raise Exception("Midway failure")
        
        mock_client.sse_request.return_value = failing_generator()

        # Execute & Assert
        with pytest.raises(Exception, match="Midway failure"):
            list(Conversation.create(
                config_guid=uuid4(),
                title="Partial Test",
                message="This will fail midway"
            ))


class TestStreamingPerformance:
    """Test cases for streaming performance characteristics."""

    def test_streaming_large_response(self, mock_client):
        """Test handling of large streaming responses."""
        # Setup - Simulate a large response with many tokens
        mock_events = []
        
        # Add initial events
        mock_events.append({"conversation_id": str(uuid4()), "title": "Large Response Test"})
        mock_events.append({"message_id": str(uuid4()), "role": "user"})
        
        # Add many token events (simulating a long response)
        for i in range(100):
            mock_events.append({"token": f"token_{i}"})
        
        # Add completion event
        mock_events.append({"token_count": 100, "generation_time_ms": 5000.0})
        
        mock_client.sse_request.return_value = iter(mock_events)

        # Execute
        result = list(Conversation.create(
            config_guid=uuid4(),
            title="Large Response Test",
            message="Generate a very long response"
        ))

        # Assert
        assert len(result) == 103  # 2 initial + 100 tokens + 1 completion
        token_events = [e for e in result if "token" in e and "token_count" not in e]
        assert len(token_events) == 100
        assert token_events[0]["token"] == "token_0"
        assert token_events[99]["token"] == "token_99"

    def test_streaming_rapid_events(self, mock_client):
        """Test handling of rapid successive events."""
        # Setup - Many events in quick succession
        mock_events = []
        for i in range(50):
            mock_events.append({"event_id": i, "timestamp": f"2024-01-01T12:00:{i:02d}Z"})
        
        mock_client.sse_request.return_value = iter(mock_events)

        # Execute
        result = list(Conversation.add_message(
            conversation_id=uuid4(),
            message="Rapid events test"
        ))

        # Assert
        assert len(result) == 50
        assert result[0]["event_id"] == 0
        assert result[49]["event_id"] == 49

    def test_streaming_memory_efficiency(self, mock_client):
        """Test that streaming doesn't accumulate all events in memory."""
        # Setup - This test verifies that we can handle streaming without
        # loading all events into memory at once (generator behavior)
        def large_event_generator():
            for i in range(1000):
                yield {"large_event": i, "data": "x" * 1000}  # 1KB per event
        
        mock_client.sse_request.return_value = large_event_generator()

        # Execute - Process events one by one without storing all
        processed_count = 0
        for event in Conversation.create(
            config_guid=uuid4(),
            title="Memory Test",
            message="Memory efficiency test"
        ):
            processed_count += 1
            # Verify we can access the event
            assert "large_event" in event
            # Only process first 10 to avoid long test
            if processed_count >= 10:
                break

        # Assert
        assert processed_count == 10

