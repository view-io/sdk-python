from typing import Optional

from ...mixins import CreateableAPIResource
from ...models.collection import CollectionModel
from ...models.embeddings_rule import EmbeddingsRuleModel
from ...models.graph_repository import GraphRepositoryModel
from ...models.lexi_embeddings_request import LexiEmbeddingsRequest
from ...models.lexi_embeddings_response import LexiEmbeddingsResponse
from ...models.search_result import SearchResultModel
from ...models.tenant_metadata import TenantMetadataModel
from ...models.vector_repository import VectorRepositoryModel
from ...sdk_logging import log_debug


# TODO: Need to check if this is correct.
class LexiEmbeddings(CreateableAPIResource):
    """Resource for Lexi embeddings processor operations."""

    CREATE_METHOD = "POST"
    PARENT_RESOURCE: str = "processing"
    RESOURCE_NAME: str = "lexiprocessing"
    REQUEST_MODEL = LexiEmbeddingsRequest
    MODEL = LexiEmbeddingsResponse

    @classmethod
    def process(
        cls,
        guid: str,
        results: SearchResultModel,
        embeddings_rule: EmbeddingsRuleModel,
        tenant: Optional[TenantMetadataModel] = None,
        collection: Optional[CollectionModel] = None,
        vector_repo: Optional[VectorRepositoryModel] = None,
        graph_repo: Optional[GraphRepositoryModel] = None,
    ) -> LexiEmbeddingsResponse:
        """
        Process Lexi search results for embeddings generation.

        Args:
            results: Search results to process
            embeddings_rule: Embeddings rule to apply
            tenant: Optional tenant metadata
            collection: Optional collection
            vector_repo: Optional vector repository
            graph_repo: Optional graph repository

        Returns:
            LexiEmbeddingsResponse containing the processed results

        Raises:
            ValueError: If required parameters are missing
        """

        request_data = {
            "guid": guid,
            "tenant": tenant,
            "collection": collection,
            "results": results,
            "embeddings_rule": embeddings_rule,
            "vector_repository": vector_repo,
            "graph_repository": graph_repo,
        }

        log_debug(f"Making Lexi embeddings request: {request_data}")
        return super().create(**request_data)
