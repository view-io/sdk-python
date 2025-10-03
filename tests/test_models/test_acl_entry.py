import pytest
from datetime import datetime
from pydantic import ValidationError

from view_sdk.models.acl_entry import ACLEntryModel


@pytest.fixture
def valid_acl_entry_data():
    """Valid ACL entry data for testing."""
    return {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "TenantGUID": "223e4567-e89b-12d3-a456-426614174001",
        "BucketGUID": "323e4567-e89b-12d3-a456-426614174002",
        "OwnerGUID": "423e4567-e89b-12d3-a456-426614174003",
        "UserGUID": "523e4567-e89b-12d3-a456-426614174004",
        "CanonicalUser": "user@example.com",
        "EnableRead": True,
        "EnableReadAcp": False,
        "EnableWrite": True,
        "EnableWriteAcp": False,
        "FullControl": False,
        "CreatedUtc": "2023-01-01T12:00:00Z",
    }


def test_create_acl_entry_with_valid_data(valid_acl_entry_data):
    """Test creating an ACL entry with valid data."""
    acl_entry = ACLEntryModel(**valid_acl_entry_data)

    assert acl_entry.guid == valid_acl_entry_data["GUID"]
    assert acl_entry.tenant_guid == valid_acl_entry_data["TenantGUID"]
    assert acl_entry.bucket_guid == valid_acl_entry_data["BucketGUID"]
    assert acl_entry.owner_guid == valid_acl_entry_data["OwnerGUID"]
    assert acl_entry.user_guid == valid_acl_entry_data["UserGUID"]
    assert acl_entry.canonical_user == valid_acl_entry_data["CanonicalUser"]
    assert acl_entry.enable_read is True
    assert acl_entry.enable_read_acp is False
    assert acl_entry.enable_write is True
    assert acl_entry.enable_write_acp is False
    assert acl_entry.full_control is False
    assert isinstance(acl_entry.created_utc, datetime)


def test_create_acl_entry_with_field_names(valid_acl_entry_data):
    """Test creating an ACL entry using field names instead of aliases."""
    # Convert aliases to field names
    field_data = {
        "guid": valid_acl_entry_data["GUID"],
        "tenant_guid": valid_acl_entry_data["TenantGUID"],
        "bucket_guid": valid_acl_entry_data["BucketGUID"],
        "owner_guid": valid_acl_entry_data["OwnerGUID"],
        "user_guid": valid_acl_entry_data["UserGUID"],
        "canonical_user": valid_acl_entry_data["CanonicalUser"],
        "enable_read": valid_acl_entry_data["EnableRead"],
        "enable_read_acp": valid_acl_entry_data["EnableReadAcp"],
        "enable_write": valid_acl_entry_data["EnableWrite"],
        "enable_write_acp": valid_acl_entry_data["EnableWriteAcp"],
        "full_control": valid_acl_entry_data["FullControl"],
        "created_utc": valid_acl_entry_data["CreatedUtc"],
    }

    acl_entry = ACLEntryModel(**field_data)
    assert acl_entry.guid == valid_acl_entry_data["GUID"]
    assert acl_entry.tenant_guid == valid_acl_entry_data["TenantGUID"]


def test_acl_entry_boolean_fields():
    """Test ACL entry boolean field combinations."""
    base_data = {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "TenantGUID": "223e4567-e89b-12d3-a456-426614174001",
        "BucketGUID": "323e4567-e89b-12d3-a456-426614174002",
        "OwnerGUID": "423e4567-e89b-12d3-a456-426614174003",
        "UserGUID": "523e4567-e89b-12d3-a456-426614174004",
        "CanonicalUser": "user@example.com",
        "CreatedUtc": "2023-01-01T12:00:00Z",
    }

    # Test all permissions enabled
    all_enabled_data = {
        **base_data,
        "EnableRead": True,
        "EnableReadAcp": True,
        "EnableWrite": True,
        "EnableWriteAcp": True,
        "FullControl": True,
    }

    acl_entry = ACLEntryModel(**all_enabled_data)
    assert acl_entry.enable_read is True
    assert acl_entry.enable_read_acp is True
    assert acl_entry.enable_write is True
    assert acl_entry.enable_write_acp is True
    assert acl_entry.full_control is True

    # Test all permissions disabled
    all_disabled_data = {
        **base_data,
        "EnableRead": False,
        "EnableReadAcp": False,
        "EnableWrite": False,
        "EnableWriteAcp": False,
        "FullControl": False,
    }

    acl_entry = ACLEntryModel(**all_disabled_data)
    assert acl_entry.enable_read is False
    assert acl_entry.enable_read_acp is False
    assert acl_entry.enable_write is False
    assert acl_entry.enable_write_acp is False
    assert acl_entry.full_control is False


def test_acl_entry_datetime_parsing():
    """Test ACL entry datetime field parsing."""
    base_data = {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "TenantGUID": "223e4567-e89b-12d3-a456-426614174001",
        "BucketGUID": "323e4567-e89b-12d3-a456-426614174002",
        "OwnerGUID": "423e4567-e89b-12d3-a456-426614174003",
        "UserGUID": "523e4567-e89b-12d3-a456-426614174004",
        "CanonicalUser": "user@example.com",
        "EnableRead": True,
        "EnableReadAcp": False,
        "EnableWrite": True,
        "EnableWriteAcp": False,
        "FullControl": False,
    }

    # Test ISO format datetime string
    iso_data = {**base_data, "CreatedUtc": "2023-01-01T12:00:00Z"}
    acl_entry = ACLEntryModel(**iso_data)
    assert isinstance(acl_entry.created_utc, datetime)
    assert acl_entry.created_utc.year == 2023
    assert acl_entry.created_utc.month == 1
    assert acl_entry.created_utc.day == 1

    # Test datetime object
    dt_obj = datetime(2023, 6, 15, 14, 30, 45)
    dt_data = {**base_data, "CreatedUtc": dt_obj}
    acl_entry = ACLEntryModel(**dt_data)
    assert isinstance(acl_entry.created_utc, datetime)
    assert acl_entry.created_utc == dt_obj


def test_acl_entry_required_fields():
    """Test that all fields are required."""
    # Test missing GUID
    with pytest.raises(ValidationError) as exc_info:
        ACLEntryModel(
            TenantGUID="223e4567-e89b-12d3-a456-426614174001",
            BucketGUID="323e4567-e89b-12d3-a456-426614174002",
            OwnerGUID="423e4567-e89b-12d3-a456-426614174003",
            UserGUID="523e4567-e89b-12d3-a456-426614174004",
            CanonicalUser="user@example.com",
            EnableRead=True,
            EnableReadAcp=False,
            EnableWrite=True,
            EnableWriteAcp=False,
            FullControl=False,
            CreatedUtc="2023-01-01T12:00:00Z",
        )
    assert "GUID" in str(exc_info.value) or "guid" in str(exc_info.value)

    # Test missing TenantGUID
    with pytest.raises(ValidationError) as exc_info:
        ACLEntryModel(
            GUID="123e4567-e89b-12d3-a456-426614174000",
            BucketGUID="323e4567-e89b-12d3-a456-426614174002",
            OwnerGUID="423e4567-e89b-12d3-a456-426614174003",
            UserGUID="523e4567-e89b-12d3-a456-426614174004",
            CanonicalUser="user@example.com",
            EnableRead=True,
            EnableReadAcp=False,
            EnableWrite=True,
            EnableWriteAcp=False,
            FullControl=False,
            CreatedUtc="2023-01-01T12:00:00Z",
        )
    assert "TenantGUID" in str(exc_info.value) or "tenant_guid" in str(exc_info.value)


def test_acl_entry_field_types():
    """Test ACL entry field type validation."""
    base_data = {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "TenantGUID": "223e4567-e89b-12d3-a456-426614174001",
        "BucketGUID": "323e4567-e89b-12d3-a456-426614174002",
        "OwnerGUID": "423e4567-e89b-12d3-a456-426614174003",
        "UserGUID": "523e4567-e89b-12d3-a456-426614174004",
        "CanonicalUser": "user@example.com",
        "EnableRead": True,
        "EnableReadAcp": False,
        "EnableWrite": True,
        "EnableWriteAcp": False,
        "FullControl": False,
        "CreatedUtc": "2023-01-01T12:00:00Z",
    }

    # Test invalid boolean for EnableRead
    with pytest.raises(ValidationError) as exc_info:
        invalid_data = {**base_data, "EnableRead": "not_a_boolean"}
        ACLEntryModel(**invalid_data)
    assert "EnableRead" in str(exc_info.value) or "enable_read" in str(exc_info.value)

    # Test invalid datetime
    with pytest.raises(ValidationError) as exc_info:
        invalid_data = {**base_data, "CreatedUtc": "not_a_datetime"}
        ACLEntryModel(**invalid_data)
    assert "CreatedUtc" in str(exc_info.value) or "created_utc" in str(exc_info.value)


def test_acl_entry_model_dump():
    """Test ACL entry model serialization."""
    data = {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "TenantGUID": "223e4567-e89b-12d3-a456-426614174001",
        "BucketGUID": "323e4567-e89b-12d3-a456-426614174002",
        "OwnerGUID": "423e4567-e89b-12d3-a456-426614174003",
        "UserGUID": "523e4567-e89b-12d3-a456-426614174004",
        "CanonicalUser": "user@example.com",
        "EnableRead": True,
        "EnableReadAcp": False,
        "EnableWrite": True,
        "EnableWriteAcp": False,
        "FullControl": False,
        "CreatedUtc": "2023-01-01T12:00:00Z",
    }

    acl_entry = ACLEntryModel(**data)
    dumped = acl_entry.model_dump()

    assert dumped["guid"] == data["GUID"]
    assert dumped["tenant_guid"] == data["TenantGUID"]
    assert dumped["bucket_guid"] == data["BucketGUID"]
    assert dumped["owner_guid"] == data["OwnerGUID"]
    assert dumped["user_guid"] == data["UserGUID"]
    assert dumped["canonical_user"] == data["CanonicalUser"]
    assert dumped["enable_read"] is True
    assert dumped["enable_read_acp"] is False
    assert dumped["enable_write"] is True
    assert dumped["enable_write_acp"] is False
    assert dumped["full_control"] is False
    assert isinstance(dumped["created_utc"], datetime)


def test_acl_entry_model_dump_by_alias():
    """Test ACL entry model serialization with aliases."""
    data = {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "TenantGUID": "223e4567-e89b-12d3-a456-426614174001",
        "BucketGUID": "323e4567-e89b-12d3-a456-426614174002",
        "OwnerGUID": "423e4567-e89b-12d3-a456-426614174003",
        "UserGUID": "523e4567-e89b-12d3-a456-426614174004",
        "CanonicalUser": "user@example.com",
        "EnableRead": True,
        "EnableReadAcp": False,
        "EnableWrite": True,
        "EnableWriteAcp": False,
        "FullControl": False,
        "CreatedUtc": "2023-01-01T12:00:00Z",
    }

    acl_entry = ACLEntryModel(**data)
    dumped = acl_entry.model_dump(by_alias=True)

    assert dumped["GUID"] == data["GUID"]
    assert dumped["TenantGUID"] == data["TenantGUID"]
    assert dumped["BucketGUID"] == data["BucketGUID"]
    assert dumped["OwnerGUID"] == data["OwnerGUID"]
    assert dumped["UserGUID"] == data["UserGUID"]
    assert dumped["CanonicalUser"] == data["CanonicalUser"]
    assert dumped["EnableRead"] is True
    assert dumped["EnableReadAcp"] is False
    assert dumped["EnableWrite"] is True
    assert dumped["EnableWriteAcp"] is False
    assert dumped["FullControl"] is False
    assert isinstance(dumped["CreatedUtc"], datetime)


def test_acl_entry_model_json():
    """Test ACL entry JSON serialization."""
    data = {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "TenantGUID": "223e4567-e89b-12d3-a456-426614174001",
        "BucketGUID": "323e4567-e89b-12d3-a456-426614174002",
        "OwnerGUID": "423e4567-e89b-12d3-a456-426614174003",
        "UserGUID": "523e4567-e89b-12d3-a456-426614174004",
        "CanonicalUser": "user@example.com",
        "EnableRead": True,
        "EnableReadAcp": False,
        "EnableWrite": True,
        "EnableWriteAcp": False,
        "FullControl": False,
        "CreatedUtc": "2023-01-01T12:00:00Z",
    }

    acl_entry = ACLEntryModel(**data)
    json_str = acl_entry.model_dump_json()

    assert isinstance(json_str, str)
    assert data["GUID"] in json_str
    assert data["TenantGUID"] in json_str
    assert data["CanonicalUser"] in json_str


def test_acl_entry_model_json_by_alias():
    """Test ACL entry JSON serialization with aliases."""
    data = {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "TenantGUID": "223e4567-e89b-12d3-a456-426614174001",
        "BucketGUID": "323e4567-e89b-12d3-a456-426614174002",
        "OwnerGUID": "423e4567-e89b-12d3-a456-426614174003",
        "UserGUID": "523e4567-e89b-12d3-a456-426614174004",
        "CanonicalUser": "user@example.com",
        "EnableRead": True,
        "EnableReadAcp": False,
        "EnableWrite": True,
        "EnableWriteAcp": False,
        "FullControl": False,
        "CreatedUtc": "2023-01-01T12:00:00Z",
    }

    acl_entry = ACLEntryModel(**data)
    json_str = acl_entry.model_dump_json(by_alias=True)

    assert isinstance(json_str, str)
    assert '"GUID"' in json_str
    assert '"TenantGUID"' in json_str
    assert '"CanonicalUser"' in json_str


def test_acl_entry_edge_cases():
    """Test ACL entry edge cases."""
    # Test empty string values
    empty_string_data = {
        "GUID": "",
        "TenantGUID": "",
        "BucketGUID": "",
        "OwnerGUID": "",
        "UserGUID": "",
        "CanonicalUser": "",
        "EnableRead": False,
        "EnableReadAcp": False,
        "EnableWrite": False,
        "EnableWriteAcp": False,
        "FullControl": False,
        "CreatedUtc": "2023-01-01T12:00:00Z",
    }

    acl_entry = ACLEntryModel(**empty_string_data)
    assert acl_entry.guid == ""
    assert acl_entry.tenant_guid == ""
    assert acl_entry.canonical_user == ""

    # Test very long string values
    long_string_data = {
        "GUID": "a" * 1000,
        "TenantGUID": "b" * 1000,
        "BucketGUID": "c" * 1000,
        "OwnerGUID": "d" * 1000,
        "UserGUID": "e" * 1000,
        "CanonicalUser": "f" * 1000,
        "EnableRead": True,
        "EnableReadAcp": True,
        "EnableWrite": True,
        "EnableWriteAcp": True,
        "FullControl": True,
        "CreatedUtc": "2023-01-01T12:00:00Z",
    }

    acl_entry = ACLEntryModel(**long_string_data)
    assert len(acl_entry.guid) == 1000
    assert len(acl_entry.canonical_user) == 1000


def test_acl_entry_model_config():
    """Test ACL entry model configuration."""
    data = {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "TenantGUID": "223e4567-e89b-12d3-a456-426614174001",
        "BucketGUID": "323e4567-e89b-12d3-a456-426614174002",
        "OwnerGUID": "423e4567-e89b-12d3-a456-426614174003",
        "UserGUID": "523e4567-e89b-12d3-a456-426614174004",
        "CanonicalUser": "user@example.com",
        "EnableRead": True,
        "EnableReadAcp": False,
        "EnableWrite": True,
        "EnableWriteAcp": False,
        "FullControl": False,
        "CreatedUtc": "2023-01-01T12:00:00Z",
    }

    acl_entry = ACLEntryModel(**data)

    # Test that populate_by_name is working (can use field names or aliases)
    assert acl_entry.model_config["populate_by_name"] is True

    # Test model validation
    assert acl_entry.model_validate(data) == acl_entry


def test_acl_entry_from_dict():
    """Test creating ACL entry from dictionary."""
    data = {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "TenantGUID": "223e4567-e89b-12d3-a456-426614174001",
        "BucketGUID": "323e4567-e89b-12d3-a456-426614174002",
        "OwnerGUID": "423e4567-e89b-12d3-a456-426614174003",
        "UserGUID": "523e4567-e89b-12d3-a456-426614174004",
        "CanonicalUser": "user@example.com",
        "EnableRead": True,
        "EnableReadAcp": False,
        "EnableWrite": True,
        "EnableWriteAcp": False,
        "FullControl": False,
        "CreatedUtc": "2023-01-01T12:00:00Z",
    }

    acl_entry = ACLEntryModel.model_validate(data)
    assert isinstance(acl_entry, ACLEntryModel)
    assert acl_entry.guid == data["GUID"]


def test_acl_entry_copy():
    """Test ACL entry model copying."""
    data = {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "TenantGUID": "223e4567-e89b-12d3-a456-426614174001",
        "BucketGUID": "323e4567-e89b-12d3-a456-426614174002",
        "OwnerGUID": "423e4567-e89b-12d3-a456-426614174003",
        "UserGUID": "523e4567-e89b-12d3-a456-426614174004",
        "CanonicalUser": "user@example.com",
        "EnableRead": True,
        "EnableReadAcp": False,
        "EnableWrite": True,
        "EnableWriteAcp": False,
        "FullControl": False,
        "CreatedUtc": "2023-01-01T12:00:00Z",
    }

    acl_entry = ACLEntryModel(**data)
    copied_entry = acl_entry.model_copy()

    assert copied_entry.guid == acl_entry.guid
    assert copied_entry.tenant_guid == acl_entry.tenant_guid
    assert copied_entry.bucket_guid == acl_entry.bucket_guid
    assert copied_entry.owner_guid == acl_entry.owner_guid
    assert copied_entry.user_guid == acl_entry.user_guid
    assert copied_entry.canonical_user == acl_entry.canonical_user
    assert copied_entry.enable_read == acl_entry.enable_read
    assert copied_entry.enable_read_acp == acl_entry.enable_read_acp
    assert copied_entry.enable_write == acl_entry.enable_write
    assert copied_entry.enable_write_acp == acl_entry.enable_write_acp
    assert copied_entry.full_control == acl_entry.full_control
    assert copied_entry.created_utc == acl_entry.created_utc


def test_acl_entry_copy_with_update():
    """Test ACL entry model copying with updates."""
    data = {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "TenantGUID": "223e4567-e89b-12d3-a456-426614174001",
        "BucketGUID": "323e4567-e89b-12d3-a456-426614174002",
        "OwnerGUID": "423e4567-e89b-12d3-a456-426614174003",
        "UserGUID": "523e4567-e89b-12d3-a456-426614174004",
        "CanonicalUser": "user@example.com",
        "EnableRead": True,
        "EnableReadAcp": False,
        "EnableWrite": True,
        "EnableWriteAcp": False,
        "FullControl": False,
        "CreatedUtc": "2023-01-01T12:00:00Z",
    }

    acl_entry = ACLEntryModel(**data)
    # Use field names instead of aliases for the update
    updated_entry = acl_entry.model_copy(
        update={"enable_read": False, "full_control": True}
    )

    assert updated_entry.guid == acl_entry.guid
    assert updated_entry.enable_read is False  # Updated
    assert updated_entry.full_control is True  # Updated
    assert updated_entry.enable_write == acl_entry.enable_write  # Unchanged
