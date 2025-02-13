from ...mixins import (
    EnumerableAPIResource,
    RetrievableAPIResource,
    UpdatableAPIResource,
)
from ...models.tenant_metadata import TenantMetadataModel


class Tenant(
    RetrievableAPIResource,
    UpdatableAPIResource,
    EnumerableAPIResource,
):
    RESOURCE_NAME: str = "tenants"
    MODEL = TenantMetadataModel
    REQUIRES_TENANT: bool = False
