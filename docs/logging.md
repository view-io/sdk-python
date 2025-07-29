# Logging

The SDK provides flexible logging capabilities to help you debug and monitor your applications.

## Console Logging

```python
from view_sdk import sdk_logging

# Set console logging level
sdk_logging.set_log_level("DEBUG")  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
```

## File Logging

```python
# Add file logging alongside console logging
sdk_logging.add_file_logging("view_sdk.log", level="INFO")
```

## Log Levels

- `DEBUG`: Detailed information for debugging
- `INFO`: General information about program execution
- `WARNING`: Indicates a potential problem
- `ERROR`: A more serious problem
- `CRITICAL`: A critical error that may prevent the program from running

## Best Practices

1. Use appropriate log levels for different types of messages
2. Enable DEBUG logging during development
3. Use INFO or WARNING for production environments
4. Implement file logging for persistent log storage
5. Rotate log files to manage disk space
