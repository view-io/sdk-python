from typing import Optional

from ...enums.document_type_enum import DocumentTypeEnum
from ...mixins import CreateableAPIResource
from ...models.metadata_rule import MetadataRuleModel
from ...models.pdf_options import PdfOptionsModel
from ...models.semantic_cell_request import SemanticCellRequest
from ...models.semantic_cell_response import SemanticCellResponse
from ...sdk_logging import log_debug


class SemanticCell(CreateableAPIResource):
    """Resource for semantic cell extraction operations."""

    CREATE_METHOD = "POST"
    PARENT_RESOURCE: str = "processing"
    RESOURCE_NAME: str = "semanticcell"
    REQUEST_MODEL = SemanticCellRequest
    MODEL = SemanticCellResponse

    @classmethod
    def process(
        cls,
        request: SemanticCellRequest,
    ) -> SemanticCellResponse:
        """
        Extract semantic cells from a document using a request object.

        Args:
            request: Semantic cell extraction request

        Returns:
            SemanticCellResponse containing the extracted cells

        Raises:
            ValueError: If required parameters are missing
        """
        if not request.data_:
            raise ValueError("No data supplied for semantic cell extraction.")
        if not request.metadata_rule:
            raise ValueError("Metadata rule is required.")

        log_debug("Making semantic cell request")
        return super().create(**request.model_dump(by_alias=True))

    @classmethod
    def process_document(
        cls,
        doc_type: DocumentTypeEnum,
        metadata_rule: MetadataRuleModel,
        data: bytes,
        max_chunk_content_length: int = 512,
        shift_size: int = 512,
        pdf_options: Optional[PdfOptionsModel] = None,
    ) -> SemanticCellResponse:
        """
        Extract semantic cells from a document using individual parameters.

        Args:
            doc_type: Document type
            metadata_rule: Metadata rule to apply
            data: Binary data to process
            max_chunk_content_length: Maximum chunk content length
            shift_size: Shift size
            pdf_options: Optional PDF processing options

        Returns:
            SemanticCellResponse containing the extracted cells

        Raises:
            ValueError: If required parameters are missing
        """
        if not data:
            raise ValueError("No data supplied for semantic cell extraction.")

        request = SemanticCellRequest(
            document_type=doc_type,
            metadata_rule=metadata_rule,
            data_=data,
            max_chunk_content_length=max_chunk_content_length,
            shift_size=shift_size,
            pdf=pdf_options,
        )

        return cls.process(request)
