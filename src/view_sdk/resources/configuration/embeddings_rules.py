from ...mixins import (
    AllRetrievableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    ExistsAPIResource,
    RetrievableAPIResource,
    UpdatableAPIResource,
    EnumerableAPIResource
)
from ...models.embeddings_rule import EmbeddingsRuleModel


class EmbeddingsRule(
    ExistsAPIResource,
    CreateableAPIResource,
    RetrievableAPIResource,
    AllRetrievableAPIResource,
    UpdatableAPIResource,
    DeletableAPIResource,
    EnumerableAPIResource
):
    RESOURCE_NAME: str = "embeddingsrules"
    MODEL = EmbeddingsRuleModel
