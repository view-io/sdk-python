import uuid
import pytest
from datetime import datetime, timezone
from view_sdk.models.udr_document import UdrDocumentModel
from view_sdk.models.api_error_response import ApiErrorResponseModel
from view_sdk.models.schema_result import SchemaResultModel
from view_sdk.models.semantic_cell import SemanticCellModel
from view_sdk.models.semantic_chunk import SemanticChunkModel
from view_sdk.models.posting import PostingModel
from view_sdk.enums.document_type_enum import DocumentTypeEnum
from view_sdk.enums.api_error_enum import ApiErrorEnum
from view_sdk.enums.semantic_cell_type_enum import SemanticCellTypeEnum
from view_sdk.models.timestamp import TimestampModel


@pytest.fixture
def basic_udr_document():
    return UdrDocumentModel(
        GUID=str(uuid.uuid4()),
        Success=True,
        Timestamp=TimestampModel(
            Start=datetime.now(timezone.utc),
            End=datetime.now(timezone.utc)
        ),
        Type=DocumentTypeEnum.Unknown,
        Terms=["term1", "term2", "term1", "term3"],
        Metadata={"key": "value"}
    )

@pytest.fixture
def error_response():
    return ApiErrorResponseModel(
        Error=ApiErrorEnum.bad_request,
        Context="Test error context",
        Description="Test error description"
    )

class TestUdrDocumentModel:
    def test_basic_fields(self, basic_udr_document):
        assert isinstance(basic_udr_document.guid, str)
        assert basic_udr_document.success is True
        assert isinstance(basic_udr_document.timestamp, TimestampModel)
        assert isinstance(basic_udr_document.timestamp.start, datetime)
        assert isinstance(basic_udr_document.timestamp.end, datetime)
        assert basic_udr_document.type == DocumentTypeEnum.Unknown
        assert len(basic_udr_document.terms) == 4
        assert basic_udr_document.metadata == {"key": "value"}

    def test_default_values(self):
        timestamp = TimestampModel(
            Start=datetime.now(timezone.utc),
            End=datetime.now(timezone.utc)
        )
        doc = UdrDocumentModel(Type=DocumentTypeEnum.Unknown, Timestamp=timestamp)
        assert doc.success is False
        assert isinstance(doc.timestamp, TimestampModel)
        assert doc.error is None
        assert doc.additional_data is None
        assert doc.metadata == {}
        assert doc.terms == []
        assert doc.postings == []
        assert doc.semantic_cells == []

    def test_error_handling(self, error_response):
        doc = UdrDocumentModel(
            Type=DocumentTypeEnum.Unknown,
            Error=error_response
        )
        assert doc.error.error == ApiErrorEnum.bad_request
        assert doc.error.context == "Test error context"
        assert doc.error.description == "Test error description"

    def test_metadata_validation(self):
        # Test with None metadata
        doc = UdrDocumentModel(Type=DocumentTypeEnum.Unknown, Metadata=None)
        assert doc.metadata == {}

        # Test with empty metadata
        doc = UdrDocumentModel(Type=DocumentTypeEnum.Unknown, Metadata={})
        assert doc.metadata == {}

    def test_terms_validation(self):
        # Test with None terms
        doc = UdrDocumentModel(Type=DocumentTypeEnum.Unknown, Terms=None)
        assert doc.terms == []

        # Test with empty terms
        doc = UdrDocumentModel(Type=DocumentTypeEnum.Unknown, Terms=[])
        assert doc.terms == []

    def test_postings_validation(self):
        # Test with None postings
        doc = UdrDocumentModel(Type=DocumentTypeEnum.Unknown, Postings=None)
        assert doc.postings == []

        # Test with empty postings
        doc = UdrDocumentModel(Type=DocumentTypeEnum.Unknown, Postings=[])
        assert doc.postings == []

    def test_top_terms(self, basic_udr_document):
        # Test default count
        top_terms = basic_udr_document.top_terms
        assert len(top_terms) <= 10
        assert top_terms["term1"] == 2  # Most frequent term
        assert top_terms["term2"] == 1
        assert top_terms["term3"] == 1

        # Test custom count
        top_terms = basic_udr_document.get_top_terms(count=2)
        assert len(top_terms) == 2
        assert "term1" in top_terms  # Most frequent term should be included

    def test_top_terms_invalid_count(self, basic_udr_document):
        with pytest.raises(ValueError, match="count must be greater than 0"):
            basic_udr_document.get_top_terms(count=0)

    def test_top_terms_empty(self):
        doc = UdrDocumentModel(Type=DocumentTypeEnum.Unknown)
        assert doc.top_terms == {}

    def test_top_terms_with_empty_strings(self):
        doc = UdrDocumentModel(
            Type=DocumentTypeEnum.Unknown,
            Terms=["term1", "", "term1", "", "term2"]
        )
        top_terms = doc.top_terms
        assert "" not in top_terms  # Empty strings should be filtered out
        assert top_terms["term1"] == 2
        assert top_terms["term2"] == 1

    def test_semantic_cells(self):
        chunk = SemanticChunkModel(
            Content="test cell content",
            Position=0
        )
        cell = SemanticCellModel(
            CellType=SemanticCellTypeEnum.Text,
            Position=0,
            Chunks=[chunk]
        )
        doc = UdrDocumentModel(
            Type=DocumentTypeEnum.Unknown,
            SemanticCells=[cell]
        )
        assert len(doc.semantic_cells) == 1
        assert doc.semantic_cells[0].chunks[0].content == "test cell content"
        assert doc.semantic_cells[0].chunks[0].length == len("test cell content")  # Length is auto-calculated
        assert doc.semantic_cells[0].length == len("test cell content")  # Cell length should match chunk length
