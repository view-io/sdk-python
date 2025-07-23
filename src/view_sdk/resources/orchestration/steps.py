from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
)
from ...models.step_metadata import StepMetadataModel


class Step(
    ExistsAPIResource,
    CreateableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    DeletableAPIResource,
):
    RESOURCE_NAME: str = "steps"
    MODEL = StepMetadataModel
    REQUIRES_TENANT = True

    @classmethod
    def retrieve(cls, resource_guid, incl_subordinates=False, incl_data=False):
        """Retrieve a step by its GUID.

        Args:
            resource_guid (str): The GUID of the step to retrieve.
            incl_subordinates (bool, optional): Whether to include subordinates in the response. Defaults to False.
            incl_data (bool, optional): Whether to include data in the response. Defaults to False.

        Returns:
            The step model with or without subordinates and data, depending on the arguments.
        """
        kwargs = {
            "resource_guid": resource_guid,
        }
        if incl_subordinates:
            kwargs["inclsub"] = None
        if incl_data:
            kwargs["incldata"] = None
        return super().retrieve(**kwargs)
