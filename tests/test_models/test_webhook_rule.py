import pytest
from datetime import datetime, timezone
from view_sdk.models.webhook_rule import WebhookRuleModel
from view_sdk.enums.webhook_event_type_enum import WebhookEventTypeEnum


def test_create_webhook_rule_with_minimal_required_fields():
    """Test creating a WebhookRule with only required fields."""
    rule = WebhookRuleModel(name="Test Rule")

    assert rule.name == "Test Rule"

    assert rule.event_type == WebhookEventTypeEnum.Unknown
    assert rule.max_attempts == 10
    assert rule.retry_interval_ms == 30000  # 30 seconds
    assert rule.timeout_ms == 60000  # 1 minute

    assert rule.created_utc is not None  # Ensure timezone awareness


def test_create_webhook_rule_with_all_fields():
    """Test creating a WebhookRule with all fields."""
    current_time = datetime.now(timezone.utc)

    data = {
        "guid": "550e8400-e29b-41d4-a716-446655440000",
        "tenant_guid": "550e8400-e29b-41d4-a716-446655440001",
        "target_guid": "550e8400-e29b-41d4-a716-446655440002",
        "name": "Complete Test Rule",
        "event_type": WebhookEventTypeEnum.ObjectWrite,
        "max_attempts": 5,
        "retry_interval_ms": 15000,
        "timeout_ms": 45000,
        "created_utc": current_time,
    }

    rule = WebhookRuleModel(**data)

    for key, value in data.items():
        assert getattr(rule, key) == value


@pytest.mark.parametrize("event_type", list(WebhookEventTypeEnum))
def test_valid_event_types(event_type):
    """Test that all enum values for event_type are accepted."""
    rule = WebhookRuleModel(name="Test Rule", event_type=event_type)
    assert rule.event_type == event_type


@pytest.mark.parametrize("name", [None, "", "   ", "\t", "\n"])
def test_invalid_names(name):
    """Test that invalid names raise validation errors."""
    with pytest.raises(ValueError, match="Name must not be empty"):
        WebhookRuleModel(name=name)


@pytest.mark.parametrize(
    "field,value,expected_error",
    [
        ("max_attempts", -1, "Input should be greater than or equal to 0"),
        ("retry_interval_ms", 0, "Input should be greater than or equal to 1"),
        ("timeout_ms", 0, "Input should be greater than or equal to 1"),
    ],
)
def test_invalid_numeric_values(field, value, expected_error):
    """Test that invalid numeric values raise appropriate validation errors."""
    data = {"name": "Test Rule"}
    data[field] = value

    with pytest.raises(ValueError, match=expected_error):
        WebhookRuleModel(**data)


def test_model_json_serialization():
    """Test that the model can be properly serialized to JSON with aliases."""
    rule = WebhookRuleModel(
        name="Test Rule", event_type=WebhookEventTypeEnum.ObjectWrite, max_attempts=5
    )

    json_data = rule.model_dump(by_alias=True)

    assert json_data["Name"] == "Test Rule"
    assert json_data["EventType"] == "ObjectWrite"
    assert json_data["MaxAttempts"] == 5
    assert json_data["RetryIntervalMs"] == 30000
    assert json_data["TimeoutMs"] == 60000


def test_model_json_deserialization():
    """Test that the model can be properly deserialized from JSON with aliases."""
    json_data = {
        "GUID": "550e8400-e29b-41d4-a716-446655440000",
        "TenantGUID": "550e8400-e29b-41d4-a716-446655440001",
        "TargetGUID": "550e8400-e29b-41d4-a716-446655440002",
        "Name": "Test Rule",
        "EventType": "ObjectWrite",
        "MaxAttempts": 5,
        "RetryIntervalMs": 15000,
        "TimeoutMs": 45000,
    }

    rule = WebhookRuleModel.model_validate(json_data)

    assert rule.guid == json_data["GUID"]
    assert rule.tenant_guid == json_data["TenantGUID"]
    assert rule.target_guid == json_data["TargetGUID"]
    assert rule.name == json_data["Name"]
    assert rule.event_type == WebhookEventTypeEnum.ObjectWrite
    assert rule.max_attempts == json_data["MaxAttempts"]
    assert rule.retry_interval_ms == json_data["RetryIntervalMs"]
    assert rule.timeout_ms == json_data["TimeoutMs"]


def test_created_utc_auto_generation():
    """Test that created_utc is automatically generated with timezone."""
    before = datetime.now(timezone.utc)
    rule = WebhookRuleModel(name="Test Rule")
    after = datetime.now(timezone.utc)

    assert before <= rule.created_utc <= after
    assert rule.created_utc.tzinfo is not None


@pytest.mark.parametrize(
    "name",
    [
        "Test Rule",
        "My Webhook Rule",
        "Rule 123",
        "A" * 100,  # Test long name
    ],
)
def test_valid_names(name):
    """Test that various valid names are accepted."""
    rule = WebhookRuleModel(name=name)
    assert rule.name == name
