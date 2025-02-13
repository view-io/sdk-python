from typing import Optional

from ...enums.document_type_enum import DocumentTypeEnum
from ...mixins import CreateableAPIResource
from ...models.type_result import TypeResultModel
from ...sdk_logging import log_debug


class TypeDetector(CreateableAPIResource):
    """Resource for type detection operations."""

    CREATE_METHOD = "POST"
    PARENT_RESOURCE = "processing"
    RESOURCE_NAME: str = "typedetection"
    MODEL = TypeResultModel

    @classmethod
    def process(
        cls,
        data: bytes,
        content_type: Optional[str] = None,
    ) -> TypeResultModel:
        """
        Determine a document type.

        Args:
            data: Binary data to analyze
            content_type: Content-type. CSV content-types are inferred using this header's value.

        Returns:
            TypeResultModel containing the detected type information.

        Raises:
            ValueError: If no data is provided.
        """
        if not data:
            raise ValueError("No data supplied for content type detection.")

        if not content_type:
            content_type = "application/octet-stream"

        request_data = {"data": data, "content_type": content_type}

        try:
            log_debug(
                f"Making type detection request with content-type: {content_type}"
            )
            return super().create(**request_data)
        except Exception as e:
            log_debug(f"Error during type detection: {str(e)}")
            # Return default type result on error, matching C# behavior
            return TypeResultModel(
                mime_type="application/octet-stream",
                extension=None,
                type=DocumentTypeEnum.Unknown,
            )
