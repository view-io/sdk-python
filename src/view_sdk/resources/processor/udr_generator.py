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
    PARENT_RESOURCE: str = "processing"
    RESOURCE_NAME: str = "udr"
    REQUEST_MODEL = UdrDocumentRequest
    MODEL = UdrDocumentModel

    @classmethod
    def process_document(
        cls, filename: Optional[str] = None, **kwargs: UdrDocumentRequest
    ) -> UdrDocumentModel:
        """
        Process document to generate UDR.

        Args:
            filename: Optional filename containing data. Will overwrite data kwarg if provided
            **kwargs: Document request parameters that will be validated through UdrDocumentRequest model
                     Can include all parameters defined in UdrDocumentRequest model

        Returns:
            UdrDocumentModel containing the processed document.

        Raises:
            ValueError: If file doesn't exist or validation fails
            SdkException: If processing fails
        """
        if filename:
            if not os.path.exists(filename):
                raise ValueError(f"File not found: {filename}")
            with open(filename, "rb") as f:
                kwargs["data"] = f.read()

        try:
            log_debug("Making UDR document request")
            return super().create(**kwargs)
        except Exception as e:
            log_error(f"Error processing document: {str(e)}")
            raise

    @classmethod
    def process_datatable(
        cls, filename: Optional[str] = None, **kwargs
    ) -> UdrDocumentModel:
        """
        Process data table to generate UDR.

        Args:
            filename: Optional filename containing SQLite data for Sqlite database type
            **kwargs: Data table request parameters that will be validated through UdrDataTableRequest model
                     Must include database_type and other parameters defined in UdrDataTableRequest model

        Returns:
            UdrDocumentModel containing the processed document.

        Raises:
            ValueError: For invalid combinations of database_type and filename or validation fails
            SdkException: If processing fails
        """
        if kwargs.get("database_type") == DatabaseTypeEnum.SQLITE:
            if not filename:
                raise ValueError(
                    "Filename must be provided when using Sqlite database type"
                )
            if not os.path.exists(filename):
                raise ValueError(f"File not found: {filename}")
            with open(filename, "rb") as f:
                kwargs["sqlite_file_data"] = f.read()
        elif filename:
            raise ValueError(
                "Filename should not be provided for non-Sqlite database types"
            )

        cls.REQUEST_MODEL = UdrDataTableRequest
        cls.RESOURCE_NAME = "datatable"
        log_debug("Making UDR data table request")

        try:
            return super().create(**kwargs)
        except Exception as e:
            log_error(f"Error processing data table: {str(e)}")
            return None  # Ensure that None is returned on error
