import pytest
from datetime import datetime, timezone
from view_sdk.models.webhook_event import WebhookEventModel
from view_sdk.enums.webhook_event_type_enum import WebhookEventTypeEnum


def test_create_webhook_event_with_minimal_required_fields():
    """Test creating a WebhookEvent with only required fields."""
    event = WebhookEventModel(url="http://example.com/webhook")

    # Check default values
    assert event.event_type == WebhookEventTypeEnum.Unknown
    assert event.content_length == 0
    assert event.timeout_ms == 60000
    assert event.content_type == "application/json"
    assert event.expect_status == 200
    assert event.retry_interval_ms == 10000
    assert event.attempt == 0
    assert event.max_attempts == 5
    assert event.http_status == 0

    # Check datetime fields
    assert event.last_attempt_utc is None
    assert event.next_attempt_utc is None
    assert event.last_failure_utc is None
    assert event.success_utc is None
    assert event.failed_utc is None


def test_create_webhook_event_with_all_fields():
    """Test creating a WebhookEvent with all fields."""
    current_time = datetime.now(timezone.utc)

    data = {
        "guid": "550e8400-e29b-41d4-a716-446655440000",
        "tenant_guid": "550e8400-e29b-41d4-a716-446655440001",
        "target_guid": "550e8400-e29b-41d4-a716-446655440002",
        "rule_guid": "550e8400-e29b-41d4-a716-446655440003",
        "event_type": WebhookEventTypeEnum.ObjectWrite,
        "content_length": 1024,
        "timeout_ms": 30000,
        "url": "http://example.com/webhook",
        "content_type": "application/xml",
        "expect_status": 201,
        "retry_interval_ms": 5000,
        "attempt": 2,
        "max_attempts": 10,
        "http_status": 503,
        "created_utc": current_time,
        "added_utc": current_time,
        "last_attempt_utc": current_time,
        "next_attempt_utc": current_time,
        "last_failure_utc": current_time,
        "success_utc": None,
        "failed_utc": None,
    }

    event = WebhookEventModel(**data)

    assert event.guid == data["guid"]
    assert event.tenant_guid == data["tenant_guid"]
    assert event.target_guid == data["target_guid"]
    assert event.rule_guid == data["rule_guid"]
    assert event.event_type == data["event_type"]
    assert event.content_length == data["content_length"]
    assert event.timeout_ms == data["timeout_ms"]
    assert event.url.unicode_string() == data["url"]
    assert event.content_type == data["content_type"]
    assert event.expect_status == data["expect_status"]
    assert event.retry_interval_ms == data["retry_interval_ms"]
    assert event.attempt == data["attempt"]
    assert event.max_attempts == data["max_attempts"]
    assert event.http_status == data["http_status"]
    assert event.created_utc == data["created_utc"]
    assert event.added_utc == data["added_utc"]
    assert event.last_attempt_utc == data["last_attempt_utc"]
    assert event.next_attempt_utc == data["next_attempt_utc"]
    assert event.last_failure_utc == data["last_failure_utc"]
    assert event.success_utc == data["success_utc"]
    assert event.failed_utc == data["failed_utc"]


@pytest.mark.parametrize("event_type", list(WebhookEventTypeEnum))
def test_valid_event_types(event_type):
    """Test that all enum values for event_type are accepted."""
    event = WebhookEventModel(url="http://example.com/webhook", event_type=event_type)
    assert event.event_type == event_type


def test_model_json_serialization():
    """Test that the model can be properly serialized to JSON with aliases."""
    event = WebhookEventModel(
        event_type=WebhookEventTypeEnum.ObjectWrite,
        content_length=1024,
        Url="http://example.com/webhook",
    )

    json_data = event.model_dump(by_alias=True)
    assert isinstance(json_data["GUID"], str)
    assert json_data["EventType"] == "ObjectWrite"
    assert json_data["ContentLength"] == 1024
    assert json_data["ContentType"] == "application/json"


def test_model_json_deserialization():
    """Test that the model can be properly deserialized from JSON with aliases."""
    json_data = {
        "GUID": "550e8400-e29b-41d4-a716-446655440000",
        "TenantGUID": "550e8400-e29b-41d4-a716-446655440001",
        "TargetGUID": "550e8400-e29b-41d4-a716-446655440002",
        "RuleGUID": "550e8400-e29b-41d4-a716-446655440003",
        "EventType": "ObjectWrite",
        "ContentType": "application/json",
        "ContentLength": 1024,
        "TimeoutMs": 30000,
        "Url": "http://example.com/webhook",
    }

    event = WebhookEventModel.model_validate(json_data)

    assert event.guid == json_data["GUID"]
    assert event.tenant_guid == json_data["TenantGUID"]
    assert event.target_guid == json_data["TargetGUID"]
    assert event.rule_guid == json_data["RuleGUID"]
    assert event.event_type == WebhookEventTypeEnum.ObjectWrite
    assert event.content_type == json_data["ContentType"]
    assert event.content_length == json_data["ContentLength"]
    assert event.timeout_ms == json_data["TimeoutMs"]
    assert event.url.unicode_string() == json_data["Url"]
