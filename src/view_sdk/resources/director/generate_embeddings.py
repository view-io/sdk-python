from ...mixins import CreateableAPIResource
from ...models.embeddings_request import EmbeddingsRequest


class GenerateEmbeddings(CreateableAPIResource):
    RESOURCE_NAME = "embeddings"
    REQUIRES_TENANT = True
    MODEL = EmbeddingsRequest
