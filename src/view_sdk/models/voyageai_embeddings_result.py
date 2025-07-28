from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class VoyageAiEmbeddings(BaseModel):
    """VoyageAI embeddings."""

    embeddings: List[float] = Field(default_factory=list, alias="Embeddings")
    index: int = 0
    object_type: Optional[str] = Field(None, alias="Object")


class VoyageAiEmbeddingsResult(BaseModel):
    """VoyageAI embeddings result."""

    object: Optional[str] = Field(default=None, alias="Object")
    data: List[VoyageAiEmbeddings] = Field(default_factory=list, alias="Data")
    success: bool = Field(default=True, alias="Success")
    status_code: int = Field(default=200, alias="StatusCode")
    model: Optional[str] = Field(default=None, alias="Model")

    model_config = ConfigDict(populate_by_name=True)

    # def to_embeddings_result(self, req: "VoyageAiEmbeddingsRequest") -> "EmbeddingsResult":
    #     """Convert to embeddings result."""
    #     if not req:
    #         raise ValueError("Request cannot be None")

    #     if req.contents and self.data:
    #         if len(req.contents) != len(self.data):
    #             raise ValueError("The number of content elements does not match the number of embeddings elements.")

    #     result = []
    #     for embed in self.data:
    #         result.append({
    #             "content": req.contents[embed.index],
    #             "embeddings": embed.embeddings
    #         })

    #     return EmbeddingsResult(
    #         success=self.success,
    #         status_code=self.status_code,
    #         model=req.model,
    #         result=result
    #     )
