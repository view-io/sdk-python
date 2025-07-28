from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from .ollama_model_result import OllamaModelResult


class ModelInformation(BaseModel):
    """Model information."""

    model: Optional[str] = Field(default=None, alias="Model", description="Model")

    size: int = Field(
        default=0,
        alias="Size",
        description="Size",
        ge=0,  # Ensures non-negative value
    )

    last_modified_utc: Optional[datetime] = Field(
        default=None,
        alias="LastModifiedUtc",
        description="Last modified timestamp, in UTC time",
    )

    md5_hash: Optional[str] = Field(
        default=None, alias="MD5Hash", description="MD5 hash"
    )

    sha1_hash: Optional[str] = Field(
        default=None, alias="SHA1Hash", description="SHA1 hash"
    )

    sha256_hash: Optional[str] = Field(
        default=None, alias="SHA256Hash", description="SHA256 hash"
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)

    @classmethod
    def from_ollama_response(
        cls, resp: Optional[OllamaModelResult]
    ) -> List["ModelInformation"]:
        """
        Create list of model information from Ollama model response.

        Args:
            resp: OllamaModelResult instance

        Returns:
            List of ModelInformation instances
        """
        if not resp or not resp.models:
            return []

        return [
            cls(
                model=model.model,
                size=model.size,
                last_modified_utc=model.last_modified_utc,
                sha256_hash=model.digest,
            )
            for model in resp.models
        ]
