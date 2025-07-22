import pytest
from unittest.mock import patch, Mock
from view_sdk.resources.orchestration.data_flow_logs import DataFlowLog
from view_sdk.models.data_flow_log import DataFlowLogModel


@pytest.fixture
def mock_client_with_tenant():
    with patch("view_sdk.resources.orchestration.data_flow_logs.get_client") as mock:
        client = Mock()
        client.tenant_guid = "test-tenant"
        mock.return_value = client
        yield client


@pytest.fixture
def mock_client_without_tenant():
    with patch("view_sdk.resources.orchestration.data_flow_logs.get_client") as mock:
        client = Mock()
        client.tenant_guid = None
        mock.return_value = client
        yield client


def test_data_flow_log_retrieve_all(mock_client_with_tenant):
    test_data = [
        {
            "GUID": "test-guid-1",
            "TenantGUID": "test-tenant",
            "DataFlowGUID": "test-flow-1",
            "RequestGUID": "test-request-1",
        },
        {
            "GUID": "test-guid-2",
            "TenantGUID": "test-tenant",
            "DataFlowGUID": "test-flow-1",
            "RequestGUID": "test-request-1",
        },
    ]
    mock_client_with_tenant.request.return_value = test_data

    results = DataFlowLog.retrieve_all(
        data_flow_guid="test-flow-1", request_guid="test-request-1"
    )

    assert len(results) == 2
    assert all(isinstance(result, DataFlowLogModel) for result in results)
    assert results[0].guid == "test-guid-1"
    assert results[1].guid == "test-guid-2"


def test_data_flow_log_retrieve_all_without_tenant(mock_client_without_tenant):
    with pytest.raises(ValueError) as exc_info:
        DataFlowLog.retrieve_all(
            data_flow_guid="test-flow-1", request_guid="test-request-1"
        )
    assert str(exc_info.value) == "Tenant GUID is required for this resource."


def test_data_flow_log_retrieve_all_missing_guid(mock_client_with_tenant):
    with pytest.raises(ValueError) as exc_info:
        DataFlowLog.retrieve_all(data_flow_guid="", request_guid="test-request-1")
    assert str(exc_info.value) == "data_flow_guid is required"

    with pytest.raises(ValueError) as exc_info:
        DataFlowLog.retrieve_all(data_flow_guid="test-flow-1", request_guid="")
    assert str(exc_info.value) == "request_guid is required"


def test_data_flow_log_retrieve_logfile(mock_client_with_tenant):
    mock_client_with_tenant.request.return_value = "Sample log content"

    result = DataFlowLog.retrieve_logfile(
        data_flow_guid="test-flow-1", request_guid="test-request-1"
    )

    assert result == "Sample log content"
    mock_client_with_tenant.request.assert_called_once()


def test_data_flow_log_retrieve_logfile_without_tenant(mock_client_without_tenant):
    with pytest.raises(ValueError) as exc_info:
        DataFlowLog.retrieve_logfile(
            data_flow_guid="test-flow-1", request_guid="test-request-1"
        )
    assert str(exc_info.value) == "Tenant GUID is required for this resource."


def test_data_flow_log_retrieve_logfile_missing_guid(mock_client_with_tenant):
    with pytest.raises(ValueError) as exc_info:
        DataFlowLog.retrieve_logfile(data_flow_guid="", request_guid="test-request-1")
    assert str(exc_info.value) == "data_flow_guid is required"

    with pytest.raises(ValueError) as exc_info:
        DataFlowLog.retrieve_logfile(data_flow_guid="test-flow-1", request_guid="")
    assert str(exc_info.value) == "request_guid is required"


def test_data_flow_log_retrieve_logfile_error(mock_client_with_tenant):
    mock_client_with_tenant.request.side_effect = Exception("Connection error")

    result = DataFlowLog.retrieve_logfile(
        data_flow_guid="test-flow-1", request_guid="test-request-1"
    )

    assert result is None
