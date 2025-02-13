import pytest
from unittest.mock import patch, Mock
from base64 import b64encode
import view_sdk
from view_sdk.resources.semantic.semantic_cell import SemanticCell
from view_sdk.models.semantic_cell_response import SemanticCellResponse
from view_sdk.models.semantic_cell_request import SemanticCellRequest
from view_sdk.enums.document_type_enum import DocumentTypeEnum
from view_sdk.models.metadata_rule import MetadataRuleModel
from view_sdk.models.pdf_options import PdfOptionsModel

@pytest.fixture(autouse=True)
def configure_sdk():
    # Configuring the SDK before running tests
    view_sdk.configure(
        tenant_guid="test_tenant_guid",
        access_key="test_access_key",
        base_url="localhost",  # Use localhost to simulate a server
        secure=False
    )

@pytest.fixture
def valid_metadata_rule():
    return MetadataRuleModel(semantic_cell_endpoint="https://example.com/endpoint")

@pytest.fixture
def valid_semantic_request(valid_metadata_rule):
    return SemanticCellRequest(
        document_type=DocumentTypeEnum.Pdf,
        metadata_rule=valid_metadata_rule,
        data_=b"test binary data",
        max_chunk_content_length=512,
        shift_size=512
    )

@patch('view_sdk.mixins.get_client')
def test_semantic_cell_process_valid_request(mock_get_client, valid_semantic_request):
    mock_client = Mock()
    mock_get_client.return_value = mock_client

    response_data = SemanticCellResponse(data_=b"test binary data").model_dump(by_alias=True)
    mock_client.request.return_value = response_data

    response = SemanticCell.process(request=valid_semantic_request)

    assert isinstance(response, SemanticCellResponse)
    assert response.data_ == b"test binary data"

    call_args = mock_client.request.call_args
    assert call_args[0][0] == "POST"
    assert "/semanticcell" in call_args[0][1]

def test_semantic_cell_process_missing_data(valid_metadata_rule):
    invalid_request = SemanticCellRequest(
        document_type=DocumentTypeEnum.Pdf,
        metadata_rule=valid_metadata_rule,
        data_=None,
        max_chunk_content_length=512,
        shift_size=512
    )

    with pytest.raises(ValueError) as exc_info:
        SemanticCell.process(request=invalid_request)
    assert str(exc_info.value) == "No data supplied for semantic cell extraction."

def test_semantic_cell_process_missing_metadata_rule():
    invalid_request = SemanticCellRequest(
        document_type=DocumentTypeEnum.Pdf,
        metadata_rule=None,
        data_=b"test binary data",
        max_chunk_content_length=512,
        shift_size=512
    )

    with pytest.raises(ValueError) as exc_info:
        SemanticCell.process(request=invalid_request)
    assert str(exc_info.value) == "Metadata rule is required."

@patch('view_sdk.mixins.get_client')
def test_semantic_cell_process_document_valid(mock_get_client, valid_metadata_rule):
    mock_client = Mock()
    mock_get_client.return_value = mock_client

    response_data = SemanticCellResponse(data_=b"test binary data").model_dump(by_alias=True)
    mock_client.request.return_value = response_data

    response = SemanticCell.process_document(
        doc_type=DocumentTypeEnum.Pdf,
        metadata_rule=valid_metadata_rule,
        data=b"test binary data"
    )

    assert isinstance(response, SemanticCellResponse)
    assert response.data_ == b"test binary data"

@patch('view_sdk.mixins.get_client')
def test_semantic_cell_process_document_with_pdf_options(mock_get_client, valid_metadata_rule):
    mock_client = Mock()
    mock_get_client.return_value = mock_client

    response_data = SemanticCellResponse(data_=b"test binary data").model_dump(by_alias=True)
    mock_client.request.return_value = response_data

    pdf_options = PdfOptionsModel(option_name="sample_option")

    response = SemanticCell.process_document(
        doc_type=DocumentTypeEnum.Pdf,
        metadata_rule=valid_metadata_rule,
        data=b"test binary data",
        pdf_options=pdf_options
    )

    assert isinstance(response, SemanticCellResponse)
    assert response.data_ == b"test binary data"

def test_semantic_cell_process_document_missing_data(valid_metadata_rule):
    with pytest.raises(ValueError) as exc_info:
        SemanticCell.process_document(
            doc_type=DocumentTypeEnum.Pdf,
            metadata_rule=valid_metadata_rule,
            data=None
        )
    assert str(exc_info.value) == "No data supplied for semantic cell extraction."

def test_semantic_cell_process_document_invalid_metadata_rule():
    with pytest.raises(ValueError) as exc_info:
        SemanticCell.process_document(
            doc_type=DocumentTypeEnum.Pdf,
            metadata_rule=None,
            data=b"test binary data"
        )
    assert str(exc_info.value) == "Metadata rule is required."
