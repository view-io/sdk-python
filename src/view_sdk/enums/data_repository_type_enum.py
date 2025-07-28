from enum import Enum

class DataRepositoryTypeEnum(str, Enum):
    Other = "Other"
    File = "File"
    CIFS = "CIFS"
    NFS = "NFS"
    AmazonS3 = "AmazonS3"
    AzureBlob = "AzureBlob"
    Web = "Web"
    Printer = "Printer" 