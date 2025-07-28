from typing import List

from pydantic import BaseModel, ConfigDict, Field

from .acl_entry import ACLEntryModel
from .user_master import UserMasterModel


class ACLModel(BaseModel):
    owner: UserMasterModel = Field(alias="Owner")
    users: List[UserMasterModel] = Field(alias="Users")
    entries: List[ACLEntryModel] = Field(alias="Entries")

    model_config = ConfigDict(populate_by_name=True)
