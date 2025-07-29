from ...mixins import CreateableAPIResource
from ...models.cleanup_request import CleanupRequest
from ...models.cleanup_response import CleanupResponse
from ...sdk_logging import log_debug


class Cleanup(CreateableAPIResource):
    """
    Resource class for managing cleanup processor operations.

    This class provides methods to process cleanup operations for both storage server
    and data crawler scenarios. It handles the cleanup of various resources including
    tenants, collections, storage pools, buckets, and repositories.
    """

    CREATE_METHOD: str = "POST"
    RESOURCE_NAME: str = "processing/cleanup"
    REQUEST_MODEL = CleanupRequest
    MODEL = CleanupResponse

    @classmethod
    def cleanup_pipeline(
        cls,
        **kwargs,
    ) -> CleanupResponse:
        """
        Process cleanup operations for storage server resources.

        This method handles the cleanup of storage-related resources including pools,
        buckets, and associated metadata and embeddings.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            CleanupResponse: Response containing the results of the cleanup operation.

        Raises:
            Exception: If there's an error processing the cleanup request.
        """
        log_debug(f"Making cleanup request for storage: {kwargs}")
        return super().create(**kwargs)
