import pytest
from pydantic import ValidationError
from view_sdk.models.semantic_cell import SemanticCellModel
from view_sdk.models.semantic_chunk import SemanticChunkModel
from view_sdk.enums.semantic_cell_type_enum import SemanticCellTypeEnum


@pytest.fixture
def valid_semantic_chunk_data():
    return {
        "GUID": "123e4567-e89b-12d3-a456-426614174000",
        "Position": 0,
        "Start": 0,
        "End": 10,
        "Content": "Test content",
        "Embeddings": [0.1, 0.2, 0.3],
    }


@pytest.fixture
def valid_semantic_cell_data(valid_semantic_chunk_data):
    return {
        "GUID": "223e4567-e89b-12d3-a456-426614174000",
        "CellType": "Text",
        "Position": 0,
        "Chunks": [valid_semantic_chunk_data],
        "Children": [],
    }


def test_create_minimal_semantic_cell():
    """Test creating a semantic cell with minimal required fields."""
    cell = SemanticCellModel()

    assert isinstance(cell.guid, str)
    assert cell.cell_type == SemanticCellTypeEnum.Text
    assert cell.position == 0
    assert cell.chunks == []
    assert cell.children == []
    assert cell.md5_hash == ""
    assert cell.sha1_hash is None
    assert cell.sha256_hash is None


def test_create_complete_semantic_cell(valid_semantic_cell_data):
    """Test creating a semantic cell with all fields populated."""
    cell = SemanticCellModel(**valid_semantic_cell_data)

    assert cell.guid == valid_semantic_cell_data["GUID"]
    assert cell.cell_type == SemanticCellTypeEnum.Text
    assert cell.position == 0
    assert len(cell.chunks) == 1
    assert isinstance(cell.chunks[0], SemanticChunkModel)
    assert len(cell.children) == 0


def test_cell_type_validation():
    """Test validation of cell type enum."""
    # Test all valid cell types
    for cell_type in SemanticCellTypeEnum:
        cell = SemanticCellModel(CellType=cell_type)
        assert cell.cell_type == cell_type

    # Test invalid cell type
    with pytest.raises(ValidationError) as exc_info:
        SemanticCellModel(CellType="InvalidType")
    assert "type=enum" in str(exc_info.value)


def test_position_validation():
    """Test validation of position field."""
    # Test valid position
    cell = SemanticCellModel(Position=5)
    assert cell.position == 5

    # Test invalid position (less than 0)
    with pytest.raises(ValidationError) as exc_info:
        SemanticCellModel(Position=-1)
    assert "greater than or equal to 0" in str(exc_info.value)


def test_nested_children():
    """Test nested children structure."""
    child_data = {
        "GUID": "child-guid",
        "CellType": "Text",
        "Position": 1,
        "Children": [],
    }

    parent_data = {
        "GUID": "parent-guid",
        "CellType": "Text",
        "Position": 0,
        "Children": [child_data],
    }

    cell = SemanticCellModel(**parent_data)
    assert len(cell.children) == 1
    assert isinstance(cell.children[0], SemanticCellModel)
    assert cell.children[0].guid == "child-guid"


def test_model_aliases():
    """Test that field aliases are working correctly."""
    data = {"guid": "test-guid", "cell_type": "Text", "position": 1}
    cell = SemanticCellModel(**data)
    assert cell.guid == "test-guid"
    assert cell.cell_type == SemanticCellTypeEnum.Text
    assert cell.position == 1


def test_validate_lists():
    """Test list validation behavior."""
    # Test empty lists
    cell = SemanticCellModel(Chunks=[], Children=[])
    assert cell.chunks == []
    assert cell.children == []

    # Test None values
    cell = SemanticCellModel(Chunks=None, Children=None)
    assert cell.chunks == []
    assert cell.children == []
