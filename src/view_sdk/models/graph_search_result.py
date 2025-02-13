from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from .graph import GraphModel
from .graph_edge import GraphEdgeModel
from .graph_node import GraphNodeModel


class GraphSearchResult(BaseModel):
    """Search result model for graph operations."""

    graphs: Optional[List[GraphModel]] = Field(
        default=None, alias="Graphs", description="List of graphs"
    )

    nodes: Optional[List[GraphNodeModel]] = Field(
        default=None, alias="Nodes", description="List of nodes"
    )

    edges: Optional[List[GraphEdgeModel]] = Field(
        default=None, alias="Edges", description="List of edges"
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
