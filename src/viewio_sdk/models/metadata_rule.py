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
from typing_extensions import Annotated, Self

from viewio_sdk.models.data_catalog_type_enum import DataCatalogTypeEnum


class MetadataRule(BaseModel):
    """
    MetadataRule
    """  # noqa: E501

    guid: StrictStr | None = Field(default=None, alias="GUID")
    tenant_guid: StrictStr | None = Field(default=None, alias="TenantGUID")
    bucket_guid: StrictStr | None = Field(default=None, alias="BucketGUID")
    owner_guid: StrictStr | None = Field(default=None, alias="OwnerGUID")
    name: StrictStr | None = Field(default=None, alias="Name")
    content_type: StrictStr | None = Field(default="text/plain", alias="ContentType")
    prefix: StrictStr | None = Field(default=None, alias="Prefix")
    suffix: StrictStr | None = Field(default=None, alias="Suffix")
    processing_endpoint: (
        Annotated[str, Field(min_length=1, strict=True, max_length=2083)] | None
    ) = Field(default="http://localhost:8501/processor", alias="ProcessingEndpoint")
    cleanup_endpoint: (
        Annotated[str, Field(min_length=1, strict=True, max_length=2083)] | None
    ) = Field(
        default="http://localhost:8501/processor/cleanup", alias="CleanupEndpoint"
    )
    type_detector_endpoint: (
        Annotated[str, Field(min_length=1, strict=True, max_length=2083)] | None
    ) = Field(
        default="http://localhost:8501/processor/typedetector",
        alias="TypeDetectorEndpoint",
    )
    semantic_cell_endpoint: (
        Annotated[str, Field(min_length=1, strict=True, max_length=2083)] | None
    ) = Field(default="http://localhost:8341/", alias="SemanticCellEndpoint")
    max_chunk_content_length: (
        Annotated[int, Field(le=16384, strict=True, ge=256)] | None
    ) = Field(default=512, alias="MaxChunkContentLength")
    shift_size: Annotated[int, Field(le=16384, strict=True, ge=1)] | None = Field(
        default=512, alias="ShiftSize"
    )
    udr_endpoint: (
        Annotated[str, Field(min_length=1, strict=True, max_length=2083)] | None
    ) = Field(default="http://localhost:8321/", alias="UdrEndpoint")
    data_catalog_type: DataCatalogTypeEnum | None = Field(
        default=None, alias="DataCatalogType"
    )
    data_catalog_endpoint: (
        Annotated[str, Field(min_length=1, strict=True, max_length=2083)] | None
    ) = Field(default="http://localhost:8201/", alias="DataCatalogEndpoint")
    data_catalog_collection: StrictStr | None = Field(
        default=None, alias="DataCatalogCollection"
    )
    graph_repository_guid: StrictStr | None = Field(
        default=None, alias="GraphRepositoryGUID"
    )
    top_terms: Annotated[int, Field(strict=True, ge=1)] | None = Field(
        default=25, alias="TopTerms"
    )
    case_insensitive: StrictBool | None = Field(default=True, alias="CaseInsensitive")
    include_flattened: StrictBool | None = Field(default=True, alias="IncludeFlattened")
    target_bucket_guid: StrictStr | None = Field(default=None, alias="TargetBucketGUID")
    max_content_length: Annotated[int, Field(strict=True, ge=1)] | None = Field(
        default=16777216, alias="MaxContentLength"
    )
    retention_minutes: Annotated[int, Field(strict=True, ge=1)] | None = Field(
        default=None, alias="RetentionMinutes"
    )
    created_utc: datetime | None = Field(default=None, alias="CreatedUtc")
    __properties: ClassVar[list[str]] = [
        "GUID",
        "TenantGUID",
        "BucketGUID",
        "OwnerGUID",
        "Name",
        "ContentType",
        "Prefix",
        "Suffix",
        "ProcessingEndpoint",
        "CleanupEndpoint",
        "TypeDetectorEndpoint",
        "SemanticCellEndpoint",
        "MaxChunkContentLength",
        "ShiftSize",
        "UdrEndpoint",
        "DataCatalogType",
        "DataCatalogEndpoint",
        "DataCatalogCollection",
        "GraphRepositoryGUID",
        "TopTerms",
        "CaseInsensitive",
        "IncludeFlattened",
        "TargetBucketGUID",
        "MaxContentLength",
        "RetentionMinutes",
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
        """Create an instance of MetadataRule from a JSON string"""
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
        # set to None if tenant_guid (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_guid is None and "tenant_guid" in self.model_fields_set:
            _dict["TenantGUID"] = None

        # set to None if bucket_guid (nullable) is None
        # and model_fields_set contains the field
        if self.bucket_guid is None and "bucket_guid" in self.model_fields_set:
            _dict["BucketGUID"] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict["Name"] = None

        # set to None if prefix (nullable) is None
        # and model_fields_set contains the field
        if self.prefix is None and "prefix" in self.model_fields_set:
            _dict["Prefix"] = None

        # set to None if suffix (nullable) is None
        # and model_fields_set contains the field
        if self.suffix is None and "suffix" in self.model_fields_set:
            _dict["Suffix"] = None

        # set to None if data_catalog_collection (nullable) is None
        # and model_fields_set contains the field
        if (
            self.data_catalog_collection is None
            and "data_catalog_collection" in self.model_fields_set
        ):
            _dict["DataCatalogCollection"] = None

        # set to None if graph_repository_guid (nullable) is None
        # and model_fields_set contains the field
        if (
            self.graph_repository_guid is None
            and "graph_repository_guid" in self.model_fields_set
        ):
            _dict["GraphRepositoryGUID"] = None

        # set to None if target_bucket_guid (nullable) is None
        # and model_fields_set contains the field
        if (
            self.target_bucket_guid is None
            and "target_bucket_guid" in self.model_fields_set
        ):
            _dict["TargetBucketGUID"] = None

        # set to None if retention_minutes (nullable) is None
        # and model_fields_set contains the field
        if (
            self.retention_minutes is None
            and "retention_minutes" in self.model_fields_set
        ):
            _dict["RetentionMinutes"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of MetadataRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "GUID": obj.get("GUID"),
                "TenantGUID": obj.get("TenantGUID"),
                "BucketGUID": obj.get("BucketGUID"),
                "OwnerGUID": obj.get("OwnerGUID"),
                "Name": obj.get("Name"),
                "ContentType": obj.get("ContentType")
                if obj.get("ContentType") is not None
                else "text/plain",
                "Prefix": obj.get("Prefix"),
                "Suffix": obj.get("Suffix"),
                "ProcessingEndpoint": obj.get("ProcessingEndpoint")
                if obj.get("ProcessingEndpoint") is not None
                else "http://localhost:8501/processor",
                "CleanupEndpoint": obj.get("CleanupEndpoint")
                if obj.get("CleanupEndpoint") is not None
                else "http://localhost:8501/processor/cleanup",
                "TypeDetectorEndpoint": obj.get("TypeDetectorEndpoint")
                if obj.get("TypeDetectorEndpoint") is not None
                else "http://localhost:8501/processor/typedetector",
                "SemanticCellEndpoint": obj.get("SemanticCellEndpoint")
                if obj.get("SemanticCellEndpoint") is not None
                else "http://localhost:8341/",
                "MaxChunkContentLength": obj.get("MaxChunkContentLength")
                if obj.get("MaxChunkContentLength") is not None
                else 512,
                "ShiftSize": obj.get("ShiftSize")
                if obj.get("ShiftSize") is not None
                else 512,
                "UdrEndpoint": obj.get("UdrEndpoint")
                if obj.get("UdrEndpoint") is not None
                else "http://localhost:8321/",
                "DataCatalogType": obj.get("DataCatalogType"),
                "DataCatalogEndpoint": obj.get("DataCatalogEndpoint")
                if obj.get("DataCatalogEndpoint") is not None
                else "http://localhost:8201/",
                "DataCatalogCollection": obj.get("DataCatalogCollection"),
                "GraphRepositoryGUID": obj.get("GraphRepositoryGUID"),
                "TopTerms": obj.get("TopTerms")
                if obj.get("TopTerms") is not None
                else 25,
                "CaseInsensitive": obj.get("CaseInsensitive")
                if obj.get("CaseInsensitive") is not None
                else True,
                "IncludeFlattened": obj.get("IncludeFlattened")
                if obj.get("IncludeFlattened") is not None
                else True,
                "TargetBucketGUID": obj.get("TargetBucketGUID"),
                "MaxContentLength": obj.get("MaxContentLength")
                if obj.get("MaxContentLength") is not None
                else 16777216,
                "RetentionMinutes": obj.get("RetentionMinutes"),
                "CreatedUtc": obj.get("CreatedUtc"),
            }
        )
        return _obj
