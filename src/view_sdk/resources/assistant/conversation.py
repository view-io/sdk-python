from typing import Generator, List
from uuid import UUID

from ...mixins import (
    CreateableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    DeletableAPIResource,
)
from ...models.conversation import ConversationModel
from ...models.conversation_request import ConversationRequestModel
from ...models.conversation_with_messages import ConversationWithMessagesModel
from ...models.list_conversations import ListConversationsModel
from ...models.message_request import MessageRequestModel
from ...models.message import MessageModel
from ...sdk_configuration import Service, get_client
from ...utils.url_helper import _get_url_v1
from ...sdk_logging import log_debug, log_warning


class Conversation(
    CreateableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    DeletableAPIResource,
):
    """
    API resource class for managing conversations in the assistant service.

    This class provides methods for creating, retrieving, listing, and deleting
    conversations. It also supports adding messages to conversations and retrieving
    conversations with their messages.

    Both create and add_message methods are stream-only and return generators that yield
    SSE events during processing, including conversation_created, message_created,
    pipeline events, embedding events, search events, generation events, and error events.

    Attributes:
        RESOURCE_NAME (str): The API resource name for conversations.
        MODEL (Type[BaseModel]): The Pydantic model for conversations.
        REQUEST_MODEL (Type[BaseModel]): The Pydantic model for conversation requests.
        SERVICE (Service): The service type (ASSISTANT).
    """
    RESOURCE_NAME: str = "assistant/conversations"
    # MODEL = ConversationModel
    REQUEST_MODEL = ConversationRequestModel
    SERVICE = Service.ASSISTANT
    REQUIRES_TENANT = True
    CREATE_METHOD = "POST"

    @classmethod
    def create(cls, **kwargs) -> Generator[dict, None, None]:
        """
        Creates a new conversation with streaming SSE events.

        This method only supports streaming output and will always return a generator
        that yields Server-Sent Events during the conversation creation process.

        Args:
            **kwargs: Keyword arguments for the conversation request.
                - config_guid (UUID): The configuration GUID to use.
                - title (str): The conversation title.
                - message (str): The initial message content.
                - metadata (dict, optional): Additional metadata for the conversation.
                - documents (list, optional): Documents to attach to the conversation.
                - headers (dict, optional): Additional headers for the request.

        Returns:
            Generator[dict, None, None]: Stream of SSE events including conversation_created,
            message_created, pipeline events, embedding events, search events, generation
            events, and error events.

        Raises:
            ValueError: If tenant GUID is required but not provided.
        """
        try:
            client = get_client(cls.SERVICE)
            headers = kwargs.pop("headers", {})
            
            if cls.REQUIRES_TENANT and client.tenant_guid is None:
                raise ValueError("Tenant GUID is required for this resource.")

            # Validate the request data
            request_data = cls.REQUEST_MODEL.model_validate(kwargs)
            
            # Build the URL for creating a conversation
            url = _get_url_v1(cls, client.tenant_guid, cls.RESOURCE_NAME)
            
            log_debug("Making streaming conversation create request")
            for event in client.sse_request(
                cls.CREATE_METHOD,
                url,
                headers=headers,
                json=request_data.model_dump(mode="json", by_alias=True),
            ):
                yield event

        except Exception as e:
            log_warning(f"Error processing streaming conversation create request: {str(e)}")
            raise

    @classmethod
    def retrieve(cls, conversation_id: UUID, **kwargs) -> ConversationWithMessagesModel:
        """
        Retrieves a conversation by its ID.
        """
        cls.MODEL = ConversationWithMessagesModel
        return super().retrieve(conversation_id, **kwargs)

    @classmethod
    def retrieve_all(cls, **kwargs) -> ListConversationsModel:
        """
        Retrieves all conversations with pagination support.

        Args:
            **kwargs: Additional keyword arguments for filtering and pagination.
                - limit (int, optional): Maximum number of conversations to return.
                - offset (int, optional): Number of conversations to skip.
                - headers (dict, optional): Additional headers for the request.

        Returns:
            ListConversationsModel: A paginated list of conversations with metadata.

        Raises:
            ValueError: If tenant GUID is required but not provided.
        """
        cls.MODEL = None
        cls.RETURNS_LIST = False
        # Use the parent method to get the raw response
        response = super().retrieve_all(**kwargs)
        
        # If the response is already a ListConversationsModel, return it
        return ListConversationsModel.model_validate(response)

    @classmethod
    def add_message(cls, conversation_id: UUID, **kwargs) -> Generator[dict, None, None]:
        """
        Adds a message to an existing conversation with streaming SSE events.

        This method only supports streaming output and will always return a generator
        that yields Server-Sent Events during the message processing.

        Args:
            conversation_id (UUID): The ID of the conversation to add the message to.
            **kwargs: Keyword arguments for the message request.
                - message (str): The message content to add.
                - documents (list, optional): Documents to attach to the message.
                - headers (dict, optional): Additional headers for the request.

        Returns:
            Generator[dict, None, None]: Stream of SSE events including message_created,
            pipeline events, embedding events, search events, generation events, and error events.

        Raises:
            ValueError: If tenant GUID is required but not provided.
        """
        try:
            client = get_client(cls.SERVICE)
            headers = kwargs.pop("headers", {})
            
            if cls.REQUIRES_TENANT and client.tenant_guid is None:
                raise ValueError("Tenant GUID is required for this resource.")

            # Validate the message request data
            message_data = MessageRequestModel.model_validate(kwargs)
            
            # Build the URL for adding a message to the conversation
            if cls.REQUIRES_TENANT:
                url = _get_url_v1(cls, client.tenant_guid, cls.RESOURCE_NAME, str(conversation_id), "messages")
            else:
                url = _get_url_v1(cls, cls.RESOURCE_NAME, str(conversation_id), "messages")

            log_debug("Making streaming add message request")
            for event in client.sse_request(
                "POST", 
                url, 
                json=message_data.model_dump(mode="json", by_alias=True), 
                headers=headers
            ):
                yield event

        except Exception as e:
            log_warning(f"Error processing streaming add message request: {str(e)}")
            raise

    @classmethod
    def get_with_messages(cls, conversation_id: UUID, **kwargs) -> ConversationWithMessagesModel:
        """
        Retrieves a conversation along with all its messages.

        Args:
            conversation_id (UUID): The ID of the conversation to retrieve.
            **kwargs: Additional keyword arguments.
                - headers (dict, optional): Additional headers for the request.

        Returns:
            ConversationWithMessagesModel: The conversation with its messages.

        Raises:
            ValueError: If tenant GUID is required but not provided.
        """
        cls.MODEL = ConversationWithMessagesModel
        return super().retrieve(conversation_id, **kwargs)
