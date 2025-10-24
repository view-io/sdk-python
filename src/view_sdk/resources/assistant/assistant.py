import json
from typing import Generator, Optional

from ...mixins import CreateableAPIResource, UpdatableAPIResource
from ...models.assistant_rag_request import AssistantRagRequest
from ...sdk_configuration import Service, get_client
from ...sdk_logging import log_debug, log_warning
from ...utils.url_helper import _get_url_v1

class Assistant(CreateableAPIResource, UpdatableAPIResource):
    """Resource for Assistant operations."""

    RESOURCE_NAME: str = ""  # Base path is empty since we use specific endpoints
    SERVICE = Service.ASSISTANT
    REQUIRES_TENANT = True
    CREATE_METHOD = "POST"

    @classmethod
    def rag_LEGACY(cls, **kwargs) -> Generator[str, None, None]:
        """
        Process a RAG request.

        Args:
            **kwargs: Keyword arguments that will be validated against AssistantRagRequest model

        Returns:
            Generator yielding response tokens

        Raises:
            ValueError: If required parameters are missing
        """
        # Validate request data using the model
        rag_request = AssistantRagRequest.model_validate(kwargs)

        log_debug("Making RAG request")
        for event in get_client(cls.SERVICE).sse_request(
            cls.CREATE_METHOD,
            "v1.0/assistant/rag/",
            json=rag_request.model_dump(mode="json", by_alias=True),
        ):
            token = event.get("token") if isinstance(event, dict) else event
            if token:
                yield token

    @classmethod
    def chat_rag_messages(cls, **kwargs) -> Generator[str, None, None]:
        """
        Process a chat request with RAG messages

        Args:
            **kwargs: Keyword arguments that will be validated against AssistantChatRequest model

        Returns:
            Generator yielding response tokens

        Raises:
            ValueError: If required parameters are missing
        """
        stream = kwargs.get("Stream", False)
        if not stream:
            cls.RESOURCE_NAME = "assistant/rag/chat"
            return super().create(**kwargs)
        else:
            try:
                url = _get_url_v1(cls, get_client(cls.SERVICE).tenant_guid, "assistant/rag/chat")
                headers = kwargs.pop("headers", {})
                log_debug("Making chat request")
                for event in get_client(cls.SERVICE).sse_request(
                    cls.CREATE_METHOD,
                    url,
                    headers=headers,
                    json=kwargs,
                ):
                    token = event.get("token") if isinstance(event, dict) else event
                    if token:
                        yield token

            except Exception as e:
                log_warning(f"Error processing chat request: {str(e)}")
                return

    @classmethod
    def chat_config(cls, config_id: str, **kwargs) -> Generator[str, None, None]:
        """
        Process a chat request with RAG messages

        Args:
            config_id: The ID of the chat configuration
            **kwargs: Keyword arguments that will be validated against AssistantChatRequest model

        Returns:
            Generator yielding response tokens

        Raises:
            ValueError: If required parameters are missing
        """
        stream = kwargs.get("Stream", False)
        if not stream:
            cls.RESOURCE_NAME = "assistant/chat"
            cls.UPDATE_METHOD = "POST"
            return super().update(config_id, **kwargs)
        else:
            try:
                log_debug("Making chat request")
                for event in get_client(cls.SERVICE).sse_request(
                    cls.CREATE_METHOD,
                    "v1.0/assistant/chat/" + config_id,
                    json=kwargs,
                ):
                    token = event.get("token") if isinstance(event, dict) else event
                    if token:
                        yield token

            except Exception as e:
                log_warning(f"Error processing chat request: {str(e)}")
                return

    @classmethod
    def chat_only(cls, **kwargs):
        """
        Process a chat request with RAG messages

        Args:
            **kwargs: Keyword arguments that will be validated against AssistantChatRequest model

        Returns:
            Response data for non-streaming requests, or Generator yielding response tokens for streaming requests

        Raises:
            ValueError: If required parameters are missing
        """
        stream = kwargs.get("Stream", False)
        if not stream:
            cls.RESOURCE_NAME = "assistant/chat/completions"
            return super().create(**kwargs)
        else:
            try:
                log_debug("Making chat request")
                for event in get_client(cls.SERVICE).sse_request(
                    cls.CREATE_METHOD,
                    "v1.0/assistant/chat/completions",
                    json=kwargs,
                ):
                    token = event.get("token") if isinstance(event, dict) else event
                    if token:
                        yield token

            except Exception as e:
                log_warning(f"Error processing chat request: {str(e)}")
                return

    @staticmethod
    def _extract_token(json_data: str) -> Optional[str]:
        """Extract token from JSON data."""
        try:
            data = json.loads(json_data)
            return data.get("token")
        except Exception:
            return None
