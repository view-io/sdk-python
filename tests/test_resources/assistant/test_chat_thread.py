import pytest
from unittest.mock import patch
from view_sdk.resources.assistant.chat_thread import ChatThread

@patch('view_sdk.resources.assistant.chat_thread.super')
def test_append(mock_super):
    mock_super().create.return_value = 'appended'
    result = ChatThread.append('thread123', foo='bar')
    assert result == 'appended'
    assert ChatThread.PARENT_RESOURCE == 'assistant/threads'
    assert ChatThread.PARENT_ID_PARAM == 'thread_id'
    assert ChatThread.RESOURCE_NAME == 'messages'
    assert ChatThread.CREATE_METHOD == 'POST'
    mock_super().create.assert_called_with(thread_id='thread123', messages=None, _data={'foo': 'bar'}) 