from datetime import datetime
from typing import List

from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    RetrievableAPIResource,
    UpdatableAPIResource,
)
from ...models.acl import ACLModel
from ...models.object_metadata import ObjectMetadataModel
from ...models.storage_tag import StorageTagModel


class Object(
    CreateableAPIResource,
    RetrievableAPIResource,
    UpdatableAPIResource,
    DeletableAPIResource,
):
    PARENT_RESOURCE = "buckets"
    PARENT_ID_PARAM = "bucket_guid"
    RESOURCE_NAME: str = "objects"
    MODEL = None

    @classmethod
    def retrieve(cls, bucket_guid: str, resource_guid: str):
        """
        Retrieve a range of bytes from an object.

        Args:
            bucket_guid (str): The GUID of the bucket containing the object.
            resource_guid (str): The GUID of the object to retrieve.
            start (int): The start byte of the range.
            end (int): The end byte of the range.
        """
        return super().retrieve(resource_guid, bucket_guid=bucket_guid)

    @classmethod
    def retrieve_metadata(cls, bucket_guid: str, resource_guid: str):
        """
        Retrieve metadata for an object.

        Args:
            bucket_guid (str): The GUID of the bucket containing the object.
            resource_guid (str): The GUID of the object to retrieve metadata for.

        Returns:
            The ObjectMetadataModel object for the specified object.
        """
        cls.MODEL = ObjectMetadataModel
        cls.QUERY_PARAMS = {"md": None}
        return super().retrieve(resource_guid, bucket_guid=bucket_guid)

    @classmethod
    def set_expiration(
        cls, bucket_guid: str, resource_guid: str, expiration_date: datetime
    ):
        """
        Set the expiration date for an object.

        Args:
            bucket_guid (str): The GUID of the bucket containing the object.
            resource_guid (str): The GUID of the object to set the expiration date for.
            expiration_date (datetime): The expiration date to set.
        """
        cls.MODEL = ObjectMetadataModel
        cls.QUERY_PARAMS = {"expiration": None}
        return super().update(
            resource_guid, bucket_guid=bucket_guid, expiration=expiration_date
        )

    @classmethod
    def retrieve_range(cls, bucket_guid: str, resource_guid: str, start: int, end: int):
        """
        Retrieve a range of bytes from an object.

        Args:
            bucket_guid (str): The GUID of the bucket containing the object.
            resource_guid (str): The GUID of the object to retrieve.
            start (int): The start byte of the range.
            end (int): The end byte of the range.
        """
        headers = {"Range": f"bytes={start}-{end}"}
        return super().retrieve(resource_guid, bucket_guid=bucket_guid, headers=headers)

    @classmethod
    def write_non_chunked(cls, bucket_guid: str, resource_guid: str, data: str):
        """
        Write non-chunked data to an object.

        Args:
            bucket_guid (str): The GUID of the bucket containing the object.
            resource_guid (str): The GUID of the object to write to.
            data (str): The data to write.
        """
        headers = {"Content-Type": "text/plain"}
        return super().update(
            resource_guid, bucket_guid=bucket_guid, data=data, headers=headers
        )

    # TODO: Properly implement this
    @classmethod
    def write_chunked(cls, bucket_guid: str, resource_guid: str, data: str):
        """
        Write chunked data to an object.

        Args:
            bucket_guid (str): The GUID of the bucket containing the object.
            resource_guid (str): The GUID of the object to write to.
            data (str): The data to write.
        """
        headers = {"Content-Type": "text/plain", "x-amz-content-sha256": "STREAMING"}
        return super().update(
            resource_guid, bucket_guid=bucket_guid, data=data, headers=headers
        )


class ObjectTags(
    CreateableAPIResource,
    AllRetrievableAPIResource,
    DeletableAPIResource,
):
    PARENT_RESOURCE = "objects"
    PARENT_ID_PARAM = "resource_guid"
    RESOURCE_NAME: str = ""
    MODEL = StorageTagModel

    @classmethod
    def create(cls, resource_guid: str, tags: List[StorageTagModel]) -> StorageTagModel:
        """
        Create tags for a specific object.

        Args:
            resource_guid (str): The unique identifier of the object.
            tags (List[StorageTagModel]): List of tags to create
        Returns:
            StorageTagModel: The tags for the object.
        """
        kwargs = {"resource_guid": resource_guid, "_data": tags}
        return super().create(**kwargs)


class ObjectACL(
    CreateableAPIResource,
    AllRetrievableAPIResource,
    DeletableAPIResource,
):
    PARENT_RESOURCE = "objects"
    PARENT_ID_PARAM = "resource_guid"
    RESOURCE_NAME: str = ""
    MODEL = ACLModel
    QUERY_PARAMS = {"acl": None}
