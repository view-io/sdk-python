import pytest
from datetime import datetime, timezone
from view_sdk.models.metadata_rule import MetadataRuleModel
from view_sdk.enums.data_catalog_type_enum import DataCatalogTypeEnum


def test_metadata_rule_create_valid():
    data = {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "TenantGUID": "abc123-e89b-12d3-a456-426614174000",
        "BucketGUID": "def456-e89b-12d3-a456-426614174000",
        "OwnerGUID": "ghi789-e89b-12d3-a456-426614174000",
        "Name": "Test Metadata Rule",
        "ContentType": "text/plain",
        "Prefix": "test-prefix",
        "Suffix": "test-suffix",
        "ProcessingEndpoint": "http://localhost:8000/v1.0/tenants/default/processing",
        "ProcessingAccessKey": "default",
        "CleanupEndpoint": "http://localhost:8000/v1.0/tenants/default/processing/cleanup",
        "CleanupAccessKey": "default",
        "ImageTextExtraction": True,
        "TopTerms": 25,
        "CaseInsensitive": True,
        "IncludeFlattened": True,
        "DataCatalogType": DataCatalogTypeEnum.Lexi,
        "DataCatalogEndpoint": "http://localhost:8000/",
        "DataCatalogAccessKey": "default",
        "DataCatalogCollection": "test-collection",
        "GraphRepositoryGUID": "jkl012-e89b-12d3-a456-426614174000",
        "MaxContentLength": 16777216,
        "RetentionMinutes": 60,
        "CreatedUtc": datetime(2023, 4, 1, 12, 0, 0, tzinfo=timezone.utc),
    }

    rule = MetadataRuleModel(**data)
    assert rule.guid == "123e4567-e89b-12d3-a456-426614174000"
    assert rule.tenant_guid == "abc123-e89b-12d3-a456-426614174000"
    assert rule.bucket_guid == "def456-e89b-12d3-a456-426614174000"
    assert rule.owner_guid == "ghi789-e89b-12d3-a456-426614174000"
    assert rule.name == "Test Metadata Rule"
    assert rule.content_type == "text/plain"
    assert rule.prefix == "test-prefix"
    assert rule.suffix == "test-suffix"
    assert (
        str(rule.processing_endpoint)
        == "http://localhost:8000/v1.0/tenants/default/processing"
    )
    assert rule.processing_access_key == "default"
    assert (
        str(rule.cleanup_endpoint)
        == "http://localhost:8000/v1.0/tenants/default/processing/cleanup"
    )
    assert rule.cleanup_access_key == "default"
    assert rule.top_terms == 25
    assert rule.case_insensitive is True
    assert rule.include_flattened is True
    assert rule.data_catalog_type == DataCatalogTypeEnum.Lexi
    assert str(rule.data_catalog_endpoint) == "http://localhost:8000/"
    assert rule.data_catalog_access_key == "default"
    assert rule.data_catalog_collection == "test-collection"
    assert rule.graph_repository_guid == "jkl012-e89b-12d3-a456-426614174000"
    assert rule.max_content_length == 16777216
    assert rule.retention_minutes == 60
    assert rule.created_utc == datetime(2023, 4, 1, 12, 0, 0, tzinfo=timezone.utc)


def test_metadata_rule_invalid_data():
    with pytest.raises(ValueError):
        MetadataRuleModel(
            guid="invalid-guid",
            processing_endpoint="invalid-url",
            cleanup_endpoint="invalid-url",
            data_catalog_endpoint="invalid-url",
            top_terms=0,
            max_content_length=0,
            retention_minutes=0,
        )
