# viewio_sdk.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_for_access_token**](AuthApi.md#login_for_access_token) | **POST** /token | Login For Access Token


# **login_for_access_token**
> Token login_for_access_token(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)

Login For Access Token

### Example


```python
import viewio_sdk
from viewio_sdk.models.token import Token
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.AuthApi(api_client)
    username = 'username_example' # str |
    password = 'password_example' # str |
    grant_type = 'grant_type_example' # str |  (optional)
    scope = '' # str |  (optional) (default to '')
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Login For Access Token
        api_response = api_instance.login_for_access_token(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
        print("The response of AuthApi->login_for_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->login_for_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  |
 **password** | **str**|  |
 **grant_type** | **str**|  | [optional]
 **scope** | **str**|  | [optional] [default to &#39;&#39;]
 **client_id** | **str**|  | [optional]
 **client_secret** | **str**|  | [optional]

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | 400 Error Responses |  -  |
**401** | 401 Error Responses |  -  |
**404** | 404 Error Responses |  -  |
**409** | 409 Error Responses |  -  |
**413** | 413 Error Responses |  -  |
**422** | Validation Error |  -  |
**500** | 500 Error Responses |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
