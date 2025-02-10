from typing import Dict, Optional

from pydantic import StrictStr


def get_response_map(model_name: StrictStr) -> Dict[str, Optional[str]]:
    """
    Map the response to the specified response type.

    :param model_name: The name of the model to map the response to.
    :type model_name: BaseModel
    :return: A dictionary mapping the response status code to
    """
    _response_types_map: Dict[str, Optional[str]] = {
        "200": model_name,
        "400": "ApiErrorResponse",
        "401": "ApiErrorResponse",
        "404": "ApiErrorResponse",
        "409": "ApiErrorResponse",
        "413": "ApiErrorResponse",
        "422": "HTTPValidationError",
        "500": "ApiErrorResponse",
    }
    return _response_types_map
