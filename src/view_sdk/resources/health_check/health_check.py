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
        original_name = cls.RESOURCE_NAME
        cls.RESOURCE_NAME = "healthcheck/config"
        result = super().check()
        cls.RESOURCE_NAME = original_name
        return result

    @classmethod
    def storage(cls) -> dict:
        """
        Get the storage of the health check.
        """
        original_name = cls.RESOURCE_NAME
        cls.RESOURCE_NAME = "healthcheck/storage-rest"
        result = super().check()
        cls.RESOURCE_NAME = original_name
        return result

    @classmethod
    def vector(cls) -> dict:
        """
        Get the vector of the health check.
        """
        original_name = cls.RESOURCE_NAME
        cls.RESOURCE_NAME = "healthcheck/vector"
        result = super().check()
        cls.RESOURCE_NAME = original_name
        return result

    @classmethod
    def processor(cls) -> dict:
        """
        Get the processor of the health check.
        """
        original_name = cls.RESOURCE_NAME
        cls.RESOURCE_NAME = "healthcheck/processor"
        result = super().check()
        cls.RESOURCE_NAME = original_name
        return result

    @classmethod
    def assistant(cls) -> dict:
        """
        Get the assistant of the health check.
        """
        original_name = cls.RESOURCE_NAME
        cls.RESOURCE_NAME = "healthcheck/assistant"
        result = super().check()
        cls.RESOURCE_NAME = original_name
        return result

    @classmethod
    def crawler(cls) -> dict:
        """
        Get the crawler of the health check.
        """
        original_name = cls.RESOURCE_NAME
        cls.RESOURCE_NAME = "healthcheck/crawler"
        result = super().check()
        cls.RESOURCE_NAME = original_name
        return result

    @classmethod
    def lexi(cls) -> dict:
        """
        Get the lexi of the health check.
        """
        original_name = cls.RESOURCE_NAME
        cls.RESOURCE_NAME = "healthcheck/lexi"
        result = super().check()
        cls.RESOURCE_NAME = original_name
        return result

    @classmethod
    def embeddings(cls) -> dict:
        """
        Get the embeddings of the health check.
        """
        original_name = cls.RESOURCE_NAME
        cls.RESOURCE_NAME = "healthcheck/embeddings"
        result = super().check()
        cls.RESOURCE_NAME = original_name
        return result

    @classmethod
    def director(cls) -> dict:
        """
        Get the director of the health check.
        """
        original_name = cls.RESOURCE_NAME
        cls.RESOURCE_NAME = "healthcheck/director"
        result = super().check()
        cls.RESOURCE_NAME = original_name
        return result
