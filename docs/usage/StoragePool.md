# StoragePool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional]
**guid** | **str** | GUID | [optional]
**tenant_guid** | **str** |  | [optional]
**encryption_key_guid** | **str** |  | [optional]
**name** | **str** |  | [optional]
**provider** | **str** |  | [optional]
**write_mode** | [**ObjectWriteModeEnum**](ObjectWriteModeEnum.md) | Object Write Mode | [optional]
**use_ssl** | **bool** | Enable or disable SSL | [optional] [default to False]
**endpoint** | **str** |  | [optional]
**access_key** | **str** |  | [optional]
**secret_key** | **str** |  | [optional]
**aws_region** | **str** |  | [optional]
**aws_bucket** | **str** |  | [optional]
**aws_base_domain** | **str** |  | [optional]
**aws_base_url** | **str** |  | [optional]
**disk_directory** | **str** |  | [optional]
**azure_account** | **str** |  | [optional]
**azure_container** | **str** |  | [optional]
**compress** | [**CompressionTypeEnum**](CompressionTypeEnum.md) | Compression Type | [optional]
**enable_read_caching** | **bool** | Enable or disable read caching | [optional] [default to False]
**date_time** | **datetime** |  | [optional]

## Example

```python
from viewio_sdk.models.storage_pool import StoragePool

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePool from a JSON string
storage_pool_instance = StoragePool.from_json(json)
# print the JSON string representation of the object
print(StoragePool.to_json())

# convert the object into a dict
storage_pool_dict = storage_pool_instance.to_dict()
# create an instance of StoragePool from a dict
storage_pool_from_dict = StoragePool.from_dict(storage_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
