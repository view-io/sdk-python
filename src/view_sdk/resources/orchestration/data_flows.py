from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
)
from ...models.data_flow import DataFlowModel


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
    def retrieve_request_performance_data(cls, dataflow_guid: str, request_guid: str):
        """Retrieve request performance data for a data flow.

        Args:
            dataflow_guid (str): The GUID of the data flow to retrieve performance data for.
            request_guid (str): The GUID of the request to retrieve performance data for.

        Returns:
            The performance data for the specified request.
        """
        cls.QUERY_PARAMS = {
            "request": request_guid,
        }
        return super().retrieve(dataflow_guid + "/performance")

    @classmethod
    def retrieve_request_log_metadata(cls, dataflow_guid: str, request_guid: str):
        """Retrieve request log metadata for a data flow.

        Args:
            dataflow_guid (str): The GUID of the data flow to retrieve performance data for.
            request_guid (str): The GUID of the request to retrieve performance data for.

        Returns:
            The log metadata for the specified request.
        """
        cls.QUERY_PARAMS = {
            "request": request_guid,
        }
        cls.MODEL = None
        return super().retrieve(dataflow_guid + "/logs")

    @classmethod
    def retrieve_request_log_file(cls, dataflow_guid: str, request_guid: str):
        """Retrieve request log file for a data flow.

        Args:
            dataflow_guid (str): The GUID of the data flow to retrieve performance data for.
            request_guid (str): The GUID of the request to retrieve performance data for.

        Returns:
            The log file for the specified request.
        """
        cls.QUERY_PARAMS = {
            "request": request_guid,
        }
        cls.MODEL = None
        return super().retrieve(dataflow_guid + "/logfile")
