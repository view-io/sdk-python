from enum import Enum


class ModelApiTypeEnum(str, Enum):
    """Model API type."""
    Ollama = "Ollama"
    OpenAi = "OpenAi"
