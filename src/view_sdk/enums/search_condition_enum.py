from enum import Enum


class SearchCondition(str, Enum):
    Equals = "Equals"
    GreaterThan = "GreaterThan"
    GreaterThanOrEqualTo = "GreaterThanOrEqualTo"
    LessThan = "LessThan"
    LessThanOrEqualTo = "LessThanOrEqualTo"
    Contains = "Contains"
    ContainsNot = "ContainsNot"
    EndsWith = "EndsWith"
    IsNotNull = "IsNotNull"
    IsNull = "IsNull"
    NotEquals = "NotEquals"
    StartsWith = "StartsWith"
