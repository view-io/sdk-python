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


def test_length_property():
    """Test the length property that returns count_bytes()."""
    # Test with no chunks or children
    cell = SemanticCellModel()
    assert cell.length == 0

    # Test with chunks
    chunk_data = {
        "GUID": "chunk-guid",
        "Content": "Hello world",
        "Length": 11,
    }
    cell = SemanticCellModel(Chunks=[chunk_data])
    assert cell.length == 11

    # Test with children
    child_data = {
        "GUID": "child-guid",
        "Chunks": [chunk_data],
    }
    cell = SemanticCellModel(Children=[child_data])
    assert cell.length == 11


def test_count_embeddings():
    """Test count_embeddings method."""
    # Test with no chunks or children
    cell = SemanticCellModel()
    assert cell.count_embeddings() == 0

    # Test with chunks containing embeddings
    chunk_data = {
        "GUID": "chunk-guid",
        "Content": "Test content",
        "Embeddings": [0.1, 0.2, 0.3],
    }
    cell = SemanticCellModel(Chunks=[chunk_data])
    assert cell.count_embeddings() == 3

    # Test with multiple chunks
    chunk_data2 = {
        "GUID": "chunk-guid-2",
        "Content": "More content",
        "Embeddings": [0.4, 0.5],
    }
    cell = SemanticCellModel(Chunks=[chunk_data, chunk_data2])
    assert cell.count_embeddings() == 5

    # Test with children
    child_data = {
        "GUID": "child-guid",
        "Chunks": [chunk_data],
    }
    cell = SemanticCellModel(Children=[child_data])
    assert cell.count_embeddings() == 3

    # Test with both chunks and children
    cell = SemanticCellModel(Chunks=[chunk_data2], Children=[child_data])
    assert cell.count_embeddings() == 5


def test_count_semantic_cells():
    """Test count_semantic_cells method."""
    # Test with no children
    cell = SemanticCellModel()
    assert cell.count_semantic_cells() == 1

    # Test with one child
    child_data = {
        "GUID": "child-guid",
        "CellType": "Text",
    }
    cell = SemanticCellModel(Children=[child_data])
    assert cell.count_semantic_cells() == 2

    # Test with nested children
    grandchild_data = {
        "GUID": "grandchild-guid",
        "CellType": "Text",
    }
    child_data_with_grandchild = {
        "GUID": "child-guid",
        "CellType": "Text",
        "Children": [grandchild_data],
    }
    cell = SemanticCellModel(Children=[child_data_with_grandchild])
    assert cell.count_semantic_cells() == 3

    # Test with multiple children
    cell = SemanticCellModel(Children=[child_data, child_data_with_grandchild])
    assert cell.count_semantic_cells() == 4


def test_count_bytes():
    """Test count_bytes method."""
    # Test with no chunks or children
    cell = SemanticCellModel()
    assert cell.count_bytes() == 0

    # Test with chunks
    chunk_data = {
        "GUID": "chunk-guid",
        "Content": "Hello",
        "Length": 5,
    }
    cell = SemanticCellModel(Chunks=[chunk_data])
    assert cell.count_bytes() == 5

    # Test with multiple chunks
    chunk_data2 = {
        "GUID": "chunk-guid-2",
        "Content": "World",
        "Length": 5,
    }
    cell = SemanticCellModel(Chunks=[chunk_data, chunk_data2])
    assert cell.count_bytes() == 10

    # Test with children
    child_data = {
        "GUID": "child-guid",
        "Chunks": [chunk_data],
    }
    cell = SemanticCellModel(Children=[child_data])
    assert cell.count_bytes() == 5

    # Test with both chunks and children
    cell = SemanticCellModel(Chunks=[chunk_data2], Children=[child_data])
    assert cell.count_bytes() == 10


def test_count_embeddings_list():
    """Test count_embeddings_list class method."""
    # Test with None
    assert SemanticCellModel.count_embeddings_list(None) == 0

    # Test with empty list
    assert SemanticCellModel.count_embeddings_list([]) == 0

    # Test with cells containing embeddings
    chunk_data = {
        "GUID": "chunk-guid",
        "Content": "Test content",
        "Embeddings": [0.1, 0.2, 0.3],
    }
    cell_data = {
        "GUID": "cell-guid",
        "Chunks": [chunk_data],
    }
    cells = [SemanticCellModel(**cell_data)]
    assert SemanticCellModel.count_embeddings_list(cells) == 3

    # Test with multiple cells
    cell_data2 = {
        "GUID": "cell-guid-2",
        "Chunks": [chunk_data],
    }
    cells = [SemanticCellModel(**cell_data), SemanticCellModel(**cell_data2)]
    assert SemanticCellModel.count_embeddings_list(cells) == 6


def test_count_semantic_cells_list():
    """Test count_semantic_cells_list class method."""
    # Test with None
    assert SemanticCellModel.count_semantic_cells_list(None) == 0

    # Test with empty list
    assert SemanticCellModel.count_semantic_cells_list([]) == 0

    # Test with single cell
    cell_data = {
        "GUID": "cell-guid",
        "CellType": "Text",
    }
    cells = [SemanticCellModel(**cell_data)]
    assert SemanticCellModel.count_semantic_cells_list(cells) == 1

    # Test with cells having children
    child_data = {
        "GUID": "child-guid",
        "CellType": "Text",
    }
    cell_data_with_child = {
        "GUID": "cell-guid",
        "CellType": "Text",
        "Children": [child_data],
    }
    cells = [SemanticCellModel(**cell_data_with_child)]
    assert SemanticCellModel.count_semantic_cells_list(cells) == 2

    # Test with multiple cells
    cells = [SemanticCellModel(**cell_data), SemanticCellModel(**cell_data_with_child)]
    assert SemanticCellModel.count_semantic_cells_list(cells) == 3


def test_count_semantic_chunks_list():
    """Test count_semantic_chunks_list class method."""
    # Test with None
    assert SemanticCellModel.count_semantic_chunks_list(None) == 0

    # Test with empty list
    assert SemanticCellModel.count_semantic_chunks_list([]) == 0

    # Test with cells containing chunks
    chunk_data = {
        "GUID": "chunk-guid",
        "Content": "Test content",
    }
    cell_data = {
        "GUID": "cell-guid",
        "Chunks": [chunk_data],
    }
    cells = [SemanticCellModel(**cell_data)]
    assert SemanticCellModel.count_semantic_chunks_list(cells) == 1

    # Test with cells having children with chunks
    child_data = {
        "GUID": "child-guid",
        "Chunks": [chunk_data],
    }
    cell_data_with_child = {
        "GUID": "cell-guid",
        "Chunks": [chunk_data],
        "Children": [child_data],
    }
    cells = [SemanticCellModel(**cell_data_with_child)]
    assert SemanticCellModel.count_semantic_chunks_list(cells) == 2

    # Test with multiple cells
    cells = [SemanticCellModel(**cell_data), SemanticCellModel(**cell_data_with_child)]
    assert SemanticCellModel.count_semantic_chunks_list(cells) == 3


def test_count_bytes_list():
    """Test count_bytes_list class method."""
    # Test with None
    assert SemanticCellModel.count_bytes_list(None) == 0

    # Test with empty list
    assert SemanticCellModel.count_bytes_list([]) == 0

    # Test with cells containing chunks
    chunk_data = {
        "GUID": "chunk-guid",
        "Content": "Hello",
        "Length": 5,
    }
    cell_data = {
        "GUID": "cell-guid",
        "Chunks": [chunk_data],
    }
    cells = [SemanticCellModel(**cell_data)]
    assert SemanticCellModel.count_bytes_list(cells) == 5

    # Test with multiple cells
    cell_data2 = {
        "GUID": "cell-guid-2",
        "Chunks": [chunk_data],
    }
    cells = [SemanticCellModel(**cell_data), SemanticCellModel(**cell_data2)]
    assert SemanticCellModel.count_bytes_list(cells) == 10


def test_additional_field_properties():
    """Test additional field properties like binary, content, lists."""
    # Test binary field
    binary_data = b"binary content"
    cell = SemanticCellModel(Binary=binary_data)
    assert cell.binary == binary_data

    # Test content field
    content = "Some text content"
    cell = SemanticCellModel(Content=content)
    assert cell.content == content

    # Test unordered list
    unordered_items = ["item1", "item2", "item3"]
    cell = SemanticCellModel(UnorderedList=unordered_items)
    assert cell.unordered_list == unordered_items

    # Test ordered list
    ordered_items = ["first", "second", "third"]
    cell = SemanticCellModel(OrderedList=ordered_items)
    assert cell.ordered_list == ordered_items

    # Test hash fields
    cell = SemanticCellModel(MD5Hash="abc123", SHA1Hash="def456", SHA256Hash="ghi789")
    assert cell.md5_hash == "abc123"
    assert cell.sha1_hash == "def456"
    assert cell.sha256_hash == "ghi789"


def test_complex_nested_structure():
    """Test complex nested structure with multiple levels."""
    # Create a complex structure: parent -> child -> grandchild
    grandchild_chunk = {
        "GUID": "grandchild-chunk",
        "Content": "Grandchild content",
        "Embeddings": [0.1, 0.2],
        "Length": 18,
    }

    grandchild_data = {
        "GUID": "grandchild-guid",
        "CellType": "Text",
        "Chunks": [grandchild_chunk],
    }

    child_chunk = {
        "GUID": "child-chunk",
        "Content": "Child content",
        "Embeddings": [0.3, 0.4, 0.5],
        "Length": 12,
    }

    child_data = {
        "GUID": "child-guid",
        "CellType": "Text",
        "Chunks": [child_chunk],
        "Children": [grandchild_data],
    }

    parent_chunk = {
        "GUID": "parent-chunk",
        "Content": "Parent content",
        "Embeddings": [0.6],
        "Length": 13,
    }

    parent_data = {
        "GUID": "parent-guid",
        "CellType": "Text",
        "Chunks": [parent_chunk],
        "Children": [child_data],
    }

    cell = SemanticCellModel(**parent_data)

    # Test counts
    assert cell.count_embeddings() == 6  # 1 + 3 + 2
    assert cell.count_semantic_cells() == 3  # parent + child + grandchild
    assert cell.count_bytes() == 45  # 14 + 13 + 18 (actual calculated lengths)

    # Test class methods with the complex structure
    cells = [cell]
    assert SemanticCellModel.count_embeddings_list(cells) == 6
    assert SemanticCellModel.count_semantic_cells_list(cells) == 3
    assert SemanticCellModel.count_semantic_chunks_list(cells) == 3
    assert SemanticCellModel.count_bytes_list(cells) == 45
