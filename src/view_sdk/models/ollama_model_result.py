from datetime import datetime
from typing import Any, List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class OllamaModelDetail(BaseModel):
    """Ollama model detail."""

    name: Optional[str] = Field(default=None, alias="name", description="Name")

    model: Optional[str] = Field(default=None, alias="model", description="Model")

    last_modified_utc: Optional[datetime] = Field(
        default=None,
        alias="modified_at",
        description="Last modified timestamp, in UTC time",
    )

    size: int = Field(
        default=0,
        alias="size",
        description="Size",
        ge=0,  # Ensures non-negative value
    )

    digest: Optional[str] = Field(default=None, alias="digest", description="Digest")

    details: Optional[Any] = Field(default=None, alias="details", description="Details")

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)


class OllamaModelResult(BaseModel):
    """Ollama model result."""

    models: List[OllamaModelDetail] = Field(
        default_factory=list, alias="models", description="List of model details"
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)

    @field_validator("models", mode="before")
    def validate_models(
        cls, v: Optional[List[OllamaModelDetail]]
    ) -> List[OllamaModelDetail]:
        """Ensure models is never None."""
        return v or []
