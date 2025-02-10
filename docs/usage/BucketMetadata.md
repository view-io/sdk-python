# BucketMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional]
**guid** | **str** |  | [optional]
**tenant_guid** | **str** |  | [optional]
**pool_guid** | **str** |  | [optional]
**owner_guid** | **str** |  | [optional]
**category** | [**BucketCategoryEnum**](BucketCategoryEnum.md) |  | [optional]
**name** | **str** |  | [optional] [default to '']
**region_string** | **str** |  | [optional] [default to 'us-west-1']
**versioning** | **bool** |  | [optional] [default to True]
**retention_minutes** | **int** |  | [optional]
**max_upload_size** | **int** |  | [optional]
**max_multipart_upload_seconds** | **int** |  | [optional] [default to 604800]
**last_access_utc** | **datetime** |  | [optional]
**created_utc** | **datetime** |  | [optional]
**owner** | [**UserMaster**](UserMaster.md) |  | [optional]

## Example

```python
from viewio_sdk.models.bucket_metadata import BucketMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of BucketMetadata from a JSON string
bucket_metadata_instance = BucketMetadata.from_json(json)
# print the JSON string representation of the object
print(BucketMetadata.to_json())

# convert the object into a dict
bucket_metadata_dict = bucket_metadata_instance.to_dict()
# create an instance of BucketMetadata from a dict
bucket_metadata_from_dict = BucketMetadata.from_dict(bucket_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
