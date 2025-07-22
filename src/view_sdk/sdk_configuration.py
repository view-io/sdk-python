# sdk_configuration.py
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional

from .base import BaseClient


class Service(Enum):
    """Available services in the system."""

    DEFAULT = "default"
    STORAGE = "storage"
    CRAWLER = "crawler"
    LEXI = "lexi"
    EMBEDDINGS = "embeddings"
    VECTOR = "vector"
    PROCESSOR = "processor"
    ASSISTANT = "assistant"
    SEMANTIC_CELLS = "semantic_cells"
    CONTROL_PLANE = "control_plane"
    ORCHESTRATOR = "orchestrator"
    CONFIG = "config"
    GRAPH_DATABASE = "graph_database"
    DIRECTOR = "director"


@dataclass
class ServicePorts:
    """Default ports for each service."""

    DEFAULT: int = 8000
    STORAGE: int = 8001
    CRAWLER: int = 8101
    LEXI: int = 8201
    EMBEDDINGS: int = 8301
    VECTOR: int = 8000
    PROCESSOR: int = 8501
    ASSISTANT: int = 8331
    SEMANTIC_CELLS: int = 8341
    CONTROL_PLANE: int = 8401
    ORCHESTRATOR: int = 8501
    CONFIG: int = 8601
    GRAPH_DATABASE: int = 8701
    DIRECTOR: int = 8501


class SdkConfiguration:
    _instance = None

    def __init__(self):
        self.access_key: Optional[str] = None
        self.tenant_guid: Optional[str] = None
        self.verbose: bool = False
        self.base_url: Optional[str] = None
        self.control_plane_url: Optional[str] = None
        self.secure: bool = False
        self.service_ports: Dict[Service, int] = {
            service: getattr(ServicePorts, service.name) for service in Service
        }
        self._clients: Dict[Service, BaseClient] = {}

    @classmethod
    def get_instance(cls) -> "SdkConfiguration":
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def configure(
        self,
        access_key: str,
        base_url: str,
        *,
        control_plane_url: Optional[str] = None,
        secure: bool = False,
        service_ports: Optional[Dict[Service, int]] = None,
        tenant_guid: Optional[str] = None,
        verbose: bool = False,
    ) -> None:
        """
        Configure the SDK with access credentials and service settings.

        Args:
            access_key: API access key for authentication
            base_url: Base domain for services (e.g., 'localhost' or 'view.io')
            control_plane_url: Optional separate domain for Control Plane service
            secure: Use HTTPS instead of HTTP
            service_ports: Optional dictionary to override default ports
            tenant_guid: Optional tenant GUID for multi-tenant environments
            verbose: Enable verbose logging

        Example:
            >>> # Local development setup
            >>> configure(
            ...     access_key="your_key",
            ...     base_url="localhost",
            ...     control_plane_url="control.view.io",
            ...     service_ports={Service.STORAGE: 9001, Service.VECTOR: 9311},
            ... )
        """
        self.access_key = access_key
        self.base_url = base_url
        self.control_plane_url = control_plane_url
        self.secure = secure
        self.tenant_guid = tenant_guid
        self.verbose = verbose

        # Update service ports if custom ones provided
        if service_ports:
            self.service_ports.update(service_ports)

    def get_service_url(self, service: Service) -> str:
        """
        Build the complete URL for a service.

        Args:
            service: Service to get URL for

        Returns:
            Complete service URL with protocol, domain, and port
        """
        protocol = "https://" if self.secure else "http://"

        # Special handling for Control Plane service
        if service == Service.CONTROL_PLANE and self.control_plane_url:
            domain = self.control_plane_url
        else:
            domain = self.base_url

        port = self.service_ports[service]
        return f"{protocol}{domain}:{port}"

    def get_client(self, service: Service) -> BaseClient:
        """
        Get or create a client for the specified service.

        Args:
            service: Service enum value

        Returns:
            BaseClient: Client instance for the specified service

        Raises:
            ValueError: If SDK is not configured
        """
        if not self.access_key or not self.base_url:
            raise ValueError("SDK is not configured. Call 'configure' first.")

        if service not in self._clients:
            endpoint = self.get_service_url(service)
            self._clients[service] = BaseClient(
                base_url=endpoint,
                access_key=self.access_key,
                tenant_guid=self.tenant_guid,
                verbose=self.verbose,
            )

        return self._clients[service]

    def close_all(self) -> None:
        """Close all active client connections."""
        for client in self._clients.values():
            client.close()
        self._clients.clear()


class EmbeddingDefaults:
    OPENAI_DEFAULT_MODEL = "text-embedding-ada-002"
    VOYAGEAI_DEFAULT_MODEL = "voyage-large-2-instruct"
    OLLAMA_DEFAULT_MODEL = "llama3"
    LANGCHAIN_DEFAULT_MODEL = "all-MiniLM-L6-v2"

    @classmethod
    def set_openai_model(cls, model: str):
        cls.OPENAI_DEFAULT_MODEL = model

    @classmethod
    def set_voyageai_model(cls, model: str):
        cls.VOYAGEAI_DEFAULT_MODEL = model

    @classmethod
    def set_ollama_model(cls, model: str):
        cls.OLLAMA_DEFAULT_MODEL = model

    @classmethod
    def set_langchain_model(cls, model: str):
        cls.LANGCHAIN_DEFAULT_MODEL = model


# Global convenience functions
def configure(
    access_key: str,
    base_url: str,
    *,
    control_plane_url: Optional[str] = None,
    secure: bool = False,
    service_ports: Optional[Dict[Service, int]] = None,
    tenant_guid: Optional[str] = None,
    verbose: bool = False,
) -> None:
    """
    Configure the SDK with access credentials and service settings.

    Args:
        access_key: API access key for authentication.
        base_url: Base domain for services (e.g., 'localhost' or 'view.io').
        control_plane_url: Optional separate domain for Control Plane service.
        secure: Use HTTPS instead of HTTP.
        service_ports: Optional dictionary to override default ports.
        tenant_guid: Optional tenant GUID for multi-tenant environments.
        verbose: Enable verbose logging.

    Example:
        >>> # Local development setup
        >>> configure(
        ...     access_key="your_key",
        ...     base_url="localhost",
        ...     control_plane_url="control.view.io",
        ...     service_ports={Service.STORAGE: 9001, Service.VECTOR: 9311},
        ... )
    """
    SdkConfiguration.get_instance().configure(
        access_key=access_key,
        base_url=base_url,
        control_plane_url=control_plane_url,
        secure=secure,
        service_ports=service_ports,
        tenant_guid=tenant_guid,
        verbose=verbose,
    )


def get_client(service: Service) -> BaseClient:
    """
    Get a client for the specified service.

    Args:
        service: Service enum value to get the client for.

    Returns:
        BaseClient: Client instance for the specified service.

    Raises:
        ValueError: If SDK is not configured.
    """
    return SdkConfiguration.get_instance().get_client(service)


def close_all() -> None:
    """
    Close all active client connections.

    This method will close all the clients that have been created and clear the internal client cache.
    """
    SdkConfiguration.get_instance().close_all()
