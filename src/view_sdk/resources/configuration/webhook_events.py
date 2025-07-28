from ...mixins import (
    AllRetrievableAPIResource,
    EnumerableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
)
from ...models.webhook_event import WebhookEventModel


class WebhookEvent(
    ExistsAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    EnumerableAPIResource,
):
    RESOURCE_NAME: str = "webhookevents"
    MODEL = WebhookEventModel
