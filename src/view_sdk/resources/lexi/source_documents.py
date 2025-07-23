from typing import Type

from pydantic import BaseModel

from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    EnumerableAPIResourceWithData,
    ExistsAPIResource,
    RetrievableAPIResource,
    RetrievableStatisticsMixin,
)
from ...models.collection_search_request import CollectionSearchRequestModel
from ...models.enumeration_query import EnumerationQueryModel
from ...models.enumeration_result import EnumerationResultModel
from ...models.search_result import SearchResultModel
from ...models.source_document import SourceDocumentModel
from ...models.source_document_statistics import SourceDocumentStatisticsModel
from ...sdk_configuration import get_client
from ...utils.url_helper import _get_url_v1


class SourceDocument(
    ExistsAPIResource,
    CreateableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    DeletableAPIResource,
    RetrievableStatisticsMixin,
    EnumerableAPIResourceWithData,
):
    """
    API resource class for managing source documents within collections.

    This class provides methods for creating, retrieving, deleting, and enumerating
    source documents. It also supports retrieving document statistics and checking
    document existence.

    Attributes:
        RESOURCE_NAME (str): The API resource name for documents.
        MODEL (Type[BaseModel]): The Pydantic model for source documents.
        STATS_MODEL (Type[BaseModel]): The Pydantic model for document statistics.
        SERVICE (Service): The service type (LEXI).
        PARENT_RESOURCE (str): The parent resource name (collections).
        PARENT_ID_PARAM (str): The parameter name for collection GUID.
        ENUMERATE_METHOD (str): The HTTP method for enumeration requests.
        ENUMERABLE_REQUEST_MODEL (Type[BaseModel]): The model for enumeration queries.
    """

    RESOURCE_NAME: str = "documents"
    MODEL = SourceDocumentModel
    STATS_MODEL = SourceDocumentStatisticsModel

    PARENT_RESOURCE: str = "collections"
    PARENT_ID_PARAM: str = "collection_guid"

    ENUMERATE_METHOD: str = "POST"
    ENUMERABLE_REQUEST_MODEL: Type[BaseModel] = EnumerationQueryModel

    @classmethod
    def retrieve_top_terms(
        cls, collection_guid: str, resource_guid: str, max_keys: int = 10
    ) -> list[str]:
        """
        Retrieves the top terms from a collection.

        Args:
            collection_guid (str): The GUID of the collection to retrieve top terms from.
            document_guid (str): The GUID of the document to retrieve top terms from.


        Returns:
            list[str]: A list of top terms.
        """
        cls.QUERY_PARAMS = {"max-keys": max_keys}
        return super().retrieve(
            resource_guid + "/topterms", collection_guid=collection_guid
        )

    @classmethod
    def retrieve(
        cls, resource_guid: str, collection_guid: str, include_data: bool = False
    ) -> "BaseModel":
        """
        Retrieves a source document.

        Args:
            resource_guid: The ID of the source document to retrieve.
            collection_guid: The ID of the collection to which the source document belongs.
            include_data: Whether to include the source document data in the response.

        Returns:
            The retrieved source document.
        """
        kwargs = {"collection_guid": collection_guid}
        if include_data:
            kwargs["incldata"] = None
        return super().retrieve(resource_guid, **kwargs)

    @classmethod
    def create(cls, collection_guid: str, **data) -> "BaseModel":
        """
        Creates a new source document in the specified collection.

        Args:
            collection_guid (str): The GUID of the collection to create the document in.
            **data: Additional data for the document creation, such as content and metadata.

        Returns:
            BaseModel: The created source document instance.

        Raises:
            ValueError: If required fields are missing or invalid.
        """
        cls.MODEL = None
        return super().create(collection_guid=collection_guid, **data)

    @classmethod
    def retrieve_all(cls, collection_guid: str) -> list["BaseModel"]:
        """
        Retrieves all source documents from a specific collection.

        Args:
            collection_guid (str): The GUID of the collection to retrieve documents from.

        Returns:
            list[BaseModel]: A list of source document instances.

        Raises:
            ValueError: If the collection_guid is invalid or missing.
        """
        return super().retrieve_all(collection_guid=collection_guid)

    @classmethod
    def delete(cls, resource_guid: str, collection_guid: str) -> bool:
        """
        Deletes a source document from a collection.

        Args:
            resource_guid (str): The GUID of the document to delete.
            collection_guid (str): The GUID of the collection containing the document.

        Returns:
            bool: True if the document was deleted successfully, False otherwise.

        Raises:
            ValueError: If either GUID is invalid or missing.
        """
        return super().delete(resource_guid, collection_guid=collection_guid)

    @classmethod
    def delete_by_key_and_version(
        cls, resource_guid: str, collection_guid: str, key: str, version: str
    ) -> bool:
        """
        Deletes a specific version of a source document identified by its key.

        Args:
            resource_guid (str): The GUID of the document to delete.
            collection_guid (str): The GUID of the collection containing the document.
            key (str): The unique key identifying the document.
            version (str): The specific version of the document to delete.

        Returns:
            bool: True if the document was deleted successfully, False otherwise.

        Raises:
            ValueError: If any required parameters are invalid or missing.
        """
        kwargs = {"collection_guid": collection_guid, "key": key, "versionId": version}
        return super().delete(resource_guid, **kwargs)

    @classmethod
    def exists(cls, resource_guid: str, collection_guid: str) -> bool:
        """
        Checks if a source document exists in a collection.

        Args:
            resource_guid (str): The GUID of the document to check.
            collection_guid (str): The GUID of the collection to check in.

        Returns:
            bool: True if the document exists, False otherwise.

        Raises:
            ValueError: If either GUID is invalid or missing.
        """
        return super().exists(resource_guid, collection_guid=collection_guid)

    @classmethod
    def retrieve_statistics(cls, resource_guid: str, collection_guid: str):
        """
        Retrieves statistics for a specific source document.

        Args:
            resource_guid (str): The GUID of the document to get statistics for.
            collection_guid (str): The GUID of the collection containing the document.

        Returns:
            STATS_MODEL: The document statistics data.

        Raises:
            ValueError: If either GUID is invalid or missing.
        """
        return super().retrieve_statistics(
            resource_guid, collection_guid=collection_guid
        )

    @classmethod
    def enumerate_with_query(
        cls, collection_guid: str, **kwargs
    ) -> "EnumerationResultModel":
        """
        Enumerates source documents in a collection using a query model.

        Args:
            collection_guid (str): The GUID of the collection to enumerate documents from.
            **kwargs: Additional query parameters that conform to the ENUMERABLE_REQUEST_MODEL.

        Returns:
            EnumerationResultModel: The enumeration results containing matching documents
                and pagination metadata.

        Raises:
            ValueError: If collection_guid is invalid or missing.
            ValidationError: If the query parameters don't match the ENUMERABLE_REQUEST_MODEL schema.
        """
        return super().enumerate_with_query(collection_guid=collection_guid, **kwargs)

    @classmethod
    def search(
        cls,
        collection_guid: str,
        include_data: bool = False,
        **search_params: CollectionSearchRequestModel,
    ) -> SearchResultModel:
        """
        Searches for documents in a collection using a query model.

        Args:
            collection_guid (str): The GUID of the collection to search in.
            include_data (bool, optional): Flag to include data in the search results. Defaults to False.
            **search_params: Keyword arguments that match the CollectionSearchRequestModel schema.

        Returns:
            SearchResultModel: The search results containing matching documents and pagination metadata.

        Raises:
            ValueError: If tenant GUID is not set in the client configuration.
        """
        data = CollectionSearchRequestModel(
            collection_guid=collection_guid, **search_params
        )

        client = get_client(cls.SERVICE)
        if client.tenant_guid is None:
            raise ValueError("Tenant GUID is required for this resource.")

        path_components, url_params = cls._get_resource_path(
            collection_guid=collection_guid, search=None
        )
        if include_data:
            path_components, url_params = cls._get_resource_path(
                collection_guid=collection_guid, search=None, incldata=None
            )

        url = _get_url_v1(cls, client.tenant_guid, *path_components, **url_params)

        results = client.request(
            "POST",
            url,
            json=data.model_dump(by_alias=True, mode="json", exclude_unset=True),
        )
        return SearchResultModel.model_validate(results)
