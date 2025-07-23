from ...mixins import CreateableAPIResource, ExistsAPIResource, RetrievableAPIResource, AllRetrievableAPIResource, UpdatableAPIResource, DeletableAPIResource

class Config(CreateableAPIResource, ExistsAPIResource, RetrievableAPIResource, AllRetrievableAPIResource,UpdatableAPIResource,DeletableAPIResource):
    """
    Config resource for Assistant operations.
    """
    RESOURCE_NAME: str = "assistant/configs"
    REQUIRES_TENANT = True
    CREATE_METHOD = "POST"
    RETURNS_LIST = False
