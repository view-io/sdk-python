from ...mixins import CreateableAPIResource
from ...sdk_configuration import Service


class GenerateEmbeddings(CreateableAPIResource):
    SERVICE = Service.DIRECTOR
    RESOURCE_NAME = "embeddings"
    REQUIRES_TENANT = True
    CREATE_METHOD = "POST"
