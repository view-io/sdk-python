import view_sdk
from view_sdk import director
from view_sdk.sdk_configuration import Service

sdk = view_sdk.configure(
    access_key="default",
    base_url="192.168.101.63",
    tenant_guid="00000000-0000-0000-0000-000000000000",
    service_ports={Service.DIRECTOR: 8000},
)


def generateEmbeddings():
    result = director.GenerateEmbeddings.create(
        EmbeddingsRule={
            "EmbeddingsGenerator": "LCProxy",
            "EmbeddingsGeneratorUrl": "http://nginx-lcproxy:8000/",
            "EmbeddingsGeneratorApiKey": "default",
            "BatchSize": 16,
            "MaxGeneratorTasks": 16,
            "MaxRetries": 3,
            "MaxFailures": 3,
        },
        Model="all-MiniLM-L6-v2",
        ApiKey="",
        Contents=[
            "This is a sample.",
        ],
    )
    print(result)


generateEmbeddings()


def listConnections():
    result = director.Connections.retrieve_all(
        "mXCNtMWDsW0/pr+IwRFUjclG5ap7t0RbHfpxzSvAUH+Siq3pFXcO/HLVkwrz/HhG4IuGfqY0K9PhM4lMshXyAPSxNrZjmxGBRctiKYpIf9fZ8SfiJA110z2E9M0ENGWGdSVMm7bYNpWq5Yy/VWBltQtzAYb2RUzZfLnvA8v0aX3leXEGDNCOAjf0CcdBrYQZz6Qiukir3y8N8LHgXXnkYDoCqy9I9c9SkH4OprGp+TXVp7wHz7g9MyD/3NhJRnWTnUmQk0TLrI4gcabuNgYkkTXHkHSwo8qHQzldUlWivO6jbHx6vY+c65EdwjPif3R7"
    )
    print(result)


listConnections()
