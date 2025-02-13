import pytest
from datetime import datetime, timezone
from pydantic import ValidationError
from view_sdk.models.tenant_metadata import TenantMetadataModel

def test_create_minimal_tenant_metadata():
    """Test creating a tenant metadata with minimal required fields."""
    tenant = TenantMetadataModel(guid="default")
    assert isinstance(tenant.guid, str)
    assert isinstance(tenant.name, str)
    assert tenant.region == "us-west-1"
    assert tenant.active is True
    assert isinstance(tenant.created_utc, datetime)
    assert tenant.s3_base_domain == ""
    assert tenant.rest_base_domain == ""
    assert tenant.default_pool_guid == ""

def test_create_complete_tenant_metadata():
    """Test creating a tenant metadata with all fields populated."""
    data = {
        "id": 1,
        "guid": "123e4567-e89b-12d3-a456-426614174000",
        "account_guid": "456e7890-e89b-12d3-a456-426614174000",
        "parent_guid": "987fcdeb-51d3-a456-426614174000",
        "name": "Test Tenant",
        "region": "eu-west-1",
        "s3_base_domain": "s3.company.com",
        "rest_base_domain": "api.company.com",
        "default_pool_guid": "abcd1234-e89b-12d3-a456-426614174000",
        "active": True,
        "is_protected": True,
        "created_utc": "2024-01-01T00:00:00Z"
    }

    tenant = TenantMetadataModel(**data)
    assert tenant.guid == data["guid"]
    assert tenant.account_guid == data["account_guid"]
    assert tenant.parent_guid == data["parent_guid"]
    assert tenant.name == data["name"]
    assert tenant.region == data["region"]
    assert tenant.s3_base_domain == data["s3_base_domain"]
    assert tenant.rest_base_domain == data["rest_base_domain"]
    assert tenant.default_pool_guid == data["default_pool_guid"]
    assert tenant.active == data["active"]
    assert tenant.is_protected == data["is_protected"]
    assert isinstance(tenant.created_utc, datetime)

def test_id_validation():
    """Test validation of id field."""
    # Valid id
    tenant = TenantMetadataModel(guid="default",id=1)
    assert tenant.id == 1

    # Invalid id (less than 1)
    with pytest.raises(ValidationError) as exc_info:
        TenantMetadataModel(id=0)
    assert "Input should be greater than or equal to 1" in str(exc_info.value)

    # Invalid id type
    with pytest.raises(ValidationError):
        TenantMetadataModel(id="invalid")

def test_guid_validation():
    """Test validation of guid fields."""
    # Test valid UUID format
    valid_uuid = "123e4567-e89b-12d3-a456-426614174000"
    tenant = TenantMetadataModel(
        guid=valid_uuid,
        parent_guid=valid_uuid,
        default_pool_guid=valid_uuid
    )
    assert tenant.guid == valid_uuid
    assert tenant.parent_guid == valid_uuid
    assert tenant.default_pool_guid == valid_uuid

def test_name_validation():
    """Test validation of name field."""
    # Test with valid name
    tenant = TenantMetadataModel(guid="default", name="Test Tenant")
    assert tenant.name == "Test Tenant"

    # Empty name is allowed (will use default empty string)
    tenant = TenantMetadataModel(guid="default", name="")
    assert tenant.name == ""

def test_region_validation():
    """Test validation of region field."""
    # Test with valid region
    tenant = TenantMetadataModel(guid="default", region="ap-southeast-1")
    assert tenant.region == "ap-southeast-1"

    # Default region
    tenant = TenantMetadataModel(guid="default")
    assert tenant.region == "us-west-1"

def test_active_validation():
    """Test validation of active field."""
    # Test with explicit True
    tenant = TenantMetadataModel(guid="default", active=True)
    assert tenant.active is True

    # Test with explicit False
    tenant = TenantMetadataModel(guid="default", active=False)
    assert tenant.active is False

    # Test default value
    tenant = TenantMetadataModel(guid="default")
    assert tenant.active is True

def test_created_utc_validation():
    """Test validation of created_utc field."""
    # Test with valid datetime string
    tenant = TenantMetadataModel(guid="default", created_utc="2024-01-01T00:00:00Z")
    assert isinstance(tenant.created_utc, datetime)

    # Test with datetime object
    now = datetime.now(timezone.utc)
    tenant = TenantMetadataModel(guid="default", created_utc=now)
    assert tenant.created_utc == now

    # Test with invalid datetime
    with pytest.raises(ValidationError) as exc_info:
        TenantMetadataModel(guid="default", created_utc="invalid-date")
    assert "type=datetime" in str(exc_info.value)

def test_model_export():
    """Test that the model correctly exports data with aliases."""
    data = {
        "guid": "123e4567-e89b-12d3-a456-426614174000",
        "name": "Test Tenant",
        "region": "eu-central-1",
    }

    tenant = TenantMetadataModel(**data)
    exported = tenant.model_dump(by_alias=True)

    assert exported["GUID"] == data["guid"]
    assert exported["Name"] == data["name"]
    assert exported["Region"] == data["region"]
    assert "Id" not in exported  # Should be excluded

def test_optional_fields():
    """Test that optional fields can be None."""
    tenant = TenantMetadataModel(
        guid="default",
        parent_guid=None,
        account_guid=None,
        name="",
        s3_base_domain="",
        rest_base_domain="",
        default_pool_guid=""
    )

    assert tenant.parent_guid is None
    assert tenant.account_guid is None
    assert tenant.name == ""
    assert tenant.s3_base_domain == ""
    assert tenant.rest_base_domain == ""
    assert tenant.default_pool_guid == ""
    assert tenant.is_protected is False  # Check default value

def test_field_aliases():
    """Test that field aliases are working correctly."""
    data = {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "AccountGUID": "456e7890-e89b-12d3-a456-426614174000",
        "ParentGUID": "987fcdeb-51d3-a456-426614174000",
        "Name": "Test Tenant",
        "Region": "us-east-1",
        "S3BaseDomain": "s3.test.com",
        "RestBaseDomain": "api.test.com",
        "DefaultPoolGUID": "abcd1234-e89b-12d3-a456-426614174000",
        "Active": True,
        "IsProtected": True,
        "CreatedUtc": "2024-01-01T00:00:00Z"
    }

    tenant = TenantMetadataModel(**data)
    assert tenant.guid == data["GUID"]
    assert tenant.account_guid == data["AccountGUID"]
    assert tenant.parent_guid == data["ParentGUID"]
    assert tenant.name == data["Name"]
    assert tenant.region == data["Region"]
    assert tenant.s3_base_domain == data["S3BaseDomain"]
    assert tenant.rest_base_domain == data["RestBaseDomain"]
    assert tenant.default_pool_guid == data["DefaultPoolGUID"]
    assert tenant.active == data["Active"]
    assert tenant.is_protected == data["IsProtected"]
