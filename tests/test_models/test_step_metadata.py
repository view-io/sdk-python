from datetime import datetime, timezone
from view_sdk.models.step_metadata import StepMetadataModel
from view_sdk.enums.step_runtime_enum import StepRuntimeEnum


def make_required_fields():
    return dict(
        step_archive_filename="archive.zip",
        step_entrypoint_filename="main.py",
        step_entrypoint_type="python",
    )


def test_step_metadata_defaults():
    fields = make_required_fields()
    model = StepMetadataModel(**fields)
    assert model.name == "My data flow step"
    assert model.runtime == StepRuntimeEnum.Dotnet8
    assert model.step_archive_filename == "archive.zip"
    assert model.step_entrypoint_filename == "main.py"
    assert model.step_entrypoint_type == "python"
    assert model.debug_assembly_load is False
    assert isinstance(model.created_utc, datetime)


def test_step_metadata_with_values():
    fields = make_required_fields()
    now = datetime(2024, 1, 1, tzinfo=timezone.utc)
    model = StepMetadataModel(
        **fields,
        name="Test Step",
        runtime=StepRuntimeEnum.Python3_12,
        debug_assembly_load=True,
        created_utc=now,
        notes="note",
        virtual_environment="venv",
        dependencies_file="reqs.txt",
        package=b"abc",
    )
    assert model.name == "Test Step"
    assert model.runtime == StepRuntimeEnum.Python3_12
    assert model.debug_assembly_load is True
    assert model.created_utc == now
    assert model.notes == "note"
    assert model.virtual_environment == "venv"
    assert model.dependencies_file == "reqs.txt"
    assert model.package == b"abc"


def test_step_metadata_aliases():
    fields = {
        "StepArchiveFilename": "archive.zip",
        "StepEntrypointFilename": "main.py",
        "StepEntrypointType": "python",
    }
    model = StepMetadataModel.model_validate(fields)
    assert model.step_archive_filename == "archive.zip"
    assert model.step_entrypoint_filename == "main.py"
    assert model.step_entrypoint_type == "python"


def test_step_metadata_serialization():
    fields = make_required_fields()
    model = StepMetadataModel(**fields)
    model_dict = model.model_dump(by_alias=True)
    assert model_dict["StepArchiveFilename"] == "archive.zip"
    assert model_dict["StepEntrypointFilename"] == "main.py"
    assert model_dict["StepEntrypointType"] == "python"
