# ObjectLock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | [optional]
**tenant_guid** | **str** |  | [optional]
**node_guid** | **str** |  | [optional]
**bucket_guid** | **str** |  | [optional]
**owner_guid** | **str** |  | [optional]
**object_guid** | **str** |  | [optional]
**key** | **str** |  | [optional] [default to '']
**version** | **str** |  | [optional] [default to '']
**is_read_lock** | **bool** |  | [optional] [default to False]
**is_write_lock** | **bool** |  | [optional] [default to False]
**created_utc** | **datetime** |  | [optional]

## Example

```python
from viewio_sdk.models.object_lock import ObjectLock

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectLock from a JSON string
object_lock_instance = ObjectLock.from_json(json)
# print the JSON string representation of the object
print(ObjectLock.to_json())

# convert the object into a dict
object_lock_dict = object_lock_instance.to_dict()
# create an instance of ObjectLock from a dict
object_lock_from_dict = ObjectLock.from_dict(object_lock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
