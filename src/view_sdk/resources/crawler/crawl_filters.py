from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    EnumerableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
    UpdatableAPIResource,
)
from ...models.crawl_filter import CrawlFilterModel


class CrawlFilter(
    ExistsAPIResource,
    CreateableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    UpdatableAPIResource,
    DeletableAPIResource,
    EnumerableAPIResource,
):
    RESOURCE_NAME: str = "crawlfilters"
    MODEL = CrawlFilterModel
