from ...mixins import CreateableAPIResource
from ...models.udr_document import UdrDocumentModel
from ...models.udr_document_request import UdrDocumentRequest


class UdrGenerator(CreateableAPIResource):
    """Resource for UDR generation operations."""

    CREATE_METHOD = "POST"
    RESOURCE_NAME: str = "processing/udr"
    REQUEST_MODEL = UdrDocumentRequest
    MODEL = UdrDocumentModel

    @classmethod
    def generate(cls, **kwargs) -> UdrDocumentModel:
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
        return super().create(**kwargs)
