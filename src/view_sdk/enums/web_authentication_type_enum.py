from enum import Enum


class WebAuthenticationTypeEnum(str, Enum):
    None_ = "None"
    Basic = "Basic"
    ApiKey = "ApiKey"
    BearerToken = "BearerToken"
