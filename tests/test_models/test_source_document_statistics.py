import pytest
from view_sdk.models.source_document_statistics import SourceDocumentStatisticsModel
from view_sdk.models.source_document import SourceDocumentModel
from view_sdk.models.udr_document import UdrDocumentModel
from view_sdk.models.semantic_cell import SemanticCellModel
from view_sdk.models.semantic_chunk import SemanticChunkModel
from view_sdk.models.schema_result import SchemaResultModel
from view_sdk.enums.document_type_enum import DocumentTypeEnum
from view_sdk.models.data_node import DataNodeModel
from view_sdk.enums.data_type_enum import DataTypeEnum


class TestSourceDocumentStatisticsModel:
    """Test cases for SourceDocumentStatisticsModel."""

    @pytest.fixture
    def mock_source_document(self):
        """Create a mock source document."""
        return SourceDocumentModel(
            guid="test-doc-guid",
            tenant_guid="test-tenant-guid",
            collection_guid="test-collection-guid",
        )

    @pytest.fixture
    def mock_udr_document_empty(self):
        """Create an empty UDR document."""
        return UdrDocumentModel(type=DocumentTypeEnum.Text)

    @pytest.fixture
    def mock_udr_document_with_terms(self):
        """Create a UDR document with terms."""
        udr = UdrDocumentModel(type=DocumentTypeEnum.Text)
        udr.terms = ["term1", "term2", "term3", "term1", "term2"]  # 5 terms, 3 distinct
        return udr

    @pytest.fixture
    def mock_schema_with_flattened(self):
        """Create a schema with flattened key-value pairs."""
        schema = SchemaResultModel()
        schema.flattened = [
            DataNodeModel(key="key1", type_=DataTypeEnum.String, data="value1"),
            DataNodeModel(key="key2", type_=DataTypeEnum.String, data="value2"),
            DataNodeModel(key="key3", type_=DataTypeEnum.String, data="value3"),
        ]
        return schema

    @pytest.fixture
    def mock_semantic_chunk(self):
        """Create a semantic chunk."""
        return SemanticChunkModel(
            guid="chunk-guid",
            content="test chunk content",  # length will be auto-calculated as 18
        )

    @pytest.fixture
    def mock_semantic_cell(self, mock_semantic_chunk):
        """Create a semantic cell with chunks."""
        return SemanticCellModel(
            guid="cell-guid", chunks=[mock_semantic_chunk], children=[]
        )

    @pytest.fixture
    def mock_nested_semantic_cells(self):
        """Create nested semantic cells structure."""
        chunk1 = SemanticChunkModel(guid="chunk1", content="content1")  # length = 8
        chunk2 = SemanticChunkModel(guid="chunk2", content="content2")  # length = 8

        child_cell = SemanticCellModel(guid="child-cell", chunks=[chunk2], children=[])

        parent_cell = SemanticCellModel(
            guid="parent-cell", chunks=[chunk1], children=[child_cell]
        )

        return [parent_cell]

    def test_basic_properties(self, mock_source_document):
        """Test basic computed properties."""
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)

        assert stats.tenant_guid == "test-tenant-guid"
        assert stats.collection_guid == "test-collection-guid"
        assert stats.source_document_guid == "test-doc-guid"

    def test_terms_empty_udr(self, mock_source_document):
        """Test terms count with no UDR document."""
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats.terms == 0

    def test_terms_with_udr_no_terms(
        self, mock_source_document, mock_udr_document_empty
    ):
        """Test terms count with UDR document but no terms."""
        mock_source_document.udr_document = mock_udr_document_empty
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats.terms == 0

    def test_terms_with_terms(self, mock_source_document, mock_udr_document_with_terms):
        """Test terms count with actual terms."""
        mock_source_document.udr_document = mock_udr_document_with_terms
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats.terms == 5

    def test_distinct_terms_empty_udr(self, mock_source_document):
        """Test distinct terms count with no UDR document."""
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats.distinct_terms == 0

    def test_distinct_terms_with_terms(
        self, mock_source_document, mock_udr_document_with_terms
    ):
        """Test distinct terms count with actual terms."""
        mock_source_document.udr_document = mock_udr_document_with_terms
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats.distinct_terms == 3

    def test_key_value_pairs_no_udr(self, mock_source_document):
        """Test key-value pairs count with no UDR document."""
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats.key_value_pairs == 0

    def test_key_value_pairs_no_schema(
        self, mock_source_document, mock_udr_document_empty
    ):
        """Test key-value pairs count with UDR but no schema."""
        mock_source_document.udr_document = mock_udr_document_empty
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats.key_value_pairs == 0

    def test_key_value_pairs_with_schema(
        self, mock_source_document, mock_udr_document_empty, mock_schema_with_flattened
    ):
        """Test key-value pairs count with schema and flattened data."""
        mock_udr_document_empty.schema_ = mock_schema_with_flattened
        mock_source_document.udr_document = mock_udr_document_empty
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats.key_value_pairs == 3

    def test_semantic_cells_no_udr(self, mock_source_document):
        """Test semantic cells count with no UDR document."""
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats.semantic_cells == 0

    def test_semantic_cells_no_cells(
        self, mock_source_document, mock_udr_document_empty
    ):
        """Test semantic cells count with UDR but no cells."""
        mock_source_document.udr_document = mock_udr_document_empty
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats.semantic_cells == 0

    def test_semantic_cells_with_cells(
        self, mock_source_document, mock_udr_document_empty, mock_semantic_cell
    ):
        """Test semantic cells count with actual cells."""
        mock_udr_document_empty.semantic_cells = [mock_semantic_cell]
        mock_source_document.udr_document = mock_udr_document_empty
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats.semantic_cells == 1

    def test_semantic_cells_nested(
        self, mock_source_document, mock_udr_document_empty, mock_nested_semantic_cells
    ):
        """Test semantic cells count with nested structure."""
        mock_udr_document_empty.semantic_cells = mock_nested_semantic_cells
        mock_source_document.udr_document = mock_udr_document_empty
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats.semantic_cells == 2  # parent + child

    def test_semantic_cell_bytes_no_udr(self, mock_source_document):
        """Test semantic cell bytes with no UDR document."""
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats.semantic_cell_bytes == 0

    def test_semantic_cell_bytes_with_cells(
        self, mock_source_document, mock_udr_document_empty
    ):
        """Test semantic cell bytes calculation."""
        # Create chunks that will result in a specific total length
        chunk1 = SemanticChunkModel(guid="chunk1", content="a" * 50)  # length = 50
        chunk2 = SemanticChunkModel(guid="chunk2", content="b" * 50)  # length = 50

        # Create a cell with chunks
        cell = SemanticCellModel(guid="test-cell", chunks=[chunk1, chunk2])

        mock_udr_document_empty.semantic_cells = [cell]
        mock_source_document.udr_document = mock_udr_document_empty
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats.semantic_cell_bytes == 100  # 50 + 50

    def test_semantic_chunks_no_udr(self, mock_source_document):
        """Test semantic chunks count with no UDR document."""
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats.semantic_chunks == 0

    def test_semantic_chunks_with_chunks(
        self, mock_source_document, mock_udr_document_empty, mock_semantic_cell
    ):
        """Test semantic chunks count with actual chunks."""
        mock_udr_document_empty.semantic_cells = [mock_semantic_cell]
        mock_source_document.udr_document = mock_udr_document_empty
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats.semantic_chunks == 1

    def test_semantic_chunks_nested(
        self, mock_source_document, mock_udr_document_empty, mock_nested_semantic_cells
    ):
        """Test semantic chunks count with nested structure."""
        mock_udr_document_empty.semantic_cells = mock_nested_semantic_cells
        mock_source_document.udr_document = mock_udr_document_empty
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats.semantic_chunks == 2  # one chunk in parent, one in child

    def test_semantic_chunk_bytes_no_udr(self, mock_source_document):
        """Test semantic chunk bytes with no UDR document."""
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats.semantic_chunk_bytes == 0

    def test_semantic_chunk_bytes_with_chunks(
        self, mock_source_document, mock_udr_document_empty, mock_nested_semantic_cells
    ):
        """Test semantic chunk bytes calculation."""
        mock_udr_document_empty.semantic_cells = mock_nested_semantic_cells
        mock_source_document.udr_document = mock_udr_document_empty
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats.semantic_chunk_bytes == 16  # 8 + 8 from nested chunks

    def test_count_semantic_cells_helper_empty(self, mock_source_document):
        """Test _count_semantic_cells helper with empty list."""
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats._count_semantic_cells([]) == 0

    def test_count_semantic_cells_helper_nested(
        self, mock_source_document, mock_nested_semantic_cells
    ):
        """Test _count_semantic_cells helper with nested structure."""
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats._count_semantic_cells(mock_nested_semantic_cells) == 2

    def test_sum_semantic_cell_bytes_helper_empty(self, mock_source_document):
        """Test _sum_semantic_cell_bytes helper with empty list."""
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats._sum_semantic_cell_bytes([]) == 0

    def test_count_semantic_chunks_helper_empty(self, mock_source_document):
        """Test _count_semantic_chunks helper with empty list."""
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats._count_semantic_chunks([]) == 0

    def test_count_semantic_chunks_helper_nested(
        self, mock_source_document, mock_nested_semantic_cells
    ):
        """Test _count_semantic_chunks helper with nested structure."""
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats._count_semantic_chunks(mock_nested_semantic_cells) == 2

    def test_sum_semantic_chunk_bytes_helper_empty(self, mock_source_document):
        """Test _sum_semantic_chunk_bytes helper with empty list."""
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert stats._sum_semantic_chunk_bytes([]) == 0

    def test_sum_semantic_chunk_bytes_helper_nested(
        self, mock_source_document, mock_nested_semantic_cells
    ):
        """Test _sum_semantic_chunk_bytes helper with nested structure."""
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        assert (
            stats._sum_semantic_chunk_bytes(mock_nested_semantic_cells) == 16
        )  # 8 + 8

    def test_source_document_excluded_from_serialization(self, mock_source_document):
        """Test that source_document is excluded from serialization."""
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        serialized = stats.model_dump()

        # source_document should not be in serialized output due to exclude=True
        assert "source_document" not in serialized
        assert "SourceDocument" not in serialized

        # But computed fields should be present
        assert "tenant_guid" in serialized
        assert "collection_guid" in serialized
        assert "source_document_guid" in serialized

    def test_model_config_populate_by_name(self, mock_source_document):
        """Test that the model supports population by alias names."""
        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)
        serialized = stats.model_dump(by_alias=True)

        # Should use alias names when serializing
        assert isinstance(serialized, dict)
        # Computed fields don't have aliases in this model, so they keep their original names
        assert "tenant_guid" in serialized

    def test_comprehensive_integration(self, mock_source_document):
        """Test a comprehensive scenario with all data types."""
        # Create a comprehensive UDR document
        udr = UdrDocumentModel(type=DocumentTypeEnum.Text)
        udr.terms = ["apple", "banana", "apple", "cherry"]  # 4 terms, 3 distinct

        # Add schema with flattened data
        schema = SchemaResultModel()
        schema.flattened = [
            DataNodeModel(key="name", type_=DataTypeEnum.String, data="test"),
            DataNodeModel(key="type", type_=DataTypeEnum.String, data="document"),
            DataNodeModel(key="size", type_=DataTypeEnum.String, data="large"),
        ]
        udr.schema_ = schema

        # Add nested semantic cells with chunks
        chunk1 = SemanticChunkModel(guid="chunk1", content="content1")  # length = 8
        chunk2 = SemanticChunkModel(guid="chunk2", content="content2")  # length = 8
        chunk3 = SemanticChunkModel(guid="chunk3", content="content3")  # length = 8

        child_cell = SemanticCellModel(
            guid="child-cell", chunks=[chunk2, chunk3], children=[]
        )

        parent_cell = SemanticCellModel(
            guid="parent-cell", chunks=[chunk1], children=[child_cell]
        )

        udr.semantic_cells = [parent_cell]
        mock_source_document.udr_document = udr

        stats = SourceDocumentStatisticsModel(source_document=mock_source_document)

        # Verify all computed properties
        assert stats.terms == 4
        assert stats.distinct_terms == 3
        assert stats.key_value_pairs == 3
        assert stats.semantic_cells == 2  # parent + child
        assert (
            stats.semantic_cell_bytes == 40
        )  # parent(8 + child's 16) + child(16) = 40
        assert stats.semantic_chunks == 3  # 1 in parent + 2 in child
        assert stats.semantic_chunk_bytes == 24  # 8 + 8 + 8
