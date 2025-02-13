from enum import Enum


class EnumerationOrderEnum(str, Enum):
    """Enumeration order."""

    CreatedAscending = "CreatedAscending"
    CreatedDescending = "CreatedDescending"
    LastAccessAscending = "LastAccessAscending"
    LastAccessDescending = "LastAccessDescending"
    KeyAscending = "KeyAscending"
    KeyDescending = "KeyDescending"
