from enum import Enum


class VectorRepositoryTypeEnum(str, Enum):
    Pgvector = "Pgvector"
    MysqlHeatwave = "MysqlHeatwave"
    Oracle23AI = "Oracle23AI"
