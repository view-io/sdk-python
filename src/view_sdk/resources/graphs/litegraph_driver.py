from typing import Any, Dict, List, Type

from litegraph_sdk import Edge as LiteEdge
from litegraph_sdk import Graph as LiteGraph
from litegraph_sdk import Node as LiteNode

from ...models.graph_edge import GraphEdgeModel
from .graph_base import GraphDriverBase


class LiteGraphDriver(GraphDriverBase):  # pragma: no cover
    """LiteGraph implementation of graph database driver."""

    def _convert_to_sdk_model(self, lite_model: Any, sdk_model_class: Type) -> Any:
        """Convert LiteGraph model to SDK model."""
        return (
            sdk_model_class.model_validate(lite_model.model_dump())
            if lite_model
            else None
        )

    def create(self, resource_type: str, model_class: Type, **params) -> Any:
        """Create a resource."""
        if resource_type == "graphs":
            lite_graph = LiteGraph.create(**params)
            return self._convert_to_sdk_model(lite_graph, model_class)
        elif resource_type == "nodes":
            lite_node = LiteNode.create(**params)
            return self._convert_to_sdk_model(lite_node, model_class)
        elif resource_type == "edges":
            lite_edge = LiteEdge.create(**params)
            return self._convert_to_sdk_model(lite_edge, model_class)

    def get(self, resource_type: str, model_class: Type, resource_guid: str) -> Any:
        """Generic get method."""
        if resource_type == "graphs":
            lite_graph = LiteGraph.retrieve(resource_guid)
            return self._convert_to_sdk_model(lite_graph, model_class)
        elif resource_type == "nodes":
            lite_node = LiteNode.retrieve(resource_guid)
            return self._convert_to_sdk_model(lite_node, model_class)
        elif resource_type == "edges":
            lite_edge = LiteEdge.retrieve(resource_guid)
            return self._convert_to_sdk_model(lite_edge, model_class)

    def delete(self, resource_type: str, resource_guid: str) -> None:
        """Generic delete method."""
        if resource_type == "graphs":
            LiteGraph.delete(resource_guid)
        elif resource_type == "nodes":
            LiteNode.delete(resource_guid)
        elif resource_type == "edges":
            LiteEdge.delete(resource_guid)

    def search(
        self, resource_type: str, model_class: Type, **search_params
    ) -> List[Any]:
        """Generic search method."""
        if resource_type == "graphs":
            lite_results = LiteGraph.search(**search_params)
            return [
                self._convert_to_sdk_model(item, model_class) for item in lite_results
            ]
        elif resource_type == "nodes":
            lite_results = LiteNode.search(**search_params)
            return [
                self._convert_to_sdk_model(item, model_class) for item in lite_results
            ]
        elif resource_type == "edges":
            lite_results = LiteEdge.search(**search_params)
            return [
                self._convert_to_sdk_model(item, model_class) for item in lite_results
            ]

    # Specialized methods
    def export_gexf(self, graph_guid: str) -> str:
        """Export graph to GEXF format."""
        return LiteGraph.export_gexf(graph_guid)

    def get_node_edges(
        self, graph_guid: str, node_guid: str, direction: str
    ) -> List[GraphEdgeModel]:
        """Get edges connected to a node."""
        lite_edges = LiteNode.get_edges(node_guid, direction=direction)
        return [self._convert_to_sdk_model(edge, GraphEdgeModel) for edge in lite_edges]

    def get_edges_between(
        self, graph_guid: str, from_node: str, to_node: str
    ) -> List[GraphEdgeModel]:
        """Get edges between nodes."""
        lite_edges = LiteEdge.between(from_node, to_node)
        return [self._convert_to_sdk_model(edge, GraphEdgeModel) for edge in lite_edges]

    def get_all(self, resource_type: str, model_class: Type) -> List[Any]:
        """Get all resources of a type."""
        if resource_type == "graphs":
            lite_graphs = LiteGraph.retrieve_all()
            return [
                self._convert_to_sdk_model(graph, model_class) for graph in lite_graphs
            ]
        # Add other resource types if needed

    def exists(self, resource_type: str, resource_guid: str) -> bool:
        """Check if a resource exists."""
        if resource_type == "graphs":
            return LiteGraph.exists(resource_guid)
        elif resource_type == "nodes":
            return LiteNode.exists(resource_guid)
        elif resource_type == "edges":
            return LiteEdge.exists(resource_guid)

    def exists_in_graph(
        self, resource_type: str, graph_guid: str, resource_guid: str
    ) -> bool:
        """Check if a resource exists in a specific graph."""
        if resource_type == "nodes":
            return LiteNode.exists_in_graph(graph_guid, resource_guid)
        elif resource_type == "edges":
            return LiteEdge.exists_in_graph(graph_guid, resource_guid)

    def create_multiple(
        self, resource_type: str, model_class: Type, items: List[Dict]
    ) -> List[Any]:
        """Create multiple resources at once."""
        if resource_type == "nodes":
            return LiteNode.create_multiple(items)

    def update(
        self, resource_type: str, model_class: Type, resource_guid: str, data: Dict
    ) -> Any:
        """Update a resource."""
        if resource_type == "graphs":
            return LiteGraph.update(resource_guid, **data)
