# GraphRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | [optional]
**tenant_guid** | **str** |  | [optional]
**name** | **str** |  | [optional] [default to 'My vector repository']
**repository_type** | [**GraphRepositoryTypeEnum**](GraphRepositoryTypeEnum.md) |  | [optional]
**endpoint_url** | **str** |  | [optional]
**api_key** | **str** |  | [optional]
**username** | **str** |  | [optional]
**password** | **str** |  | [optional]
**hostname** | **str** |  | [optional]
**port** | **int** |  | [optional] [default to 0]
**graph_identifier** | **str** |  | [optional]
**created_utc** | **datetime** |  | [optional]

## Example

```python
from viewio_sdk.models.graph_repository import GraphRepository

# TODO update the JSON string below
json = "{}"
# create an instance of GraphRepository from a JSON string
graph_repository_instance = GraphRepository.from_json(json)
# print the JSON string representation of the object
print(GraphRepository.to_json())

# convert the object into a dict
graph_repository_dict = graph_repository_instance.to_dict()
# create an instance of GraphRepository from a dict
graph_repository_from_dict = GraphRepository.from_dict(graph_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
