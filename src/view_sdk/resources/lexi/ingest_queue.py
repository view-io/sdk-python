from ...mixins import (
    AllRetrievableAPIResource,
    DeletableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
    RetrievableStatisticsMixin,
)
from ...models.ingestion_queue_entry import IngestionQueueEntryModel
from ...models.ingestion_queue_statistics import IngestQueueStatisticsModel
from ...sdk_configuration import get_client
from ...utils.url_helper import _get_url_v1


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

    @classmethod
    def retrieve_statistics(cls, **kwargs):
        """
        Retrieves general statistics for the ingest queue (without requiring a specific GUID).

        Returns:
            STATS_MODEL: The ingest queue statistics data.

        Raises:
            ValueError: If tenant GUID is required but not provided.
        """
        client = get_client(cls.SERVICE)

        if cls.REQUIRES_TENANT and client.tenant_guid is None:
            raise ValueError("Tenant GUID is required for this resource.")

        path_components, url_params = cls._get_resource_path(**kwargs)
        if cls.REQUIRES_TENANT:
            url = _get_url_v1(cls, client.tenant_guid, *path_components, stats=None, **url_params)
        else:
            url = _get_url_v1(cls, *path_components, stats=None, **url_params)

        response = client.request("GET", url)
        return cls.STATS_MODEL.model_validate(response) if cls.STATS_MODEL else response
