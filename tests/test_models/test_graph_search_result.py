import pytest
from view_sdk.models.graph_search_result import GraphSearchResult
from view_sdk.models.graph import GraphModel
from view_sdk.models.graph_node import GraphNodeModel
from view_sdk.models.graph_edge import GraphEdgeModel

def test_graph_search_result_defaults():
    result = GraphSearchResult()
    assert result.graphs is None
    assert result.nodes is None
    assert result.edges is None

def test_graph_search_result_with_values():
    graph = GraphModel(guid="g1")
    node = GraphNodeModel(guid="n1", tenant_guid="t1", graph_guid="g1")
    edge = GraphEdgeModel(guid="e1", tenant_guid="t1", graph_guid="g1", from_node_guid="n1", to_node_guid="n2")
    result = GraphSearchResult(graphs=[graph], nodes=[node], edges=[edge])
    assert result.graphs == [graph]
    assert result.nodes == [node]
    assert result.edges == [edge]

def test_graph_search_result_aliases():
    data = {
        "Graphs": [{"GUID": "g1"}],
        "Nodes": [{"GUID": "n1", "TenantGUID": "t1", "GraphGUID": "g1"}],
        "Edges": [{"GUID": "e1", "TenantGUID": "t1", "GraphGUID": "g1", "From": "n1", "To": "n2"}],
    }
    result = GraphSearchResult.model_validate(data)
    assert result.graphs[0].guid == "g1"
    assert result.nodes[0].guid == "n1"
    assert result.edges[0].guid == "e1"

def test_graph_search_result_serialization():
    graph = GraphModel(guid="g1")
    node = GraphNodeModel(guid="n1", tenant_guid="t1", graph_guid="g1")
    edge = GraphEdgeModel(guid="e1", tenant_guid="t1", graph_guid="g1", from_node_guid="n1", to_node_guid="n2")
    result = GraphSearchResult(graphs=[graph], nodes=[node], edges=[edge])
    model_dict = result.model_dump(by_alias=True)
    assert model_dict["Graphs"][0]["GUID"] == "g1"
    assert model_dict["Nodes"][0]["GUID"] == "n1"
    assert model_dict["Edges"][0]["GUID"] == "e1" 