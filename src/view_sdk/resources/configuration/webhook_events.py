from ...mixins import (
    AllRetrievableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
    EnumerableAPIResource,
)
from ...models.webhook_event import WebhookEventModel


class WebhookEvent(
    ExistsAPIResource, RetrievableAPIResource, AllRetrievableAPIResource, EnumerableAPIResource
):
    RESOURCE_NAME: str = "webhookevents"
    MODEL = WebhookEventModel
