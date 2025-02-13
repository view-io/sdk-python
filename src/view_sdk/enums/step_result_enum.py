from enum import Enum


class StepResultEnum(str, Enum):
    """Result of a step execution."""

    Success = "Success"
    Failure = "Failure"
    Exception = "Exception"
