from enum import Enum


class DataTypeEnum(str, Enum):
    """Types of data supported."""

    Object = "Object"
    Array = "Array"
    Timestamp = "Timestamp"
    Integer = "Integer"
    Long = "Long"
    Decimal = "Decimal"
    Double = "Double"
    Float = "Float"
    String = "String"
    Boolean = "Boolean"
    Binary = "Binary"
    Null = "Null"
    Unknown = "Unknown"
