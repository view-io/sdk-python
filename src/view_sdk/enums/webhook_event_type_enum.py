from enum import Enum


class WebhookEventTypeEnum(str, Enum):
    Unknown = "Unknown"
    ObjectWrite = "ObjectWrite"
    UdrDocumentGenerated = "UdrDocumentGenerated"
    EmbeddingsGenerated = "EmbeddingsGenerated"
