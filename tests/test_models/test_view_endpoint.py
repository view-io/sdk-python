import pytest
from datetime import datetime, timezone
from view_sdk.models.view_endpoint import ViewEndpointModel


def test_create_view_endpoint_with_all_fields():
    """Test creating a ViewEndpoint with all fields."""
    data = {
        "guid": "550e8400-e29b-41d4-a716-446655440000",
        "tenant_guid": "550e8400-e29b-41d4-a716-446655440001",
        "owner_guid": "550e8400-e29b-41d4-a716-446655440002",
        "name": "Test Endpoint",
        "use_ssl": True,
        "bucket_name": "test-bucket",
        "region": "eu-west-1",
        "access_key": "test-access-key",
        "secret_key": "test-secret-key",
        "api_key": "test-api-key",
        "created_utc": datetime(2024, 1, 1, tzinfo=timezone.utc)
    }
    
    endpoint = ViewEndpointModel(**data)
    
    for key, value in data.items():
        assert getattr(endpoint, key) == value

def test_url_validation_with_trailing_slash():
    """Test that URLs are automatically appended with trailing slash if missing."""
    data = {
        "s3_url": "http://example.com",
        "s3_base_url": "http://example.com/{bucket}/{key}",
        "rest_url": "http://example.com"
    }
    
    endpoint = ViewEndpointModel(**data)
    
    assert endpoint.s3_url == "http://example.com/"
    assert endpoint.s3_base_url == "http://example.com/{bucket}/{key}/"
    assert endpoint.rest_url == "http://example.com/"

@pytest.mark.parametrize("field,value", [
    ("s3_url", ""),
    ("s3_url", None),
    ("rest_url", ""),
    ("rest_url", None),
])
def test_invalid_empty_urls(field, value):
    """Test that empty URLs raise validation errors."""
    data = {field: value}
    with pytest.raises(ValueError):
        ViewEndpointModel(**data)

@pytest.mark.parametrize("s3_base_url", [
    "http://example.com/invalid",  # Missing both placeholders
    "http://example.com/{bucket}/invalid",  # Missing key placeholder
    "http://example.com/{key}/invalid",  # Missing bucket placeholder
    "",  # Empty string
    None,  # None value
])
def test_invalid_s3_base_url(s3_base_url):
    """Test that invalid s3_base_url values raise validation errors."""
    with pytest.raises(ValueError):
        ViewEndpointModel(s3_base_url=s3_base_url)


def test_model_json_deserialization():
    """Test that the model can be properly deserialized from JSON with aliases."""
    json_data = {
        "GUID": "550e8400-e29b-41d4-a716-446655440000",
        "TenantGUID": "550e8400-e29b-41d4-a716-446655440001",
        "OwnerGUID": "550e8400-e29b-41d4-a716-446655440002",
        "Name": "Test Endpoint",
        "UseSsl": True,
        "S3Url": "http://s3.example.com",
        "BucketName": "test-bucket"
    }
    
    endpoint = ViewEndpointModel.model_validate(json_data)
    
    assert endpoint.guid == json_data["GUID"]
    assert endpoint.tenant_guid == json_data["TenantGUID"]
    assert endpoint.name == json_data["Name"]
    assert endpoint.use_ssl == json_data["UseSsl"]
    assert endpoint.s3_url == "http://s3.example.com/"
    assert endpoint.bucket_name == json_data["BucketName"]