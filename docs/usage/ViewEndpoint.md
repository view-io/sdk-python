# ViewEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | [optional]
**tenant_guid** | **str** |  | [optional]
**owner_guid** | **str** |  | [optional]
**name** | **str** |  | [optional] [default to 'My View endpoint']
**use_ssl** | **bool** |  | [optional] [default to False]
**s3_url** | **str** |  | [optional] [default to 'http://localhost:8002/']
**s3_uri** | **str** |  | [optional] [default to 'http://localhost:8002/']
**s3_base_url** | **str** |  | [optional] [default to 'http://localhost:8002/{bucket}/{key}']
**rest_url** | **str** |  | [optional] [default to 'http://localhost:8001/']
**bucket_name** | **str** |  | [optional] [default to 'data']
**region** | **str** |  | [optional] [default to 'us-west-1']
**access_key** | **str** |  | [optional]
**secret_key** | **str** |  | [optional]
**api_key** | **str** |  | [optional]
**created_utc** | **datetime** |  | [optional]

## Example

```python
from viewio_sdk.models.view_endpoint import ViewEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of ViewEndpoint from a JSON string
view_endpoint_instance = ViewEndpoint.from_json(json)
# print the JSON string representation of the object
print(ViewEndpoint.to_json())

# convert the object into a dict
view_endpoint_dict = view_endpoint_instance.to_dict()
# create an instance of ViewEndpoint from a dict
view_endpoint_from_dict = ViewEndpoint.from_dict(view_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
