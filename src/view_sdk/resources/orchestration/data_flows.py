from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
)
from ...models.data_flow import DataFlowModel
from ...sdk_configuration import get_client
from ...sdk_logging import logger
from ...utils.url_helper import _get_url_v1


class DataFlow(
    ExistsAPIResource,
    CreateableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    DeletableAPIResource,
):
    RESOURCE_NAME: str = "dataflows"
    MODEL = DataFlowModel

    @classmethod
    def retrieve(cls, resource_guid, with_steps=False):
        """Retrieve a data flow by its GUID.

        Args:
            resource_guid (str): The GUID of the data flow to retrieve.
            with_steps (bool, optional): Whether to include steps in the response. Defaults to False.

        Returns:
            The data flow model with or without steps, depending on the with_steps argument.
        """
        kwargs = {
            "resource_guid": resource_guid,
        }
        if with_steps:
            kwargs["inclsub"] = None
        return super().retrieve(**kwargs)

    @classmethod
    def retrieve_request_performance_data(cls, request_guid: str):
        """Retrieve request performance data for a data flow.

        Args:
            request_guid (str): The GUID of the request to retrieve performance data for.

        Returns:
            The performance data for the specified request.
        """
        cls.PARENT_RESOURCE: str = "dataflows"
        cls.PARENT_ID_PARAM: str = None
        cls.RESOURCE_NAME: str = "processor/performance"

        if not request_guid:
            raise ValueError("request_guid is required")

        client = get_client(cls.SERVICE)
        if cls.REQUIRES_TENANT and client.tenant_guid is None:
            raise ValueError("Tenant GUID is required for this resource.")

        try:
            url = _get_url_v1(
                cls,
                client.tenant_guid,
                cls.PARENT_RESOURCE,
                cls.RESOURCE_NAME,
                request=request_guid,
            )
            response = client.request("GET", url)
            return cls.MODEL.model_validate(response)
        except Exception as e:
            logger.warning(f"Failed to retrieve request performance data: {e}")
            return None
