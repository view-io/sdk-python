import view_sdk
from view_sdk import orchestration

sdk = view_sdk.configure(
    access_key="default",
    base_url="view.homedns.org",
    tenant_guid="00000000-0000-0000-0000-000000000000",
)


def deleteDataFlow():
    response = orchestration.DataFlow.delete("321cea16-7b64-4038-899a-ea3a82b0b457")
    print(response)


# deleteDataFlow()


def existsDataFlow():
    exists = orchestration.DataFlow.exists("321cea16-7b64-4038-899a-ea3a82b0b457")
    print(exists)


# existsDataFlow()


def readAllDataFlows():
    dataflows = orchestration.DataFlow.retrieve_all()
    print(dataflows)


# readAllDataFlows()


def readPerformanceData():
    performanceData = orchestration.DataFlow.retrieve_request_log_file(
        "321cea16-7b64-4038-899a-ea3a82b0b457", "00000000-0000-0000-0000-000000000000"
    )
    print(performanceData)


# readPerformanceData()


def readDataFlow():
    dataflow = orchestration.DataFlow.retrieve(
        "321cea16-7b64-4038-899a-ea3a82b0b457", True
    )
    print(dataflow)


# readDataFlow()


def createDataFlow():
    dataflow = orchestration.DataFlow.create(
        TriggerGUID="00000000-0000-0000-0000-000000000000",
        StepGUID="00000000-0000-0000-0000-000000000000",
        Name="Another data flow",
        Notes="My notes",
        LogRetentionDays=7,
        Map={
            "StepGUID": "00000000-0000-0000-0000-000000000000",
            "Success": None,
            "Failure": None,
            "Exception": None,
        },
    )
    print(dataflow)


# createDataFlow()


def deleteStep():
    response = orchestration.Step.delete("cf731a32-9581-4583-8bd2-50267b036352")
    print(response)


# deleteStep()


def existsStep():
    exists = orchestration.Step.exists("cf731a32-9581-4583-8bd2-50267b036352")
    print(exists)


# existsStep()


def readAllSteps():
    steps = orchestration.Step.retrieve_all()
    print(steps)


# readAllSteps()


def readStep():
    step = orchestration.Step.retrieve(
        "cf731a32-9581-4583-8bd2-50267b036352", incl_data=True, incl_subordinates=True
    )
    print(step)


# readStep()


def createStep():
    step = orchestration.Step.create(
        Name="Another test step",
        Runtime="Dotnet8",
        StepArchiveFilename="TestStep.zip",
        StepEntrypointFilename="LoopbackGetStep.dll",
        StepEntrypointType="LoopbackGetStep.LoopbackGetStep",
        MD5Hash="900B50364A091B1D09A374EBD364F056",
        SHA1Hash="1216C1DCD4E7A2A5A2F615F852AB886F2BB29202",
        SHA256Hash="46403910F99FDE6F0581E66F70638AB961CBF13BA64D870E8816C84BAC05462F",
        DebugAssemblyLoad=False,
        DebugWrapperScript=False,
        DebugRequestData=False,
        DebugResponseData=False,
        ConsoleLogging=True,
        VirtualEnvironment=None,
        DependenciesFile=None,
        CreatedUtc="2024-05-09T16:13:55.608668Z",
        Package="",
    )
    print(step)


# createStep()


def deleteTrigger():
    response = orchestration.Trigger.delete("8fc742a5-9ef7-4304-8ea4-2fba6b755f92")
    print(response)


# deleteTrigger()


def existsTrigger():
    exists = orchestration.Trigger.exists("8fc742a5-9ef7-4304-8ea4-2fba6b755f92")
    print(exists)


# existsTrigger()


def updateTrigger():
    trigger = orchestration.Trigger.update(
        "8fc742a5-9ef7-4304-8ea4-2fba6b755f92",
        TriggerType="HTTP",
        Name="My second trigger updated",
        HttpMethod="GET",
        HttpUrlPrefix="/default2",
    )
    print(trigger)


# updateTrigger()


def readAllTriggers():
    triggers = orchestration.Trigger.retrieve_all()
    print(triggers)


# readAllTriggers()


def readTrigger():
    trigger = orchestration.Trigger.retrieve("8fc742a5-9ef7-4304-8ea4-2fba6b755f92")
    print(trigger)


# readTrigger()


def createTrigger():
    trigger = orchestration.Trigger.create(
        TriggerType="HTTP",
        Name="My second trigger",
        HttpMethod="GET",
        HttpUrlPrefix="/default2",
    )
    print(trigger)


# createTrigger()
