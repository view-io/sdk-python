import base64
import binascii
import uuid
from datetime import datetime, timezone
from typing import Optional
from pydantic import Base64Str, BaseModel, ConfigDict, Field, field_validator
from .user_master import UserMasterModel


class EncryptionKeyModel(BaseModel):
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    owner_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="OwnerGUID"
    )
    key_base64: Base64Str = Field(default="", alias="KeyBase64")
    key_hex: str = Field(default="", alias="KeyHex")
    iv_base64: Base64Str = Field(default="", alias="IvBase64")
    iv_hex: str = Field(default="", alias="IvHex")
    salt_base64: Base64Str = Field(default="", alias="SaltBase64")
    salt_hex: str = Field(default="", alias="SaltHex")
    name: str = Field(default="", alias="Name")
    description: str = Field(default="", alias="Description")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )
    user: Optional[UserMasterModel] = Field(None, alias="User")
    key: Optional[bytes] = Field(default=None, exclude=True, alias="Key")
    iv: Optional[bytes] = Field(default=None, exclude=True, alias="Iv")
    salt: Optional[bytes] = Field(default=None, exclude=True, alias="Salt")

    # Validation to ensure key length matches constraints from C#
    @field_validator("key_base64", "iv_base64", "salt_base64", mode="before")
    def validate_base64_length(cls, value, field):
        decoded_value = base64.b64decode(value)
        if field.field_name == "key_base64" and len(decoded_value) != 32:
            raise ValueError("Key must be 32 bytes in length")
        # if field.field_name in ['iv_base64', 'salt_base64'] and len(decoded_value) != 16:
        #     raise ValueError(f'{field.field_name.replace("_", " ").capitalize()} must be 16 bytes in length')
        return value

    @field_validator("key_hex", "iv_hex", "salt_hex", mode="before")
    def validate_hex_length(cls, value, field):
        decoded_value = binascii.unhexlify(value)
        if field.field_name == "key_hex" and len(decoded_value) != 32:
            raise ValueError("Key must be 32 bytes in length")
        # if field.field_name in ['iv_hex', 'salt_hex'] and len(decoded_value) != 16:
        #     raise ValueError(f'{field.field_name.replace("_", " ").capitalize()} must be 16 bytes in length')
        return value

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
