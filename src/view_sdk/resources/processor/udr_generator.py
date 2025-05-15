import os
from typing import Optional

from ...mixins import CreateableAPIResource
from ...models.udr_datatable_request import DatabaseTypeEnum, UdrDataTableRequest
from ...models.udr_document import UdrDocumentModel
from ...models.udr_document_request import UdrDocumentRequest
from ...sdk_logging import log_debug, log_error


class UdrGenerator(CreateableAPIResource):
    """Resource for UDR generation operations."""

    CREATE_METHOD = "POST"
    RESOURCE_NAME: str = "processing/udr"
    REQUEST_MODEL = UdrDocumentRequest
    MODEL = UdrDocumentModel

    @classmethod
    def generate(   
        cls,
        **kwargs
    ) -> UdrDocumentModel:
        """
        Process document to generate UDR.

        Args:
            **kwargs: Document request parameters that will be validated through UdrDocumentRequest model
                     Can include all parameters defined in UdrDocumentRequest model

        Returns:
            UdrDocumentModel containing the processed document.

        Raises:
            ValueError: If file doesn't exist or validation fails
            SdkException: If processing fails
        """
        cls.MODEL = None
        cls.REQUEST_MODEL = None
        return super().create(**kwargs)


   