import uuid
from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, field_validator


class ModelConfigurationModel(BaseModel):
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID")
    model_name: str = Field(default="owner/modelname", alias="ModelName")

    embeddings: bool = Field(default=True, alias="Embeddings")
    completions: bool = Field(default=True, alias="Completions")

    context_size: int = Field(default=4096, alias="ContextSize")
    max_output_tokens: int = Field(default=4096, alias="MaxOutputTokens")
    temperature: float = Field(default=0.2, alias="Temperature")
    top_p: float = Field(default=1.0, alias="TopP")
    top_k: int = Field(default=40, alias="TopK")
    frequency_penalty: float = Field(default=0.0, alias="FrequencyPenalty")
    presence_penalty: float = Field(default=0.0, alias="PresencePenalty")

    enable_streaming: bool = Field(default=True, alias="EnableStreaming")
    timeout_ms: int = Field(default=30000, alias="TimeoutMs")

    additional_data: Optional[str] = Field(default=None, alias="AdditionalData")
    active: bool = Field(default=True, alias="Active")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(populate_by_name=True)

    # --- Validators to mimic C# rules ---

    @field_validator("context_size")
    def validate_context_size(cls, v: int) -> int:
        if v < 1:
            raise ValueError("ContextSize must be >= 1")
        return v

    @field_validator("max_output_tokens")
    def validate_max_output_tokens(cls, v: int) -> int:
        if v < 1 or v > 2_000_000:
            raise ValueError("MaxOutputTokens must be between 1 and 2,000,000")
        return v

    @field_validator("temperature")
    def validate_temperature(cls, v: float) -> float:
        if v < 0.0 or v > 2.0:
            raise ValueError("Temperature must be between 0.0 and 2.0")
        return v

    @field_validator("top_p")
    def validate_top_p(cls, v: float) -> float:
        if v < 0.0 or v > 1.0:
            raise ValueError("TopP must be between 0.0 and 1.0")
        return v

    @field_validator("top_k")
    def validate_top_k(cls, v: int) -> int:
        if v < 1 or v > 100:
            raise ValueError("TopK must be between 1 and 100")
        return v

    @field_validator("frequency_penalty", "presence_penalty")
    def validate_penalties(cls, v: float) -> float:
        if v < -2.0 or v > 2.0:
            raise ValueError("Penalty values must be between -2.0 and 2.0")
        return v

    @field_validator("timeout_ms")
    def validate_timeout(cls, v: int) -> int:
        if v <= 1000:
            raise ValueError("TimeoutMs must be greater than 1000")
        return v
