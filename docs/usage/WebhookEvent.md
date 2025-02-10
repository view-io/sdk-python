# WebhookEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | [optional]
**tenant_guid** | **str** |  | [optional]
**target_guid** | **str** |  | [optional]
**rule_guid** | **str** |  | [optional]
**event_type** | [**WebhookEventTypeEnum**](WebhookEventTypeEnum.md) |  | [optional]
**content_length** | **int** |  | [optional] [default to 0]
**timeout_ms** | **int** |  | [optional] [default to 60000]
**url** | **str** |  |
**content_type** | **str** |  | [optional] [default to 'application/json']
**expect_status** | **int** |  | [optional] [default to 200]
**retry_interval_ms** | **int** |  | [optional] [default to 10000]
**attempt** | **int** |  | [optional] [default to 0]
**max_attempts** | **int** |  | [optional] [default to 5]
**http_status** | **int** |  | [optional] [default to 0]
**created_utc** | **datetime** |  | [optional]
**added_utc** | **datetime** |  | [optional]
**last_attempt_utc** | **datetime** |  | [optional]
**next_attempt_utc** | **datetime** |  | [optional]
**last_failure_utc** | **datetime** |  | [optional]
**success_utc** | **datetime** |  | [optional]
**failed_utc** | **datetime** |  | [optional]

## Example

```python
from viewio_sdk.models.webhook_event import WebhookEvent

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEvent from a JSON string
webhook_event_instance = WebhookEvent.from_json(json)
# print the JSON string representation of the object
print(WebhookEvent.to_json())

# convert the object into a dict
webhook_event_dict = webhook_event_instance.to_dict()
# create an instance of WebhookEvent from a dict
webhook_event_from_dict = WebhookEvent.from_dict(webhook_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
