from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class OpenAiEmbeddingsRequest(BaseModel):
    """OpenAI embeddings request."""

    model: Optional[str] = Field(None, alias="Model")
    contents: List[str] = Field(default_factory=list, alias="Input")

    model_config = ConfigDict(populate_by_name=True)

    # @classmethod
    # def from_embeddings_request(cls, req: "EmbeddingsRequest") -> "OpenAiEmbeddingsRequest":
    #     """Create from embeddings request."""
    #     if not req:
    #         raise ValueError("Request cannot be None")

    #     return cls(
    #         model=req.model,
    #         contents=req.contents
    #     )
