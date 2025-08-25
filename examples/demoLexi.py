import view_sdk
from view_sdk import lexi

sdk = view_sdk.configure(
    access_key="default",
    base_url="YOUR_SERVER_URL_HERE",  # Replace with your actual server URL
    secure=False,  # Use HTTP (server doesn't support HTTPS)
    tenant_guid="00000000-0000-0000-0000-000000000000",
)


def deleteIngestQueue():
    response = lexi.IngestQueue.delete("00000000-0000-0000-0000-000000000000")
    print(response)


# deleteIngestQueue()


def existsIngestQueue():
    exists = lexi.IngestQueue.exists("d6fb173a-5b62-4b6d-a8bb-f3024e697520")
    print(exists)


# existsIngestQueue()


def readIngestQueue():
    queue = lexi.IngestQueue.retrieve_statistics()
    print(queue)


#readIngestQueue()


def readAllIngestQueue():
    queues = lexi.IngestQueue.retrieve_all()
    print(queues)


#readAllIngestQueue()


def uploadSourceDocument():
    document = lexi.SourceDocument.create(
        "00000000-0000-0000-0000-000000000000",
        TenantGUID="00000000-0000-0000-0000-000000000000",
        CollectionGUID="00000000-0000-0000-0000-000000000000",
        ObjectKey="blake.json",
        ObjectVersion="1",
        ObjectGUID="00000000-0000-0000-0000-000000000000",
        ContentType="application/json",
        DocumentType="JSON",
        SourceUrl="http://localhost:9000/tenants/default/buckets/data/objects/sample.json",
        UdrDocument={},
    )
    print(document)


# uploadSourceDocument()


def readSourceDocumentStatistics():
    statistics = lexi.SourceDocument.retrieve_statistics(
        "41669cec-1e80-4206-b123-c76867c6734f", "00000000-0000-0000-0000-000000000000"
    )
    print(statistics)


#readSourceDocumentStatistics()


def readTopTerms():
    terms = lexi.SourceDocument.retrieve_top_terms(
        "00000000-0000-0000-0000-000000000000", "41669cec-1e80-4206-b123-c76867c6734f"
    )
    print(terms)


#readTopTerms()


def readSourceDocument():
    document = lexi.SourceDocument.retrieve(
        "00000000-0000-0000-0000-000000000000",
        "00000000-0000-0000-0000-000000000000",
        True,
    )
    print(document)


#readSourceDocument()


def readAllSourceDocuments():
    documents = lexi.SourceDocument.retrieve_all("00000000-0000-0000-0000-000000000000")
    print(documents)


readAllSourceDocuments()


def deleteCollection():
    response = lexi.Collection.delete("79bedb07-6408-4841-987c-3bb4b0e6ffd8")
    print(response)


# deleteCollection()


def searchCollection():
    search = lexi.Collection.search(
        "79bedb07-6408-4841-987c-3bb4b0e6ffd8",
        emit_results=True,
        MaxResults=2,
        Skip=1,
        ContinuationToken="",
        Ordering="CreatedDescending",
        Filter={
            "CreatedAfter": "2024-01-01 00:00:00.000000",
            "CreatedBefore": "2025-01-01 00:00:00.000000",
            "Terms": ["foo"],
            "MimeTypes": [],
            "Prefixes": [],
            "Suffixes": [],
            "SchemaFilters": [],
        },
    )
    print(search)


# searchCollection()


def existsCollection():
    exists = lexi.Collection.exists("79bedb07-6408-4841-987c-3bb4b0e6ffd8")
    print(exists)


# existsCollection()


def readCollectionStatistics():
    statistics = lexi.Collection.retrieve_statistics(
        "79bedb07-6408-4841-987c-3bb4b0e6ffd8"
    )
    print(statistics)


# readCollectionStatistics()


# readTopTerms()


def enumerateCollectionDocuments():
    documents = lexi.Collection.enumerate_documents(
        "79bedb07-6408-4841-987c-3bb4b0e6ffd8",
        {
            "MaxResults": 100,
            "Skip": 0,
            "ContinuationToken": None,
            "Ordering": "CreatedDescending",
            "Filters": [{"Field": "ObjectKey", "Condition": "IsNotNull", "Value": ""}],
        },
    )
    print(documents)


# enumerateCollectionDocuments()


def readAllCollections():
    collections = lexi.Collection.retrieve_all()
    print(collections)


# readAllCollections()


def readCollection():
    collection = lexi.Collection.retrieve("966a6a81-b8f3-49c5-8401-ade062926c40")
    print(collection)


# readCollection()


def createCollection():
    collection = lexi.Collection.create(
        Name="My second collection", AdditionalData="Yet another collection"
    )
    print(collection)


# createCollection()
