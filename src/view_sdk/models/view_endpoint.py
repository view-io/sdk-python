import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class ViewEndpointModel(BaseModel):
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    owner_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="OwnerGUID"
    )
    name: str = Field(default="My View endpoint", alias="Name")
    use_ssl: bool = Field(default=False, alias="UseSsl")

    s3_url: str = Field(default="http://localhost:8002/", alias="S3Url")
    s3_uri: str = Field(default="http://localhost:8002/", alias="S3Uri")
    s3_base_url: str = Field(
        default="http://localhost:8002/{bucket}/{key}", alias="S3BaseUrl"
    )
    rest_url: str = Field(default="http://localhost:8001/", alias="RestUrl")

    bucket_name: str = Field(default="data", alias="BucketName")
    region: str = Field(default="us-west-1", alias="Region")
    access_key: Optional[str] = Field(default=None, alias="AccessKey")
    secret_key: Optional[str] = Field(default=None, alias="SecretKey")
    api_key: Optional[str] = Field(default=None, alias="ApiKey")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)

    @field_validator("s3_url")
    def validate_s3_url(cls, v):
        if not v:
            raise ValueError("S3 URL must not be empty.")

        if not v.endswith("/"):
            v += "/"
        return v

    @field_validator("s3_base_url")
    def validate_s3_base_url(cls, v):
        if not v:
            raise ValueError("S3 Base URL must not be empty.")
        if "{bucket}" not in v:
            raise ValueError("Supplied S3 base URL is missing {bucket} from URL.")
        if "{key}" not in v:
            raise ValueError("Supplied S3 base URL is missing {key} from URL.")

        if not v.endswith("/"):
            v += "/"
        return v

    @field_validator("rest_url")
    def validate_rest_url(cls, v):
        if not v:
            raise ValueError("REST URL must not be empty.")

        if not v.endswith("/"):
            v += "/"
        return v
