import view_sdk
from view_sdk import processor
from view_sdk.models.semantic_cell_request import DocumentTypeEnum

sdk = view_sdk.configure( access_key="default",base_url="view.homedns.org", tenant_guid= "00000000-0000-0000-0000-000000000000")

def udrGeneration():
    result = processor.UdrGenerator.generate(
        GUID= "00000000-0000-0000-0000-000000000000",
        Key= "testfile.text",
        ContentType= "text/plain",
        Type= "Text",
        IncludeFlattened= True,
        CaseInsensitive= True,
        TopTerms= 10,
        AdditionalData= "The body below is simple sample text, base64 encoded, taken from https://en.wikipedia.org/wiki/Artificial_intelligence.",
        Metadata= {
            "foo": "bar"
        },
        MetadataRule= {
            "GUID": "00000000-0000-0000-0000-000000000000",
            "TenantGUID": "00000000-0000-0000-0000-000000000000",
            "BucketGUID": "00000000-0000-0000-0000-000000000000",
            "OwnerGUID": "00000000-0000-0000-0000-000000000000",
            "Name": "My metadata rule",
            "ContentType": "text/plain",
            "UdrEndpoint": "http://localhost:8000/",
            "DataCatalogType": "Lexi",
            "DataCatalogEndpoint": "http://localhost:8000/",
            "DataCatalogCollection": "00000000-0000-0000-0000-000000000000",
            "TopTerms": 10,
            "CaseInsensitive": True,
            "IncludeFlattened": True
        },
        Data= "QXJ0aWZpY2lhbCBpbnRlbGxpZ2VuY2UgKEFJKSwgaW4gaXRzIGJyb2FkZXN0IHNlbnNlLCBpcyBpbnRlbGxpZ2VuY2UgZXhoaWJpdGVkIGJ5IG1hY2hpbmVzLCBwYXJ0aWN1bGFybHkgY29tcHV0ZXIgc3lzdGVtcy4gSXQgaXMgYSBmaWVsZCBvZiByZXNlYXJjaCBpbiBjb21wdXRlciBzY2llbmNlIHRoYXQgZGV2ZWxvcHMgYW5kIHN0dWRpZXMgbWV0aG9kcyBhbmQgc29mdHdhcmUgdGhhdCBlbmFibGUgbWFjaGluZXMgdG8gcGVyY2VpdmUgdGhlaXIgZW52aXJvbm1lbnQgYW5kIHVzZSBsZWFybmluZyBhbmQgaW50ZWxsaWdlbmNlIHRvIHRha2UgYWN0aW9ucyB0aGF0IG1heGltaXplIHRoZWlyIGNoYW5jZXMgb2YgYWNoaWV2aW5nIGRlZmluZWQgZ29hbHMuWzFdIFN1Y2ggbWFjaGluZXMgbWF5IGJlIGNhbGxlZCBBSXMuCgpTb21lIGhpZ2gtcHJvZmlsZSBhcHBsaWNhdGlvbnMgb2YgQUkgaW5jbHVkZSBhZHZhbmNlZCB3ZWIgc2VhcmNoIGVuZ2luZXMgKGUuZy4sIEdvb2dsZSBTZWFyY2gpOyByZWNvbW1lbmRhdGlvbiBzeXN0ZW1zICh1c2VkIGJ5IFlvdVR1YmUsIEFtYXpvbiwgYW5kIE5ldGZsaXgpOyBpbnRlcmFjdGluZyB2aWEgaHVtYW4gc3BlZWNoIChlLmcuLCBHb29nbGUgQXNzaXN0YW50LCBTaXJpLCBhbmQgQWxleGEpOyBhdXRvbm9tb3VzIHZlaGljbGVzIChlLmcuLCBXYXltbyk7IGdlbmVyYXRpdmUgYW5kIGNyZWF0aXZlIHRvb2xzIChlLmcuLCBDaGF0R1BULCBBcHBsZSBJbnRlbGxpZ2VuY2UsIGFuZCBBSSBhcnQpOyBhbmQgc3VwZXJodW1hbiBwbGF5IGFuZCBhbmFseXNpcyBpbiBzdHJhdGVneSBnYW1lcyAoZS5nLiwgY2hlc3MgYW5kIEdvKS5bMl0gSG93ZXZlciwgbWFueSBBSSBhcHBsaWNhdGlvbnMgYXJlIG5vdCBwZXJjZWl2ZWQgYXMgQUk6ICJBIGxvdCBvZiBjdXR0aW5nIGVkZ2UgQUkgaGFzIGZpbHRlcmVkIGludG8gZ2VuZXJhbCBhcHBsaWNhdGlvbnMsIG9mdGVuIHdpdGhvdXQgYmVpbmcgY2FsbGVkIEFJIGJlY2F1c2Ugb25jZSBzb21ldGhpbmcgYmVjb21lcyB1c2VmdWwgZW5vdWdoIGFuZCBjb21tb24gZW5vdWdoIGl0J3Mgbm90IGxhYmVsZWQgQUkgYW55bW9yZS4iWzNdWzRd"
    )
    print(result)

# udrGeneration()

def semanticCelExtraction():
    result = processor.SemanticCell.extraction(
    DocumentType='pdf',
    Data="JVBERi0xLjcNCiW1tbW1DQoxIDAgb2JqDQo8PC9UeXBlL0NhdGFsb2cvUGFnZXMgMiAwIFIvTGFuZyhlbikgL1N0cnVjdFRyZWVSb290IDE4IDAgUi9NYXJrSW5mbzw8L01hcmtlZCB0cnVlPj4vTWV0YWRhdGEgODAgMCBSL1ZpZXdlclByZWZlcmVuY2VzIDgxIDAgUj4+DQplbmRvYmoNCjIgMCBvYmoNCjw8L1R5cGUvUGFnZXMvQ291bnQgMS9LaWRzWyAzIDAgUl0gPj4NCmVuZG9iag0KMyAwIG9iag0KPDwvVHlwZS9QYWdlL1BhcmVudCAyIDAgUi9SZXNvdXJjZXM8PC9Gb250PDwvRjEgNSAwIFIvRjIgMTIgMCBSL0YzIDE0IDAgUj",
    MetadataRule={
        "SemanticCellEndpoint": "http://viewdemo:8000/",
        "MinChunkContentLength": 1,
        "MaxChunkContentLength": 512,
        "ShiftSize": 512
    })
    print(result)

# semanticCelExtraction()

    

def cleanup():
    result = processor.Cleanup.cleanup_pipeline(Async=True,    Tenant= {
        "GUID": "00000000-0000-0000-0000-000000000000",
        "Name": "Default Tenant",
        "Region": "us-west-1",
        "S3BaseDomain": "localhost",
        "DefaultPoolGUID": "00000000-0000-0000-0000-000000000000",
        "Active": True
    },
    Collection= {
        "GUID": "00000000-0000-0000-0000-000000000000",
        "TenantGUID": "00000000-0000-0000-0000-000000000000",
        "Name": "My first collection",
        "AllowOverwrites": True,
        "AdditionalData": "Created by setup"
    },
    DataRepository= {
        "GUID": "00000000-0000-0000-0000-000000000000",
        "TenantGUID": "00000000-0000-0000-0000-000000000000",
        "OwnerGUID": "00000000-0000-0000-0000-000000000000",
        "Name": "My disk data repository",
        "RepositoryType": "File",
        "DiskDirectory": "./disk/"
    },
    Object= {
        "GUID": "00000000-0000-0000-0000-000000000001",
        "ParentGUID": None,
        "TenantGUID": "00000000-0000-0000-0000-000000000000",
        "TenantName": "My default tenant",
        "NodeGUID": None,
        "PoolGUID": "00000000-0000-0000-0000-000000000000",
        "BucketGUID": "00000000-0000-0000-0000-000000000000",
        "BucketName": "data",
        "OwnerGUID": "00000000-0000-0000-0000-000000000000",
        "Key": "hello2.txt",
        "Version": "1",
        "ContentType": "text/plain",
        "DocumentType": "Text",
        "ContentLength": 13,
        "Data": "VGhpcyBpcyBhIHNhbXBsZSBkb2N1bWVudCB3aXRoIGp1c3QgYSBoYW5kZnVsIG9mIHdvcmRzIHRoYXQgd2lsbCBiZSBwcm9jZXNzZWQgYnkgVmlldw=="
    },
    MetadataRule= {
        "GUID": "00000000-0000-0000-0000-000000000000",
        "TenantGUID": "00000000-0000-0000-0000-000000000000",
        "BucketGUID": "00000000-0000-0000-0000-000000000000",
        "OwnerGUID": "00000000-0000-0000-0000-000000000000",
        "Name": "example-metadata-rule",
        "ContentType": "*",
        "MaxContentLength": 16777216,
        "DataFlowEndpoint": "http://localhost:8501/processor",
        "TypeDetectorEndpoint": "http://localhost:8501/processor/typedetector",
        "SemanticCellEndpoint": "http://localhost:8341/",
        "MaxChunkContentLength": 512,
        "ShiftSize": 448,
        "UdrEndpoint": "http://localhost:8321/",
        "TopTerms": 25,
        "CaseInsensitive": True,
        "IncludeFlattened": True,
        "DataCatalogEndpoint": "http://localhost:8201/",
        "DataCatalogType": "Lexi",
        "DataCatalogCollection": "00000000-0000-0000-0000-000000000000",
        "GraphRepositoryGUID": "00000000-0000-0000-0000-000000000000"
    },
    EmbeddingsRule= {
        "GUID": "00000000-0000-0000-0000-000000000000",
        "TenantGUID": "00000000-0000-0000-0000-000000000000",
        "BucketGUID": "00000000-0000-0000-0000-000000000000",
        "OwnerGUID": "00000000-0000-0000-0000-000000000000",
        "Name": "My storage server embeddings rule",
        "ContentType": "*",
        "GraphRepositoryGUID": "00000000-0000-0000-0000-000000000000",
        "VectorRepositoryGUID": "00000000-0000-0000-0000-000000000000",
        "DataFlowEndpoint": "http://localhost:8501/processor",
        "EmbeddingsGenerator": "LCProxy",
        "GeneratorUrl": "http://localhost:8301/",
        "GeneratorApiKey": "",
        "VectorStoreUrl": "http://localhost:8311/",
        "MaxContentLength": 16777216
    },
    VectorRepository= {
        "GUID": "00000000-0000-0000-0000-000000000000",
        "TenantGUID": "00000000-0000-0000-0000-000000000000",
        "Name": "My vector repository",
        "RepositoryType": "Pgvector",
        "Model": "all-MiniLM-L6-v2",
        "Dimensionality": 384,
        "DatabaseHostname": "localhost",
        "DatabaseName": "vectordb",
        "DatabaseTable": "minilm",
        "DatabasePort": 5432,
        "DatabaseUser": "postgres",
        "DatabasePassword": "password"
    },
    GraphRepository= {
        "GUID": "00000000-0000-0000-0000-000000000000",
        "TenantGUID": "00000000-0000-0000-0000-000000000000",
        "Name": "My LiteGraph instance",
        "RepositoryType": "LiteGraph",
        "EndpointUrl": "http://localhost:8701/",
        "ApiKey": "default",
        "GraphIdentifier": "00000000-0000-0000-0000-000000000000"
    })
    print(result)

# cleanup()

def processingPipeline():
    result = processor.Processor.processing_pipeline( Async= True,
    Tenant= {
        "GUID": "00000000-0000-0000-0000-000000000000",
        "Name": "Default Tenant",
        "Region": "us-west-1",
        "S3BaseDomain": "localhost",
        "DefaultPoolGUID": "00000000-0000-0000-0000-000000000000",
        "Active": True
    },
    Collection={
        "GUID": "00000000-0000-0000-0000-000000000000",
        "TenantGUID": "00000000-0000-0000-0000-000000000000",
        "Name": "My first collection",
        "AllowOverwrites": True,
        "AdditionalData": "Created by setup"
    },
    Bucket={
        "GUID": "00000000-0000-0000-0000-000000000000",
        "TenantGUID": "00000000-0000-0000-0000-000000000000",
        "PoolGUID": "00000000-0000-0000-0000-000000000000",
        "OwnerGUID": "00000000-0000-0000-0000-000000000000",
        "Category": "Data",
        "Name": "example-data-bucket",
        "RegionString": "us-west-1",
        "Versioning": True,
        "MaxMultipartUploadSeconds": 604800
    },
    Pool={
        "GUID": "00000000-0000-0000-0000-000000000000",
        "TenantGUID": "00000000-0000-0000-0000-000000000000",
        "Name": "default",
        "Provider": "Disk",
        "WriteMode": "GUID",
        "UseSsl": False,
        "DiskDirectory": "./disk/",
        "Compress": "None",
        "EnableReadCaching": False
    },
    Object= {
        "GUID": "00000000-0000-0000-0000-000000000000",
        "ParentGUID": None,
        "TenantGUID": "00000000-0000-0000-0000-000000000000",
        "TenantName": "My default tenant",
        "PoolGUID": "00000000-0000-0000-0000-000000000000",
        "BucketGUID": "00000000-0000-0000-0000-000000000000",
        "BucketName": "data",
        "OwnerGUID": "00000000-0000-0000-0000-000000000000",
        "Key": "hello1.txt",
        "Version": "1",
        "ContentType": "text/plain",
        "DocumentType": "Text",
        "ContentLength": 13
    },
    MetadataRule= {
        "GUID": "00000000-0000-0000-0000-000000000000",
        "TenantGUID": "00000000-0000-0000-0000-000000000000",
        "BucketGUID": "00000000-0000-0000-0000-000000000000",
        "OwnerGUID": "00000000-0000-0000-0000-000000000000",
        "Name": "example-metadata-rule",
        "ContentType": "*",
        "MaxContentLength": 16777216,
        "DataFlowEndpoint": "http://localhost:8501/processor",
        "TypeDetectorEndpoint": "http://localhost:8501/processor/typedetector",
        "SemanticCellEndpoint": "http://localhost:8341/",
        "MaxChunkContentLength": 512,
        "ShiftSize": 448,
        "UdrEndpoint": "http://localhost:8321/",
        "TopTerms": 25,
        "CaseInsensitive": True,
        "IncludeFlattened": True,
        "DataCatalogEndpoint": "http://localhost:8201/",
        "DataCatalogType": "Lexi",
        "DataCatalogCollection": "default",
        "GraphRepositoryGUID": "00000000-0000-0000-0000-000000000000",
        "TargetBucketGUID": "00000000-0000-0000-0000-000000000000"
    },
    EmbeddingsRule= {
        "GUID": "00000000-0000-0000-0000-000000000000",
        "TenantGUID": "00000000-0000-0000-0000-000000000000",
        "BucketGUID": "00000000-0000-0000-0000-000000000000",
        "OwnerGUID": "00000000-0000-0000-0000-000000000000",
        "Name": "My storage server embeddings rule",
        "ContentType": "*",
        "GraphRepositoryGUID": "00000000-0000-0000-0000-000000000000",
        "VectorRepositoryGUID": "00000000-0000-0000-0000-000000000000",
        "DataFlowEndpoint": "http://localhost:8501/processor",
        "EmbeddingsGenerator": "LCProxy",
        "GeneratorUrl": "http://localhost:8301/",
        "GeneratorApiKey": "",
        "VectorStoreUrl": "http://localhost:8311/",
        "MaxContentLength": 16777216
    },
    VectorRepository= {
        "GUID": "00000000-0000-0000-0000-000000000000",
        "Name": "My vector repository",
        "RepositoryType": "Pgvector",
        "Model": "all-MiniLM-L6-v2",
        "Dimensionality": 384,
        "DatabaseHostname": "localhost",
        "DatabaseName": "vectordb",
        "DatabaseTable": "minilm",
        "DatabasePort": 5432,
        "DatabaseUser": "postgres",
        "DatabasePassword": "password"
    },
    GraphRepository= {
        "GUID": "00000000-0000-0000-0000-000000000000",
        "TenantGUID": "00000000-0000-0000-0000-000000000000",
        "Name": "My LiteGraph instance",
        "RepositoryType": "LiteGraph",
        "EndpointUrl": "http://localhost:8701/",
        "ApiKey": "default",
        "GraphIdentifier": "00000000-0000-0000-0000-000000000000"
    })
    print(result)

# processingPipeline()

def typeDetection():
    result = processor.TypeDetector.type_detection(menu= {
        "id": "file",
        "value": "File",
        "popup": {
            "menuitem": [
            {"value": "New", "onclick": "CreateNewDoc()"},
            {"value": "Open", "onclick": "OpenDoc()"},
            {"value": "Close", "onclick": "CloseDoc()"}
            ]
        }
        })
    print(result)

# typeDetection()
    