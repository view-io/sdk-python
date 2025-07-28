import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..enums.software_instance_type_enum import SoftwareInstanceTypeEnum


class NodeModel(BaseModel):
    id: int = Field(default=None, ge=1, exclude=True)
    guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="GUID", strict=True
    )
    name: Optional[str] = Field(default=None, alias="Name")
    hostname: str = Field(default="localhost", alias="Hostname")
    instance_type: SoftwareInstanceTypeEnum = Field(
        default=SoftwareInstanceTypeEnum.storage_server, alias="InstanceType"
    )
    last_start_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="LastStartUtc"
    )
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    # Validator for id to mimic the C# behavior where Id should be greater than 0
    @field_validator("id")
    def validate_id(cls, value):
        if value < 1:
            raise ValueError("Id must be greater than 0")
        return value

    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)


if __name__ == "__main__":
    # Test the NodeModel
    node_data = {
        "id": 1,
        "guid": "123e4567-e89b-12d3-a456-426614174000",
        "name": "Test Node",
        "hostname": "localhost",
        "instance_type": "storage_server",
        "last_start_utc": "2023-09-12T12:34:56.789Z",
        "created_utc": "2023-09-12T12:34:56.789Z",
    }
    print(NodeModel(**node_data))
