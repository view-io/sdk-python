from unittest.mock import patch
from view_sdk.resources.storage.buckets import Bucket, BucketTags, BucketACL


# Test Bucket.list_objects method
@patch("view_sdk.resources.storage.buckets.super")
def test_bucket_list_objects(mock_super):
    """Test list_objects method."""
    mock_super().retrieve.return_value = {
        "objects": [{"name": "file1.txt", "size": 1024}]
    }

    response = Bucket.list_objects("test-bucket-guid")

    assert response == {"objects": [{"name": "file1.txt", "size": 1024}]}
    mock_super().retrieve.assert_called_with("test-bucket-guid")


# Test Bucket.retrieve_metadata method
@patch("view_sdk.resources.storage.buckets.super")
def test_bucket_retrieve_metadata(mock_super):
    """Test retrieve_metadata method."""
    mock_super().retrieve.return_value = {
        "guid": "test-bucket-guid",
        "name": "test-bucket",
    }

    response = Bucket.retrieve_metadata("test-bucket-guid")

    assert response == {"guid": "test-bucket-guid", "name": "test-bucket"}
    mock_super().retrieve.assert_called_with("test-bucket-guid", md=None)


# Test BucketTags.retrieve method
@patch("view_sdk.resources.storage.buckets.get_client")
def test_bucket_tags_retrieve(mock_get_client):
    """Test BucketTags retrieve method."""
    from unittest.mock import Mock

    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_response = [{"Key": "environment", "Value": "production"}]
    mock_client.request.return_value = mock_response

    response = BucketTags.retrieve("test-bucket-guid")

    assert len(response) == 1
    assert response[0].key == "environment"
    assert response[0].value == "production"

    call_args = mock_client.request.call_args
    assert call_args[0][0] == "GET"
    assert "buckets/test-bucket-guid" in call_args[0][1]


# Test BucketTags.create method
@patch("view_sdk.mixins.get_client")
def test_bucket_tags_create(mock_get_client):
    """Test BucketTags create method."""
    from unittest.mock import Mock

    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_response = [{"Key": "environment", "Value": "production"}]
    mock_client.request.return_value = mock_response

    from view_sdk.models.storage_tag import StorageTagModel

    tags = [StorageTagModel(key="environment", value="production")]
    response = BucketTags.create("test-bucket-guid", tags)

    assert len(response) == 1
    assert response[0].key == "environment"
    assert response[0].value == "production"

    call_args = mock_client.request.call_args
    assert call_args[0][0] == "PUT"
    assert "buckets/test-bucket-guid" in call_args[0][1]


# Test BucketACL.retrieve method
@patch("view_sdk.resources.storage.buckets.get_client")
def test_bucket_acl_retrieve(mock_get_client):
    """Test BucketACL retrieve method."""
    from unittest.mock import Mock

    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_response = [{"Owner": {"guid": "owner1"}, "Users": [], "Entries": []}]
    mock_client.request.return_value = mock_response

    response = BucketACL.retrieve("test-bucket-guid")

    assert len(response) == 1
    assert response[0].owner.guid == "owner1"

    call_args = mock_client.request.call_args
    assert call_args[0][0] == "GET"
    assert "buckets/test-bucket-guid" in call_args[0][1]


# Test BucketACL.create method
@patch("view_sdk.mixins.get_client")
def test_bucket_acl_create(mock_get_client):
    """Test BucketACL create method."""
    from unittest.mock import Mock

    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_response = [
        {
            "GUID": "acl1",
            "TenantGUID": "tenant1",
            "BucketGUID": "bucket1",
            "OwnerGUID": "owner1",
            "UserGUID": "user1",
            "CanonicalUser": "user1",
            "EnableRead": True,
            "EnableReadAcp": False,
            "EnableWrite": False,
            "EnableWriteAcp": False,
            "FullControl": False,
            "CreatedUtc": "2023-01-01T00:00:00Z",
        }
    ]
    mock_client.request.return_value = mock_response

    from view_sdk.models.acl_entry import ACLEntryModel

    acl = ACLEntryModel(
        guid="acl1",
        tenant_guid="tenant1",
        bucket_guid="bucket1",
        owner_guid="owner1",
        user_guid="user1",
        canonical_user="user1",
        enable_read=True,
        enable_read_acp=False,
        enable_write=False,
        enable_write_acp=False,
        full_control=False,
        created_utc="2023-01-01T00:00:00Z",
    )
    response = BucketACL.create("test-bucket-guid", acl)

    assert len(response) == 1
    assert response[0].guid == "acl1"
    assert response[0].user_guid == "user1"

    call_args = mock_client.request.call_args
    assert call_args[0][0] == "PUT"
    assert "buckets/test-bucket-guid" in call_args[0][1]
