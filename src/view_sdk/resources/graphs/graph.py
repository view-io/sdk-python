import uuid
from typing import Dict, List

from ...enums.graph_node_type_enum import GraphNodeTypeEnum
from ...models.graph import GraphModel
from ...models.graph_data import GraphDataModel
from ...models.graph_edge import GraphEdgeModel
from ...models.graph_node import GraphNodeModel
from .graph_base import GraphResourceBase
from .litegraph_driver import LiteGraphDriver


class Graph(GraphResourceBase):
    """Graph resource for managing graphs."""

    RESOURCE_NAME = "graphs"
    MODEL = GraphModel
    DRIVER = LiteGraphDriver

    @classmethod
    def create(
        cls, guid: str = None, name: str = None, data: Dict = None
    ) -> GraphModel:
        """Create a new graph."""
        if not guid:
            guid = str(uuid.uuid4())

        params = {"guid": guid, "name": name}
        if data:
            params["data"] = data

        return super().create(**params)

    @classmethod
    def export_gexf(cls, resource_guid: str) -> str:
        """Export graph to GEXF format."""
        instance = cls()
        return instance._driver.export_gexf(resource_guid)

    @classmethod
    def retrieve_all(cls) -> List[GraphModel]:
        """Retrieve all graphs."""
        instance = cls()
        return instance._driver.get_all(cls.RESOURCE_NAME, cls.MODEL)


class Node(GraphResourceBase):
    """Node resource for managing graph nodes."""

    RESOURCE_NAME = "nodes"
    MODEL = GraphNodeModel
    DRIVER = LiteGraphDriver

    @classmethod
    def create(
        cls,
        graph_guid: str,
        name: str = None,
        node_type: GraphNodeTypeEnum = GraphNodeTypeEnum.Unknown,
        data: Dict = None,
    ) -> GraphNodeModel:
        """Create a node in a graph."""
        params = {
            "graph_guid": graph_guid,
            "name": name,
            "data": GraphDataModel(type_=node_type, **data) if data else None,
        }
        return super().create(**params)

    @classmethod
    def get_edges(
        cls, graph_guid: str, node_guid: str, direction: str = "both"
    ) -> List["Edge"]:
        """Get edges connected to this node."""
        instance = cls()
        return instance._driver.get_node_edges(graph_guid, node_guid, direction)

    # Specialized node creation methods
    @classmethod
    def create_tenant(cls, graph_guid: str, tenant_data: Dict) -> GraphNodeModel:
        """Create a tenant node."""
        return cls.create(
            graph_guid=graph_guid,
            node_type=GraphNodeTypeEnum.Tenant,
            data={"tenant": tenant_data},
        )

    @classmethod
    def create_storage_pool(cls, graph_guid: str, pool_data: Dict) -> GraphNodeModel:
        """Create a storage pool node."""
        return cls.create(
            graph_guid=graph_guid,
            node_type=GraphNodeTypeEnum.StoragePool,
            data={"storage_pool": pool_data},
        )

    @classmethod
    def create_multiple(cls, nodes: List[Dict]) -> List[GraphNodeModel]:
        """Create multiple nodes at once."""
        instance = cls()
        return instance._driver.create_multiple(cls.RESOURCE_NAME, cls.MODEL, nodes)

    @classmethod
    def exists(cls, graph_guid: str, node_guid: str) -> bool:
        """Check if a node exists in the graph."""
        instance = cls()
        return instance._driver.exists_in_graph(
            cls.RESOURCE_NAME, graph_guid, node_guid
        )


class Edge(GraphResourceBase):
    """Edge resource for managing graph edges."""

    RESOURCE_NAME = "edges"
    MODEL = GraphEdgeModel
    DRIVER = LiteGraphDriver

    @classmethod
    def create(
        cls,
        graph_guid: str,
        from_node: str,
        to_node: str,
        name: str = None,
        cost: int = 0,
    ) -> GraphEdgeModel:
        """Create an edge between nodes."""
        params = {
            "graph_guid": graph_guid,
            "from_node_guid": from_node,
            "to_node_guid": to_node,
            "name": name,
            "cost": cost,
        }
        return super().create(**params)

    @classmethod
    def between(
        cls, graph_guid: str, from_node: str, to_node: str
    ) -> List[GraphEdgeModel]:
        """Get edges between two nodes."""
        instance = cls()
        return instance._driver.get_edges_between(graph_guid, from_node, to_node)
