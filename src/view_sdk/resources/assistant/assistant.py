import json
from typing import Generator, Optional

from ...mixins import CreateableAPIResource
from ...models.assistant_chat_request import AssistantChatRequest
from ...models.assistant_rag_request import AssistantRagRequest
from ...sdk_configuration import Service, get_client
from ...sdk_logging import log_debug, log_warning


class Assistant(CreateableAPIResource):
    """Resource for Assistant operations."""

    RESOURCE_NAME: str = ""  # Base path is empty since we use specific endpoints
    SERVICE = Service.ASSISTANT
    REQUIRES_TENANT = False
    CREATE_METHOD = "POST"

    @classmethod
    def process_rag(cls, **kwargs) -> Generator[str, None, None]:
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
            "v1.0/rag/",
            json=rag_request.model_dump(mode="json", by_alias=True),
        ):
            token = event.get("token") if isinstance(event, dict) else event
            if token:
                yield token

    @classmethod
    def process_chat(cls, **kwargs) -> Generator[str, None, None]:
        """
        Process a chat request.

        Args:
            **kwargs: Keyword arguments that will be validated against AssistantChatRequest model

        Returns:
            Generator yielding response tokens

        Raises:
            ValueError: If required parameters are missing
        """
        # Validate request data using the model
        chat_request = AssistantChatRequest.model_validate(kwargs)

        try:
            log_debug("Making chat request")
            for event in get_client(cls.SERVICE).sse_request(
                cls.CREATE_METHOD,
                "v1.0/chat/",
                json=chat_request.model_dump(mode="json"),
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
