from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
    UpdatableAPIResource,
    EnumerableAPIResource,
)
from ...models.graph_repository import GraphRepositoryModel


class GraphRepository(
    ExistsAPIResource,
    CreateableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    UpdatableAPIResource,
    DeletableAPIResource,
    EnumerableAPIResource,
):
    RESOURCE_NAME: str = "graphrepositories"
    MODEL = GraphRepositoryModel
