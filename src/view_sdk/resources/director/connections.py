from ...mixins import AllRetrievableAPIResource
from ...sdk_configuration import Service


class Connections(AllRetrievableAPIResource):
    """
    Connections resource for Director operations.
    """

    RESOURCE_NAME = "connections"
    REQUIRES_TENANT = False
    MODEL = None
    SERVICE = Service.DIRECTOR

    @classmethod
    def retrieve_all(cls, token: str) -> list["BaseModel"]:
        """
        Retrieve all connections.
        """
        return super().retrieve_all(headers={"x-token": token})
