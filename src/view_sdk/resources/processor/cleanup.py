from typing import Optional

from ...mixins import CreateableAPIResource
from ...models.bucket import BucketMetadataModel
from ...models.cleanup_request import CleanupRequest
from ...models.cleanup_response import CleanupResponse
from ...models.collection import CollectionModel
from ...models.data_repository import DataRepositoryModel
from ...models.embeddings_rule import EmbeddingsRuleModel
from ...models.graph_repository import GraphRepositoryModel
from ...models.metadata_rule import MetadataRuleModel
from ...models.object_metadata import ObjectMetadataModel
from ...models.pool import StoragePool
from ...models.tenant_metadata import TenantMetadataModel
from ...models.vector_repository import VectorRepositoryModel
from ...sdk_logging import log_debug, log_error


class Cleanup(CreateableAPIResource):
    """
    Resource class for managing cleanup processor operations.

    This class provides methods to process cleanup operations for both storage server
    and data crawler scenarios. It handles the cleanup of various resources including
    tenants, collections, storage pools, buckets, and repositories.
    """

    CREATE_METHOD: str = "POST"
    PARENT_RESOURCE: str = "processing"
    RESOURCE_NAME: str = "cleanup"
    REQUEST_MODEL = CleanupRequest
    MODEL = CleanupResponse

    @classmethod
    def process_storage(
        cls,
        guid: str,
        tenant: Optional[TenantMetadataModel],
        collection: Optional[CollectionModel],
        pool: Optional[StoragePool],
        bucket: Optional[BucketMetadataModel],
        obj: ObjectMetadataModel,
        metadata_rule: MetadataRuleModel,
        embeddings_rule: Optional[EmbeddingsRuleModel],
        vector_repo: Optional[VectorRepositoryModel],
        graph_repo: Optional[GraphRepositoryModel],
    ) -> CleanupResponse:
        """
        Process cleanup operations for storage server resources.

        This method handles the cleanup of storage-related resources including pools,
        buckets, and associated metadata and embeddings.

        Args:
            tenant (Optional[TenantMetadataModel]): Tenant metadata information.
            collection (Optional[CollectionModel]): Collection information.
            pool (Optional[StoragePool]): Storage pool information.
            bucket (Optional[BucketMetadataModel]): Bucket metadata information.
            obj (ObjectMetadataModel): Object metadata information.
            metadata_rule (MetadataRuleModel): Rules for metadata cleanup.
            embeddings_rule (Optional[EmbeddingsRuleModel]): Rules for embeddings cleanup.
            vector_repo (Optional[VectorRepositoryModel]): Vector repository information.
            graph_repo (Optional[GraphRepositoryModel]): Graph repository information.

        Returns:
            CleanupResponse: Response containing the results of the cleanup operation.

        Raises:
            Exception: If there's an error processing the cleanup request.
        """
        request_data = {
            "guid": guid,
            "tenant": tenant,
            "collection": collection,
            "pool": pool,
            "bucket": bucket,
            "object": obj,
            "metadata_rule": metadata_rule,
            "embeddings_rule": embeddings_rule,
            "vector_repository": vector_repo,
            "graph_repository": graph_repo,
        }

        log_debug(f"Making cleanup request for storage: {request_data}")
        try:
            return super().create(**request_data)
        except Exception as e:
            log_error(f"Error processing cleanup request: {e}")
            raise e

    @classmethod
    def process_crawler(
        cls,
        guid: str,
        tenant: Optional[TenantMetadataModel],
        collection: Optional[CollectionModel],
        data_repository: Optional[DataRepositoryModel],
        obj: ObjectMetadataModel,
        metadata_rule: MetadataRuleModel,
        embeddings_rule: Optional[EmbeddingsRuleModel],
        vector_repo: Optional[VectorRepositoryModel],
        graph_repo: Optional[GraphRepositoryModel],
    ) -> CleanupResponse:
        """
        Process cleanup operations for data crawler resources.

        This method handles the cleanup of crawler-related resources including data
        repositories and their associated metadata and embeddings.

        Args:
            tenant (Optional[TenantMetadataModel]): Tenant metadata information.
            collection (Optional[CollectionModel]): Collection information.
            data_repository (Optional[DataRepositoryModel]): Data repository information.
            obj (ObjectMetadataModel): Object metadata information.
            metadata_rule (MetadataRuleModel): Rules for metadata cleanup.
            embeddings_rule (Optional[EmbeddingsRuleModel]): Rules for embeddings cleanup.
            vector_repo (Optional[VectorRepositoryModel]): Vector repository information.
            graph_repo (Optional[GraphRepositoryModel]): Graph repository information.

        Returns:
            CleanupResponse: Response containing the results of the cleanup operation.

        Raises:
            Exception: If there's an error processing the cleanup request.
        """
        request_data = {
            "guid": guid,
            "tenant": tenant,
            "collection": collection,
            "data_repository": data_repository,
            "object": obj,
            "metadata_rule": metadata_rule,
            "embeddings_rule": embeddings_rule,
            "vector_repository": vector_repo,
            "graph_repository": graph_repo,
        }

        log_debug(f"Making cleanup request for crawler: {request_data}")
        try:
            return super().create(**request_data)
        except Exception as e:
            log_error(f"Error processing cleanup request: {e}")
            raise e
