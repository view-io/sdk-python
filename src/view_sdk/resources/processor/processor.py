from typing import Optional

from ...mixins import CreateableAPIResource
from ...models.bucket import BucketMetadataModel
from ...models.collection import CollectionModel
from ...models.data_repository import DataRepositoryModel
from ...models.embeddings_rule import EmbeddingsRuleModel
from ...models.graph_repository import GraphRepositoryModel
from ...models.metadata_rule import MetadataRuleModel
from ...models.object_metadata import ObjectMetadataModel
from ...models.pool import StoragePool
from ...models.processor_request import ProcessorRequest
from ...models.processor_response import ProcessorResponse
from ...models.tenant_metadata import TenantMetadataModel
from ...models.vector_repository import VectorRepositoryModel
from ...sdk_logging import log_debug


class Processor(CreateableAPIResource):
    """
    Resource class for managing processor pipeline operations.

    This class handles document processing operations for both storage server and
    data crawler scenarios. It supports processing documents with metadata rules,
    embeddings rules, and optional vector and graph repository integrations.

    Attributes:
        RESOURCE_NAME (str): The API resource name for processor operations.
        MODEL (Type[BaseModel]): The response model for processor operations.
        REQUEST_MODEL (Type[BaseModel]): The request model for processor operations.
        SERVICE (Service): The service type (PROCESSOR).
        REQUIRES_TENANT (bool): Whether tenant GUID is required (False).
        CREATE_METHOD (str): The HTTP method for create operations (POST).
    """

    CREATE_METHOD = "POST"
    RESOURCE_NAME: str = "processing"
    REQUEST_MODEL = ProcessorRequest
    MODEL = ProcessorResponse

    @classmethod
    def process_storage(
        cls,
        guid: str,
        tenant: TenantMetadataModel,
        collection: CollectionModel,
        pool: StoragePool,
        bucket: BucketMetadataModel,
        obj: ObjectMetadataModel,
        metadata_rule: MetadataRuleModel,
        embeddings_rule: Optional[EmbeddingsRuleModel] = None,
        vector_repo: Optional[VectorRepositoryModel] = None,
        graph_repo: Optional[GraphRepositoryModel] = None,
    ) -> ProcessorResponse:
        """
        Process a document from storage server through the processing pipeline.

        This method handles the processing of documents stored in the storage server,
        applying metadata rules, optional embeddings rules, and integrating with
        vector and graph repositories as needed.

        Args:
            tenant (TenantMetadataModel): Tenant metadata information.
            collection (CollectionModel): Collection information.
            pool (StoragePool): Storage pool information.
            bucket (BucketMetadataModel): Bucket metadata information.
            obj (ObjectMetadataModel): Object metadata information.
            metadata_rule (MetadataRuleModel): Rules for metadata processing.
            embeddings_rule (Optional[EmbeddingsRuleModel]): Rules for embeddings processing.
                Defaults to None.
            vector_repo (Optional[VectorRepositoryModel]): Vector repository information.
                Defaults to None.
            graph_repo (Optional[GraphRepositoryModel]): Graph repository information.
                Defaults to None.

        Returns:
            ProcessorResponse: Response containing the results of the processing operation.

        Note:
            The method logs debug information about the processing request before execution.
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

        log_debug(f"Making processor request for storage: {request_data}")
        return super().create(**request_data)

    @classmethod
    def process_crawler(
        cls,
        guid: str,
        tenant: Optional[TenantMetadataModel],
        collection: Optional[CollectionModel],
        data_repository: Optional[DataRepositoryModel],
        obj: ObjectMetadataModel,
        metadata_rule: MetadataRuleModel,
        embeddings_rule: Optional[EmbeddingsRuleModel] = None,
        vector_repo: Optional[VectorRepositoryModel] = None,
        graph_repo: Optional[GraphRepositoryModel] = None,
    ) -> ProcessorResponse:
        """
        Process a document from data crawler through the processing pipeline.

        This method handles the processing of documents from the data crawler,
        applying metadata rules, optional embeddings rules, and integrating with
        vector and graph repositories as needed.

        Args:
            tenant (Optional[TenantMetadataModel]): Tenant metadata information.
                Can be None for non-tenant-specific operations.
            collection (Optional[CollectionModel]): Collection information.
                Can be None for collection-independent operations.
            data_repository (Optional[DataRepositoryModel]): Data repository information.
                Can be None for repository-independent operations.
            obj (ObjectMetadataModel): Object metadata information.
            metadata_rule (MetadataRuleModel): Rules for metadata processing.
            embeddings_rule (Optional[EmbeddingsRuleModel]): Rules for embeddings processing.
                Defaults to None.
            vector_repo (Optional[VectorRepositoryModel]): Vector repository information.
                Defaults to None.
            graph_repo (Optional[GraphRepositoryModel]): Graph repository information.
                Defaults to None.

        Returns:
            ProcessorResponse: Response containing the results of the processing operation.

        Note:
            The method logs debug information about the processing request before execution.
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

        log_debug(f"Making processor request for crawler: {request_data}")
        return super().create(**request_data)
