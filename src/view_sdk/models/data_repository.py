import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class DataRepositoryModel(BaseModel):
    id: int = Field(default=0, ge=1, alias="Id")
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    owner_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="OwnerGUID"
    )
    name: str = Field(default="My file repository", alias="Name")
    repository_type: str = Field(
        default="File", alias="RepositoryType"
    )  # Replace with Enum if needed
    use_ssl: bool = Field(default=False, alias="UseSsl")
    include_subdirectories: bool = Field(default=True, alias="IncludeSubdirectories")

    disk_directory: Optional[str] = Field(None, alias="DiskDirectory")
    s3_endpoint_url: Optional[str] = Field(None, alias="S3EndpointUrl")
    s3_base_url: Optional[str] = Field(None, alias="S3BaseUrl")
    s3_access_key: Optional[str] = Field(None, alias="S3AccessKey")
    s3_secret_key: Optional[str] = Field(None, alias="S3SecretKey")
    s3_bucket_name: Optional[str] = Field(None, alias="S3BucketName")
    s3_region: Optional[str] = Field(None, alias="S3Region")

    azure_endpoint_url: Optional[str] = Field(None, alias="AzureEndpointUrl")
    azure_account_name: Optional[str] = Field(None, alias="AzureAccountName")
    azure_container_name: Optional[str] = Field(None, alias="AzureContainerName")
    azure_access_key: Optional[str] = Field(None, alias="AzureAccessKey")

    cifs_hostname: Optional[str] = Field(None, alias="CifsHostname")
    cifs_username: Optional[str] = Field(None, alias="CifsUsername")
    cifs_password: Optional[str] = Field(None, alias="CifsPassword")
    cifs_share_name: Optional[str] = Field(None, alias="CifsShareName")

    nfs_hostname: Optional[str] = Field(None, alias="NfsHostname")
    nfs_user_id: int = Field(default=0, ge=0, alias="NfsUserId")
    nfs_group_id: int = Field(default=0, ge=0, alias="NfsGroupId")
    nfs_share_name: Optional[str] = Field(None, alias="NfsShareName")
    nfs_version: Optional[str] = Field(None, alias="NfsVersion")

    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    _directory_validator_fields = [
        "disk_directory",
        "s3_endpoint_url",
        "s3_base_url",
        "azure_endpoint_url",
    ]

    @field_validator(*_directory_validator_fields, mode="before")
    def validate_directory(cls, v):
        if v:
            v = v.replace("\\", "/")
            if not v.endswith("/"):
                v += "/"
        return v

    @field_validator("id")
    def validate_id(cls, v):
        if v < 1:
            raise ValueError("Id must be greater than or equal to 1.")
        return v

    @field_validator("nfs_user_id", "nfs_group_id")
    def validate_nfs_ids(cls, v, field):
        if v < 0:
            raise ValueError(f"{field.name} must be non-negative.")
        return v

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
