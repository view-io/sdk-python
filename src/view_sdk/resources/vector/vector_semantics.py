from ...mixins import (
    AllRetrievableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
)
from ...models.semantic_cell import SemanticCellModel
from ...models.semantic_chunk import SemanticChunkModel


class SemanticCells(
    ExistsAPIResource, RetrievableAPIResource, AllRetrievableAPIResource
):
    """Manages semantic cell operations in vector repositories."""

    RESOURCE_NAME: str = "cells"
    MODEL = SemanticCellModel

    PARENT_RESOURCE: str = "documents"
    PARENT_ID_PARAM: str = "doc_guid"
    QUERY_PARAMS = {"repo_guid": None}

    @classmethod
    def _get_resource_path(cls, *resource_guids: str, **kwargs) -> tuple:
        """Override to handle nested repository and document paths."""
        path_components = []

        # Add repository path
        if "repo_guid" in kwargs:
            repo_guid = kwargs.pop("repo_guid")
            path_components.extend(["vectorrepositories", repo_guid])

        # Add document path
        if cls.PARENT_ID_PARAM in kwargs:
            doc_guid = kwargs.pop(cls.PARENT_ID_PARAM)
            path_components.extend([cls.PARENT_RESOURCE, doc_guid])

        # Add cells resource and any specific cell guid
        path_components.append(cls.RESOURCE_NAME)
        path_components.extend(resource_guids)

        return tuple(path_components), kwargs

    @classmethod
    def retrieve(cls, repo_guid: str, doc_guid: str, cell_guid: str):
        """Read a specific semantic cell from a document.
        
        Args:
            repo_guid (str): The GUID of the vector repository.
            doc_guid (str): The GUID of the vector document.
            cell_guid (str): The GUID of the semantic cell.

        Returns:
            SemanticCellModel: The retrieved semantic cell instance.
        """
        kwargs = {"repo_guid": repo_guid, "doc_guid": doc_guid}
        return super().retrieve(cell_guid, **kwargs)
    
    @classmethod
    def exists(cls, repo_guid: str, doc_guid: str, cell_guid: str):
        """Check if a specific semantic cell exists in a document.
        
        Args:
            repo_guid (str): The GUID of the vector repository.
            doc_guid (str): The GUID of the vector document.
            cell_guid (str): The GUID of the semantic cell.

        Returns:
            bool: True if the semantic cell exists, False otherwise.
        """
        kwargs = {"repo_guid": repo_guid, "doc_guid": doc_guid}
        return super().exists(cell_guid, **kwargs)

    @classmethod
    def retrieve_all(cls, repo_guid: str, doc_guid: str):
        """Retrieve all semantic cells from a document.
        
        Args:
            repo_guid (str): The GUID of the vector repository.
            doc_guid (str): The GUID of the vector document.

        Returns:
            list[SemanticCellModel]: A list of semantic cell instances.
        """
        kwargs = {"repo_guid": repo_guid, "doc_guid": doc_guid}
        return super().retrieve_all(**kwargs)

class SemanticChunks(
    ExistsAPIResource, RetrievableAPIResource, AllRetrievableAPIResource
):
    """Manages semantic chunk operations within cells."""

    RESOURCE_NAME: str = "chunks"
    MODEL = SemanticChunkModel

    PARENT_RESOURCE: str = "cells"
    PARENT_ID_PARAM: str = "cell_guid"
    QUERY_PARAMS = {"repo_guid": None, "doc_guid": None}

    @classmethod
    def _get_resource_path(cls, *resource_guids: str, **kwargs) -> tuple:
        """Override to handle nested repository, document and cell paths."""
        path_components = []

        # Add repository path
        if "repo_guid" in kwargs:
            repo_guid = kwargs.pop("repo_guid")
            path_components.extend(["vectorrepositories", repo_guid])

        # Add document path
        if "doc_guid" in kwargs:
            doc_guid = kwargs.pop("doc_guid")
            path_components.extend(["documents", doc_guid])

        # Add cell path
        if cls.PARENT_ID_PARAM in kwargs:
            cell_guid = kwargs.pop(cls.PARENT_ID_PARAM)
            path_components.extend([cls.PARENT_RESOURCE, cell_guid])

        # Add chunks resource and any specific chunk guid
        path_components.append(cls.RESOURCE_NAME)
        path_components.extend(resource_guids)

        return tuple(path_components), kwargs

    @classmethod
    def retrieve_all(cls, repo_guid: str, doc_guid: str, cell_guid: str):
        """Read semantic chunks from a specific cell.

        Args:
            repo_guid (str): The GUID of the vector repository.
            doc_guid (str): The GUID of the vector document.
            cell_guid (str): The GUID of the semantic cell.

        Returns:
            list[SemanticChunkModel]: A list of semantic chunk instances.
        """
        kwargs = {"repo_guid": repo_guid, "doc_guid": doc_guid, "cell_guid": cell_guid}
        return super().retrieve_all(**kwargs)

    @classmethod
    def retrieve(cls, repo_guid: str, doc_guid: str, cell_guid: str, chunk_guid: str):
        """Read a specific semantic chunk from a cell.
        
        Args:
            repo_guid (str): The GUID of the vector repository.
            doc_guid (str): The GUID of the vector document.
            cell_guid (str): The GUID of the semantic cell.
            chunk_guid (str): The GUID of the semantic chunk.

        Returns:
            SemanticChunkModel: The retrieved semantic chunk instance.
        """
        kwargs = {"repo_guid": repo_guid, "doc_guid": doc_guid, "cell_guid": cell_guid}
        return super().retrieve(chunk_guid, **kwargs)
    
    @classmethod
    def exists(cls, repo_guid: str, doc_guid: str, cell_guid: str, chunk_guid: str):
        """Check if a specific semantic chunk exists in a cell.
        
        Args:
            repo_guid (str): The GUID of the vector repository.
            doc_guid (str): The GUID of the vector document.
            cell_guid (str): The GUID of the semantic cell.
            chunk_guid (str): The GUID of the semantic chunk.

        Returns:
            bool: True if the semantic chunk exists, False otherwise.
        """
        kwargs = {"repo_guid": repo_guid, "doc_guid": doc_guid, "cell_guid": cell_guid}
        return super().exists(chunk_guid, **kwargs)
    
    