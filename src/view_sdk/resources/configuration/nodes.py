from ...mixins import (
    AllRetrievableAPIResource,
    DeletableAPIResource,
    EnumerableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
)
from ...models.node import NodeModel


class Node(
    ExistsAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    DeletableAPIResource,
    EnumerableAPIResource,
):
    RESOURCE_NAME: str = "nodes"
    MODEL = NodeModel
    REQUIRES_TENANT: bool = False
