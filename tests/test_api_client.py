import pytest
import datetime
import decimal
from viewio_sdk.api_client import ApiClient
from viewio_sdk.configuration import Configuration
from viewio_sdk.exceptions import ApiException
from viewio_sdk.models.node import Node
from pydantic import SecretStr

@pytest.fixture
def api_client():
    return ApiClient()

def test_user_agent(api_client):
    assert "OpenAPI-Generator" in api_client.user_agent
    api_client.user_agent = "Custom User Agent"
    assert api_client.user_agent == "Custom User Agent"

def test_set_default_header(api_client):
    api_client.set_default_header("X-Test", "Test Value")
    assert api_client.default_headers["X-Test"] == "Test Value"

def test_get_default():
    default_client = ApiClient.get_default()
    assert isinstance(default_client, ApiClient)

def test_set_default():
    custom_client = ApiClient(Configuration())
    ApiClient.set_default(custom_client)
    assert ApiClient.get_default() == custom_client

def test_sanitize_for_serialization(api_client):
    test_data = {
        "string": "test",
        "int": 123,
        "float": 123.45,
        "bool": True,
        "none": None,
        "list": [1, 2, 3],
        "dict": {"key": "value"},
        "date": datetime.date(2023, 1, 1),
        "datetime": datetime.datetime(2023, 1, 1, 12, 0),
        "decimal": decimal.Decimal("123.45"),
        "secret": SecretStr("password"),
    }

    result = api_client.sanitize_for_serialization(test_data)

    assert result["string"] == "test"
    assert result["int"] == 123
    assert result["float"] == 123.45
    assert result["bool"] is True
    assert result["none"] is None
    assert result["list"] == [1, 2, 3]
    assert result["dict"] == {"key": "value"}
    assert result["date"] == "2023-01-01"
    assert result["datetime"] == "2023-01-01T12:00:00"
    assert result["decimal"] == "123.45"
    assert result["secret"] == "password"

def test_deserialize(api_client):
    json_data = '{"GUID": "value", "Name": "value"}'
    result = api_client.deserialize(json_data, Node, "application/json")
    assert result == Node.from_json(json_data)

    text_data = "Hello, World!"
    result = api_client.deserialize(text_data, str, "text/plain")
    assert result == "Hello, World!"

    with pytest.raises(ApiException):
        api_client.deserialize("data", str, "unsupported/type")

def test_parameters_to_tuples(api_client):
    params = {"key1": "value1", "key2": ["value2", "value3"]}
    collection_formats = {"key2": "csv"}
    result = api_client.parameters_to_tuples(params, collection_formats)
    assert ("key1", "value1") in result
    assert ("key2", "value2,value3") in result

def test_parameters_to_url_query(api_client):
    params = {"key1": "value 1", "key2": ["value2", "value3"]}
    collection_formats = {"key2": "csv"}
    result = api_client.parameters_to_url_query(params, collection_formats)
    assert "key1=value%201" in result
    assert "key2=value2,value3" in result

def test_select_header_accept(api_client):
    accepts = ["application/json", "application/xml"]
    result = api_client.select_header_accept(accepts)
    assert result == "application/json"

    result = api_client.select_header_accept([])
    assert result is None

def test_select_header_content_type(api_client):
    content_types = ["application/json", "application/xml"]
    result = api_client.select_header_content_type(content_types)
    assert result == "application/json"

    result = api_client.select_header_content_type([])
    assert result is None

def test_deserialize_primitive(api_client):
    assert api_client._ApiClient__deserialize_primitive("123", int) == 123
    assert api_client._ApiClient__deserialize_primitive("true", bool) is True
    assert api_client._ApiClient__deserialize_primitive("test", str) == "test"

def test_deserialize_object(api_client):
    obj = {"key": "value"}
    assert api_client._ApiClient__deserialize_object(obj) == obj

def test_deserialize_date(api_client):
    date_str = "2023-01-01"
    result = api_client._ApiClient__deserialize_date(date_str)
    assert isinstance(result, datetime.date)
    assert result.isoformat() == date_str

def test_deserialize_datetime(api_client):
    datetime_str = "2023-01-01T12:00:00"
    result = api_client._ApiClient__deserialize_datetime(datetime_str)
    assert isinstance(result, datetime.datetime)
    assert result.isoformat() == datetime_str

def test_deserialize_model(api_client):
    class TestModel:
        @classmethod
        def from_dict(cls, data):
            return cls()

    data = {"key": "value"}
    result = api_client._ApiClient__deserialize_model(data, TestModel)
    assert isinstance(result, TestModel)

