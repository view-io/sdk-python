from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    EnumerableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
)
from ...models.crawl_operation_request import CrawlOperationRequestModel
from ...sdk_configuration import get_client
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
    RESOURCE_NAME: str = "crawloperations"
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
        # For start operation, we need to construct the URL manually
        client = get_client(cls.SERVICE)
        url = _get_url_v1(
            cls, client.tenant_guid, "crawloperations", operation_guid, "start"
        )
        data = cls._dump_model_data(kwargs, cls.REQUEST_MODEL)
        response = client.request(cls.CREATE_METHOD, url, json=data)
        return response

    @classmethod
    def stop(cls, operation_guid: str, **kwargs: CrawlOperationRequestModel):
        """Stop a crawl operation.

        Args:
            operation_guid (str): The GUID of the crawl operation to stop
            **kwargs: Additional arguments validated against CrawlOperationRequestModel

        Returns:
            The created crawl operation response
        """
        # For stop operation, we need to construct the URL manually
        client = get_client(cls.SERVICE)
        url = _get_url_v1(
            cls, client.tenant_guid, "crawloperations", operation_guid, "stop"
        )
        data = cls._dump_model_data(kwargs, cls.REQUEST_MODEL)
        response = client.request(cls.CREATE_METHOD, url, json=data)
        return response

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
