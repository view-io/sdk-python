def _get_url_base(cls, *args, **kwargs) -> str:
    """
    Common URL construction logic for View SDK resources.

    Args:
        *args: Variable-length argument list. The first argument is the tenant GUID if `REQUIRES_TENANT` is True, followed by any additional path segments.
        **kwargs: Optional keyword arguments representing query parameters to include in the URL.

    Returns:
        str: The constructed URL without version prefix.
    """
    parts = []

    # Add tenant if required and present
    if cls.REQUIRES_TENANT and args and isinstance(args[0], str):
        parts.append(f"tenants/{args[0]}")
        args = args[1:]

    # Add any remaining path components
    parts.extend(str(arg) for arg in args)

    # Build query string from kwargs
    query_params = []
    for key, value in kwargs.items():
        if value is None:
            query_params.append(key)
        else:
            query_params.append(f"{key}={value}")

    url = "/".join(str(part) for part in parts if part)
    if query_params:
        url = f"{url}?{'&'.join(query_params)}"

    return url


def _get_url_v1(cls, *args, **kwargs) -> str:
    """
    Constructs a v1.0 URL for a resource in the View SDK.

    Args:
        *args: Variable-length argument list. The first argument is the tenant GUID if `REQUIRES_TENANT` is True, followed by any additional path segments.
        **kwargs: Optional keyword arguments representing query parameters to include in the URL.

    Returns:
        str: The constructed v1.0 URL for the resource.
    """
    return f"v1.0/{_get_url_base(cls, *args, **kwargs)}"


def _get_url_v2(cls, *args, **kwargs) -> str:
    """
    Constructs a v2.0 URL for a resource in the View SDK.

    Args:
        *args: Variable-length argument list. The first argument is the tenant GUID if `REQUIRES_TENANT` is True, followed by any additional path segments.
        **kwargs: Optional keyword arguments representing query parameters to include in the URL.

    Returns:
        str: The constructed v2.0 URL for the resource.
    """
    return f"v2.0/{_get_url_base(cls, *args, **kwargs)}"
