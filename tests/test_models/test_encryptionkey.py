import pytest
import base64
from datetime import datetime, timezone
from pydantic import ValidationError
from view_sdk.models.encryption_key import EncryptionKeyModel

def generate_valid_base64(length: int = 32) -> str:
    """Helper function to generate valid base64 of specified byte length."""
    return base64.b64encode(b'0' * length).decode('utf-8')

def generate_valid_hex(length: int = 32) -> str:
    """Helper function to generate valid hex of specified byte length."""
    return '0' * (length * 2)  # Each byte is 2 hex characters

def test_encryption_key_minimal_creation():
    """Test creating an EncryptionKey with minimal required fields."""
    key_base64 = generate_valid_base64(32)
    key_hex = generate_valid_hex(32)

    key = EncryptionKeyModel(
        tenant_guid="12345678-1234-5678-1234-567812345678",
        owner_guid="98765432-1234-5678-1234-567812345678",
        key_base64=key_base64,
        key_hex=key_hex,
        iv_base64=generate_valid_base64(16),
        iv_hex=generate_valid_hex(16),
        salt_base64=generate_valid_base64(16),
        salt_hex=generate_valid_hex(16)
    )

    assert isinstance(key.created_utc, datetime)
    assert key.name == ""
    assert key.description == ""

def test_encryption_key_full_creation():
    """Test creating an EncryptionKey with all fields."""
    data = {
        "GUID": "12345678-1234-5678-1234-567812345678",
        "TenantGUID": "98765432-1234-5678-1234-567812345678",
        "OwnerGUID": "abcdef12-1234-5678-1234-567812345678",
        "KeyBase64": generate_valid_base64(32),
        "KeyHex": generate_valid_hex(32),
        "IvBase64": generate_valid_base64(16),
        "IvHex": generate_valid_hex(16),
        "SaltBase64": generate_valid_base64(16),
        "SaltHex": generate_valid_hex(16),
        "Name": "Test Key",
        "Description": "Test Description",
        "CreatedUtc": datetime.now(timezone.utc)
    }

    key = EncryptionKeyModel(**data)
    assert key.name == "Test Key"
    assert key.description == "Test Description"

def test_invalid_key_base64_length():
    """Test validation of key_base64 length (must be 32 bytes when decoded)."""
    with pytest.raises(ValidationError) as exc_info:
        EncryptionKeyModel(
            tenant_guid="12345678-1234-5678-1234-567812345678",
            owner_guid="98765432-1234-5678-1234-567812345678",
            key_base64=generate_valid_base64(16),  # Too short
            key_hex=generate_valid_hex(32),
            iv_base64=generate_valid_base64(16),
            iv_hex=generate_valid_hex(16),
            salt_base64=generate_valid_base64(16),
            salt_hex=generate_valid_hex(16)
        )
    assert "Key must be 32 bytes in length" in str(exc_info.value)

def test_invalid_key_hex_length():
    """Test validation of key_hex length (must be 32 bytes when decoded)."""
    with pytest.raises(ValidationError) as exc_info:
        EncryptionKeyModel(
            tenant_guid="12345678-1234-5678-1234-567812345678",
            owner_guid="98765432-1234-5678-1234-567812345678",
            key_base64=generate_valid_base64(32),
            key_hex=generate_valid_hex(16),  # Too short
            iv_base64=generate_valid_base64(16),
            iv_hex=generate_valid_hex(16),
            salt_base64=generate_valid_base64(16),
            salt_hex=generate_valid_hex(16)
        )
    assert "Key must be 32 bytes in length" in str(exc_info.value)

def test_invalid_base64_format():
    """Test validation of base64 format."""
    with pytest.raises(ValidationError) as exc_info:
        EncryptionKeyModel(
            tenant_guid="12345678-1234-5678-1234-567812345678",
            owner_guid="98765432-1234-5678-1234-567812345678",
            key_base64="not-base64!@#",
            key_hex=generate_valid_hex(32),
            iv_base64=generate_valid_base64(16),
            iv_hex=generate_valid_hex(16),
            salt_base64=generate_valid_base64(16),
            salt_hex=generate_valid_hex(16)
        )
    assert "Invalid base64" in str(exc_info.value)

def test_invalid_hex_format():
    """Test validation of hex format."""
    with pytest.raises(ValidationError) as exc_info:
        EncryptionKeyModel(
            tenant_guid="12345678-1234-5678-1234-567812345678",
            owner_guid="98765432-1234-5678-1234-567812345678",
            key_base64=generate_valid_base64(32),
            key_hex="not-hex!@#",
            iv_base64=generate_valid_base64(16),
            iv_hex=generate_valid_hex(16),
            salt_base64=generate_valid_base64(16),
            salt_hex=generate_valid_hex(16)
        )
    assert "Non-hexadecimal digit found" in str(exc_info.value)

def test_cross_format_validation():
    """Test that base64 and hex values represent the same data."""
    key_bytes = b'1' * 32
    key = EncryptionKeyModel(
        tenant_guid="12345678-1234-5678-1234-567812345678",
        owner_guid="98765432-1234-5678-1234-567812345678",
        key_base64=base64.b64encode(key_bytes).decode(),
        key_hex=key_bytes.hex(),
        iv_base64=generate_valid_base64(16),
        iv_hex=generate_valid_hex(16),
        salt_base64=generate_valid_base64(16),
        salt_hex=generate_valid_hex(16)
    )

    assert key.key_base64.encode() == bytes.fromhex(key.key_hex)
