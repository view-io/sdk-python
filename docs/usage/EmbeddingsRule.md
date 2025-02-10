# EmbeddingsRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | [optional]
**tenant_guid** | **str** |  | [optional]
**bucket_guid** | **str** |  | [optional]
**owner_guid** | **str** |  | [optional]
**name** | **str** |  | [optional]
**content_type** | **str** |  | [optional] [default to 'text/plain']
**prefix** | **str** |  | [optional]
**suffix** | **str** |  | [optional]
**target_bucket_guid** | **str** |  | [optional]
**graph_repository_guid** | **str** |  | [optional]
**vector_repository_guid** | **str** |  | [optional]
**data_flow_endpoint** | **str** |  | [optional] [default to 'http://localhost:8501/processor']
**embeddings_generator** | [**EmbeddingsGeneratorEnum**](EmbeddingsGeneratorEnum.md) |  | [optional]
**generator_url** | **str** |  | [optional] [default to 'http://localhost:8301/']
**generator_api_key** | **str** |  | [optional]
**batch_size** | **int** |  | [optional] [default to 16]
**max_generator_tasks** | **int** |  | [optional] [default to 16]
**max_retries** | **int** |  | [optional] [default to 3]
**max_failures** | **int** |  | [optional] [default to 3]
**vector_store_url** | **str** |  | [optional] [default to 'http://localhost:8311/']
**max_content_length** | **int** |  | [optional] [default to 16777216]
**retention_minutes** | **int** |  | [optional]
**created_utc** | **datetime** |  | [optional]

## Example

```python
from viewio_sdk.models.embeddings_rule import EmbeddingsRule

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddingsRule from a JSON string
embeddings_rule_instance = EmbeddingsRule.from_json(json)
# print the JSON string representation of the object
print(EmbeddingsRule.to_json())

# convert the object into a dict
embeddings_rule_dict = embeddings_rule_instance.to_dict()
# create an instance of EmbeddingsRule from a dict
embeddings_rule_from_dict = EmbeddingsRule.from_dict(embeddings_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
