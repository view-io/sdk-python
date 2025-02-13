from typing import Type

from pydantic import BaseModel

from .models.enumeration_query import EnumerationQueryModel
from .models.enumeration_result import EnumerationResultModel
from .sdk_configuration import Service, get_client
from .utils.url_helper import _get_url_base, _get_url_v1, _get_url_v2


class BaseAPIResource:
    """
    Base mixin class for all API resources.

    Attributes:
        RESOURCE_NAME (str): The name of the resource.
        MODEL (Type[BaseModel]): The Pydantic model representing the resource.
        REQUIRES_TENANT (bool): Indicates if a tenant GUID is required.
        SERVICE (Type[Service]): The service associated with the resource.
        PARENT_RESOURCE (str): The name of the parent resource, if applicable.
        PARENT_ID_PARAM (str): The parameter name for the parent resource GUID.
        QUERY_PARAMS (dict[str, str | None]): Predefined query parameters for the resource.
    """

    RESOURCE_NAME: str = ""
    MODEL: Type[BaseModel] = None
    REQUIRES_TENANT: bool = True
    SERVICE: Type[Service] = Service.DEFAULT

    # Nested resource configuration
    PARENT_RESOURCE: str = ""
    PARENT_ID_PARAM: str = "parent_guid"
    QUERY_PARAMS: dict[str, str | None] = {}

    @classmethod
    def _validate_parent_guid(cls, parent_guid: str) -> None:
        """
        Validates the parent GUID if provided.

        Args:
            parent_guid (str): The GUID of the parent resource.

        Raises:
            ValueError: If the parent_guid is empty or None.
        """
        if parent_guid is not None and not parent_guid:
            raise ValueError(f"{cls.PARENT_ID_PARAM} cannot be empty if provided")

    @classmethod
    def _get_resource_path(cls, *resource_guids: str, **kwargs) -> tuple:
        """
        Builds the resource path components.

        Args:
            *resource_guids (str): Variable length resource GUIDs.
            **kwargs: Additional keyword arguments, including the parent GUID.

        Returns:
            tuple: A tuple containing path components and remaining keyword arguments.
        """
        path_components = []

        # Add parent resource components if defined and parent_guid is provided
        if cls.PARENT_RESOURCE and cls.PARENT_ID_PARAM in kwargs:
            parent_guid = kwargs.pop(cls.PARENT_ID_PARAM)
            cls._validate_parent_guid(parent_guid)
            if parent_guid is not None:
                path_components.extend([cls.PARENT_RESOURCE, parent_guid])

        elif cls.PARENT_RESOURCE and not cls.PARENT_ID_PARAM:
            path_components.append(cls.PARENT_RESOURCE)

        # Add current resource components
        path_components.append(cls.RESOURCE_NAME)
        path_components.extend(resource_guids)

        # Update kwargs with any predefined query parameters
        kwargs.update(cls.QUERY_PARAMS)

        return tuple(path_components), kwargs

    @classmethod
    def _dump_model_data(
        cls, data: dict | list[dict], model: Type[BaseModel] = None
    ) -> dict | list[dict]:
        """
        Dumps model data according to the specified model.

        Args:
            data (dict | list[dict]): The data to dump, can be a single dict or list of dicts
            model (Type[BaseModel], optional): The model to use for validation.
                Defaults to None.

        Returns:
            dict | list[dict]: The dumped data
        """
        if isinstance(data, list):
            model_to_use = model or cls.MODEL
            if model_to_use is not None:
                return [
                    model_to_use(**item).model_dump(
                        mode="json", by_alias=True, exclude_unset=True
                    )
                    for item in data
                ]
            return data

        model_to_use = model or cls.MODEL
        if model_to_use is not None:
            return model_to_use(**data).model_dump(
                mode="json", by_alias=True, exclude_unset=True
            )
        return data


class ExistsAPIResource(BaseAPIResource):
    """Mixin class for checking if a resource exists."""

    @classmethod
    def exists(cls, resource_guid: str, **kwargs) -> bool:
        """
        Checks if a resource exists.

        Args:
            resource_guid (str): The unique identifier of the resource.
            **kwargs: Additional keyword arguments for the request.

        Returns:
            bool: True if the resource exists, False otherwise.

        Raises:
            ValueError: If tenant GUID is required but not provided.
        """
        client = get_client(cls.SERVICE)

        if cls.REQUIRES_TENANT and client.tenant_guid is None:
            raise ValueError("Tenant GUID is required for this resource.")

        path_components, url_params = cls._get_resource_path(resource_guid, **kwargs)
        if cls.REQUIRES_TENANT:
            url = _get_url_v1(cls, client.tenant_guid, *path_components, **url_params)
        else:
            url = _get_url_v1(cls, *path_components, **url_params)

        try:
            client.request("HEAD", url)
            return True
        except Exception:
            return False


class CreateableAPIResource(BaseAPIResource):
    """Mixin class for creating API resources."""

    CREATE_METHOD: str = "PUT"
    REQUEST_MODEL: Type[BaseModel] = None

    @classmethod
    def create(cls, **kwargs) -> "BaseModel":
        """
        Creates a new resource.

        Args:
            **kwargs: Keyword arguments for the request, including the resource data.
                - headers (dict, optional): Additional headers for the request.
                - _data (dict, optional): The data to be sent in the request body.

        Returns:
            BaseModel: The created resource, validated against the REQUEST_MODEL if defined.

        Raises:
            ValueError: If tenant GUID is required but not provided.
        """
        client = get_client(cls.SERVICE)
        headers = kwargs.pop("headers", {})
        if cls.REQUIRES_TENANT and client.tenant_guid is None:
            raise ValueError("Tenant GUID is required for this resource.")

        # Extract data and path parameters separately
        data = kwargs.pop(
            "_data", kwargs.copy()
        )  # Get 'data' if provided, else use kwargs

        if cls.PARENT_ID_PARAM in kwargs:
            # Extract parent_guid and prepare path kwargs
            parent_guid = kwargs.pop(cls.PARENT_ID_PARAM)
            path_kwargs = {cls.PARENT_ID_PARAM: parent_guid}
            path_components, url_params = cls._get_resource_path(**path_kwargs)
        else:
            path_components, url_params = cls._get_resource_path(**{})

        # Validate and dump the data
        data = cls._dump_model_data(data, cls.REQUEST_MODEL)

        if cls.REQUIRES_TENANT:
            url = _get_url_v1(cls, client.tenant_guid, *path_components, **url_params)
        else:
            url = _get_url_v1(cls, *path_components, **url_params)

        instance = client.request(cls.CREATE_METHOD, url, json=data, headers=headers)
        return cls.MODEL.model_validate(instance) if cls.MODEL else instance


class RetrievableAPIResource(BaseAPIResource):
    """Mixin class for retrieving API resources."""

    @classmethod
    def retrieve(cls, resource_guid: str, **kwargs) -> "BaseModel":
        """
        Retrieves a resource.

        Args:
            resource_guid (str): The unique identifier of the resource.
            **kwargs: Additional keyword arguments for the request.
                - headers (dict, optional): Additional headers for the request.

        Returns:
            BaseModel: The retrieved resource, validated against the MODEL if defined.

        Raises:
            ValueError: If tenant GUID is required but not provided.
        """
        client = get_client(cls.SERVICE)
        headers = kwargs.pop("headers", {})

        if cls.REQUIRES_TENANT and client.tenant_guid is None:
            raise ValueError("Tenant GUID is required for this resource.")

        path_components, url_params = cls._get_resource_path(resource_guid, **kwargs)
        if cls.REQUIRES_TENANT:
            url = _get_url_v1(cls, client.tenant_guid, *path_components, **url_params)
        else:
            url = _get_url_v1(cls, *path_components, **url_params)

        instance = client.request("GET", url, headers=headers)
        return cls.MODEL.model_validate(instance) if cls.MODEL else instance


class AllRetrievableAPIResource(BaseAPIResource):
    """Mixin class for retrieving all API resources of a given type."""

    @classmethod
    def retrieve_all(cls, **kwargs) -> list["BaseModel"]:
        """
        Retrieves all resources of a given type.

        Args:
            **kwargs: Additional keyword arguments for filtering and pagination.
                - parent_guid (str, optional): The GUID of the parent resource.

        Returns:
            list[BaseModel]: A list of retrieved resources, validated against the MODEL if defined.

        Raises:
            ValueError: If tenant GUID is required but not provided.
        """
        client = get_client(cls.SERVICE)

        if cls.REQUIRES_TENANT and client.tenant_guid is None:
            raise ValueError("Tenant GUID is required for this resource.")

        # Validate parent_guid if provided
        if parent_guid := kwargs.get(cls.PARENT_ID_PARAM):
            cls._validate_parent_guid(parent_guid)

        path_components, url_params = cls._get_resource_path(**kwargs)
        if cls.REQUIRES_TENANT:
            url = _get_url_v1(cls, client.tenant_guid, *path_components, **url_params)
        else:
            url = _get_url_v1(cls, *path_components, **url_params)

        instances = client.request("GET", url)
        if not isinstance(instances, list):
            instances = []
        return (
            [cls.MODEL.model_validate(instance) for instance in instances]
            if cls.MODEL
            else instances
        )


class RetrievableStatisticsMixin(BaseAPIResource):
    """Mixin class for retrieving statistics for a given resource."""

    STATS_MODEL: Type[BaseModel] = None

    @classmethod
    def retrieve_statistics(cls, resource_guid: str, **kwargs):
        """
        Retrieves statistics for a given resource.

        Args:
            resource_guid (str): The unique identifier of the resource.
            **kwargs: Additional keyword arguments for the request.

        Returns:
            STATS_MODEL: The statistics data for the resource, validated against STATS_MODEL if defined.

        Raises:
            ValueError: If tenant GUID is required but not provided.
        """
        client = get_client(cls.SERVICE)

        if cls.REQUIRES_TENANT and client.tenant_guid is None:
            raise ValueError("Tenant GUID is required for this resource.")

        path_components, url_params = cls._get_resource_path(resource_guid, **kwargs)
        if cls.REQUIRES_TENANT:
            url = _get_url_v1(
                cls, client.tenant_guid, *path_components, stats=None, **url_params
            )
        else:
            url = _get_url_v1(cls, *path_components, stats=None, **url_params)

        response = client.request("GET", url)
        return cls.STATS_MODEL.model_validate(response) if cls.STATS_MODEL else response


class UpdatableAPIResource(BaseAPIResource):
    """Mixin class for updating API resources."""

    REQUEST_MODEL: Type[BaseModel] = None

    @classmethod
    def update(cls, resource_guid: str, **kwargs) -> "BaseModel":
        """
        Updates a resource.

        Args:
            resource_guid (str): The unique identifier of the resource.
            **kwargs: Keyword arguments for the request, including the updated resource data.
                - headers (dict, optional): Additional headers for the request.
                - data (dict, optional): The data to be sent in the request body.

        Returns:
            BaseModel: The updated resource, validated against the MODEL if defined.

        Raises:
            ValueError: If tenant GUID is required but not provided.
        """
        client = get_client(cls.SERVICE)
        headers = kwargs.pop("headers", {})
        if cls.REQUIRES_TENANT and client.tenant_guid is None:
            raise ValueError("Tenant GUID is required for this resource.")

        # Extract data and path parameters separately
        data = kwargs.pop(
            "data", kwargs.copy()
        )  # Get 'data' if provided, else use kwargs

        if cls.PARENT_ID_PARAM in kwargs:
            # Extract parent_guid and prepare path kwargs
            parent_guid = kwargs.pop(cls.PARENT_ID_PARAM)
            path_kwargs = {cls.PARENT_ID_PARAM: parent_guid}
            path_components, url_params = cls._get_resource_path(
                resource_guid, **path_kwargs
            )
        else:
            path_components, url_params = cls._get_resource_path(resource_guid, **{})

        # Validate and dump the data
        data = cls._dump_model_data(data, cls.REQUEST_MODEL)
        if cls.REQUIRES_TENANT:
            url = _get_url_v1(cls, client.tenant_guid, *path_components, **url_params)
        else:
            url = _get_url_v1(cls, *path_components, **url_params)

        instance = client.request("PUT", url, json=data, headers=headers)
        return cls.MODEL.model_validate(instance) if cls.MODEL else instance


class DeletableAPIResource(BaseAPIResource):
    """Mixin class for deleting API resources."""

    @classmethod
    def delete(cls, resource_guid: str, **kwargs) -> bool:
        """
        Deletes a resource.

        Args:
            resource_guid (str): The unique identifier of the resource.
            **kwargs: Additional keyword arguments for the request.
                - parent_guid (str, optional): The GUID of the parent resource.

        Returns:
            bool: True if the resource was deleted successfully, False otherwise.

        Raises:
            ValueError: If tenant GUID is required but not provided.
        """
        client = get_client(cls.SERVICE)

        if cls.REQUIRES_TENANT and client.tenant_guid is None:
            raise ValueError("Tenant GUID is required for this resource.")

        # Validate parent_guid if provided
        if parent_guid := kwargs.get(cls.PARENT_ID_PARAM):
            cls._validate_parent_guid(parent_guid)

        path_components, url_params = cls._get_resource_path(resource_guid, **kwargs)
        if cls.REQUIRES_TENANT:
            url = _get_url_v1(cls, client.tenant_guid, *path_components, **url_params)
        else:
            url = _get_url_v1(cls, *path_components, **url_params)

        try:
            client.request("DELETE", url)
            return True
        except Exception:
            return False


class EnumerableAPIResource(BaseAPIResource):
    """Mixin class for enumerating API resources."""

    @classmethod
    def enumerate(cls) -> "EnumerationResultModel":
        """
        Enumerates resources of a given type.

        Returns:
            EnumerationResultModel: The enumeration results containing the list of resources
                and any pagination metadata.

        Raises:
            ValueError: If tenant GUID is required but not provided.
        """
        client = get_client(cls.SERVICE)

        if cls.REQUIRES_TENANT and client.tenant_guid is None:
            raise ValueError("Tenant GUID is required for this resource.")

        path_components, url_params = cls._get_resource_path(**{})
        url_params["enumerate"] = None  # Add enumerate flag

        if cls.REQUIRES_TENANT:
            url = _get_url_v2(cls, client.tenant_guid, *path_components, **url_params)
        else:
            url = _get_url_v2(cls, *path_components, **url_params)

        response = client.request("GET", url)
        return (
            EnumerationResultModel[cls.MODEL].model_validate(response)
            if cls.MODEL
            else response
        )


class EnumerableAPIResourceWithData(BaseAPIResource):
    """Mixin class for enumerating API resources with data using V1 URL helper."""

    ENUMERABLE_REQUEST_MODEL: Type[BaseModel] = EnumerationQueryModel

    @classmethod
    def enumerate_with_query(cls, **kwargs) -> "EnumerationResultModel":
        """
        Enumerates resources of a given type with data using a query model.

        This method supports advanced querying capabilities through the ENUMERABLE_REQUEST_MODEL,
        which defaults to EnumerationQueryModel.

        Args:
            **kwargs: Query parameters that conform to the ENUMERABLE_REQUEST_MODEL schema.
                These parameters will be validated against the model before making the request.

        Returns:
            EnumerationResultModel: The enumeration results containing the list of resources
                and any pagination metadata.

        Raises:
            ValueError: If tenant GUID is required but not provided.
            ValidationError: If the provided query parameters don't match the ENUMERABLE_REQUEST_MODEL schema.
        """
        client = get_client(cls.SERVICE)

        if cls.REQUIRES_TENANT and client.tenant_guid is None:
            raise ValueError("Tenant GUID is required for this resource.")
        # Extract data from kwargs
        data_dict = kwargs.copy()

        parent_guid: str | None = None
        if cls.PARENT_ID_PARAM in data_dict:
            parent_guid = data_dict.pop(cls.PARENT_ID_PARAM)
        elif parent_guid is None:
            raise ValueError(f"{cls.PARENT_ID_PARAM} is required for this resource.")

        path_components, url_params = cls._get_resource_path(
            **{cls.PARENT_ID_PARAM: parent_guid}
        )

        url_params["enumerate"] = None

        if cls.REQUIRES_TENANT:
            url = _get_url_v1(cls, client.tenant_guid, *path_components, **url_params)
        else:
            url = _get_url_v1(cls, *path_components, **url_params)

        # Replace model dump code with new method
        data = cls._dump_model_data(data_dict, cls.ENUMERABLE_REQUEST_MODEL)

        response = client.request("POST", url, json=data)
        return (
            EnumerationResultModel[cls.MODEL].model_validate(response)
            if cls.MODEL
            else response
        )


class HealthCheckAPIResource(BaseAPIResource):
    """Mixin class for checking the health of a resource."""

    PARENT_ID_PARAM = None

    @classmethod
    def check(cls) -> bool:
        """
        Checks the health of a resource.

        Returns:
            bool: True if the health check is successful, False otherwise.

        Raises:
            ValueError: If tenant GUID is required but not provided.
        """
        client = get_client(cls.SERVICE)

        if cls.REQUIRES_TENANT and client.tenant_guid is None:
            raise ValueError("Tenant GUID is required for this resource.")

        path_components, url_params = cls._get_resource_path()
        if cls.REQUIRES_TENANT:
            url = _get_url_base(cls, client.tenant_guid, *path_components, **url_params)
        else:
            url = _get_url_base(cls, *path_components, **url_params)

        try:
            client.request("HEAD", url)
            return True
        except Exception:
            return False
