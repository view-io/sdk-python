# Configuration

Learn how to configure the View AI SDK for your specific needs.

## Basic Configuration

```python
import view_sdk

view_sdk.configure(
    access_key="your_key",
    base_url="localhost",
    tenant_guid="your_tenant_id"
)
```

## Advanced Configuration

```python
view_sdk.configure(
    access_key="your_key",
    base_url="localhost",
    control_plane_url="control.view.io",
    secure=True,
    tenant_guid="your_tenant_id",
    verbose=True,
    timeout=30,
    retry_attempts=3,
    max_connections=10,
    connection_timeout=10,
    log_level="INFO",
    log_file="sdk.log"
)
```

## Configuration Options

- `access_key`: Your API access key
- `base_url`: Base URL for API endpoints
- `control_plane_url`: URL for control plane operations
- `secure`: Enable/disable HTTPS
- `tenant_guid`: Your tenant ID
- `verbose`: Enable/disable verbose logging
- `timeout`: Request timeout in seconds
- `retry_attempts`: Number of retry attempts for failed requests
- `max_connections`: Maximum number of concurrent connections
- `connection_timeout`: Timeout for establishing new connections
- `log_level`: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `log_file`: Path to log file for file logging

## Environment Variables

```bash
export VIEW_ACCESS_KEY="your_key"
export VIEW_BASE_URL="localhost"
export VIEW_TENANT_GUID="your_tenant_id"
export VIEW_LOG_LEVEL="INFO"
export VIEW_LOG_FILE="sdk.log"
```

## Best Practices

1. Use environment variables for sensitive configuration
2. Enable HTTPS in production environments
3. Configure appropriate timeouts for your use case
4. Enable retries for better reliability
5. Set appropriate logging levels for your environment
6. Use file logging in production for audit trails
7. Configure connection limits based on your system resources
