# viewio_sdk.ConfigurationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bucket**](ConfigurationApi.md#create_bucket) | **PUT** /v1.0/tenants/{tenant_guid}/buckets/ | Create Bucket
[**create_collection**](ConfigurationApi.md#create_collection) | **PUT** /v1.0/tenants/{tenant_guid}/collections/ | Create Collection
[**create_credential**](ConfigurationApi.md#create_credential) | **PUT** /v1.0/tenants/{tenant_guid}/credentials/ | Create Credential
[**create_data_repository**](ConfigurationApi.md#create_data_repository) | **PUT** /v1.0/tenants/{tenant_guid}/datarepositories/ | Create Data Repository
[**create_embeddings_rule**](ConfigurationApi.md#create_embeddings_rule) | **PUT** /v1.0/tenants/{tenant_guid}/embeddingsrules/ | Create Embeddings Rule
[**create_encryption_key**](ConfigurationApi.md#create_encryption_key) | **PUT** /v1.0/tenants/{tenant_guid}/encryptionkeys/ | Create Encryption Key
[**create_graph_repository**](ConfigurationApi.md#create_graph_repository) | **PUT** /v1.0/tenants/{tenant_guid}/graphrepositories/ | Create Graph Repository
[**create_metadata_rule**](ConfigurationApi.md#create_metadata_rule) | **PUT** /v1.0/tenants/{tenant_guid}/metadatarules/ | Create Metadata Rule
[**create_node**](ConfigurationApi.md#create_node) | **PUT** /v1.0/nodes/ | Create Node
[**create_object_lock**](ConfigurationApi.md#create_object_lock) | **PUT** /v1.0/tenants/{tenant_guid}/objectlocks/ | Create Object Lock
[**create_pool**](ConfigurationApi.md#create_pool) | **PUT** /v1.0/tenants/{tenant_guid}/pools/ | Create Pool
[**create_user**](ConfigurationApi.md#create_user) | **PUT** /v1.0/tenants/{tenant_guid}/users/ | Create User
[**create_vector_repository**](ConfigurationApi.md#create_vector_repository) | **PUT** /v1.0/tenants/{tenant_guid}/vectorrepositories/ | Create Vector Repository
[**create_view_endpoint**](ConfigurationApi.md#create_view_endpoint) | **PUT** /v1.0/tenants/{tenant_guid}/viewendpoints/ | Create View Endpoint
[**create_webhook_rule**](ConfigurationApi.md#create_webhook_rule) | **PUT** /v1.0/tenants/{tenant_guid}/webhookrules/ | Create Webhook Rule
[**create_webhook_target**](ConfigurationApi.md#create_webhook_target) | **PUT** /v1.0/tenants/{tenant_guid}/webhooktargets/ | Create Webhook Target
[**delete_bucket**](ConfigurationApi.md#delete_bucket) | **DELETE** /v1.0/tenants/{tenant_guid}/buckets/{bucket_guid} | Delete Bucket
[**delete_collection**](ConfigurationApi.md#delete_collection) | **DELETE** /v1.0/tenants/{tenant_guid}/collections/{collection_guid} | Delete Collection
[**delete_credential**](ConfigurationApi.md#delete_credential) | **DELETE** /v1.0/tenants/{tenant_guid}/credentials/{credential_guid} | Delete Credential
[**delete_data_repository**](ConfigurationApi.md#delete_data_repository) | **DELETE** /v1.0/tenants/{tenant_guid}/datarepositories/{data_repository_guid} | Delete Data Repository
[**delete_embeddings_rule**](ConfigurationApi.md#delete_embeddings_rule) | **DELETE** /v1.0/tenants/{tenant_guid}/embeddingsrules/{embeddings_rule_guid} | Delete Embeddings Rule
[**delete_encryption_key**](ConfigurationApi.md#delete_encryption_key) | **DELETE** /v1.0/tenants/{tenant_guid}/encryptionkeys/{encryption_key_guid} | Delete Encryption Key
[**delete_graph_repository**](ConfigurationApi.md#delete_graph_repository) | **DELETE** /v1.0/tenants/{tenant_guid}/graphrepositories/{graph_repository_guid} | Delete Graph Repository
[**delete_metadata_rule**](ConfigurationApi.md#delete_metadata_rule) | **DELETE** /v1.0/tenants/{tenant_guid}/metadatarules/{metadata_rule_guid} | Delete Metadata Rule
[**delete_node**](ConfigurationApi.md#delete_node) | **DELETE** /v1.0/nodes/{node_guid} | Delete Node
[**delete_object_lock**](ConfigurationApi.md#delete_object_lock) | **DELETE** /v1.0/tenants/{tenant_guid}/objectlocks/{object_lock_guid} | Delete Object Lock
[**delete_pool**](ConfigurationApi.md#delete_pool) | **DELETE** /v1.0/tenants/{tenant_guid}/pools/{pool_guid} | Delete Pool
[**delete_user**](ConfigurationApi.md#delete_user) | **DELETE** /v1.0/tenants/{tenant_guid}/users/{user_guid} | Delete User
[**delete_vector_repository**](ConfigurationApi.md#delete_vector_repository) | **DELETE** /v1.0/tenants/{tenant_guid}/vectorrepositories/{vector_repository_guid} | Delete Vector Repository
[**delete_view_endpoint**](ConfigurationApi.md#delete_view_endpoint) | **DELETE** /v1.0/tenants/{tenant_guid}/viewendpoints/{view_endpoint_guid} | Delete View Endpoint
[**delete_webhook_rule**](ConfigurationApi.md#delete_webhook_rule) | **DELETE** /v1.0/tenants/{tenant_guid}/webhookrules/{webhook_rule_guid} | Delete Webhook Rule
[**delete_webhook_target**](ConfigurationApi.md#delete_webhook_target) | **DELETE** /v1.0/tenants/{tenant_guid}/webhooktargets/{webhook_target_guid} | Delete Webhook Target
[**exists_bucket**](ConfigurationApi.md#exists_bucket) | **HEAD** /v1.0/tenants/{tenant_guid}/buckets/{bucket_guid} | Exists Bucket
[**exists_collection**](ConfigurationApi.md#exists_collection) | **HEAD** /v1.0/tenants/{tenant_guid}/collections/{collection_guid} | Exists Collection
[**exists_credential**](ConfigurationApi.md#exists_credential) | **HEAD** /v1.0/tenants/{tenant_guid}/credentials/{credential_guid} | Exists Credential
[**exists_embeddings_rule**](ConfigurationApi.md#exists_embeddings_rule) | **HEAD** /v1.0/tenants/{tenant_guid}/embeddingsrules/{embeddings_rule_guid} | Exists Embeddings Rule
[**exists_encryption_key**](ConfigurationApi.md#exists_encryption_key) | **HEAD** /v1.0/tenants/{tenant_guid}/encryptionkeys/{encryption_key_guid} | Exists Encryption Key
[**exists_graph_repository**](ConfigurationApi.md#exists_graph_repository) | **HEAD** /v1.0/tenants/{tenant_guid}/graphrepositories/{graph_repository_guid} | Exists Graph Repository
[**exists_metadata_rule**](ConfigurationApi.md#exists_metadata_rule) | **HEAD** /v1.0/tenants/{tenant_guid}/metadatarules/{metadata_rule_guid} | Exists Metadata Rule
[**exists_node**](ConfigurationApi.md#exists_node) | **HEAD** /v1.0/nodes/{node_guid} | Exists Node
[**exists_object_lock**](ConfigurationApi.md#exists_object_lock) | **HEAD** /v1.0/tenants/{tenant_guid}/objectlocks/{object_lock_guid} | Exists Object Lock
[**exists_pool**](ConfigurationApi.md#exists_pool) | **HEAD** /v1.0/tenants/{tenant_guid}/pools/{pool_guid} | Exists Pool
[**exists_user**](ConfigurationApi.md#exists_user) | **HEAD** /v1.0/tenants/{tenant_guid}/users/{user_guid} | Exists User
[**exists_vector_repository**](ConfigurationApi.md#exists_vector_repository) | **HEAD** /v1.0/tenants/{tenant_guid}/vectorrepositories/{vector_repository_guid} | Exists Vector Repository
[**exists_view_endpoint**](ConfigurationApi.md#exists_view_endpoint) | **HEAD** /v1.0/tenants/{tenant_guid}/viewendpoints/{view_endpoint_guid} | Exists View Endpoint
[**exists_webhook_event**](ConfigurationApi.md#exists_webhook_event) | **HEAD** /v1.0/tenants/{tenant_guid}/webhookevents/{webhook_event_guid} | Exists Webhook Event
[**exists_webhook_rule**](ConfigurationApi.md#exists_webhook_rule) | **HEAD** /v1.0/tenants/{tenant_guid}/webhookrules/{webhook_rule_guid} | Exists Webhook Rule
[**exists_webhook_target**](ConfigurationApi.md#exists_webhook_target) | **HEAD** /v1.0/tenants/{tenant_guid}/webhooktargets/{webhook_target_guid} | Exists Webhook Target
[**retrieve_bucket**](ConfigurationApi.md#retrieve_bucket) | **GET** /v1.0/tenants/{tenant_guid}/buckets/{bucket_guid} | Retrieve Bucket
[**retrieve_buckets**](ConfigurationApi.md#retrieve_buckets) | **GET** /v1.0/tenants/{tenant_guid}/buckets/ | Retrieve Buckets
[**retrieve_collection**](ConfigurationApi.md#retrieve_collection) | **GET** /v1.0/tenants/{tenant_guid}/collections/{collection_guid} | Retrieve Collection
[**retrieve_collections**](ConfigurationApi.md#retrieve_collections) | **GET** /v1.0/tenants/{tenant_guid}/collections/ | Retrieve Collections
[**retrieve_credential**](ConfigurationApi.md#retrieve_credential) | **GET** /v1.0/tenants/{tenant_guid}/credentials/{credential_guid} | Retrieve Credential
[**retrieve_credentials**](ConfigurationApi.md#retrieve_credentials) | **GET** /v1.0/tenants/{tenant_guid}/credentials/ | Retrieve Credentials
[**retrieve_data_repositories**](ConfigurationApi.md#retrieve_data_repositories) | **GET** /v1.0/tenants/{tenant_guid}/datarepositories/ | Retrieve Data Repositories
[**retrieve_data_repository**](ConfigurationApi.md#retrieve_data_repository) | **GET** /v1.0/tenants/{tenant_guid}/datarepositories/{data_repository_guid} | Retrieve Data Repository
[**retrieve_embeddings_rule**](ConfigurationApi.md#retrieve_embeddings_rule) | **GET** /v1.0/tenants/{tenant_guid}/embeddingsrules/{embeddings_rule_guid} | Retrieve Embeddings Rule
[**retrieve_embeddings_rules**](ConfigurationApi.md#retrieve_embeddings_rules) | **GET** /v1.0/tenants/{tenant_guid}/embeddingsrules/ | Retrieve Embeddings Rules
[**retrieve_encryption_key**](ConfigurationApi.md#retrieve_encryption_key) | **GET** /v1.0/tenants/{tenant_guid}/encryptionkeys/{encryption_key_guid} | Retrieve Encryption Key
[**retrieve_encryption_keys**](ConfigurationApi.md#retrieve_encryption_keys) | **GET** /v1.0/tenants/{tenant_guid}/encryptionkeys/ | Retrieve Encryption Keys
[**retrieve_graph_repositories**](ConfigurationApi.md#retrieve_graph_repositories) | **GET** /v1.0/tenants/{tenant_guid}/graphrepositories/ | Retrieve Graph Repositories
[**retrieve_graph_repository**](ConfigurationApi.md#retrieve_graph_repository) | **GET** /v1.0/tenants/{tenant_guid}/graphrepositories/{graph_repository_guid} | Retrieve Graph Repository
[**retrieve_metadata_rule**](ConfigurationApi.md#retrieve_metadata_rule) | **GET** /v1.0/tenants/{tenant_guid}/metadatarules/{metadata_rule_guid} | Retrieve Metadata Rule
[**retrieve_metadata_rules**](ConfigurationApi.md#retrieve_metadata_rules) | **GET** /v1.0/tenants/{tenant_guid}/metadatarules/ | Retrieve Metadata Rules
[**retrieve_node**](ConfigurationApi.md#retrieve_node) | **GET** /v1.0/nodes/{node_guid} | Retrieve Node
[**retrieve_nodes**](ConfigurationApi.md#retrieve_nodes) | **GET** /v1.0/nodes/ | Retrieve Nodes
[**retrieve_object_lock**](ConfigurationApi.md#retrieve_object_lock) | **GET** /v1.0/tenants/{tenant_guid}/objectlocks/{object_lock_guid} | Retrieve Object Lock
[**retrieve_object_locks**](ConfigurationApi.md#retrieve_object_locks) | **GET** /v1.0/tenants/{tenant_guid}/objectlocks/ | Retrieve Object Locks
[**retrieve_pool**](ConfigurationApi.md#retrieve_pool) | **GET** /v1.0/tenants/{tenant_guid}/pools/{pool_guid} | Retrieve Pool
[**retrieve_pools**](ConfigurationApi.md#retrieve_pools) | **GET** /v1.0/tenants/{tenant_guid}/pools/ | Retrieve Pools
[**retrieve_tenant**](ConfigurationApi.md#retrieve_tenant) | **GET** /v1.0/tenants/{tenant_guid} | Retrieve Tenant
[**retrieve_user**](ConfigurationApi.md#retrieve_user) | **GET** /v1.0/tenants/{tenant_guid}/users/{user_guid} | Retrieve User
[**retrieve_users**](ConfigurationApi.md#retrieve_users) | **GET** /v1.0/tenants/{tenant_guid}/users/ | Retrieve Users
[**retrieve_vector_repositories**](ConfigurationApi.md#retrieve_vector_repositories) | **GET** /v1.0/tenants/{tenant_guid}/vectorrepositories/ | Retrieve Vector Repositories
[**retrieve_vector_repository**](ConfigurationApi.md#retrieve_vector_repository) | **GET** /v1.0/tenants/{tenant_guid}/vectorrepositories/{vector_repository_guid} | Retrieve Vector Repository
[**retrieve_view_endpoint**](ConfigurationApi.md#retrieve_view_endpoint) | **GET** /v1.0/tenants/{tenant_guid}/viewendpoints/{view_endpoint_guid} | Retrieve View Endpoint
[**retrieve_view_endpoints**](ConfigurationApi.md#retrieve_view_endpoints) | **GET** /v1.0/tenants/{tenant_guid}/viewendpoints/ | Retrieve View Endpoints
[**retrieve_webhook_event**](ConfigurationApi.md#retrieve_webhook_event) | **GET** /v1.0/tenants/{tenant_guid}/webhookevents/{webhook_event_guid} | Retrieve Webhook Event
[**retrieve_webhook_events**](ConfigurationApi.md#retrieve_webhook_events) | **GET** /v1.0/tenants/{tenant_guid}/webhookevents/ | Retrieve Webhook Events
[**retrieve_webhook_rule**](ConfigurationApi.md#retrieve_webhook_rule) | **GET** /v1.0/tenants/{tenant_guid}/webhookrules/{webhook_rule_guid} | Retrieve Webhook Rule
[**retrieve_webhook_rules**](ConfigurationApi.md#retrieve_webhook_rules) | **GET** /v1.0/tenants/{tenant_guid}/webhookrules/ | Retrieve Webhook Rules
[**retrieve_webhook_target**](ConfigurationApi.md#retrieve_webhook_target) | **GET** /v1.0/tenants/{tenant_guid}/webhooktargets/{webhook_target_guid} | Retrieve Webhook Target
[**retrieve_webhook_targets**](ConfigurationApi.md#retrieve_webhook_targets) | **GET** /v1.0/tenants/{tenant_guid}/webhooktargets/ | Retrieve Webhook Targets
[**update_bucket**](ConfigurationApi.md#update_bucket) | **PUT** /v1.0/tenants/{tenant_guid}/buckets/{bucket_guid} | Update Bucket
[**update_credential**](ConfigurationApi.md#update_credential) | **PUT** /v1.0/tenants/{tenant_guid}/credentials/{credential_guid} | Update Credential
[**update_embeddings_rule**](ConfigurationApi.md#update_embeddings_rule) | **PUT** /v1.0/tenants/{tenant_guid}/embeddingsrules/{embeddings_rule_guid} | Update Embeddings Rule
[**update_encryption_key**](ConfigurationApi.md#update_encryption_key) | **PUT** /v1.0/tenants/{tenant_guid}/encryptionkeys/{encryption_key_guid} | Update Encryption Key
[**update_graph_repository**](ConfigurationApi.md#update_graph_repository) | **PUT** /v1.0/tenants/{tenant_guid}/graphrepositories/{graph_repository_guid} | Update Graph Repository
[**update_metadata_rule**](ConfigurationApi.md#update_metadata_rule) | **PUT** /v1.0/tenants/{tenant_guid}/metadatarules/{metadata_rule_guid} | Update Metadata Rule
[**update_node**](ConfigurationApi.md#update_node) | **PUT** /v1.0/nodes/{node_guid} | Update Node
[**update_object_lock**](ConfigurationApi.md#update_object_lock) | **PUT** /v1.0/tenants/{tenant_guid}/objectlocks/{object_lock_guid} | Update Object Lock
[**update_pool**](ConfigurationApi.md#update_pool) | **PUT** /v1.0/tenants/{tenant_guid}/pools/{pool_guid} | Update Pool
[**update_tenant**](ConfigurationApi.md#update_tenant) | **PUT** /v1.0/tenants/{tenant_guid} | Update Tenant
[**update_user**](ConfigurationApi.md#update_user) | **PUT** /v1.0/tenants/{tenant_guid}/users/{user_guid} | Update User
[**update_vector_repository**](ConfigurationApi.md#update_vector_repository) | **PUT** /v1.0/tenants/{tenant_guid}/vectorrepositories/{vector_repository_guid} | Update Vector Repository
[**update_view_endpoint**](ConfigurationApi.md#update_view_endpoint) | **PUT** /v1.0/tenants/{tenant_guid}/viewendpoints/{view_endpoint_guid} | Update View Endpoint
[**update_webhook_rule**](ConfigurationApi.md#update_webhook_rule) | **PUT** /v1.0/tenants/{tenant_guid}/webhookrules/{webhook_rule_guid} | Update Webhook Rule
[**update_webhook_target**](ConfigurationApi.md#update_webhook_target) | **PUT** /v1.0/tenants/{tenant_guid}/webhooktargets/{webhook_target_guid} | Update Webhook Target


# **create_bucket**
> BucketMetadata create_bucket(tenant_guid, bucket_metadata)

Create Bucket

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.bucket_metadata import BucketMetadata
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    bucket_metadata = viewio_sdk.BucketMetadata() # BucketMetadata |

    try:
        # Create Bucket
        api_response = api_instance.create_bucket(tenant_guid, bucket_metadata)
        print("The response of ConfigurationApi->create_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->create_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **bucket_metadata** | [**BucketMetadata**](BucketMetadata.md)|  |

### Return type

[**BucketMetadata**](BucketMetadata.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_collection**
> Collection create_collection(tenant_guid, collection)

Create Collection

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.collection import Collection
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    collection = viewio_sdk.Collection() # Collection |

    try:
        # Create Collection
        api_response = api_instance.create_collection(tenant_guid, collection)
        print("The response of ConfigurationApi->create_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->create_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **collection** | [**Collection**](Collection.md)|  |

### Return type

[**Collection**](Collection.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_credential**
> Credential create_credential(tenant_guid, credential)

Create Credential

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.credential import Credential
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    credential = viewio_sdk.Credential() # Credential |

    try:
        # Create Credential
        api_response = api_instance.create_credential(tenant_guid, credential)
        print("The response of ConfigurationApi->create_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->create_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **credential** | [**Credential**](Credential.md)|  |

### Return type

[**Credential**](Credential.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_data_repository**
> DataRepository create_data_repository(tenant_guid, data_repository)

Create Data Repository

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.data_repository import DataRepository
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    data_repository = viewio_sdk.DataRepository() # DataRepository |

    try:
        # Create Data Repository
        api_response = api_instance.create_data_repository(tenant_guid, data_repository)
        print("The response of ConfigurationApi->create_data_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->create_data_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **data_repository** | [**DataRepository**](DataRepository.md)|  |

### Return type

[**DataRepository**](DataRepository.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_embeddings_rule**
> EmbeddingsRule create_embeddings_rule(tenant_guid, embeddings_rule)

Create Embeddings Rule

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.embeddings_rule import EmbeddingsRule
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    embeddings_rule = viewio_sdk.EmbeddingsRule() # EmbeddingsRule |

    try:
        # Create Embeddings Rule
        api_response = api_instance.create_embeddings_rule(tenant_guid, embeddings_rule)
        print("The response of ConfigurationApi->create_embeddings_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->create_embeddings_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **embeddings_rule** | [**EmbeddingsRule**](EmbeddingsRule.md)|  |

### Return type

[**EmbeddingsRule**](EmbeddingsRule.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_encryption_key**
> EncryptionKey create_encryption_key(tenant_guid, encryption_key)

Create Encryption Key

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.encryption_key import EncryptionKey
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    encryption_key = viewio_sdk.EncryptionKey() # EncryptionKey |

    try:
        # Create Encryption Key
        api_response = api_instance.create_encryption_key(tenant_guid, encryption_key)
        print("The response of ConfigurationApi->create_encryption_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->create_encryption_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **encryption_key** | [**EncryptionKey**](EncryptionKey.md)|  |

### Return type

[**EncryptionKey**](EncryptionKey.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_graph_repository**
> GraphRepository create_graph_repository(tenant_guid, graph_repository)

Create Graph Repository

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.graph_repository import GraphRepository
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    graph_repository = viewio_sdk.GraphRepository() # GraphRepository |

    try:
        # Create Graph Repository
        api_response = api_instance.create_graph_repository(tenant_guid, graph_repository)
        print("The response of ConfigurationApi->create_graph_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->create_graph_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **graph_repository** | [**GraphRepository**](GraphRepository.md)|  |

### Return type

[**GraphRepository**](GraphRepository.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_metadata_rule**
> MetadataRule create_metadata_rule(tenant_guid, metadata_rule)

Create Metadata Rule

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.metadata_rule import MetadataRule
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    metadata_rule = viewio_sdk.MetadataRule() # MetadataRule |

    try:
        # Create Metadata Rule
        api_response = api_instance.create_metadata_rule(tenant_guid, metadata_rule)
        print("The response of ConfigurationApi->create_metadata_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->create_metadata_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **metadata_rule** | [**MetadataRule**](MetadataRule.md)|  |

### Return type

[**MetadataRule**](MetadataRule.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_node**
> Node create_node(node)

Create Node

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.node import Node
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    node = viewio_sdk.Node() # Node |

    try:
        # Create Node
        api_response = api_instance.create_node(node)
        print("The response of ConfigurationApi->create_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->create_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | [**Node**](Node.md)|  |

### Return type

[**Node**](Node.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_object_lock**
> ObjectLock create_object_lock(tenant_guid, object_lock)

Create Object Lock

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.object_lock import ObjectLock
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    object_lock = viewio_sdk.ObjectLock() # ObjectLock |

    try:
        # Create Object Lock
        api_response = api_instance.create_object_lock(tenant_guid, object_lock)
        print("The response of ConfigurationApi->create_object_lock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->create_object_lock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **object_lock** | [**ObjectLock**](ObjectLock.md)|  |

### Return type

[**ObjectLock**](ObjectLock.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_pool**
> StoragePool create_pool(tenant_guid, storage_pool)

Create Pool

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.storage_pool import StoragePool
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    storage_pool = viewio_sdk.StoragePool() # StoragePool |

    try:
        # Create Pool
        api_response = api_instance.create_pool(tenant_guid, storage_pool)
        print("The response of ConfigurationApi->create_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->create_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **storage_pool** | [**StoragePool**](StoragePool.md)|  |

### Return type

[**StoragePool**](StoragePool.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_user**
> UserMaster create_user(tenant_guid, user_master)

Create User

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.user_master import UserMaster
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    user_master = viewio_sdk.UserMaster() # UserMaster |

    try:
        # Create User
        api_response = api_instance.create_user(tenant_guid, user_master)
        print("The response of ConfigurationApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **user_master** | [**UserMaster**](UserMaster.md)|  |

### Return type

[**UserMaster**](UserMaster.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_vector_repository**
> VectorRepository create_vector_repository(tenant_guid, vector_repository)

Create Vector Repository

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.vector_repository import VectorRepository
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    vector_repository = viewio_sdk.VectorRepository() # VectorRepository |

    try:
        # Create Vector Repository
        api_response = api_instance.create_vector_repository(tenant_guid, vector_repository)
        print("The response of ConfigurationApi->create_vector_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->create_vector_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **vector_repository** | [**VectorRepository**](VectorRepository.md)|  |

### Return type

[**VectorRepository**](VectorRepository.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_view_endpoint**
> ViewEndpoint create_view_endpoint(tenant_guid, view_endpoint)

Create View Endpoint

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.view_endpoint import ViewEndpoint
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    view_endpoint = viewio_sdk.ViewEndpoint() # ViewEndpoint |

    try:
        # Create View Endpoint
        api_response = api_instance.create_view_endpoint(tenant_guid, view_endpoint)
        print("The response of ConfigurationApi->create_view_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->create_view_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **view_endpoint** | [**ViewEndpoint**](ViewEndpoint.md)|  |

### Return type

[**ViewEndpoint**](ViewEndpoint.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_webhook_rule**
> WebhookRule create_webhook_rule(tenant_guid, webhook_rule)

Create Webhook Rule

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.webhook_rule import WebhookRule
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    webhook_rule = viewio_sdk.WebhookRule() # WebhookRule |

    try:
        # Create Webhook Rule
        api_response = api_instance.create_webhook_rule(tenant_guid, webhook_rule)
        print("The response of ConfigurationApi->create_webhook_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->create_webhook_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **webhook_rule** | [**WebhookRule**](WebhookRule.md)|  |

### Return type

[**WebhookRule**](WebhookRule.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_webhook_target**
> WebhookTarget create_webhook_target(tenant_guid, webhook_target)

Create Webhook Target

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.webhook_target import WebhookTarget
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    webhook_target = viewio_sdk.WebhookTarget() # WebhookTarget |

    try:
        # Create Webhook Target
        api_response = api_instance.create_webhook_target(tenant_guid, webhook_target)
        print("The response of ConfigurationApi->create_webhook_target:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->create_webhook_target: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **webhook_target** | [**WebhookTarget**](WebhookTarget.md)|  |

### Return type

[**WebhookTarget**](WebhookTarget.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **delete_bucket**
> BucketMetadata delete_bucket(tenant_guid, bucket_guid)

Delete Bucket

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.bucket_metadata import BucketMetadata
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    bucket_guid = 'bucket_guid_example' # str |

    try:
        # Delete Bucket
        api_response = api_instance.delete_bucket(tenant_guid, bucket_guid)
        print("The response of ConfigurationApi->delete_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->delete_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **bucket_guid** | **str**|  |

### Return type

[**BucketMetadata**](BucketMetadata.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **delete_collection**
> Collection delete_collection(tenant_guid, collection_guid)

Delete Collection

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.collection import Collection
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    collection_guid = 'collection_guid_example' # str |

    try:
        # Delete Collection
        api_response = api_instance.delete_collection(tenant_guid, collection_guid)
        print("The response of ConfigurationApi->delete_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->delete_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **collection_guid** | **str**|  |

### Return type

[**Collection**](Collection.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **delete_credential**
> Credential delete_credential(tenant_guid, credential_guid)

Delete Credential

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.credential import Credential
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    credential_guid = 'credential_guid_example' # str |

    try:
        # Delete Credential
        api_response = api_instance.delete_credential(tenant_guid, credential_guid)
        print("The response of ConfigurationApi->delete_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->delete_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **credential_guid** | **str**|  |

### Return type

[**Credential**](Credential.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **delete_data_repository**
> DataRepository delete_data_repository(tenant_guid, data_repository_guid)

Delete Data Repository

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.data_repository import DataRepository
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    data_repository_guid = 'data_repository_guid_example' # str |

    try:
        # Delete Data Repository
        api_response = api_instance.delete_data_repository(tenant_guid, data_repository_guid)
        print("The response of ConfigurationApi->delete_data_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->delete_data_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **data_repository_guid** | **str**|  |

### Return type

[**DataRepository**](DataRepository.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **delete_embeddings_rule**
> EmbeddingsRule delete_embeddings_rule(tenant_guid, embeddings_rule_guid)

Delete Embeddings Rule

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.embeddings_rule import EmbeddingsRule
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    embeddings_rule_guid = 'embeddings_rule_guid_example' # str |

    try:
        # Delete Embeddings Rule
        api_response = api_instance.delete_embeddings_rule(tenant_guid, embeddings_rule_guid)
        print("The response of ConfigurationApi->delete_embeddings_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->delete_embeddings_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **embeddings_rule_guid** | **str**|  |

### Return type

[**EmbeddingsRule**](EmbeddingsRule.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **delete_encryption_key**
> EncryptionKey delete_encryption_key(tenant_guid, encryption_key_guid)

Delete Encryption Key

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.encryption_key import EncryptionKey
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    encryption_key_guid = 'encryption_key_guid_example' # str |

    try:
        # Delete Encryption Key
        api_response = api_instance.delete_encryption_key(tenant_guid, encryption_key_guid)
        print("The response of ConfigurationApi->delete_encryption_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->delete_encryption_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **encryption_key_guid** | **str**|  |

### Return type

[**EncryptionKey**](EncryptionKey.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **delete_graph_repository**
> GraphRepository delete_graph_repository(tenant_guid, graph_repository_guid)

Delete Graph Repository

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.graph_repository import GraphRepository
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    graph_repository_guid = 'graph_repository_guid_example' # str |

    try:
        # Delete Graph Repository
        api_response = api_instance.delete_graph_repository(tenant_guid, graph_repository_guid)
        print("The response of ConfigurationApi->delete_graph_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->delete_graph_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **graph_repository_guid** | **str**|  |

### Return type

[**GraphRepository**](GraphRepository.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **delete_metadata_rule**
> MetadataRule delete_metadata_rule(tenant_guid, metadata_rule_guid)

Delete Metadata Rule

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.metadata_rule import MetadataRule
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    metadata_rule_guid = 'metadata_rule_guid_example' # str |

    try:
        # Delete Metadata Rule
        api_response = api_instance.delete_metadata_rule(tenant_guid, metadata_rule_guid)
        print("The response of ConfigurationApi->delete_metadata_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->delete_metadata_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **metadata_rule_guid** | **str**|  |

### Return type

[**MetadataRule**](MetadataRule.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **delete_node**
> Node delete_node(node_guid)

Delete Node

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.node import Node
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    node_guid = 'node_guid_example' # str |

    try:
        # Delete Node
        api_response = api_instance.delete_node(node_guid)
        print("The response of ConfigurationApi->delete_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->delete_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_guid** | **str**|  |

### Return type

[**Node**](Node.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **delete_object_lock**
> ObjectLock delete_object_lock(tenant_guid, object_lock_guid)

Delete Object Lock

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.object_lock import ObjectLock
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    object_lock_guid = 'object_lock_guid_example' # str |

    try:
        # Delete Object Lock
        api_response = api_instance.delete_object_lock(tenant_guid, object_lock_guid)
        print("The response of ConfigurationApi->delete_object_lock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->delete_object_lock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **object_lock_guid** | **str**|  |

### Return type

[**ObjectLock**](ObjectLock.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **delete_pool**
> StoragePool delete_pool(tenant_guid, pool_guid)

Delete Pool

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.storage_pool import StoragePool
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    pool_guid = 'pool_guid_example' # str |

    try:
        # Delete Pool
        api_response = api_instance.delete_pool(tenant_guid, pool_guid)
        print("The response of ConfigurationApi->delete_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->delete_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **pool_guid** | **str**|  |

### Return type

[**StoragePool**](StoragePool.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **delete_user**
> UserMaster delete_user(tenant_guid, user_guid)

Delete User

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.user_master import UserMaster
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    user_guid = 'user_guid_example' # str |

    try:
        # Delete User
        api_response = api_instance.delete_user(tenant_guid, user_guid)
        print("The response of ConfigurationApi->delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **user_guid** | **str**|  |

### Return type

[**UserMaster**](UserMaster.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **delete_vector_repository**
> VectorRepository delete_vector_repository(tenant_guid, vector_repository_guid)

Delete Vector Repository

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.vector_repository import VectorRepository
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    vector_repository_guid = 'vector_repository_guid_example' # str |

    try:
        # Delete Vector Repository
        api_response = api_instance.delete_vector_repository(tenant_guid, vector_repository_guid)
        print("The response of ConfigurationApi->delete_vector_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->delete_vector_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **vector_repository_guid** | **str**|  |

### Return type

[**VectorRepository**](VectorRepository.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **delete_view_endpoint**
> ViewEndpoint delete_view_endpoint(tenant_guid, view_endpoint_guid)

Delete View Endpoint

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.view_endpoint import ViewEndpoint
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    view_endpoint_guid = 'view_endpoint_guid_example' # str |

    try:
        # Delete View Endpoint
        api_response = api_instance.delete_view_endpoint(tenant_guid, view_endpoint_guid)
        print("The response of ConfigurationApi->delete_view_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->delete_view_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **view_endpoint_guid** | **str**|  |

### Return type

[**ViewEndpoint**](ViewEndpoint.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **delete_webhook_rule**
> WebhookRule delete_webhook_rule(tenant_guid, webhook_rule_guid)

Delete Webhook Rule

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.webhook_rule import WebhookRule
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    webhook_rule_guid = 'webhook_rule_guid_example' # str |

    try:
        # Delete Webhook Rule
        api_response = api_instance.delete_webhook_rule(tenant_guid, webhook_rule_guid)
        print("The response of ConfigurationApi->delete_webhook_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->delete_webhook_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **webhook_rule_guid** | **str**|  |

### Return type

[**WebhookRule**](WebhookRule.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **delete_webhook_target**
> WebhookTarget delete_webhook_target(tenant_guid, webhook_target_guid)

Delete Webhook Target

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.webhook_target import WebhookTarget
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    webhook_target_guid = 'webhook_target_guid_example' # str |

    try:
        # Delete Webhook Target
        api_response = api_instance.delete_webhook_target(tenant_guid, webhook_target_guid)
        print("The response of ConfigurationApi->delete_webhook_target:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->delete_webhook_target: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **webhook_target_guid** | **str**|  |

### Return type

[**WebhookTarget**](WebhookTarget.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **exists_bucket**
> object exists_bucket(tenant_guid, bucket_guid)

Exists Bucket

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    bucket_guid = 'bucket_guid_example' # str |

    try:
        # Exists Bucket
        api_response = api_instance.exists_bucket(tenant_guid, bucket_guid)
        print("The response of ConfigurationApi->exists_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->exists_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **bucket_guid** | **str**|  |

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **exists_collection**
> object exists_collection(tenant_guid, collection_guid)

Exists Collection

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    collection_guid = 'collection_guid_example' # str |

    try:
        # Exists Collection
        api_response = api_instance.exists_collection(tenant_guid, collection_guid)
        print("The response of ConfigurationApi->exists_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->exists_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **collection_guid** | **str**|  |

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **exists_credential**
> object exists_credential(tenant_guid, credential_guid)

Exists Credential

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    credential_guid = 'credential_guid_example' # str |

    try:
        # Exists Credential
        api_response = api_instance.exists_credential(tenant_guid, credential_guid)
        print("The response of ConfigurationApi->exists_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->exists_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **credential_guid** | **str**|  |

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **exists_embeddings_rule**
> object exists_embeddings_rule(tenant_guid, embeddings_rule_guid)

Exists Embeddings Rule

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    embeddings_rule_guid = 'embeddings_rule_guid_example' # str |

    try:
        # Exists Embeddings Rule
        api_response = api_instance.exists_embeddings_rule(tenant_guid, embeddings_rule_guid)
        print("The response of ConfigurationApi->exists_embeddings_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->exists_embeddings_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **embeddings_rule_guid** | **str**|  |

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **exists_encryption_key**
> object exists_encryption_key(tenant_guid, encryption_key_guid)

Exists Encryption Key

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    encryption_key_guid = 'encryption_key_guid_example' # str |

    try:
        # Exists Encryption Key
        api_response = api_instance.exists_encryption_key(tenant_guid, encryption_key_guid)
        print("The response of ConfigurationApi->exists_encryption_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->exists_encryption_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **encryption_key_guid** | **str**|  |

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **exists_graph_repository**
> object exists_graph_repository(tenant_guid, graph_repository_guid)

Exists Graph Repository

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    graph_repository_guid = 'graph_repository_guid_example' # str |

    try:
        # Exists Graph Repository
        api_response = api_instance.exists_graph_repository(tenant_guid, graph_repository_guid)
        print("The response of ConfigurationApi->exists_graph_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->exists_graph_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **graph_repository_guid** | **str**|  |

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **exists_metadata_rule**
> object exists_metadata_rule(tenant_guid, metadata_rule_guid)

Exists Metadata Rule

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    metadata_rule_guid = 'metadata_rule_guid_example' # str |

    try:
        # Exists Metadata Rule
        api_response = api_instance.exists_metadata_rule(tenant_guid, metadata_rule_guid)
        print("The response of ConfigurationApi->exists_metadata_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->exists_metadata_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **metadata_rule_guid** | **str**|  |

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **exists_node**
> object exists_node(node_guid)

Exists Node

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    node_guid = 'node_guid_example' # str |

    try:
        # Exists Node
        api_response = api_instance.exists_node(node_guid)
        print("The response of ConfigurationApi->exists_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->exists_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_guid** | **str**|  |

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **exists_object_lock**
> object exists_object_lock(tenant_guid, object_lock_guid)

Exists Object Lock

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    object_lock_guid = 'object_lock_guid_example' # str |

    try:
        # Exists Object Lock
        api_response = api_instance.exists_object_lock(tenant_guid, object_lock_guid)
        print("The response of ConfigurationApi->exists_object_lock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->exists_object_lock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **object_lock_guid** | **str**|  |

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **exists_pool**
> object exists_pool(tenant_guid, pool_guid)

Exists Pool

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    pool_guid = 'pool_guid_example' # str |

    try:
        # Exists Pool
        api_response = api_instance.exists_pool(tenant_guid, pool_guid)
        print("The response of ConfigurationApi->exists_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->exists_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **pool_guid** | **str**|  |

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **exists_user**
> object exists_user(tenant_guid, user_guid)

Exists User

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    user_guid = 'user_guid_example' # str |

    try:
        # Exists User
        api_response = api_instance.exists_user(tenant_guid, user_guid)
        print("The response of ConfigurationApi->exists_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->exists_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **user_guid** | **str**|  |

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **exists_vector_repository**
> object exists_vector_repository(tenant_guid, vector_repository_guid)

Exists Vector Repository

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    vector_repository_guid = 'vector_repository_guid_example' # str |

    try:
        # Exists Vector Repository
        api_response = api_instance.exists_vector_repository(tenant_guid, vector_repository_guid)
        print("The response of ConfigurationApi->exists_vector_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->exists_vector_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **vector_repository_guid** | **str**|  |

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **exists_view_endpoint**
> object exists_view_endpoint(tenant_guid, view_endpoint_guid)

Exists View Endpoint

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    view_endpoint_guid = 'view_endpoint_guid_example' # str |

    try:
        # Exists View Endpoint
        api_response = api_instance.exists_view_endpoint(tenant_guid, view_endpoint_guid)
        print("The response of ConfigurationApi->exists_view_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->exists_view_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **view_endpoint_guid** | **str**|  |

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **exists_webhook_event**
> object exists_webhook_event(tenant_guid, webhook_event_guid)

Exists Webhook Event

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    webhook_event_guid = 'webhook_event_guid_example' # str |

    try:
        # Exists Webhook Event
        api_response = api_instance.exists_webhook_event(tenant_guid, webhook_event_guid)
        print("The response of ConfigurationApi->exists_webhook_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->exists_webhook_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **webhook_event_guid** | **str**|  |

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **exists_webhook_rule**
> object exists_webhook_rule(tenant_guid, webhook_rule_guid)

Exists Webhook Rule

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    webhook_rule_guid = 'webhook_rule_guid_example' # str |

    try:
        # Exists Webhook Rule
        api_response = api_instance.exists_webhook_rule(tenant_guid, webhook_rule_guid)
        print("The response of ConfigurationApi->exists_webhook_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->exists_webhook_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **webhook_rule_guid** | **str**|  |

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **exists_webhook_target**
> object exists_webhook_target(tenant_guid, webhook_target_guid)

Exists Webhook Target

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    webhook_target_guid = 'webhook_target_guid_example' # str |

    try:
        # Exists Webhook Target
        api_response = api_instance.exists_webhook_target(tenant_guid, webhook_target_guid)
        print("The response of ConfigurationApi->exists_webhook_target:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->exists_webhook_target: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **webhook_target_guid** | **str**|  |

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_bucket**
> BucketMetadata retrieve_bucket(tenant_guid, bucket_guid)

Retrieve Bucket

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.bucket_metadata import BucketMetadata
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    bucket_guid = 'bucket_guid_example' # str |

    try:
        # Retrieve Bucket
        api_response = api_instance.retrieve_bucket(tenant_guid, bucket_guid)
        print("The response of ConfigurationApi->retrieve_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **bucket_guid** | **str**|  |

### Return type

[**BucketMetadata**](BucketMetadata.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_buckets**
> List[BucketMetadata] retrieve_buckets(tenant_guid)

Retrieve Buckets

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.bucket_metadata import BucketMetadata
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |

    try:
        # Retrieve Buckets
        api_response = api_instance.retrieve_buckets(tenant_guid)
        print("The response of ConfigurationApi->retrieve_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |

### Return type

[**List[BucketMetadata]**](BucketMetadata.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_collection**
> Collection retrieve_collection(tenant_guid, collection_guid)

Retrieve Collection

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.collection import Collection
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    collection_guid = 'collection_guid_example' # str |

    try:
        # Retrieve Collection
        api_response = api_instance.retrieve_collection(tenant_guid, collection_guid)
        print("The response of ConfigurationApi->retrieve_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **collection_guid** | **str**|  |

### Return type

[**Collection**](Collection.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_collections**
> List[Collection] retrieve_collections(tenant_guid)

Retrieve Collections

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.collection import Collection
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |

    try:
        # Retrieve Collections
        api_response = api_instance.retrieve_collections(tenant_guid)
        print("The response of ConfigurationApi->retrieve_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |

### Return type

[**List[Collection]**](Collection.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_credential**
> Credential retrieve_credential(tenant_guid, credential_guid)

Retrieve Credential

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.credential import Credential
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    credential_guid = 'credential_guid_example' # str |

    try:
        # Retrieve Credential
        api_response = api_instance.retrieve_credential(tenant_guid, credential_guid)
        print("The response of ConfigurationApi->retrieve_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **credential_guid** | **str**|  |

### Return type

[**Credential**](Credential.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_credentials**
> List[Credential] retrieve_credentials(tenant_guid)

Retrieve Credentials

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.credential import Credential
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |

    try:
        # Retrieve Credentials
        api_response = api_instance.retrieve_credentials(tenant_guid)
        print("The response of ConfigurationApi->retrieve_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |

### Return type

[**List[Credential]**](Credential.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_data_repositories**
> List[DataRepository] retrieve_data_repositories(tenant_guid)

Retrieve Data Repositories

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.data_repository import DataRepository
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |

    try:
        # Retrieve Data Repositories
        api_response = api_instance.retrieve_data_repositories(tenant_guid)
        print("The response of ConfigurationApi->retrieve_data_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_data_repositories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |

### Return type

[**List[DataRepository]**](DataRepository.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_data_repository**
> DataRepository retrieve_data_repository(tenant_guid, data_repository_guid)

Retrieve Data Repository

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.data_repository import DataRepository
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    data_repository_guid = 'data_repository_guid_example' # str |

    try:
        # Retrieve Data Repository
        api_response = api_instance.retrieve_data_repository(tenant_guid, data_repository_guid)
        print("The response of ConfigurationApi->retrieve_data_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_data_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **data_repository_guid** | **str**|  |

### Return type

[**DataRepository**](DataRepository.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_embeddings_rule**
> EmbeddingsRule retrieve_embeddings_rule(tenant_guid, embeddings_rule_guid)

Retrieve Embeddings Rule

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.embeddings_rule import EmbeddingsRule
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    embeddings_rule_guid = 'embeddings_rule_guid_example' # str |

    try:
        # Retrieve Embeddings Rule
        api_response = api_instance.retrieve_embeddings_rule(tenant_guid, embeddings_rule_guid)
        print("The response of ConfigurationApi->retrieve_embeddings_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_embeddings_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **embeddings_rule_guid** | **str**|  |

### Return type

[**EmbeddingsRule**](EmbeddingsRule.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_embeddings_rules**
> List[EmbeddingsRule] retrieve_embeddings_rules(tenant_guid)

Retrieve Embeddings Rules

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.embeddings_rule import EmbeddingsRule
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |

    try:
        # Retrieve Embeddings Rules
        api_response = api_instance.retrieve_embeddings_rules(tenant_guid)
        print("The response of ConfigurationApi->retrieve_embeddings_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_embeddings_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |

### Return type

[**List[EmbeddingsRule]**](EmbeddingsRule.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_encryption_key**
> EncryptionKey retrieve_encryption_key(tenant_guid, encryption_key_guid)

Retrieve Encryption Key

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.encryption_key import EncryptionKey
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    encryption_key_guid = 'encryption_key_guid_example' # str |

    try:
        # Retrieve Encryption Key
        api_response = api_instance.retrieve_encryption_key(tenant_guid, encryption_key_guid)
        print("The response of ConfigurationApi->retrieve_encryption_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_encryption_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **encryption_key_guid** | **str**|  |

### Return type

[**EncryptionKey**](EncryptionKey.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_encryption_keys**
> List[EncryptionKey] retrieve_encryption_keys(tenant_guid)

Retrieve Encryption Keys

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.encryption_key import EncryptionKey
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |

    try:
        # Retrieve Encryption Keys
        api_response = api_instance.retrieve_encryption_keys(tenant_guid)
        print("The response of ConfigurationApi->retrieve_encryption_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_encryption_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |

### Return type

[**List[EncryptionKey]**](EncryptionKey.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_graph_repositories**
> List[GraphRepository] retrieve_graph_repositories(tenant_guid)

Retrieve Graph Repositories

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.graph_repository import GraphRepository
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |

    try:
        # Retrieve Graph Repositories
        api_response = api_instance.retrieve_graph_repositories(tenant_guid)
        print("The response of ConfigurationApi->retrieve_graph_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_graph_repositories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |

### Return type

[**List[GraphRepository]**](GraphRepository.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_graph_repository**
> GraphRepository retrieve_graph_repository(tenant_guid, graph_repository_guid)

Retrieve Graph Repository

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.graph_repository import GraphRepository
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    graph_repository_guid = 'graph_repository_guid_example' # str |

    try:
        # Retrieve Graph Repository
        api_response = api_instance.retrieve_graph_repository(tenant_guid, graph_repository_guid)
        print("The response of ConfigurationApi->retrieve_graph_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_graph_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **graph_repository_guid** | **str**|  |

### Return type

[**GraphRepository**](GraphRepository.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_metadata_rule**
> MetadataRule retrieve_metadata_rule(tenant_guid, metadata_rule_guid)

Retrieve Metadata Rule

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.metadata_rule import MetadataRule
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    metadata_rule_guid = 'metadata_rule_guid_example' # str |

    try:
        # Retrieve Metadata Rule
        api_response = api_instance.retrieve_metadata_rule(tenant_guid, metadata_rule_guid)
        print("The response of ConfigurationApi->retrieve_metadata_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_metadata_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **metadata_rule_guid** | **str**|  |

### Return type

[**MetadataRule**](MetadataRule.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_metadata_rules**
> List[MetadataRule] retrieve_metadata_rules(tenant_guid)

Retrieve Metadata Rules

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.metadata_rule import MetadataRule
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |

    try:
        # Retrieve Metadata Rules
        api_response = api_instance.retrieve_metadata_rules(tenant_guid)
        print("The response of ConfigurationApi->retrieve_metadata_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_metadata_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |

### Return type

[**List[MetadataRule]**](MetadataRule.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_node**
> Node retrieve_node(node_guid)

Retrieve Node

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.node import Node
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    node_guid = 'node_guid_example' # str |

    try:
        # Retrieve Node
        api_response = api_instance.retrieve_node(node_guid)
        print("The response of ConfigurationApi->retrieve_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_guid** | **str**|  |

### Return type

[**Node**](Node.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_nodes**
> List[Node] retrieve_nodes()

Retrieve Nodes

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.node import Node
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)

    try:
        # Retrieve Nodes
        api_response = api_instance.retrieve_nodes()
        print("The response of ConfigurationApi->retrieve_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_nodes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Node]**](Node.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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
**500** | 500 Error Responses |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_object_lock**
> ObjectLock retrieve_object_lock(tenant_guid, object_lock_guid)

Retrieve Object Lock

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.object_lock import ObjectLock
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    object_lock_guid = 'object_lock_guid_example' # str |

    try:
        # Retrieve Object Lock
        api_response = api_instance.retrieve_object_lock(tenant_guid, object_lock_guid)
        print("The response of ConfigurationApi->retrieve_object_lock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_object_lock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **object_lock_guid** | **str**|  |

### Return type

[**ObjectLock**](ObjectLock.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_object_locks**
> List[ObjectLock] retrieve_object_locks(tenant_guid)

Retrieve Object Locks

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.object_lock import ObjectLock
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |

    try:
        # Retrieve Object Locks
        api_response = api_instance.retrieve_object_locks(tenant_guid)
        print("The response of ConfigurationApi->retrieve_object_locks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_object_locks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |

### Return type

[**List[ObjectLock]**](ObjectLock.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_pool**
> StoragePool retrieve_pool(tenant_guid, pool_guid)

Retrieve Pool

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.storage_pool import StoragePool
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    pool_guid = 'pool_guid_example' # str |

    try:
        # Retrieve Pool
        api_response = api_instance.retrieve_pool(tenant_guid, pool_guid)
        print("The response of ConfigurationApi->retrieve_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **pool_guid** | **str**|  |

### Return type

[**StoragePool**](StoragePool.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_pools**
> List[StoragePool] retrieve_pools(tenant_guid)

Retrieve Pools

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.storage_pool import StoragePool
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |

    try:
        # Retrieve Pools
        api_response = api_instance.retrieve_pools(tenant_guid)
        print("The response of ConfigurationApi->retrieve_pools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_pools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |

### Return type

[**List[StoragePool]**](StoragePool.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_tenant**
> TenantMetadata retrieve_tenant(tenant_guid)

Retrieve Tenant

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.tenant_metadata import TenantMetadata
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |

    try:
        # Retrieve Tenant
        api_response = api_instance.retrieve_tenant(tenant_guid)
        print("The response of ConfigurationApi->retrieve_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |

### Return type

[**TenantMetadata**](TenantMetadata.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_user**
> UserMaster retrieve_user(tenant_guid, user_guid)

Retrieve User

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.user_master import UserMaster
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    user_guid = 'user_guid_example' # str |

    try:
        # Retrieve User
        api_response = api_instance.retrieve_user(tenant_guid, user_guid)
        print("The response of ConfigurationApi->retrieve_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **user_guid** | **str**|  |

### Return type

[**UserMaster**](UserMaster.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_users**
> List[UserMaster] retrieve_users(tenant_guid)

Retrieve Users

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.user_master import UserMaster
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |

    try:
        # Retrieve Users
        api_response = api_instance.retrieve_users(tenant_guid)
        print("The response of ConfigurationApi->retrieve_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |

### Return type

[**List[UserMaster]**](UserMaster.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_vector_repositories**
> List[VectorRepository] retrieve_vector_repositories(tenant_guid)

Retrieve Vector Repositories

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.vector_repository import VectorRepository
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |

    try:
        # Retrieve Vector Repositories
        api_response = api_instance.retrieve_vector_repositories(tenant_guid)
        print("The response of ConfigurationApi->retrieve_vector_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_vector_repositories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |

### Return type

[**List[VectorRepository]**](VectorRepository.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_vector_repository**
> VectorRepository retrieve_vector_repository(tenant_guid, vector_repository_guid)

Retrieve Vector Repository

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.vector_repository import VectorRepository
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    vector_repository_guid = 'vector_repository_guid_example' # str |

    try:
        # Retrieve Vector Repository
        api_response = api_instance.retrieve_vector_repository(tenant_guid, vector_repository_guid)
        print("The response of ConfigurationApi->retrieve_vector_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_vector_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **vector_repository_guid** | **str**|  |

### Return type

[**VectorRepository**](VectorRepository.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_view_endpoint**
> ViewEndpoint retrieve_view_endpoint(tenant_guid, view_endpoint_guid)

Retrieve View Endpoint

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.view_endpoint import ViewEndpoint
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    view_endpoint_guid = 'view_endpoint_guid_example' # str |

    try:
        # Retrieve View Endpoint
        api_response = api_instance.retrieve_view_endpoint(tenant_guid, view_endpoint_guid)
        print("The response of ConfigurationApi->retrieve_view_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_view_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **view_endpoint_guid** | **str**|  |

### Return type

[**ViewEndpoint**](ViewEndpoint.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_view_endpoints**
> List[ViewEndpoint] retrieve_view_endpoints(tenant_guid)

Retrieve View Endpoints

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.view_endpoint import ViewEndpoint
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |

    try:
        # Retrieve View Endpoints
        api_response = api_instance.retrieve_view_endpoints(tenant_guid)
        print("The response of ConfigurationApi->retrieve_view_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_view_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |

### Return type

[**List[ViewEndpoint]**](ViewEndpoint.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_webhook_event**
> WebhookEvent retrieve_webhook_event(tenant_guid, webhook_event_guid)

Retrieve Webhook Event

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.webhook_event import WebhookEvent
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    webhook_event_guid = 'webhook_event_guid_example' # str |

    try:
        # Retrieve Webhook Event
        api_response = api_instance.retrieve_webhook_event(tenant_guid, webhook_event_guid)
        print("The response of ConfigurationApi->retrieve_webhook_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_webhook_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **webhook_event_guid** | **str**|  |

### Return type

[**WebhookEvent**](WebhookEvent.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_webhook_events**
> List[WebhookEvent] retrieve_webhook_events(tenant_guid)

Retrieve Webhook Events

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.webhook_event import WebhookEvent
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |

    try:
        # Retrieve Webhook Events
        api_response = api_instance.retrieve_webhook_events(tenant_guid)
        print("The response of ConfigurationApi->retrieve_webhook_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_webhook_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |

### Return type

[**List[WebhookEvent]**](WebhookEvent.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_webhook_rule**
> WebhookRule retrieve_webhook_rule(tenant_guid, webhook_rule_guid)

Retrieve Webhook Rule

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.webhook_rule import WebhookRule
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    webhook_rule_guid = 'webhook_rule_guid_example' # str |

    try:
        # Retrieve Webhook Rule
        api_response = api_instance.retrieve_webhook_rule(tenant_guid, webhook_rule_guid)
        print("The response of ConfigurationApi->retrieve_webhook_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_webhook_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **webhook_rule_guid** | **str**|  |

### Return type

[**WebhookRule**](WebhookRule.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_webhook_rules**
> List[WebhookRule] retrieve_webhook_rules(tenant_guid)

Retrieve Webhook Rules

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.webhook_rule import WebhookRule
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |

    try:
        # Retrieve Webhook Rules
        api_response = api_instance.retrieve_webhook_rules(tenant_guid)
        print("The response of ConfigurationApi->retrieve_webhook_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_webhook_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |

### Return type

[**List[WebhookRule]**](WebhookRule.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_webhook_target**
> WebhookTarget retrieve_webhook_target(tenant_guid, webhook_target_guid)

Retrieve Webhook Target

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.webhook_target import WebhookTarget
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    webhook_target_guid = 'webhook_target_guid_example' # str |

    try:
        # Retrieve Webhook Target
        api_response = api_instance.retrieve_webhook_target(tenant_guid, webhook_target_guid)
        print("The response of ConfigurationApi->retrieve_webhook_target:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_webhook_target: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **webhook_target_guid** | **str**|  |

### Return type

[**WebhookTarget**](WebhookTarget.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_webhook_targets**
> List[WebhookTarget] retrieve_webhook_targets(tenant_guid)

Retrieve Webhook Targets

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.webhook_target import WebhookTarget
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |

    try:
        # Retrieve Webhook Targets
        api_response = api_instance.retrieve_webhook_targets(tenant_guid)
        print("The response of ConfigurationApi->retrieve_webhook_targets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->retrieve_webhook_targets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |

### Return type

[**List[WebhookTarget]**](WebhookTarget.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **update_bucket**
> BucketMetadata update_bucket(tenant_guid, bucket_guid, bucket_metadata)

Update Bucket

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.bucket_metadata import BucketMetadata
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    bucket_guid = 'bucket_guid_example' # str |
    bucket_metadata = viewio_sdk.BucketMetadata() # BucketMetadata |

    try:
        # Update Bucket
        api_response = api_instance.update_bucket(tenant_guid, bucket_guid, bucket_metadata)
        print("The response of ConfigurationApi->update_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->update_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **bucket_guid** | **str**|  |
 **bucket_metadata** | [**BucketMetadata**](BucketMetadata.md)|  |

### Return type

[**BucketMetadata**](BucketMetadata.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **update_credential**
> Credential update_credential(tenant_guid, credential_guid, credential)

Update Credential

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.credential import Credential
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    credential_guid = 'credential_guid_example' # str |
    credential = viewio_sdk.Credential() # Credential |

    try:
        # Update Credential
        api_response = api_instance.update_credential(tenant_guid, credential_guid, credential)
        print("The response of ConfigurationApi->update_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->update_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **credential_guid** | **str**|  |
 **credential** | [**Credential**](Credential.md)|  |

### Return type

[**Credential**](Credential.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **update_embeddings_rule**
> EmbeddingsRule update_embeddings_rule(tenant_guid, embeddings_rule_guid, embeddings_rule)

Update Embeddings Rule

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.embeddings_rule import EmbeddingsRule
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    embeddings_rule_guid = 'embeddings_rule_guid_example' # str |
    embeddings_rule = viewio_sdk.EmbeddingsRule() # EmbeddingsRule |

    try:
        # Update Embeddings Rule
        api_response = api_instance.update_embeddings_rule(tenant_guid, embeddings_rule_guid, embeddings_rule)
        print("The response of ConfigurationApi->update_embeddings_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->update_embeddings_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **embeddings_rule_guid** | **str**|  |
 **embeddings_rule** | [**EmbeddingsRule**](EmbeddingsRule.md)|  |

### Return type

[**EmbeddingsRule**](EmbeddingsRule.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **update_encryption_key**
> EncryptionKey update_encryption_key(tenant_guid, encryption_key_guid, encryption_key)

Update Encryption Key

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.encryption_key import EncryptionKey
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    encryption_key_guid = 'encryption_key_guid_example' # str |
    encryption_key = viewio_sdk.EncryptionKey() # EncryptionKey |

    try:
        # Update Encryption Key
        api_response = api_instance.update_encryption_key(tenant_guid, encryption_key_guid, encryption_key)
        print("The response of ConfigurationApi->update_encryption_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->update_encryption_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **encryption_key_guid** | **str**|  |
 **encryption_key** | [**EncryptionKey**](EncryptionKey.md)|  |

### Return type

[**EncryptionKey**](EncryptionKey.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **update_graph_repository**
> GraphRepository update_graph_repository(tenant_guid, graph_repository_guid, graph_repository)

Update Graph Repository

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.graph_repository import GraphRepository
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    graph_repository_guid = 'graph_repository_guid_example' # str |
    graph_repository = viewio_sdk.GraphRepository() # GraphRepository |

    try:
        # Update Graph Repository
        api_response = api_instance.update_graph_repository(tenant_guid, graph_repository_guid, graph_repository)
        print("The response of ConfigurationApi->update_graph_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->update_graph_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **graph_repository_guid** | **str**|  |
 **graph_repository** | [**GraphRepository**](GraphRepository.md)|  |

### Return type

[**GraphRepository**](GraphRepository.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **update_metadata_rule**
> MetadataRule update_metadata_rule(tenant_guid, metadata_rule_guid, metadata_rule)

Update Metadata Rule

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.metadata_rule import MetadataRule
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    metadata_rule_guid = 'metadata_rule_guid_example' # str |
    metadata_rule = viewio_sdk.MetadataRule() # MetadataRule |

    try:
        # Update Metadata Rule
        api_response = api_instance.update_metadata_rule(tenant_guid, metadata_rule_guid, metadata_rule)
        print("The response of ConfigurationApi->update_metadata_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->update_metadata_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **metadata_rule_guid** | **str**|  |
 **metadata_rule** | [**MetadataRule**](MetadataRule.md)|  |

### Return type

[**MetadataRule**](MetadataRule.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **update_node**
> Node update_node(node_guid, node)

Update Node

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.node import Node
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    node_guid = 'node_guid_example' # str |
    node = viewio_sdk.Node() # Node |

    try:
        # Update Node
        api_response = api_instance.update_node(node_guid, node)
        print("The response of ConfigurationApi->update_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->update_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_guid** | **str**|  |
 **node** | [**Node**](Node.md)|  |

### Return type

[**Node**](Node.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **update_object_lock**
> ObjectLock update_object_lock(tenant_guid, object_lock_guid, object_lock)

Update Object Lock

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.object_lock import ObjectLock
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    object_lock_guid = 'object_lock_guid_example' # str |
    object_lock = viewio_sdk.ObjectLock() # ObjectLock |

    try:
        # Update Object Lock
        api_response = api_instance.update_object_lock(tenant_guid, object_lock_guid, object_lock)
        print("The response of ConfigurationApi->update_object_lock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->update_object_lock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **object_lock_guid** | **str**|  |
 **object_lock** | [**ObjectLock**](ObjectLock.md)|  |

### Return type

[**ObjectLock**](ObjectLock.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **update_pool**
> StoragePool update_pool(tenant_guid, pool_guid, storage_pool)

Update Pool

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.storage_pool import StoragePool
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    pool_guid = 'pool_guid_example' # str |
    storage_pool = viewio_sdk.StoragePool() # StoragePool |

    try:
        # Update Pool
        api_response = api_instance.update_pool(tenant_guid, pool_guid, storage_pool)
        print("The response of ConfigurationApi->update_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->update_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **pool_guid** | **str**|  |
 **storage_pool** | [**StoragePool**](StoragePool.md)|  |

### Return type

[**StoragePool**](StoragePool.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **update_tenant**
> TenantMetadata update_tenant(tenant_guid, tenant_metadata)

Update Tenant

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.tenant_metadata import TenantMetadata
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    tenant_metadata = viewio_sdk.TenantMetadata() # TenantMetadata |

    try:
        # Update Tenant
        api_response = api_instance.update_tenant(tenant_guid, tenant_metadata)
        print("The response of ConfigurationApi->update_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->update_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **tenant_metadata** | [**TenantMetadata**](TenantMetadata.md)|  |

### Return type

[**TenantMetadata**](TenantMetadata.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **update_user**
> UserMaster update_user(tenant_guid, user_guid, user_master)

Update User

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.user_master import UserMaster
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    user_guid = 'user_guid_example' # str |
    user_master = viewio_sdk.UserMaster() # UserMaster |

    try:
        # Update User
        api_response = api_instance.update_user(tenant_guid, user_guid, user_master)
        print("The response of ConfigurationApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **user_guid** | **str**|  |
 **user_master** | [**UserMaster**](UserMaster.md)|  |

### Return type

[**UserMaster**](UserMaster.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **update_vector_repository**
> VectorRepository update_vector_repository(tenant_guid, vector_repository_guid, vector_repository)

Update Vector Repository

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.vector_repository import VectorRepository
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    vector_repository_guid = 'vector_repository_guid_example' # str |
    vector_repository = viewio_sdk.VectorRepository() # VectorRepository |

    try:
        # Update Vector Repository
        api_response = api_instance.update_vector_repository(tenant_guid, vector_repository_guid, vector_repository)
        print("The response of ConfigurationApi->update_vector_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->update_vector_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **vector_repository_guid** | **str**|  |
 **vector_repository** | [**VectorRepository**](VectorRepository.md)|  |

### Return type

[**VectorRepository**](VectorRepository.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **update_view_endpoint**
> ViewEndpoint update_view_endpoint(tenant_guid, view_endpoint_guid, view_endpoint)

Update View Endpoint

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.view_endpoint import ViewEndpoint
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    view_endpoint_guid = 'view_endpoint_guid_example' # str |
    view_endpoint = viewio_sdk.ViewEndpoint() # ViewEndpoint |

    try:
        # Update View Endpoint
        api_response = api_instance.update_view_endpoint(tenant_guid, view_endpoint_guid, view_endpoint)
        print("The response of ConfigurationApi->update_view_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->update_view_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **view_endpoint_guid** | **str**|  |
 **view_endpoint** | [**ViewEndpoint**](ViewEndpoint.md)|  |

### Return type

[**ViewEndpoint**](ViewEndpoint.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **update_webhook_rule**
> WebhookRule update_webhook_rule(tenant_guid, webhook_rule_guid, webhook_rule)

Update Webhook Rule

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.webhook_rule import WebhookRule
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    webhook_rule_guid = 'webhook_rule_guid_example' # str |
    webhook_rule = viewio_sdk.WebhookRule() # WebhookRule |

    try:
        # Update Webhook Rule
        api_response = api_instance.update_webhook_rule(tenant_guid, webhook_rule_guid, webhook_rule)
        print("The response of ConfigurationApi->update_webhook_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->update_webhook_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **webhook_rule_guid** | **str**|  |
 **webhook_rule** | [**WebhookRule**](WebhookRule.md)|  |

### Return type

[**WebhookRule**](WebhookRule.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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

# **update_webhook_target**
> WebhookTarget update_webhook_target(tenant_guid, webhook_target_guid, webhook_target)

Update Webhook Target

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import viewio_sdk
from viewio_sdk.models.webhook_target import WebhookTarget
from viewio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = viewio_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with viewio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = viewio_sdk.ConfigurationApi(api_client)
    tenant_guid = 'tenant_guid_example' # str |
    webhook_target_guid = 'webhook_target_guid_example' # str |
    webhook_target = viewio_sdk.WebhookTarget() # WebhookTarget |

    try:
        # Update Webhook Target
        api_response = api_instance.update_webhook_target(tenant_guid, webhook_target_guid, webhook_target)
        print("The response of ConfigurationApi->update_webhook_target:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->update_webhook_target: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_guid** | **str**|  |
 **webhook_target_guid** | **str**|  |
 **webhook_target** | [**WebhookTarget**](WebhookTarget.md)|  |

### Return type

[**WebhookTarget**](WebhookTarget.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
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
