import pytest
from datetime import datetime, timezone
from pydantic import ValidationError
from view_sdk.models.embeddings_rule import EmbeddingsRuleModel
from view_sdk.enums.embeddings_generator_enum import EmbeddingsGeneratorEnum


def test_embeddings_rule_minimal_creation():
    """Test creating an EmbeddingsRule with minimal required fields."""
    rule = EmbeddingsRuleModel(owner_guid="12345678-1234-5678-1234-567812345678")

    # Check default values
    assert rule.content_type == "text/plain"
    assert rule.embeddings_generator == EmbeddingsGeneratorEnum.LCProxy
    assert (
        rule.embeddings_generator_url
        == "http://localhost:8000/v1.0/tenants/default/embeddings"
    )
    assert rule.embeddings_generator_api_key == "default"
    assert (
        rule.processing_endpoint
        == "http://localhost:8000/v1.0/tenants/default/processing"
    )
    assert rule.processing_access_key == "default"
    assert rule.vector_store_url == "http://localhost:8000/"
    assert rule.vector_store_access_key == "default"
    assert rule.embeddings_batch_size == 16
    assert rule.max_embeddings_tasks == 16
    assert rule.max_embeddings_retries == 3
    assert rule.max_embeddings_failures == 3
    assert rule.max_content_length == 16 * 1024 * 1024
    assert isinstance(rule.created_utc, datetime)


def test_embeddings_rule_full_creation():
    """Test creating an EmbeddingsRule with all fields."""
    data = {
        "GUID": "12345678-1234-5678-1234-567812345678",
        "TenantGUID": "98765432-1234-5678-1234-567812345678",
        "BucketGUID": "abcdef12-1234-5678-1234-567812345678",
        "OwnerGUID": "11111111-1234-5678-1234-567812345678",
        "Name": "Test Embeddings Rule",
        "ContentType": "application/pdf",
        "Prefix": "docs/",
        "Suffix": ".pdf",
        "GraphRepositoryGUID": "33333333-1234-5678-1234-567812345678",
        "VectorRepositoryGUID": "44444444-1234-5678-1234-567812345678",
        "ProcessingEndpoint": "http://custom:8000/processing",
        "ProcessingAccessKey": "proc-key-123",
        "EmbeddingsGenerator": "OpenAI",
        "EmbeddingsGeneratorUrl": "http://custom:8000/embeddings",
        "EmbeddingsGeneratorApiKey": "emb-key-123",
        "EmbeddingsBatchSize": 32,
        "MaxEmbeddingsTasks": 24,
        "MaxEmbeddingsRetries": 5,
        "MaxEmbeddingsFailures": 4,
        "VectorStoreUrl": "http://custom:8000/vectors",
        "VectorStoreAccessKey": "vec-key-123",
        "MaxContentLength": 32 * 1024 * 1024,
        "RetentionMinutes": 1440,
        "CreatedUtc": datetime.now(timezone.utc),
    }

    rule = EmbeddingsRuleModel(**data)
    assert rule.name == "Test Embeddings Rule"
    assert rule.content_type == "application/pdf"
    assert rule.prefix == "docs/"
    assert rule.suffix == ".pdf"
    assert rule.processing_endpoint == "http://custom:8000/processing"
    assert rule.processing_access_key == "proc-key-123"
    assert rule.embeddings_generator == EmbeddingsGeneratorEnum.OpenAI
    assert rule.embeddings_generator_url == "http://custom:8000/embeddings"
    assert rule.embeddings_generator_api_key == "emb-key-123"
    assert rule.vector_store_url == "http://custom:8000/vectors"
    assert rule.vector_store_access_key == "vec-key-123"
    assert rule.embeddings_batch_size == 32
    assert rule.max_embeddings_tasks == 24


def test_invalid_batch_size():
    """Test validation of batch size."""
    with pytest.raises(ValidationError) as exc_info:
        EmbeddingsRuleModel(
            owner_guid="12345678-1234-5678-1234-567812345678", embeddings_batch_size=0
        )
    assert "embeddings_batch_size" in str(exc_info.value)
    assert "greater than or equal to 1" in str(exc_info.value)


def test_invalid_max_generator_tasks():
    """Test validation of max generator tasks."""
    with pytest.raises(ValidationError) as exc_info:
        EmbeddingsRuleModel(
            owner_guid="12345678-1234-5678-1234-567812345678", max_embeddings_tasks=0
        )
    assert "max_embeddings_tasks" in str(exc_info.value)
    assert "greater than or equal to 1" in str(exc_info.value)


def test_invalid_max_retries():
    """Test validation of max retries."""
    with pytest.raises(ValidationError) as exc_info:
        EmbeddingsRuleModel(
            owner_guid="12345678-1234-5678-1234-567812345678", max_embeddings_retries=0
        )
    assert "max_embeddings_retries" in str(exc_info.value)
    assert "greater than or equal to 1" in str(exc_info.value)


def test_invalid_max_failures():
    """Test validation of max failures."""
    with pytest.raises(ValidationError) as exc_info:
        EmbeddingsRuleModel(
            owner_guid="12345678-1234-5678-1234-567812345678", max_embeddings_failures=0
        )
    assert "max_embeddings_failures" in str(exc_info.value)
    assert "greater than or equal to 1" in str(exc_info.value)


def test_invalid_retention_minutes():
    """Test validation of retention minutes."""
    with pytest.raises(ValidationError) as exc_info:
        EmbeddingsRuleModel(
            owner_guid="12345678-1234-5678-1234-567812345678", retention_minutes=0
        )
    assert "retention_minutes" in str(exc_info.value)
    assert "greater than or equal to 1" in str(exc_info.value)


def test_invalid_max_content_length():
    """Test validation of max content length."""
    with pytest.raises(ValidationError) as exc_info:
        EmbeddingsRuleModel(
            owner_guid="12345678-1234-5678-1234-567812345678", max_content_length=0
        )
    assert "max_content_length" in str(exc_info.value)
    assert "greater than or equal to 1" in str(exc_info.value)


def test_embeddings_generator_enum():
    """Test validation of embeddings generator enum."""
    rule = EmbeddingsRuleModel(
        owner_guid="12345678-1234-5678-1234-567812345678",
        embeddings_generator=EmbeddingsGeneratorEnum.OpenAI,
    )
    assert rule.embeddings_generator == EmbeddingsGeneratorEnum.OpenAI

    # Test invalid enum value
    with pytest.raises(ValidationError) as exc_info:
        EmbeddingsRuleModel(
            owner_guid="12345678-1234-5678-1234-567812345678",
            embeddings_generator="InvalidGenerator",
        )
    assert "embeddings_generator" in str(exc_info.value)


def test_optional_fields():
    """Test that optional fields can be None."""
    rule = EmbeddingsRuleModel(owner_guid="12345678-1234-5678-1234-567812345678")

    assert rule.tenant_guid is None
    assert rule.bucket_guid is None
    assert rule.name is None
    assert rule.prefix is None
    assert rule.suffix is None
    assert rule.graph_repository_guid is None
    assert rule.vector_repository_guid is None
    assert rule.retention_minutes is None
