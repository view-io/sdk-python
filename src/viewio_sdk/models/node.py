"""
View.IO SDK

This SDK provides a set of tools and functions to interact with the View.IO APIs. It simplifies the process of integrating View.IO's services into your application by making API requests, and processing responses.

The version of the OpenAPI document: 0.1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from datetime import datetime
from typing import Any, ClassVar

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing_extensions import Annotated, Self

from viewio_sdk.models.software_instance_type_enum import SoftwareInstanceTypeEnum


class Node(BaseModel):
    """
    Node
    """  # noqa: E501

    id: Annotated[int, Field(strict=True, ge=1)] | None = None
    guid: StrictStr | None = Field(default=None, alias="GUID")
    name: StrictStr | None = None
    hostname: StrictStr | None = "localhost"
    instance_type: SoftwareInstanceTypeEnum | None = Field(
        default=None, alias="InstanceType"
    )
    last_start_utc: datetime | None = Field(default=None, alias="LastStartUtc")
    created_utc: datetime | None = Field(default=None, alias="CreatedUtc")
    __properties: ClassVar[list[str]] = [
        "id",
        "GUID",
        "name",
        "hostname",
        "InstanceType",
        "LastStartUtc",
        "CreatedUtc",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self | None:
        """Create an instance of Node from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: set[str] = set()

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict["name"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of Node from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "GUID": obj.get("GUID"),
                "name": obj.get("name"),
                "hostname": obj.get("hostname")
                if obj.get("hostname") is not None
                else "localhost",
                "InstanceType": obj.get("InstanceType"),
                "LastStartUtc": obj.get("LastStartUtc"),
                "CreatedUtc": obj.get("CreatedUtc"),
            }
        )
        return _obj
