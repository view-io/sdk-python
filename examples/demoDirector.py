import view_sdk
from view_sdk import director

sdk = view_sdk.configure(
    access_key="default",
    base_url="view.homedns.org",
    tenant_guid="00000000-0000-0000-0000-000000000000",
)


def generateEmbeddings():
    result = director.GenerateEmbeddings.create(
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
        "mXCNtMWDsW0/pr+IwRFUjeDO2cbVr5o4WlPplku8dbpYzqXbeV0c5ofMbX/YiOhMzPSr1DRg/PyE25KpaGzto0+uchyYY2jGJvlj7I/nSFmqlMEsXYy73LsvYjG4tSlimGN60Hj51mmvdaieE8BOVStYfehip+tEXiELfP7tXX6N6EIFAyCQZRWtRoKkXK+DZoY265roa6TwGehPTz4n4vrKb3XwrWzAWOl/pb6G+t3+P/oa52JqKojKT1wB+sLJ8sjzJpalYuQzLEOcK5Nwyw=="
    )
    print(result)


# listConnections()
