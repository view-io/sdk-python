from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
    UpdatableAPIResource,
)
from ...models.webhook_target import WebhookTargetModel


class WebhookTarget(
    ExistsAPIResource,
    CreateableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    UpdatableAPIResource,
    DeletableAPIResource,
):
    RESOURCE_NAME: str = "webhooktargets"
    MODEL = WebhookTargetModel
