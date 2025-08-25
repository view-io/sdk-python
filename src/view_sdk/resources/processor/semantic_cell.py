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
        else:
            # Handle direct kwargs (not wrapped in a request object)
            # Check for both 'data' and 'Data' parameters
            data = kwargs.get("data") or kwargs.get("Data")
            if not data:
                raise ValueError("No data supplied for semantic cell extraction.")
            # Normalize to lowercase 'data' for consistency
            if "Data" in kwargs:
                kwargs["data"] = kwargs.pop("Data")
        return super().create(**kwargs)
