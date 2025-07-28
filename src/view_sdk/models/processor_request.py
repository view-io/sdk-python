import uuid
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field
from .object_metadata import ObjectMetadataModel


class ProcessorRequest(BaseModel):
    """Processor request model."""

    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    metadata_rule_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="MetadataRuleGUID"
    )
    embeddings_rule_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="EmbeddingsRuleGUID"
    )
    object: Optional[ObjectMetadataModel] = Field(None, alias="Object")

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
