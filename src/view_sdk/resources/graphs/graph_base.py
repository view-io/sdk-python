from abc import ABC, abstractmethod
from typing import Any, ClassVar, Dict, List, Type


class GraphDriverBase(ABC):
    """Abstract base class for graph database drivers."""

    @abstractmethod
    def create(self, resource_type: str, model_class: Type, **params) -> Any:
        """Create a resource."""
        pass

    @abstractmethod
    def get(self, resource_type: str, model_class: Type, resource_guid: str) -> Any:
        """Get a resource."""
        pass

    @abstractmethod
    def delete(self, resource_type: str, resource_guid: str) -> None:
        """Delete a resource."""
        pass

    @abstractmethod
    def search(self, resource_type: str, model_class: Type, **search_params) -> Any:
        """Search for resources."""
        pass

    @abstractmethod
    def get_all(self, resource_type: str, model_class: Type) -> List[Any]:
        """Get all resources of a type."""
        pass

    @abstractmethod
    def exists(self, resource_type: str, resource_guid: str) -> bool:
        """Check if a resource exists."""
        pass

    @abstractmethod
    def exists_in_graph(
        self, resource_type: str, graph_guid: str, resource_guid: str
    ) -> bool:
        """Check if a resource exists in a specific graph."""
        pass

    @abstractmethod
    def create_multiple(
        self, resource_type: str, model_class: Type, items: List[Dict]
    ) -> List[Any]:
        """Create multiple resources at once."""
        pass

    @abstractmethod
    def update(
        self, resource_type: str, model_class: Type, resource_guid: str, data: Dict
    ) -> Any:
        """Update a resource."""
        pass

    @abstractmethod
    def export_gexf(self, graph_guid: str) -> str:
        """Export graph to GEXF format."""
        pass

    @abstractmethod
    def get_node_edges(
        self, graph_guid: str, node_guid: str, direction: str
    ) -> List[Any]:
        """Get edges connected to a node."""
        pass

    @abstractmethod
    def get_edges_between(
        self, graph_guid: str, from_node: str, to_node: str
    ) -> List[Any]:
        """Get edges between nodes."""
        pass


class GraphResourceBase(ABC):
    """Abstract base class for graph resources."""

    RESOURCE_NAME: ClassVar[str] = ""
    MODEL: ClassVar[Type] = None
    DRIVER: ClassVar[Type[GraphDriverBase]] = None

    def __init__(self):
        if not self.DRIVER:
            raise ValueError("DRIVER must be set in the implementing class")
        if not self.RESOURCE_NAME:
            raise ValueError("RESOURCE_NAME must be set in the implementing class")
        if not self.MODEL:
            raise ValueError("MODEL must be set in the implementing class")
        self._driver = self.DRIVER()

    @classmethod
    def create(cls, **params):
        """Create a resource."""
        instance = cls()
        return instance._driver.create(cls.RESOURCE_NAME, cls.MODEL, **params)

    @classmethod
    def retrieve(cls, resource_guid: str):
        """Retrieve a resource."""
        instance = cls()
        return instance._driver.get(cls.RESOURCE_NAME, cls.MODEL, resource_guid)

    @classmethod
    def delete(cls, resource_guid: str):
        """Delete a resource."""
        instance = cls()
        return instance._driver.delete(cls.RESOURCE_NAME, resource_guid)

    @classmethod
    def search(cls, **search_params):
        """Search for resources."""
        instance = cls()
        return instance._driver.search(cls.RESOURCE_NAME, cls.MODEL, **search_params)

    @classmethod
    def exists(cls, resource_guid: str) -> bool:
        """Check if a resource exists."""
        instance = cls()
        return instance._driver.exists(cls.RESOURCE_NAME, resource_guid)
