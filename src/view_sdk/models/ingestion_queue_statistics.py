from pydantic import BaseModel, ConfigDict, Field, field_validator


class IngestQueueStatisticsModel(BaseModel):
    """Ingest queue statistics."""

    document_count: int = Field(default=0, alias="DocumentCount", ge=0)
    total_bytes: int = Field(default=0, alias="TotalBytes", ge=0)

    model_config = ConfigDict(populate_by_name=True)

    @field_validator("document_count")
    def validate_document_count(cls, v):
        if v < 0:
            raise ValueError("DocumentCount must be greater than or equal to 0")
        return v

    @field_validator("total_bytes")
    def validate_total_bytes(cls, v):
        if v < 0:
            raise ValueError("TotalBytes must be greater than or equal to 0")
        return v
