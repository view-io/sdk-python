from enum import Enum


class SchemaConditionEnum(str, Enum):
    Contains = "Contains"
    ContainsNot = "ContainsNot"
    EndsWith = "EndsWith"
    Equals = "Equals"
    GreaterThan = "GreaterThan"
    GreaterThanOrEqualTo = "GreaterThanOrEqualTo"
    IsNotNull = "IsNotNull"
    IsNull = "IsNull"
    LessThan = "LessThan"
    LessThanOrEqualTo = "LessThanOrEqualTo"
    NotEquals = "NotEquals"
    StartsWith = "StartsWith"
