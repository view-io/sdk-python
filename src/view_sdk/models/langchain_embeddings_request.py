from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class LangchainEmbeddingsRequest(BaseModel):
    """Langchain embeddings request."""

    model: Optional[str] = Field(
        default=None, alias="Model", description="Model used to generate embeddings"
    )

    api_key: Optional[str] = Field(
        default=None, alias="ApiKey", description="API key for Huggingface"
    )

    contents: List[str] = Field(
        default_factory=list, alias="Contents", description="Contents"
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
