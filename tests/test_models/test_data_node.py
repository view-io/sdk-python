import pytest
from view_sdk.models.data_node import DataNodeModel
from view_sdk.enums.data_type_enum import DataTypeEnum


class TestDataNodeModel:
    """Test cases for DataNodeModel."""

    def test_init_with_defaults(self):
        """Test initialization with default values."""
        node = DataNodeModel()
        assert node.key is None
        assert node.type_ == DataTypeEnum.Null
        assert node.data is None

    def test_init_with_values(self):
        """Test initialization with provided values."""
        node = DataNodeModel(
            key="test_key", data="test_data", type_=DataTypeEnum.String
        )
        assert node.key == "test_key"
        assert node.data == "test_data"
        assert node.type_ == DataTypeEnum.String

    def test_field_aliases(self):
        """Test that field aliases work correctly."""
        node = DataNodeModel(Key="test_key", Data="test_data", Type=DataTypeEnum.String)
        assert node.key == "test_key"
        assert node.data == "test_data"
        assert node.type_ == DataTypeEnum.String

    def test_empty_key_validation(self):
        """Test that empty keys are rejected."""
        with pytest.raises(ValueError, match="Key must not be empty when provided"):
            DataNodeModel(key="")
        with pytest.raises(ValueError, match="Key must not be empty when provided"):
            DataNodeModel(key="   ")

    @pytest.mark.parametrize(
        "value,expected_type",
        [
            (None, DataTypeEnum.Null),
            ("test", DataTypeEnum.String),
            (42, DataTypeEnum.Integer),
            (2147483648, DataTypeEnum.Long),  # Greater than int32 max
            (-2147483649, DataTypeEnum.Long),  # Less than int32 min
            (3.14, DataTypeEnum.Decimal),
            ("3.14", DataTypeEnum.Decimal),
            (True, DataTypeEnum.Boolean),
            ("true", DataTypeEnum.Boolean),
            ("false", DataTypeEnum.Boolean),
            ("FALSE", DataTypeEnum.Boolean),
        ],
    )
    def test_type_from_value(self, value, expected_type):
        """Test type detection from different value types."""
        assert DataNodeModel.type_from_value(value) == expected_type

    def test_automatic_type_detection(self):
        """Test that type is automatically detected when not provided."""
        test_cases = [
            (42, DataTypeEnum.Integer),
            (3.14, DataTypeEnum.Decimal),
            ("test", DataTypeEnum.String),
            (True, DataTypeEnum.Boolean),
            (None, DataTypeEnum.Null),
            (2147483648, DataTypeEnum.Long),
        ]

        for value, expected_type in test_cases:
            node = DataNodeModel(key="test", data=value)
            assert node.type_ == expected_type, f"Failed for value: {value}"

    def test_type_override(self):
        """Test that explicit type overrides automatic detection."""
        # Even though 42 would normally be detected as Integer,
        # we explicitly set it as String
        node = DataNodeModel(key="test", data=42, type_=DataTypeEnum.String)
        assert node.type_ == DataTypeEnum.String
