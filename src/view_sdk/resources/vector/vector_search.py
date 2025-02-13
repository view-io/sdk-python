from typing import List

from ...mixins import BaseAPIResource
from ...models.find_embeddings_request import FindEmbeddingsRequestModel
from ...models.find_embeddings_result import FindEmbeddingsResultModel
from ...models.vector_chunk import VectorChunkModel
from ...models.vector_query_request import VectorQueryRequestModel
from ...models.vector_search_request import VectorSearchRequestModel
from ...sdk_configuration import Service, get_client
from ...utils.url_helper import _get_url_v1


# TODO: need think of a better name
class Search(BaseAPIResource):
    """A class for performing vector-based search operations in vector repositories.

    This class provides methods for querying, searching, and finding embeddings in vector
    repositories. It inherits from BaseAPIResource and requires a tenant GUID for
    all operations.

    Attributes:
        RESOURCE_NAME (str): Name of the resource ("vectorrepositories")
        SERVICE (Service): The service type (VECTOR)
    """

    RESOURCE_NAME: str = "vectorrepositories"
    SERVICE = Service.VECTOR

    @classmethod
    def query(cls, **query_params: VectorQueryRequestModel) -> str:
        """Execute a query against a vector repository.

        Args:
            **query_params: Keyword arguments that match the VectorQueryRequestModel schema.
                Must include vector_repository_guid and other required parameters as defined
                in the model.

        Returns:
            str: The query response from the vector repository.

        Raises:
            ValueError: If tenant GUID is not set in the client configuration.
        """
        data = VectorQueryRequestModel(**query_params)

        client = get_client(cls.SERVICE)
        if client.tenant_guid is None:
            raise ValueError("Tenant GUID is required for this resource.")

        path_components, url_params = cls._get_resource_path(
            data.vector_repository_guid, "query"
        )
        url = _get_url_v1(cls, client.tenant_guid, *path_components, **url_params)

        return client.request(
            "POST",
            url,
            json=data.model_dump(by_alias=True, mode="json", exclude_unset=True),
        )

    @classmethod
    def search(
        cls, **search_params: VectorSearchRequestModel
    ) -> List[VectorChunkModel]:
        """Search for vector chunks in a vector repository.

        Args:
            **search_params: Keyword arguments that match the VectorSearchRequestModel schema.
                Must include vector_repository_guid and other required parameters as defined
                in the model.

        Returns:
            List[VectorChunkModel]: A list of vector chunks that match the search criteria.
                Returns an empty list if no matches are found.

        Raises:
            ValueError: If tenant GUID is not set in the client configuration.
        """
        data = VectorSearchRequestModel(**search_params)

        client = get_client(cls.SERVICE)
        if client.tenant_guid is None:
            raise ValueError("Tenant GUID is required for this resource.")

        path_components, url_params = cls._get_resource_path(
            data.vector_repository_guid, "search"
        )
        url = _get_url_v1(cls, client.tenant_guid, *path_components, **url_params)

        results = client.request(
            "POST",
            url,
            json=data.model_dump(by_alias=True, mode="json", exclude_unset=True),
        )
        return (
            [VectorChunkModel.model_validate(chunk) for chunk in results]
            if results
            else []
        )

    @classmethod
    def find_embeddings(
        cls, **find_params: FindEmbeddingsRequestModel
    ) -> FindEmbeddingsResultModel:
        """Find embeddings in a vector repository based on specified criteria.

        Args:
            **find_params: Keyword arguments that match the FindEmbeddingsRequestModel schema.
                Must include vector_repository_guid and other required parameters as defined
                in the model.

        Returns:
            FindEmbeddingsResultModel: The result containing found embeddings.
                Returns None if no embeddings are found.

        Raises:
            ValueError: If tenant GUID is not set in the client configuration.
        """
        data = FindEmbeddingsRequestModel(**find_params)

        client = get_client(cls.SERVICE)
        if client.tenant_guid is None:
            raise ValueError("Tenant GUID is required for this resource.")

        path_components, url_params = cls._get_resource_path(
            data.vector_repository_guid, "find"
        )
        url = _get_url_v1(cls, client.tenant_guid, *path_components, **url_params)

        result = client.request(
            "POST",
            url,
            json=data.model_dump(by_alias=True, mode="json", exclude_unset=True),
        )
        return FindEmbeddingsResultModel.model_validate(result) if result else None
