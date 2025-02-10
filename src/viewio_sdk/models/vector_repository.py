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

from viewio_sdk.models.vector_repository_type_enum import VectorRepositoryTypeEnum


class VectorRepository(BaseModel):
    """
    VectorRepository
    """  # noqa: E501

    guid: StrictStr | None = Field(default=None, alias="GUID")
    tenant_guid: StrictStr | None = Field(default=None, alias="TenantGUID")
    name: StrictStr | None = Field(default="My vector repository", alias="Name")
    repository_type: VectorRepositoryTypeEnum | None = Field(
        default=None, alias="RepositoryType"
    )
    endpoint_url: StrictStr | None = Field(default=None, alias="EndpointUrl")
    api_key: StrictStr | None = Field(default=None, alias="ApiKey")
    model: StrictStr | None = Field(default="all-MiniLM-L6-v2", alias="Model")
    dimensionality: Annotated[int, Field(strict=True, ge=1)] | None = Field(
        default=384, alias="Dimensionality"
    )
    database_hostname: StrictStr | None = Field(default=None, alias="DatabaseHostname")
    database_name: StrictStr | None = Field(default=None, alias="DatabaseName")
    database_table: StrictStr | None = Field(default=None, alias="DatabaseTable")
    database_port: Annotated[int, Field(le=65535, strict=True, ge=0)] | None = Field(
        default=0, alias="DatabasePort"
    )
    database_user: StrictStr | None = Field(default=None, alias="DatabaseUser")
    database_password: StrictStr | None = Field(default=None, alias="DatabasePassword")
    prompt_prefix: StrictStr | None = Field(
        default="Use the following pieces of context to answer the question at the end. Documents are sorted by similarity to the question. If the context is not enough for you to answer the question, politely explain that you don't have relevant context. Do not try to make up an answer.",
        alias="PromptPrefix",
    )
    prompt_suffix: StrictStr | None = Field(default=None, alias="PromptSuffix")
    created_utc: datetime | None = Field(default=None, alias="CreatedUtc")
    __properties: ClassVar[list[str]] = [
        "GUID",
        "TenantGUID",
        "Name",
        "RepositoryType",
        "EndpointUrl",
        "ApiKey",
        "Model",
        "Dimensionality",
        "DatabaseHostname",
        "DatabaseName",
        "DatabaseTable",
        "DatabasePort",
        "DatabaseUser",
        "DatabasePassword",
        "PromptPrefix",
        "PromptSuffix",
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
        """Create an instance of VectorRepository from a JSON string"""
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
        # set to None if endpoint_url (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint_url is None and "endpoint_url" in self.model_fields_set:
            _dict["EndpointUrl"] = None

        # set to None if api_key (nullable) is None
        # and model_fields_set contains the field
        if self.api_key is None and "api_key" in self.model_fields_set:
            _dict["ApiKey"] = None

        # set to None if database_hostname (nullable) is None
        # and model_fields_set contains the field
        if (
            self.database_hostname is None
            and "database_hostname" in self.model_fields_set
        ):
            _dict["DatabaseHostname"] = None

        # set to None if database_name (nullable) is None
        # and model_fields_set contains the field
        if self.database_name is None and "database_name" in self.model_fields_set:
            _dict["DatabaseName"] = None

        # set to None if database_table (nullable) is None
        # and model_fields_set contains the field
        if self.database_table is None and "database_table" in self.model_fields_set:
            _dict["DatabaseTable"] = None

        # set to None if database_user (nullable) is None
        # and model_fields_set contains the field
        if self.database_user is None and "database_user" in self.model_fields_set:
            _dict["DatabaseUser"] = None

        # set to None if database_password (nullable) is None
        # and model_fields_set contains the field
        if (
            self.database_password is None
            and "database_password" in self.model_fields_set
        ):
            _dict["DatabasePassword"] = None

        # set to None if prompt_suffix (nullable) is None
        # and model_fields_set contains the field
        if self.prompt_suffix is None and "prompt_suffix" in self.model_fields_set:
            _dict["PromptSuffix"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of VectorRepository from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "GUID": obj.get("GUID"),
                "TenantGUID": obj.get("TenantGUID"),
                "Name": obj.get("Name")
                if obj.get("Name") is not None
                else "My vector repository",
                "RepositoryType": obj.get("RepositoryType"),
                "EndpointUrl": obj.get("EndpointUrl"),
                "ApiKey": obj.get("ApiKey"),
                "Model": obj.get("Model")
                if obj.get("Model") is not None
                else "all-MiniLM-L6-v2",
                "Dimensionality": obj.get("Dimensionality")
                if obj.get("Dimensionality") is not None
                else 384,
                "DatabaseHostname": obj.get("DatabaseHostname"),
                "DatabaseName": obj.get("DatabaseName"),
                "DatabaseTable": obj.get("DatabaseTable"),
                "DatabasePort": obj.get("DatabasePort")
                if obj.get("DatabasePort") is not None
                else 0,
                "DatabaseUser": obj.get("DatabaseUser"),
                "DatabasePassword": obj.get("DatabasePassword"),
                "PromptPrefix": obj.get("PromptPrefix")
                if obj.get("PromptPrefix") is not None
                else "Use the following pieces of context to answer the question at the end. Documents are sorted by similarity to the question. If the context is not enough for you to answer the question, politely explain that you don't have relevant context. Do not try to make up an answer.",
                "PromptSuffix": obj.get("PromptSuffix"),
                "CreatedUtc": obj.get("CreatedUtc"),
            }
        )
        return _obj
