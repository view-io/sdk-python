# Node


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional]
**guid** | **str** |  | [optional]
**name** | **str** |  | [optional]
**hostname** | **str** |  | [optional] [default to 'localhost']
**instance_type** | [**SoftwareInstanceTypeEnum**](SoftwareInstanceTypeEnum.md) |  | [optional]
**last_start_utc** | **datetime** |  | [optional]
**created_utc** | **datetime** |  | [optional]

## Example

```python
from viewio_sdk.models.node import Node

# TODO update the JSON string below
json = "{}"
# create an instance of Node from a JSON string
node_instance = Node.from_json(json)
# print the JSON string representation of the object
print(Node.to_json())

# convert the object into a dict
node_dict = node_instance.to_dict()
# create an instance of Node from a dict
node_from_dict = Node.from_dict(node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
