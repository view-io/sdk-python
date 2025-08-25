from datetime import datetime
from typing import List

from ...mixins import (
    CreateableAPIResource,
    DeletableAPIResource,
    RetrievableAPIResource,
    UpdatableAPIResource,
)
from ...models.acl import ACLModel
from ...models.object_metadata import ObjectMetadataModel
from ...models.storage_tag import StorageTagModel
from ...sdk_configuration import Service

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
    SERVICE = Service.STORAGE

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
            resource_guid,
            bucket_guid=bucket_guid,
            expiration=expiration_date,
            data={"ExpirationUtc": expiration_date},
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

    @classmethod
    def delete(cls, bucket_guid: str, resource_guid: str):
        """
        Delete an object.
        """
        return super().delete(resource_guid, bucket_guid=bucket_guid)


class ObjectTags(
    RetrievableAPIResource,
    UpdatableAPIResource,
    DeletableAPIResource,
):
    PARENT_RESOURCE = "buckets"
    PARENT_ID_PARAM = "bucket_guid"
    RESOURCE_NAME: str = "objects"
    MODEL = StorageTagModel
    QUERY_PARAMS = {"tags": None}

    @classmethod
    def create_tags(
        cls, bucket_guid: str, resource_guid: str, tags: List[StorageTagModel]
    ) -> StorageTagModel:
        """
        Create tags for a specific object.

        Args:
            resource_guid (str): The unique identifier of the object.
            tags (List[StorageTagModel]): List of tags to create
        Returns:
            StorageTagModel: The tags for the object.
        """
        return super().update(resource_guid, bucket_guid=bucket_guid, data=tags)

    @classmethod
    def read_tags(cls, bucket_guid: str, resource_guid: str):
        """
        Args:
            bucket_guid (str): The GUID of the bucket containing the object.
            resource_guid (str): The GUID of the object to read tags for.
        Returns:
            The tags for the object.
        """
        cls.MODEL = None
        return super().retrieve(resource_guid, bucket_guid=bucket_guid)

    @classmethod
    def delete_tags(cls, bucket_guid: str, resource_guid: str):
        """
        Args:
            bucket_guid (str): The GUID of the bucket containing the object.
            resource_guid (str): The GUID of the object to delete tags for.
        Returns:
            True if the tags were deleted successfully, False otherwise.
        """
        return super().delete(resource_guid, bucket_guid=bucket_guid)


class ObjectACL(
    RetrievableAPIResource,
    UpdatableAPIResource,
    DeletableAPIResource,
):
    PARENT_RESOURCE = "buckets"
    PARENT_ID_PARAM = "bucket_guid"
    RESOURCE_NAME: str = "objects"
    MODEL = ACLModel
    QUERY_PARAMS = {"acl": None}

    @classmethod
    def create_acl(cls, bucket_guid: str, resource_guid: str, acl: ACLModel):
        """
        Args:
            bucket_guid (str): The GUID of the bucket containing the object.
            resource_guid (str): The GUID of the object to create an ACL for.
            acl (ACLModel): The ACL to create.
        Returns:
            The ACL for the object.
        """
        cls.MODEL = None
        return super().update(resource_guid, bucket_guid=bucket_guid, data=acl)

    @classmethod
    def read_acl(cls, bucket_guid: str, resource_guid: str):
        """
        Args:
            bucket_guid (str): The GUID of the bucket containing the object.
            resource_guid (str): The GUID of the object to read ACL for.
        Returns:
            The ACL for the object.
        """
        cls.MODEL = None
        return super().retrieve(resource_guid, bucket_guid=bucket_guid)

    @classmethod
    def delete_acl(cls, bucket_guid: str, resource_guid: str):
        """
        Args:
            bucket_guid (str): The GUID of the bucket containing the object.
            resource_guid (str): The GUID of the object to delete ACL for.
        Returns:
            True if the ACL was deleted successfully, False otherwise.
        """
        return super().delete(resource_guid, bucket_guid=bucket_guid)
