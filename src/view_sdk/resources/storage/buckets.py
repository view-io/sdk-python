from typing import List

from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    EnumerableAPIResource,
    RetrievableAPIResource,
    UpdatableAPIResource,
)
from ...models.acl import ACLModel
from ...models.bucket import BucketMetadataModel
from ...models.bucket_enumeration_result import BucketEnumerationResultModel
from ...models.storage_tag import StorageTagModel


class Bucket(
    CreateableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    UpdatableAPIResource,
    DeletableAPIResource,
    EnumerableAPIResource,
):
    RESOURCE_NAME: str = "buckets"
    MODEL = BucketMetadataModel

    @classmethod
    def list_buckets(cls):
        """
        List all buckets.

        Returns:
            A list of BucketMetadataModel objects.
        """
        return super().retrieve_all()

    @classmethod
    def list_objects(cls, resource_guid: str):
        """
        List objects in a bucket.

        Args:
            resource_guid (str): The GUID of the bucket to list objects from.

        Returns:
            A BucketEnumerationResultModel object containing the list of objects.
        """
        cls.MODEL = BucketEnumerationResultModel
        return super().retrieve(resource_guid)

    @classmethod
    def retrieve_metadata(cls, resource_guid: str):
        """
        Retrieve metadata for a bucket.

        Args:
            resource_guid (str): The GUID of the bucket to retrieve metadata for.

        Returns:
            A BucketMetadataModel object containing the bucket metadata.
        """
        return super().retrieve(resource_guid, md=None)


class BucketTags(
    CreateableAPIResource,
    RetrievableAPIResource,
    DeletableAPIResource,
):
    PARENT_RESOURCE = "buckets"
    PARENT_ID_PARAM = "resource_guid"
    RESOURCE_NAME: str = ""
    MODEL = StorageTagModel
    QUERY_PARAMS = {"tags": None}

    @classmethod
    def create(cls, resource_guid: str, tags: List[StorageTagModel]) -> StorageTagModel:
        """
        Create tags for a specific bucket.
        Args:
            resource_guid (str): The unique identifier of the bucket.
            tags (List[StorageTagModel]): A list of StorageTagModel objects to create.

        Returns:
            StorageTagModel: The tags for the bucket.
        """
        kwargs = {"resource_guid": resource_guid, "_data": tags}
        return super().create(**kwargs)


class BucketACL(
    CreateableAPIResource,
    RetrievableAPIResource,
    DeletableAPIResource,
):
    PARENT_RESOURCE = "buckets"
    PARENT_ID_PARAM = "resource_guid"
    RESOURCE_NAME: str = ""
    MODEL = ACLModel
    QUERY_PARAMS = {"acl": None}

    @classmethod
    def create(cls, resource_guid: str, acl: ACLModel) -> ACLModel:
        """
        Create tags for a specific bucket.
        Args:
            resource_guid (str): The unique identifier of the bucket.
            acl (ACLModel): A list of StorageTagModel objects to create.

        Returns:
            StorageTagModel: The tags for the bucket.
        """
        kwargs = {"resource_guid": resource_guid, "_data": acl}
        return super().create(**kwargs)
