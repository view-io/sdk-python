from enum import Enum


class StepRuntimeEnum(str, Enum):
    """Runtime for the step."""

    Dotnet8 = "Dotnet8"
    Python3_12 = "Python3_12"
