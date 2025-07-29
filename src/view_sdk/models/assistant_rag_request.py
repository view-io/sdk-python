from pydantic import BaseModel, ConfigDict, Field, field_validator


class AssistantRagRequest(BaseModel):
    """View Assistant RAG request."""

    prompt_prefix: str = Field(
        default=(
            "You are a helpful AI assistant. "
            "Please use the information that follows as context to answer the user question listed below. "
            "Do not make up an answer. If you do not know, say you do not know. "
        ),
        alias="PromptPrefix",
        description="Prompt prefix",
    )

    question: str = Field(
        default="What information do you have?",
        alias="Question",
        description="Question to ask",
    )

    max_results: int = Field(
        default=10,
        alias="MaxResults",
        description="Maximum number of documents to retrieve",
        ge=1,
        le=100,
    )

    temperature: float = Field(
        default=0.1,
        alias="Temperature",
        description="Temperature, between 0 and 1",
        gt=0,
        le=1,
    )

    top_p: float = Field(
        default=0.95,
        alias="TopP",
        description="Top P, between 0 and 1",
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
        default="llama3.1:8b",
        alias="GenerationModel",
        description="Generation model and tag",
    )

    generation_provider: str = Field(
        default="ollama",
        alias="GenerationProvider",
        description="Generation provider (valid values: ollama)",
    )

    ollama_hostname: str = Field(
        default="ollama",
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

    vector_database_hostname: str = Field(
        default="pgvector",
        alias="VectorDatabaseHostname",
        description="Vector database hostname",
    )

    vector_database_port: int = Field(
        default=5432,
        alias="VectorDatabasePort",
        description="Vector database port",
        ge=0,
        le=65535,
    )

    vector_database_name: str = Field(
        default="vectordb",
        alias="VectorDatabaseName",
        description="Vector database name",
    )

    vector_database_user: str = Field(
        default="postgres",
        alias="VectorDatabaseUser",
        description="Vector database user",
    )

    vector_database_password: str = Field(
        default="password",
        alias="VectorDatabasePassword",
        description="Vector database password",
    )

    stream: bool = Field(
        default=True,
        alias="Stream",
        description="Enable streaming of responses",
    )

    context_sort: bool = Field(
        default=True,
        alias="ContextSort",
        description="Enable or disable contextual sorting",
    )

    context_scope: int = Field(
        default=2,
        alias="ContextScope",
        description="Context scope; number of neighboring data elements to retrieve",
        ge=1,
        le=16,
    )

    rerank: bool = Field(
        default=True,
        alias="Rerank",
        description="Enable or disable re-ranking of chunks or documents",
    )

    rerank_top_k: int = Field(
        default=10,
        alias="RerankTopK",
        description="Re-ranking of top chunks or documents",
        ge=1,
        le=16,
    )

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)

    @field_validator("generation_provider")
    def validate_generation_provider(cls, v: str) -> str:
        """Validate generation provider."""
        valid_providers = ["ollama"]
        if v not in valid_providers:
            raise ValueError(f"Generation provider '{v}' is not valid")
        return v
