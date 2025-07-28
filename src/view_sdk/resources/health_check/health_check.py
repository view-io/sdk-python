from ...mixins import HealthCheckAPIResource


class HealthCheck(HealthCheckAPIResource):
    """Resource for HealthCheck operations."""

    RESOURCE_NAME: str = "healthcheck"
    REQUIRES_TENANT = False

    @classmethod
    def configuration(cls) -> dict:
        """
        Get the configuration of the health check.
        """
        cls.RESOURCE_NAME = cls.RESOURCE_NAME + "/config"
        return super().check()

    @classmethod
    def storage(cls) -> dict:
        """
        Get the storage of the health check.
        """
        cls.RESOURCE_NAME = cls.RESOURCE_NAME + "/storage-rest"
        return super().check()

    @classmethod
    def vector(cls) -> dict:
        """
        Get the vector of the health check.
        """
        cls.RESOURCE_NAME = cls.RESOURCE_NAME + "/vector"
        return super().check()

    @classmethod
    def processor(cls) -> dict:
        """
        Get the processor of the health check.
        """
        cls.RESOURCE_NAME = cls.RESOURCE_NAME + "/processor"
        return super().check()

    @classmethod
    def assistant(cls) -> dict:
        """
        Get the assistant of the health check.
        """
        cls.RESOURCE_NAME = cls.RESOURCE_NAME + "/assistant"
        return super().check()

    @classmethod
    def crawler(cls) -> dict:
        """
        Get the crawler of the health check.
        """
        cls.RESOURCE_NAME = cls.RESOURCE_NAME + "/crawler"
        return super().check()

    @classmethod
    def lexi(cls) -> dict:
        """
        Get the lexi of the health check.
        """
        cls.RESOURCE_NAME = cls.RESOURCE_NAME + "/lexi"
        return super().check()

    @classmethod
    def embeddings(cls) -> dict:
        """
        Get the embeddings of the health check.
        """
        cls.RESOURCE_NAME = cls.RESOURCE_NAME + "/embeddings"
        return super().check()

    @classmethod
    def director(cls) -> dict:
        """
        Get the director of the health check.
        """
        cls.RESOURCE_NAME = cls.RESOURCE_NAME + "/director"
        return super().check()
