from ...enums.document_type_enum import DocumentTypeEnum
from ...mixins import CreateableAPIResource
from ...models.type_result import TypeResultModel


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
        if "data" not in kwargs or not kwargs["data"]:
            raise ValueError("No data supplied for content type detection.")
        if "content_type" not in kwargs or kwargs["content_type"] is None:
            kwargs["content_type"] = "application/octet-stream"
        try:
            return super().create(**kwargs)
        except Exception:
            return TypeResultModel(
                mime_type="application/octet-stream",
                extension=None,
                type_=DocumentTypeEnum.Unknown,
            )
