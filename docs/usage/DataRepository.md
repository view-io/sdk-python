# DataRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**guid** | **str** |  | [optional]
**tenant_guid** | **str** |  | [optional]
**owner_guid** | **str** |  | [optional]
**name** | **str** |  | [optional] [default to 'My file repository']
**repository_type** | **str** |  | [optional] [default to 'File']
**use_ssl** | **bool** |  | [optional] [default to False]
**include_subdirectories** | **bool** |  | [optional] [default to True]
**disk_directory** | **str** |  | [optional]
**s3_endpoint_url** | **str** |  | [optional]
**s3_base_url** | **str** |  | [optional]
**s3_access_key** | **str** |  | [optional]
**s3_secret_key** | **str** |  | [optional]
**s3_bucket_name** | **str** |  | [optional]
**s3_region** | **str** |  | [optional]
**azure_endpoint_url** | **str** |  | [optional]
**azure_account_name** | **str** |  | [optional]
**azure_container_name** | **str** |  | [optional]
**azure_access_key** | **str** |  | [optional]
**cifs_hostname** | **str** |  | [optional]
**cifs_username** | **str** |  | [optional]
**cifs_password** | **str** |  | [optional]
**cifs_share_name** | **str** |  | [optional]
**nfs_hostname** | **str** |  | [optional]
**nfs_user_id** | **int** |  | [optional] [default to 0]
**nfs_group_id** | **int** |  | [optional] [default to 0]
**nfs_share_name** | **str** |  | [optional]
**nfs_version** | **str** |  | [optional]
**created_utc** | **datetime** |  | [optional]

## Example

```python
from viewio_sdk.models.data_repository import DataRepository

# TODO update the JSON string below
json = "{}"
# create an instance of DataRepository from a JSON string
data_repository_instance = DataRepository.from_json(json)
# print the JSON string representation of the object
print(DataRepository.to_json())

# convert the object into a dict
data_repository_dict = data_repository_instance.to_dict()
# create an instance of DataRepository from a dict
data_repository_from_dict = DataRepository.from_dict(data_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
