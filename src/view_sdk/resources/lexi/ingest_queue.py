from ...mixins import (
    AllRetrievableAPIResource,
    DeletableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
    RetrievableStatisticsMixin,
)
from ...models.ingestion_queue_entry import IngestionQueueEntryModel
from ...models.ingestion_queue_statistics import IngestQueueStatisticsModel


class IngestQueue(
    ExistsAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    DeletableAPIResource,
    RetrievableStatisticsMixin,
):
    """
    Resource class for managing ingest queue entries.
    Provides functionality to check existence, retrieve, list all, and delete queue entries.
    """

    RESOURCE_NAME: str = "ingestqueue"
    MODEL = IngestionQueueEntryModel
    STATS_MODEL = IngestQueueStatisticsModel
    REQUIRES_TENANT = True
