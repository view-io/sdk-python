# Assistant Service

The Assistant service provides AI-powered assistance capabilities through the View AI SDK.

## Features

- Chat-based interactions with AI
- RAG (Retrieval Augmented Generation) support
- Multiple AI model support
- Streaming responses
- Temperature control for response generation

## Usage

```python
import view_sdk

# Configure the SDK
view_sdk.configure(access_key="your_key", base_url="localhost")

# Initialize Assistant
assistant = view_sdk.Assistant()

# Simple chat request
response = assistant.process_chat(
    question="What is machine learning?",
    temperature=0.7,
    max_tokens=500
)

# RAG request with context
response = assistant.process_rag(
    question="Analyze this document",
    temperature=0.7,
    max_tokens=1000,
    context_documents=["doc1", "doc2"]
)

# Stream responses
for chunk in assistant.process_chat(
    question="Tell me a story",
    stream=True
):
    print(chunk, end="")
```

## Configuration Options

- `temperature`: Controls response randomness (0.0-1.0)
- `max_tokens`: Maximum tokens in response
- `generation_model`: AI model to use
- `generation_provider`: AI provider (OpenAI, Ollama, etc.)
- `stream`: Enable streaming responses

## Best Practices

1. Use appropriate temperature settings:
   - Lower (0.1-0.3) for factual responses
   - Higher (0.7-0.9) for creative content

2. Handle streaming responses properly:
   ```python
   try:
       for chunk in assistant.process_chat(..., stream=True):
           print(chunk, end="")
   except Exception as e:
       print(f"Error: {e}")
   ```

3. Implement proper error handling:
   ```python
   try:
       response = assistant.process_rag(...)
   except view_sdk.exceptions.AssistantError as e:
       print(f"Assistant error: {e}")
   except view_sdk.exceptions.ConfigurationError as e:
       print(f"Configuration error: {e}")
   ```
