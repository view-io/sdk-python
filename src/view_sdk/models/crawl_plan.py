import uuid
from datetime import datetime, timezone
from pydantic import BaseModel, ConfigDict, Field


class CrawlPlanModel(BaseModel):
    guid: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="GUID")
    tenant_guid: str = Field(
        default_factory=lambda: str(uuid.uuid4()), alias="TenantGUID"
    )
    id: int = Field(default=0, exclude=True, alias="Id")
    data_repository_guid: str = Field(..., alias="DataRepositoryGUID")
    crawl_schedule_guid: str = Field(..., alias="CrawlScheduleGUID")
    metadata_rule_guid: str = Field(..., alias="MetadataRuleGUID")
    embeddings_rule_guid: str = Field(..., alias="EmbeddingsRuleGUID")
    crawl_filter_guid: str = Field(..., alias="CrawlFilterGUID")
    name: str = Field(..., alias="Name")
    enumeration_directory: str = Field(..., alias="EnumerationDirectory")
    enumerations_to_retain: int = Field(..., alias="EnumerationsToRetain")
    max_drain_tasks: int = Field(..., alias="MaxDrainTasks")
    process_additions: bool = Field(..., alias="ProcessAdditions")
    process_deletions: bool = Field(..., alias="ProcessDeletions")
    process_updates: bool = Field(..., alias="ProcessUpdates")
    created_utc: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), alias="CreatedUtc"
    )

    model_config = ConfigDict(populate_by_name=True)
