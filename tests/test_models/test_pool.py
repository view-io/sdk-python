import pytest
from datetime import datetime, timezone
from pydantic import ValidationError
from view_sdk.models.pool import StoragePool
from view_sdk.enums.compression_type_enum import CompressionTypeEnum
from view_sdk.enums.object_write_mode_enum import ObjectWriteModeEnum

def test_create_complete_storage_pool():
    """Test creating a storage pool with all fields populated."""
    data = {
        "guid": "123e4567-e89b-12d3-a456-426614174000",
        "tenant_guid": "987fcdeb-51d3-a456-426614174000",
        "encryption_key_guid": "abcd1234-e89b-12d3-a456-426614174000",
        "name": "Test Pool",
        "provider": "S3",
        "write_mode": "KEY",
        "use_ssl": True,
        "access_key": "AKIAXXXXXXXXXXXXXXXX",
        "secret_key": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "aws_region": "us-west-2",
        "aws_bucket": "test-bucket",
        "aws_base_domain": "s3.amazonaws.com",
        "disk_directory": "/data/storage",
        "azure_account": "testaccount",
        "azure_container": "testcontainer",
        "compress": "Gzip",
        "enable_read_caching": True,
        "date_time": "2024-01-01T00:00:00Z"
    }
    
    pool = StoragePool(**data)
    assert pool.guid == data["guid"]
    assert pool.tenant_guid == data["tenant_guid"]
    assert pool.name == data["name"]
    assert pool.provider == data["provider"]
    assert pool.write_mode == ObjectWriteModeEnum.KEY
    assert pool.use_ssl is True
    assert pool.access_key == data["access_key"]
    assert pool.secret_key == data["secret_key"]
    assert pool.aws_region == data["aws_region"]
    assert pool.aws_bucket == data["aws_bucket"]
    assert pool.compress == CompressionTypeEnum.Gzip
    assert pool.enable_read_caching is True
    assert pool.date_time == datetime(2024, 1, 1, 0, 0, 0, tzinfo=timezone.utc)

def test_compression_type_validation():
    """Test validation of compression type enum."""
    # Valid compression types
    for compress_type in CompressionTypeEnum:
        pool = StoragePool(compress=compress_type)
        assert pool.compress == compress_type

    # Invalid compression type
    with pytest.raises(ValidationError) as exc_info:
        StoragePool(compress="InvalidCompression")
    assert "type=enum" in str(exc_info.value)

def test_write_mode_validation():
    """Test validation of write mode enum."""
    # Valid write modes
    for write_mode in ObjectWriteModeEnum:
        pool = StoragePool(write_mode=write_mode)
        assert pool.write_mode == write_mode

    # Invalid write mode
    with pytest.raises(ValidationError) as exc_info:
        StoragePool(write_mode="InvalidMode")
    assert "type=enum" in str(exc_info.value)

def test_endpoint_url_validation():
    """Test validation of endpoint URL."""
    # Valid endpoint URL
   
    # Invalid endpoint URL
    with pytest.raises(ValidationError) as exc_info:
        StoragePool(endpoint="not-a-url")
    assert "URL" in str(exc_info.value)

def test_date_time_validation():
    """Test validation of date_time field."""
    # Valid datetime string
    pool = StoragePool(date_time="2024-01-01T00:00:00Z")
    assert isinstance(pool.date_time, datetime)

    # Valid datetime object
    now = datetime.now(timezone.utc)
    pool = StoragePool(date_time=now)
    assert pool.date_time == now

    # Invalid datetime
    with pytest.raises(ValidationError) as exc_info:
        StoragePool(date_time="not-a-date")
    assert "type=datetime" in str(exc_info.value)

def test_model_export():
    """Test that the model correctly exports data."""
    pool = StoragePool(
        name="Test Pool",
        provider="S3",
        write_mode="KEY",
        compress="Gzip"
    )
    
    data = pool.model_dump(by_alias=True)
    assert data["Name"] == "Test Pool"
    assert data["Provider"] == "S3"
    assert data["WriteMode"] == "KEY"
    assert data["Compress"] == "Gzip"
    assert "Id" not in data  # Should be excluded

def test_optional_fields():
    """Test that optional fields can be None."""
    pool = StoragePool(
        tenant_guid=None,
        encryption_key_guid=None,
        name=None,
        endpoint=None,
        access_key=None,
        secret_key=None,
        aws_region=None,
        aws_bucket=None,
        aws_base_domain=None,
        aws_base_url=None,
        disk_directory=None,
        azure_account=None,
        azure_container=None
    )
    
    assert pool.tenant_guid is None
    assert pool.encryption_key_guid is None
    assert pool.name is None
    assert pool.endpoint is None
    assert pool.access_key is None
    assert pool.secret_key is None
    assert pool.aws_region is None
    assert pool.aws_bucket is None
    assert pool.aws_base_domain is None
    assert pool.aws_base_url is None
    assert pool.disk_directory is None
    assert pool.azure_account is None
    assert pool.azure_container is None