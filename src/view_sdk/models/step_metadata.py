import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..enums.step_runtime_enum import StepRuntimeEnum


class StepMetadataModel(BaseModel):
    """Data flow step."""

    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    name: str = Field(default="My data flow step", alias="Name")
    success: Optional[str] = Field(default=None, alias="Success")
    failure: Optional[str] = Field(default=None, alias="Failure")
    exception: Optional[str] = Field(default=None, alias="Exception")
    runtime: StepRuntimeEnum = Field(default=StepRuntimeEnum.Dotnet8, alias="Runtime")
    step_archive_filename: str = Field(alias="StepArchiveFilename")
    step_entrypoint_filename: str = Field(alias="StepEntrypointFilename")
    step_entrypoint_type: str = Field(alias="StepEntrypointType")
    md5_hash: Optional[str] = Field(default=None, alias="MD5Hash")
    sha1_hash: Optional[str] = Field(default=None, alias="SHA1Hash")
    sha256_hash: Optional[str] = Field(default=None, alias="SHA256Hash")
    notes: Optional[str] = Field(default=None, alias="Notes")
    debug_assembly_load: bool = Field(default=False, alias="DebugAssemblyLoad")
    virtual_environment: Optional[str] = Field(default=None, alias="VirtualEnvironment")
    dependencies_file: Optional[str] = Field(default=None, alias="DependenciesFile")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )
    package: Optional[bytes] = Field(default=None, alias="Package")
    success_step: Optional["StepMetadataModel"] = Field(
        default=None, alias="SuccessStep"
    )
    failure_step: Optional["StepMetadataModel"] = Field(
        default=None, alias="FailureStep"
    )
    exception_step: Optional["StepMetadataModel"] = Field(
        default=None, alias="ExceptionStep"
    )

    @field_validator(
        "step_archive_filename", "step_entrypoint_filename", "step_entrypoint_type"
    )
    def validate_required_fields(cls, v: str, field) -> str:
        if not v or not v.strip():
            raise ValueError(f"{field.alias} must not be empty")
        return v

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)
