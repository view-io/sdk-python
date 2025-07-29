from typing import List

from ...models.model_information import ModelInformation
from ...models.ollama_embeddings_request import OllamaEmbeddingsRequest
from ...models.ollama_embeddings_result import OllamaEmbeddingsResult
from ...models.ollama_model_result import OllamaModelResult
from ...sdk_configuration import EmbeddingDefaults, Service
from ...sdk_logging import log_debug, log_warning
from .vector_mixins import (
    ConnectivityMixin,
    EmbeddingsGeneratorMixin,
    ModelDeletionMixin,
    MultiModelLoaderMixin,
)


class Ollama(
    EmbeddingsGeneratorMixin,
    MultiModelLoaderMixin,
    ModelDeletionMixin,
    ConnectivityMixin,
):
    """Resource for Ollama operations."""

    RESOURCE_NAME: str = "api"
    MODEL = OllamaEmbeddingsResult
    REQUEST_MODEL = OllamaEmbeddingsRequest
    SERVICE = Service.EMBEDDINGS
    REQUIRES_TENANT = False
    CREATE_METHOD = "POST"
    DEFAULT_MODEL = EmbeddingDefaults.OLLAMA_DEFAULT_MODEL

    @classmethod
    def list_models(cls) -> List[ModelInformation]:
        """
        List available models.

        Returns:
            List[ModelInformation]: List of available models
        """
        try:
            log_debug("Retrieving model list")
            result = super().retrieve("tags")
            if result:
                model_result = OllamaModelResult.model_validate(result)
                return ModelInformation.from_ollama_response(model_result)
            return []
        except Exception as e:
            log_warning(f"Error listing models: {str(e)}")
            return []
