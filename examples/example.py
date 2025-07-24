"""Example script demonstrating the usage of view_sdk.

This script shows how to configure the SDK and process a document using the UdrGenerator.
"""

import view_sdk
from view_sdk import sdk_logging

# Set logging level to DEBUG for detailed output
sdk_logging.set_log_level(level="DEBUG")

# Configure the SDK with required parameters
view_sdk.configure(
    access_key="default",
    base_url="view.homedns.org",
    tenant_guid="default",
    verbose=False,
)


# export graph as gexf
view_sdk_graph = view_sdk.graphs.Graph.export_gexf(
    resource_guid="00000000-0000-0000-0000-000000000000"
)
print(view_sdk_graph)

# enumerate blobs
blobs = view_sdk.configuration.Blob.enumerate()
print(f"Result: {blobs}")

# retrieve source document
src_docs = view_sdk.lexi.SourceDocument.retrieve(
    resource_guid="b9a88ebb-2ec3-486c-8e34-bce615d2f325", collection_guid="default"
)

print(f"retrieved source document: {src_docs}")

# enumerate with query
vector_repo = view_sdk.vector.Repositories.enumerate_documents(
    repo_guid="example-vector-repository",
    max_results=5,
    include_data=False,
    continuation_token=None,
    tenant_guid=None,
    bucket_guid=None,
    collection_guid=None,
    vector_repository_guid="example-vector-repository",
    ordering="CreatedDescending",
)

#  Or you can also pass filters as a keyword argument with a dictionary
filters = {
    "MaxResults": 5,
    "IncludeData": False,
    "ContinuationToken": None,
    "TenantGUID": None,
    "BucketGUID": None,
    "CollectionGUID": None,
    "VectorRepositoryGUID": "example-vector-repository",
    "Ordering": "CreatedDescending",
}
vector_repo = view_sdk.vector.Repositories.enumerate_documents(
    repo_guid="example-vector-repository", **filters
)
print(f"Repository details: {vector_repo}")

vector_repo_stats = view_sdk.vector.Repositories.get_statistics(
    repo_guid="example-vector-repository"
)

print(f"Repository statistics: {vector_repo_stats}")
view_sdk.configuration.HealthCheck.check()
print(
    view_sdk.configuration.Authentication.retrieve_token_details(
        "mXCNtMWDsW0/pr+IwRFUjVImF1/y6Oam27XXByuVWzI2uFk4pePTGokx8A5IATp8DImwXaQcmiJPUFXiAbiXSxlRZmw8taRa/bUMf+dLZzmcZ7XLiRr3ZUNlkM3qe7zY9DTAnoVmwFX+OQ+ZiEsskWiPqs8iUq1I/wWNEDp8gXF1n7fjWSIZDn44CvnF8BPr96bL0UCPGavTA2RsNKQR5WRhggPvDKraAbWcvqkAlkHr5Nb3j3oHq6ZLzYKdYRt+oxcqGfW/kDtMcm5jfSH4mWObODoilqa+1lxB4VySsTkm96FPIsszvAe9fKSnrOPn"
    )
)
print(
    view_sdk.storage.BucketTags.create(
        "example-data-bucket", tags=[{"Key": "foo2", "Value": "bar2"}]
    )
)
print(view_sdk.storage.Object.retrieve("example-data-bucket", "34.pdf"))

print(
    view_sdk.storage.BucketACL.create(
        bucket_guid="example-data-bucket",
        **{
            "Owner": {
                "GUID": "default",
                "TenantGUID": "default",
                "FirstName": "Default",
                "LastName": "User",
                "FullName": "Default User",
                "Notes": "Default password is password",
                "Email": "default@user.com",
                "Active": True,
                "CreatedUtc": "2024-08-06T16:30:09.495213Z",
            },
            "Users": [
                {
                    "GUID": "default",
                    "TenantGUID": "default",
                    "FirstName": "Default",
                    "LastName": "User",
                    "FullName": "Default User",
                    "Notes": "Default password is password",
                    "Email": "default@user.com",
                    "Active": True,
                    "CreatedUtc": "2024-08-06T16:30:09.495213Z",
                }
            ],
            "Entries": [
                {
                    "GUID": "default",
                    "TenantGUID": "default",
                    "BucketGUID": "example-data-bucket",
                    "OwnerGUID": "default",
                    "UserGUID": "default",
                    "CanonicalUser": "",
                    "EnableRead": True,
                    "EnableReadAcp": True,
                    "EnableWrite": True,
                    "EnableWriteAcp": True,
                    "FullControl": True,
                    "CreatedUtc": "2024-08-06T16:30:09.643691Z",
                }
            ],
        },
    )
)
