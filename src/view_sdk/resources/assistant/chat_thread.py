from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
    UpdatableAPIResource,
)


class ChatThread(
    CreateableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    UpdatableAPIResource,
    DeletableAPIResource,
):
    """
    ChatThread resource for Assistant operations.
    """

    RESOURCE_NAME: str = "assistant/threads"
    REQUIRES_TENANT = True
    CREATE_METHOD = "POST"
    RETURNS_LIST = False

    @classmethod
    def append(cls, thread_id: str, **kwargs) -> dict:
        """
        Append a message to a chat thread.
        """
        cls.PARENT_RESOURCE = "assistant/threads"
        cls.PARENT_ID_PARAM = "thread_id"
        cls.RESOURCE_NAME = "messages"
        cls.CREATE_METHOD = "POST"
        return super().create(thread_id=thread_id, messages=None, _data=kwargs)
