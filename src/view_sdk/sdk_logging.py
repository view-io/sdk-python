import logging
from typing import Optional

# Set up a logger for the SDK
logger = logging.getLogger("view_sdk")
logger.setLevel(logging.DEBUG)

# Create a console handler with a default log level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter that matches the typical C# log format (e.g., timestamp, level, message)
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)


def set_log_level(level: Optional[str] = "INFO"):
    """
    Set the logging level for the SDK logger.

    :params level (str): The desired logging level (e.g., "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL").
    :return: None
    """
    if level:
        logger.setLevel(getattr(logging, level.upper(), logging.INFO))
        console_handler.setLevel(getattr(logging, level.upper(), logging.INFO))


def add_file_logging(log_file_path: str, level: Optional[str] = "INFO"):
    """Add file logging to the SDK logger.

    :params log_file_path (str): Path to the log file.
    :params level (str): The desired logging level (e.g., "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL").
    :return: None
    """
    global file_handler
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(getattr(logging, level.upper(), logging.INFO))
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


def log_debug(message: str):
    """Log a debug message."""
    logger.debug(message)


def log_info(message: str):
    """Log an info message."""
    logger.info(message)


def log_warning(message: str):
    """Log a warning message."""
    logger.warning(message)


def log_error(message: str):
    """Log an error message."""
    logger.error(message)


def log_critical(message: str):
    """Log a critical message."""
    logger.critical(message)
