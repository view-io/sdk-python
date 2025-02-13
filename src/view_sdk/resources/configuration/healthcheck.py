from ...mixins import HealthCheckAPIResource


class HealthCheck(HealthCheckAPIResource):
    PARENT_RESOURCE: str = "healthcheck"
    RESOURCE_NAME: str = "config"
    REQUIRES_TENANT = False
