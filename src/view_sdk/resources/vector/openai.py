from ...models.openai_embeddings_request import OpenAiEmbeddingsRequest
from ...models.openai_embeddings_result import OpenAiEmbeddingsResult
from ...sdk_configuration import EmbeddingDefaults, Service, get_client
from .vector_mixins import ConnectivityMixin, EmbeddingsGeneratorMixin


class OpenAI(EmbeddingsGeneratorMixin, ConnectivityMixin):
    """Resource for OpenAI operations."""

    RESOURCE_NAME: str = "embeddings"
    MODEL = OpenAiEmbeddingsResult
    REQUEST_MODEL = OpenAiEmbeddingsRequest
    SERVICE = Service.EMBEDDINGS
    REQUIRES_TENANT = False
    CREATE_METHOD = "POST"
    DEFAULT_MODEL = EmbeddingDefaults.OPENAI_DEFAULT_MODEL

    @classmethod
    def validate_connectivity(cls) -> bool:
        """
        Validate connectivity to the OpenAI service.

        Returns:
            bool: True if service is accessible, False otherwise
        """
        client = get_client(cls.SERVICE)
        try:
            # OpenAI specific connectivity check
            client.request("HEAD", "models")
            return True
        except Exception:
            return False

    @classmethod
    def generate_embeddings(
        cls,
        embed_request: OpenAiEmbeddingsRequest,
        timeout: int = 30,
    ) -> OpenAiEmbeddingsResult:
        """
        Generate embeddings using OpenAI.

        Args:
            embed_request: The embeddings request
            timeout: Request timeout in seconds (default: 30)

        Returns:
            OpenAiEmbeddingsResult containing the generated embeddings

        Raises:
            ValueError: If timeout is less than 1
        """
        if timeout < 1:
            raise ValueError("Timeout must be greater than 0")

        # Set default model if not specified
        if not embed_request.model:
            embed_request.model = cls.DEFAULT_MODEL

        try:
            # Add bearer token to request headers
            headers = {"Authorization": f"Bearer {get_client(cls.SERVICE).access_key}"}
            return super().create(
                headers=headers, **embed_request.model_dump(mode="json", by_alias=True)
            )
        except Exception:
            return OpenAiEmbeddingsResult(
                success=False, status_code=500, model=embed_request.model
            )
