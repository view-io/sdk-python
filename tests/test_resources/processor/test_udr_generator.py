import os
import pytest
from unittest.mock import Mock, patch
import uuid

from view_sdk.models.udr_document import UdrDocumentModel
from view_sdk.models.udr_document_request import UdrDocumentRequest
from view_sdk.models.udr_datatable_request import UdrDataTableRequest, DatabaseTypeEnum
from view_sdk.resources.processor.udr_generator import UdrGenerator
from view_sdk.sdk_configuration import SdkConfiguration
from view_sdk.exceptions import SdkException
from view_sdk.enums.document_type_enum import DocumentTypeEnum


@pytest.fixture(scope="module", autouse=True)
def configure_sdk():
    SdkConfiguration.get_instance().configure(
        tenant_guid="test_tenant_guid",
        access_key="test_access_key",
        base_url="http://localhost:8501",
        secure=False,
    )


@pytest.fixture(scope="function")
def mock_http_client():
    with patch('httpx.Client') as mock:
        client_instance = Mock()
        mock.return_value = client_instance
        yield client_instance


@pytest.fixture
def sample_udr_response():
    return {
        "GUID": str(uuid.uuid4()),
        "Success": True,
        "Error": None,
        "AdditionalData": None,
        "Metadata": {"key": "value"},
        "Key": "test_key",
        "Type": "Unknown",
        "Terms": ["sample", "terms"],
        "Schema": None,
        "Cells": [],
        "Text": "Sample processed text",
        "Postings": []
    }


@pytest.fixture
def sample_document_data():
    return b"Sample document content"


@pytest.fixture
def temp_document(tmp_path):
    doc_path = tmp_path / "test_doc.txt"
    doc_path.write_bytes(b"Sample document content")
    return str(doc_path)


@pytest.fixture
def temp_sqlite_db(tmp_path):
    db_path = tmp_path / "test.db"
    db_path.write_bytes(b"Sample SQLite DB content")
    return str(db_path)


def test_process_document_success(mock_http_client, sample_udr_response, temp_document):
    # Setup mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = sample_udr_response
    mock_http_client.request.return_value = mock_response

    # Test with file
    result = UdrGenerator.process_document(
        filename=temp_document,
        type_=DocumentTypeEnum.Text
    )

    assert isinstance(result, UdrDocumentModel)
    assert result.guid == sample_udr_response["GUID"]
    assert result.success == sample_udr_response["Success"]

    # Test with direct data
    result = UdrGenerator.process_document(
        data=b"Direct content",
        type_=DocumentTypeEnum.Text
    )

    assert isinstance(result, UdrDocumentModel)
    assert result.guid == sample_udr_response["GUID"]


def test_process_document_file_not_found():
    with pytest.raises(ValueError, match="File not found"):
        UdrGenerator.process_document(filename="nonexistent.txt")

def test_process_datatable_sqlite_success(mock_http_client, sample_udr_response, temp_sqlite_db):
    # Setup mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = sample_udr_response
    mock_http_client.post.return_value = mock_response

    result = UdrGenerator.process_datatable(
        filename=temp_sqlite_db,
        database_type=DatabaseTypeEnum.SQLITE,
        query="SELECT * FROM test"
    )

    assert isinstance(result, UdrDocumentModel)

def test_process_datatable_non_sqlite():
    with pytest.raises(ValueError, match="Filename should not be provided"):
        UdrGenerator.process_datatable(
            filename="test.db",
            database_type=DatabaseTypeEnum.POSTGRESQL,
            connection_string="postgresql://test",
            query="SELECT * FROM test"
        )


def test_process_datatable_sqlite_no_file():
    with pytest.raises(ValueError, match="Filename must be provided"):
        UdrGenerator.process_datatable(
            database_type=DatabaseTypeEnum.SQLITE,
            query="SELECT * FROM test"
        )


def test_process_datatable_error(mock_http_client, temp_sqlite_db):
    # Setup mock response to raise an exception
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = Exception("API Error")
    mock_http_client.request.return_value = mock_response

    result = UdrGenerator.process_datatable(
        filename=temp_sqlite_db,
        database_type=DatabaseTypeEnum.SQLITE,
        query="SELECT * FROM test"
    )
    assert result
