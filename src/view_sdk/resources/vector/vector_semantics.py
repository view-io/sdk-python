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
    def read(cls, repo_guid: str, doc_guid: str, cell_guid: str):
        """Read a specific semantic cell from a document."""
        kwargs = {"repo_guid": repo_guid, "doc_guid": doc_guid}
        return super().retrieve(cell_guid, **kwargs)


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
    def read(cls, repo_guid: str, doc_guid: str, cell_guid: str):
        """Read semantic chunks from a specific cell."""
        kwargs = {"repo_guid": repo_guid, "doc_guid": doc_guid, "cell_guid": cell_guid}
        return super().retrieve(cell_guid, **kwargs)
