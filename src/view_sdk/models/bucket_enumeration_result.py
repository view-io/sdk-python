from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from .object_metadata import ObjectMetadataModel
from .object_statistics import ObjectStatistics
from .timestamp import TimestampModel


class BucketEnumerationResultModel(BaseModel):
    success: bool = Field(default=True, alias="Success")
    timestamp: TimestampModel = Field(default_factory=TimestampModel, alias="Timestamp")
    max_results: int = Field(default=1000, alias="MaxResults", ge=1)
    iterations_required: int = Field(default=0, alias="IterationsRequired", ge=0)
    statistics: Optional[ObjectStatistics] = Field(default=None, alias="Statistics")
    continuation_token: Optional[str] = Field(default=None, alias="ContinuationToken")
    shared_prefixes: Optional[List[str]] = Field(default=None, alias="SharedPrefixes")
    objects: Optional[List[ObjectMetadataModel]] = Field(default=None, alias="Objects")
    delete_markers: Optional[List[ObjectMetadataModel]] = Field(
        default=None, alias="DeleteMarkers"
    )
    end_of_results: bool = Field(default=True, alias="EndOfResults")
    total_records: int = Field(default=0, alias="TotalRecords", ge=0)
    records_remaining: int = Field(default=0, alias="RecordsRemaining", ge=0)

    model_config = ConfigDict(populate_by_name=True)
