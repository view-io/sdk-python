import pytest
from unittest.mock import patch, Mock
from pydantic import BaseModel
from view_sdk.mixins import (
    ExistsAPIResource,
    CreateableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    UpdatableAPIResource,
    DeletableAPIResource,
    RetrievableStatisticsMixin,
    EnumerableAPIResource,
    EnumerableAPIResourceWithData
)
from view_sdk.exceptions import ResourceNotFoundError

# Test models
class MockModel(BaseModel):
    id: str
    name: str

class MockStatsModel(BaseModel):
    count: int
    size: int

# Test resource classes
class TestExistsResource(ExistsAPIResource):
    RESOURCE_NAME = "test"
    REQUIRES_TENANT = True

class TestCreateResource(CreateableAPIResource):
    RESOURCE_NAME = "test"
    MODEL = MockModel
    REQUIRES_TENANT = True

class TestRetrieveResource(RetrievableAPIResource):
    RESOURCE_NAME = "test"
    MODEL = MockModel
    REQUIRES_TENANT = True

class TestAllRetrieveResource(AllRetrievableAPIResource):
    RESOURCE_NAME = "test"
    MODEL = MockModel
    REQUIRES_TENANT = True
    PARENT_RESOURCE = "parents"
    PARENT_ID_PARAM = "test_parent_guid"

class TestUpdateResource(UpdatableAPIResource):
    RESOURCE_NAME = "test"
    MODEL = MockModel
    REQUIRES_TENANT = True
    PARENT_RESOURCE = "parents"
    PARENT_ID_PARAM = "test_parent_guid"

class TestDeleteResource(DeletableAPIResource):
    RESOURCE_NAME = "test"
    REQUIRES_TENANT = True
    PARENT_RESOURCE = "parents"
    PARENT_ID_PARAM = "test_parent_guid"

class TestStatsResource(RetrievableStatisticsMixin):
    RESOURCE_NAME = "test"
    STATS_MODEL = MockStatsModel
    REQUIRES_TENANT = True
    SERVICE = "test-service"

class TestStatsResourceNoModel(RetrievableStatisticsMixin):
    RESOURCE_NAME = "test"
    REQUIRES_TENANT = True
    SERVICE = "test-service"

class TestCreateResourceWithRequestModel(CreateableAPIResource):
    RESOURCE_NAME = "test"
    MODEL = MockModel
    REQUEST_MODEL = MockModel
    REQUIRES_TENANT = True

class TestEnumerableResource(EnumerableAPIResource):
    RESOURCE_NAME = "test"
    MODEL = MockModel
    REQUIRES_TENANT = True

class TestEnumerableAPIResourceWithData(EnumerableAPIResourceWithData):
    RESOURCE_NAME = "test"
    MODEL = MockModel
    REQUIRES_TENANT = True
    PARENT_ID_PARAM = "test_parent_guid"

@pytest.fixture
def mock_client_with_tenant():
    with patch('view_sdk.mixins.get_client') as mock:
        client = Mock()
        client.tenant_guid = "test-tenant"
        mock.return_value = client
        yield client

@pytest.fixture
def mock_client_without_tenant():
    with patch('view_sdk.mixins.get_client') as mock:
        client = Mock()
        client.tenant_guid = None
        mock.return_value = client
        yield client

def test_exists_resource_with_tenant(mock_client_with_tenant):
    # Test successful exists check
    mock_client_with_tenant.request.return_value = None
    assert TestExistsResource.exists("test-id") is True

    # Test non-existent resource
    mock_client_with_tenant.request.side_effect = ResourceNotFoundError("Not found")
    assert TestExistsResource.exists("test-id") is False

def test_exists_resource_without_tenant(mock_client_without_tenant):
    with pytest.raises(ValueError) as exc_info:
        TestExistsResource.exists("test-id")
    assert str(exc_info.value) == "Tenant GUID is required for this resource."

def test_createable_resource_with_tenant(mock_client_with_tenant):
    test_data = {"id": "test-id", "name": "test-name"}
    mock_client_with_tenant.request.return_value = test_data

    result = TestCreateResource.create(**test_data)
    assert isinstance(result, MockModel)
    assert result.id == "test-id"
    assert result.name == "test-name"

def test_createable_resource_without_tenant(mock_client_without_tenant):
    test_data = {"id": "test-id", "name": "test-name"}
    with pytest.raises(ValueError) as exc_info:
        TestCreateResource.create(**test_data)
    assert str(exc_info.value) == "Tenant GUID is required for this resource."

def test_retrievable_resource_with_tenant(mock_client_with_tenant):
    test_data = {"id": "test-id", "name": "test-name"}
    mock_client_with_tenant.request.return_value = test_data

    result = TestRetrieveResource.retrieve("test-id")
    assert isinstance(result, MockModel)
    assert result.id == "test-id"
    assert result.name == "test-name"

def test_retrievable_resource_without_tenant(mock_client_without_tenant):
    with pytest.raises(ValueError) as exc_info:
        TestRetrieveResource.retrieve("test-id")
    assert str(exc_info.value) == "Tenant GUID is required for this resource."

def test_all_retrievable_resource_with_tenant(mock_client_with_tenant):
    test_data = [
        {"id": "test-id-1", "name": "test-name-1"},
        {"id": "test-id-2", "name": "test-name-2"}
    ]
    mock_client_with_tenant.request.return_value = test_data

    results = TestAllRetrieveResource.retrieve_all(test_parent_guid="parent-id")
    assert len(results) == 2
    assert all(isinstance(result, MockModel) for result in results)
    assert results[0].id == "test-id-1"
    assert results[1].id == "test-id-2"

def test_all_retrievable_resource_without_tenant(mock_client_without_tenant):
    with pytest.raises(ValueError) as exc_info:
        TestAllRetrieveResource.retrieve_all(test_parent_guid="parent-id")
    assert str(exc_info.value) == "Tenant GUID is required for this resource."

def test_updatable_resource_with_tenant(mock_client_with_tenant):
    test_data = {"id": "test-id", "name": "updated-name"}
    mock_client_with_tenant.request.return_value = test_data

    result = TestUpdateResource.update("test-id", **test_data)
    assert isinstance(result, MockModel)
    assert result.id == "test-id"
    assert result.name == "updated-name"

def test_updatable_resource_without_tenant(mock_client_without_tenant):
    test_data = {"id": "test-id", "name": "updated-name"}
    with pytest.raises(ValueError) as exc_info:
        TestUpdateResource.update("test-id", **test_data)
    assert str(exc_info.value) == "Tenant GUID is required for this resource."

def test_deletable_resource_with_tenant(mock_client_with_tenant):
    mock_client_with_tenant.request.return_value = None
    TestDeleteResource.delete("test-id")
    mock_client_with_tenant.request.assert_called_once()

def test_deletable_resource_without_tenant(mock_client_without_tenant):
    with pytest.raises(ValueError) as exc_info:
        TestDeleteResource.delete("test-id")
    assert str(exc_info.value) == "Tenant GUID is required for this resource."

# Test resources that don't require tenant
class TestResourceNoTenant(ExistsAPIResource, CreateableAPIResource,
                         RetrievableAPIResource, AllRetrievableAPIResource,
                         UpdatableAPIResource, DeletableAPIResource,
                         EnumerableAPIResource):
    RESOURCE_NAME = "test"
    MODEL = MockModel
    REQUIRES_TENANT = False
    PARENT_RESOURCE = "parents"
    PARENT_ID_PARAM = "test_parent_guid"

def test_exists_no_tenant_requirement(mock_client_without_tenant):
    mock_client_without_tenant.request.return_value = None
    assert TestResourceNoTenant.exists("test-id") is True

def test_create_no_tenant_requirement(mock_client_without_tenant):
    test_data = {"id": "test-id", "name": "test-name"}
    mock_client_without_tenant.request.return_value = test_data

    result = TestResourceNoTenant.create(**test_data)
    assert isinstance(result, MockModel)
    assert result.id == "test-id"

def test_retrieve_no_tenant_requirement(mock_client_without_tenant):
    test_data = {"id": "test-id", "name": "test-name"}
    mock_client_without_tenant.request.return_value = test_data

    result = TestResourceNoTenant.retrieve("test-id")
    assert isinstance(result, MockModel)
    assert result.id == "test-id"

def test_retrieve_all_no_tenant_requirement(mock_client_without_tenant):
    test_data = [
        {"id": "test-id-1", "name": "test-1"},
        {"id": "test-id-2", "name": "test-2"}
    ]
    mock_client_without_tenant.request.return_value = test_data

    results = TestResourceNoTenant.retrieve_all()
    assert len(results) == 2
    assert all(isinstance(result, MockModel) for result in results)

def test_update_no_tenant_requirement(mock_client_without_tenant):
    test_data = {"id": "test-id", "name": "updated-name"}
    mock_client_without_tenant.request.return_value = test_data

    result = TestResourceNoTenant.update("test-id", **test_data)
    assert isinstance(result, MockModel)
    assert result.name == "updated-name"

def test_delete_no_tenant_requirement(mock_client_without_tenant):
    mock_client_without_tenant.request.return_value = None
    TestResourceNoTenant.delete("test-id")
    mock_client_without_tenant.request.assert_called_once()

def test_enumerate_no_tenant_requirement(mock_client_without_tenant):
    test_data = {
        "Success": True,
        "Objects": [
            {"id": "test-id-1", "name": "test-1"},
            {"id": "test-id-2", "name": "test-2"}
        ]
    }
    mock_client_without_tenant.request.return_value = test_data

    result = TestResourceNoTenant.enumerate()
    assert result.success is True
    assert len(result.objects) == 2
    assert all(isinstance(obj, MockModel) for obj in result.objects)

# Test parent ID functionality for non-tenant resources
def test_no_tenant_with_parent_guid(mock_client_without_tenant):
    test_data = {"id": "test-id", "name": "test-name"}
    mock_client_without_tenant.request.return_value = test_data

    result = TestResourceNoTenant.create(test_parent_guid="parent-id", **test_data)
    assert isinstance(result, MockModel)
    mock_client_without_tenant.request.assert_called_once()

def test_no_tenant_with_invalid_parent_guid(mock_client_without_tenant):
    with pytest.raises(ValueError) as exc_info:
        TestResourceNoTenant.create(test_parent_guid="", id="test-id", name="test-name")
    assert str(exc_info.value) == "test_parent_guid cannot be empty if provided"

# New test cases for RetrievableStatisticsMixin
def test_retrieve_statistics_with_tenant(mock_client_with_tenant):
    test_data = {"count": 10, "size": 1024}
    mock_client_with_tenant.request.return_value = test_data

    result = TestStatsResource.retrieve_statistics("test-id")
    assert isinstance(result, MockStatsModel)
    assert result.count == 10
    assert result.size == 1024

def test_retrieve_statistics_without_model(mock_client_with_tenant):
    test_data = {"count": 10, "size": 1024}
    mock_client_with_tenant.request.return_value = test_data

    result = TestStatsResourceNoModel.retrieve_statistics("test-id")
    assert result == test_data

def test_retrieve_statistics_without_tenant(mock_client_without_tenant):
    with pytest.raises(ValueError) as exc_info:
        TestStatsResource.retrieve_statistics("test-id")
    assert str(exc_info.value) == "Tenant GUID is required for this resource."

def test_retrieve_statistics_with_parent(mock_client_with_tenant):
    test_data = {"count": 10, "size": 1024}
    mock_client_with_tenant.request.return_value = test_data

    result = TestStatsResource.retrieve_statistics(
        "test-id",
        parent_guid="parent-id"
    )
    assert isinstance(result, MockStatsModel)
    assert result.count == 10
    assert result.size == 1024

# Additional test cases for error handling in existing mixins
def test_createable_resource_invalid_model(mock_client_with_tenant):
    test_data = {"invalid": "data"}
    mock_client_with_tenant.request.return_value = test_data

    with pytest.raises(ValueError):
        TestCreateResource.create(**test_data)

def test_updatable_resource_invalid_model(mock_client_with_tenant):
    test_data = {"invalid": "data"}
    mock_client_with_tenant.request.return_value = test_data

    with pytest.raises(ValueError):
        TestUpdateResource.update("test-id", **test_data)

def test_retrievable_resource_not_found(mock_client_with_tenant):
    mock_client_with_tenant.request.side_effect = ResourceNotFoundError("Not found")

    with pytest.raises(ResourceNotFoundError):
        TestRetrieveResource.retrieve("test-id")

def test_all_retrievable_with_parent(mock_client_with_tenant):
    test_data = [
        {"id": "test-id-1", "name": "test-name-1"},
        {"id": "test-id-2", "name": "test-name-2"}
    ]
    mock_client_with_tenant.request.return_value = test_data

    results = TestAllRetrieveResource.retrieve_all(test_parent_guid="parent-id")
    assert len(results) == 2
    assert all(isinstance(result, MockModel) for result in results)

def test_update_with_parent(mock_client_with_tenant):
    test_data = {"id": "test-id", "name": "updated-name"}
    mock_client_with_tenant.request.return_value = test_data

    result = TestUpdateResource.update(
        "test-id",
        test_parent_guid="parent-id",
        **test_data
    )
    assert isinstance(result, MockModel)
    assert result.name == "updated-name"

def test_delete_with_parent(mock_client_with_tenant):
    mock_client_with_tenant.request.return_value = None
    TestDeleteResource.delete("test-id", test_parent_guid="parent-id")
    mock_client_with_tenant.request.assert_called_once()

# Test error handling for parent_guid validation
def test_retrieve_with_invalid_parent(mock_client_with_tenant):
    with pytest.raises(ValueError) as exc_info:
        TestRetrieveResource.retrieve("test-id", parent_guid="")
    assert "1 validation error for MockModel" in str(exc_info.value)

def test_all_retrieve_with_invalid_parent(mock_client_with_tenant):
    # Mock return value as an empty list since we expect the request to fail validation
    mock_client_with_tenant.request.return_value = []

    with pytest.raises(ValueError) as exc_info:
        TestAllRetrieveResource.retrieve_all(test_parent_guid="")
    assert str(exc_info.value) == "test_parent_guid cannot be empty if provided"

def test_update_with_invalid_parent(mock_client_with_tenant):
    test_data = {"id": "test-id", "name": "test-name"}
    with pytest.raises(ValueError) as exc_info:
        TestUpdateResource.update("test-id", test_parent_guid="", **test_data)
    assert "parent_guid cannot be empty if provided" in str(exc_info.value)

def test_delete_with_invalid_parent(mock_client_with_tenant):
    with pytest.raises(ValueError) as exc_info:
        TestDeleteResource.delete("test-id", test_parent_guid="")
    assert str(exc_info.value) == "test_parent_guid cannot be empty if provided"

def test_create_with_request_model(mock_client_with_tenant):
    test_data = {"id": "test-id", "name": "test-name"}
    mock_client_with_tenant.request.return_value = test_data

    result = TestCreateResourceWithRequestModel.create(**test_data)
    assert isinstance(result, MockModel)
    assert result.id == "test-id"
    assert result.name == "test-name"

def test_create_with_custom_method(mock_client_with_tenant):
    TestCreateResourceWithRequestModel.CREATE_METHOD = "POST"
    test_data = {"id": "test-id", "name": "test-name"}
    mock_client_with_tenant.request.return_value = test_data

    result = TestCreateResourceWithRequestModel.create(**test_data)
    assert isinstance(result, MockModel)
    TestCreateResourceWithRequestModel.CREATE_METHOD = "PUT"

def test_enumerable_resource(mock_client_with_tenant):
    test_data = {
        "Success": True,
        "Objects": [
            {"id": "test-id-1", "name": "test-1"},
            {"id": "test-id-2", "name": "test-2"}
        ]
    }
    mock_client_with_tenant.request.return_value = test_data

    result = TestEnumerableResource.enumerate()
    assert result.success is True
    assert len(result.objects) == 2
    assert all(isinstance(obj, MockModel) for obj in result.objects)

def test_enumerable_resource_without_model(mock_client_with_tenant):
    TestEnumerableResource.MODEL = None
    test_data = {
        "Success": True,
        "Objects": [
            {"id": "test-id-1", "name": "test-1"}
        ]
    }
    mock_client_with_tenant.request.return_value = test_data

    result = TestEnumerableResource.enumerate()
    assert result == test_data
    TestEnumerableResource.MODEL = MockModel

def test_enumerable_resource_without_tenant(mock_client_without_tenant):
    with pytest.raises(ValueError) as exc_info:
        TestEnumerableResource.enumerate()
    assert str(exc_info.value) == "Tenant GUID is required for this resource."

# New test cases for EnumerableAPIResourceWithData
@patch('view_sdk.mixins.get_client')
def test_enumerate_with_query_success(mock_get_client):
    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_client.tenant_guid = "tenant123"
    mock_client.request.return_value = {"success": True, "max_results": 1000}

    result = TestEnumerableAPIResourceWithData.enumerate_with_query(test_parent_guid="parent123")
    assert result.success == True
    assert result.max_results == 1000

@patch('view_sdk.mixins.get_client')
def test_enumerate_with_query_missing_tenant(mock_get_client):
    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_client.tenant_guid = None

    with pytest.raises(ValueError, match="Tenant GUID is required for this resource."):
        TestEnumerableAPIResourceWithData.enumerate_with_query(test_parent_guid="parent123")

@patch('view_sdk.mixins.get_client')
def test_enumerate_with_query_missing_parent_guid(mock_get_client):
    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_client.tenant_guid = "tenant123"

    with pytest.raises(ValueError, match="test_parent_guid is required for this resource."):
        TestEnumerableAPIResourceWithData.enumerate_with_query()
