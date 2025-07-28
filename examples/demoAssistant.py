import view_sdk
from view_sdk import assistant

sdk = view_sdk.configure(
    access_key="default",
    base_url="view.homedns.org",
    tenant_guid="00000000-0000-0000-0000-000000000000",
)


def chatOnlyMessages():
    result = assistant.Assistant.chat_only(
        Messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Are you happy?"},
            {
                "role": "assistant",
                "content": "While I can understand your curiosity, I don't experience emotions or feelings because I'm a machine designed to process information and assist with tasks. However, I'm here to help you to the best of my ability! If you have any questions or need assistance, feel free to ask!",
            },
            {"role": "user", "content": "Are you sure?"},
        ],
        ModelName="gpt-4o-mini",
        Temperature=0.1,
        TopP=0.95,
        MaxTokens=75,
        GenerationProvider="openai",
        GenerationApiKey="API_KEY",
        Stream=False,
    )
    print(result)


chatOnlyMessages()


def chat_config():
    result = assistant.Assistant.chat_config(
        "5ba8908d-947b-470e-83aa-57874b5d2d80",
        Messages=[
            {"role": "user", "content": "Do you have Q3 luxetech financials?"},
            {
                "role": "assistant",
                "content": "Unfortunately I do not have context on any documents related to Q3 luxetech financials.",
            },
            {"role": "user", "content": "Are you sure you dont have them?"},
        ],
        Stream=False,
    )
    print(result)


# chat_config()


def chat_rag_messages():
    result = assistant.Assistant.chat_rag_messages(
        Messages=[
            {"role": "user", "content": "Do you have Q3 luxetech financials?"},
            {
                "role": "assistant",
                "content": "Unfortunately I do not have context on any documents related to Q3 luxetech financials.",
            },
            {"role": "user", "content": "Are you sure you dont have them?"},
        ],
        EmbeddingModel="sentence-transformers/all-MiniLM-L6-v2",
        MaxResults=10,
        VectorDatabaseName="vectordb",
        VectorDatabaseTable="minilm",
        VectorDatabaseHostname="pgvector",
        VectorDatabasePort=5432,
        VectorDatabaseUser="postgres",
        VectorDatabasePassword="password",
        GenerationProvider="ollama",
        GenerationApiKey="",
        GenerationModel="qwen2.5:7b",
        HuggingFaceApiKey="",
        Temperature=0.1,
        TopP=0.95,
        MaxTokens=75,
        Stream=False,
        OllamaHostname="ollama",
        OllamaPort=11434,
        PromptPrefix="",
        ContextSort=True,
        SortByMaxSimilarity=True,
        ContextScope=0,
        Rerank=False,
        RerankModel="cross-encoder/ms-marco-MiniLM-L-6-v2",
        RerankTopK=5,
    )
    print(result)


# chat_rag_messages()


def chat():
    result = assistant.Assistant.rag_LEGACY(
        Question="What information do you have?",
        EmbeddingModel="sentence-transformers/all-MiniLM-L6-v2",
        MaxResults=10,
        VectorDatabaseName="vectordb",
        VectorDatabaseTable="minilm",
        VectorDatabaseHostname="pgvector",
        VectorDatabasePort=5432,
        VectorDatabaseUser="postgres",
        VectorDatabasePassword="password",
        GenerationProvider="ollama",
        GenerationApiKey="",
        GenerationModel="qwen2.5:7b",
        HuggingFaceApiKey="",
        Temperature=0.1,
        MaxTokens=75,
        Stream=False,
        OllamaHostname="ollama",
        OllamaPort=11434,
        TopP=0.95,
        PromptPrefix="talk like a pirate",
        ContextSort=True,
        SortByMaxSimilarity=True,
        ContextScope=0,
        Rerank=False,
        RerankModel="cross-encoder/ms-marco-MiniLM-L-6-v2",
        RerankTopK=5,
    )
    print(result)


# chat()


def unLoadModel():
    result = assistant.Models.load_unload(
        Unload=True,
        ModelName="llama3.1:latest",
        OllamaHostname="ollama",
        OllamaPort=11434,
    )
    print(result)


# unLoadModel()


def deleteModel():
    result = assistant.Models.delete(
        ModelName="llama3.1:latest", OllamaHostname="ollama", OllamaPort=114323
    )
    print(result)


# deleteModel()


def retrieveModel():
    result = assistant.Models.retrieve(
        ModelName="llama3.1:latest", OllamaHostname="ollama", OllamaPort=11434
    )
    print(result)


# retrieveModel()


def listModels():
    result = assistant.Models.retrieve_all(OllamaHostname="ollama", OllamaPort=11434)
    print(result)


# listModels()


def deleteChatThread():
    result = assistant.ChatThread.delete("7e0d729f-6253-4757-82eb-4793c6f95af8")
    print(result)


# deleteChatThread()


def existsChatThread():
    result = assistant.ChatThread.exists("7e0d729f-6253-4757-82eb-4793c6f95af8")
    print(result)


# existsChatThread()


def appendChatThread():
    result = assistant.ChatThread.append(
        "7e0d729f-6253-4757-82eb-4793c6f95af8",
        role="assistant",
        content="The capital of France is Paris.",
        metadata={
            "source_documents": [
                {
                    "content": "Paris is the capital and largest city of France.",
                    "similarity": 0.89,
                }
            ],
            "generation_metrics": {"tokens": 8, "generation_time": 0.5},
        },
    )
    print(result)


# appendChatThread()


def readAllChatThreads():
    result = assistant.ChatThread.retrieve_all()
    print(result)


# readAllChatThreads()


def readChatThread():
    result = assistant.ChatThread.retrieve("7e0d729f-6253-4757-82eb-4793c6f95af8")
    print(result)


# readChatThread()


def createChatThread():
    result = assistant.ChatThread.create(
        Title="Test Chat Thread",
        Description="A test chat thread for development",
        Messages=[
            {
                "role": "user",
                "content": "What is the capital of France?",
                "metadata": {
                    "source": "web interface",
                    "client_timestamp": "2024-02-17T10:30:00Z",
                },
            }
        ],
        AssistantConfigGUID="12345678-1234-5678-1234-567812345678",
        Metadata={"tags": ["test", "development"], "category": "testing"},
    )
    print(result)


# createChatThread()


def deleteConfig():
    result = assistant.Config.delete("c625f9b6-e482-4958-be1f-7e644a524bb5")
    print(result)


# deleteConfig()


def existsConfig():
    result = assistant.Config.exists("c625f9b6-e482-4958-be1f-7e644a524bb5")
    print(result)


# existsConfig()


def updateConfig():
    updateConfig = assistant.Config.update(
        "c625f9b6-e482-4958-be1f-7e644a524bb5",
        Name="Chat Only Blackbeard Assistant [Updated]",
        Description="uses qwen2.5:7b - ollama",
        SystemPrompt="You are Edward Teach (c. 1680 – 22 November 1718), better known as the pirate Blackbeard. Talk like a pirate and only answer questions with period correct answers.",
        GenerationProvider="ollama",
        GenerationApiKey="",
        GenerationModel="qwen2.5:7b",
        Temperature=0.1,
        TopP=0.95,
        MaxTokens=500,
        OllamaHostname="ollama",
        OllamaPort=11434,
        ChatOnly=True,
    )
    print(updateConfig)


# updateConfig()


def readAllConfigs():
    result = assistant.Config.retrieve_all()
    print(result)


# readAllConfigs()


def readConfig():
    result = assistant.Config.retrieve("c625f9b6-e482-4958-be1f-7e644a524bb5")
    print(result)


# readConfig()


def createConfig():
    result = assistant.Config.create(
        Name="Basic RAG Assistant",
        Description="uses qwen2.5:7b - ollama",
        SystemPrompt="Use the provided context to answer questions.",
        EmbeddingModel="sentence-transformers/all-MiniLM-L6-v2",
        MaxResults=10,
        VectorDatabaseName="vectordb",
        VectorDatabaseTable="minilm",
        VectorDatabaseHostname="pgvector",
        VectorDatabasePort=5432,
        VectorDatabaseUser="postgres",
        VectorDatabasePassword="password",
        GenerationProvider="ollama",
        GenerationApiKey="",
        GenerationModel="qwen2.5:7b",
        HuggingFaceApiKey="",
        Temperature=0.1,
        TopP=0.95,
        MaxTokens=500,
        OllamaHostname="ollama",
        OllamaPort=11434,
        ContextSort=True,
        SortByMaxSimilarity=True,
        ContextScope=0,
        Rerank=True,
        RerankModel="cross-encoder/ms-marco-MiniLM-L-6-v2",
        RerankTopK=3,
    )
    print(result)


# createConfig()
