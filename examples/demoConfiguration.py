import view_sdk
from view_sdk import configuration

sdk = view_sdk.configure(
    access_key="default",
    base_url="YOUR_SERVER_URL_HERE",
    tenant_guid="00000000-0000-0000-0000-000000000000",
)


def deleteObjectLock():
    objectLock = configuration.ObjectLock.delete("00000000-0000-0000-0000-000000000000")
    print(objectLock)


# deleteObjectLock()


def readObjectLock():
    objectLock = configuration.ObjectLock.retrieve(
        "00000000-0000-0000-0000-000000000000"
    )
    print(objectLock)


# readObjectLock()


def readAllObjectLocks():
    objectLocks = configuration.ObjectLock.retrieve_all()
    print(objectLocks)


#readAllObjectLocks()


def enumerateObjectLocks():
    objectLocks = configuration.ObjectLock.enumerate()
    print(objectLocks)


#enumerateObjectLocks()


def deleteWebhookRule():
    webhookRule = configuration.WebhookRule.delete(
        "0664fc21-9ece-4be2-9ee4-6ddb8624621d"
    )
    print(webhookRule)


#deleteWebhookRule()


def existsWebhookRule():
    webhookRule = configuration.WebhookRule.exists(
        "0664fc21-9ece-4be2-9ee4-6ddb8624621d"
    )
    print(webhookRule)


#existsWebhookRule()


def updateWebhookRule():
    webhookRule = configuration.WebhookRule.update(
        "0664fc21-9ece-4be2-9ee4-6ddb8624621d",
        Name="My webhook rule [updated]",
        TargetGUID="00000000-0000-0000-0000-000000000000",
        EventType="ObjectWrite",
        MaxAttempts=5,
    )
    print(webhookRule)


#updateWebhookRule()


def readAllWebhookRules():
    webhookRules = configuration.WebhookRule.retrieve_all()
    print(webhookRules)


# readAllWebhookRules()


def enumerateWebhookRules():
    webhookRules = configuration.WebhookRule.enumerate()
    print(webhookRules)


# enumerateWebhookRules()


def readWebhookRule():
    webhookRule = configuration.WebhookRule.retrieve(
        "0664fc21-9ece-4be2-9ee4-6ddb8624621d"
    )
    print(webhookRule)


# readWebhookRule()


def createWebhookRule():
    webhookRule = configuration.WebhookRule.create(
        Name="My webhook rule",
        TargetGUID="00000000-0000-0000-0000-000000000000",
        EventType="ObjectWrite",
        MaxAttempts=5,
        RetryIntervalMs=10000,
        TimeoutMs=30000,
    )
    print(webhookRule)


# createWebhookRule()


# readAllWebhookRules()


def deleteWebhookTarget():
    webhookTarget = configuration.WebhookTarget.delete(
        "e6509b81-dc3c-44e3-ab16-16e907fb03ef"
    )
    print(webhookTarget)


# deleteWebhookTarget()


def existsWebhookTarget():
    webhookTarget = configuration.WebhookTarget.exists(
        "e6509b81-dc3c-44e3-ab16-16e907fb03ef"
    )
    print(webhookTarget)


# existsWebhookTarget()


def updateWebhookTarget():
    webhookTarget = configuration.WebhookTarget.update(
        "e6509b81-dc3c-44e3-ab16-16e907fb03ef",
        Name="My webhook target [updated]",
        Url="http://localhost:8311",
        ContentType="application/json",
        ExpectStatus=200,
    )
    print(webhookTarget)


# updateWebhookTarget()


def enumerateWebhookTargets():
    webhookTargets = configuration.WebhookTarget.enumerate()
    print(webhookTargets)


# enumerateWebhookTargets()


def readAllWebhookTargets():
    webhookTargets = configuration.WebhookTarget.retrieve_all()
    print(webhookTargets)


# readAllWebhookTargets()


def readWebhookTarget():
    webhookTarget = configuration.WebhookTarget.retrieve(
        "e6509b81-dc3c-44e3-ab16-16e907fb03ef"
    )
    print(webhookTarget)


# readWebhookTarget()


def createWebhookTarget():
    webhookTarget = configuration.WebhookTarget.create(
        Name="My webhook target",
        Url="http://localhost:8311",
        ContentType="application/json",
        ExpectStatus=200,
    )
    print(webhookTarget)


# createWebhookTarget()


def existsWebhookEvent():
    webhookEvent = configuration.WebhookEvent.exists(
        "00000000-0000-0000-0000-000000000000"
    )
    print(webhookEvent)


# existsWebhookEvent()


def readAllWebhookEvents():
    webhookEvents = configuration.WebhookEvent.retrieve_all()
    print(webhookEvents)


# readAllWebhookEvents()


def readWebhookEvent():
    webhookEvent = configuration.WebhookEvent.retrieve(
        "00000000-0000-0000-0000-000000000000"
    )
    print(webhookEvent)


# readWebhookEvent()


def enumerateWebhookEvents():
    webhookEvents = configuration.WebhookEvent.enumerate()
    print(webhookEvents)


# enumerateWebhookEvents()


def existsBlob():
    blob = configuration.Blob.exists("b1a953d8-2a51-496a-a272-52ebe326fd2d")
    print(blob)


# existsBlob()


def deleteBlob():
    blob = configuration.Blob.delete("b1a953d8-2a51-496a-a272-52ebe326fd2d")
    print(blob)


# deleteBlob()


def updateBlob():
    blob = configuration.Blob.update(
        "b1a953d8-2a51-496a-a272-52ebe326fd2d",
        ContentType="text/plain",
        Name="helloworld_updated.txt",
        Description="A text file containing 'Hello, world!'",
        RefObjType="[usermanaged]",
        RefObjGUID="[usermanaged]",
        Data="SGVsbG8sIHdvcmxkIQ==",
    )
    print(blob)


# updateBlob()


def readAllBlobs():
    blobs = configuration.Blob.retrieve_all()
    print(blobs)


# readAllBlobs()


def enumerateBlobs():
    blobs = configuration.Blob.enumerate()
    print(blobs)


# enumerateBlobs()


def readBlob():
    blob = configuration.Blob.retrieve("b1a953d8-2a51-496a-a272-52ebe326fd2d", True)
    print(blob)


# readBlob()


# readBlob()


def createBlob():
    blob = configuration.Blob.create(
        ContentType="text/plain",
        Name="helloworld.txt",
        Description="A text file containing 'Hello, world!'",
        RefObjType="[usermanaged]",
        RefObjGUID="[usermanaged]",
        Data="SGVsbG8sIHdvcmxkIQ==",
    )
    print(blob)


createBlob()


def deleteEncryptionKey():
    encryptionKey = configuration.EncryptionKey.delete(
        "ee70aa3b-b00f-4459-95e1-4683a4404b08"
    )
    print(encryptionKey)


# deleteEncryptionKey()


def existsEncryptionKey():
    encryptionKey = configuration.EncryptionKey.exists(
        "ee70aa3b-b00f-4459-95e1-4683a4404b08"
    )
    print(encryptionKey)


# existsEncryptionKey()


def updateEncryptionKey():
    encryptionKey = configuration.EncryptionKey.update(
        "ee70aa3b-b00f-4459-95e1-4683a4404b08",
        KeyBase64="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=",
        KeyHex="0000000000000000000000000000000000000000000000000000000000000000",
        IvBase64="AAAAAAAAAAAAAAAAAAAAAA==",
        IvHex="00000000000000000000000000000000",
        SaltBase64="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=",
        SaltHex="0000000000000000000000000000000000000000000000000000000000000000",
        Name="Another default key",
        Description="Another default key [updated]",
    )
    print(encryptionKey)


# updateEncryptionKey()


def enumerateEncryptionKeys():
    encryptionKeys = configuration.EncryptionKey.enumerate()
    print(encryptionKeys)


# enumerateEncryptionKeys()


def readAllEncryptionKeys():
    encryptionKeys = configuration.EncryptionKey.retrieve_all()
    print(encryptionKeys)

#readAllEncryptionKeys()


def readEncryptionKey():
    encryptionKey = configuration.EncryptionKey.retrieve(
        "597591cf-009c-4b9f-b0f6-d265f6d34f79"
    )
    print(encryptionKey)


# readEncryptionKey()


def createEncryptionKey():
    encryptionKey = configuration.EncryptionKey.create(
        KeyBase64="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=",
        KeyHex="0000000000000000000000000000000000000000000000000000000000000000",
        IvBase64="AAAAAAAAAAAAAAAAAAAAAA==",
        IvHex="00000000000000000000000000000000",
        SaltBase64="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=",
        SaltHex="0000000000000000000000000000000000000000000000000000000000000000",
        Name="Another default key",
        Description="Another default key",
    )
    print(encryptionKey)


#createEncryptionKey()


def existsGraphRepository():
    graphRepository = configuration.GraphRepository.exists(
        "626c44ef-cdc5-450f-8760-e6b863624cd8"
    )
    print(graphRepository)


# existsGraphRepository()


def updateGraphRepository():
    graphRepository = configuration.GraphRepository.update(
        "626c44ef-cdc5-450f-8760-e6b863624cd8",
        Name="My LiteGraph instance [updated]",
        RepositoryType="LiteGraph",
        EndpointUrl="http://localhost:8701/",
        ApiKey="default",
        GraphIdentifier="00000000-0000-0000-0000-000000000000",
    )
    print(graphRepository)


# updateGraphRepository()


# existsGraphRepository()


def readGraphRepository():
    graphRepository = configuration.GraphRepository.retrieve(
        "00000000-0000-0000-0000-000000000000"
    )
    print(graphRepository)


#readGraphRepository()


def createGraphRepository():
    graphRepository = configuration.GraphRepository.create(
        Name="My LiteGraph instance",
        RepositoryType="LiteGraph",
        EndpointUrl="http://localhost:8701/",
        ApiKey="default",
        GraphIdentifier="00000000-0000-0000-0000-000000000000",
    )
    print(graphRepository)


# createGraphRepository()


def deleteGraphRepository():
    graphRepository = configuration.GraphRepository.delete(
        "2fd4c223-34f9-4150-a5fb-ce1ccbe36762"
    )
    print(graphRepository)


# deleteGraphRepository()


def readAllGraphRepositories():
    graphRepositories = configuration.GraphRepository.retrieve_all()
    print(graphRepositories)


# readAllGraphRepositories()


def enumerateGraphRepositories():
    graphRepositories = configuration.GraphRepository.enumerate()
    print(graphRepositories)


enumerateGraphRepositories()


# deleteVectorRepository()


def updateVectorRepository():
    vectorRepository = configuration.VectorRepository.update(
        "2fd4c223-34f9-4150-a5fb-ce1ccbe36762",
        Name="My vector repository [updated]",
        RepositoryType="Pgvector",
        Model="all-MiniLM-L6-v2",
        Dimensionality=384,
        DatabaseHostname="localhost",
        DatabaseName="vectordb",
        SchemaName="public",
        DatabaseTable="minilm",
        DatabasePort=5432,
        DatabaseUser="postgres",
        DatabasePassword="password",
    )
    print(vectorRepository)


# updateVectorRepository()


def existsVectorRepository():
    vectorRepository = configuration.VectorRepository.exists(
        "2fd4c223-34f9-4150-a5fb-ce1ccbe36762"
    )
    print(vectorRepository)


# existsVectorRepository()


def readAllVectorRepositories():
    vectorRepositories = configuration.VectorRepository.retrieve_all()
    print(vectorRepositories)


# readAllVectorRepositories()


def enumerateVectorRepositories():
    vectorRepositories = configuration.VectorRepository.enumerate()
    print(vectorRepositories)


# enumerateVectorRepositories()


def readVectorRepository():
    vectorRepository = configuration.VectorRepository.retrieve(
        "00000000-0000-0000-0000-000000000000"
    )
    print(vectorRepository)


#readVectorRepository()


def createVectorRepository():
    vectorRepository = configuration.VectorRepository.create(
        Name="My vector repository",
        RepositoryType="Pgvector",
        Model="all-MiniLM-L6-v2",
        Dimensionality=384,
        DatabaseHostname="localhost",
        DatabaseName="vectordb",
        SchemaName="public",
        DatabaseTable="minilm",
        DatabasePort=5432,
        DatabaseUser="postgres",
        DatabasePassword="password",
    )
    print(vectorRepository)


# createVectorRepository()


def deleteEmbeddingsRules():
    embeddingsRules = configuration.EmbeddingsRule.delete(
        "51050c21-1640-43c4-bd1f-0e4748eca602"
    )
    print(embeddingsRules)


# deleteEmbeddingsRules()


def existsEmbeddingsRules():
    embeddingsRules = configuration.EmbeddingsRule.exists(
        "00000000-0000-0000-0000-000000000000"
    )
    print(embeddingsRules)


#existsEmbeddingsRules()


def updateEmbeddingsRules():
    embeddingsRules = configuration.EmbeddingsRule.update(
        "00000000-0000-0000-0000-000000000000",
        BucketGUID="00000000-0000-0000-0000-000000000000",
        Name="Embeddings rule [updated]",
        ContentType="*",
        GraphRepositoryGUID="00000000-0000-0000-0000-000000000000",
        VectorRepositoryGUID="00000000-0000-0000-0000-000000000000",
        ProcessingEndpoint="http://localhost:8000/v1.0/tenants/00000000-0000-0000-0000-000000000000/processing",
        ProcessingAccessKey="default",
        EmbeddingsGenerator="LCProxy",
        EmbeddingsGeneratorUrl="http://localhost:8000/v1.0/tenants/00000000-0000-0000-0000-000000000000/embeddings",
        EmbeddingsGeneratorApiKey="",
        EmbeddingsBatchSize=512,
        MaxEmbeddingsTasks=32,
        MaxEmbeddingsRetries=3,
        MaxEmbeddingsFailures=3,
        VectorStoreUrl="http://localhost:8000/",
        VectorStoreAccessKey="default",
        MaxContentLength=16777216,
    )
    print(embeddingsRules)


# updateEmbeddingsRules()


def readAllEmbeddingsRules():
    embeddingsRules = configuration.EmbeddingsRule.retrieve_all()
    print(embeddingsRules)


# readAllEmbeddingsRules()


def enumerateEmbeddingsRules():
    embeddingsRules = configuration.EmbeddingsRule.enumerate()
    print(embeddingsRules)


# enumerateEmbeddingsRules()


def readEmbeddingsRules():
    embeddingsRules = configuration.EmbeddingsRule.retrieve(
        "00000000-0000-0000-0000-000000000000"
    )
    print(embeddingsRules)


#readEmbeddingsRules()


def createEmbeddingRules():
    embeddingRules = configuration.EmbeddingsRule.create(
        BucketGUID="00000000-0000-0000-0000-000000000000",
        Name="Embeddings rule",
        ContentType="*",
        GraphRepositoryGUID="00000000-0000-0000-0000-000000000000",
        VectorRepositoryGUID="00000000-0000-0000-0000-000000000000",
        ProcessingEndpoint="http://localhost:8000/v1.0/tenants/00000000-0000-0000-0000-000000000000/processing",
        ProcessingAccessKey="default",
        EmbeddingsGenerator="LCProxy",
        EmbeddingsGeneratorUrl="http://localhost:8000/v1.0/tenants/00000000-0000-0000-0000-000000000000/embeddings",
        EmbeddingsGeneratorApiKey="",
        EmbeddingsBatchSize=512,
        MaxEmbeddingsTasks=32,
        MaxEmbeddingsRetries=3,
        MaxEmbeddingsFailures=3,
        VectorStoreUrl="http://localhost:8000/",
        VectorStoreAccessKey="default",
        MaxContentLength=16777216,
    )
    print(embeddingRules)


createEmbeddingRules()


def deleteMetaDataRules():
    metaDataRules = configuration.MetadataRule.delete(
        "7cbdd486-5cf6-415c-b504-436ce2b6eb44"
    )
    print(metaDataRules)


# deleteMetaDataRules()


def existsMetaDataRules():
    metaDataRules = configuration.MetadataRule.exists(
        "00000000-0000-0000-0000-000000000000"
    )
    print(metaDataRules)


#existsMetaDataRules()


def updateMetaDataRules():
    metaDataRules = configuration.MetadataRule.update(
        "00000000-0000-0000-0000-000000000000",
        BucketGUID="00000000-0000-0000-0000-000000000000",
        Name="example-metadata-rule-ash-updated",
        OwnerGUID="00000000-0000-0000-0000-000000000000",
        ContentType="*",
        MaxContentLength=134217728,
        ProcessingEndpoint="http://localhost:8000/v1.0/tenants/00000000-0000-0000-0000-000000000000/processing",
        ProcessingAccessKey="default",
        CleanupEndpoint="http://localhost:8000/v1.0/tenants/00000000-0000-0000-0000-000000000000/processing/cleanup",
        CleanupAccessKey="default",
        TopTerms=25,
        CaseInsensitive=True,
        IncludeFlattened=True,
        DataCatalogEndpoint="http://localhost:8000/",
        DataCatalogAccessKey="default",
        DataCatalogType="Lexi",
        DataCatalogCollection="00000000-0000-0000-0000-000000000000",
        GraphRepositoryGUID="00000000-0000-0000-0000-000000000000",
    )
    print(metaDataRules)


#updateMetaDataRules()


def readAllMetaDataRules():
    metaDataRules = configuration.MetadataRule.retrieve_all()
    print(metaDataRules)


#readAllMetaDataRules()


def enumerateMetaDataRules():
    metaDataRules = configuration.MetadataRule.enumerate()
    print(metaDataRules)


#enumerateMetaDataRules()


def readMetaDataRules():
    metaDataRules = configuration.MetadataRule.retrieve(
        "00000000-0000-0000-0000-000000000000"
    )
    print(metaDataRules)


#readMetaDataRules()


def createMetaDataRules():
    metaDataRules = configuration.MetadataRule.create(
        BucketGUID="00000000-0000-0000-0000-000000000000",
        Name="example-metadata-rule-ash",
        OwnerGUID="00000000-0000-0000-0000-000000000000",
        ContentType="*",
        MaxContentLength=134217728,
        ProcessingEndpoint="http://localhost:8000/v1.0/tenants/00000000-0000-0000-0000-000000000000/processing",
        ProcessingAccessKey="default",
        CleanupEndpoint="http://localhost:8000/v1.0/tenants/00000000-0000-0000-0000-000000000000/processing/cleanup",
        CleanupAccessKey="default",
        TopTerms=25,
        CaseInsensitive=True,
        IncludeFlattened=True,
        DataCatalogEndpoint="http://localhost:8000/",
        DataCatalogAccessKey="default",
        DataCatalogType="Lexi",
        DataCatalogCollection="00000000-0000-0000-0000-000000000000",
        GraphRepositoryGUID="00000000-0000-0000-0000-000000000000",
    )
    print(metaDataRules)


# createMetaDataRules()


def deleteCredential():
    credential = configuration.Credential.delete("a0589510-c808-417c-aea8-6bf3c35179a4")
    print(credential)


# deleteCredential()


def existsCredential():
    credential = configuration.Credential.exists("a0589510-c808-417c-aea8-6bf3c35179a4")
    print(credential)


# existsCredential()


def enumerateCredentials():
    credentials = configuration.Credential.enumerate()
    print(credentials)


# enumerateCredentials()


def readAllCredentials():
    credentials = configuration.Credential.retrieve_all()
    print(credentials)


# readAllCredentials()


def readCredential():
    credential = configuration.Credential.retrieve(
        "56dd6af5-c424-4fa0-9052-6d2ae7d6567c"
    )
    print(credential)


# readCredential()


def createCredential():
    credential = configuration.Credential.create(
        UserGUID="00000000-0000-0000-0000-000000000000",
        Name="Default credential",
        Active=True,
    )
    print(credential)

# createCredential()


def deleteUser():
    user = configuration.User.delete("b40e2df1-4a6c-4263-94db-9e9459fffd6c")
    print(user)


# deleteUser()


def existsUser():
    user = configuration.User.exists("b40e2df1-4a6c-4263-94db-9e9459fffd6c")
    print(user)


# existsUser()


def updateUser():
    user = configuration.User.update(
        "b40e2df1-4a6c-4263-94db-9e9459fffd6c",
        FirstName="New [updated]",
        LastName="User",
        Notes="Default password is password",
        Email="new@user.com",
        PasswordSha256="5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
    )
    print(user)


#updateUser()


def readAllUsers():
    users = configuration.User.retrieve_all()
    print(users)


#readAllUsers()


def enumerateUsers():
    users = configuration.User.enumerate()
    print(users)


#enumerateUsers()


def readUser():
    user = configuration.User.retrieve("00000000-0000-0000-0000-000000000000")
    print(user)


#readUser()


def createUser():
    user = configuration.User.create(
        FirstName="New",
        LastName="User",
        Notes="Default password is password",
        Email="new@user.com",
        PasswordSha256="5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
    )
    print(user)


#createUser()


def deleteNode():
    node = configuration.Node.delete(
        "784141bc-9717-4d0e-8079-1db6782baec6",
        headers={
            "x-token": "mXCNtMWDsW0/pr+IwRFUjVEm1mJD/fYAdFa//QO/CRjH93Tu8E7oeyn1KqlJe6LF/wsiT5aISGFvQ6RVBJ8mjQMVVoItV5Q7/LWq6A+7hm7dV9qTcQMXxyvga0rmStlyr0ktIG1KM7RWN7fT8lH+oBT4dSM8iLe+S8v/LqzrGYovKqduNNbDaM1h9tgW4HrfojIxLcA3E23VsSBn74MJmokhyYldzHkgPPFJjCfbkgieu7+tB8TLJmOU4gR3Ziy2KOiFO2GEj5z7Z+h5k0PLiz8MtnR62ieZt4G/1+vK6i9sUj9AEg5hNNIb50hbWsur"
        },
    )
    print(node)


# deleteNode()


def checkNode():
    node = configuration.Node.exists(
        "784141bc-9717-4d0e-8079-1db6782baec6",
        headers={
            "x-token": "mXCNtMWDsW0/pr+IwRFUjVEm1mJD/fYAdFa//QO/CRjH93Tu8E7oeyn1KqlJe6LF/wsiT5aISGFvQ6RVBJ8mjQMVVoItV5Q7/LWq6A+7hm7dV9qTcQMXxyvga0rmStlyr0ktIG1KM7RWN7fT8lH+oBT4dSM8iLe+S8v/LqzrGYovKqduNNbDaM1h9tgW4HrfojIxLcA3E23VsSBn74MJmokhyYldzHkgPPFJjCfbkgieu7+tB8TLJmOU4gR3Ziy2KOiFO2GEj5z7Z+h5k0PLiz8MtnR62ieZt4G/1+vK6i9sUj9AEg5hNNIb50hbWsur"
        },
    )
    print(node)


#checkNode()


def retrieveNode():
    node = configuration.Node.retrieve(
        "cc40e4b0-1dd3-467d-9d60-fe17846b58be",
        headers={
            "x-token": "mXCNtMWDsW0/pr+IwRFUjclG5ap7t0RbHfpxzSvAUH+Siq3pFXcO/HLVkwrz/HhG4IuGfqY0K9PhM4lMshXyAPSxNrZjmxGBRctiKYpIf9fZ8SfiJA110z2E9M0ENGWGdSVMm7bYNpWq5Yy/VWBltQtzAYb2RUzZfLnvA8v0aX3leXEGDNCOAjf0CcdBrYQZz6Qiukir3y8N8LHgXXnkYDoCqy9I9c9SkH4OprGp+TXVp7wHz7g9MyD/3NhJRnWTnUmQk0TLrI4gcabuNgYkkTXHkHSwo8qHQzldUlWivO6jbHx6vY+c65EdwjPif3R7"
        },
    )
    print(node)


#retrieveNode()  


def enumerateNodes():
    nodes = configuration.Node.enumerate(
        headers={
            "x-token": "mXCNtMWDsW0/pr+IwRFUjclG5ap7t0RbHfpxzSvAUH+Siq3pFXcO/HLVkwrz/HhG4IuGfqY0K9PhM4lMshXyAPSxNrZjmxGBRctiKYpIf9fZ8SfiJA110z2E9M0ENGWGdSVMm7bYNpWq5Yy/VWBltQtzAYb2RUzZfLnvA8v0aX3leXEGDNCOAjf0CcdBrYQZz6Qiukir3y8N8LHgXXnkYDoCqy9I9c9SkH4OprGp+TXVp7wHz7g9MyD/3NhJRnWTnUmQk0TLrI4gcabuNgYkkTXHkHSwo8qHQzldUlWivO6jbHx6vY+c65EdwjPif3R7"
        }
    )
    print(nodes)


#enumerateNodes()


def retrieveAllNodes():
    nodes = configuration.Node.retrieve_all(
        headers={
            "x-token": "mXCNtMWDsW0/pr+IwRFUjclG5ap7t0RbHfpxzSvAUH+Siq3pFXcO/HLVkwrz/HhG4IuGfqY0K9PhM4lMshXyAPSxNrZjmxGBRctiKYpIf9fZ8SfiJA110z2E9M0ENGWGdSVMm7bYNpWq5Yy/VWBltQtzAYb2RUzZfLnvA8v0aX3leXEGDNCOAjf0CcdBrYQZz6Qiukir3y8N8LHgXXnkYDoCqy9I9c9SkH4OprGp+TXVp7wHz7g9MyD/3NhJRnWTnUmQk0TLrI4gcabuNgYkkTXHkHSwo8qHQzldUlWivO6jbHx6vY+c65EdwjPif3R7"
        }
    )
    print(nodes)


# retrieveAllNodes()


def deleteTenant():
    tenant = configuration.Tenant.delete(
        "b7d0a699-52a3-4d97-b24e-d15b9bd066f4",
        headers={
            "x-token": "mXCNtMWDsW0/pr+IwRFUjVEm1mJD/fYAdFa//QO/CRjH93Tu8E7oeyn1KqlJe6LF/wsiT5aISGFvQ6RVBJ8mjQMVVoItV5Q7/LWq6A+7hm7dV9qTcQMXxyvga0rmStlyr0ktIG1KM7RWN7fT8lH+oBT4dSM8iLe+S8v/LqzrGYovKqduNNbDaM1h9tgW4HrfojIxLcA3E23VsSBn74MJmokhyYldzHkgPPFJjCfbkgieu7+tB8TLJmOU4gR3Ziy2KOiFO2GEj5z7Z+h5k0PLiz8MtnR62ieZt4G/1+vK6i9sUj9AEg5hNNIb50hbWsur"
        },
    )
    print(tenant)


# deleteTenant()


def existTenant():
    tenant = configuration.Tenant.exists(
        "00000000-0000-0000-0000-000000000000",
        headers={
            "x-token": "mXCNtMWDsW0/pr+IwRFUjclG5ap7t0RbHfpxzSvAUH+Siq3pFXcO/HLVkwrz/HhG4IuGfqY0K9PhM4lMshXyAPSxNrZjmxGBRctiKYpIf9fZ8SfiJA110z2E9M0ENGWGdSVMm7bYNpWq5Yy/VWBltQtzAYb2RUzZfLnvA8v0aX3leXEGDNCOAjf0CcdBrYQZz6Qiukir3y8N8LHgXXnkYDoCqy9I9c9SkH4OprGp+TXVp7wHz7g9MyD/3NhJRnWTnUmQk0TLrI4gcabuNgYkkTXHkHSwo8qHQzldUlWivO6jbHx6vY+c65EdwjPif3R7"
        },
    )
    print(tenant)


# existTenant()


def updateTenant():
    tenant = configuration.Tenant.update(
        "b7d0a699-52a3-4d97-b24e-d15b9bd066f4",
        headers={
            "x-token": "mXCNtMWDsW0/pr+IwRFUjVEm1mJD/fYAdFa//QO/CRjH93Tu8E7oeyn1KqlJe6LF/wsiT5aISGFvQ6RVBJ8mjQMVVoItV5Q7/LWq6A+7hm7dV9qTcQMXxyvga0rmStlyr0ktIG1KM7RWN7fT8lH+oBT4dSM8iLe+S8v/LqzrGYovKqduNNbDaM1h9tgW4HrfojIxLcA3E23VsSBn74MJmokhyYldzHkgPPFJjCfbkgieu7+tB8TLJmOU4gR3Ziy2KOiFO2GEj5z7Z+h5k0PLiz8MtnR62ieZt4G/1+vK6i9sUj9AEg5hNNIb50hbWsur"
        },
        data={
            "GUID": "b7d0a699-52a3-4d97-b24e-d15b9bd066f4",
            "AccountGUID": "00000000-0000-0000-0000-000000000000",
            "DefaultPoolGUID": "00000000-0000-0000-0000-000000000000",
            "Name": "My tenant [updated]",
            "Region": "us-west-1",
            "S3BaseDomain": "localhost",
            "RestBaseDomain": "localhost",
            "Active": True,
            "IsProtected": False,
            "CreatedUtc": "2025-05-05T10:07:59.000503Z",
        },
    )
    print(tenant)


# updateTenant()


def readAllTenants():
    tenants = configuration.Tenant.retrieve_all(
        headers={
            "x-token": "mXCNtMWDsW0/pr+IwRFUjclG5ap7t0RbHfpxzSvAUH+Siq3pFXcO/HLVkwrz/HhG4IuGfqY0K9PhM4lMshXyAPSxNrZjmxGBRctiKYpIf9fZ8SfiJA110z2E9M0ENGWGdSVMm7bYNpWq5Yy/VWBltQtzAYb2RUzZfLnvA8v0aX3leXEGDNCOAjf0CcdBrYQZz6Qiukir3y8N8LHgXXnkYDoCqy9I9c9SkH4OprGp+TXVp7wHz7g9MyD/3NhJRnWTnUmQk0TLrI4gcabuNgYkkTXHkHSwo8qHQzldUlWivO6jbHx6vY+c65EdwjPif3R7"
        }
    )
    print(tenants)


# readAllTenants()


def readTenant():
    tenant = configuration.Tenant.retrieve(
        "00000000-0000-0000-0000-000000000000",
        headers={
            "x-token": "mXCNtMWDsW0/pr+IwRFUjclG5ap7t0RbHfpxzSvAUH+Siq3pFXcO/HLVkwrz/HhG4IuGfqY0K9PhM4lMshXyAPSxNrZjmxGBRctiKYpIf9fZ8SfiJA110z2E9M0ENGWGdSVMm7bYNpWq5Yy/VWBltQtzAYb2RUzZfLnvA8v0aX3leXEGDNCOAjf0CcdBrYQZz6Qiukir3y8N8LHgXXnkYDoCqy9I9c9SkH4OprGp+TXVp7wHz7g9MyD/3NhJRnWTnUmQk0TLrI4gcabuNgYkkTXHkHSwo8qHQzldUlWivO6jbHx6vY+c65EdwjPif3R7"
        },
    )
    print(tenant)


#readTenant()


def enumerateTenants():
    tenants = configuration.Tenant.enumerate(
        headers={
            "x-token": "mXCNtMWDsW0/pr+IwRFUjclG5ap7t0RbHfpxzSvAUH+Siq3pFXcO/HLVkwrz/HhG4IuGfqY0K9PhM4lMshXyAPSxNrZjmxGBRctiKYpIf9fZ8SfiJA110z2E9M0ENGWGdSVMm7bYNpWq5Yy/VWBltQtzAYb2RUzZfLnvA8v0aX3leXEGDNCOAjf0CcdBrYQZz6Qiukir3y8N8LHgXXnkYDoCqy9I9c9SkH4OprGp+TXVp7wHz7g9MyD/3NhJRnWTnUmQk0TLrI4gcabuNgYkkTXHkHSwo8qHQzldUlWivO6jbHx6vY+c65EdwjPif3R7"
        }
    )
    print(tenants)


# enumerateTenants()


def createTenant():
    tenant = configuration.Tenant.create(
        headers={
            "x-token": "mXCNtMWDsW0/pr+IwRFUjVEm1mJD/fYAdFa//QO/CRjH93Tu8E7oeyn1KqlJe6LF/wsiT5aISGFvQ6RVBJ8mjQMVVoItV5Q7/LWq6A+7hm7dV9qTcQMXxyvga0rmStlyr0ktIG1KM7RWN7fT8lH+oBT4dSM8iLe+S8v/LqzrGYovKqduNNbDaM1h9tgW4HrfojIxLcA3E23VsSBn74MJmokhyYldzHkgPPFJjCfbkgieu7+tB8TLJmOU4gR3Ziy2KOiFO2GEj5z7Z+h5k0PLiz8MtnR62ieZt4G/1+vK6i9sUj9AEg5hNNIb50hbWsur"
        },
        AccountGUID="00000000-0000-0000-0000-000000000000",
        Name="My tenant",
        DefaultPoolGUID="00000000-0000-0000-0000-000000000000",
        S3BaseDomain="localhost",
        RestBaseDomain="localhost",
    )
    print(tenant)


# createTenant()


def getTokenDetails():
    token = configuration.Authentication.retrieve_token_details(
        token="mXCNtMWDsW0/pr+IwRFUjclG5ap7t0RbHfpxzSvAUH+Siq3pFXcO/HLVkwrz/HhG4IuGfqY0K9PhM4lMshXyAPSxNrZjmxGBRctiKYpIf9fZ8SfiJA110z2E9M0ENGWGdSVMm7bYNpWq5Yy/VWBltQtzAYb2RUzZfLnvA8v0aX3leXEGDNCOAjf0CcdBrYQZz6Qiukir3y8N8LHgXXnkYDoCqy9I9c9SkH4OprGp+TXVp7wHz7g9MyD/3NhJRnWTnUmQk0TLrI4gcabuNgYkkTXHkHSwo8qHQzldUlWivO6jbHx6vY+c65EdwjPif3R7"
    )
    print(token)


#getTokenDetails()


def getAdministratorToken():
    token = configuration.Authentication.retrieve_administrator_token(
        email="admin@view.io", password="viewadmin"
    )
    print(token)


#getAdministratorToken()


def getAuthenticationTokenSha256():
    token = configuration.Authentication.generate_authentication_token_sha_256(
        "default@user.com",
        "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "00000000-0000-0000-0000-000000000000",
    )
    print(token)


#getAuthenticationTokenSha256()


def getTenantsForEmail():
    tenants = configuration.Authentication.retrieve_tenants_for_email("default@user.com")
    print(tenants)


#getTenantsForEmail()


def getAuthenticationToken():
    token = configuration.Authentication.generate_authentication_token(
        "default@user.com", "password", "00000000-0000-0000-0000-000000000000"
    )
    print(token)


#getAuthenticationToken()
