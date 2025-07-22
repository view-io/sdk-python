import pytest
from unittest.mock import patch, MagicMock
from view_sdk.resources.storage.multipart_uploads import MultipartUploads
from view_sdk.resources.storage.healthcheck import HealthCheck


@pytest.fixture(autouse=True)
def reset_class_vars():
    MultipartUploads.MODEL = None
    MultipartUploads.QUERY_PARAMS = None
    MultipartUploads.UPDATE_METHOD = None

@patch('view_sdk.resources.storage.multipart_uploads.super')
def test_create(mock_super):
    mock_super().create.return_value = 'created'
    result = MultipartUploads.create('bucket-guid', foo='bar')
    assert result == 'created'
    assert MultipartUploads.MODEL is None
    mock_super().create.assert_called()

@patch('view_sdk.resources.storage.multipart_uploads.super')
def test_retrieve(mock_super):
    mock_super().retrieve.return_value = 'retrieved'
    result = MultipartUploads.retrieve('bucket-guid', 'resource-guid')
    assert result == 'retrieved'
    mock_super().retrieve.assert_called()

@patch('view_sdk.resources.storage.multipart_uploads.super')
def test_retrieve_all(mock_super):
    mock_super().retrieve_all.return_value = ['upload1', 'upload2']
    result = MultipartUploads.retrieve_all('bucket-guid')
    assert result == ['upload1', 'upload2']
    mock_super().retrieve_all.assert_called()

@patch('view_sdk.resources.storage.multipart_uploads.super')
def test_retrieve_part(mock_super):
    mock_super().retrieve.return_value = 'part'
    result = MultipartUploads.retrieve_part('bucket-guid', 'resource-guid', 1)
    assert result == 'part'
    assert MultipartUploads.QUERY_PARAMS == {'part_number': 1}
    mock_super().retrieve.assert_called()

@patch('view_sdk.resources.storage.multipart_uploads.super')
def test_delete_part(mock_super):
    mock_super().delete.return_value = True
    result = MultipartUploads.delete_part('bucket-guid', 'resource-guid', 2)
    assert result is True
    assert MultipartUploads.QUERY_PARAMS == {'part_number': 2}
    mock_super().delete.assert_called()

@patch('view_sdk.resources.storage.multipart_uploads.super')
def test_upload_part(mock_super):
    mock_super().update.return_value = 'uploaded'
    result = MultipartUploads.upload_part('bucket-guid', 'resource-guid', 3, 'somedata')
    assert result == 'uploaded'
    assert MultipartUploads.QUERY_PARAMS == {'part_number': 3}
    assert MultipartUploads.MODEL is None
    mock_super().update.assert_called()

@patch('view_sdk.resources.storage.multipart_uploads.super')
def test_complete_upload(mock_super):
    mock_super().update.return_value = 'completed'
    result = MultipartUploads.complete_upload('bucket-guid', 'resource-guid')
    assert result == 'completed'
    assert MultipartUploads.UPDATE_METHOD == 'POST'
    assert MultipartUploads.MODEL is None
    mock_super().update.assert_called()

@patch.object(MultipartUploads, 'delete', autospec=True)
def test_delete(mock_delete):
    mock_delete.return_value = True
    result = MultipartUploads.delete('bucket-guid', 'resource-guid')
    assert result is True
    mock_delete.assert_called()


def test_healthcheck_resource_attributes():
    assert HealthCheck.PARENT_RESOURCE == "healthcheck"
    assert HealthCheck.RESOURCE_NAME == "storage-rest"

@patch('view_sdk.resources.storage.healthcheck.HealthCheck.check')
def test_healthcheck_api_call(mock_check):
    mock_check.return_value = True
    result = HealthCheck.check()
    assert result is True
    mock_check.assert_called()