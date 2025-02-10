# UserMaster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | [optional]
**tenant_guid** | **str** |  | [optional]
**first_name** | **str** |  | [optional] [default to '']
**last_name** | **str** |  | [optional] [default to '']
**full_name** | **str** |  | [optional]
**notes** | **str** |  | [optional]
**email** | **str** |  | [optional] [default to '']
**password_sha256** | **str** |  | [optional] [default to '']
**active** | **bool** |  | [optional] [default to True]
**created_utc** | **datetime** |  | [optional]

## Example

```python
from viewio_sdk.models.user_master import UserMaster

# TODO update the JSON string below
json = "{}"
# create an instance of UserMaster from a JSON string
user_master_instance = UserMaster.from_json(json)
# print the JSON string representation of the object
print(UserMaster.to_json())

# convert the object into a dict
user_master_dict = user_master_instance.to_dict()
# create an instance of UserMaster from a dict
user_master_from_dict = UserMaster.from_dict(user_master_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
