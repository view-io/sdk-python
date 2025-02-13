from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    RetrievableAPIResource,
    UpdatableAPIResource,
)
from ...models.multipart_upload import MultipartUploadPartModel


class MultipartUploads(
    CreateableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    UpdatableAPIResource,
    DeletableAPIResource,
):
    PARENT_RESOURCE = "buckets"
    PARENT_ID_PARAM = "bucket_guid"
    RESOURCE_NAME: str = "uploads"
    MODEL = MultipartUploadPartModel

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
        cls.QUERY_PARAMS = {"parts": None, "part_number": part_number}
        headers = {"Content-Type": "text/plain"}
        return super().create(
            resource_guid, bucket_guid=bucket_guid, data=data, headers=headers
        )

    @classmethod
    def complete_upload(cls, bucket_guid: str, resource_guid: str):
        """
        Complete a multipart upload.

        Args:
            bucket_guid (str): The GUID of the bucket containing the multipart upload.
            resource_guid (str): The GUID of the multipart upload to complete.
        """
        cls.CREATE_METHOD = "POST"
        cls.MODEL = None  # As there's no request body for this endpoint
        return super().create(resource_guid, bucket_guid=bucket_guid)
