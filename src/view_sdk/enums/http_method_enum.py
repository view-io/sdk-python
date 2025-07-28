from enum import Enum


class HttpMethodEnum(str, Enum):
    """HTTP method enum."""

    UNKNOWN = "UNKNOWN"
    GET = "GET"
    PUT = "PUT"
    POST = "POST"
    DELETE = "DELETE"
    PATCH = "PATCH"
