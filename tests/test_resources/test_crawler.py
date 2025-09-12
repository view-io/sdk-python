import pytest
from unittest.mock import patch, Mock
from view_sdk.resources.crawler.crawl_operations import CrawlOperation
from view_sdk.models.crawl_operation_request import CrawlOperationRequestModel


@pytest.fixture
def valid_crawl_operation_request():
    return CrawlOperationRequestModel(name="Test Operation").model_dump(
        mode="json", by_alias=True
    )


@patch("view_sdk.resources.crawler.crawl_operations.get_client")
def test_crawl_operation_start(mock_get_client, valid_crawl_operation_request):
    mock_client = Mock()
    mock_get_client.return_value = mock_client

    mock_client.request.return_value = valid_crawl_operation_request

    response = CrawlOperation.start(
        operation_guid="test_guid", **valid_crawl_operation_request
    )

    assert response == valid_crawl_operation_request

    call_args = mock_client.request.call_args
    assert call_args[0][0] == "POST"
    assert "/crawloperations/test_guid/start" in call_args[0][1]


@patch("view_sdk.resources.crawler.crawl_operations.get_client")
def test_crawl_operation_stop(mock_get_client, valid_crawl_operation_request):
    mock_client = Mock()
    mock_get_client.return_value = mock_client

    mock_client.request.return_value = valid_crawl_operation_request

    response = CrawlOperation.stop(
        operation_guid="test_guid", **valid_crawl_operation_request
    )

    assert response == valid_crawl_operation_request

    call_args = mock_client.request.call_args
    assert call_args[0][0] == "POST"
    assert "/crawloperations/test_guid/stop" in call_args[0][1]


@patch("view_sdk.resources.crawler.crawl_operations.get_client")
def test_crawl_operation_enumerate(mock_get_client):
    mock_client = Mock()
    mock_get_client.return_value = mock_client

    mock_response = {"operation_guid": "test_guid", "status": "enumerated"}
    mock_client.request.return_value = mock_response

    response = CrawlOperation.enumerateCrawlOperation(operation_guid="test_guid")

    assert response == mock_response

    call_args = mock_client.request.call_args
    assert call_args[0][0] == "GET"
    # The URL will be v1.0/tenants//test_guid/enumeration due to empty PARENT_RESOURCE
    assert "test_guid/enumeration" in call_args[0][1]
