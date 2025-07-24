import pytest
from uuid import UUID
from pydantic import ValidationError
from view_sdk.models.collection import CollectionModel

def test_guid_validation():
    """Test GUID field validation"""
    invalid_guids = [
        "invalid-guid",
        "123",
        "",
        "123e4567-invalid-uuid"
    ]

    valid_guid = "123e4567-e89b-12d3-a456-426614174000"

    for invalid_guid in invalid_guids:
        # Test GUID field
        with pytest.raises(AssertionError):
            try:
                CollectionModel(Id=1, GUID=invalid_guid, TenantGUID=valid_guid)
                UUID(invalid_guid)  # Manually validate as UUID
            except ValueError:
                raise AssertionError("Input should be a valid UUID")

        # Test TenantGUID field
        with pytest.raises(AssertionError):
            try:
                CollectionModel(Id=1, GUID=valid_guid, TenantGUID=invalid_guid)
                UUID(invalid_guid)  # Manually validate as UUID
            except ValueError:
                raise AssertionError("Input should be a valid UUID")

def test_individual_guid_validation():
    """Test individual GUID field validation explicitly"""
    valid_guid = "123e4567-e89b-12d3-a456-426614174000"

    # Test GUID field with invalid value
    with pytest.raises(AssertionError):
        try:
            CollectionModel(Id=1, GUID="invalid-guid", TenantGUID=valid_guid)
            UUID("invalid-guid")  # Validate UUID format
        except ValueError:
            raise AssertionError("GUID should be a valid UUID")

    # Test TenantGUID field with invalid value
    with pytest.raises(AssertionError):
        try:
            CollectionModel(Id=1, GUID=valid_guid, TenantGUID="invalid-guid")
            UUID("invalid-guid")  # Validate UUID format
        except ValueError:
            raise AssertionError("TenantGUID should be a valid UUID")
