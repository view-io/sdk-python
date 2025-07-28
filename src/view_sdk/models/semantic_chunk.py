import uuid
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class SemanticChunkModel(BaseModel):
    """Semantic chunk."""

    guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="GUID", description="GUID"
    )
    md5_hash: Optional[str] = Field(None, alias="MD5Hash", description="MD5")
    sha1_hash: Optional[str] = Field(None, alias="SHA1Hash", description="SHA1")
    sha256_hash: Optional[str] = Field(None, alias="SHA256Hash", description="SHA256")
    position: int = Field(default=0, ge=0, alias="Position", description="Position")
    start: int = Field(default=0, ge=0, alias="Start", description="Start position")
    end: int = Field(default=0, ge=0, alias="End", description="End position")
    length: int = Field(default=0, ge=0, alias="Length", description="Length")
    binary: Optional[bytes] = Field(None, alias="Binary", description="Binary data")
    content: Optional[str] = Field(None, alias="Content", description="Content")
    embeddings: List[float] = Field(
        default_factory=list, alias="Embeddings", description="Embeddings"
    )

    model_config = ConfigDict(
        use_enum_values=True, populate_by_name=True, validate_assignment=True
    )

    @field_validator("embeddings", mode="before")
    def validate_embeddings(cls, v: Optional[List[float]]) -> List[float]:
        """Ensure embeddings is never None."""
        return v or []

    def __init__(self, **data):
        """Initialize the semantic chunk and calculate hashes if content is provided."""
        super().__init__(**data)
        if self.content:
            import hashlib

            content_bytes = self.content.encode("utf-8")
            self.length = len(self.content)
            self.md5_hash = hashlib.md5(content_bytes).hexdigest().upper()
            self.sha1_hash = hashlib.sha1(content_bytes).hexdigest().upper()
            self.sha256_hash = hashlib.sha256(content_bytes).hexdigest().upper()
