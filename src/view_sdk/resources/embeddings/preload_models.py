from ...mixins import CreateableAPIResource
from ...models.preload_models_request import PreloadModelsRequest


class PreloadModels(CreateableAPIResource):
    PARENT_RESOURCE = "embeddings"
    RESOURCE_NAME = "preload"
    REQUEST_MODEL = PreloadModelsRequest

    @classmethod
    def load(cls, **kwargs: PreloadModelsRequest):
        return cls.create(**kwargs)
