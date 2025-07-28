from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from .generate_embeddings_result import GenerateEmbeddingsResultModel
from .generate_embeddings_request import GenerateEmbeddingsRequestModel
from .content_embedding import ContentEmbeddingModel
from .api_error_response import ApiErrorResponseModel


class OpenAiEmbeddings(BaseModel):
    """OpenAI embeddings data."""

    index: int
    embeddings: List[float]
    object: Optional[str]


class OpenAiEmbeddingsResult(BaseModel):
    """OpenAI embeddings result."""

    object: Optional[str] = Field(default=None, alias="Object")
    data: List[OpenAiEmbeddings] = Field(default_factory=list, alias="Data")

    model_config = ConfigDict(populate_by_name=True)

    def to_embeddings_result(
        self,
        req: "GenerateEmbeddingsRequestModel",
        success: bool = True,
        status_code: int = 200,
        error: "ApiErrorResponseModel" = None,
    ) -> "GenerateEmbeddingsResultModel":
        if req is None:
            raise ValueError("Request cannot be None")

        result = GenerateEmbeddingsResultModel(
            success=success,
            status_code=status_code,
            error=error,
            semantic_cells=getattr(req, "semantic_cells", []),
            content_embeddings=[],
        )

        # Map contents to ContentEmbeddingModel
        if req.contents:
            for content in req.contents:
                result.content_embeddings.append(
                    ContentEmbeddingModel(content=content, embeddings=[])
                )

        # Map OpenAI embeddings to content embeddings by index
        if self.data:
            for embed in self.data:
                if embed.index < len(result.content_embeddings):
                    result.content_embeddings[embed.index].embeddings = embed.embeddings

        # Update semantic chunk embeddings if semantic_cells and content_embeddings are present
        if result.semantic_cells and result.content_embeddings:
            # Flatten all chunks from all semantic cells
            all_chunks = [
                chunk
                for cell in result.semantic_cells
                for chunk in getattr(cell, "chunks", [])
            ]
            for chunk in all_chunks:
                for c_embed in result.content_embeddings:
                    if chunk.content == c_embed.content:
                        chunk.embeddings = c_embed.embeddings

        return result
