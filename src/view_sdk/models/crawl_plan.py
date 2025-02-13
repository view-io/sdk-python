from pydantic import AnyUrl, BaseModel, ConfigDict, Field


class CrawlPlanModel(BaseModel):
    data_repository_guid: str = Field(..., alias="DataRepositoryGUID")
    crawl_schedule_guid: str = Field(..., alias="CrawlScheduleGUID")
    crawl_filter_guid: str = Field(..., alias="CrawlFilterGUID")
    name: str = Field(..., alias="Name")
    enumeration_directory: str = Field(..., alias="EnumerationDirectory")
    enumerations_to_retain: int = Field(..., alias="EnumerationsToRetain")
    metadata_rule_guid: str = Field(..., alias="MetadataRuleGUID")
    processing_endpoint: AnyUrl = Field(..., alias="ProcessingEndpoint")
    processing_access_key: str = Field(..., alias="ProcessingAccessKey")
    cleanup_endpoint: AnyUrl = Field(..., alias="CleanupEndpoint")
    cleanup_access_key: str = Field(..., alias="CleanupAccessKey")

    model_config = ConfigDict(populate_by_name=True)
