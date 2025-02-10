# TenantMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional]
**guid** | **str** |  | [optional]
**parent_guid** | **str** |  | [optional]
**name** | **str** |  | [optional] [default to '']
**region** | **str** |  | [optional] [default to 'us-west-1']
**s3_base_domain** | **str** |  | [optional] [default to '']
**rest_base_domain** | **str** |  | [optional] [default to '']
**default_pool_guid** | **str** |  | [optional] [default to '']
**active** | **bool** |  | [optional] [default to True]
**created_utc** | **datetime** |  | [optional]

## Example

```python
from viewio_sdk.models.tenant_metadata import TenantMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TenantMetadata from a JSON string
tenant_metadata_instance = TenantMetadata.from_json(json)
# print the JSON string representation of the object
print(TenantMetadata.to_json())

# convert the object into a dict
tenant_metadata_dict = tenant_metadata_instance.to_dict()
# create an instance of TenantMetadata from a dict
tenant_metadata_from_dict = TenantMetadata.from_dict(tenant_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
