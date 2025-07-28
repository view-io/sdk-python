from ...mixins import CreateableAPIResource
from ...models.generate_embeddings_request import GenerateEmbeddingsRequestModel


class GenerateEmbeddings(CreateableAPIResource):
    RESOURCE_NAME = "embeddings"
    REQUEST_MODEL = GenerateEmbeddingsRequestModel

    @classmethod
    def generate(cls, **kwargs: GenerateEmbeddingsRequestModel):
        """Generate embeddings for the provided input.

        Args:
            **kwargs: Keyword arguments matching the GenerateEmbeddingsRequestModel schema.
                     These specify the input text and embedding configuration.

        Returns:
            The response from the embeddings generation API containing the generated embeddings.
        """
        return cls.create(**kwargs)
