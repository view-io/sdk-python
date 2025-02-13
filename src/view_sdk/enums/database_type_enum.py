from enum import Enum


class DatabaseTypeEnum(str, Enum):
    """Valid database types."""

    MYSQL = "Mysql"
    POSTGRESQL = "Postgresql"
    SQLSERVER = "SqlServer"
    SQLITE = "Sqlite"
