from enum import Enum


class EmbeddingsGeneratorEnum(str, Enum):
    OpenAI = "OpenAI"
    LCProxy = "LCProxy"
    Ollama = "Ollama"
    VoyageAI = "VoyageAI"
