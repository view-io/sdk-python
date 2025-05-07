import view_sdk
from view_sdk import storage

sdk = view_sdk.configure( access_key="default",base_url="ampere.view.io", secure=True, tenant_guid= "00000000-0000-0000-0000-000000000000")

def deleteBucketACL():
    bucket = storage.BucketACL.delete("00000000-0000-0000-0000-000000000000")
    print(bucket)

deleteBucketACL()

def readBucketACL():
    bucket = storage.BucketACL.retrieve("00000000-0000-0000-0000-000000000000")
    print(bucket)

# readBucketACL()

def createBucketACL():
    bucket = storage.BucketACL.create("00000000-0000-0000-0000-000000000000",
    {
          "Owner": {
                "GUID": "default",
                "TenantGUID": "default",
                "FirstName": "Default",
                "LastName": "User",
                "FullName": "Default User",
                "Notes": "Default password is password",
                "Email": "default@user.com",
                "Active": True,
                "CreatedUtc": "2024-08-06T16:30:09.495213Z"
             },
    "Users": [
        {
            "GUID": "default",
            "TenantGUID": "default",
            "FirstName": "Default",
            "LastName": "User",
            "FullName": "Default User",
            "Notes": "Default password is password",
            "Email": "default@user.com",
            "Active": True,
            "CreatedUtc": "2024-08-06T16:30:09.495213Z"
        }
    ],
    "Entries": [
        {
            "GUID": "default",
            "TenantGUID": "default",
            "BucketGUID": "example-data-bucket",
            "OwnerGUID": "default",
            "UserGUID": "default",
            "CanonicalUser": "",
            "EnableRead": True,
            "EnableReadAcp": True,
            "EnableWrite": True,
            "EnableWriteAcp": True,
            "FullControl": True,
            "CreatedUtc": "2024-08-06T16:30:09.643691Z"
        }
        ]
    }
    )
    print(bucket)

# createBucketACL()

def deleteBucketTag():
    bucket = storage.BucketTags.delete("00000000-0000-0000-0000-000000000000")
    print(bucket)

# deleteBucketTag()

def readBucketTag():
    bucket = storage.BucketTags.retrieve("00000000-0000-0000-0000-000000000000")
    print(bucket)

# readBucketTag()

def createBucketTags():
    bucket = storage.BucketTags.create("00000000-0000-0000-0000-000000000000",
        [
            {"Key": "Name", "Value": "testbucket"},
        ]
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
        Versioning=True
    )
    print(bucket)

# updateBucket()

def readBucketMetadata():
    bucket = storage.Bucket.retrieve_metadata("00000000-0000-0000-0000-000000000000")
    print(bucket)

# readBucketMetadata()

def readAllObjects():
    objects = storage.Bucket.list_objects("00000000-0000-0000-0000-000000000000")
    print(objects)

# readAllObjects()

def readAllBuckets():
    buckets = storage.Bucket.list_buckets()
    print(buckets)

# readAllBuckets()

def createBucket():
    bucket = storage.Bucket.create(
        PoolGUID="00000000-0000-0000-0000-000000000000",
        Name="testbucket",
        RegionString="us-west-1",
        Versioning=True
    )
    print(bucket)

# createBucket()

def existsBucket():
    bucket = storage.Bucket.exists("00000000-0000-0000-0000-000000000000")
    print(bucket)

# existsStoragePool()

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
      Provider="Disk",
      WriteMode="GUID",
      UseSsl=False,
      DiskDirectory="./disk/",
      Compress="None",
      EnableReadCaching=False,
    )
    print(storagePool)  

# createStoragePool()