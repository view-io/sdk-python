from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
    UpdatableAPIResource,
    EnumerableAPIResource,
)
from ...models.vector_repository import VectorRepositoryModel


class VectorRepository(
    ExistsAPIResource,
    CreateableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    UpdatableAPIResource,
    DeletableAPIResource,
    EnumerableAPIResource,
):
    RESOURCE_NAME: str = "vectorrepositories"
    MODEL = VectorRepositoryModel
