import pytest
from unittest.mock import patch, MagicMock
from view_sdk.resources.vector.openai import OpenAI
from view_sdk.models.openai_embeddings_request import OpenAiEmbeddingsRequest
from view_sdk.models.openai_embeddings_result import OpenAiEmbeddingsResult
from view_sdk.sdk_configuration import EmbeddingDefaults


class TestOpenAI:
    def test_validate_connectivity_success(self):
        mock_client = MagicMock()
        mock_client.request = MagicMock()  # This won't raise an exception

        with patch(
            "view_sdk.resources.vector.openai.get_client", return_value=mock_client
        ) as mock_get_client:
            assert OpenAI.validate_connectivity() is True
            mock_get_client.assert_called_once()
            mock_client.request.assert_called_once_with("HEAD", "models")

    def test_validate_connectivity_failure(self):
        mock_client = MagicMock()
        mock_client.request = MagicMock(side_effect=Exception("Connection failed"))

        with patch(
            "view_sdk.resources.vector.openai.get_client", return_value=mock_client
        ) as mock_get_client:
            assert OpenAI.validate_connectivity() is False
            mock_get_client.assert_called_once()
            mock_client.request.assert_called_once_with("HEAD", "models")

    def test_generate_embeddings_success(self):
        # Setup
        mock_client = MagicMock()
        mock_client.access_key = "test_key"

        embed_request = OpenAiEmbeddingsRequest(
            input=["test text"], model="text-embedding-ada-002"
        )
        expected_result = OpenAiEmbeddingsResult(
            success=True, status_code=200, model="text-embedding-ada-002"
        )

        with patch(
            "view_sdk.resources.vector.openai.get_client", return_value=mock_client
        ):
            with patch(
                "view_sdk.resources.vector.openai.EmbeddingsGeneratorMixin.create"
            ) as mock_create:
                mock_create.return_value = expected_result

                # Execute
                result = OpenAI.generate_embeddings(embed_request)

                # Assert
                assert result == expected_result
                mock_create.assert_called_once()
                assert "Authorization" in mock_create.call_args[1]["headers"]

    def test_generate_embeddings_with_default_model(self):
        # Setup
        mock_client = MagicMock()
        mock_client.access_key = "test_key"
        embed_request = OpenAiEmbeddingsRequest(input=["test text"])

        with patch(
            "view_sdk.resources.vector.openai.get_client", return_value=mock_client
        ):
            with patch(
                "view_sdk.resources.vector.openai.EmbeddingsGeneratorMixin.create"
            ):
                # Execute
                OpenAI.generate_embeddings(embed_request)

                # Assert
                assert embed_request.model == EmbeddingDefaults.OPENAI_DEFAULT_MODEL

    def test_generate_embeddings_invalid_timeout(self):
        embed_request = OpenAiEmbeddingsRequest(
            input=["test text"], model="text-embedding-ada-002"
        )

        with pytest.raises(ValueError, match="Timeout must be greater than 0"):
            OpenAI.generate_embeddings(embed_request, timeout=0)

    def test_generate_embeddings_failure(self):
        # Setup
        mock_client = MagicMock()
        mock_client.access_key = "test_key"
        embed_request = OpenAiEmbeddingsRequest(
            input=["test text"], model="text-embedding-ada-002"
        )

        with patch(
            "view_sdk.resources.vector.openai.get_client", return_value=mock_client
        ):
            with patch(
                "view_sdk.resources.vector.openai.EmbeddingsGeneratorMixin.create"
            ) as mock_create:
                mock_create.side_effect = Exception("API Error")

                # Execute
                result = OpenAI.generate_embeddings(embed_request)

                # Assert
                assert isinstance(result, OpenAiEmbeddingsResult)
                assert result.object is None
                assert result.data == []
