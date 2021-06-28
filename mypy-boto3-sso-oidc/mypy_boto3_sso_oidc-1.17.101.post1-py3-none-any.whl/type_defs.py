"""
Type annotations for sso-oidc service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sso_oidc.type_defs import CreateTokenRequestTypeDef

    data: CreateTokenRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateTokenRequestTypeDef",
    "CreateTokenResponseResponseTypeDef",
    "RegisterClientRequestTypeDef",
    "RegisterClientResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "StartDeviceAuthorizationRequestTypeDef",
    "StartDeviceAuthorizationResponseResponseTypeDef",
)

_RequiredCreateTokenRequestTypeDef = TypedDict(
    "_RequiredCreateTokenRequestTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "grantType": str,
        "deviceCode": str,
    },
)
_OptionalCreateTokenRequestTypeDef = TypedDict(
    "_OptionalCreateTokenRequestTypeDef",
    {
        "code": str,
        "refreshToken": str,
        "scope": List[str],
        "redirectUri": str,
    },
    total=False,
)


class CreateTokenRequestTypeDef(
    _RequiredCreateTokenRequestTypeDef, _OptionalCreateTokenRequestTypeDef
):
    pass


CreateTokenResponseResponseTypeDef = TypedDict(
    "CreateTokenResponseResponseTypeDef",
    {
        "accessToken": str,
        "tokenType": str,
        "expiresIn": int,
        "refreshToken": str,
        "idToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterClientRequestTypeDef = TypedDict(
    "_RequiredRegisterClientRequestTypeDef",
    {
        "clientName": str,
        "clientType": str,
    },
)
_OptionalRegisterClientRequestTypeDef = TypedDict(
    "_OptionalRegisterClientRequestTypeDef",
    {
        "scopes": List[str],
    },
    total=False,
)


class RegisterClientRequestTypeDef(
    _RequiredRegisterClientRequestTypeDef, _OptionalRegisterClientRequestTypeDef
):
    pass


RegisterClientResponseResponseTypeDef = TypedDict(
    "RegisterClientResponseResponseTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "clientIdIssuedAt": int,
        "clientSecretExpiresAt": int,
        "authorizationEndpoint": str,
        "tokenEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

StartDeviceAuthorizationRequestTypeDef = TypedDict(
    "StartDeviceAuthorizationRequestTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "startUrl": str,
    },
)

StartDeviceAuthorizationResponseResponseTypeDef = TypedDict(
    "StartDeviceAuthorizationResponseResponseTypeDef",
    {
        "deviceCode": str,
        "userCode": str,
        "verificationUri": str,
        "verificationUriComplete": str,
        "expiresIn": int,
        "interval": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
