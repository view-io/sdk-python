import json
from typing import Optional, TypeVar

import httpx

from .enums.api_error_enum import ApiErrorEnum
from .exceptions import SdkException, get_exception_for_error_code
from .models.api_error_response import ApiErrorResponseModel
from .sdk_logging import log_debug, log_error, log_info, log_warning

T = TypeVar("T", bound="BaseClient")


class BaseClient:
    """
    Base client class for making HTTP requests to the API.

    This class handles authentication, request retries, error handling, and both regular
    HTTP requests and Server-Sent Events (SSE) requests.

    Attributes:
        base_url (str): The base URL for all API requests.
        access_key (str): The API access key for authentication.
        tenant_guid (Optional[str]): The tenant GUID for multi-tenant operations.
        timeout (int): Request timeout in seconds.
        retries (int): Number of retry attempts for failed requests.
        verbose (bool): Whether to include detailed error information.
        client (httpx.Client): The underlying HTTP client.
    """

    def __init__(
        self,
        base_url: str,
        access_key: str,
        tenant_guid: Optional[str] = None,
        timeout: int = 10,
        retries: int = 3,
        verbose: bool = False,
    ):
        """
        Initialize a new BaseClient instance.

        Args:
            base_url (str): The base URL for all API requests.
            access_key (str): The API access key for authentication.
            tenant_guid (Optional[str], optional): The tenant GUID for multi-tenant operations. Defaults to None.
            timeout (int, optional): Request timeout in seconds. Defaults to 10.
            retries (int, optional): Number of retry attempts for failed requests. Defaults to 3.
            verbose (bool, optional): Whether to include detailed error information. Defaults to False.
        """
        self.base_url = base_url
        self.access_key = access_key
        self.tenant_guid = tenant_guid
        self.timeout = timeout
        self.retries = retries
        self.client = httpx.Client(base_url=self.base_url, timeout=self.timeout)
        self.verbose = verbose
        log_info(
            f"Initialized BaseClient with base_url: {base_url}, timeout: {timeout}, retries: {retries}, verbose: {verbose}"
        )

    def _get_headers(self):
        """
        Generate the default headers for API requests.

        Returns:
            dict: A dictionary containing the authorization and content-type headers.
        """
        return {
            "Authorization": f"Bearer {self.access_key}",
            "Content-Type": "application/json",
        }

    def request(self, method: str, url: str, **kwargs):
        """
        Make an HTTP request to the API with automatic retries and error handling.

        Args:
            method (str): The HTTP method to use (GET, POST, PUT, DELETE, etc.).
            url (str): The URL to send the request to.
            **kwargs: Additional arguments to pass to the underlying httpx request.
                - headers (dict, optional): Additional headers for the request.
                - data (dict, optional): The data to be sent in the request body.

        Returns:
            dict: The JSON response from the API if the response has content, None otherwise.

        Raises:
            SdkException: If the request fails after all retries.
            Various exceptions from get_exception_for_error_code based on the API error response.
        """
        # Get default headers and update with any existing headers from kwargs
        headers = self._get_headers()
        if "headers" in kwargs:
            headers.update(kwargs["headers"])
        kwargs["headers"] = headers

        log_info(
            f"Making {method} request to URL: {url} with headers: {headers} and kwargs: {kwargs}"
        )

        for attempt in range(self.retries):
            try:
                response = self.client.request(method, url, **kwargs)
                response.raise_for_status()
                log_info(f"Request successful: {response.status_code}")
                log_debug(f"Response: {response.text}")
                # Handle cases where the response may not have a body (e.g., HEAD requests)
                return response.json() if response.content else None
            except json.JSONDecodeError:
                return response.content
            except httpx.HTTPStatusError as e:
                try:
                    # Check if response is JSON before trying to parse it
                    if e.response.headers.get("Content-Type") == "application/json":
                        error_response = ApiErrorResponseModel(**e.response.json())
                        log_error(
                            f"HTTPStatusError: {e.response.status_code} - {error_response.error} - {error_response.description}"
                        )
                        # Pass verbose to get_exception_for_error_code to manage traceback visibility
                        raise get_exception_for_error_code(
                            error_response.error, self.verbose, e
                        )
                    else:
                        log_debug(
                            f"Non-JSON response received from server: {e.response.content}"
                        )
                        log_error("Server responded with non-JSON content.")

                        raise get_exception_for_error_code(
                            ApiErrorEnum.internal_error, self.verbose, e
                        )
                except ValueError:
                    log_debug(f"Failed to parse error response: {e}")
                    log_error("Unexpected error while parsing error response.")

                    raise get_exception_for_error_code(
                        ApiErrorEnum.internal_error, self.verbose, e
                    )
            except httpx.RequestError as e:
                log_warning(f"Request attempt {attempt + 1} failed: {e}")
                if attempt == self.retries - 1:
                    log_error("Max retries reached. Failing request.")
                    raise SdkException(
                        f"Request failed after {self.retries} attempts: {e}"
                    )

        raise SdkException("Max retries reached.")

    def sse_request(self, method: str, url: str, **kwargs):
        """
        Handles Server-Sent Events (SSE) requests and yields events.

        Args:
            method (str): HTTP method to use
            url (str): URL to send the request to
            **kwargs: Additional arguments to pass to the request
                - headers (dict, optional): Additional headers for the request.

        Yields:
            dict: Parsed SSE event data

        Raises:
            SdkException: If the SSE request fails.
            Various exceptions from get_exception_for_error_code based on the API error response.
        """
        headers = kwargs.pop("headers", {})
        headers.update(self._get_headers())
        headers["Accept"] = "text/event-stream"
        kwargs["headers"] = headers

        log_info(f"Making SSE {method} request to URL: {url} with headers: {headers}")

        response = None
        try:
            request = self.client.build_request(method, url, **kwargs)
            response = self.client.send(request, stream=True)
            response.raise_for_status()

            for line in response.iter_lines():
                if not line:
                    continue

                if isinstance(line, bytes):
                    line = line.decode("utf-8")
                if line.startswith("data: "):
                    data = line[6:]  # Remove 'data: ' prefix
                    try:
                        event_data = json.loads(data)
                        log_debug(f"Received SSE event: {event_data}")
                        yield event_data
                    except json.JSONDecodeError as e:
                        log_warning(
                            f"Failed to parse SSE event data: {data}. Error: {e}"
                        )
                        yield data  # Return raw data if JSON parsing fails

        except httpx.HTTPStatusError as e:
            e.response.read()  # Ensure the response content is read
            if e.response.headers.get("Content-Type") == "application/json":
                try:
                    error_data = e.response.json()
                    if "error" in error_data:
                        # Handle unexpected JSON structure
                        log_error(f"Unexpected error: {error_data['error']}")
                        raise SdkException(error_data["error"])
                    else:
                        # Handle expected JSON structure
                        error_response = ApiErrorResponseModel(**error_data)
                        log_error(
                            f"HTTPStatusError: {e.response.status_code} - {error_response.error} - {error_response.description}"
                        )
                        raise get_exception_for_error_code(
                            error_response.error, self.verbose, e
                        )
                except json.JSONDecodeError:
                    log_error("Failed to decode JSON error response.")
                    raise get_exception_for_error_code(
                        ApiErrorEnum.internal_error, self.verbose, e
                    )
            else:
                log_error("Server responded with non-JSON content.")
                raise get_exception_for_error_code(
                    ApiErrorEnum.internal_error, self.verbose, e
                )
        except httpx.RequestError as e:
            log_error(f"SSE request failed: {e}")
            raise get_exception_for_error_code(
                ApiErrorEnum.internal_error, self.verbose, e
            )
        finally:
            if response is not None:
                response.close()

    def close(self):
        """
        Close the HTTP client and release any resources.

        This method should be called when the client is no longer needed to ensure
        proper cleanup of resources.
        """
        log_info("Closing HTTP client.")
        self.client.close()
