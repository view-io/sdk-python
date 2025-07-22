import pytest
from datetime import datetime, timezone
from pydantic import ValidationError
from view_sdk.models.user_master import UserMasterModel


def test_create_minimal_user_master():
    """Test creating a user master with minimal required fields."""
    user = UserMasterModel()
    assert isinstance(user.guid, str)
    assert isinstance(user.tenant_guid, str)
    assert user.first_name == ""
    assert user.last_name == ""
    assert user.full_name == ""
    assert user.notes == ""
    assert user.email == ""
    assert user.password_sha256 == ""
    assert user.active is True
    assert isinstance(user.created_utc, datetime)


def test_create_complete_user_master():
    """Test creating a user master with all fields populated."""
    data = {
        "guid": "123e4567-e89b-12d3-a456-426614174000",
        "tenant_guid": "987fcdeb-51d3-a456-426614174000",
        "first_name": "John",
        "last_name": "Doe",
        "notes": "Test user",
        "email": "john.doe@example.com",
        "password_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "active": True,
        "created_utc": "2024-01-01T00:00:00Z",
    }

    user = UserMasterModel(**data)
    assert user.guid == data["guid"]
    assert user.tenant_guid == data["tenant_guid"]
    assert user.first_name == data["first_name"]
    assert user.last_name == data["last_name"]
    assert user.notes == data["notes"]
    assert user.email == data["email"]
    assert user.password_sha256 == data["password_sha256"]
    assert user.active == data["active"]
    assert isinstance(user.created_utc, datetime)


def test_guid_validation():
    """Test validation of guid fields."""
    # Test valid UUID format
    valid_uuid = "123e4567-e89b-12d3-a456-426614174000"
    user = UserMasterModel(guid=valid_uuid, tenant_guid=valid_uuid)
    assert user.guid == valid_uuid
    assert user.tenant_guid == valid_uuid

    # Auto-generated guids
    user = UserMasterModel()
    assert isinstance(user.guid, str)
    assert isinstance(user.tenant_guid, str)
    assert len(user.guid) > 0
    assert len(user.tenant_guid) > 0


def test_active_validation():
    """Test validation of active field."""
    # Test with explicit True
    user = UserMasterModel(active=True)
    assert user.active is True

    # Test with explicit False
    user = UserMasterModel(active=False)
    assert user.active is False

    # Test default value
    user = UserMasterModel()
    assert user.active is True


def test_created_utc_validation():
    """Test validation of created_utc field."""
    # Test with valid datetime string
    user = UserMasterModel(created_utc="2024-01-01T00:00:00Z")
    assert isinstance(user.created_utc, datetime)

    # Test with datetime object
    now = datetime.now(timezone.utc)
    user = UserMasterModel(created_utc=now)
    assert user.created_utc == now

    # Test with invalid datetime
    with pytest.raises(ValidationError) as exc_info:
        UserMasterModel(created_utc="invalid-date")
    assert "type=datetime" in str(exc_info.value)


def test_model_export():
    """Test that the model correctly exports data with aliases."""
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "notes": "Test notes",
    }

    user = UserMasterModel(**data)
    exported = user.model_dump(by_alias=True)

    assert exported["FirstName"] == data["first_name"]
    assert exported["LastName"] == data["last_name"]
    assert exported["Email"] == data["email"]
    assert exported["Notes"] == data["notes"]
    assert "PasswordSha256" not in exported  # Should be excluded
    assert "FullName" in exported  # Should be included and computed


def test_password_sha256_exclusion():
    """Test that password_sha256 is properly excluded from export."""
    user = UserMasterModel(
        password_sha256="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    )

    exported = user.model_dump(exclude={"password_sha256"})
    assert "password_sha256" not in exported

    exported_aliased = user.model_dump(by_alias=True)
    assert "PasswordSha256" not in exported_aliased


def test_field_aliases():
    """Test that field aliases are working correctly."""
    data = {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "TenantGUID": "987fcdeb-51d3-a456-426614174000",
        "FirstName": "John",
        "LastName": "Doe",
        "Notes": "Test notes",
        "Email": "john.doe@example.com",
        "Active": True,
        "CreatedUtc": "2024-01-01T00:00:00Z",
    }

    user = UserMasterModel(**data)
    assert user.guid == data["GUID"]
    assert user.tenant_guid == data["TenantGUID"]
    assert user.first_name == data["FirstName"]
    assert user.last_name == data["LastName"]
    assert user.notes == data["Notes"]
    assert user.email == data["Email"]
    assert user.active == data["Active"]
