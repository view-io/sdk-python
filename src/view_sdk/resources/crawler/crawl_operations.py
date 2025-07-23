from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    EnumerableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
)
from ...models.crawl_operation_request import CrawlOperationRequestModel
from ...sdk_configuration import Service, get_client
from ...utils.url_helper import _get_url_v1


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
    
    @classmethod
    def enumerateCrawlOperation(cls, operation_guid: str):
        """Enumerate crawl operation.

        Args:
            operation_guid (str): The GUID of the crawl operation to enumerate
            **kwargs: Additional arguments for enumeration

        Returns:
            The enumerated crawl operation
        """
        client = get_client(cls.SERVICE)
        url = _get_url_v1(cls, cls.PARENT_RESOURCE, operation_guid, "enumeration")
        response = client.request("GET", url)
        return response
