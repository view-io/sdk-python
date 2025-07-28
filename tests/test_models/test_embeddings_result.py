from view_sdk.models.embeddings_result import EmbeddingsResult
from view_sdk.models.embeddings_map import EmbeddingsMap


def test_embeddings_result_defaults():
    result = EmbeddingsResult()
    assert result.success is False
    assert result.status_code == 200
    assert result.model is None
    assert result.result == []


def test_embeddings_result_with_values():
    emb_map = EmbeddingsMap()
    result = EmbeddingsResult(
        success=True, status_code=201, model="test-model", result=[emb_map]
    )
    assert result.success is True
    assert result.status_code == 201
    assert result.model == "test-model"
    assert result.result == [emb_map]


def test_embeddings_result_result_none():
    # Should coerce None to []
    result = EmbeddingsResult(result=None)
    assert result.result == []


def test_embeddings_result_aliases():
    # Test that aliases work for input and output
    data = {"Success": True, "StatusCode": 201, "Model": "test-model", "Result": []}
    result = EmbeddingsResult.model_validate(data)
    assert result.success is True
    assert result.status_code == 201
    assert result.model == "test-model"
    assert result.result == []
    # Output aliases
    dumped = result.model_dump(by_alias=True)
    assert dumped["Success"] is True
    assert dumped["StatusCode"] == 201
    assert dumped["Model"] == "test-model"
    assert dumped["Result"] == []
