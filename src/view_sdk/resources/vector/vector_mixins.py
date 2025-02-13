from typing import List

from ...mixins import CreateableAPIResource, DeletableAPIResource
from ...sdk_configuration import get_client
from ...sdk_logging import log_debug, log_warning
from ...utils.url_helper import _get_url_base, _get_url_v1


class EmbeddingsGeneratorMixin(CreateableAPIResource):
    """
    Mixin class for generating embeddings from input data.

    This mixin provides functionality to generate embeddings using various models.
    It supports customizable timeouts and handles model defaults.

    Attributes:
        SERVICE: The service to use for embeddings generation.
        REQUIRES_TENANT (bool): Whether tenant GUID is required (False).
        CREATE_METHOD (str): The HTTP method for create operations (POST).
        DEFAULT_MODEL: The default model to use for embeddings generation.
        REQUEST_MODEL: The request model for embeddings generation.
        MODEL: The response model for embeddings generation.
    """

    SERVICE = None
    REQUIRES_TENANT = False
    CREATE_METHOD = "POST"
    DEFAULT_MODEL = None
    REQUEST_MODEL = None
    MODEL = None

    @classmethod
    def generate_embeddings(cls, embed_request, timeout: int = 30):
        """
        Generate embeddings for the given request.

        Args:
            embed_request: The embeddings request containing input data and model preferences.
            timeout (int, optional): Request timeout in seconds. Defaults to 30.

        Returns:
            MODEL: The embeddings generation response, containing the generated
                embeddings or error information.

        Raises:
            ValueError: If timeout is less than 1.
            Exception: If embeddings generation fails.

        Note:
            If no model is specified in the request, the DEFAULT_MODEL will be used.
        """
        client = get_client(cls.SERVICE)

        if timeout < 1:
            raise ValueError("Timeout must be greater than 0")

        if not embed_request.model:
            embed_request.model = cls.DEFAULT_MODEL

        try:
            log_debug(f"Making embeddings request with model: {embed_request.model}")
            url = _get_url_v1(cls, "embeddings")
            result = client.request(
                "POST",
                url,
                json=embed_request.model_dump(mode="json", by_alias=True),
                timeout=timeout,
            )
            return cls.MODEL.model_validate(result)
        except Exception as e:
            log_warning(f"Error generating embeddings: {str(e)}")
            return cls.MODEL(success=False, status_code=500, model=embed_request.model)


class ModelLoaderMixin(CreateableAPIResource):
    """
    Mixin class for loading machine learning models.

    This mixin provides functionality to load models into memory for faster
    inference. It handles model loading requests and error reporting.
    """

    @classmethod
    def load_model(cls, model: str) -> bool:
        """
        Load a single model into memory.

        Args:
            model (str): The name or identifier of the model to load.

        Returns:
            bool: True if the model was loaded successfully, False otherwise.

        Raises:
            ValueError: If model name is empty.
        """
        if not model:
            raise ValueError("Model name cannot be empty")

        try:
            log_debug(f"Loading model: {model}")
            url = _get_url_v1(cls, "preload")
            client = get_client(cls.SERVICE)
            client.request("POST", url, json={"model": model})
            return True
        except Exception as e:
            log_warning(f"Error loading model: {str(e)}")
            return False


class MultiModelLoaderMixin(ModelLoaderMixin):
    """
    Mixin class for loading multiple machine learning models.

    This mixin extends ModelLoaderMixin to provide batch loading capabilities
    for multiple models simultaneously.
    """

    @classmethod
    def load_models(cls, models: List[str]) -> bool:
        """
        Load multiple models into memory.

        This method attempts to load all specified models and returns success
        only if all models are loaded successfully.

        Args:
            models (List[str]): List of model names or identifiers to load.

        Returns:
            bool: True if all models were loaded successfully, False if any failed.

        Raises:
            ValueError: If the models list is empty.
        """
        if not models:
            raise ValueError("No models specified for loading")

        try:
            return all(cls.load_model(model) for model in models)
        except Exception as e:
            log_warning(f"Error loading models: {str(e)}")
            return False


class ModelDeletionMixin(DeletableAPIResource):
    """
    Mixin class for deleting machine learning models.

    This mixin provides functionality to remove models from memory and clean up
    associated resources.
    """

    @classmethod
    def delete_model(cls, name: str) -> bool:
        """
        Delete a model and free its resources.

        Args:
            name (str): The name or identifier of the model to delete.

        Returns:
            bool: True if the model was deleted successfully, False otherwise.

        Raises:
            ValueError: If model name is empty.
        """
        if not name:
            raise ValueError("Model name cannot be empty")

        try:
            log_debug(f"Deleting model: {name}")
            url = _get_url_v1(cls, "delete")
            client = get_client(cls.SERVICE)
            client.request("DELETE", url, json={"name": name})
            return True
        except Exception as e:
            log_warning(f"Error deleting model: {str(e)}")
            return False


class ConnectivityMixin:
    """
    Mixin class for validating service connectivity.

    This mixin provides methods to check if a service is accessible and responding
    to requests. It's useful for health checks and service validation.
    """

    @classmethod
    def validate_connectivity(cls) -> bool:
        """
        Check if the service is accessible and responding.

        This method attempts to make a lightweight HEAD request to the service
        to verify its availability.

        Returns:
            bool: True if the service is accessible and responding, False otherwise.

        Note:
            This method uses a HEAD request to minimize network overhead during
            connectivity checks.
        """
        client = get_client(cls.SERVICE)
        try:
            url = _get_url_base(cls)
            client.request("HEAD", url)
            return True
        except Exception:
            return False
