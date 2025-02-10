from viewio_sdk.models.api_error_response import ApiErrorResponse
from viewio_sdk.models.api_error_enum import ApiErrorEnum

def test_api_error_response_creation():
    error_response = ApiErrorResponse(
        Error=ApiErrorEnum.BADREQUEST,
        Context="Test context",
        Description="Test description"
    )
    assert error_response.error == ApiErrorEnum.BADREQUEST
    assert error_response.context == "Test context"
    assert error_response.description == "Test description"

def test_api_error_response_to_str():
    error_response = ApiErrorResponse(
        Error=ApiErrorEnum.NOTFOUND,
        Context="Item not found",
        Description="The requested item does not exist"
    )
    str_representation = error_response.to_str()
    assert "NOTFOUND" in str_representation
    assert "Item not found" in str_representation
    assert "The requested item does not exist" in str_representation

def test_api_error_response_to_json():
    error_response = ApiErrorResponse(
        Error=ApiErrorEnum.AUTHENTICATIONFAILED,
        Context="Invalid credentials",
        Description="The provided credentials are incorrect"
    )
    json_representation = error_response.to_json()
    assert "AuthenticationFailed" in json_representation
    assert "Invalid credentials" in json_representation
    assert "The provided credentials are incorrect" in json_representation

def test_api_error_response_from_json():
    json_str = '{"Error": "Conflict", "Context": "Duplicate entry", "Message": "The item already exists"}'
    error_response = ApiErrorResponse.from_json(json_str)
    assert error_response.error == ApiErrorEnum.CONFLICT
    assert error_response.context == "Duplicate entry"
    assert error_response.description == "The item already exists"

def test_api_error_response_to_dict():
    error_response = ApiErrorResponse(
        Error=ApiErrorEnum.INTERNALERROR,
        Context="Server error",
        Description="An unexpected error occurred"
    )
    dict_representation = error_response.to_dict()
    assert dict_representation["Error"] == "InternalError"
    assert dict_representation["Context"] == "Server error"
    assert dict_representation["Description"] == "An unexpected error occurred"

def test_api_error_response_from_dict():
    error_dict = {
        "Error": "TooLarge",
        "Context": "File size exceeded",
        "Message": "The uploaded file is too large"
    }
    error_response = ApiErrorResponse.from_dict(error_dict)
    assert error_response.error == ApiErrorEnum.TOOLARGE
    assert error_response.context == "File size exceeded"
    assert error_response.description == "The uploaded file is too large"

def test_api_error_response_nullable_fields():
    error_response = ApiErrorResponse(Error=ApiErrorEnum.BADREQUEST)
    assert error_response.context is None
    assert error_response.description is None

    dict_representation = error_response.to_dict()
    assert "Context" not in dict_representation
    assert "Description" not in dict_representation

def test_api_error_enum_values():
    assert ApiErrorEnum.AUTHENTICATIONFAILED.value == "AuthenticationFailed"
    assert ApiErrorEnum.NOTFOUND.value == "NotFound"
    assert ApiErrorEnum.EMBEDDINGSGENERATIONFAILED.value == "EmbeddingsGenerationFailed"

def test_api_error_enum_from_json():
    json_str = '"NoObjectData"'
    enum_value = ApiErrorEnum.from_json(json_str)
    assert enum_value == ApiErrorEnum.NOOBJECTDATA

