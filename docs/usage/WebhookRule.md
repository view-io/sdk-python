# WebhookRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | [optional]
**tenant_guid** | **str** |  | [optional]
**target_guid** | **str** |  | [optional]
**name** | **str** |  | [optional]
**event_type** | [**WebhookEventTypeEnum**](WebhookEventTypeEnum.md) |  | [optional]
**max_attempts** | **int** |  | [optional] [default to 10]
**retry_interval_ms** | **int** |  | [optional] [default to 30000]
**timeout_ms** | **int** |  | [optional] [default to 60000]
**created_utc** | **datetime** |  | [optional]

## Example

```python
from viewio_sdk.models.webhook_rule import WebhookRule

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRule from a JSON string
webhook_rule_instance = WebhookRule.from_json(json)
# print the JSON string representation of the object
print(WebhookRule.to_json())

# convert the object into a dict
webhook_rule_dict = webhook_rule_instance.to_dict()
# create an instance of WebhookRule from a dict
webhook_rule_from_dict = WebhookRule.from_dict(webhook_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
