import pytest
from datetime import datetime, timezone
from view_sdk.models.object_lock import ObjectLockModel


def test_object_lock_create_valid():
    data = {
        "guid": "123e4567-e89b-12d3-a456-426614174000",
        "tenant_guid": "abc123-e89b-12d3-a456-426614174000",
        "node_guid": "def456-e89b-12d3-a456-426614174000",
        "bucket_guid": "ghi789-e89b-12d3-a456-426614174000",
        "owner_guid": "jkl012-e89b-12d3-a456-426614174000",
        "object_guid": "mno345-e89b-12d3-a456-426614174000",
        "key": "test-key",
        "version": "test-version",
        "is_read_lock": True,
        "is_write_lock": False,
        "created_utc": datetime(2023, 4, 1, 12, 0, 0, tzinfo=timezone.utc),
    }

    lock = ObjectLockModel(**data)
    assert lock.guid == "123e4567-e89b-12d3-a456-426614174000"
    assert lock.tenant_guid == "abc123-e89b-12d3-a456-426614174000"
    assert lock.node_guid == "def456-e89b-12d3-a456-426614174000"
    assert lock.bucket_guid == "ghi789-e89b-12d3-a456-426614174000"
    assert lock.owner_guid == "jkl012-e89b-12d3-a456-426614174000"
    assert lock.object_guid == "mno345-e89b-12d3-a456-426614174000"
    assert lock.key == "test-key"
    assert lock.version == "test-version"
    assert lock.is_read_lock
    assert not lock.is_write_lock
    assert lock.created_utc == datetime(2023, 4, 1, 12, 0, 0, tzinfo=timezone.utc)


def test_object_lock_invalid_data():
    with pytest.raises(ValueError):
        ObjectLockModel(guid="invalid-guid", key=None, version=None)
