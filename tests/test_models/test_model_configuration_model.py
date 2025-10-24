import pytest
import uuid
from datetime import datetime, timezone
from view_sdk.models.model_configuration_model import ModelConfigurationModel


def test_model_configuration_model_defaults():
    """Test that ModelConfigurationModel has correct default values."""
    model = ModelConfigurationModel()

    # Test GUID generation
    assert model.guid is not None
    assert len(model.guid) == 36  # UUID length
    assert isinstance(uuid.UUID(model.guid), uuid.UUID)

    # Test tenant GUID generation
    assert model.tenant_guid is not None
    assert len(model.tenant_guid) == 36
    assert isinstance(uuid.UUID(model.tenant_guid), uuid.UUID)

    # Test default values
    assert model.model_name == "owner/modelname"
    assert model.embeddings is True
    assert model.completions is True
    assert model.context_size == 4096
    assert model.max_output_tokens == 4096
    assert model.temperature == 0.2
    assert model.top_p == 1.0
    assert model.top_k == 40
    assert model.frequency_penalty == 0.0
    assert model.presence_penalty == 0.0
    assert model.enable_streaming is True
    assert model.timeout_ms == 30000
    assert model.additional_data is None
    assert model.active is True

    # Test created_utc timestamp
    assert model.created_utc is not None
    assert isinstance(model.created_utc, datetime)
    assert model.created_utc.tzinfo == timezone.utc


def test_model_configuration_model_custom_values():
    """Test ModelConfigurationModel with custom values."""
    custom_guid = str(uuid.uuid4())
    custom_tenant_guid = str(uuid.uuid4())
    custom_created_utc = datetime.now(timezone.utc)

    model = ModelConfigurationModel(
        guid=custom_guid,
        tenant_guid=custom_tenant_guid,
        model_name="custom/model",
        embeddings=False,
        completions=False,
        context_size=8192,
        max_output_tokens=2048,
        temperature=0.7,
        top_p=0.9,
        top_k=50,
        frequency_penalty=0.5,
        presence_penalty=0.3,
        enable_streaming=False,
        timeout_ms=60000,
        additional_data="custom data",
        active=False,
        created_utc=custom_created_utc,
    )

    assert model.guid == custom_guid
    assert model.tenant_guid == custom_tenant_guid
    assert model.model_name == "custom/model"
    assert model.embeddings is False
    assert model.completions is False
    assert model.context_size == 8192
    assert model.max_output_tokens == 2048
    assert model.temperature == 0.7
    assert model.top_p == 0.9
    assert model.top_k == 50
    assert model.frequency_penalty == 0.5
    assert model.presence_penalty == 0.3
    assert model.enable_streaming is False
    assert model.timeout_ms == 60000
    assert model.additional_data == "custom data"
    assert model.active is False
    assert model.created_utc == custom_created_utc


def test_model_configuration_model_guid_uniqueness():
    """Test that each ModelConfigurationModel instance gets a unique GUID."""
    model1 = ModelConfigurationModel()
    model2 = ModelConfigurationModel()
    assert model1.guid != model2.guid
    assert model1.tenant_guid != model2.tenant_guid


def test_model_configuration_model_created_utc_timestamp():
    """Test that created_utc is set to current UTC time."""
    before_creation = datetime.now(timezone.utc)
    model = ModelConfigurationModel()
    after_creation = datetime.now(timezone.utc)

    assert before_creation <= model.created_utc <= after_creation


def test_model_configuration_model_context_size_validation():
    """Test context_size field validation."""
    # Valid values
    model = ModelConfigurationModel(context_size=1)
    assert model.context_size == 1

    model = ModelConfigurationModel(context_size=1000000)
    assert model.context_size == 1000000

    # Invalid values
    with pytest.raises(ValueError, match="ContextSize must be >= 1"):
        ModelConfigurationModel(context_size=0)

    with pytest.raises(ValueError, match="ContextSize must be >= 1"):
        ModelConfigurationModel(context_size=-1)


def test_model_configuration_model_max_output_tokens_validation():
    """Test max_output_tokens field validation."""
    # Valid values
    model = ModelConfigurationModel(max_output_tokens=1)
    assert model.max_output_tokens == 1

    model = ModelConfigurationModel(max_output_tokens=2_000_000)
    assert model.max_output_tokens == 2_000_000

    # Invalid values
    with pytest.raises(
        ValueError, match="MaxOutputTokens must be between 1 and 2,000,000"
    ):
        ModelConfigurationModel(max_output_tokens=0)

    with pytest.raises(
        ValueError, match="MaxOutputTokens must be between 1 and 2,000,000"
    ):
        ModelConfigurationModel(max_output_tokens=2_000_001)


def test_model_configuration_model_temperature_validation():
    """Test temperature field validation."""
    # Valid values
    model = ModelConfigurationModel(temperature=0.0)
    assert model.temperature == 0.0

    model = ModelConfigurationModel(temperature=2.0)
    assert model.temperature == 2.0

    model = ModelConfigurationModel(temperature=1.5)
    assert model.temperature == 1.5

    # Invalid values
    with pytest.raises(ValueError, match="Temperature must be between 0.0 and 2.0"):
        ModelConfigurationModel(temperature=-0.1)

    with pytest.raises(ValueError, match="Temperature must be between 0.0 and 2.0"):
        ModelConfigurationModel(temperature=2.1)


def test_model_configuration_model_top_p_validation():
    """Test top_p field validation."""
    # Valid values
    model = ModelConfigurationModel(top_p=0.0)
    assert model.top_p == 0.0

    model = ModelConfigurationModel(top_p=1.0)
    assert model.top_p == 1.0

    model = ModelConfigurationModel(top_p=0.5)
    assert model.top_p == 0.5

    # Invalid values
    with pytest.raises(ValueError, match="TopP must be between 0.0 and 1.0"):
        ModelConfigurationModel(top_p=-0.1)

    with pytest.raises(ValueError, match="TopP must be between 0.0 and 1.0"):
        ModelConfigurationModel(top_p=1.1)


def test_model_configuration_model_top_k_validation():
    """Test top_k field validation."""
    # Valid values
    model = ModelConfigurationModel(top_k=1)
    assert model.top_k == 1

    model = ModelConfigurationModel(top_k=100)
    assert model.top_k == 100

    model = ModelConfigurationModel(top_k=50)
    assert model.top_k == 50

    # Invalid values
    with pytest.raises(ValueError, match="TopK must be between 1 and 100"):
        ModelConfigurationModel(top_k=0)

    with pytest.raises(ValueError, match="TopK must be between 1 and 100"):
        ModelConfigurationModel(top_k=101)


def test_model_configuration_model_penalty_validation():
    """Test frequency_penalty and presence_penalty field validation."""
    # Valid values
    model = ModelConfigurationModel(frequency_penalty=-2.0, presence_penalty=-2.0)
    assert model.frequency_penalty == -2.0
    assert model.presence_penalty == -2.0

    model = ModelConfigurationModel(frequency_penalty=2.0, presence_penalty=2.0)
    assert model.frequency_penalty == 2.0
    assert model.presence_penalty == 2.0

    model = ModelConfigurationModel(frequency_penalty=0.5, presence_penalty=-0.5)
    assert model.frequency_penalty == 0.5
    assert model.presence_penalty == -0.5

    # Invalid values
    with pytest.raises(ValueError, match="Penalty values must be between -2.0 and 2.0"):
        ModelConfigurationModel(frequency_penalty=-2.1)

    with pytest.raises(ValueError, match="Penalty values must be between -2.0 and 2.0"):
        ModelConfigurationModel(presence_penalty=2.1)


def test_model_configuration_model_timeout_validation():
    """Test timeout_ms field validation."""
    # Valid values
    model = ModelConfigurationModel(timeout_ms=1001)
    assert model.timeout_ms == 1001

    model = ModelConfigurationModel(timeout_ms=60000)
    assert model.timeout_ms == 60000

    # Invalid values
    with pytest.raises(ValueError, match="TimeoutMs must be greater than 1000"):
        ModelConfigurationModel(timeout_ms=1000)

    with pytest.raises(ValueError, match="TimeoutMs must be greater than 1000"):
        ModelConfigurationModel(timeout_ms=500)


def test_model_configuration_model_alias_mapping():
    """Test that field aliases work correctly."""
    data = {
        "GUID": "test-guid",
        "TenantGUID": "test-tenant-guid",
        "ModelName": "test/model",
        "Embeddings": False,
        "Completions": False,
        "ContextSize": 2048,
        "MaxOutputTokens": 1024,
        "Temperature": 0.8,
        "TopP": 0.9,
        "TopK": 30,
        "FrequencyPenalty": 0.1,
        "PresencePenalty": 0.2,
        "EnableStreaming": False,
        "TimeoutMs": 45000,
        "AdditionalData": "test data",
        "Active": False,
        "CreatedUtc": datetime.now(timezone.utc),
    }

    model = ModelConfigurationModel(**data)

    assert model.guid == "test-guid"
    assert model.tenant_guid == "test-tenant-guid"
    assert model.model_name == "test/model"
    assert model.embeddings is False
    assert model.completions is False
    assert model.context_size == 2048
    assert model.max_output_tokens == 1024
    assert model.temperature == 0.8
    assert model.top_p == 0.9
    assert model.top_k == 30
    assert model.frequency_penalty == 0.1
    assert model.presence_penalty == 0.2
    assert model.enable_streaming is False
    assert model.timeout_ms == 45000
    assert model.additional_data == "test data"
    assert model.active is False


def test_model_configuration_model_serialization():
    """Test that the model can be serialized and deserialized."""
    model = ModelConfigurationModel(
        model_name="test/model", temperature=0.5, top_p=0.8, additional_data="test data"
    )

    # Test serialization
    model_dict = model.model_dump()
    assert isinstance(model_dict, dict)
    assert model_dict["model_name"] == "test/model"
    assert model_dict["temperature"] == 0.5
    assert model_dict["top_p"] == 0.8
    assert model_dict["additional_data"] == "test data"

    # Test deserialization
    new_model = ModelConfigurationModel(**model_dict)
    assert new_model.model_name == model.model_name
    assert new_model.temperature == model.temperature
    assert new_model.top_p == model.top_p
    assert new_model.additional_data == model.additional_data


def test_model_configuration_model_with_alias_serialization():
    """Test serialization with aliases."""
    model = ModelConfigurationModel(model_name="test/model", temperature=0.5)

    # Test serialization with aliases
    model_dict = model.model_dump(by_alias=True)
    assert "ModelName" in model_dict
    assert "Temperature" in model_dict
    assert model_dict["ModelName"] == "test/model"
    assert model_dict["Temperature"] == 0.5
