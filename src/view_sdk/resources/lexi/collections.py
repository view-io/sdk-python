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
from ...models.enumeration_query import EnumerationQueryModel


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
    
    @classmethod
    def enumerate_documents(cls, resource_guid, data: EnumerationQueryModel):
        """Enumerate the documents in a collection.

        Args:
            resource_guid (str): The GUID of the collection to enumerate documents from.
        """
        cls.PARENT_RESOURCE = "collections"
        cls.PARENT_ID_PARAM = "collection_guid"
        cls.RESOURCE_NAME = "documents"
        cls.QUERY_PARAMS = {
            "enumerate": None,
        }
        cls.CREATE_METHOD = "POST"
        cls.MODEL = None
        return super().create(collection_guid=resource_guid, _data=data)
    
    @classmethod
    def search(cls, resource_guid, include_data=False, include_top_terms=False, emit_results=False, **kwargs):
        """Search a collection.

        Args:
            resource_guid (str): The GUID of the collection to search.
            **kwargs: Additional keyword arguments to pass to the search request.
        """
        cls.PARENT_RESOURCE = "collections"
        cls.PARENT_ID_PARAM = "collection_guid"
        cls.RESOURCE_NAME = "documents"
        cls.CREATE_METHOD = "POST"
        cls.QUERY_PARAMS = {
            "search": None,
        }

        if include_data:
            cls.QUERY_PARAMS = {
                "search": None,
                "incldata": None,
            }
        elif include_top_terms:
            cls.QUERY_PARAMS = {
                "search": None,
                "incltopterms": None,
            }
        elif emit_results:
            cls.QUERY_PARAMS = {
                "search": None,
                "async": None,
            }
        cls.MODEL = None
        return super().create(collection_guid=resource_guid, _data=kwargs)
