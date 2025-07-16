from ...mixins import (
    EnumerableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    UpdatableAPIResource,
    CreateableAPIResource,
    ExistsAPIResource,
    DeletableAPIResource
)
from ...models.tenant_metadata import TenantMetadataModel


class Tenant(
    RetrievableAPIResource,
    UpdatableAPIResource,   
    EnumerableAPIResource,
    CreateableAPIResource,
    AllRetrievableAPIResource,
    ExistsAPIResource,
    DeletableAPIResource
):
    RESOURCE_NAME: str = "tenants"
    MODEL = TenantMetadataModel
    REQUIRES_TENANT: bool = False
