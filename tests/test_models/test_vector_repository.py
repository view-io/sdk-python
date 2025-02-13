import pytest
from datetime import datetime, timezone
from pydantic import ValidationError
from view_sdk.models.vector_repository import VectorRepositoryModel
from view_sdk.enums.vector_repository_type_enum import VectorRepositoryTypeEnum


def test_create_complete_vector_repository():
    """Test creating a vector repository with all fields populated."""
    data = {
        "guid": "123e4567-e89b-12d3-a456-426614174000",
        "tenant_guid": "987fcdeb-51d3-a456-426614174000",
        "name": "Test Vector DB",
        "repository_type": "Oracle23AI",
        "endpoint_url": "https://vector.example.com",
        "api_key": "sk-1234567890",
        "model": "custom-model",
        "dimensionality": 768,
        "database_hostname": "db.example.com",
        "database_name": "vectordb",
        "database_table": "embeddings",
        "database_port": 5432,
        "database_user": "admin",
        "database_password": "secret",
        "prompt_prefix": "Custom prefix:",
        "prompt_suffix": "Custom suffix:",
        "created_utc": "2024-01-01T00:00:00Z"
    }
    
    repo = VectorRepositoryModel(**data)
    assert repo.guid == data["guid"]
    assert repo.tenant_guid == data["tenant_guid"]
    assert repo.name == data["name"]
    assert repo.repository_type == VectorRepositoryTypeEnum.Oracle23AI
    assert repo.endpoint_url == data["endpoint_url"]
    assert repo.api_key == data["api_key"]
    assert repo.model == data["model"]
    assert repo.dimensionality == data["dimensionality"]
    assert repo.database_hostname == data["database_hostname"]
    assert repo.database_name == data["database_name"]
    assert repo.database_table == data["database_table"]
    assert repo.database_port == data["database_port"]
    assert repo.database_user == data["database_user"]
    assert repo.database_password == data["database_password"]
    assert repo.prompt_prefix == data["prompt_prefix"]
    assert repo.prompt_suffix == data["prompt_suffix"]

def test_repository_type_validation():
    """Test validation of repository type enum."""
    # Test all valid repository types
    for repo_type in VectorRepositoryTypeEnum:
        repo = VectorRepositoryModel(repository_type=repo_type)
        assert repo.repository_type == repo_type

    # Test invalid repository type
    with pytest.raises(ValidationError) as exc_info:
        VectorRepositoryModel(repository_type="InvalidType")
    assert "type=enum" in str(exc_info.value)

def test_dimensionality_validation():
    """Test validation of dimensionality field."""
    # Test valid dimensionality
    repo = VectorRepositoryModel(dimensionality=512)
    assert repo.dimensionality == 512

    # Test invalid dimensionality (less than 1)
    with pytest.raises(ValidationError) as exc_info:
        VectorRepositoryModel(dimensionality=0)
    assert "greater than or equal to 1" in str(exc_info.value)

    # Test invalid type
    with pytest.raises(ValidationError):
        VectorRepositoryModel(dimensionality="invalid")

def test_database_port_validation():
    """Test validation of database port field."""
    # Test valid ports
    valid_ports = [0, 1, 1024, 3306, 5432, 65535]
    for port in valid_ports:
        repo = VectorRepositoryModel(database_port=port)
        assert repo.database_port == port

    # Test invalid port (greater than 65535)
    with pytest.raises(ValidationError) as exc_info:
        VectorRepositoryModel(database_port=65536)
    assert "less than or equal to 65535" in str(exc_info.value)

    # Test invalid port (less than 0)
    with pytest.raises(ValidationError) as exc_info:
        VectorRepositoryModel(database_port=-1)
    assert "greater than or equal to 0" in str(exc_info.value)

def test_endpoint_url_validation():
    """Test validation of endpoint URL field."""
    # Test valid URLs
    valid_urls = [
        "https://vector.example.com",
        "http://localhost:8080",
        None  # None should be valid as it's optional
    ]
    for url in valid_urls:
        repo = VectorRepositoryModel(endpoint_url=url)
        assert repo.endpoint_url == url

def test_created_utc_validation():
    """Test validation of created_utc field."""
    # Test with valid datetime string
    repo = VectorRepositoryModel(created_utc="2024-01-01T00:00:00Z")
    assert isinstance(repo.created_utc, datetime)

    # Test with datetime object
    now = datetime.now(timezone.utc)
    repo = VectorRepositoryModel(created_utc=now)
    assert repo.created_utc == now

    # Test with invalid datetime
    with pytest.raises(ValidationError) as exc_info:
        VectorRepositoryModel(created_utc="invalid-date")
    assert "type=datetime" in str(exc_info.value)

def test_model_export():
    """Test that the model correctly exports data with aliases."""
    data = {
        "name": "Test Repo",
        "repository_type": "Pgvector",
        "model": "custom-model",
        "dimensionality": 512
    }
    
    repo = VectorRepositoryModel(**data)
    exported = repo.model_dump(by_alias=True)
    
    assert exported["Name"] == data["name"]
    assert exported["RepositoryType"] == data["repository_type"]
    assert exported["Model"] == data["model"]
    assert exported["Dimensionality"] == data["dimensionality"]

def test_field_aliases():
    """Test that field aliases are working correctly."""
    data = {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "TenantGUID": "987fcdeb-51d3-a456-426614174000",
        "Name": "Test Repository",
        "RepositoryType": "MysqlHeatwave",
        "EndpointUrl": "https://vector.example.com",
        "DatabaseHostname": "db.example.com",
        "DatabasePort": 3306,
        "CreatedUtc": "2024-01-01T00:00:00Z"
    }
    
    repo = VectorRepositoryModel(**data)
    assert repo.guid == data["GUID"]
    assert repo.tenant_guid == data["TenantGUID"]
    assert repo.name == data["Name"]
    assert repo.repository_type == data["RepositoryType"]
    assert repo.endpoint_url == data["EndpointUrl"]
    assert repo.database_hostname == data["DatabaseHostname"]
    assert repo.database_port == data["DatabasePort"]

def test_optional_fields():
    """Test that optional fields can be None."""
    repo = VectorRepositoryModel(
        endpoint_url=None,
        api_key=None,
        database_hostname=None,
        database_name=None,
        database_table=None,
        database_user=None,
        database_password=None,
        prompt_suffix=None
    )
    
    assert repo.endpoint_url is None
    assert repo.api_key is None
    assert repo.database_hostname is None
    assert repo.database_name is None
    assert repo.database_table is None
    assert repo.database_user is None
    assert repo.database_password is None
    assert repo.prompt_suffix is None

def test_prompt_prefix_default():
    """Test the default prompt prefix value and customization."""
    # Test default value
    repo = VectorRepositoryModel()
    assert "Use the following pieces of context" in repo.prompt_prefix
    assert "politely explain that you don't have relevant context" in repo.prompt_prefix

    # Test custom value
    custom_prefix = "Custom prompt prefix"
    repo = VectorRepositoryModel(prompt_prefix=custom_prefix)
    assert repo.prompt_prefix == custom_prefix

def test_name_validation():
    """Test name field validation and default value."""
    # Test default name
    repo = VectorRepositoryModel()
    assert repo.name == "My vector repository"

    # Test custom name
    custom_name = "Custom Vector DB"
    repo = VectorRepositoryModel(name=custom_name)
    assert repo.name == custom_name

    # Test empty string
    repo = VectorRepositoryModel(name="")
    assert repo.name == ""