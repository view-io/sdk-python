from ...mixins import HealthCheckAPIResource


class SwitchBoard(HealthCheckAPIResource):
    """Resource for Assistant operations."""

    RESOURCE_NAME: str = ""
    REQUIRES_TENANT = False
