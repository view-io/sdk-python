from typing import Optional

from ...enums.document_type_enum import DocumentTypeEnum
from ...mixins import CreateableAPIResource
from ...models.type_result import TypeResultModel
from ...sdk_logging import log_debug


class TypeDetector(CreateableAPIResource):
    """Resource for type detection operations."""

    CREATE_METHOD = "POST"
    RESOURCE_NAME: str = "processing/typedetection"
    MODEL = TypeResultModel

    @classmethod
    def type_detection(
        cls,
        **kwargs,
    ) -> TypeResultModel:
        """
        Determine a document type.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            TypeResultModel containing the detected type information.

        Raises:
            ValueError: If no data is provided.
        """
     
        return super().create(**kwargs)