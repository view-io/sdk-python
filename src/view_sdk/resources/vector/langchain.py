from ...models.langchain_embeddings_request import LangchainEmbeddingsRequest
from ...models.langchain_embeddings_result import LangchainEmbeddingsResult
from ...sdk_configuration import EmbeddingDefaults, Service
from .vector_mixins import (
    ConnectivityMixin,
    EmbeddingsGeneratorMixin,
    MultiModelLoaderMixin,
)


class Langchain(EmbeddingsGeneratorMixin, MultiModelLoaderMixin, ConnectivityMixin):
    """Resource for Langchain operations."""

    RESOURCE_NAME: str = "embeddings"
    MODEL = LangchainEmbeddingsResult
    REQUEST_MODEL = LangchainEmbeddingsRequest
    SERVICE = Service.EMBEDDINGS
    REQUIRES_TENANT = False
    CREATE_METHOD = "POST"
    DEFAULT_MODEL = EmbeddingDefaults.LANGCHAIN_DEFAULT_MODEL
