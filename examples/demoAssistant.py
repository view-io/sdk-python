import view_sdk
from view_sdk import assistant
from view_sdk.sdk_configuration import Service
from uuid import UUID

sdk = view_sdk.configure(
    access_key="default",
    base_url="192.168.101.63",  # Replace with your actual server URL
    tenant_guid="00000000-0000-0000-0000-000000000000",
    verbose=True
)


def chatOnlyMessages():
    result = assistant.Assistant.chat_only(
        Messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Are you happy?"},
            {
                "role": "assistant",
                "content": "While I can understand your curiosity, I don't experience emotions or feelings because I'm a machine designed to process information and assist with tasks. However, I'm here to help you to the best of my ability! If you have any questions or need assistance, feel free to ask!"
            },
            {"role": "user", "content": "Are you sure?"}
        ],
        GenerationModel="smollm:135m",
        Temperature=0.1,
        TopP=0.95,
        MaxTokens=75,
        GenerationProvider="ollama",
        Stream=False,
        OllamaHostname="ollama",
        OllamaPort=11434,
    )
    
    # Handle the generator result
    try:
        # For non-streaming requests, the result is yielded and then StopIteration is raised
        actual_result = next(result)
        print("Chat response:", actual_result)
    except StopIteration as e:
        # The actual result is in the StopIteration exception value
        if hasattr(e, 'value') and e.value is not None:
            print("Chat response:", e.value)
        else:
            print("No response received")
    except Exception as e:
        print(f"Error: {e}")


# chatOnlyMessages()


def chat_config():
    result = assistant.Assistant.chat_config(
        "5ba8908d-947b-470e-83aa-57874b5d2d80",
        Messages=[
            {"role": "user", "content": "Do you have Q3 luxetech financials?"},
            {
                "role": "assistant",
                "content": "Unfortunately I do not have context on any documents related to Q3 luxetech financials.",
            },
            {"role": "user", "content": "Are you sure you dont have them?"},
        ],
        Stream=False,
    )
    
    # Handle the generator result
    try:
        # For non-streaming requests, the result is yielded and then StopIteration is raised
        actual_result = next(result)
        print("Chat config response:", actual_result)
    except StopIteration as e:
        # The actual result is in the StopIteration exception value
        if hasattr(e, 'value') and e.value is not None:
            print("Chat config response:", e.value)
        else:
            print("No response received")
    except Exception as e:
        print(f"Error: {e}")


#chat_config()


def chat_rag_messages():
    result = assistant.Assistant.chat_rag_messages(
        Messages=[
            {
                "role": "user",
                "content": "What does the documentation say about embeddings?"
            }
        ],
        Documents=None,
        EnableDocumentFilter=True,
        GenerationModel="smollm:135m",
        GenerationProvider="ollama",
        EmbeddingModel="all-MiniLM-L6-v2",
        MaxResults=20,
        VectorDatabaseName="vectordb",
        VectorDatabaseTable="view-00000000-0000-0000-0000-000000000000",
        VectorDatabaseHostname="pgvector",
        VectorDatabasePort=5432,
        VectorDatabaseUser="postgres",
        VectorDatabasePassword="22222222-2222-2222-2222-222222222222",
        Stream=True,
        Temperature=0.7,
        MaxTokens=256,
        SystemPrompt="Use the following pieces of context to answer the question; if the context is not enough, politely explain that you don't have relevant context. Don't make up answers.",
        Rerank=False,
        RerankModel="cross-encoder/ms-marco-MiniLM-L-6-v2",
        RerankTopK=3,
        UseCitations=False
    )
    
    # Handle the generator result
    try:
        # For non-streaming requests, the result is yielded and then StopIteration is raised
        actual_result = next(result)
        print("Chat RAG response:", actual_result)
    except StopIteration as e:
        # The actual result is in the StopIteration exception value
        if hasattr(e, 'value') and e.value is not None:
            print("Chat RAG response:", e.value)
        else:
            print("No response received")
    except Exception as e:
        print(f"Error: {e}")


chat_rag_messages()


def chat():
    result = assistant.Assistant.rag_LEGACY(
        Question="What information do you have?",
        EmbeddingModel="sentence-transformers/all-MiniLM-L6-v2",
        MaxResults=10,
        VectorDatabaseName="vectordb",
        VectorDatabaseTable="minilm",
        VectorDatabaseHostname="pgvector",
        VectorDatabasePort=5432,
        VectorDatabaseUser="postgres",
        VectorDatabasePassword="password",
        GenerationProvider="ollama",
        GenerationApiKey="",
        GenerationModel="qwen2.5:7b",
        HuggingFaceApiKey="",
        Temperature=0.1,
        MaxTokens=75,
        OllamaHostname="ollama",
        OllamaPort=11434,
        TopP=0.95,
        PromptPrefix="talk like a pirate",
        ContextSort=True,
        SortByMaxSimilarity=True,
        ContextScope=1,
        Rerank=False,
        RerankModel="cross-encoder/ms-marco-MiniLM-L-6-v2",
        RerankTopK=5,
    )
    
    # Handle the streaming generator result
    try:
        # Collect all tokens from the streaming response
        tokens = []
        for token in result:
            tokens.append(token)
        
        # Join all tokens to form the complete response
        complete_response = "".join(tokens)
        print("RAG LEGACY response:", complete_response)
    except Exception as e:
        print(f"Error: {e}")


# chat()

# Uncomment to run conversation workflow demo
# conversationWorkflow()


def unLoadModel():
    result = assistant.Models.load_unload(
        Unload=True,
        ModelName="llama3.1:latest",
        OllamaHostname="ollama",
        OllamaPort=11434,
    )
    print(result)


# unLoadModel()


def deleteModel():
    result = assistant.Models.delete(
        ModelName="llama3.1:latest", OllamaHostname="ollama", OllamaPort=114323
    )
    print(result)


# deleteModel()


def retrieveModel():
    result = assistant.Models.retrieve(
        ModelName="llama3.1:latest", OllamaHostname="ollama", OllamaPort=11434
    )
    print(result)


# retrieveModel()


def listModels():
    result = assistant.Models.retrieve_all(OllamaHostname="ollama", OllamaPort=11434)
    print(result)


# listModels()


def deleteChatThread():
    result = assistant.ChatThread.delete("7e0d729f-6253-4757-82eb-4793c6f95af8")
    print(result)


# deleteChatThread()


def existsChatThread():
    result = assistant.ChatThread.exists("7e0d729f-6253-4757-82eb-4793c6f95af8")
    print(result)


# existsChatThread()


def appendChatThread():
    result = assistant.ChatThread.append(
        "7e0d729f-6253-4757-82eb-4793c6f95af8",
        role="assistant",
        content="The capital of France is Paris.",
        metadata={
            "source_documents": [
                {
                    "content": "Paris is the capital and largest city of France.",
                    "similarity": 0.89,
                }
            ],
            "generation_metrics": {"tokens": 8, "generation_time": 0.5},
        },
    )
    print(result)


# appendChatThread()


def readAllChatThreads():
    result = assistant.ChatThread.retrieve_all()
    print(result)


# readAllChatThreads()


def readChatThread():
    result = assistant.ChatThread.retrieve("7e0d729f-6253-4757-82eb-4793c6f95af8")
    print(result)


# readChatThread()


def createChatThread():
    result = assistant.ChatThread.create(
        Title="Test Chat Thread",
        Description="A test chat thread for development",
        Messages=[
            {
                "role": "user",
                "content": "What is the capital of France?",
                "metadata": {
                    "source": "web interface",
                    "client_timestamp": "2024-02-17T10:30:00Z",
                },
            }
        ],
        AssistantConfigGUID="12345678-1234-5678-1234-567812345678",
        Metadata={"tags": ["test", "development"], "category": "testing"},
    )
    print(result)


# createChatThread()


def deleteConfig():
    result = assistant.Config.delete("c625f9b6-e482-4958-be1f-7e644a524bb5")
    print(result)


# deleteConfig()


def existsConfig():
    result = assistant.Config.exists("c625f9b6-e482-4958-be1f-7e644a524bb5")
    print(result)


# existsConfig()


def updateConfig():
    updateConfig = assistant.Config.update(
        "c625f9b6-e482-4958-be1f-7e644a524bb5",
        Name="Chat Only Blackbeard Assistant [Updated]",
        Description="uses qwen2.5:7b - ollama",
        SystemPrompt="You are Edward Teach (c. 1680 – 22 November 1718), better known as the pirate Blackbeard. Talk like a pirate and only answer questions with period correct answers.",
        GenerationProvider="ollama",
        GenerationApiKey="",
        GenerationModel="qwen2.5:7b",
        Temperature=0.1,
        TopP=0.95,
        MaxTokens=500,
        OllamaHostname="ollama",
        OllamaPort=11434,
        ChatOnly=True,
    )
    print(updateConfig)


# updateConfig()


def readAllConfigs():
    result = assistant.Config.retrieve_all()
    print(result)


# readAllConfigs()


def readConfig():
    result = assistant.Config.retrieve("c625f9b6-e482-4958-be1f-7e644a524bb5")
    print(result)


# readConfig()


def createConfig():
    result = assistant.Config.create(
        Name="Basic RAG Assistant",
        Description="uses qwen2.5:7b - ollama",
        SystemPrompt="Use the provided context to answer questions.",
        EmbeddingModel="sentence-transformers/all-MiniLM-L6-v2",
        MaxResults=10,
        VectorDatabaseName="vectordb",
        VectorDatabaseTable="minilm",
        VectorDatabaseHostname="pgvector",
        VectorDatabasePort=5432,
        VectorDatabaseUser="postgres",
        VectorDatabasePassword="password",
        GenerationProvider="ollama",
        GenerationApiKey="",
        GenerationModel="qwen2.5:7b",
        HuggingFaceApiKey="",
        Temperature=0.1,
        TopP=0.95,
        MaxTokens=500,
        OllamaHostname="ollama",
        OllamaPort=11434,
        ContextSort=True,
        SortByMaxSimilarity=True,
        ContextScope=1,
        Rerank=True,
        RerankModel="cross-encoder/ms-marco-MiniLM-L-6-v2",
        RerankTopK=3,
    )
    print(result)


# createConfig()


def createConversationStreaming():
    """
    Demonstrates creating a new conversation with streaming SSE events.
    Note: Conversation creation is stream-only and always returns SSE events.
    """
    print("=== Creating Conversation with Streaming ===")
    
    try:
        # Create conversation (always streams)
        events = assistant.Conversation.create(
            config_guid=UUID("40712f89-1b66-49f8-96de-2436a09fd6ae"),  # Replace with actual config GUID
            title="Streaming Demo Conversation",
            message="What are the key benefits of using RAG?",
            metadata={
                "source": "demo_script_streaming",
                "category": "testing",
                "priority": "normal"
            },
            documents=None
        )
        
        conversation_id = None
        message_id = None
        
        # Process streaming events
        for event in events:
            print(f"Received event: {event}")
            
            # Extract important information from events
            if isinstance(event, dict):
                # Handle conversation creation event
                if "conversation_id" in event and "tenant_guid" in event and "title" in event:
                    conversation_id = event.get("conversation_id")
                    title = event.get("title")
                    print(f"✓ Conversation created with ID: {conversation_id}, Title: {title}")
                
                # Handle message creation event
                elif "message_id" in event and "role" in event:
                    message_id = event.get("message_id")
                    role = event.get("role")
                    print(f"✓ Message created with ID: {message_id}, Role: {role}")
                
                # Handle pipeline start event
                elif "config_guid" in event and "message_id" in event:
                    print("✓ Processing pipeline started")
                
                # Handle embedding events
                elif "query" in event and "model" in event and "provider" in event:
                    model = event.get("model")
                    provider = event.get("provider")
                    query = event.get("query")
                    print(f"✓ Embedding started with {provider}/{model} for query: '{query}'")
                
                # Handle error events
                elif "error" in event:
                    error = event.get("error")
                    error_type = event.get("error_type", "Unknown")
                    print(f"⚠️ Error occurred ({error_type}): {error}")
                
                # Handle other events
                else:
                    # Check for specific fields to identify event types
                    if "embedding_time_ms" in event:
                        embedding_time = event.get("embedding_time_ms", 0)
                        print(f"✓ Embedding completed in {embedding_time:.2f}ms")
                    elif "source_count" in event:
                        source_count = event.get("source_count", 0)
                        retrieval_time = event.get("retrieval_time_ms", 0)
                        print(f"✓ Search completed: {source_count} sources in {retrieval_time:.2f}ms")
                    elif "token_count" in event:
                        token_count = event.get("token_count", 0)
                        generation_time = event.get("generation_time_ms", 0)
                        tokens_per_second = event.get("tokens_per_second", 0)
                        print(f"✓ Generation completed: {token_count} tokens in {generation_time:.2f}ms ({tokens_per_second:.2f} tokens/sec)")
                    elif "total_time_ms" in event:
                        total_time = event.get("total_time_ms", 0)
                        print(f"✓ Pipeline completed in {total_time:.2f}ms")
        
        print(f"\n=== Streaming Conversation Creation Complete ===")
        print(f"Conversation ID: {conversation_id}")
        print(f"Message ID: {message_id}")
        
        return conversation_id
        
    except Exception as e:
        print(f"Error in streaming conversation creation: {e}")
        return None

# Test streaming mode
# createConversationStreaming()

def listConversations():
    """
    Demonstrates retrieving all conversations with pagination.
    """
    result = assistant.Conversation.retrieve_all(
        limit=10,
        offset=0
    )
    print("List of conversations:", result)
    print(f"Total conversations: {result.total}")
    print(f"Showing {len(result.conversations)} conversations")
    return result


# listConversations()


def retrieveConversation():
    """
    Demonstrates retrieving a specific conversation by ID.
    """
    # Replace with an actual conversation ID from your system
    conversation_id = UUID("cc2ec91c-20da-4886-8845-559cef23eb6d")
    
    try:
        result = assistant.Conversation.retrieve(conversation_id)
        print("Retrieved conversation:", result)
        return result
    except Exception as e:
        print(f"Error retrieving conversation: {e}")
        return None


# retrieveConversation()


def addMessageToConversation():
    """
    Demonstrates adding a message to an existing conversation with streaming.
    Note: add_message is stream-only and returns SSE events.
    """
    # Replace with an actual conversation ID from your system
    conversation_id = UUID("2e68f926-aa5e-43df-b0f3-ba978f419af6")
    
    try:
        print(f"=== Adding Message to Conversation {conversation_id} ===")
        events = assistant.Conversation.add_message(
            conversation_id=conversation_id,
            message="Can you explain the difference between supervised and unsupervised learning?",
            documents=None  # Optional: can include documents for context
        )
        
        message_id = None
        
        # Process streaming events
        for event in events:
            print(f"Received event: {event}")
            
            if isinstance(event, dict):
                # Handle message creation event
                if "message_id" in event and "role" in event:
                    message_id = event.get("message_id")
                    role = event.get("role")
                    print(f"✓ Message created with ID: {message_id}, Role: {role}")
                
                # Handle pipeline events
                elif "query" in event and "model" in event:
                    model = event.get("model")
                    provider = event.get("provider")
                    query = event.get("query")
                    print(f"✓ Processing with {provider}/{model}: '{query}'")
                
                # Handle error events
                elif "error" in event:
                    error = event.get("error")
                    error_type = event.get("error_type", "Unknown")
                    print(f"⚠️ Error occurred ({error_type}): {error}")
                
                # Handle completion events
                elif "token_count" in event:
                    token_count = event.get("token_count", 0)
                    generation_time = event.get("generation_time_ms", 0)
                    tokens_per_second = event.get("tokens_per_second", 0)
                    print(f"✓ Generation completed: {token_count} tokens in {generation_time:.2f}ms ({tokens_per_second:.2f} tokens/sec)")
                
                elif "total_time_ms" in event:
                    total_time = event.get("total_time_ms", 0)
                    print(f"✓ Pipeline completed in {total_time:.2f}ms")
        
        print(f"\n=== Message Addition Complete ===")
        print(f"Message ID: {message_id}")
        return message_id
        
    except Exception as e:
        print(f"Error adding message: {e}")
        return None


# addMessageToConversation()


def getConversationWithMessages():
    """
    Demonstrates retrieving a conversation along with all its messages.
    """
    # Replace with an actual conversation ID from your system
    conversation_id = UUID("2e68f926-aa5e-43df-b0f3-ba978f419af6")
    
    try:
        result = assistant.Conversation.get_with_messages(conversation_id)
        print("Conversation with messages:", result)
        print(f"Conversation title: {result.conversation.title}")
        print(f"Number of messages: {len(result.messages)}")
        
        # Print each message
        for i, message in enumerate(result.messages):
            print(f"Message {i+1} ({message.role}): {message.content[:100]}...")
        
        return result
    except Exception as e:
        print(f"Error retrieving conversation with messages: {e}")
        return None


# getConversationWithMessages()


def deleteConversation():
    """
    Demonstrates deleting a conversation.
    """
    # Replace with an actual conversation ID from your system
    conversation_id = UUID("2e68f926-aa5e-43df-b0f3-ba978f419af6")
    
    try:
        result = assistant.Conversation.delete(conversation_id)
        print("Deleted conversation:", result)
        return result
    except Exception as e:
        print(f"Error deleting conversation: {e}")
        return None


# deleteConversation()


def conversationWorkflow():
    """
    Demonstrates a complete conversation workflow:
    1. Create a conversation
    2. Add messages to it
    3. Retrieve it with messages
    4. List all conversations
    5. Optionally delete it
    """
    print("=== Starting Conversation Workflow Demo ===")
    
    # Step 1: Create a conversation
    print("\n1. Creating a new conversation...")
    # Note: createConversation was removed since create is now stream-only
    # Using createConversationStreaming instead
    conversation_id = createConversationStreaming()
    if not conversation_id:
        print("Failed to create conversation. Stopping workflow.")
        return
    
    print(f"Created conversation with ID: {conversation_id}")
    
    # Step 2: Add a few messages
    print("\n2. Adding messages to the conversation...")
    
    # Add first message (streaming)
    print("Adding first message...")
    message1_events = assistant.Conversation.add_message(
        conversation_id=conversation_id,
        message="What are the main types of machine learning algorithms?"
    )
    message1_id = None
    for event in message1_events:
        if isinstance(event, dict) and "message_id" in event and "role" in event:
            message1_id = event.get("message_id")
            print(f"✓ Added message 1: {message1_id}")
            break
    
    # Add second message (streaming)
    print("Adding second message...")
    message2_events = assistant.Conversation.add_message(
        conversation_id=conversation_id,
        message="Can you provide examples of each type?"
    )
    message2_id = None
    for event in message2_events:
        if isinstance(event, dict) and "message_id" in event and "role" in event:
            message2_id = event.get("message_id")
            print(f"✓ Added message 2: {message2_id}")
            break
    
    # Step 3: Retrieve conversation with all messages
    print("\n3. Retrieving conversation with all messages...")
    full_conversation = assistant.Conversation.get_with_messages(conversation_id)
    print(f"Retrieved conversation '{full_conversation.conversation.title}' with {len(full_conversation.messages)} messages")
    
    # Step 4: List all conversations
    print("\n4. Listing all conversations...")
    all_conversations = listConversations()
    
    # Step 5: Optionally delete (commented out for safety)
    print(f"\n5. Conversation workflow completed. Conversation ID: {conversation_id}")
    print("Note: To delete this conversation, uncomment the delete line below")
    # assistant.Conversation.delete(conversation_id)
    
    return conversation_id


# conversationWorkflow()
