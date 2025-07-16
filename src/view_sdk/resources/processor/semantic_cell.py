
from ...mixins import CreateableAPIResource
from ...models.semantic_cell_response import SemanticCellResponse
from ...sdk_logging import log_debug


class SemanticCell(CreateableAPIResource):
    """Resource for semantic cell extraction operations."""

    CREATE_METHOD = "POST"
    RESOURCE_NAME: str = "processing/semanticcell"
    MODEL = SemanticCellResponse

    @classmethod
    def extraction(
        cls,
        **kwargs,
    ) -> SemanticCellResponse:
        """
        Extract semantic cells from a document using individual parameters.

        Args:
            **kwargs: Keyword arguments for the semantic cell extraction request

        Returns:
            SemanticCellResponse containing the extracted cells

        Raises:
            ValueError: If required parameters are missing
        """
        cls.MODEL = None
        cls.REQUEST_MODEL = None
        return super().create(**kwargs)
