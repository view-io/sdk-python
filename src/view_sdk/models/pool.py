import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from ..enums.compression_type_enum import CompressionTypeEnum
from ..enums.object_write_mode_enum import ObjectWriteModeEnum


class StoragePool(BaseModel):
    id: Optional[int] = Field(None, ge=1, alias="Id", exclude=True)
    guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="GUID", description="GUID"
    )
    tenant_guid: Optional[str] = Field(
        None, alias="TenantGUID", description="Tenant GUID"
    )
    encryption_key_guid: Optional[str] = Field(
        None, alias="EncryptionKeyGUID", description="Encryption Key GUID"
    )
    name: Optional[str] = Field(None, alias="Name", description="Name")
    provider: Optional[str] = Field(
        default="Disk", alias="Provider", description="Provider"
    )
    write_mode: ObjectWriteModeEnum = Field(
        default=ObjectWriteModeEnum.GUID,
        alias="WriteMode",
        description="Object Write Mode",
    )
    use_ssl: bool = Field(
        default=False, alias="UseSsl", description="Enable or disable SSL"
    )
    endpoint: Optional[HttpUrl] = Field(
        None, alias="Endpoint", description="Endpoint URL for storage provider"
    )
    access_key: Optional[str] = Field(None, alias="AccessKey", description="Access Key")
    secret_key: Optional[str] = Field(None, alias="SecretKey", description="Secret Key")
    aws_region: Optional[str] = Field(None, alias="AwsRegion", description="AWS Region")
    aws_bucket: Optional[str] = Field(None, alias="AwsBucket", description="AWS Bucket")
    aws_base_domain: Optional[str] = Field(
        None, alias="AwsBaseDomain", description="AWS Base Domain"
    )
    aws_base_url: Optional[str] = Field(
        None, alias="AwsBaseUrl", description="AWS Base URL"
    )
    disk_directory: Optional[str] = Field(
        None, alias="DiskDirectory", description="Disk Directory"
    )
    azure_account: Optional[str] = Field(
        None, alias="AzureAccount", description="Azure Account"
    )
    azure_container: Optional[str] = Field(
        None, alias="AzureContainer", description="Azure Container"
    )
    compress: CompressionTypeEnum = Field(
        default=CompressionTypeEnum.none,
        alias="Compress",
        description="Compression Type",
    )
    enable_read_caching: bool = Field(
        default=False,
        alias="EnableReadCaching",
        description="Enable or disable read caching",
    )
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        alias="CreatedUtc",
        description="Created UTC",
    )

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
