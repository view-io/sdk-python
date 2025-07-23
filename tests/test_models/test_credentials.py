import pytest
from datetime import datetime, timezone
from pydantic import ValidationError
from view_sdk.models.credential import CredentialModel

@pytest.fixture
def valid_credential_data():
    return {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "TenantGUID": "223e4567-e89b-12d3-a456-426614174000",
        "UserGUID": "323e4567-e89b-12d3-a456-426614174000",
        "AccessKey": "AKIAIOSFODNN7EXAMPLE",
        "SecretKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
        "Active": False,
        "CreatedUtc": "2023-09-12T12:34:56.789Z"
    }

def test_credential_default_values():
    credential = CredentialModel()
    assert credential.access_key == ""
    assert credential.secret_key == ""
    assert credential.active is True
    assert credential.created_utc.tzinfo is not None

def test_created_utc_validation():
    credential = CredentialModel(CreatedUtc="2023-09-12T12:34:56.789Z")
    assert credential.created_utc.tzinfo is not None

    now = datetime.now(timezone.utc)
    credential = CredentialModel(CreatedUtc=now)
    assert credential.created_utc == now

    naive_now = datetime.now()
    credential = CredentialModel(CreatedUtc=naive_now)

    with pytest.raises(ValidationError) as exc_info:
        CredentialModel(CreatedUtc="invalid-date")
    assert "Input should be a valid datetime" in str(exc_info.value)

def test_field_validation_errors():
    with pytest.raises(ValidationError) as exc_info:
        CredentialModel(
            AccessKey=None,
            SecretKey=None,
            Active="not-a-boolean"
        )
    errors = exc_info.value.errors()
    error_types = [err["type"] for err in errors]
    assert "string_type" in error_types or "none_not_allowed" in error_types

def test_model_copy(valid_credential_data):
    credential = CredentialModel(**valid_credential_data)
    copied = credential.model_copy()
    assert credential.guid == copied.guid
    assert credential.access_key == copied.access_key
    assert credential.secret_key == copied.secret_key
    assert credential.active == copied.active
    assert credential.created_utc == copied.created_utc
