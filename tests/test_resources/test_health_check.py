import pytest
from unittest.mock import patch
from view_sdk.resources.health_check.health_check import HealthCheck

@pytest.fixture
def mock_check():
    with patch('view_sdk.resources.health_check.health_check.HealthCheckAPIResource.check') as mock_check:
        mock_check.return_value = {"status": "ok"}
        yield mock_check

def test_healthcheck_configuration(mock_check):
    result = HealthCheck.configuration()
    assert result == {"status": "ok"}
    mock_check.assert_called_once()

def test_healthcheck_storage(mock_check):
    result = HealthCheck.storage()
    assert result == {"status": "ok"}
    mock_check.assert_called_once()

def test_healthcheck_vector(mock_check):
    result = HealthCheck.vector()
    assert result == {"status": "ok"}
    mock_check.assert_called_once()

def test_healthcheck_processor(mock_check):
    result = HealthCheck.processor()
    assert result == {"status": "ok"}
    mock_check.assert_called_once()

def test_healthcheck_assistant(mock_check):
    result = HealthCheck.assistant()
    assert result == {"status": "ok"}
    mock_check.assert_called_once()

def test_healthcheck_crawler(mock_check):
    result = HealthCheck.crawler()
    assert result == {"status": "ok"}
    mock_check.assert_called_once()

def test_healthcheck_lexi(mock_check):
    result = HealthCheck.lexi()
    assert result == {"status": "ok"}
    mock_check.assert_called_once()

def test_healthcheck_embeddings(mock_check):
    result = HealthCheck.embeddings()
    assert result == {"status": "ok"}
    mock_check.assert_called_once()

def test_healthcheck_director(mock_check):
    result = HealthCheck.director()
    assert result == {"status": "ok"}
    mock_check.assert_called_once() 