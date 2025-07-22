from ...mixins import (
    AllRetrievableAPIResource,
    DeletableAPIResource,
    EnumerableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
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
