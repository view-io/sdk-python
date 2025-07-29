import pytest
from datetime import datetime, timezone
from view_sdk.models.account import AccountModel


def test_account_model_defaults():
    account = AccountModel()
    assert account.id == 0
    assert account.guid is not None
    assert account.name is None
    assert account.additional_data is None
    assert account.created_utc is not None
    assert account.created_utc.tzinfo == timezone.utc


def test_account_model_validate_id():
    with pytest.raises(ValueError):
        AccountModel(id=-1)
    account = AccountModel(id=10)
    assert account.id == 10


def test_account_model_guid_generation():
    account1 = AccountModel()
    account2 = AccountModel()
    assert account1.guid != account2.guid
    assert len(account1.guid) == 36  # UUID length


def test_account_model_created_utc():
    before_creation = datetime.now(timezone.utc)
    account = AccountModel()
    after_creation = datetime.now(timezone.utc)
    assert before_creation <= account.created_utc <= after_creation
