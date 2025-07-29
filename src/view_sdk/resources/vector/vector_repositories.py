from ...exceptions import SdkException
from ...mixins import DeletableAPIResource
from ...models.embeddings_document import EmbeddingsDocumentModel
from ...models.enumeration_query import EnumerationQueryModel
from ...models.enumeration_result import EnumerationResultModel
from ...models.vector_repository_statistics import VectorRepositoryStatisticsModel
from ...sdk_configuration import get_client
from ...utils.url_helper import _get_url_v1


class Repositories(
    DeletableAPIResource,
):
    """
    API resource class for managing vector repositories.

    This class provides methods for enumerating documents within repositories,
    retrieving repository statistics, and managing repository contents. It supports
    both document enumeration with filtering and repository-wide operations.

    Attributes:
        RESOURCE_NAME (str): The API resource name for vector repositories.
        MODEL (Type[BaseModel]): The model for embeddings documents.
        STATS_MODEL (Type[BaseModel]): The model for repository statistics.
        REQUEST_MODEL (Type[BaseModel]): The model for enumeration queries.
        SERVICE (Service): The service type (VECTOR).
    """

    RESOURCE_NAME: str = "vectorrepositories"
    MODEL = EmbeddingsDocumentModel
    STATS_MODEL = VectorRepositoryStatisticsModel
    REQUEST_MODEL = EnumerationQueryModel

    @classmethod
    def enumerate_documents(
        cls, repo_guid: str, **kwargs: EnumerationQueryModel
    ) -> EnumerationResultModel:
        """
        Enumerate documents within a vector repository with optional filtering.

        This method allows for querying and filtering documents within a repository
        using the specified enumeration parameters.

        Args:
            repo_guid (str): The GUID of the vector repository.
            **kwargs: Query parameters conforming to EnumerationQueryModel schema,
                such as filters, pagination, and sorting options.

        Returns:
            EnumerationResultModel[EmbeddingsDocumentModel]: The enumeration results
                containing matching documents and pagination metadata.

        Raises:
            ValueError: If repo_guid is invalid or missing.
            ValidationError: If query parameters don't match the REQUEST_MODEL schema.
        """
        client = get_client(cls.SERVICE)

        # Validate request data using REQUEST_MODEL
        if cls.REQUEST_MODEL is not None:
            data = cls.REQUEST_MODEL(**kwargs).model_dump(
                mode="json", by_alias=True, exclude_unset=True
            )

            path_components = (cls.RESOURCE_NAME, repo_guid, "enumerate")
            url = _get_url_v1(cls, client.tenant_guid, *path_components)
            response = client.request("POST", url, json=data)
            return EnumerationResultModel[cls.MODEL].model_validate(response)

    @classmethod
    def get_statistics(cls, repo_guid: str) -> VectorRepositoryStatisticsModel:
        """
        Retrieve statistics for a vector repository.

        This method fetches statistical information about a repository, such as
        document count, size, and other relevant metrics.

        Args:
            repo_guid (str): The GUID of the vector repository.

        Returns:
            VectorRepositoryStatisticsModel: The repository statistics.

        Raises:
            ValueError: If repo_guid is invalid or missing.
            SdkException: If the server returns an empty response.
        """
        client = get_client(cls.SERVICE)
        path_components = (cls.RESOURCE_NAME, repo_guid, "stats")
        url = _get_url_v1(cls, client.tenant_guid, *path_components)
        result = client.request("GET", url)
        if result:
            return cls.STATS_MODEL.model_validate(result)
        else:
            raise SdkException("Empty response")

    @classmethod
    def truncate(cls, repo_guid: str) -> bool:
        """
        Remove all documents from a vector repository.

        This method performs a complete cleanup of the repository, removing all
        stored documents while preserving the repository itself.

        Args:
            repo_guid (str): The GUID of the vector repository to truncate.

        Returns:
            bool: True if the repository was successfully truncated, False otherwise.

        Raises:
            ValueError: If repo_guid is invalid or missing.

        Note:
            This operation cannot be undone. Use with caution as it permanently
            deletes all documents in the repository.
        """
        return cls.delete(repo_guid)
