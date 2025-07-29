# Code Examples

Explore these examples to learn how to use the View AI SDK effectively.

```{toctree}
:maxdepth: 2

basic_examples
configuration_examples
assistant_examples
vector_examples
advanced_examples
```

## Basic Examples

```python
import view_sdk

# Configure the SDK
view_sdk.configure(
    access_key="your_key",
    base_url="localhost"
)

# Create a node
node = view_sdk.configuration.Node.create(
    name="Test Node",
    hostname="test.example.com"
)

# Create a data repository
repo = view_sdk.configuration.DataRepository.create(
    name="Test Repository",
    description="Test data repository"
)

# Clean up
view_sdk.close_all()
```

See individual example pages for more detailed code samples and use cases.
