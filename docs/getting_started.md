# Getting Started

## Installation

```bash
pip install view-sdk
```

## Quick Start

```python
import view_sdk
from view_sdk import sdk_logging

# Optional: Enable debug logging
sdk_logging.set_log_level(level="DEBUG")

# Configure the SDK
view_sdk.configure(
    access_key="your_key",
    base_url="localhost",
    control_plane_url="control.view.io",  # Optional
    secure=False,  # Use HTTPS instead of HTTP
    tenant_guid="your_tenant_id",  # Optional
    verbose=False  # Enable verbose logging
)

# Your first SDK operation
try:
    node = view_sdk.configuration.Node.create(
        name="Test Node",
        hostname="test.example.com",
        instance_type="StorageServer"
    )
    print(f"Successfully created node: {node.name}")
except view_sdk.exceptions.SdkException as e:
    print(f"Error: {e}")

# Clean up
view_sdk.close_all()
```
