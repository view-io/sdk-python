from unittest.mock import Mock, patch
import pytest

from view_sdk.resources.graphs.graph import Graph, Node, Edge
from view_sdk.models.graph import GraphModel
from view_sdk.models.graph_node import GraphNodeModel
from view_sdk.models.graph_edge import GraphEdgeModel
from view_sdk.models.graph_data import GraphDataModel
from view_sdk.enums.graph_node_type_enum import GraphNodeTypeEnum

# Patch the SDK configuration to bypass the initial configuration check
@pytest.fixture(autouse=True)
def mock_litegraph_sdk():
    """
    Mock the litegraph_sdk package to prevent 'SDK is not configured' errors.
    This ensures tests can run without explicitly calling configure.
    """
    mock_graph = Mock()
    mock_node = Mock()
    mock_edge = Mock()

    # Mock Graph methods
    mock_graph.create.return_value = GraphModel(
        guid="test-graph-guid",
        name="test-graph",
        created_utc="2024-01-01T00:00:00Z"
    )
    mock_graph.retrieve.return_value = GraphModel(
        guid="test-graph-guid",
        name="test-graph",
        created_utc="2024-01-01T00:00:00Z"
    )
    mock_graph.retrieve_all.return_value = [
        GraphModel(
            guid="1",
            name="Graph 1",
            created_utc="2024-01-01T00:00:00Z"
        ),
        GraphModel(
            guid="2",
            name="Graph 2",
            created_utc="2024-01-01T00:00:00Z"
        )
    ]

    # Mock Node methods
    def create_node(**kwargs):
        if kwargs.get("data") and isinstance(kwargs["data"], GraphDataModel):
            node_data = {
                "Type": kwargs["data"].type_,
            }
            if kwargs["data"].tenant:
                node_data["Tenant"] = kwargs["data"].tenant.model_dump()
        else:
            node_data = {
                "Type": GraphNodeTypeEnum.Unknown
            }

        return GraphNodeModel(
            guid="node-guid",
            graph_guid=kwargs.get("graph_guid", "test-graph-guid"),
            name=kwargs.get("name", "test-node"),
            data=node_data
        )
    mock_node.create.side_effect = create_node

    # Mock Edge methods
    mock_edge.create.return_value = GraphEdgeModel(
        guid="edge-guid",
        graph_guid="test-graph-guid",
        from_node_guid="node1",
        to_node_guid="node2",
        name="test-edge",
        cost=1
    )

    with patch('view_sdk.resources.graphs.litegraph_driver.LiteGraph', mock_graph), \
         patch('view_sdk.resources.graphs.litegraph_driver.LiteNode', mock_node), \
         patch('view_sdk.resources.graphs.litegraph_driver.LiteEdge', mock_edge):
        yield

def test_graph_create():
    """Test graph creation."""
    graph = Graph.create(name="Test Graph")
    assert isinstance(graph, GraphModel)
    assert graph.name == "test-graph"
    assert graph.guid == "test-graph-guid"

def test_graph_retrieve_all():
    """Test retrieving all graphs."""
    graphs = Graph.retrieve_all()
    assert len(graphs) == 2
    assert all(isinstance(g, GraphModel) for g in graphs)

def test_node_create():
    """Test node creation."""
    node = Node.create(
        graph_guid="test-graph-guid",
        name="Test Node"
    )
    assert isinstance(node, GraphNodeModel)
    assert node.guid == "node-guid"
    assert node.name == "Test Node"
    assert node.data == GraphDataModel(type_=GraphNodeTypeEnum.Unknown)



def test_edge_create():
    """Test edge creation."""
    edge = Edge.create(
        graph_guid="test-graph-guid",
        from_node="node1",
        to_node="node2",
        name="Test Edge"
    )
    assert isinstance(edge, GraphEdgeModel)
    assert edge.guid == "edge-guid"
    assert edge.from_node_guid == "node1"
    assert edge.to_node_guid == "node2"
