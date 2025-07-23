from unittest.mock import patch
from view_sdk.resources.storage.objects import Object, ObjectTags, ObjectACL
from datetime import datetime

# Object tests
@patch('view_sdk.resources.storage.objects.super')
def test_object_retrieve(mock_super):
    mock_super().retrieve.return_value = 'retrieved'
    result = Object.retrieve('bucket1', 'obj1')
    assert result == 'retrieved'
    mock_super().retrieve.assert_called_with('obj1', bucket_guid='bucket1')

@patch('view_sdk.resources.storage.objects.super')
def test_object_retrieve_metadata(mock_super):
    mock_super().retrieve.return_value = 'metadata'
    result = Object.retrieve_metadata('bucket1', 'obj1')
    assert result == 'metadata'
    assert Object.MODEL is not None
    assert Object.QUERY_PARAMS == {'md': None}
    mock_super().retrieve.assert_called_with('obj1', bucket_guid='bucket1')

@patch('view_sdk.resources.storage.objects.super')
def test_object_set_expiration(mock_super):
    mock_super().update.return_value = 'updated'
    dt = datetime.now()
    result = Object.set_expiration('bucket1', 'obj1', dt)
    assert result == 'updated'
    assert Object.MODEL is not None
    assert Object.QUERY_PARAMS == {'expiration': None}
    mock_super().update.assert_called_with('obj1', bucket_guid='bucket1', expiration=dt, data={'ExpirationUtc': dt})

@patch('view_sdk.resources.storage.objects.super')
def test_object_retrieve_range(mock_super):
    mock_super().retrieve.return_value = 'range'
    result = Object.retrieve_range('bucket1', 'obj1', 0, 99)
    assert result == 'range'
    mock_super().retrieve.assert_called_with('obj1', bucket_guid='bucket1', headers={'Range': 'bytes=0-99'})

@patch('view_sdk.resources.storage.objects.super')
def test_object_write_non_chunked(mock_super):
    mock_super().update.return_value = 'written'
    result = Object.write_non_chunked('bucket1', 'obj1', 'somedata')
    assert result == 'written'
    mock_super().update.assert_called_with('obj1', bucket_guid='bucket1', data='somedata', headers={'Content-Type': 'text/plain'})

@patch('view_sdk.resources.storage.objects.super')
def test_object_write_chunked(mock_super):
    mock_super().update.return_value = 'written'
    result = Object.write_chunked('bucket1', 'obj1', 'somedata')
    assert result == 'written'
    mock_super().update.assert_called_with('obj1', bucket_guid='bucket1', data='somedata', headers={'Content-Type': 'text/plain', 'x-amz-content-sha256': 'STREAMING'})

@patch('view_sdk.resources.storage.objects.super')
def test_object_delete(mock_super):
    mock_super().delete.return_value = 'deleted'
    result = Object.delete('bucket1', 'obj1')
    assert result == 'deleted'
    mock_super().delete.assert_called_with('obj1', bucket_guid='bucket1')

# ObjectTags tests
@patch('view_sdk.resources.storage.objects.super')
def test_objecttags_create_tags(mock_super):
    mock_super().update.return_value = 'tags_created'
    result = ObjectTags.create_tags('bucket1', 'obj1', ['tag1'])
    assert result == 'tags_created'
    mock_super().update.assert_called_with('obj1', bucket_guid='bucket1', data=['tag1'])

@patch('view_sdk.resources.storage.objects.super')
def test_objecttags_read_tags(mock_super):
    mock_super().retrieve.return_value = 'tags_read'
    result = ObjectTags.read_tags('bucket1', 'obj1')
    assert result == 'tags_read'
    assert ObjectTags.MODEL is None
    mock_super().retrieve.assert_called_with('obj1', bucket_guid='bucket1')

@patch('view_sdk.resources.storage.objects.super')
def test_objecttags_delete_tags(mock_super):
    mock_super().delete.return_value = 'tags_deleted'
    result = ObjectTags.delete_tags('bucket1', 'obj1')
    assert result == 'tags_deleted'
    mock_super().delete.assert_called_with('obj1', bucket_guid='bucket1')

# ObjectACL tests
@patch('view_sdk.resources.storage.objects.super')
def test_objectacl_create_acl(mock_super):
    mock_super().update.return_value = 'acl_created'
    result = ObjectACL.create_acl('bucket1', 'obj1', 'acl')
    assert result == 'acl_created'
    assert ObjectACL.MODEL is None
    mock_super().update.assert_called_with('obj1', bucket_guid='bucket1', data='acl')

@patch('view_sdk.resources.storage.objects.super')
def test_objectacl_read_acl(mock_super):
    mock_super().retrieve.return_value = 'acl_read'
    result = ObjectACL.read_acl('bucket1', 'obj1')
    assert result == 'acl_read'
    assert ObjectACL.MODEL is None
    mock_super().retrieve.assert_called_with('obj1', bucket_guid='bucket1')

@patch('view_sdk.resources.storage.objects.super')
def test_objectacl_delete_acl(mock_super):
    mock_super().delete.return_value = 'acl_deleted'
    result = ObjectACL.delete_acl('bucket1', 'obj1')
    assert result == 'acl_deleted'
    mock_super().delete.assert_called_with('obj1', bucket_guid='bucket1') 