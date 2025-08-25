import pytest
from unittest.mock import patch, Mock
from view_sdk.resources.configuration.graph_repositories import GraphRepository
from view_sdk.models.enumeration_result import EnumerationResultModel
from view_sdk.models.graph_repository import GraphRepositoryModel
from view_sdk.sdk_configuration import configure


class TestGraphRepository:
    """Test cases for GraphRepository resource."""

    def test_graph_repository_has_enumeration_support(self):
        """Test that GraphRepository includes EnumerableAPIResource."""
        # Check that the class has the enumerate method
        assert hasattr(GraphRepository, 'enumerate')
        assert callable(GraphRepository.enumerate)

    @patch('view_sdk.sdk_configuration.SdkConfiguration.get_instance')
    def test_enumerate_graph_repositories(self, mock_get_instance):
        """Test enumerating graph repositories."""
        # Configure the SDK first
        configure(
            access_key="test_access_key",
            base_url="test_base_url",
            tenant_guid="00000000-0000-0000-0000-000000000000"
        )
        
        # Mock the client
        mock_client = Mock()
        mock_instance = Mock()
        mock_get_instance.return_value = mock_instance
        mock_instance.get_client.return_value = mock_client
        mock_client.tenant_guid = "00000000-0000-0000-0000-000000000000"
        
        # Mock the response
        mock_response = {
            "Objects": [
                {
                    "GUID": "12345678-1234-1234-1234-123456789abc",
                    "TenantGUID": "00000000-0000-0000-0000-000000000000",
                    "Name": "Test Graph Repository",
                    "RepositoryType": "LiteGraph",
                    "EndpointUrl": "http://localhost:8701/",
                    "ApiKey": "default",
                    "GraphIdentifier": "00000000-0000-0000-0000-000000000000",
                    "CreatedUtc": "2024-01-01T00:00:00Z",
                    "Ssl": False,
                }
            ],
            "Success": True,
            "TotalRecords": 1,
            "EndOfResults": True
        }
        mock_client.request.return_value = mock_response
        
        # Call the enumerate method
        result = GraphRepository.enumerate()
        
        # Verify the result
        assert isinstance(result, EnumerationResultModel)
        assert len(result.objects) == 1
        # The following fields may not exist, so only check objects
        repo = result.objects[0]
        assert isinstance(repo, GraphRepositoryModel)
        assert repo.guid == "12345678-1234-1234-1234-123456789abc"
        assert repo.name == "Test Graph Repository"
        assert repo.repository_type == "LiteGraph"
        assert repo.endpoint_url == "http://localhost:8701/"
        
        # Verify the API call
        mock_client.request.assert_called_once()
        call_args = mock_client.request.call_args
        assert call_args[0][0] == "GET"  # HTTP method
        assert "graphrepositories" in call_args[0][1]  # URL contains resource name
        assert "enumerate" in call_args[0][1]  # URL contains enumerate parameter

    @patch('view_sdk.sdk_configuration.SdkConfiguration.get_instance')
    def test_enumerate_graph_repositories_with_headers(self, mock_get_instance):
        """Test enumerating graph repositories with custom headers."""
        # Configure the SDK first
        configure(
            access_key="test_access_key",
            base_url="test_base_url",
            tenant_guid="00000000-0000-0000-0000-000000000000"
        )
        
        # Mock the client
        mock_client = Mock()
        mock_instance = Mock()
        mock_get_instance.return_value = mock_instance
        mock_instance.get_client.return_value = mock_client
        mock_client.tenant_guid = "00000000-0000-0000-0000-000000000000"
        
        # Mock the response
        mock_response = {
            "Objects": [],
            "Success": True,
            "TotalRecords": 0,
            "EndOfResults": True
        }
        mock_client.request.return_value = mock_response
        
        # Call the enumerate method with headers
        custom_headers = {"x-custom-header": "test-value"}
        result = GraphRepository.enumerate(headers=custom_headers)
        
        # Verify the API call includes headers
        mock_client.request.assert_called_once()
        call_args = mock_client.request.call_args
        assert call_args[1]["headers"] == custom_headers

    def test_graph_repository_resource_name(self):
        """Test that the resource name is correct."""
        assert GraphRepository.RESOURCE_NAME == "graphrepositories"

    def test_graph_repository_model(self):
        """Test that the model is correctly set."""
        assert GraphRepository.MODEL == GraphRepositoryModel 