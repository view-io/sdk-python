import pytest
from unittest.mock import Mock, patch
from typing import Optional

from view_sdk.enums.document_type_enum import DocumentTypeEnum
from view_sdk.models.type_result import TypeResultModel
from view_sdk.resources.processor.type_detector import TypeDetector


class TestTypeDetector:
    def test_process_empty_data(self):
        """Test that ValueError is raised when no data is provided."""
        with pytest.raises(ValueError, match="No data supplied for content type detection."):
            TypeDetector.process(data=b'')

    @patch('view_sdk.mixins.CreateableAPIResource.create')
    def test_process_with_data_and_content_type(self, mock_create):
        """Test processing with specific content type."""
        # Prepare mock return value
        expected_result = TypeResultModel(
            mime_type='text/csv',
            extension='.csv',
            type_=DocumentTypeEnum.Csv
        )
        mock_create.return_value = expected_result

        # Test the method
        result = TypeDetector.process(
            data=b'sample,data\n1,2', 
            content_type='text/csv'
        )

        # Verify interactions
        mock_create.assert_called_once_with(
            data=b'sample,data\n1,2', 
            content_type='text/csv'
        )
        assert result == expected_result

    @patch('view_sdk.mixins.CreateableAPIResource.create')
    def test_process_without_content_type(self, mock_create):
        """Test processing without explicit content type."""
        # Prepare mock return value
        expected_result = TypeResultModel(
            mime_type='application/octet-stream',
            extension=None,
            type_=DocumentTypeEnum.Unknown
        )
        mock_create.return_value = expected_result

        # Test the method
        result = TypeDetector.process(data=b'some binary data')

        # Verify interactions
        mock_create.assert_called_once_with(
            data=b'some binary data', 
            content_type='application/octet-stream'
        )
        assert result == expected_result

    @patch('view_sdk.mixins.CreateableAPIResource.create')
    def test_process_create_exception_handling(self, mock_create):
        """Test error handling when create method raises an exception."""
        # Simulate create method raising an exception
        mock_create.side_effect = Exception("API error")

        # Test the method
        result = TypeDetector.process(data=b'some data')

        # Verify default result is returned
        assert result.mime_type == 'application/octet-stream'
        assert result.extension is None
        assert result.type_ == DocumentTypeEnum.Unknown

    def test_type_result_model_default_values(self):
        """Test TypeResultModel default values."""
        result = TypeResultModel()
        assert result.mime_type is None
        assert result.extension is None
        assert result.type_ == DocumentTypeEnum.Unknown

    def test_type_result_model_custom_values(self):
        """Test TypeResultModel with custom values."""
        result = TypeResultModel(
            mime_type='application/pdf',
            extension='.pdf',
            type_=DocumentTypeEnum.Pdf
        )
        assert result.mime_type == 'application/pdf'
        assert result.extension == '.pdf'
        assert result.type_ == DocumentTypeEnum.Pdf