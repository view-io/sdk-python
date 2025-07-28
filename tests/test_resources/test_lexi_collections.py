from unittest.mock import patch
from view_sdk.resources.lexi.collections import Collection
from view_sdk.models.enumeration_query import EnumerationQueryModel


@patch("view_sdk.resources.lexi.collections.super")
def test_retrieve_top_terms(mock_super):
    mock_super().retrieve.return_value = "top_terms_result"
    result = Collection.retrieve_top_terms("col-guid", max_keys=5)
    assert result == "top_terms_result"
    assert Collection.PARENT_RESOURCE == "collections"
    assert Collection.PARENT_ID_PARAM == "collection_guid"
    assert Collection.RESOURCE_NAME == "topterms"
    mock_super().retrieve.assert_called()


@patch("view_sdk.resources.lexi.collections.super")
def test_enumerate_documents(mock_super):
    mock_super().create.return_value = "enumerate_result"
    dummy_data = EnumerationQueryModel()
    result = Collection.enumerate_documents("col-guid", dummy_data)
    assert result == "enumerate_result"
    assert Collection.PARENT_RESOURCE == "collections"
    assert Collection.PARENT_ID_PARAM == "collection_guid"
    assert Collection.RESOURCE_NAME == "documents"
    assert Collection.QUERY_PARAMS == {"enumerate": None}
    assert Collection.CREATE_METHOD == "POST"
    assert Collection.MODEL is None
    mock_super().create.assert_called()


@patch("view_sdk.resources.lexi.collections.super")
def test_search_default(mock_super):
    mock_super().create.return_value = "search_result"
    result = Collection.search("col-guid", foo="bar")
    assert result == "search_result"
    assert Collection.QUERY_PARAMS == {"search": None}
    mock_super().create.assert_called()


@patch("view_sdk.resources.lexi.collections.super")
def test_search_include_data(mock_super):
    mock_super().create.return_value = "search_result"
    result = Collection.search("col-guid", include_data=True)
    assert result == "search_result"
    assert Collection.QUERY_PARAMS == {"search": None, "incldata": None}
    mock_super().create.assert_called()


@patch("view_sdk.resources.lexi.collections.super")
def test_search_include_top_terms(mock_super):
    mock_super().create.return_value = "search_result"
    result = Collection.search("col-guid", include_top_terms=True)
    assert result == "search_result"
    assert Collection.QUERY_PARAMS == {"search": None, "incltopterms": None}
    mock_super().create.assert_called()


@patch("view_sdk.resources.lexi.collections.super")
def test_search_emit_results(mock_super):
    mock_super().create.return_value = "search_result"
    result = Collection.search("col-guid", emit_results=True)
    assert result == "search_result"
    assert Collection.QUERY_PARAMS == {"search": None, "async": None}
    mock_super().create.assert_called()
