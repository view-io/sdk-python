import pytest
from datetime import datetime, timezone
from pydantic import ValidationError
from view_sdk.models.graph_repository import GraphRepositoryModel
from view_sdk.enums.graph_repository_type_enum import GraphRepositoryTypeEnum

def test_graph_repository_minimal_creation():
    """Test creating a GraphRepository with minimal required fields."""
    repo = GraphRepositoryModel(
        tenant_guid="12345678-1234-5678-1234-567812345678"
    )

    # Check default values
    assert repo.name == "My vector repository"
    assert repo.repository_type == GraphRepositoryTypeEnum.LiteGraph
    assert repo.endpoint_url is None
    assert repo.api_key is None
    assert repo.username is None
    assert repo.password is None
    assert repo.hostname is None
    assert repo.port == 0
    assert repo.graph_identifier is None
    assert isinstance(repo.created_utc, datetime)

def test_graph_repository_full_creation():
    """Test creating a GraphRepository with all fields."""
    data = {
        "GUID": "12345678-1234-5678-1234-567812345678",
        "TenantGUID": "98765432-1234-5678-1234-567812345678",
        "Name": "Test Graph Repository",
        "RepositoryType": "LiteGraph",
        "EndpointUrl": "http://localhost:8080",
        "ApiKey": "test-api-key",
        "Username": "testuser",
        "Password": "testpass",
        "Hostname": "localhost",
        "Port": 8080,
        "GraphIdentifier": "test-graph",
        "CreatedUtc": datetime.now(timezone.utc)
    }

    repo = GraphRepositoryModel(**data)
    assert repo.name == "Test Graph Repository"
    assert repo.repository_type == GraphRepositoryTypeEnum.LiteGraph
    assert repo.endpoint_url == "http://localhost:8080"
    assert repo.api_key == "test-api-key"
    assert repo.username == "testuser"
    assert repo.password == "testpass"
    assert repo.hostname == "localhost"
    assert repo.port == 8080
    assert repo.graph_identifier == "test-graph"

def test_invalid_port_range():
    """Test validation of port number range."""
    # Test port below range
    with pytest.raises(ValidationError) as exc_info:
        GraphRepositoryModel(
            tenant_guid="12345678-1234-5678-1234-567812345678",
            port=-1
        )
    assert "port" in str(exc_info.value)
    assert "greater than or equal to 0" in str(exc_info.value)

    # Test port above range
    with pytest.raises(ValidationError) as exc_info:
        GraphRepositoryModel(
            tenant_guid="12345678-1234-5678-1234-567812345678",
            port=65536
        )
    assert "port" in str(exc_info.value)
    assert "less than or equal to 65535" in str(exc_info.value)

def test_repository_type_enum():
    """Test validation of repository type enum."""
    # Test valid enum value
    repo = GraphRepositoryModel(
        tenant_guid="12345678-1234-5678-1234-567812345678",
        repository_type=GraphRepositoryTypeEnum.LiteGraph
    )
    assert repo.repository_type == GraphRepositoryTypeEnum.LiteGraph

    # Test invalid enum value
    with pytest.raises(ValidationError) as exc_info:
        GraphRepositoryModel(
            tenant_guid="12345678-1234-5678-1234-567812345678",
            repository_type="InvalidType"
        )
    assert "repository_type" in str(exc_info.value)

def test_optional_fields():
    """Test that optional fields can be None."""
    repo = GraphRepositoryModel(
        tenant_guid="12345678-1234-5678-1234-567812345678"
    )

    assert repo.endpoint_url is None
    assert repo.api_key is None
    assert repo.username is None
    assert repo.password is None
    assert repo.hostname is None
    assert repo.graph_identifier is None

def test_alias_mapping():
    """Test that field aliases are working correctly."""
    data = {
        "TenantGUID": "12345678-1234-5678-1234-567812345678",
        "Name": "Test Repository",
        "RepositoryType": "LiteGraph",
        "EndpointUrl": "http://localhost:8080",
        "Port": 8080
    }

    repo = GraphRepositoryModel(**data)
    assert repo.tenant_guid == "12345678-1234-5678-1234-567812345678"
    assert repo.name == "Test Repository"
    assert repo.repository_type == GraphRepositoryTypeEnum.LiteGraph
    assert repo.endpoint_url == "http://localhost:8080"
    assert repo.port == 8080

def test_default_name():
    """Test that default name is set correctly."""
    repo = GraphRepositoryModel(
        tenant_guid="12345678-1234-5678-1234-567812345678"
    )
    assert repo.name == "My vector repository"

def test_created_utc_auto_generation():
    """Test that created_utc is automatically generated."""
    repo = GraphRepositoryModel(
        tenant_guid="12345678-1234-5678-1234-567812345678"
    )
    assert isinstance(repo.created_utc, datetime)
    assert repo.created_utc.tzinfo == timezone.utc

def test_custom_created_utc():
    """Test setting custom created_utc."""
    custom_date = datetime(2024, 1, 1, tzinfo=timezone.utc)
    repo = GraphRepositoryModel(
        tenant_guid="12345678-1234-5678-1234-567812345678",
        created_utc=custom_date
    )
    assert repo.created_utc == custom_date

def test_populate_by_name():
    """Test that both alias and original field names work."""
    # Test with original field names
    repo1 = GraphRepositoryModel(
        tenant_guid="12345678-1234-5678-1234-567812345678",
        name="Test Repo 1"
    )
    assert repo1.name == "Test Repo 1"

    # Test with alias field names
    repo2 = GraphRepositoryModel(
        TenantGUID="12345678-1234-5678-1234-567812345678",
        Name="Test Repo 2"
    )
    assert repo2.name == "Test Repo 2"
