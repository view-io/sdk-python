# Basic Examples

Learn how to use the View AI SDK through practical examples.

## SDK Initialization

```python
import view_sdk

# Basic configuration
view_sdk.configure(
    access_key="your_key",
    base_url="localhost"
)

# Advanced configuration
view_sdk.configure(
    access_key="your_key",
    base_url="localhost",
    secure=True,
    log_level="INFO",
    log_file="sdk.log"
)
```

## Assistant Service Examples

```python
# Chat with AI
assistant = view_sdk.Assistant()
response = assistant.process_chat(
    question="What is AI?",
    temperature=0.7
)

# RAG with context
response = assistant.process_rag(
    question="Analyze this data",
    context_documents=["doc1", "doc2"]
)
```


## Vector Operations

```python
# Create vector repository
repo = view_sdk.configuration.VectorRepository.create(
    name="embeddings_repo",
    dimensionality=1536
)

# Generate embeddings
embeddings = view_sdk.vector.Embeddings()
result = embeddings.generate(
    contents=["text to embed"],
    model="text-embedding-ada-002"
)

# Search vectors
search = view_sdk.vector.Search(repo.guid)
results = search.query(
    vector=result.embeddings[0],
    max_results=10
)
```

## Error Handling

```python
from view_sdk.exceptions import ViewError, ConfigurationError

try:
    result = assistant.process_chat(question="What is AI?")
except ConfigurationError as e:
    print(f"Configuration error: {e}")
except ViewError as e:
    print(f"SDK error: {e}")
finally:
    view_sdk.close_all()
```

## Resource Cleanup

```python
# Always close connections when done
view_sdk.close_all()

# Or use context manager
with view_sdk.configure(access_key="your_key", base_url="localhost"):
    # Your code here
    pass  # Connections automatically closed
```
