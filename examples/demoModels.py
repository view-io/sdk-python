import view_sdk
from view_sdk import configuration
from view_sdk.sdk_configuration import Service

# Configure the SDK
sdk = view_sdk.configure(
    access_key="default",
    base_url="192.168.101.63",
    tenant_guid="00000000-0000-0000-0000-000000000000",
    service_ports={Service.DEFAULT: 8000},
)

# =============================================================================
# ModelConfiguration Operations
# =============================================================================

def createModelConfiguration():
    """Create a new model configuration."""
    model_config = configuration.ModelConfiguration.create(
        ModelName="llama2:7b",
        Embeddings=True,
        Completions=True,
        ContextSize=4096,
        MaxOutputTokens=2048,
        Temperature=0.7,
        TopP=0.9,
        TopK=40,
        FrequencyPenalty=0.0,
        PresencePenalty=0.0,
        EnableStreaming=True,
        TimeoutMs=30000,
        AdditionalData="Demo model configuration for testing",
        Active=True
    )
    print("Created ModelConfiguration:")
    print(model_config)
    return model_config

#createModelConfiguration()

def readModelConfiguration():
    """Retrieve a specific model configuration by GUID."""
    model_config = configuration.ModelConfiguration.retrieve(
        "00000000-0000-0000-0000-000000000000"
    )
    print("Retrieved ModelConfiguration:")
    print(model_config)

#readModelConfiguration()

def updateModelConfiguration():
    """Update an existing model configuration."""
    model_config = configuration.ModelConfiguration.update(
        "00000000-0000-0000-0000-000000000000",
        ModelName="llama2:13b",
        Temperature=0.8,
        MaxOutputTokens=4096,
        AdditionalData="Updated model configuration for testing"
    )
    print("Updated ModelConfiguration:")
    print(model_config)

#updateModelConfiguration()

def deleteModelConfiguration():
    """Delete a model configuration."""
    result = configuration.ModelConfiguration.delete(
        "00000000-0000-0000-0000-000000000000"
    )
    print("Deleted ModelConfiguration:")
    print(result)

#deleteModelConfiguration()

def existsModelConfiguration():
    """Check if a model configuration exists."""
    exists = configuration.ModelConfiguration.exists(
        "00000000-0000-0000-0000-000000000000"
    )
    print("ModelConfiguration exists:")
    print(exists)

#existsModelConfiguration()

def enumerateModelConfigurations():
    """Enumerate all model configurations."""
    model_configs = configuration.ModelConfiguration.enumerate()
    print("Enumerated ModelConfigurations:")
    print(model_configs)

#enumerateModelConfigurations()

def retrieveAllModelConfigurations():
    """Retrieve all model configurations."""
    model_configs = configuration.ModelConfiguration.retrieve_all()
    print("All ModelConfigurations:")
    print(model_configs)

#retrieveAllModelConfigurations()

# =============================================================================
# ModelEndpoint Operations
# =============================================================================

def createModelEndpoint():
    """Create a new model endpoint."""
    model_endpoint = configuration.ModelEndpoint.create(
        Name="Ollama Local Endpoint",
        EndpointUrl="http://localhost:11434/",
        BearerToken=None,
        ApiType="Ollama",
        TimeoutMs=30000,
        AdditionalData="Local Ollama endpoint for testing",
        Active=True
    )
    print("Created ModelEndpoint:")
    print(model_endpoint)
    return model_endpoint

#createModelEndpoint()

def readModelEndpoint():
    """Retrieve a specific model endpoint by GUID."""
    model_endpoint = configuration.ModelEndpoint.retrieve(
        "00000000-0000-0000-0000-000000000000"
    )
    print("Retrieved ModelEndpoint:")
    print(model_endpoint)

#readModelEndpoint()

def updateModelEndpoint():
    """Update an existing model endpoint."""
    model_endpoint = configuration.ModelEndpoint.update(
        "00000000-0000-0000-0000-000000000000",
        Name="Ollama Local Endpoint [Updated]",
        EndpointUrl="http://localhost:11435/",
        TimeoutMs=60000,
        AdditionalData="Updated Ollama endpoint for testing"
    )
    print("Updated ModelEndpoint:")
    print(model_endpoint)

#updateModelEndpoint()

def deleteModelEndpoint():
    """Delete a model endpoint."""
    result = configuration.ModelEndpoint.delete(
        "00000000-0000-0000-0000-000000000000"
    )
    print("Deleted ModelEndpoint:")
    print(result)

# deleteModelEndpoint()

def existsModelEndpoint():
    """Check if a model endpoint exists."""
    exists = configuration.ModelEndpoint.exists(
        "00000000-0000-0000-0000-000000000000"
    )
    print("ModelEndpoint exists:")
    print(exists)

#existsModelEndpoint()

def enumerateModelEndpoints():
    """Enumerate all model endpoints."""
    model_endpoints = configuration.ModelEndpoint.enumerate()
    print("Enumerated ModelEndpoints:")
    print(model_endpoints)

#enumerateModelEndpoints()

def retrieveAllModelEndpoints():
    """Retrieve all model endpoints."""
    model_endpoints = configuration.ModelEndpoint.retrieve_all()
    print("All ModelEndpoints:")
    print(model_endpoints)

#retrieveAllModelEndpoints()

# =============================================================================
# ModelProfile Operations
# =============================================================================

def createModelProfile():
    """Create a new model profile."""
    model_profile = configuration.ModelProfile.create(
        ModelConfigurationGUID="00000000-0000-0000-0000-000000000000",
        ModelEndpointGUID="00000000-0000-0000-0000-000000000000",
        Name="Demo Model Profile",
        AdditionalData="Demo model profile for testing",
        Active=True
    )
    print("Created ModelProfile:")
    print(model_profile)
    return model_profile

createModelProfile()

def readModelProfile():
    """Retrieve a specific model profile by GUID."""
    model_profile = configuration.ModelProfile.retrieve(
        "00000000-0000-0000-0000-000000000000"
    )
    print("Retrieved ModelProfile:")
    print(model_profile)

readModelProfile()

def updateModelProfile():
    """Update an existing model profile."""
    model_profile = configuration.ModelProfile.update(
        "00000000-0000-0000-0000-000000000000",
        ModelConfigurationGUID="00000000-0000-0000-0000-000000000000",
        ModelEndpointGUID="00000000-0000-0000-0000-000000000000",
        Name="Demo Model Profile [Updated]",
        AdditionalData="Updated demo model profile for testing"
    )
    print("Updated ModelProfile:")
    print(model_profile)

updateModelProfile()

def deleteModelProfile():
    """Delete a model profile."""
    result = configuration.ModelProfile.delete(
        "00000000-0000-0000-0000-000000000000"
    )
    print("Deleted ModelProfile:")
    print(result)

#deleteModelProfile()

def existsModelProfile():
    """Check if a model profile exists."""
    exists = configuration.ModelProfile.exists(
        "00000000-0000-0000-0000-000000000000"
    )
    print("ModelProfile exists:")
    print(exists)

existsModelProfile()

def enumerateModelProfiles():
    """Enumerate all model profiles."""
    model_profiles = configuration.ModelProfile.enumerate()
    print("Enumerated ModelProfiles:")
    print(model_profiles)

enumerateModelProfiles()

def retrieveAllModelProfiles():
    """Retrieve all model profiles."""
    model_profiles = configuration.ModelProfile.retrieve_all()
    print("All ModelProfiles:")
    print(model_profiles)

retrieveAllModelProfiles()

# =============================================================================
# Workflow Example: Create Complete Model Setup
# =============================================================================

def createCompleteModelSetup():
    """Create a complete model setup with configuration, endpoint, and profile."""
    print("Creating complete model setup...")
    
    # Step 1: Create Model Configuration
    print("\n1. Creating Model Configuration...")
    model_config = createModelConfiguration()
    config_guid = model_config.guid if hasattr(model_config, 'guid') else model_config.get('GUID')
    
    # Step 2: Create Model Endpoint
    print("\n2. Creating Model Endpoint...")
    model_endpoint = createModelEndpoint()
    endpoint_guid = model_endpoint.guid if hasattr(model_endpoint, 'guid') else model_endpoint.get('GUID')
    
    # Step 3: Create Model Profile linking configuration and endpoint
    print("\n3. Creating Model Profile...")
    model_profile = configuration.ModelProfile.create(
        ModelConfigurationGUID=config_guid,
        ModelEndpointGUID=endpoint_guid,
        Name="Complete Demo Profile",
        AdditionalData="Complete model setup for testing",
        Active=True
    )
    print("Created ModelProfile:")
    print(model_profile)
    
    print("\nComplete model setup created successfully!")
    return {
        'model_config': model_config,
        'model_endpoint': model_endpoint,
        'model_profile': model_profile
    }

# createCompleteModelSetup()
