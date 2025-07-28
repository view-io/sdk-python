from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    EnumerableAPIResource,
    RetrievableAPIResource,
    UpdatableAPIResource,
)
from ...models.data_repository import DataRepositoryModel


class DataRepository(
    CreateableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    DeletableAPIResource,
    UpdatableAPIResource,
    EnumerableAPIResource,
):
    RESOURCE_NAME: str = "datarepositories"
    MODEL = DataRepositoryModel
