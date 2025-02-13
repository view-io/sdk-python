from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class PreloadModelsRequest(BaseModel):
    """Preload models request."""

    models: List[str] = Field(default_factory=list, alias="Models")
    api_key: Optional[str] = Field(None, alias="ApiKey")

    model_config = ConfigDict(populate_by_name=True)
