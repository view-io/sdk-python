# MetadataRule


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
**processing_endpoint** | **str** |  | [optional] [default to 'http://localhost:8501/processor']
**cleanup_endpoint** | **str** |  | [optional] [default to 'http://localhost:8501/processor/cleanup']
**type_detector_endpoint** | **str** |  | [optional] [default to 'http://localhost:8501/processor/typedetector']
**semantic_cell_endpoint** | **str** |  | [optional] [default to 'http://localhost:8341/']
**max_chunk_content_length** | **int** |  | [optional] [default to 512]
**shift_size** | **int** |  | [optional] [default to 512]
**udr_endpoint** | **str** |  | [optional] [default to 'http://localhost:8321/']
**data_catalog_type** | [**DataCatalogTypeEnum**](DataCatalogTypeEnum.md) |  | [optional]
**data_catalog_endpoint** | **str** |  | [optional] [default to 'http://localhost:8201/']
**data_catalog_collection** | **str** |  | [optional]
**graph_repository_guid** | **str** |  | [optional]
**top_terms** | **int** |  | [optional] [default to 25]
**case_insensitive** | **bool** |  | [optional] [default to True]
**include_flattened** | **bool** |  | [optional] [default to True]
**target_bucket_guid** | **str** |  | [optional]
**max_content_length** | **int** |  | [optional] [default to 16777216]
**retention_minutes** | **int** |  | [optional]
**created_utc** | **datetime** |  | [optional]

## Example

```python
from viewio_sdk.models.metadata_rule import MetadataRule

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataRule from a JSON string
metadata_rule_instance = MetadataRule.from_json(json)
# print the JSON string representation of the object
print(MetadataRule.to_json())

# convert the object into a dict
metadata_rule_dict = metadata_rule_instance.to_dict()
# create an instance of MetadataRule from a dict
metadata_rule_from_dict = MetadataRule.from_dict(metadata_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
