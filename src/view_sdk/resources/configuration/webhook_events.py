from ...mixins import (
    AllRetrievableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
)
from ...models.webhook_event import WebhookEventModel


class WebhookEvent(
    ExistsAPIResource, RetrievableAPIResource, AllRetrievableAPIResource
):
    RESOURCE_NAME: str = "webhookevents"
    MODEL = WebhookEventModel
