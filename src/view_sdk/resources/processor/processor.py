from ...mixins import CreateableAPIResource
from ...models.processor_request import ProcessorRequest
from ...models.processor_response import ProcessorResponse
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
    def processing_pipeline(
        cls,
        **kwargs,
    ) -> ProcessorResponse:
        """
        Process a document from data crawler through the processing pipeline.

        This method handles the processing of documents from the data crawler,
        applying metadata rules, optional embeddings rules, and integrating with
        vector and graph repositories as needed.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            ProcessorResponse: Response containing the results of the processing operation.

        Note:
            The method logs debug information about the processing request before execution.
        """
        cls.MODEL = None
        cls.REQUEST_MODEL = None
        log_debug(f"Making processor request for crawler: {kwargs}")
        return super().create(**kwargs)
