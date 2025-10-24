import view_sdk
from view_sdk import crawler
from view_sdk.sdk_configuration import Service

sdk = view_sdk.configure(
    access_key="default",
    base_url="192.168.101.63",  # Replace with your actual server URL
    secure=False,
    tenant_guid="00000000-0000-0000-0000-000000000000",
    service_ports={Service.CRAWLER: 8000},
)


def stopCrawlOperation():
    crawlOperation = crawler.CrawlOperation.stop(
        "00000000-0000-0000-0000-000000000000", Name="My crawl operation"
    )
    print(crawlOperation)


# stopCrawlOperation()


def startCrawlOperation():
    crawlOperation = crawler.CrawlOperation.start(
        "00000000-0000-0000-0000-000000000000", Name="My crawl operation"
    )
    print(crawlOperation)


# startCrawlOperation()


def readAllCrawlOperations():
    crawlOperations = crawler.CrawlOperation.retrieve_all()
    print(crawlOperations)


# readAllCrawlOperations()


def enumerateCrawlOperation():
    enumeration = crawler.CrawlOperation.enumerateCrawlOperation(
        "00000000-0000-0000-0000-000000000000"
    )
    print(enumeration)


# enumerateCrawlOperation()


def readCrawlOperation():
    crawlOperation = crawler.CrawlOperation.retrieve(
        "00000000-0000-0000-0000-000000000000"
    )
    print(crawlOperation)


# readCrawlOperation()


def enumerateCrawlOperations():
    crawlOperations = crawler.CrawlOperation.enumerate()
    print(crawlOperations)


# enumerateCrawlOperations()


def deleteCrawlPlan():
    crawlPlan = crawler.CrawlPlan.delete("00000000-0000-0000-0000-000000000000")
    print(crawlPlan)


# deleteCrawlPlan()


def existsCrawlPlan():
    crawlPlan = crawler.CrawlPlan.exists("d417776c-f0bf-438b-8509-eb3b41b878ab")
    print(crawlPlan)


existsCrawlPlan()


def updateCrawlPlan():
    crawlPlan = crawler.CrawlPlan.update(
        "d417776c-f0bf-438b-8509-eb3b41b878ab",
        DataRepositoryGUID="00000000-0000-0000-0000-000000000000",
        CrawlScheduleGUID="00000000-0000-0000-0000-000000000000",
        CrawlFilterGUID="00000000-0000-0000-0000-000000000000",
        Name="My crawl plan [updated]",
        EnumerationDirectory="./enumerations/",
        EnumerationsToRetain=30,
        MetadataRuleGUID="00000000-0000-0000-0000-000000000000",
        ProcessingEndpoint="http://nginx-processor:8000/v1.0/tenants/00000000-0000-0000-0000-000000000000/processing",
        ProcessingAccessKey="default",
        CleanupEndpoint="http://nginx-processor:8000/v1.0/tenants/00000000-0000-0000-0000-000000000000/processing/cleanup",
        CleanupAccessKey="default",
    )
    print(crawlPlan)


updateCrawlPlan()


def readAllCrawlPlans():
    crawlPlans = crawler.CrawlPlan.retrieve_all()
    print(crawlPlans)


readAllCrawlPlans()


def enumerateCrawlPlans():
    crawlPlans = crawler.CrawlPlan.enumerate()
    print(crawlPlans)


enumerateCrawlPlans()


def readCrawlPlan():
    crawlPlan = crawler.CrawlPlan.retrieve("d417776c-f0bf-438b-8509-eb3b41b878ab")
    print(crawlPlan)


readCrawlPlan()


def createCrawlPlan():
    crawlPlan = crawler.CrawlPlan.create(
        DataRepositoryGUID="00000000-0000-0000-0000-000000000000",
        CrawlScheduleGUID="00000000-0000-0000-0000-000000000000",
        CrawlFilterGUID="00000000-0000-0000-0000-000000000000",
        Name="My crawl plan",
        EnumerationDirectory="./enumerations/",
        EnumerationsToRetain=30,
        MaxDrainTasks=10,
        ProcessAdditions=True,
        ProcessDeletions=True,
        ProcessUpdates=True,
        MetadataRuleGUID="00000000-0000-0000-0000-000000000000",
        ProcessingEndpoint="http://nginx-processor:8000/v1.0/tenants/00000000-0000-0000-0000-000000000000/processing",
        ProcessingAccessKey="default",
        CleanupEndpoint="http://nginx-processor:8000/v1.0/tenants/00000000-0000-0000-0000-000000000000/processing/cleanup",
        CleanupAccessKey="default",
    )
    print(crawlPlan)


createCrawlPlan()


def deleteCrawlFilter():
    crawlFilter = crawler.CrawlFilter.delete("00000000-0000-0000-0000-000000000000")
    print(crawlFilter)


# deleteCrawlFilter()


def existsCrawlFilter():
    crawlFilter = crawler.CrawlFilter.exists("00000000-0000-0000-0000-000000000000")
    print(crawlFilter)


# existsCrawlFilter()


def updateCrawlFilter():
    crawlFilter = crawler.CrawlFilter.update(
        "00000000-0000-0000-0000-000000000000",
        Name="My filter [updated]",
        MinimumSize=1,
        MaximumSize=134217728,
        IncludeSubdirectories=True,
        ContentType="*",
    )
    print(crawlFilter)


# updateCrawlFilter()


def enumerateCrawlFilters():
    crawlFilters = crawler.CrawlFilter.enumerate()
    print(crawlFilters)


# enumerateCrawlFilters()


def readCrawlFilter():
    crawlFilter = crawler.CrawlFilter.retrieve("00000000-0000-0000-0000-000000000000")
    print(crawlFilter)


# readCrawlFilter()


def createCrawlFilter():
    crawlFilter = crawler.CrawlFilter.create(
        Name="My filter",
        MinimumSize=1,
        MaximumSize=134217728,
        IncludeSubdirectories=True,
        ContentType="*",
    )
    print(crawlFilter)


# createCrawlFilter()


def existsCrawlSchedule():
    crawlSchedule = crawler.CrawlSchedule.exists("00000000-0000-0000-0000-000000000000")
    print(crawlSchedule)


# existsCrawlSchedule()


def deleteCrawlSchedule():
    crawlSchedule = crawler.CrawlSchedule.delete("00000000-0000-0000-0000-000000000000")
    print(crawlSchedule)


# deleteCrawlSchedule()


def updateCrawlSchedule():
    crawlSchedule = crawler.CrawlSchedule.update(
        "00000000-0000-0000-0000-000000000000",
        Name="My schedule [updated]",
        Schedule="DaysInterval",
        Interval=1,
    )
    print(crawlSchedule)


# updateCrawlSchedule()


def readAllCrawlSchedules():
    crawlSchedules = crawler.CrawlSchedule.retrieve_all()
    print(crawlSchedules)


# readAllCrawlSchedules()


def enumerateCrawlSchedules():
    crawlSchedules = crawler.CrawlSchedule.enumerate()
    print(crawlSchedules)


# enumerateCrawlSchedules()


def readCrawlSchedule():
    crawlSchedule = crawler.CrawlSchedule.retrieve(
        "00000000-0000-0000-0000-000000000000"
    )
    print(crawlSchedule)


# readCrawlSchedule()


def createCrawlSchedule():
    crawlSchedule = crawler.CrawlSchedule.create(
        Name="My schedule", Schedule="DaysInterval", Interval=1
    )
    print(crawlSchedule)


# createCrawlSchedule()


# existsDataRepository()


def deleteDataRepository():
    dataRepository = crawler.DataRepository.delete(
        "00000000-0000-0000-0000-000000000000"
    )
    print(dataRepository)


# deleteDataRepository()


def readAllDataRepositories():
    dataRepositories = crawler.DataRepository.retrieve_all()
    print(dataRepositories)


# readAllDataRepositories()


def enumerateDataRepositories():
    dataRepositories = crawler.DataRepository.enumerate()
    print(dataRepositories)


# enumerateDataRepositories()


def updateDataRepository():
    dataRepository = crawler.DataRepository.update(
        "186f92a5-dfb3-41be-be7e-8fbc2ce82911",
        Name="My NFS repository [updated]",
        RepositoryType="NFS",
        NfsVersion="V3",
        NfsHostname="192.168.86.248",
        NfsUserId=0,
        NfsGroupId=0,
        NfsShareName="/nfs",
        NfsIncludeSubdirectories=True,
    )
    print(dataRepository)


# updateDataRepository()


def readDataRepository():
    dataRepository = crawler.DataRepository.retrieve(
        "186f92a5-dfb3-41be-be7e-8fbc2ce82911"
    )
    print(dataRepository)


# readDataRepository()


def createDataRepository():
    dataRepository = crawler.DataRepository.create(
        Name="My NFS repository",
        RepositoryType="NFS",
        NfsVersion="V3",
        NfsHostname="192.168.86.248",
        NfsUserId=0,
        NfsGroupId=0,
        NfsShareName="/nfs",
        NfsIncludeSubdirectories=True,
    )
    print(dataRepository)


# createDataRepository()  # Commented out to avoid potential issues
