import uuid
import pytest
from datetime import datetime, timezone
from unittest.mock import patch

from view_sdk.resources.lexi.source_documents import SourceDocument
from view_sdk.models.source_document import SourceDocumentModel
from view_sdk.models.enumeration_result import EnumerationResultModel
from view_sdk.models.source_document_statistics import SourceDocumentStatisticsModel


@pytest.fixture
def mock_source_document():
    return {
        "GUID": str(uuid.uuid4()),
        "TenantGUID": str(uuid.uuid4()),
        "CollectionGUID": str(uuid.uuid4()),
        "ObjectGUID": str(uuid.uuid4()),
        "ObjectKey": "test_document.txt",
        "ObjectVersion": "1",
        "ContentType": "text/plain",
        "ContentLength": 100,
        "MD5Hash": "test_hash",
        "CreatedUtc": datetime.now(timezone.utc).isoformat(),
    }


@pytest.fixture
def collection_guid():
    return str(uuid.uuid4())


@pytest.fixture
def document_guid():
    return str(uuid.uuid4())


class TestSourceDocument:
    @patch("view_sdk.resources.lexi.source_documents.CreateableAPIResource.create")
    def test_create(self, mock_create, mock_source_document, collection_guid):
        mock_create.return_value = SourceDocumentModel(**mock_source_document)

        result = SourceDocument.create(
            collection_guid=collection_guid, **mock_source_document
        )

        assert isinstance(result, SourceDocumentModel)
        mock_create.assert_called_once_with(
            collection_guid=collection_guid, **mock_source_document
        )

    @patch("view_sdk.resources.lexi.source_documents.RetrievableAPIResource.retrieve")
    def test_retrieve(
        self, mock_retrieve, mock_source_document, collection_guid, document_guid
    ):
        mock_retrieve.return_value = SourceDocumentModel(**mock_source_document)

        result = SourceDocument.retrieve(document_guid, collection_guid)

        assert isinstance(result, SourceDocumentModel)
        mock_retrieve.assert_called_once_with(
            document_guid, collection_guid=collection_guid
        )

    @patch("view_sdk.resources.lexi.source_documents.RetrievableAPIResource.retrieve")
    def test_retrieve_with_data(
        self, mock_retrieve, mock_source_document, collection_guid, document_guid
    ):
        mock_retrieve.return_value = SourceDocumentModel(**mock_source_document)

        result = SourceDocument.retrieve(
            document_guid, collection_guid, include_data=True
        )

        assert isinstance(result, SourceDocumentModel)
        mock_retrieve.assert_called_once_with(
            document_guid, collection_guid=collection_guid, incldata=None
        )

    @patch("view_sdk.resources.lexi.source_documents.DeletableAPIResource.delete")
    def test_delete(self, mock_delete, collection_guid, document_guid):
        SourceDocument.delete(document_guid, collection_guid)

        mock_delete.assert_called_once_with(
            document_guid, collection_guid=collection_guid
        )

    @patch("view_sdk.resources.lexi.source_documents.DeletableAPIResource.delete")
    def test_delete_by_key_and_version(
        self, mock_delete, collection_guid, document_guid
    ):
        key = "test_key"
        version = "1"

        SourceDocument.delete_by_key_and_version(
            document_guid, collection_guid, key, version
        )

        mock_delete.assert_called_once_with(
            document_guid, collection_guid=collection_guid, key=key, versionId=version
        )

    @patch("view_sdk.resources.lexi.source_documents.ExistsAPIResource.exists")
    def test_exists(self, mock_exists, collection_guid, document_guid):
        mock_exists.return_value = True

        result = SourceDocument.exists(document_guid, collection_guid)

        assert result is True
        mock_exists.assert_called_once_with(
            document_guid, collection_guid=collection_guid
        )

    @patch(
        "view_sdk.resources.lexi.source_documents.RetrievableStatisticsMixin.retrieve_statistics"
    )
    def test_retrieve_statistics(
        self, mock_stats, collection_guid, document_guid, mock_source_document
    ):
        # Create a complete source document with UDR details
        mock_source_document.update(
            {
                "UdrDocument": {
                    "Type": "Unknown",
                    "Terms": ["term1", "term2", "term1"],
                    "Schema_": {"Flattened": [{"key": "value1"}, {"key": "value2"}]},
                    "SemanticCells": [
                        {
                            "GUID": str(uuid.uuid4()),
                            "CellType": "Text",
                            "Position": 0,
                            "Length": 100,
                            "Chunks": [
                                {
                                    "GUID": str(uuid.uuid4()),
                                    "Position": 0,
                                    "Length": 50,
                                    "Content": "chunk1",
                                },
                                {
                                    "GUID": str(uuid.uuid4()),
                                    "Position": 1,
                                    "Length": 50,
                                    "Content": "chunk2",
                                },
                            ],
                            "Children": [],
                        }
                    ],
                }
            }
        )

        # Create the source document model first
        source_doc = SourceDocumentModel(**mock_source_document)
        print(source_doc)
        # Create the statistics model with the source document
        mock_stats_data = {"SourceDocument": source_doc}

        mock_stats.return_value = SourceDocumentStatisticsModel(**mock_stats_data)

        result = SourceDocument.retrieve_statistics(
            document_guid, collection_guid=collection_guid
        )

        # Assert the computed fields
        assert isinstance(result, SourceDocumentStatisticsModel)
        assert result.terms == 3  # Total terms count
        assert result.distinct_terms == 2  # Unique terms count
        assert result.key_value_pairs == 0
        assert result.semantic_cells == 1
        assert result.semantic_cell_bytes == 12
        assert result.semantic_chunks == 2
        assert result.semantic_chunk_bytes == 12

        mock_stats.assert_called_once_with(
            document_guid, collection_guid=collection_guid
        )

    @patch(
        "view_sdk.resources.lexi.source_documents.EnumerableAPIResourceWithData.enumerate_with_query"
    )
    def test_enumerate_with_query(self, mock_enumerate, collection_guid):
        query = {"filter": "test"}
        mock_result = {"items": [], "continuation_token": None}
        mock_enumerate.return_value = EnumerationResultModel(**mock_result)

        result = SourceDocument.enumerate_with_query(collection_guid, **query)

        assert isinstance(result, EnumerationResultModel)
        mock_enumerate.assert_called_once_with(collection_guid=collection_guid, **query)

    @patch(
        "view_sdk.resources.lexi.source_documents.AllRetrievableAPIResource.retrieve_all"
    )
    def test_retrieve_all(
        self, mock_retrieve_all, mock_source_document, collection_guid
    ):
        mock_retrieve_all.return_value = [SourceDocumentModel(**mock_source_document)]

        result = SourceDocument.retrieve_all(collection_guid)

        assert isinstance(result, list)
        assert all(isinstance(item, SourceDocumentModel) for item in result)
        mock_retrieve_all.assert_called_once_with(collection_guid=collection_guid)
