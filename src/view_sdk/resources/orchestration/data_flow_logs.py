from typing import List, Optional

from ...mixins import AllRetrievableAPIResource, RetrievableAPIResource
from ...models.data_flow_log import DataFlowLogModel
from ...sdk_configuration import get_client
from ...sdk_logging import logger
from ...utils.url_helper import _get_url_v1


class DataFlowLog(AllRetrievableAPIResource, RetrievableAPIResource):
    RESOURCE_NAME: str = "dataflows"
    MODEL = DataFlowLogModel
    REQUIRES_TENANT = True

    PARENT_RESOURCE: str = "dataflows"
    PARENT_ID_PARAM: str = "data_flow_guid"

    @classmethod
    def retrieve_all(
        cls, data_flow_guid: str, request_guid: str
    ) -> List[DataFlowLogModel]:
        """Retrieve all data flow logs.

        Args:
            data_flow_guid (str): Data flow GUID
            request_guid (str): Request GUID

        Returns:
            List[DataFlowLogModel]: List of data flow logs
        """
        if not data_flow_guid:
            raise ValueError("data_flow_guid is required")
        if not request_guid:
            raise ValueError("request_guid is required")

        client = get_client(cls.SERVICE)
        if cls.REQUIRES_TENANT and client.tenant_guid is None:
            raise ValueError("Tenant GUID is required for this resource.")

        url = _get_url_v1(
            cls,
            client.tenant_guid,
            cls.PARENT_RESOURCE,
            data_flow_guid,
            "logs",
            request=request_guid,
        )

        instances = client.request("GET", url)
        return [cls.MODEL.model_validate(instance) for instance in instances]

    @classmethod
    def retrieve_logfile(cls, data_flow_guid: str, request_guid: str) -> Optional[str]:
        """Retrieve data flow logfile.

        Args:
            data_flow_guid (str): Data flow GUID
            request_guid (str): Request GUID

        Returns:
            Optional[str]: Log file content if successful, None otherwise
        """
        if not data_flow_guid:
            raise ValueError("data_flow_guid is required")
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
                data_flow_guid,
                "logfile",
                request=request_guid,
            )
            return client.request("GET", url)
        except Exception as e:
            logger.warning(f"Failed to retrieve logfile: {str(e)}")
            return None
