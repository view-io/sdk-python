# VectorRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | [optional]
**tenant_guid** | **str** |  | [optional]
**name** | **str** |  | [optional] [default to 'My vector repository']
**repository_type** | [**VectorRepositoryTypeEnum**](VectorRepositoryTypeEnum.md) |  | [optional]
**endpoint_url** | **str** |  | [optional]
**api_key** | **str** |  | [optional]
**model** | **str** |  | [optional] [default to 'all-MiniLM-L6-v2']
**dimensionality** | **int** |  | [optional] [default to 384]
**database_hostname** | **str** |  | [optional]
**database_name** | **str** |  | [optional]
**database_table** | **str** |  | [optional]
**database_port** | **int** |  | [optional] [default to 0]
**database_user** | **str** |  | [optional]
**database_password** | **str** |  | [optional]
**prompt_prefix** | **str** |  | [optional] [default to 'Use the following pieces of context to answer the question at the end. Documents are sorted by similarity to the question. If the context is not enough for you to answer the question, politely explain that you don't have relevant context. Do not try to make up an answer.']
**prompt_suffix** | **str** |  | [optional]
**created_utc** | **datetime** |  | [optional]

## Example

```python
from viewio_sdk.models.vector_repository import VectorRepository

# TODO update the JSON string below
json = "{}"
# create an instance of VectorRepository from a JSON string
vector_repository_instance = VectorRepository.from_json(json)
# print the JSON string representation of the object
print(VectorRepository.to_json())

# convert the object into a dict
vector_repository_dict = vector_repository_instance.to_dict()
# create an instance of VectorRepository from a dict
vector_repository_from_dict = VectorRepository.from_dict(vector_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
