from enum import Enum


class StorageTypeEnum(str, Enum):
    """
    Storage type.
    """

    AWS_S3 = "AwsS3"
    """Amazon Simple Storage Service."""

    AZURE = "Azure"
    """Microsoft Azure BLOB Storage Service."""

    DISK = "Disk"
    """Local filesystem/disk storage."""

    CIFS = "SMB"
    """CIFS/SMB, e.g. Windows file share or SAMBA."""

    NFS = "NFS"
    """NFS, e.g. Linux export."""
