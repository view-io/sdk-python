from ...mixins import (
    AllRetrievableAPIResource,
    DeletableAPIResource,
    RetrievableAPIResource,
    UpdatableAPIResource,
)
from ...models.multipart_upload import MultipartUploadPartModel
from ...sdk_configuration import Service


class MultipartUploads(
    UpdatableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    DeletableAPIResource,
):
    PARENT_RESOURCE = "buckets"
    PARENT_ID_PARAM = "bucket_guid"
    RESOURCE_NAME: str = "uploads"
    MODEL = MultipartUploadPartModel
    SERVICE = Service.STORAGE
    @classmethod
    def create(cls, bucket_guid: str, **kwargs: MultipartUploadPartModel):
        """
        Args:
            bucket_guid (str): The GUID of the bucket containing the multipart upload.
            **kwargs: Additional keyword arguments for the request.
        Returns:
            The MultipartUploadPartModel object for the specified part.
        """
        cls.MODEL = None
        return super().create(bucket_guid=bucket_guid, _data=kwargs)

    @classmethod
    def retrieve(cls, bucket_guid: str, resource_guid: str):
        """
        Args:
            bucket_guid (str): The GUID of the bucket containing the multipart upload.
            resource_guid (str): The GUID of the multipart upload to retrieve.
        Returns:
            The MultipartUploadPartModel object for the specified part.
        """
        return super().retrieve(resource_guid, bucket_guid=bucket_guid)

    @classmethod
    def retrieve_all(cls, bucket_guid: str):
        """
        Args:
            bucket_guid (str): The GUID of the bucket containing the multipart uploads.
        Returns:
            A list of MultipartUploadPartModel objects for all multipart uploads in the specified bucket.
        """
        return super().retrieve_all(bucket_guid=bucket_guid)

    @classmethod
    def retrieve_part(cls, bucket_guid: str, resource_guid: str, part_number: int):
        """
        Retrieve a specific part of a multipart upload.

        Args:
            bucket_guid (str): The GUID of the bucket containing the multipart upload.
            resource_guid (str): The GUID of the multipart upload to retrieve.
            part_number (int): The number of the part to retrieve.

        Returns:
            The MultipartUploadPartModel object for the specified part.
        """
        cls.QUERY_PARAMS = {"part_number": part_number}
        return super().retrieve(resource_guid, bucket_guid=bucket_guid)

    @classmethod
    def delete_part(cls, bucket_guid: str, resource_guid: str, part_number: int):
        """
        Delete a specific part of a multipart upload.

        Args:
            bucket_guid (str): The GUID of the bucket containing the multipart upload.
            resource_guid (str): The GUID of the multipart upload to delete.
            part_number (int): The number of the part to delete.
        """
        cls.QUERY_PARAMS = {"part_number": part_number}
        return super().delete(resource_guid, bucket_guid=bucket_guid)

    @classmethod
    def upload_part(
        cls, bucket_guid: str, resource_guid: str, part_number: int, data: str
    ):
        """
        Upload a specific part of a multipart upload.

        Args:
            bucket_guid (str): The GUID of the bucket containing the multipart upload.
            resource_guid (str): The GUID of the multipart upload to upload to.
            part_number (int): The number of the part to upload.
            data (str): The data to upload.
        """
        cls.QUERY_PARAMS = {"part_number": part_number}
        headers = {"Content-Type": "text/plain"}
        cls.MODEL = None
        return super().update(
            resource_guid + "/parts/",
            bucket_guid=bucket_guid,
            data=data,
            headers=headers,
        )

    @classmethod
    def complete_upload(cls, bucket_guid: str, resource_guid: str):
        """
        Complete a multipart upload.

        Args:
            bucket_guid (str): The GUID of the bucket containing the multipart upload.
            resource_guid (str): The GUID of the multipart upload to complete.
        """
        cls.UPDATE_METHOD = "POST"
        cls.MODEL = None  # As there's no request body for this endpoint
        return super().update(resource_guid, bucket_guid=bucket_guid)

    @classmethod
    def delete(cls, bucket_guid: str, resource_guid: str):
        """
        Args:
            bucket_guid (str): The GUID of the bucket containing the multipart upload.
            resource_guid (str): The GUID of the multipart upload to delete.
        Returns:
            True if the multipart upload was deleted successfully, False otherwise.
        """
        return super().delete(resource_guid, bucket_guid=bucket_guid)
