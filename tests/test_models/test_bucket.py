import pytest
from datetime import datetime, timezone
from uuid import UUID
from pydantic import ValidationError
from view_sdk.models.bucket import BucketMetadataModel
from view_sdk.models.user_master import UserMasterModel
from view_sdk.enums.bucket_category_enum import BucketCategoryEnum


@pytest.fixture
def valid_user_data():
    return {
        "GUID": "123e4567-e89b-12d3-a456-426614174001",
        "TenantGUID": "123e4567-e89b-12d3-a456-426614174002",
        "FirstName": "John",
        "LastName": "Doe",
        "Email": "john.doe@example.com",
        "PasswordSha256": "hashedpassword",
        "Active": True,
    }


@pytest.fixture
def valid_bucket_data(valid_user_data):
    return {
        "Id": 1,
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "TenantGUID": "223e4567-e89b-12d3-a456-426614174000",
        "PoolGUID": "323e4567-e89b-12d3-a456-426614174000",
        "OwnerGUID": "423e4567-e89b-12d3-a456-426614174000",
        "Category": "Data",
        "Name": "Test Bucket",
        "RegionString": "us-west-1",
        "Versioning": True,
        "RetentionMinutes": 60,
        "MaxUploadSize": 1024 * 1024 * 1024,
        "MaxMultipartUploadSeconds": 604800,
        "LastAccessUtc": "2023-09-12T12:34:56.789Z",
        "CreatedUtc": "2023-09-12T12:34:56.789Z",
        "Owner": valid_user_data,
    }


def test_valid_bucket_creation(valid_bucket_data):
    bucket = BucketMetadataModel(**valid_bucket_data)
    assert bucket.id == 1
    assert isinstance(bucket.guid, str)
    assert UUID(bucket.guid)  # Validates UUID format
    assert bucket.name == "Test Bucket"
    assert bucket.category == "Data"
    assert bucket.region_string == "us-west-1"
    assert bucket.versioning is True
    assert bucket.retention_minutes == 60
    assert bucket.max_upload_size == 1024 * 1024 * 1024
    assert bucket.max_multipart_upload_seconds == 604800
    assert isinstance(bucket.owner, UserMasterModel)
    assert bucket.owner.first_name == "John"


def test_bucket_default_values():
    """Test that defaults are set correctly when minimal data is provided"""
    bucket = BucketMetadataModel(
        guid="123e4567-e89b-12d3-a456-426614174000",
        tenant_guid="223e4567-e89b-12d3-a456-426614174000",
        pool_guid="323e4567-e89b-12d3-a456-426614174000",
        owner_guid="423e4567-e89b-12d3-a456-426614174000",
    )
    # Check UUIDs are properly formatted
    assert isinstance(UUID(bucket.guid), UUID)
    assert isinstance(UUID(bucket.tenant_guid), UUID)
    assert isinstance(UUID(bucket.pool_guid), UUID)
    assert isinstance(UUID(bucket.owner_guid), UUID)

    # Check default values
    assert bucket.category == BucketCategoryEnum.Data  # Check against enum
    assert bucket.name == ""  # Empty string is the default
    assert bucket.region_string == "us-west-1"
    assert bucket.versioning is True
    assert bucket.max_multipart_upload_seconds == 60 * 60 * 24 * 7
    assert isinstance(bucket.last_access_utc, datetime)
    assert isinstance(bucket.created_utc, datetime)
    assert bucket.owner is None
    assert bucket.retention_minutes is None
    assert bucket.max_upload_size is None


def test_invalid_category():
    """Test validation of category enum"""
    with pytest.raises(ValidationError) as exc_info:
        BucketMetadataModel(Category="InvalidCategory")
    assert "Input should be 'Data', 'Metadata' or 'Embeddings'" in str(exc_info.value)


def test_valid_categories():
    """Test all valid category values"""
    for category in BucketCategoryEnum:
        bucket = BucketMetadataModel(Category=category.value)
        assert bucket.category == category.value


def test_retention_minutes_validation():
    """Test validation of retention_minutes field"""
    # Test valid value
    bucket = BucketMetadataModel(RetentionMinutes=60)
    assert bucket.retention_minutes == 60

    # Test invalid values
    invalid_values = [0, -1]
    for value in invalid_values:
        with pytest.raises(ValidationError) as exc_info:
            BucketMetadataModel(RetentionMinutes=value)
        assert "Input should be greater than or equal to 1" in str(exc_info.value)


def test_datetime_fields():
    """Test datetime field validation and conversion"""
    # Test with valid ISO format
    bucket = BucketMetadataModel(
        LastAccessUtc="2023-09-12T12:34:56.789Z", CreatedUtc="2023-09-12T12:34:56.789Z"
    )
    assert isinstance(bucket.last_access_utc, datetime)
    assert isinstance(bucket.created_utc, datetime)
    assert bucket.last_access_utc.tzinfo == timezone.utc
    assert bucket.created_utc.tzinfo == timezone.utc

    # Test with invalid datetime format
    with pytest.raises(ValidationError) as exc_info:
        BucketMetadataModel(LastAccessUtc="invalid-date")
    assert "Input should be a valid datetime" in str(exc_info.value)


def test_owner_validation_valid_data(valid_user_data):
    """Test owner field validation with valid data"""
    bucket = BucketMetadataModel(
        guid="123e4567-e89b-12d3-a456-426614174000",
        tenant_guid="223e4567-e89b-12d3-a456-426614174000",
        pool_guid="323e4567-e89b-12d3-a456-426614174000",
        owner_guid="423e4567-e89b-12d3-a456-426614174000",
        Owner=valid_user_data,
    )
    assert isinstance(bucket.owner, UserMasterModel)
    assert bucket.owner.email == "john.doe@example.com"
    assert bucket.owner.first_name == "John"
    assert bucket.owner.last_name == "Doe"


def test_model_dump(valid_bucket_data):
    """Test model serialization"""
    bucket = BucketMetadataModel(**valid_bucket_data)
    dumped = bucket.model_dump(mode="json")

    # Check excluded fields
    assert "id" not in dumped
    assert "retention_minutes" not in dumped

    # Check included fields
    assert "guid" in dumped
    assert "category" in dumped
    assert "owner" in dumped
    assert isinstance(dumped["owner"], dict)


def test_model_aliases():
    """Test that field aliases are working correctly"""
    test_data = {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "TenantGUID": "223e4567-e89b-12d3-a456-426614174000",
        "Category": "Data",
        "Name": "Test Bucket",
    }
    bucket = BucketMetadataModel(**test_data)
    assert bucket.guid == test_data["GUID"]
    assert bucket.tenant_guid == test_data["TenantGUID"]
    assert bucket.category == test_data["Category"]
    assert bucket.name == test_data["Name"]


def test_max_upload_size():
    """Test max_upload_size field"""
    # Test with valid values
    valid_sizes = [None, 1024, 1024 * 1024 * 1024]
    for size in valid_sizes:
        bucket = BucketMetadataModel(MaxUploadSize=size)
        assert bucket.max_upload_size == size


def test_max_multipart_upload_seconds():
    """Test max_multipart_upload_seconds field default and validation"""
    # Test default value
    bucket = BucketMetadataModel()
    assert bucket.max_multipart_upload_seconds == 60 * 60 * 24 * 7  # 7 days

    # Test custom value
    bucket = BucketMetadataModel(MaxMultipartUploadSeconds=3600)
    assert bucket.max_multipart_upload_seconds == 3600
