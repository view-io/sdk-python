from ...mixins import (
    AllRetrievableAPIResource,
    DeletableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
    EnumerableAPIResource,
)
from ...models.object_lock import ObjectLockModel


class ObjectLock(
    ExistsAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    DeletableAPIResource,
    EnumerableAPIResource,
):
    RESOURCE_NAME: str = "objectlocks"
    MODEL = ObjectLockModel
