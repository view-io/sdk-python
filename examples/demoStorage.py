import view_sdk
from view_sdk import storage
from view_sdk.sdk_configuration import Service

sdk = view_sdk.configure(
    access_key="default",
    base_url="192.168.101.63",
    tenant_guid="00000000-0000-0000-0000-000000000000",
    service_ports={Service.STORAGE: 8001},
)


def completeMultipartUpload():
    object = storage.MultipartUploads.complete_upload(
        "fa099b91-8f4d-4b32-8d2a-1761e4a3740a", "foo.txt"
    )
    print(object)


# completeMultipartUpload()


def deleteMultipartUpload():
    object = storage.MultipartUploads.delete(
        "fa099b91-8f4d-4b32-8d2a-1761e4a3740a", "foo.txt"
    )
    print(object)


# deleteMultipartUpload()


def deleteMultipartUploadPart():
    object = storage.MultipartUploads.delete_part(
        "fa099b91-8f4d-4b32-8d2a-1761e4a3740a", "foo.txt", 1
    )
    print(object)


# deleteMultipartUploadPart()


def readMultipartUploadPart():
    object = storage.MultipartUploads.retrieve_part(
        "fa099b91-8f4d-4b32-8d2a-1761e4a3740a", "foo.txt", 1
    )
    print(object)


# readMultipartUploadPart()


def uploadMultipartUpload():
    object = storage.MultipartUploads.upload_part(
        "fa099b91-8f4d-4b32-8d2a-1761e4a3740a", "foo.txt", 1, "test"
    )
    print(object)


# uploadMultipartUpload()


def readAllMultipartUploads():
    object = storage.MultipartUploads.retrieve_all(
        "fa099b91-8f4d-4b32-8d2a-1761e4a3740a"
    )
    print(object)


# readAllMultipartUploads()


def retrieveMultipartUpload():
    object = storage.MultipartUploads.retrieve(
        "fa099b91-8f4d-4b32-8d2a-1761e4a3740a",
        "foo.txt",
    )
    print(object)


# retrieveMultipartUpload()


def createMultipartUpload():
    object = storage.MultipartUploads.create(
        bucket_guid="00000000-0000-0000-0000-000000000000", Key="test_sdk.new"
    )
    print(object)


#createMultipartUpload()


def deleteObject():
    object = storage.Object.delete(
        "fa099b91-8f4d-4b32-8d2a-1761e4a3740a", "test_sdk.new"
    )
    print(object)


# deleteObject()


def deleteObjectACL():
    object = storage.ObjectACL.delete_acl(
        "fa099b91-8f4d-4b32-8d2a-1761e4a3740a", "test_sdk.new"
    )
    print(object)


# deleteObjectACL()


def readObjectACL():
    object = storage.ObjectACL.read_acl(
        "fa099b91-8f4d-4b32-8d2a-1761e4a3740a", "test_sdk.new"
    )
    print(object)


# readObjectACL()


def createObjectACL():
    object = storage.ObjectACL.create_acl(
        "fa099b91-8f4d-4b32-8d2a-1761e4a3740a",
        "test_sdk.new",
        {
            "Owner": {
                "GUID": "00000000-0000-0000-0000-000000000000",
                "TenantGUID": "00000000-0000-0000-0000-000000000000",
                "FirstName": "Default",
                "LastName": "User",
                "FullName": "Default User",
                "Notes": "Default password is password",
                "Email": "default@user.com",
                "Active": True,
                "CreatedUtc": "2024-08-06T16:40:20.223290Z",
            },
            "Users": [],
            "Entries": [],
        },
    )
    print(object)


# createObjectACL()


def deleteObjectTags():
    object = storage.ObjectTags.delete_tags(
        "fa099b91-8f4d-4b32-8d2a-1761e4a3740a", "test_sdk.new"
    )
    print(object)


# deleteObjectTags()


def readObjectTags():
    object = storage.ObjectTags.read_tags(
        "00000000-0000-0000-0000-000000000000", "test_sdk.new"
    )
    print(object)


# readObjectTags()


def createObjectTags():
    object = storage.ObjectTags.create_tags(
        "00000000-0000-0000-0000-000000000000",
        "test_sdk.new",
        [{"Key": "Name", "Value": "testbucket"}],
    )
    print(object)


# createObjectTags()


def setObjectExpiration():
    object = storage.Object.set_expiration(
        "00000000-0000-0000-0000-000000000000",
        "test_sdk.new",
        "2025-08-06T16:30:09.495213Z",
    )
    print(object)


# setObjectExpiration()


def readObjectMetadata():
    object = storage.Object.retrieve_metadata(
        "00000000-0000-0000-0000-000000000000", "test_sdk.new"
    )
    print(object)


# readObjectMetadata()


def readObjectDataInRange():
    object = storage.Object.retrieve_range(
        "00000000-0000-0000-0000-000000000000", "test_sdk.new", 0, 1
    )
    print(object)


# readObjectDataInRange()


def readObjectData():
    object = storage.Object.retrieve("00000000-0000-0000-0000-000000000000", "test_sdk.new")
    print(object)


#readObjectData()


def writeObject():
    object = storage.Object.write_chunked(
        "00000000-0000-0000-0000-000000000000", "test_sdk.new", "test"
    )
    print(object)


# writeObject()


def deleteBucketACL():
    bucket = storage.BucketACL.delete("00000000-0000-0000-0000-000000000000")
    print(bucket)


# deleteBucketACL()


def readBucketACL():
    bucket = storage.BucketACL.retrieve("00000000-0000-0000-0000-000000000000")
    print(bucket)


#readBucketACL()


def createBucketACL():
    bucket = storage.BucketACL.create(
        "00000000-0000-0000-0000-000000000000",
        {
            "Owner": {
                "GUID": "00000000-0000-0000-0000-000000000000",
                "TenantGUID": "00000000-0000-0000-0000-000000000000",
                "FirstName": "Default",
                "LastName": "User",
                "FullName": "Default User",
                "Notes": "Default password is password",
                "Email": "default@user.com",
                "Active": True,
                "CreatedUtc": "2024-08-06T16:30:09.495213Z",
            },
            "Users": [
                {
                    "GUID": "00000000-0000-0000-0000-000000000000",
                    "TenantGUID": "00000000-0000-0000-0000-000000000000",
                    "FirstName": "Default",
                    "LastName": "User",
                    "FullName": "Default User",
                    "Notes": "Default password is password",
                    "Email": "default@user.com",
                    "Active": True,
                    "CreatedUtc": "2024-08-06T16:30:09.495213Z",
                }
            ],
            "Entries": [
                {
                    "GUID": "00000000-0000-0000-0000-000000000000",
                    "TenantGUID": "00000000-0000-0000-0000-000000000000",
                    "BucketGUID": "00000000-0000-0000-0000-000000000000",
                    "OwnerGUID": "00000000-0000-0000-0000-000000000000",
                    "UserGUID": "00000000-0000-0000-0000-000000000000",
                    "CanonicalUser": "",
                    "EnableRead": True,
                    "EnableReadAcp": True,
                    "EnableWrite": True,
                    "EnableWriteAcp": True,
                    "FullControl": True,
                    "CreatedUtc": "2024-08-06T16:30:09.643691Z",
                }
            ],
        },
    )
    print(bucket)


#createBucketACL()


def deleteBucketTag():
    bucket = storage.BucketTags.delete("00000000-0000-0000-0000-000000000000")
    print(bucket)


# deleteBucketTag()


def readBucketTag():
    bucket = storage.BucketTags.retrieve("00000000-0000-0000-0000-000000000000")
    print(bucket)


#readBucketTag()


def createBucketTags():
    bucket = storage.BucketTags.create(
        "00000000-0000-0000-0000-000000000000",
        [
            {"Key": "Name", "Value": "testbucket"},
        ],
    )
    print(bucket)


# createBucketTags()


def deleteBucket():
    bucket = storage.Bucket.delete("00000000-0000-0000-0000-000000000000")
    print(bucket)


# deleteBucket()


def updateBucket():
    bucket = storage.Bucket.update(
        "00000000-0000-0000-0000-000000000000",
        Name="testbucket",
        RegionString="us-west-1",
        Versioning=True,
    )
    print(bucket)


#updateBucket()


def readBucketMetadata():
    bucket = storage.Bucket.retrieve_metadata("00000000-0000-0000-0000-000000000000")
    print(bucket)


#readBucketMetadata()


def readAllObjects():
    objects = storage.Bucket.list_objects("00000000-0000-0000-0000-000000000000")
    print(objects)


#readAllObjects()


def readAllBuckets():
    buckets = storage.Bucket.list_buckets()
    print(buckets)


# readAllBuckets()


def createBucket():
    bucket = storage.Bucket.create(
        PoolGUID="00000000-0000-0000-0000-000000000000",
        Name="testbucket",
        RegionString="us-west-1",
        Versioning=True,
    )
    print(bucket)


# createBucket()



def existsStoragePool():
    storagePool = storage.Pool.exists("00000000-0000-0000-0000-000000000000")
    print(storagePool)


#existsStoragePool()


def deleteStoragePool():
    storagePool = storage.Pool.delete("00000000-0000-0000-0000-000000000000")
    print(storagePool)


# deleteStoragePool()


def updateStoragePool():
    storagePool = storage.Pool.update(
        "00000000-0000-0000-0000-000000000000",
        Name="My disk storage pool [updated]",
        Provider="Disk",
        WriteMode="GUID",
        UseSsl=False,
        DiskDirectory="./disk/",
        Compress="None",
        EnableReadCaching=False,
    )
    print(storagePool)

# updateStoragePool()


def readStoragePool():
    storagePool = storage.Pool.retrieve("00000000-0000-0000-0000-000000000000")
    print(storagePool)


# readStoragePool()


def readAllStoragePools():
    storagePools = storage.Pool.retrieve_all()
    print(storagePools)


# readAllStoragePools()


def createStoragePool():
    storagePool = storage.Pool.create(
        Name="My disk storage pool",
        Provider="AwsS3",
        WriteMode="GUID",
        UseSsl=False,
        Endpoint="https://s3.amazonaws.com",
        AccessKey="AKIAIOSFODNN7EXAMPLE",
        SecretKey="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
        BucketName="my-production-bucket",
        RegionString="us-west-1"
    )
    print(storagePool)

createStoragePool()
