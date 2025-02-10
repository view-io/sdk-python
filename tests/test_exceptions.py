import pytest
from viewio_sdk.exceptions import (
    ApiTypeError, ApiValueError, ApiAttributeError, ApiKeyError,
    ApiException, BadRequestException, NotFoundException,
    UnauthorizedException, ForbiddenException, ServiceException,
    render_path
)

def test_api_type_error():
    with pytest.raises(ApiTypeError) as exc_info:
        raise ApiTypeError("Type error", path_to_item=["a", "b", 1], valid_classes=(str, int), key_type=True)
    assert "Type error at ['a']['b'][1]" in str(exc_info.value)

def test_api_value_error():
    with pytest.raises(ApiValueError) as exc_info:
        raise ApiValueError("Value error", path_to_item=["x", "y", 2])
    assert "Value error at ['x']['y'][2]" in str(exc_info.value)

def test_api_attribute_error():
    with pytest.raises(ApiAttributeError) as exc_info:
        raise ApiAttributeError("Attribute error", path_to_item=["attr1", "attr2"])
    assert "Attribute error at ['attr1']['attr2']" in str(exc_info.value)

def test_api_key_error():
    with pytest.raises(ApiKeyError) as exc_info:
        raise ApiKeyError("Key error", path_to_item=["key1", "key2"])
    assert "Key error at ['key1']['key2']" in str(exc_info.value)

def test_api_exception():
    exc = ApiException(status=500, reason="Internal Server Error", body="Error occurred", data={"error": "details"})
    assert exc.status == 500
    assert exc.reason == "Internal Server Error"
    assert exc.body == "Error occurred"
    assert exc.data == {"error": "details"}

def test_api_exception_from_response():
    class MockResponse:
        def __init__(self, status, reason):
            self.status = status
            self.reason = reason
        def getheaders(self):
            return {"Content-Type": "application/json"}

    with pytest.raises(BadRequestException):
        ApiException.from_response(http_resp=MockResponse(400, "Bad Request"), body="Invalid input", data=None)

    with pytest.raises(UnauthorizedException):
        ApiException.from_response(http_resp=MockResponse(401, "Unauthorized"), body="Invalid token", data=None)

    with pytest.raises(ForbiddenException):
        ApiException.from_response(http_resp=MockResponse(403, "Forbidden"), body="Access denied", data=None)

    with pytest.raises(NotFoundException):
        ApiException.from_response(http_resp=MockResponse(404, "Not Found"), body="Resource not found", data=None)

    with pytest.raises(ServiceException):
        ApiException.from_response(http_resp=MockResponse(500, "Internal Server Error"), body="Server error", data=None)

def test_api_exception_str():
    exc = ApiException(status=404, reason="Not Found", body="Resource not found")
    exc_str = str(exc)
    assert "(404)" in exc_str
    assert "Reason: Not Found" in exc_str
    assert "HTTP response body: Resource not found" in exc_str

def test_render_path():
    path = ["user", "addresses", 0, "street"]
    rendered = render_path(path)
    assert rendered == "['user']['addresses'][0]['street']"
