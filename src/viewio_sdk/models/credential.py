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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing_extensions import Self


class Credential(BaseModel):
    """
    Credential
    """  # noqa: E501

    guid: StrictStr | None = Field(default=None, alias="GUID")
    tenant_guid: StrictStr | None = Field(default=None, alias="TenantGUID")
    user_guid: StrictStr | None = Field(default=None, alias="UserGUID")
    access_key: StrictStr | None = Field(default="", alias="AccessKey")
    secret_key: StrictStr | None = Field(default="", alias="SecretKey")
    active: StrictBool | None = Field(default=True, alias="Active")
    created_utc: datetime | None = Field(default=None, alias="CreatedUtc")
    __properties: ClassVar[list[str]] = [
        "GUID",
        "TenantGUID",
        "UserGUID",
        "AccessKey",
        "SecretKey",
        "Active",
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
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self | None:
        """Create an instance of Credential from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of Credential from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "GUID": obj.get("GUID"),
                "TenantGUID": obj.get("TenantGUID"),
                "UserGUID": obj.get("UserGUID"),
                "AccessKey": obj.get("AccessKey")
                if obj.get("AccessKey") is not None
                else "",
                "SecretKey": obj.get("SecretKey")
                if obj.get("SecretKey") is not None
                else "",
                "Active": obj.get("Active") if obj.get("Active") is not None else True,
                "CreatedUtc": obj.get("CreatedUtc"),
            }
        )
        return _obj
