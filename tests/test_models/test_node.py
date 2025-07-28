import pytest
from datetime import datetime
from pydantic import ValidationError
from view_sdk.models.node import NodeModel


@pytest.fixture
def valid_node_data():
    return {
        "Id": 1,
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "Name": "Test Node",
        "Hostname": "localhost",
        "InstanceType": "StorageServer",
        "LastStartUtc": "2023-09-12T12:34:56.789Z",
        "CreatedUtc": "2023-09-12T12:34:56.789Z",
    }


def test_valid_node_creation(valid_node_data):
    node = NodeModel(**valid_node_data)
    assert str(node.guid) == "123e4567-e89b-12d3-a456-426614174000"
    assert node.name == "Test Node"
    assert node.hostname == "localhost"
    assert node.instance_type == "StorageServer"
    assert isinstance(node.last_start_utc, datetime)
    assert isinstance(node.created_utc, datetime)


def test_datetime_validation():
    """Test validation of datetime fields"""
    try:
        NodeModel(Hostname="localhost", LastStartUtc="invalid-date")
        pytest.fail("Expected ValidationError for invalid date")
    except ValidationError as e:
        assert "Input should be a valid datetime" in str(e)


def test_model_dump(valid_node_data):
    """Test model serialization"""
    node = NodeModel(**valid_node_data)
    dumped = node.model_dump(mode="json")

    # Check for both included and excluded fields
    assert "id" not in dumped  # Should be excluded
    assert "guid" in dumped
    assert "hostname" in dumped
    assert "instance_type" in dumped
    assert dumped["instance_type"] == "StorageServer"


def test_model_aliases():
    """Test that field aliases are working correctly"""
    test_data = {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "Name": "Test Node",
        "Hostname": "localhost",
        "InstanceType": "StorageServer",
        "LastStartUtc": "2023-09-12T12:34:56.789Z",
        "CreatedUtc": "2023-09-12T12:34:56.789Z",
    }

    # Test with aliased field names
    node = NodeModel(**test_data)
    assert str(node.guid) == "123e4567-e89b-12d3-a456-426614174000"
    assert node.name == "Test Node"
    assert node.hostname == "localhost"
    assert node.instance_type == "StorageServer"

    # Test with non-aliased field names
    node = NodeModel(
        hostname="localhost",
        guid="123e4567-e89b-12d3-a456-426614174000",
        name="Test Node",
        instance_type="StorageServer",
    )
    assert str(node.guid) == "123e4567-e89b-12d3-a456-426614174000"
    assert node.name == "Test Node"
    assert node.hostname == "localhost"
    assert node.instance_type == "StorageServer"


def test_optional_fields():
    """Test optional fields behavior"""
    # Test minimal required fields
    node = NodeModel(Hostname="localhost")
    assert node.name is None

    # Test with explicit None
    node = NodeModel(Hostname="localhost", Name=None)
    assert node.name is None

    # Test with empty string
    node = NodeModel(Hostname="localhost", Name="")
    assert node.name == ""
