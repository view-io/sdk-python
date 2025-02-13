from ...mixins import CreateableAPIResource, DeletableAPIResource, ExistsAPIResource
from ...models.embeddings_document import EmbeddingsDocumentModel
from ...sdk_configuration import Service


class Documents(
    ExistsAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
):
    """
    API resource class for managing vector documents within repositories.

    This class provides methods for writing, deleting, and checking existence of
    vector documents in vector repositories. It supports both direct document operations
    and filter-based operations.

    Attributes:
        RESOURCE_NAME (str): The API resource name for documents.
        MODEL (Type[BaseModel]): The Pydantic model for embeddings documents.
        SERVICE (Service): The service type (VECTOR).
        PARENT_RESOURCE (str): The parent resource name (vectorrepositories).
        PARENT_ID_PARAM (str): The parameter name for repository GUID.
    """

    RESOURCE_NAME: str = "documents"
    MODEL = EmbeddingsDocumentModel
    SERVICE = Service.VECTOR

    PARENT_RESOURCE: str = "vectorrepositories"
    PARENT_ID_PARAM: str = "repo_guid"

    @classmethod
    def write(cls, **kwargs) -> EmbeddingsDocumentModel:
        """
        Write a new vector document to a repository.

        This is an alias for the create method, providing a more intuitive name
        for the operation of writing documents to a vector repository.

        Args:
            **kwargs: Keyword arguments for document creation, including:
                - repo_guid (str): The GUID of the vector repository.
                - Other document attributes as defined in EmbeddingsDocumentModel.

        Returns:
            EmbeddingsDocumentModel: The created vector document instance.

        Raises:
            ValueError: If required fields are missing or invalid.
        """
        return cls.create(**kwargs)

    @classmethod
    def delete_by_filter(cls, repo_guid: str, **filter_params) -> bool:
        """
        Delete documents from a repository based on filter parameters.

        This method allows for bulk deletion of documents that match the specified
        filter criteria within a vector repository.

        Args:
            repo_guid (str): The GUID of the vector repository.
            **filter_params: Filter parameters to identify documents to delete.
                These parameters depend on the repository's supported filter options.

        Returns:
            bool: True if the deletion was successful, False otherwise.

        Raises:
            ValueError: If repo_guid is invalid or missing, or if filter parameters
                are invalid.
        """
        return cls.delete(None, repo_guid=repo_guid, **filter_params)
