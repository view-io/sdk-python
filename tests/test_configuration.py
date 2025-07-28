import pytest
from view_sdk.sdk_configuration import configure, get_client, Service, SdkConfiguration
from view_sdk.base import BaseClient


@pytest.fixture(autouse=True)
def reset_client():
    """Reset the global client before each test"""
    SdkConfiguration._instance = None
    yield
    SdkConfiguration._instance = None


def test_configure():
    configure(
        access_key="test-key", base_url="api.example.com", tenant_guid="test-tenant"
    )
    client = get_client(Service.STORAGE)
    assert isinstance(client, BaseClient)
    assert client.access_key == "test-key"
    assert client.base_url == "http://api.example.com:8001"
    assert client.tenant_guid == "test-tenant"


def test_configure_without_tenant():
    configure(access_key="test-key", base_url="api.example.com")
    client = get_client(Service.STORAGE)
    assert isinstance(client, BaseClient)
    assert client.tenant_guid is None


def test_get_client_without_configure():
    # The client should be None due to the autouse fixture
    with pytest.raises(ValueError) as exc_info:
        get_client(Service.STORAGE)
    assert str(exc_info.value) == "SDK is not configured. Call 'configure' first."


def test_double_configure():
    """Test that configuring twice works correctly"""
    configure(
        access_key="test-key-1",
        base_url="api1.example.com",
        tenant_guid="test-tenant-1",
    )

    configure(
        access_key="test-key-2",
        base_url="api2.example.com",
        tenant_guid="test-tenant-2",
    )

    client = get_client(Service.STORAGE)
    assert client.access_key == "test-key-2"
    assert client.base_url == "http://api2.example.com:8001"
    assert client.tenant_guid == "test-tenant-2"
