from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    RetrievableAPIResource,
)
from ...models.data_repository import DataRepositoryModel


class DataRepository(
    CreateableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    DeletableAPIResource,
):
    RESOURCE_NAME: str = "datarepositories"
    MODEL = DataRepositoryModel
