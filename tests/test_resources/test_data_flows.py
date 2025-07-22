import pytest
from unittest.mock import patch
from view_sdk.resources.orchestration.data_flows import DataFlow

@patch('view_sdk.resources.orchestration.data_flows.super')
def test_retrieve_default(mock_super):
    mock_super().retrieve.return_value = 'dataflow_result'
    result = DataFlow.retrieve('df-guid')
    assert result == 'dataflow_result'
    mock_super().retrieve.assert_called_with(resource_guid='df-guid')

@patch('view_sdk.resources.orchestration.data_flows.super')
def test_retrieve_with_steps(mock_super):
    mock_super().retrieve.return_value = 'dataflow_result_with_steps'
    result = DataFlow.retrieve('df-guid', with_steps=True)
    assert result == 'dataflow_result_with_steps'
    mock_super().retrieve.assert_called_with(resource_guid='df-guid', inclsub=None)

@patch('view_sdk.resources.orchestration.data_flows.super')
def test_retrieve_request_performance_data(mock_super):
    mock_super().retrieve.return_value = 'perf_data'
    result = DataFlow.retrieve_request_performance_data('df-guid', 'req-guid')
    assert result == 'perf_data'
    assert DataFlow.QUERY_PARAMS == {'request': 'req-guid'}
    mock_super().retrieve.assert_called_with('df-guid/performance')

@patch('view_sdk.resources.orchestration.data_flows.super')
def test_retrieve_request_log_metadata(mock_super):
    mock_super().retrieve.return_value = 'log_metadata'
    result = DataFlow.retrieve_request_log_metadata('df-guid', 'req-guid')
    assert result == 'log_metadata'
    assert DataFlow.QUERY_PARAMS == {'request': 'req-guid'}
    assert DataFlow.MODEL is None
    mock_super().retrieve.assert_called_with('df-guid/logs')

@patch('view_sdk.resources.orchestration.data_flows.super')
def test_retrieve_request_log_file(mock_super):
    mock_super().retrieve.return_value = 'log_file'
    result = DataFlow.retrieve_request_log_file('df-guid', 'req-guid')
    assert result == 'log_file'
    assert DataFlow.QUERY_PARAMS == {'request': 'req-guid'}
    assert DataFlow.MODEL is None
    mock_super().retrieve.assert_called_with('df-guid/logfile') 