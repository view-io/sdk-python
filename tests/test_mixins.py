import pytest
from unittest.mock import patch, Mock
from pydantic import BaseModel
from view_sdk.mixins import (
    BaseAPIResource,
    ExistsAPIResource,
    CreateableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    UpdatableAPIResource,
    DeletableAPIResource,
    RetrievableStatisticsMixin,
    EnumerableAPIResource,
    EnumerableAPIResourceWithData,
    HealthCheckAPIResource,
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


class TestEnumerableAPIResourceWithDataNoModel(EnumerableAPIResourceWithData):
    RESOURCE_NAME = "test"
    MODEL = None
    REQUIRES_TENANT = True
    PARENT_ID_PARAM = "test_parent_guid"


class TestHealthCheckResource(HealthCheckAPIResource):
    RESOURCE_NAME = "test"
    REQUIRES_TENANT = True


class TestHealthCheckResourceNoTenant(HealthCheckAPIResource):
    RESOURCE_NAME = "test"
    REQUIRES_TENANT = False


class TestResourceWithParentNoParam(BaseAPIResource):
    RESOURCE_NAME = "test"
    PARENT_RESOURCE = "parents"
    PARENT_ID_PARAM = ""  # Empty string to test the elif condition
    REQUIRES_TENANT = True


class TestResourceWithDumpModelData(BaseAPIResource):
    RESOURCE_NAME = "test"
    MODEL = None  # Test when MODEL is None
    REQUIRES_TENANT = True


@pytest.fixture
def mock_client_with_tenant():
    with patch("view_sdk.mixins.get_client") as mock:
        client = Mock()
        client.tenant_guid = "test-tenant"
        mock.return_value = client
        yield client


@pytest.fixture
def mock_client_without_tenant():
    with patch("view_sdk.mixins.get_client") as mock:
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
        {"id": "test-id-2", "name": "test-name-2"},
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
class TestResourceNoTenant(
    ExistsAPIResource,
    CreateableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    UpdatableAPIResource,
    DeletableAPIResource,
    EnumerableAPIResource,
):
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
        {"id": "test-id-2", "name": "test-2"},
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
            {"id": "test-id-2", "name": "test-2"},
        ],
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

    result = TestStatsResource.retrieve_statistics("test-id", parent_guid="parent-id")
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
        {"id": "test-id-2", "name": "test-name-2"},
    ]
    mock_client_with_tenant.request.return_value = test_data

    results = TestAllRetrieveResource.retrieve_all(test_parent_guid="parent-id")
    assert len(results) == 2
    assert all(isinstance(result, MockModel) for result in results)


def test_update_with_parent(mock_client_with_tenant):
    test_data = {"id": "test-id", "name": "updated-name"}
    mock_client_with_tenant.request.return_value = test_data

    result = TestUpdateResource.update(
        "test-id", test_parent_guid="parent-id", **test_data
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
            {"id": "test-id-2", "name": "test-2"},
        ],
    }
    mock_client_with_tenant.request.return_value = test_data

    result = TestEnumerableResource.enumerate()
    assert result.success is True
    assert len(result.objects) == 2
    assert all(isinstance(obj, MockModel) for obj in result.objects)


def test_enumerable_resource_without_model(mock_client_with_tenant):
    TestEnumerableResource.MODEL = None
    test_data = {"Success": True, "Objects": [{"id": "test-id-1", "name": "test-1"}]}
    mock_client_with_tenant.request.return_value = test_data

    result = TestEnumerableResource.enumerate()
    assert result == test_data
    TestEnumerableResource.MODEL = MockModel


def test_enumerable_resource_without_tenant(mock_client_without_tenant):
    with pytest.raises(ValueError) as exc_info:
        TestEnumerableResource.enumerate()
    assert str(exc_info.value) == "Tenant GUID is required for this resource."


# New test cases for EnumerableAPIResourceWithData
@patch("view_sdk.mixins.get_client")
def test_enumerate_with_query_success(mock_get_client):
    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_client.tenant_guid = "tenant123"
    mock_client.request.return_value = {"success": True, "max_results": 1000}

    result = TestEnumerableAPIResourceWithData.enumerate_with_query(
        test_parent_guid="parent123"
    )
    assert result.success
    assert result.max_results == 1000


@patch("view_sdk.mixins.get_client")
def test_enumerate_with_query_missing_tenant(mock_get_client):
    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_client.tenant_guid = None

    with pytest.raises(ValueError, match="Tenant GUID is required for this resource."):
        TestEnumerableAPIResourceWithData.enumerate_with_query(
            test_parent_guid="parent123"
        )


@patch("view_sdk.mixins.get_client")
def test_enumerate_with_query_missing_parent_guid(mock_get_client):
    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_client.tenant_guid = "tenant123"

    with pytest.raises(
        ValueError, match="test_parent_guid is required for this resource."
    ):
        TestEnumerableAPIResourceWithData.enumerate_with_query()


# Test cases for missing coverage blocks


def test_get_resource_path_parent_no_param():
    """Test _get_resource_path when PARENT_RESOURCE exists but PARENT_ID_PARAM is empty."""
    path_components, kwargs = TestResourceWithParentNoParam._get_resource_path()
    assert "parents" in path_components
    assert "test" in path_components


def test_dump_model_data_list_no_model():
    """Test _dump_model_data with list data when model is None."""
    data = [{"id": "1", "name": "test1"}, {"id": "2", "name": "test2"}]
    result = TestResourceWithDumpModelData._dump_model_data(data)
    assert result == data


def test_dump_model_data_dict_no_model():
    """Test _dump_model_data with dict data when model is None."""
    data = {"id": "1", "name": "test1"}
    result = TestResourceWithDumpModelData._dump_model_data(data)
    assert result == data


def test_dump_model_data_list_with_model():
    """Test _dump_model_data with list data when model is provided."""
    data = [{"id": "1", "name": "test1"}, {"id": "2", "name": "test2"}]
    result = TestResourceWithDumpModelData._dump_model_data(data, MockModel)
    assert len(result) == 2
    assert all("id" in item for item in result)


def test_dump_model_data_dict_with_model():
    """Test _dump_model_data with dict data when model is provided."""
    data = {"id": "1", "name": "test1"}
    result = TestResourceWithDumpModelData._dump_model_data(data, MockModel)
    assert "id" in result
    assert "name" in result


@patch("view_sdk.mixins.get_client")
def test_all_retrievable_non_list_response(mock_get_client):
    """Test AllRetrievableAPIResource when response is not a list and RETURNS_LIST is True."""
    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_client.tenant_guid = "tenant123"
    mock_client.request.return_value = {"not": "a list"}  # Non-list response

    TestAllRetrieveResource.RETURNS_LIST = True
    results = TestAllRetrieveResource.retrieve_all()
    assert results == []  # Should return empty list
    TestAllRetrieveResource.RETURNS_LIST = True  # Reset


@patch("view_sdk.mixins.get_client")
def test_all_retrievable_non_list_response_returns_list_false(mock_get_client):
    """Test AllRetrievableAPIResource when response is not a list and RETURNS_LIST is False."""
    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_client.tenant_guid = "tenant123"
    mock_client.request.return_value = {"not": "a list"}  # Non-list response

    # Create a temporary class with RETURNS_LIST = False and MODEL = None
    class TempAllRetrieveResource(AllRetrievableAPIResource):
        RESOURCE_NAME = "test"
        MODEL = None  # No model validation
        REQUIRES_TENANT = True
        PARENT_RESOURCE = "parents"
        PARENT_ID_PARAM = "test_parent_guid"
        RETURNS_LIST = False

    results = TempAllRetrieveResource.retrieve_all()
    assert results == {"not": "a list"}  # Should return the response as-is


@patch("view_sdk.mixins.get_client")
def test_stats_resource_no_model(mock_get_client):
    """Test RetrievableStatisticsMixin when STATS_MODEL is None."""
    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_client.tenant_guid = "tenant123"
    mock_client.request.return_value = {"count": 10, "size": 1024}

    result = TestStatsResourceNoModel.retrieve_statistics("test-id")
    assert result == {"count": 10, "size": 1024}


@patch("view_sdk.mixins.get_client")
def test_delete_resource_exception(mock_get_client):
    """Test DeletableAPIResource exception handling in delete method."""
    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_client.tenant_guid = "tenant123"
    mock_client.request.side_effect = Exception("Delete failed")

    result = TestDeleteResource.delete("test-id")
    assert result is False


@patch("view_sdk.mixins.get_client")
def test_health_check_resource_with_tenant(mock_get_client):
    """Test HealthCheckAPIResource with tenant requirement."""
    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_client.tenant_guid = "tenant123"
    mock_client.request.return_value = None

    result = TestHealthCheckResource.check()
    assert result is True


@patch("view_sdk.mixins.get_client")
def test_health_check_resource_without_tenant(mock_get_client):
    """Test HealthCheckAPIResource without tenant requirement."""
    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_client.tenant_guid = None
    mock_client.request.return_value = None

    result = TestHealthCheckResourceNoTenant.check()
    assert result is True


@patch("view_sdk.mixins.get_client")
def test_health_check_resource_exception(mock_get_client):
    """Test HealthCheckAPIResource exception handling."""
    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_client.tenant_guid = "tenant123"
    mock_client.request.side_effect = Exception("Health check failed")

    result = TestHealthCheckResource.check()
    assert result is False


@patch("view_sdk.mixins.get_client")
def test_health_check_resource_no_tenant_required(mock_get_client):
    """Test HealthCheckAPIResource when tenant is required but not provided."""
    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_client.tenant_guid = None

    with pytest.raises(ValueError, match="Tenant GUID is required for this resource."):
        TestHealthCheckResource.check()


@patch("view_sdk.mixins.get_client")
def test_enumerable_with_data_no_model(mock_get_client):
    """Test EnumerableAPIResourceWithData when MODEL is None."""
    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_client.tenant_guid = "tenant123"
    mock_client.request.return_value = {"success": True, "max_results": 1000}

    result = TestEnumerableAPIResourceWithDataNoModel.enumerate_with_query(
        test_parent_guid="parent123"
    )
    assert result == {"success": True, "max_results": 1000}


def test_validate_parent_guid_empty():
    """Test _validate_parent_guid with empty string."""
    with pytest.raises(
        ValueError, match="test_parent_guid cannot be empty if provided"
    ):
        TestAllRetrieveResource._validate_parent_guid("")


def test_validate_parent_guid_none():
    """Test _validate_parent_guid with None (should not raise)."""
    # Should not raise an exception
    TestAllRetrieveResource._validate_parent_guid(None)


def test_validate_parent_guid_valid():
    """Test _validate_parent_guid with valid GUID (should not raise)."""
    # Should not raise an exception
    TestAllRetrieveResource._validate_parent_guid("valid-guid")


# Test query parameters functionality
class TestResourceWithQueryParams(BaseAPIResource):
    RESOURCE_NAME = "test"
    QUERY_PARAMS = {"param1": "value1", "param2": None}
    REQUIRES_TENANT = True


def test_get_resource_path_with_query_params():
    """Test _get_resource_path with predefined query parameters."""
    path_components, kwargs = TestResourceWithQueryParams._get_resource_path("guid1")
    assert "test" in path_components
    assert "guid1" in path_components
    assert kwargs["param1"] == "value1"
    assert kwargs["param2"] is None


# Test parent GUID validation in various scenarios
@patch("view_sdk.mixins.get_client")
def test_all_retrievable_with_empty_parent_guid(mock_get_client):
    """Test AllRetrievableAPIResource with empty parent GUID."""
    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_client.tenant_guid = "tenant123"

    with pytest.raises(
        ValueError, match="test_parent_guid cannot be empty if provided"
    ):
        TestAllRetrieveResource.retrieve_all(test_parent_guid="")


@patch("view_sdk.mixins.get_client")
def test_delete_with_empty_parent_guid(mock_get_client):
    """Test DeletableAPIResource with empty parent GUID."""
    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_client.tenant_guid = "tenant123"

    with pytest.raises(
        ValueError, match="test_parent_guid cannot be empty if provided"
    ):
        TestDeleteResource.delete("test-id", test_parent_guid="")


# Test createable resource with _data parameter
@patch("view_sdk.mixins.get_client")
def test_create_with_data_parameter(mock_get_client):
    """Test CreateableAPIResource with _data parameter."""
    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_client.tenant_guid = "tenant123"
    mock_client.request.return_value = {"id": "test-id", "name": "test-name"}

    result = TestCreateResource.create(_data={"id": "test-id", "name": "test-name"})
    assert isinstance(result, MockModel)
    assert result.id == "test-id"


# Test updatable resource with data parameter
@patch("view_sdk.mixins.get_client")
def test_update_with_data_parameter(mock_get_client):
    """Test UpdatableAPIResource with data parameter."""
    mock_client = Mock()
    mock_get_client.return_value = mock_client
    mock_client.tenant_guid = "tenant123"
    mock_client.request.return_value = {"id": "test-id", "name": "updated-name"}

    result = TestUpdateResource.update(
        "test-id", data={"id": "test-id", "name": "updated-name"}
    )
    assert isinstance(result, MockModel)
    assert result.name == "updated-name"
