import pytest
from datetime import datetime, timezone
from pydantic import ValidationError
from view_sdk.models.data_repository import DataRepositoryModel

def test_data_repository_minimal_creation():
    """Test creating a DataRepository with minimal required fields."""
    repo = DataRepositoryModel(
        tenant_guid="12345678-1234-5678-1234-567812345678",
        owner_guid="98765432-1234-5678-1234-567812345678"
    )
    assert repo.repository_type == "File"
    assert repo.name == "My file repository"
    assert isinstance(repo.created_utc, datetime)

def test_data_repository_full_creation():
    """Test creating a DataRepository with all fields."""
    data = {
        "id": 1,
        "guid": "12345678-1234-5678-1234-567812345678",
        "tenant_guid": "98765432-1234-5678-1234-567812345678",
        "owner_guid": "abcdef12-1234-5678-1234-567812345678",
        "name": "My file repository",
        "repository_type": "File",
        "use_ssl": False,
        "include_subdirectories": False,
        "disk_directory": "/test/directory/",
        "s3_endpoint_url": "https://s3.amazonaws.com/",
        "s3_base_url": "https://my-bucket.s3.amazonaws.com/",
        "s3_access_key": "test_access_key",
        "s3_secret_key": "test_secret_key",
        "s3_bucket_name": "test-bucket",
        "s3_region": "us-west-2",
        "azure_endpoint_url": "https://account.blob.core.windows.net/",
        "azure_account_name": "testaccount",
        "azure_container_name": "testcontainer",
        "azure_access_key": "test_azure_key",
        "cifs_hostname": "test-server",
        "cifs_username": "test-user",
        "cifs_password": "test-password",
        "cifs_share_name": "test-share",
        "nfs_hostname": "test-nfs-server",
        "nfs_user_id": 1000,
        "nfs_group_id": 1000,
        "nfs_share_name": "test-nfs-share",
        "nfs_version": "4.1",
        "created_utc": datetime.now(timezone.utc)
    }
    repo = DataRepositoryModel(**data)
    assert repo.name == "My file repository"
    assert repo.repository_type == "File"
    assert repo.use_ssl is False
    assert repo.include_subdirectories is False
    assert repo.disk_directory == "/test/directory/"
    assert repo.s3_bucket_name == "test-bucket"
    assert repo.nfs_user_id == 1000

def test_directory_path_normalization():
    """Test that directory paths are normalized correctly."""
    repo = DataRepositoryModel(
        tenant_guid="12345678-1234-5678-1234-567812345678",
        owner_guid="98765432-1234-5678-1234-567812345678",
        disk_directory="C:\\test\\directory\\",
        s3_endpoint_url="http://localhost:9000\\test\\",
        s3_base_url="http://localhost:9000\\bucket\\",
    )
    assert repo.disk_directory == "C:/test/directory/"
    assert repo.s3_endpoint_url == "http://localhost:9000/test/"
    assert repo.s3_base_url == "http://localhost:9000/bucket/"

def test_invalid_nfs_ids():
    """Test validation of NFS user and group IDs."""
    with pytest.raises(ValidationError) as exc_info:
        DataRepositoryModel(
            tenant_guid="12345678-1234-5678-1234-567812345678",
            owner_guid="98765432-1234-5678-1234-567812345678",
            nfs_user_id=-1
        )
    assert "nfs_user_id" in str(exc_info.value)

    with pytest.raises(ValidationError) as exc_info:
        DataRepositoryModel(
            tenant_guid="12345678-1234-5678-1234-567812345678",
            owner_guid="98765432-1234-5678-1234-567812345678",
            nfs_group_id=-1
        )
    assert "nfs_group_id" in str(exc_info.value)

def test_optional_fields():
    """Test that optional fields can be None."""
    repo = DataRepositoryModel(
        tenant_guid="12345678-1234-5678-1234-567812345678",
        owner_guid="98765432-1234-5678-1234-567812345678"
    )
    assert repo.disk_directory is None
    assert repo.s3_endpoint_url is None
    assert repo.s3_base_url is None
    assert repo.s3_access_key is None
    assert repo.s3_secret_key is None
    assert repo.s3_bucket_name is None
    assert repo.s3_region is None
    assert repo.azure_endpoint_url is None
    assert repo.azure_account_name is None
    assert repo.azure_container_name is None
    assert repo.azure_access_key is None
    assert repo.cifs_hostname is None
    assert repo.cifs_username is None
    assert repo.cifs_password is None
    assert repo.cifs_share_name is None
    assert repo.nfs_hostname is None
    assert repo.nfs_share_name is None
    assert repo.nfs_version is None


def test_alias_mapping():
    """Test that field aliases are working correctly."""
    data = {
        "TenantGUID": "12345678-1234-5678-1234-567812345678",
        "OwnerGUID": "98765432-1234-5678-1234-567812345678",
        "Name": "Test Repository",
        "RepositoryType": "S3",
        "UseSsl": False,
        "IncludeSubdirectories": False
    }
    repo = DataRepositoryModel(**data)
    assert repo.tenant_guid == "12345678-1234-5678-1234-567812345678"
    assert repo.owner_guid == "98765432-1234-5678-1234-567812345678"
    assert repo.name == "Test Repository"
    assert repo.repository_type == "S3"
