# WebhookTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | [optional]
**tenant_guid** | **str** |  | [optional]
**name** | **str** |  | [optional] [default to 'My webhook target']
**url** | **str** |  | [optional]
**content_type** | **str** |  | [optional] [default to 'application/json']
**expect_status** | **int** |  | [optional] [default to 200]
**created_utc** | **datetime** |  | [optional]

## Example

```python
from viewio_sdk.models.webhook_target import WebhookTarget

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTarget from a JSON string
webhook_target_instance = WebhookTarget.from_json(json)
# print the JSON string representation of the object
print(WebhookTarget.to_json())

# convert the object into a dict
webhook_target_dict = webhook_target_instance.to_dict()
# create an instance of WebhookTarget from a dict
webhook_target_from_dict = WebhookTarget.from_dict(webhook_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
