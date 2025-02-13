from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    EnumerableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
)
from ...models.crawl_operation_request import CrawlOperationRequestModel


class CrawlOperation(
    ExistsAPIResource,
    CreateableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    DeletableAPIResource,
    EnumerableAPIResource,
):
    CREATE_METHOD = "POST"
    PARENT_RESOURCE = "crawloperations"
    PARENT_ID_PARAM = "operation_guid"
    RESOURCE_NAME: str = "start"
    REQUEST_MODEL = CrawlOperationRequestModel

    @classmethod
    def start(cls, operation_guid: str, **kwargs: CrawlOperationRequestModel):
        """Start a crawl operation.

        Args:
            operation_guid (str): The GUID of the crawl operation to start
            **kwargs: Additional arguments validated against CrawlOperationRequestModel

        Returns:
            The created crawl operation response
        """
        return super().create(operation_guid=operation_guid, **kwargs)

    @classmethod
    def stop(cls, operation_guid: str, **kwargs: CrawlOperationRequestModel):
        """Stop a crawl operation.

        Args:
            operation_guid (str): The GUID of the crawl operation to stop
            **kwargs: Additional arguments validated against CrawlOperationRequestModel

        Returns:
            The created crawl operation response
        """
        return super().create(operation_guid=operation_guid, **kwargs)
