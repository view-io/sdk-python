# src/view_sdk/resources/vector/voyageai.py
from ...models.voyageai_embeddings_request import VoyageAiEmbeddingsRequest
from ...models.voyageai_embeddings_result import VoyageAiEmbeddingsResult
from ...sdk_configuration import (  # Ensure get_client is imported
    EmbeddingDefaults,
    Service,
    get_client,
)
from .vector_mixins import ConnectivityMixin, EmbeddingsGeneratorMixin


class VoyageAI(EmbeddingsGeneratorMixin, ConnectivityMixin):
    """Resource for VoyageAI operations."""

    RESOURCE_NAME: str = "v1/embeddings"
    MODEL = VoyageAiEmbeddingsResult
    REQUEST_MODEL = VoyageAiEmbeddingsRequest
    SERVICE = Service.EMBEDDINGS
    REQUIRES_TENANT = False
    CREATE_METHOD = "POST"
    DEFAULT_MODEL = EmbeddingDefaults.VOYAGEAI_DEFAULT_MODEL

    @classmethod
    def validate_connectivity(cls) -> bool:
        """Check if the VoyageAI service is accessible.

        Returns:
            bool: True if service is accessible, False otherwise
        """
        client = get_client(cls.SERVICE)  # Call the standalone function
        try:
            response = client.request("GET", "healthz")
            return response.status_code == 200  # Check for successful response
        except Exception:
            return False

    @classmethod
    def generate_embeddings(
        cls,
        embed_request: VoyageAiEmbeddingsRequest,
        timeout: int = 30,
    ) -> VoyageAiEmbeddingsResult:
        """Generate embeddings using VoyageAI service.

        Args:
            embed_request: Request containing text to embed and model settings
            timeout: Request timeout in seconds, default 30

        Returns:
            VoyageAiEmbeddingsResult: Contains embeddings or error status

        Raises:
            ValueError: If timeout is less than 1
        """
        if timeout < 1:
            raise ValueError("Timeout must be greater than 0")

        if not embed_request.model:
            embed_request.model = cls.DEFAULT_MODEL

        try:
            client = get_client(cls.SERVICE)
            headers = {"Authorization": f"Bearer {client.access_key}"}

            response = client.request(
                "POST",
                cls.RESOURCE_NAME,
                json=embed_request.model_dump(mode="json", by_alias=True),
                headers=headers,
            )

            # Create a successful result based on the response
            return cls.MODEL(
                success=True, status_code=200, model=embed_request.model, data=response
            )
        except Exception:
            # Create a failed result if an exception occurs
            return cls.MODEL(success=False, status_code=500, model=embed_request.model)
