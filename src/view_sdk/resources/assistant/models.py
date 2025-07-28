from pydantic import BaseModel
from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
    UpdatableAPIResource,
)


class Models(
    CreateableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    UpdatableAPIResource,
    DeletableAPIResource,
):
    """
    Models resource for Assistant operations.
    """

    RESOURCE_NAME: str = "assistant/models"
    REQUIRES_TENANT = True
    CREATE_METHOD = "POST"

    @classmethod
    def retrieve_all(cls, **kwargs) -> list["BaseModel"]:
        """
        Retrieve all models.
        """
        cls.CREATE_METHOD = "POST"
        return super().create(**kwargs)

    @classmethod
    def retrieve(cls, **kwargs) -> "BaseModel":
        """
        Retrieve a model by ID.
        """
        cls.CREATE_METHOD = "POST"
        cls.RESOURCE_NAME = "assistant/models/pull"
        return super().create(**kwargs)

    @classmethod
    def delete(cls, **kwargs) -> "BaseModel":
        """
        Delete a model by ID.
        """
        cls.CREATE_METHOD = "POST"
        cls.RESOURCE_NAME = "assistant/models/delete"
        return super().create(**kwargs)

    @classmethod
    def load_unload(cls, **kwargs) -> "BaseModel":
        """
        Load an unloaded model.
        """
        cls.CREATE_METHOD = "POST"
        cls.RESOURCE_NAME = "assistant/models/load"
        return super().create(**kwargs)
