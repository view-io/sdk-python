from typing import List

from ...models.authentication_token import AuthenticationTokenModel
from ...models.tenant_metadata import TenantMetadataModel
from ...sdk_configuration import Service, get_client
from ...utils.url_helper import _get_url_v1


class Authentication:
    SERVICE = Service.DEFAULT
    REQUIRES_TENANT = False

    @classmethod
    def retrieve_tenants_for_email(cls, email: str) -> List[TenantMetadataModel]:
        """
        Retrieves tenants associated with the given email.

        Args:
            email (str): The email address to retrieve tenants for.

        Returns:
            List[TenantMetadataModel]:The list of tenants associated with the email.
        """
        client = get_client(cls.SERVICE)
        headers = {"x-email": email}
        url = _get_url_v1(cls, "token", "tenants")
        response = client.request("GET", url, headers=headers)
        return [TenantMetadataModel.model_validate(**tenant) for tenant in response]

    @classmethod
    def generate_authentication_token(
        cls, email: str, password: str, tenant_guid: str
    ) -> AuthenticationTokenModel:
        """
        Generates an authentication token for the given email, password, and tenant GUID.

        Args:
            email (str): The email address.
            password (str): The password.
            tenant_guid (str): The tenant GUID.

        Returns:
            AuthenticationTokenModel: The authentication token model.
        """
        client = get_client(cls.SERVICE)
        headers = {
            "x-email": email,
            "x-password": password,
            "x-tenant-guid": tenant_guid,
        }
        url = _get_url_v1(cls, "token")
        response = client.request("GET", url, headers=headers)
        return AuthenticationTokenModel.model_validate(response)

    @classmethod
    def generate_authentication_token_sha_256(
        cls, email: str, password_sha256: str, tenant_guid: str
    ) -> AuthenticationTokenModel:
        """
        Generates an authentication token for the given email, SHA-256 hashed password, and tenant GUID.

        Args:
            email (str): The email address.
            password_sha256 (str): The SHA-256 hashed password.
            tenant_guid (str): The tenant GUID.

        Returns:
            AuthenticationTokenModel: The authentication token model.
        """
        client = get_client(cls.SERVICE)
        headers = {
            "x-email": email,
            "x-password-sha256": password_sha256,
            "x-tenant-guid": tenant_guid,
        }
        url = _get_url_v1(cls, "token")
        response = client.request("GET", url, headers=headers)
        return AuthenticationTokenModel.model_validate(response)

    # TODO: is this needed in user SDK?
    # @classmethod
    # def generate_administrator_token(cls, email, password):
    #     pass

    @classmethod
    def validate_authentication_token(cls, token: str) -> AuthenticationTokenModel:
        """
        Validates the given authentication token.

        Args:
            token (str): The authentication token.

        Returns:
            dict: The validation response.
        """
        client = get_client(cls.SERVICE)
        headers = {"x-token": token}
        url = _get_url_v1(cls, "token", "validate")
        response = client.request("GET", url, headers=headers)
        return AuthenticationTokenModel.model_validate(response)

    @classmethod
    def retrieve_token_details(cls, token: str):
        """
        Retrieves details for the given authentication token.

        Args:
            token (str): The authentication token.

        Returns:
            dict: The token details.
        """
        client = get_client(cls.SERVICE)
        headers = {"x-token": token}
        url = _get_url_v1(cls, "token", "details")
        response = client.request("GET", url, headers=headers)
        return AuthenticationTokenModel.model_validate(response)

    @classmethod
    def retrieve_administrator_token(cls, email: str, password: str):
        """
        Retrieves an administrator token for the given email and password.

        Args:
            email (str): The email address.
            password (str): The password.

        Returns:
            AuthenticationTokenModel: The authentication token model.
        """
        client = get_client(cls.SERVICE)
        headers = {"x-email": email, "x-password": password}
        url = _get_url_v1(cls, "token")
        response = client.request("GET", url, headers=headers)
        return AuthenticationTokenModel.model_validate(response)

    @classmethod
    def retrieve_administrator_token_sha_256(cls, email: str, password_sha256: str):
        """
        Retrieves an administrator token for the given email and SHA-256 hashed password.

        Args:
            email (str): The email address.
            password_sha256 (str): The SHA-256 hashed password.

        Returns:
            AuthenticationTokenModel: The authentication token model.
        """
        client = get_client(cls.SERVICE)
        headers = {"x-email": email, "x-password-sha256": password_sha256}
        url = _get_url_v1(cls, "token")
        response = client.request("GET", url, headers=headers)
        return AuthenticationTokenModel.model_validate(response)
