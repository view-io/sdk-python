import uuid
import pytest
from decimal import Decimal
from datetime import datetime, timezone
from view_sdk.models.source_document import SourceDocumentModel
from view_sdk.models.document_score import DocumentScoreModel
from view_sdk.models.udr_document import UdrDocumentModel
from view_sdk.enums.document_type_enum import DocumentTypeEnum
from view_sdk.models.timestamp import TimestampModel

@pytest.fixture
def basic_source_document():
    return SourceDocumentModel(
        GUID=str(uuid.uuid4()),
        TenantGUID=str(uuid.uuid4()),
        CollectionGUID=str(uuid.uuid4()),
        ObjectGUID=str(uuid.uuid4()),
        ObjectKey="test_document.txt",
        ObjectVersion="1",
        ContentType="text/plain",
        ContentLength=100,
        MD5Hash="test_hash",
        CreatedUtc=datetime.now(timezone.utc)
    )

@pytest.fixture
def document_score():
    return DocumentScoreModel(
        Score=Decimal("0.95"),
        TermsScore=Decimal("0.90"),
        FiltersScore=Decimal("0.85")
    )

class TestSourceDocumentModel:
    def test_basic_fields(self, basic_source_document):
        assert isinstance(basic_source_document.guid, str)
        assert isinstance(basic_source_document.tenant_guid, str)
        assert isinstance(basic_source_document.collection_guid, str)
        assert isinstance(basic_source_document.object_guid, str)
        assert basic_source_document.object_key == "test_document.txt"
        assert basic_source_document.object_version == "1"
        assert basic_source_document.content_type == "text/plain"
        assert basic_source_document.content_length == 100
        assert basic_source_document.md5_hash == "test_hash"
        assert isinstance(basic_source_document.created_utc, datetime)

    def test_default_values(self):
        # Test with minimum required fields
        doc = SourceDocumentModel(
            GUID=str(uuid.uuid4()),
            TenantGUID=str(uuid.uuid4()),
            CollectionGUID=str(uuid.uuid4()),
            ObjectGUID=str(uuid.uuid4()),
            MD5Hash="test_hash"
        )

        # Check default values
        assert doc.bucket_guid is None
        assert doc.data_flow_request_guid is None
        assert doc.graph_repository_guid is None
        assert doc.graph_node_identifier is None
        assert doc.data_repository_guid is None
        assert doc.object_key is None
        assert doc.object_version == "1"  # Default version
        assert doc.content_type == "application/octet-stream"  # Default content type
        assert doc.document_type == DocumentTypeEnum.Unknown
        assert doc.source_url is None
        assert doc.content_length == 0
        assert doc.sha1_hash is None
        assert doc.sha256_hash is None
        assert isinstance(doc.created_utc, datetime)
        assert doc.expiration_utc is None
        assert doc.score is None
        assert doc.udr_document is None

    def test_document_score(self, basic_source_document, document_score):
        doc = basic_source_document.model_copy()
        doc.score = document_score

        assert doc.score.score == Decimal("0.95")
        assert doc.score.terms_score == Decimal("0.90")
        assert doc.score.filters_score == Decimal("0.85")

    def test_udr_document(self, basic_source_document):
        timestamp = TimestampModel(
            StartUtc=datetime.now(timezone.utc),
            EndUtc=datetime.now(timezone.utc)
        )

        udr_doc = UdrDocumentModel(
            Type=DocumentTypeEnum.Unknown,
            Terms=["term1", "term2"],
            Timestamp=timestamp
        )

        doc = basic_source_document.model_copy()
        doc.udr_document = udr_doc

        assert doc.udr_document.terms == ["term1", "term2"]
        assert doc.udr_document.type == DocumentTypeEnum.Unknown
        assert doc.udr_document.success is False
        assert isinstance(doc.udr_document.timestamp, TimestampModel)
        assert doc.udr_document.error is None
        assert doc.udr_document.metadata == {}
        assert doc.udr_document.postings == []
        assert doc.udr_document.semantic_cells == []

    def test_expiration_date(self, basic_source_document):
        expiration = datetime.now(timezone.utc)
        doc = basic_source_document.model_copy()
        doc.expiration_utc = expiration

        assert doc.expiration_utc == expiration

    def test_hash_values(self, basic_source_document):
        doc = basic_source_document.model_copy()
        doc.sha1_hash = "test_sha1"
        doc.sha256_hash = "test_sha256"

        assert doc.sha1_hash == "test_sha1"
        assert doc.sha256_hash == "test_sha256"

    def test_graph_fields(self, basic_source_document):
        doc = basic_source_document.model_copy()
        doc.graph_repository_guid = str(uuid.uuid4())
        doc.graph_node_identifier = "test_node"

        assert isinstance(doc.graph_repository_guid, str)
        assert doc.graph_node_identifier == "test_node"

    def test_data_repository_fields(self, basic_source_document):
        doc = basic_source_document.model_copy()
        doc.data_repository_guid = str(uuid.uuid4())
        doc.data_flow_request_guid = str(uuid.uuid4())

        assert isinstance(doc.data_repository_guid, str)
        assert isinstance(doc.data_flow_request_guid, str)
