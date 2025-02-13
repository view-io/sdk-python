from ...mixins import RetrievableAPIResource


class Connections(RetrievableAPIResource):
    RESOURCE_NAME = "connections"
    REQUIRES_TENANT = False
    MODEL = None
