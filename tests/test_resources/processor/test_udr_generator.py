import pytest
from unittest.mock import Mock, patch
import uuid
from base64 import b64encode

from view_sdk.models.udr_document import UdrDocumentModel
from view_sdk.resources.processor.udr_generator import UdrGenerator
from view_sdk.sdk_configuration import SdkConfiguration
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
    with patch("httpx.Client") as mock:
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
        "Postings": [],
    }


@pytest.fixture
def sample_document_data():
    return b64encode(b"Sample document content").decode("utf-8")


def test_process_document_success(
    mock_http_client, sample_udr_response, sample_document_data
):
    # Setup mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = sample_udr_response
    mock_http_client.request.return_value = mock_response

    # Test with file
    result = UdrGenerator.generate(
        data=sample_document_data, type_=DocumentTypeEnum.Text
    )

    assert isinstance(result, UdrDocumentModel)
    assert result.guid == sample_udr_response["GUID"]
    assert result.success == sample_udr_response["Success"]

    # Test with direct data
    result = UdrGenerator.generate(data=b"Direct content", type_=DocumentTypeEnum.Text)

    assert isinstance(result, UdrDocumentModel)
    assert result.guid == sample_udr_response["GUID"]
