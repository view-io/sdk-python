from typing import List

from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    RetrievableAPIResource,
    UpdatableAPIResource,
    EnumerableAPIResource,
)
from ...models.acl import ACLModel
from ...models.acl_entry import ACLEntryModel
from ...models.bucket import BucketMetadataModel
from ...models.bucket_enumeration_result import BucketEnumerationResultModel
from ...models.storage_tag import StorageTagModel
from ...sdk_configuration import Service, get_client
from ...utils.url_helper import _get_url_v1


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
    SERVICE = Service.STORAGE

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
    SERVICE = Service.STORAGE

    @classmethod
    def retrieve(cls, resource_guid: str, **kwargs) -> List[StorageTagModel]:
        """
        Retrieve tags for a specific bucket.
        Args:
            resource_guid (str): The unique identifier of the bucket.
            **kwargs: Additional keyword arguments for the request.

        Returns:
            List[StorageTagModel]: The tags for the bucket.
        """
        # Construct the URL manually to ensure correct path
        client = get_client(cls.SERVICE)
        url = _get_url_v1(cls, client.tenant_guid, "buckets", resource_guid, **cls.QUERY_PARAMS)
        headers = kwargs.pop("headers", {})
        response = client.request("GET", url, headers=headers)
        
        # Handle the response validation
        if isinstance(response, list):
            return [StorageTagModel.model_validate(tag) for tag in response]
        else:
            return StorageTagModel.model_validate(response)

    @classmethod
    def create(cls, resource_guid: str, tags: List[StorageTagModel]) -> List[StorageTagModel]:
        """
        Create tags for a specific bucket.
        Args:
            resource_guid (str): The unique identifier of the bucket.
            tags (List[StorageTagModel]): A list of StorageTagModel objects to create.

        Returns:
            List[StorageTagModel]: The created tags for the bucket.
        """
        kwargs = {"resource_guid": resource_guid, "_data": tags}
        # Temporarily set MODEL to None to prevent parent validation
        original_model = cls.MODEL
        cls.MODEL = None
        
        try:
            # Call the parent create method without model validation
            response = super().create(**kwargs)
            
            # Handle the response validation ourselves
            if isinstance(response, list):
                return [StorageTagModel.model_validate(tag) for tag in response]
            else:
                return StorageTagModel.model_validate(response)
        finally:
            # Restore the original model
            cls.MODEL = original_model


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
    SERVICE = Service.STORAGE

    @classmethod
    def retrieve(cls, resource_guid: str, **kwargs) -> List[ACLModel]:
        """
        Retrieve ACL for a specific bucket.
        Args:
            resource_guid (str): The unique identifier of the bucket.
            **kwargs: Additional keyword arguments for the request.

        Returns:
            List[ACLModel]: The ACL entries for the bucket.
        """
        # Construct the URL manually to ensure correct path
        client = get_client(cls.SERVICE)
        url = _get_url_v1(cls, client.tenant_guid, "buckets", resource_guid, **cls.QUERY_PARAMS)
        headers = kwargs.pop("headers", {})
        response = client.request("GET", url, headers=headers)
        
        # Handle the response validation
        if isinstance(response, list):
            return [ACLModel.model_validate(entry) for entry in response]
        else:
            return ACLModel.model_validate(response)

    @classmethod
    def create(cls, resource_guid: str, acl: ACLEntryModel) -> List[ACLEntryModel]:
        """
        Create ACL for a specific bucket.
        Args:
            resource_guid (str): The unique identifier of the bucket.
            acl (ACLEntryModel): The ACL entry model to create.

        Returns:
            List[ACLEntryModel]: The created ACL entries for the bucket.
        """
        kwargs = {"resource_guid": resource_guid, "_data": acl}
        # Temporarily set MODEL to None to prevent parent validation
        original_model = cls.MODEL
        cls.MODEL = None
        
        try:
            # Call the parent create method without model validation
            response = super().create(**kwargs)
            
            # Handle the response validation ourselves
            if isinstance(response, list):
                return [ACLEntryModel.model_validate(entry) for entry in response]
            else:
                return ACLEntryModel.model_validate(response)
        finally:
            # Restore the original model
            cls.MODEL = original_model
