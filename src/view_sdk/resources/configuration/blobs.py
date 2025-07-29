from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    EnumerableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
    UpdatableAPIResource,
)
from ...models.blob import BlobModel
from ...sdk_configuration import Service


class Blob(
    ExistsAPIResource,
    CreateableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    DeletableAPIResource,
    UpdatableAPIResource,
    EnumerableAPIResource,
):
    RESOURCE_NAME: str = "blobs"
    MODEL = BlobModel
    SERVICE = Service.DEFAULT

    @classmethod
    def retrieve(cls, resource_guid: str, include_data=False) -> BlobModel:
        """
        Retrieves a blob.

        Args:
            resource_guid: The ID of the blob to retrieve.
            include_data: Whether to include the blob data in the response.

        Returns:
            BlobModel: The retrieved blob.
        """
        return super().retrieve(resource_guid, incldata=None if include_data else None)
