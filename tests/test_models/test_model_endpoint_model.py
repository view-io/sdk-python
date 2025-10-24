import pytest
import uuid
from datetime import datetime, timezone
from view_sdk.models.model_endpoint_model import ModelEndpointModel
from view_sdk.enums.model_api_type_enum import ModelApiTypeEnum


def test_model_endpoint_model_defaults():
    """Test that ModelEndpointModel has correct default values."""
    model = ModelEndpointModel()

    # Test GUID generation
    assert model.guid is not None
    assert len(model.guid) == 36  # UUID length
    assert isinstance(uuid.UUID(model.guid), uuid.UUID)

    # Test tenant GUID generation
    assert model.tenant_guid is not None
    assert len(model.tenant_guid) == 36
    assert isinstance(uuid.UUID(model.tenant_guid), uuid.UUID)

    # Test default values
    assert model.name == "My model endpoint"
    assert model.endpoint_url == "http://localhost:11434/"
    assert model.bearer_token is None
    assert model.api_type == ModelApiTypeEnum.Ollama
    assert model.timeout_ms == 30000
    assert model.additional_data is None
    assert model.active is True

    # Test created_utc timestamp
    assert model.created_utc is not None
    assert isinstance(model.created_utc, datetime)
    assert model.created_utc.tzinfo == timezone.utc


def test_model_endpoint_model_custom_values():
    """Test ModelEndpointModel with custom values."""
    custom_guid = str(uuid.uuid4())
    custom_tenant_guid = str(uuid.uuid4())
    custom_created_utc = datetime.now(timezone.utc)

    model = ModelEndpointModel(
        guid=custom_guid,
        tenant_guid=custom_tenant_guid,
        name="Custom Endpoint",
        endpoint_url="https://api.openai.com/v1/",
        bearer_token="sk-test-token",
        api_type=ModelApiTypeEnum.OpenAi,
        timeout_ms=60000,
        additional_data="custom endpoint data",
        active=False,
        created_utc=custom_created_utc,
    )

    assert model.guid == custom_guid
    assert model.tenant_guid == custom_tenant_guid
    assert model.name == "Custom Endpoint"
    assert model.endpoint_url == "https://api.openai.com/v1/"
    assert model.bearer_token == "sk-test-token"
    assert model.api_type == ModelApiTypeEnum.OpenAi
    assert model.timeout_ms == 60000
    assert model.additional_data == "custom endpoint data"
    assert model.active is False
    assert model.created_utc == custom_created_utc


def test_model_endpoint_model_guid_uniqueness():
    """Test that each ModelEndpointModel instance gets a unique GUID."""
    model1 = ModelEndpointModel()
    model2 = ModelEndpointModel()
    assert model1.guid != model2.guid
    assert model1.tenant_guid != model2.tenant_guid


def test_model_endpoint_model_created_utc_timestamp():
    """Test that created_utc is set to current UTC time."""
    before_creation = datetime.now(timezone.utc)
    model = ModelEndpointModel()
    after_creation = datetime.now(timezone.utc)

    assert before_creation <= model.created_utc <= after_creation


def test_model_endpoint_model_api_type_enum():
    """Test that api_type accepts valid enum values."""
    # Test Ollama
    model = ModelEndpointModel(api_type=ModelApiTypeEnum.Ollama)
    assert model.api_type == ModelApiTypeEnum.Ollama

    # Test OpenAi
    model = ModelEndpointModel(api_type=ModelApiTypeEnum.OpenAi)
    assert model.api_type == ModelApiTypeEnum.OpenAi

    # Test string values (should work due to str enum)
    model = ModelEndpointModel(api_type="Ollama")
    assert model.api_type == ModelApiTypeEnum.Ollama

    model = ModelEndpointModel(api_type="OpenAi")
    assert model.api_type == ModelApiTypeEnum.OpenAi


def test_model_endpoint_model_timeout_validation():
    """Test timeout_ms field validation."""
    # Valid values
    model = ModelEndpointModel(timeout_ms=1001)
    assert model.timeout_ms == 1001

    model = ModelEndpointModel(timeout_ms=60000)
    assert model.timeout_ms == 60000

    # Invalid values
    with pytest.raises(ValueError, match="TimeoutMs must be greater than 1000"):
        ModelEndpointModel(timeout_ms=1000)

    with pytest.raises(ValueError, match="TimeoutMs must be greater than 1000"):
        ModelEndpointModel(timeout_ms=500)


def test_model_endpoint_model_alias_mapping():
    """Test that field aliases work correctly."""
    data = {
        "GUID": "test-guid",
        "TenantGUID": "test-tenant-guid",
        "Name": "Test Endpoint",
        "EndpointUrl": "https://test.example.com/",
        "BearerToken": "test-bearer-token",
        "ApiType": "OpenAi",
        "TimeoutMs": 45000,
        "AdditionalData": "test data",
        "Active": False,
        "CreatedUtc": datetime.now(timezone.utc),
    }

    model = ModelEndpointModel(**data)

    assert model.guid == "test-guid"
    assert model.tenant_guid == "test-tenant-guid"
    assert model.name == "Test Endpoint"
    assert model.endpoint_url == "https://test.example.com/"
    assert model.bearer_token == "test-bearer-token"
    assert model.api_type == ModelApiTypeEnum.OpenAi
    assert model.timeout_ms == 45000
    assert model.additional_data == "test data"
    assert model.active is False


def test_model_endpoint_model_serialization():
    """Test that the model can be serialized and deserialized."""
    model = ModelEndpointModel(
        name="Test Endpoint",
        endpoint_url="https://test.example.com/",
        bearer_token="test-token",
        api_type=ModelApiTypeEnum.OpenAi,
        additional_data="test data",
    )

    # Test serialization
    model_dict = model.model_dump()
    assert isinstance(model_dict, dict)
    assert model_dict["name"] == "Test Endpoint"
    assert model_dict["endpoint_url"] == "https://test.example.com/"
    assert model_dict["bearer_token"] == "test-token"
    assert model_dict["api_type"] == "OpenAi"
    assert model_dict["additional_data"] == "test data"

    # Test deserialization
    new_model = ModelEndpointModel(**model_dict)
    assert new_model.name == model.name
    assert new_model.endpoint_url == model.endpoint_url
    assert new_model.bearer_token == model.bearer_token
    assert new_model.api_type == model.api_type
    assert new_model.additional_data == model.additional_data


def test_model_endpoint_model_with_alias_serialization():
    """Test serialization with aliases."""
    model = ModelEndpointModel(
        name="Test Endpoint",
        endpoint_url="https://test.example.com/",
        api_type=ModelApiTypeEnum.OpenAi,
    )

    # Test serialization with aliases
    model_dict = model.model_dump(by_alias=True)
    assert "Name" in model_dict
    assert "EndpointUrl" in model_dict
    assert "ApiType" in model_dict
    assert model_dict["Name"] == "Test Endpoint"
    assert model_dict["EndpointUrl"] == "https://test.example.com/"
    assert model_dict["ApiType"] == "OpenAi"


def test_model_endpoint_model_optional_fields():
    """Test that optional fields work correctly."""
    # Test with None values
    model = ModelEndpointModel(bearer_token=None, additional_data=None)

    assert model.bearer_token is None
    assert model.additional_data is None

    # Test with empty string
    model = ModelEndpointModel(bearer_token="", additional_data="")

    assert model.bearer_token == ""
    assert model.additional_data == ""


def test_model_endpoint_model_boolean_fields():
    """Test boolean field handling."""
    # Test active field
    model = ModelEndpointModel(active=True)
    assert model.active is True

    model = ModelEndpointModel(active=False)
    assert model.active is False


def test_model_endpoint_model_url_handling():
    """Test various URL formats."""
    # Test URL without trailing slash
    model = ModelEndpointModel(endpoint_url="https://api.example.com")
    assert model.endpoint_url == "https://api.example.com"

    # Test URL with trailing slash
    model = ModelEndpointModel(endpoint_url="https://api.example.com/")
    assert model.endpoint_url == "https://api.example.com/"

    # Test localhost URL
    model = ModelEndpointModel(endpoint_url="http://localhost:8080")
    assert model.endpoint_url == "http://localhost:8080"

    # Test URL with path
    model = ModelEndpointModel(endpoint_url="https://api.example.com/v1/chat")
    assert model.endpoint_url == "https://api.example.com/v1/chat"


def test_model_endpoint_model_edge_cases():
    """Test edge cases and boundary conditions."""
    # Test with minimum timeout
    model = ModelEndpointModel(timeout_ms=1001)
    assert model.timeout_ms == 1001

    # Test with very long timeout
    model = ModelEndpointModel(timeout_ms=300000)  # 5 minutes
    assert model.timeout_ms == 300000

    # Test with empty name
    model = ModelEndpointModel(name="")
    assert model.name == ""

    # Test with very long name
    long_name = "A" * 1000
    model = ModelEndpointModel(name=long_name)
    assert model.name == long_name
