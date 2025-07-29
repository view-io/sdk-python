from pydantic import BaseModel, ConfigDict, Field, field_validator


class AssistantChatRequest(BaseModel):
    """View Assistant chat request."""

    question: str = Field(
        default="What information do you have?",
        alias="Question",
        description="Question to ask the assistant",
    )

    temperature: float = Field(
        default=0.1,
        alias="Temperature",
        description="Temperature, between 0 and 1",
        gt=0,
        le=1,
    )

    max_tokens: int = Field(
        default=2048,
        alias="MaxTokens",
        description="Maximum number of tokens to generate",
        ge=1,
        le=16384,
    )

    generation_model: str = Field(
        default="llama3.1:latest",
        alias="GenerationModel",
        description="Generation model and tag",
    )

    generation_provider: str = Field(
        default="ollama",
        alias="GenerationProvider",
        description="Generation provider (valid values: ollama)",
    )

    ollama_hostname: str = Field(
        default="localhost",
        alias="OllamaHostname",
        description="Ollama hostname",
    )

    ollama_port: int = Field(
        default=11434,
        alias="OllamaPort",
        description="Ollama TCP port",
        ge=0,
        le=65535,
    )

    stream: bool = Field(
        default=True,
        alias="Stream",
        description="Enable streaming of responses",
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)

    @field_validator("generation_provider")
    def validate_generation_provider(cls, v: str) -> str:
        """Validate generation provider."""
        valid_providers = ["ollama"]
        if v not in valid_providers:
            raise ValueError(f"Generation provider '{v}' is not valid")
        return v
