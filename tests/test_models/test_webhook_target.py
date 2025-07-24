import pytest
from datetime import datetime, timezone
from pydantic import ValidationError
from view_sdk.models.webhook_target import WebhookTargetModel

def test_create_webhook_target_with_minimal_required_fields():
    """Test creating a WebhookTarget with only required fields."""
    target = WebhookTargetModel(Url="http://example.com/webhook")

    # Check required and default values
    assert target.url.unicode_string() == "http://example.com/webhook"
    assert target.name == "My webhook target"
    assert target.content_type == "application/json"
    assert target.expect_status == 200

    # Check datetime field
    assert target.created_utc.tzinfo == timezone.utc

@pytest.mark.parametrize("url", [
    None,
    "",
    "   ",
    "\t",
    "\n"
])
def test_invalid_urls(url):
    """Test that invalid URLs raise validation errors."""
    with pytest.raises((ValueError, ValidationError)) as exc_info:
        WebhookTargetModel(Url=url)

    error_msg = str(exc_info.value)
    assert "Input should be a valid URL" in error_msg or "URL input should be a string" in error_msg

@pytest.mark.parametrize("content_type", [
    None,
    "",
    "   ",
    "\t",
    "\n"
])
def test_invalid_content_types(content_type):
    """Test that invalid content types raise validation errors."""
    with pytest.raises((ValueError, ValidationError)) as exc_info:
        WebhookTargetModel(
            Url="http://example.com/webhook",
            ContentType=content_type,

        )
    error_msg = str(exc_info.value)

    assert "Content type must not be empty" in error_msg or "Input should be a valid string" in error_msg


@pytest.mark.parametrize("expect_status,expected_error", [
    (99, "greater than or equal to 100"),
    (600, "less than or equal to 599"),
    (-1, "greater than or equal to 100"),
])
def test_invalid_expect_status(expect_status, expected_error):
    """Test that invalid expect_status values raise appropriate validation errors."""
    with pytest.raises(ValidationError) as exc_info:
        WebhookTargetModel(
            Url="http://example.com/webhook",
            ExpectStatus=expect_status
        )
    assert expected_error in str(exc_info.value).lower()

def test_model_json_serialization():
    """Test that the model can be properly serialized to JSON with aliases."""
    target = WebhookTargetModel(
        Name="Test Webhook",
        Url="http://example.com/webhook",
        ContentType="application/xml",
        ExpectStatus=201
    )

    json_data = target.model_dump(by_alias=True)

    assert json_data["Name"] == "Test Webhook"
    assert json_data["Url"].unicode_string() == "http://example.com/webhook"
    assert json_data["ContentType"] == "application/xml"
    assert json_data["ExpectStatus"] == 201

@pytest.mark.parametrize("url", [
    "http://example.com/webhook",
    "https://api.example.com/webhook",
    "http://localhost:8080/webhook",
    "https://custom-domain.com/path/to/webhook",
])
def test_valid_urls(url):
    """Test that various valid URL formats are accepted."""
    target = WebhookTargetModel(Url=url)
    assert target.url.unicode_string() == url

@pytest.mark.parametrize("content_type", [
    "application/json",
    "application/xml",
    "text/plain",
    "application/x-www-form-urlencoded",
])
def test_valid_content_types(content_type):
    """Test that various valid content types are accepted."""
    target = WebhookTargetModel(
        Url="http://example.com/webhook",
        ContentType=content_type
    )
    assert target.content_type == content_type

def test_model_defaults_and_generated_fields():
    """Test that default values and auto-generated fields work correctly."""
    target = WebhookTargetModel(Url="http://example.com/webhook")


    # Check default values
    assert target.name == "My webhook target"
    assert target.content_type == "application/json"
    assert target.expect_status == 200

    # Check that created_utc is a timezone-aware datetime
    assert isinstance(target.created_utc, datetime)
    assert target.created_utc.tzinfo == timezone.utc

def test_alias_field_access():
    """Test that fields can be accessed and set using aliases"""
    target = WebhookTargetModel(
        GUID="custom-guid",
        TenantGUID="custom-tenant-guid",
        Url="http://example.com/webhook",
        Name="Custom Name",
        ContentType="text/plain",
        ExpectStatus=201
    )

    # Check access using Python names
    assert target.guid == "custom-guid"
    assert target.tenant_guid == "custom-tenant-guid"
    assert target.name == "Custom Name"
    assert target.content_type == "text/plain"
    assert target.expect_status == 201

    # Check serialization uses aliases
    json_data = target.model_dump(by_alias=True)
    assert json_data["GUID"] == "custom-guid"
    assert json_data["TenantGUID"] == "custom-tenant-guid"
    assert json_data["Name"] == "Custom Name"
    assert json_data["ContentType"] == "text/plain"
    assert json_data["ExpectStatus"] == 201
