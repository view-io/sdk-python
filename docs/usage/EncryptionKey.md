# EncryptionKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | [optional]
**tenant_guid** | **str** |  | [optional]
**owner_guid** | **str** |  | [optional]
**key_base64** | **str** |  | [optional] [default to '']
**key_hex** | **str** |  | [optional] [default to '']
**iv_base64** | **str** |  | [optional] [default to '']
**iv_hex** | **str** |  | [optional] [default to '']
**salt_base64** | **str** |  | [optional] [default to '']
**salt_hex** | **str** |  | [optional] [default to '']
**name** | **str** |  | [optional] [default to '']
**description** | **str** |  | [optional] [default to '']
**created_utc** | **datetime** |  | [optional]

## Example

```python
from viewio_sdk.models.encryption_key import EncryptionKey

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionKey from a JSON string
encryption_key_instance = EncryptionKey.from_json(json)
# print the JSON string representation of the object
print(EncryptionKey.to_json())

# convert the object into a dict
encryption_key_dict = encryption_key_instance.to_dict()
# create an instance of EncryptionKey from a dict
encryption_key_from_dict = EncryptionKey.from_dict(encryption_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
