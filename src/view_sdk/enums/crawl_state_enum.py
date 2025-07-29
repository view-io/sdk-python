from enum import Enum


class CrawlStateEnum(str, Enum):
    NotStarted = "NotStarted"
    Starting = "Starting"
    Stopped = "Stopped"
    Canceled = "Canceled"
    Enumerating = "Enumerating"
    Retrieving = "Retrieving"
    Deleting = "Deleting"
    Success = "Success"
    Failed = "Failed"
