from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
    RetrievableStatisticsMixin,
)
from ...models.collection import CollectionModel
from ...models.collection_statistics import CollectionStatisticsModel


class Collection(
    ExistsAPIResource,
    CreateableAPIResource,
    RetrievableAPIResource,
    RetrievableStatisticsMixin,
    AllRetrievableAPIResource,
    DeletableAPIResource,
):
    RESOURCE_NAME: str = "collections"
    MODEL = CollectionModel
    STATS_MODEL = CollectionStatisticsModel

    @classmethod
    def retrieve_top_terms(cls, resource_guid, max_keys=10):
        """Retrieve the top terms from a collection.

        Args:
            resource_guid (str): The GUID of the collection to retrieve top terms from.
            max_keys (int, optional): Maximum number of top terms to return. Defaults to 10.

        Returns:
            The response containing the top terms from the specified collection.
        """
        cls.PARENT_RESOURCE = "collections"
        cls.PARENT_ID_PARAM = "collection_guid"
        cls.RESOURCE_NAME = "topterms"
        kwargs = {
            "collection_guid": resource_guid,
            "resource_guid": "",
            "max-keys": max_keys,
        }

        return super().retrieve(**kwargs)
