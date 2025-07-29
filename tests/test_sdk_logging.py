import pytest
import logging
import os
from unittest.mock import patch
from view_sdk.sdk_logging import (
    set_log_level,
    add_file_logging,
    log_debug,
    log_info,
    log_warning,
    log_error,
    log_critical,
    logger,
)


@pytest.fixture
def temp_log_file(tmp_path):
    return tmp_path / "test.log"


def test_set_log_level():
    # Test setting valid log levels
    set_log_level("DEBUG")
    assert logger.level == logging.DEBUG

    set_log_level("INFO")
    assert logger.level == logging.INFO

    set_log_level("WARNING")
    assert logger.level == logging.WARNING

    # Test invalid log level (should default to INFO)
    set_log_level("INVALID")
    assert logger.level == logging.INFO


def test_add_file_logging(temp_log_file):
    add_file_logging(str(temp_log_file))
    assert os.path.exists(temp_log_file)

    # Test if file handler was added
    file_handlers = [h for h in logger.handlers if isinstance(h, logging.FileHandler)]
    assert file_handlers

    # Clean up
    logger.removeHandler(file_handlers[0])


@patch.object(logger, "debug")
def test_log_debug(mock_debug):
    log_debug("test debug message")
    mock_debug.assert_called_once_with("test debug message")


@patch.object(logger, "info")
def test_log_info(mock_info):
    log_info("test info message")
    mock_info.assert_called_once_with("test info message")


@patch.object(logger, "warning")
def test_log_warning(mock_warning):
    log_warning("test warning message")
    mock_warning.assert_called_once_with("test warning message")


@patch.object(logger, "error")
def test_log_error(mock_error):
    log_error("test error message")
    mock_error.assert_called_once_with("test error message")


@patch.object(logger, "critical")
def test_log_critical(mock_critical):
    log_critical("test critical message")
    mock_critical.assert_called_once_with("test critical message")


def test_logger_formatting(temp_log_file):
    add_file_logging(str(temp_log_file))
    test_message = "test formatting message"
    log_info(test_message)

    with open(temp_log_file) as f:
        log_content = f.read()
        assert test_message in log_content
        # Check for timestamp format
        assert "[INFO]" in log_content

    # Clean up
    file_handlers = [h for h in logger.handlers if isinstance(h, logging.FileHandler)]
    logger.removeHandler(file_handlers[0])
