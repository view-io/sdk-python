import view_sdk
from view_sdk import health_check

sdk = view_sdk.configure(
    access_key="default",
    base_url="view.homedns.org",
    tenant_guid="00000000-0000-0000-0000-000000000000",
)


def checkServer():
    result = health_check.SwitchBoard.check()
    print(result)


checkServer()


def checkEmbedding():
    result = health_check.HealthCheck.embeddings()
    print(result)


# checkEmbedding()


def checkLexi():
    result = health_check.HealthCheck.lexi()
    print(result)


# checkLexi()


def checkCrawler():
    result = health_check.HealthCheck.crawler()
    print(result)


# checkCrawler()


def checkDirector():
    result = health_check.HealthCheck.director()
    print(result)


# checkDirector()


def checkAssistant():
    result = health_check.HealthCheck.assistant()
    print(result)


# checkAssistant()


def checkProcessor():
    result = health_check.HealthCheck.processor()
    print(result)


# checkProcessor()


def checkVector():
    result = health_check.HealthCheck.vector()
    print(result)


# checkVector()


def checkStorage():
    result = health_check.HealthCheck.storage()
    print(result)


# checkStorage()


def checkConfiguration():
    result = health_check.HealthCheck.configuration()
    print(result)


# checkConfiguration()
