from ...mixins import CreateableAPIResource
from ...models.semantic_cell_response import SemanticCellResponse


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
        request = kwargs.get("request")
        if request is not None:
            if not getattr(request, "data_", None):
                raise ValueError("No data supplied for semantic cell extraction.")
            if not getattr(request, "metadata_rule", None):
                raise ValueError("Metadata rule is required.")
        else:
            # Handle direct kwargs (not wrapped in a request object)
            if not kwargs.get("data"):
                raise ValueError("No data supplied for semantic cell extraction.")
            if not kwargs.get("metadata_rule"):
                raise ValueError("Metadata rule is required.")
        return super().create(**kwargs)
