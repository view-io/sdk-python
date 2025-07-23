<img src="assets/view_logo.png" height="48">

# Python SDK for View AI

<!-- [![PyPI version](https://badge.fury.io/py/view-sdk.svg)](https://badge.fury.io/py/view-sdk)
[![Downloads](https://static.pepy.tech/badge/view-sdk)](https://pepy.tech/project/view-sdk) -->

View AI enables organizations to rapidly deploy conversational AI experiences and yield instant insights. This SDK provides a simplified interface for consuming View AI configuration services in Python applications.

## License

View software is licensed under the [Fair Core License (FCL)](https://fcl.dev/) with graduation after two years to an Apache 2.0 license. Use of the software requires acceptance of the license terms found in the file `LICENSE.md`.

## Requirements

- Python 3.8 or higher
- pip package manager

### Dependencies

- `httpx`: For making HTTP requests
- `pydantic`: For data validation and serialization
- `typing`: For type hints

## Installation

Install the SDK using pip:

```bash
pip install view-sdk
```

Install the SDK along with LiteGraph SDK:

```bash
pip install view-sdk[litegraph_sdk]
```

## Getting Started

### Basic Configuration

```python
import view_sdk
import litegraph_sdk
from view_sdk import sdk_logging

# Optional: Enable debug logging
sdk_logging.set_log_level(level="DEBUG")

# Configure the View SDK
view_sdk.configure(
    access_key="your_key",
    base_url="localhost",
    control_plane_url="control.view.io",  # Optional
    secure=False,  # Use HTTPS instead of HTTP
    tenant_guid="your_tenant_id",  # Optional
    verbose=False  # Enable verbose logging
)

# Configure the LiteGraph SDK
litegraph_sdk.configure(
    access_key="your_litegraph_key",
    endpoint="http://your-litegraph-endpoint",
    tenant_guid="your_tenant_id"
)
```

## Available Services

The SDK provides access to the following services:

- **Assistant**: AI assistant management and interactions
- **Configuration**: System configuration and settings management
  - Blobs, Credentials, Data Repositories
  - Encryption Keys, Graph Repositories
  - Nodes, Tenants, Users
  - Vector Repositories, Webhooks
- **Graphs**: Graph database operations
  - Create and manage graphs
  - Add and connect nodes with edges
  - Support for graph data and metadata
  - Integration with LiteGraph for advanced graph operations
- **Lexi**: Natural language processing capabilities
- **Orchestration**: Workflow and process orchestration
- **Processor**: Data processing and transformation
- **Semantic**: Semantic analysis and processing
- **Storage**: Data storage operations
- **Vector**: Vector operations and similarity search
- **IngestQueue**: Manage ingest queue operations

### Example Usage

```python
from view_sdk.exceptions import SdkException

try:
    # Working with Blobs
    # Enumerate all blobs
    blobs = view_sdk.configuration.Blob.enumerate()
    print(f"Retrieved blobs: {blobs}")

    # Working with Source Documents
    # Retrieve a specific source document
    src_doc = view_sdk.lexi.SourceDocument.retrieve(
        resource_guid="document-guid",
        collection_guid="collection-guid"
    )
    print(f"Retrieved source document: {src_doc}")

    # Working with Vector Repositories
    # Enumerate documents with detailed parameters
    vector_docs = view_sdk.vector.Repositories.enumerate_documents(
        repo_guid="example-vector-repository",
        max_results=5,
        include_data=False,
        ordering="CreatedDescending"
    )
    print(f"Vector repository documents: {vector_docs}")

    # Get vector repository statistics
    repo_stats = view_sdk.vector.Repositories.get_statistics(
        repo_guid="example-vector-repository"
    )
    print(f"Repository statistics: {repo_stats}")

    # Working with Triggers
    # List all triggers
    all_triggers = view_sdk.orchestration.Trigger.retrieve_all()
    print(f"Found {len(all_triggers)} triggers")
    if all_triggers:
        print(f"First trigger GUID: {all_triggers[0].guid}")

    # Alternative way to enumerate documents using filters dictionary
    filters = {
        "MaxResults": 5,
        "IncludeData": False,
        "Ordering": "CreatedDescending",
    }
    vector_docs = view_sdk.vector.Repositories.enumerate_documents(
        repo_guid="example-vector-repository",
        **filters
    )

except SdkException as e:
    print(f"Error: {e}")

# Clean up resources
view_sdk.close_all()  # Close all active client connections
```

### Example Usage with Graphs

```python
# Working with Graphs
try:
    # Create a new graph
    graph = view_sdk.graphs.Graph.create(name="My Graph")
    print(f"Created graph: {graph}")

    # Add nodes to the graph
    node1 = view_sdk.graphs.Node.create(
        graph_guid=graph.guid,
        name="Node 1"
    )
    node2 = view_sdk.graphs.Node.create(
        graph_guid=graph.guid,
        name="Node 2"
    )

    # Connect nodes with an edge
    edge = view_sdk.graphs.Edge.create(
        graph_guid=graph.guid,
        from_node=node1.guid,
        to_node=node2.guid,
        name="Connection",
        cost=1
    )

    # Export graph in GEXF format
    gexf_data = view_sdk.graphs.Graph.export_gexf(
        resource_guid=graph.guid
    )
    print(f"GEXF export: {gexf_data}")

except view_sdk.exceptions.SdkException as e:
    print(f"Error working with graphs: {e}")
```

## Error Handling

The SDK provides comprehensive error handling with specific exception types:

```python
try:
    # Your SDK operations here
    pass
except view_sdk.exceptions.AuthenticationError as e:
    print(f"Authentication failed: {e}")
except view_sdk.exceptions.AuthorizationError as e:
    print(f"Authorization failed: {e}")
except view_sdk.exceptions.ResourceNotFoundError as e:
    print(f"Resource not found: {e}")
except view_sdk.exceptions.ValidationError as e:
    print(f"Validation error: {e}")
except view_sdk.exceptions.TimeoutError as e:
    print(f"Request timed out: {e}")
except view_sdk.exceptions.BadGatewayError as e:
    print(f"Bad gateway error: {e}")
except view_sdk.exceptions.NoEmbeddingsConnectivityError as e:
    print(f"Cannot connect to embeddings service: {e}")
except view_sdk.exceptions.NoVectorConnectivityError as e:
    print(f"Cannot connect to vector store: {e}")
except view_sdk.exceptions.SdkException as e:
    print(f"General SDK error: {e}")
```

## Logging

The SDK provides flexible logging capabilities:

```python
from view_sdk import sdk_logging

# Set console logging level
sdk_logging.set_log_level("DEBUG")  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL

# Add file logging
sdk_logging.add_file_logging("view_sdk.log", level="INFO")
```

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## Support

For support, please:
1. Check the [documentation](docs/)
2. Open an issue on GitHub
3. Contact View AI support

## Development

### Setting up Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality. To set up pre-commit:

```bash
# Install pre-commit
pip install pre-commit

# Install the pre-commit hooks
pre-commit install

# (Optional) Run pre-commit on all files
pre-commit run --all-files
```

The pre-commit hooks will run automatically on `git commit`. They help maintain:

- Code formatting (using ruff)
- Import sorting
- Code quality checks
- And other project-specific checks

### Running Tests

The project uses `tox` for running tests in isolated environments. Make sure you have tox installed:

```bash
pip install tox
```

To run the default test environment:

```bash
tox
```

To run specific test environments:

```bash
# Run only the tests
tox -e default

# Run tests with coverage report
tox -- --cov view_sdk --cov-report term-missing

# Build documentation
tox -e docs

# Build the package
tox -e build

# Clean build artifacts
tox -e clean
```

### Development Installation

For development, you can install the package with all test dependencies:

```bash
pip install -e ".[testing]"
```

#### Building and Installing LiteGraph SDK

For development and testing purposes, you'll need to build and install the litegraph SDK:

```bash
# Navigate to litegraph SDK directory
cd ../litegraph_sdk

# Build the wheel using tox
tox -e build

# Note the path to the generated .whl file in dist/
# Update the absolute path in setup.cfg's [options.extras_require] section:
# testing =
#     ...
#     litegraph_sdk @ file://localhost//absolute/path/to/litegraph_sdk-x.y.z-py3-none-any.whl

# Return to view SDK directory
cd ../python_sdk_viewio

# Install with testing dependencies (including litegraph SDK)
pip install -e ".[testing]"
```

### Viewing Documentation

To build and view the SDK documentation locally:

```bash
# Build the documentation
tox -e docs

# Navigate to the built documentation
cd docs/_build/html

# Start a local server
python -m http.server
```

Then open your web browser and visit `http://localhost:8000` to view the documentation.

### Publishing

The project uses `tox` to automate the publishing process. To publish a new version:

1. Update version in `setup.cfg`
2. Run the publishing environments:

```bash
# Run tests and build checks before publishing
tox -e test,build

# Build and publish to PyPI
tox -e publish

# Build and publish to Test PyPI
tox -e publish-test
```

The publish environments handle:
- Running all tests
- Building source and wheel distributions
- Checking package metadata and README
- Uploading to PyPI/Test PyPI

Make sure you have the following environment variables set for authentication:
```bash
# For PyPI
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=your_pypi_token

# For Test PyPI
export TWINE_TEST_USERNAME=__token__
export TWINE_TEST_PASSWORD=your_testpypi_token
```

For more information about publishing Python packages, see the [Python Packaging User Guide](https://packaging.python.org/tutorials/packaging-projects/).

## Feedback and Issues

Have feedback or found an issue? Please file an issue in our GitHub repository.

## Documentation

For detailed API documentation and examples, visit [View Documentation](https://docs.view.io).

## Version History

Please refer to [CHANGELOG.md](CHANGELOG.md) for a detailed version history.
