"""
Type annotations for amplifybackend service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/type_defs.html)

Usage::

    ```python
    from mypy_boto3_amplifybackend.type_defs import BackendAPIAppSyncAuthSettingsTypeDef

    data: BackendAPIAppSyncAuthSettingsTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    AdditionalConstraintsElementType,
    AuthResourcesType,
    DeliveryMethodType,
    MFAModeType,
    MfaTypesElementType,
    ModeType,
    OAuthGrantTypeType,
    OAuthScopesElementType,
    RequiredSignUpAttributesElementType,
    ResolutionStrategyType,
    SignInMethodType,
    StatusType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BackendAPIAppSyncAuthSettingsTypeDef",
    "BackendAPIAuthTypeTypeDef",
    "BackendAPIConflictResolutionTypeDef",
    "BackendAPIResourceConfigTypeDef",
    "BackendAuthSocialProviderConfigTypeDef",
    "BackendJobRespObjTypeDef",
    "CloneBackendRequestTypeDef",
    "CloneBackendResponseResponseTypeDef",
    "CreateBackendAPIRequestTypeDef",
    "CreateBackendAPIResponseResponseTypeDef",
    "CreateBackendAuthForgotPasswordConfigTypeDef",
    "CreateBackendAuthIdentityPoolConfigTypeDef",
    "CreateBackendAuthMFAConfigTypeDef",
    "CreateBackendAuthOAuthConfigTypeDef",
    "CreateBackendAuthPasswordPolicyConfigTypeDef",
    "CreateBackendAuthRequestTypeDef",
    "CreateBackendAuthResourceConfigTypeDef",
    "CreateBackendAuthResponseResponseTypeDef",
    "CreateBackendAuthUserPoolConfigTypeDef",
    "CreateBackendConfigRequestTypeDef",
    "CreateBackendConfigResponseResponseTypeDef",
    "CreateBackendRequestTypeDef",
    "CreateBackendResponseResponseTypeDef",
    "CreateTokenRequestTypeDef",
    "CreateTokenResponseResponseTypeDef",
    "DeleteBackendAPIRequestTypeDef",
    "DeleteBackendAPIResponseResponseTypeDef",
    "DeleteBackendAuthRequestTypeDef",
    "DeleteBackendAuthResponseResponseTypeDef",
    "DeleteBackendRequestTypeDef",
    "DeleteBackendResponseResponseTypeDef",
    "DeleteTokenRequestTypeDef",
    "DeleteTokenResponseResponseTypeDef",
    "EmailSettingsTypeDef",
    "GenerateBackendAPIModelsRequestTypeDef",
    "GenerateBackendAPIModelsResponseResponseTypeDef",
    "GetBackendAPIModelsRequestTypeDef",
    "GetBackendAPIModelsResponseResponseTypeDef",
    "GetBackendAPIRequestTypeDef",
    "GetBackendAPIResponseResponseTypeDef",
    "GetBackendAuthRequestTypeDef",
    "GetBackendAuthResponseResponseTypeDef",
    "GetBackendJobRequestTypeDef",
    "GetBackendJobResponseResponseTypeDef",
    "GetBackendRequestTypeDef",
    "GetBackendResponseResponseTypeDef",
    "GetTokenRequestTypeDef",
    "GetTokenResponseResponseTypeDef",
    "ImportBackendAuthRequestTypeDef",
    "ImportBackendAuthResponseResponseTypeDef",
    "ListBackendJobsRequestTypeDef",
    "ListBackendJobsResponseResponseTypeDef",
    "LoginAuthConfigReqObjTypeDef",
    "PaginatorConfigTypeDef",
    "RemoveAllBackendsRequestTypeDef",
    "RemoveAllBackendsResponseResponseTypeDef",
    "RemoveBackendConfigRequestTypeDef",
    "RemoveBackendConfigResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SettingsTypeDef",
    "SmsSettingsTypeDef",
    "SocialProviderSettingsTypeDef",
    "UpdateBackendAPIRequestTypeDef",
    "UpdateBackendAPIResponseResponseTypeDef",
    "UpdateBackendAuthForgotPasswordConfigTypeDef",
    "UpdateBackendAuthIdentityPoolConfigTypeDef",
    "UpdateBackendAuthMFAConfigTypeDef",
    "UpdateBackendAuthOAuthConfigTypeDef",
    "UpdateBackendAuthPasswordPolicyConfigTypeDef",
    "UpdateBackendAuthRequestTypeDef",
    "UpdateBackendAuthResourceConfigTypeDef",
    "UpdateBackendAuthResponseResponseTypeDef",
    "UpdateBackendAuthUserPoolConfigTypeDef",
    "UpdateBackendConfigRequestTypeDef",
    "UpdateBackendConfigResponseResponseTypeDef",
    "UpdateBackendJobRequestTypeDef",
    "UpdateBackendJobResponseResponseTypeDef",
)

BackendAPIAppSyncAuthSettingsTypeDef = TypedDict(
    "BackendAPIAppSyncAuthSettingsTypeDef",
    {
        "CognitoUserPoolId": str,
        "Description": str,
        "ExpirationTime": float,
        "OpenIDAuthTTL": str,
        "OpenIDClientId": str,
        "OpenIDIatTTL": str,
        "OpenIDIssueURL": str,
        "OpenIDProviderName": str,
    },
    total=False,
)

BackendAPIAuthTypeTypeDef = TypedDict(
    "BackendAPIAuthTypeTypeDef",
    {
        "Mode": ModeType,
        "Settings": "BackendAPIAppSyncAuthSettingsTypeDef",
    },
    total=False,
)

BackendAPIConflictResolutionTypeDef = TypedDict(
    "BackendAPIConflictResolutionTypeDef",
    {
        "ResolutionStrategy": ResolutionStrategyType,
    },
    total=False,
)

BackendAPIResourceConfigTypeDef = TypedDict(
    "BackendAPIResourceConfigTypeDef",
    {
        "AdditionalAuthTypes": List["BackendAPIAuthTypeTypeDef"],
        "ApiName": str,
        "ConflictResolution": "BackendAPIConflictResolutionTypeDef",
        "DefaultAuthType": "BackendAPIAuthTypeTypeDef",
        "Service": str,
        "TransformSchema": str,
    },
    total=False,
)

BackendAuthSocialProviderConfigTypeDef = TypedDict(
    "BackendAuthSocialProviderConfigTypeDef",
    {
        "ClientId": str,
        "ClientSecret": str,
    },
    total=False,
)

_RequiredBackendJobRespObjTypeDef = TypedDict(
    "_RequiredBackendJobRespObjTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
    },
)
_OptionalBackendJobRespObjTypeDef = TypedDict(
    "_OptionalBackendJobRespObjTypeDef",
    {
        "CreateTime": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "UpdateTime": str,
    },
    total=False,
)


class BackendJobRespObjTypeDef(
    _RequiredBackendJobRespObjTypeDef, _OptionalBackendJobRespObjTypeDef
):
    pass


CloneBackendRequestTypeDef = TypedDict(
    "CloneBackendRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "TargetEnvironmentName": str,
    },
)

CloneBackendResponseResponseTypeDef = TypedDict(
    "CloneBackendResponseResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBackendAPIRequestTypeDef = TypedDict(
    "CreateBackendAPIRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": "BackendAPIResourceConfigTypeDef",
        "ResourceName": str,
    },
)

CreateBackendAPIResponseResponseTypeDef = TypedDict(
    "CreateBackendAPIResponseResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBackendAuthForgotPasswordConfigTypeDef = TypedDict(
    "_RequiredCreateBackendAuthForgotPasswordConfigTypeDef",
    {
        "DeliveryMethod": DeliveryMethodType,
    },
)
_OptionalCreateBackendAuthForgotPasswordConfigTypeDef = TypedDict(
    "_OptionalCreateBackendAuthForgotPasswordConfigTypeDef",
    {
        "EmailSettings": "EmailSettingsTypeDef",
        "SmsSettings": "SmsSettingsTypeDef",
    },
    total=False,
)


class CreateBackendAuthForgotPasswordConfigTypeDef(
    _RequiredCreateBackendAuthForgotPasswordConfigTypeDef,
    _OptionalCreateBackendAuthForgotPasswordConfigTypeDef,
):
    pass


CreateBackendAuthIdentityPoolConfigTypeDef = TypedDict(
    "CreateBackendAuthIdentityPoolConfigTypeDef",
    {
        "IdentityPoolName": str,
        "UnauthenticatedLogin": bool,
    },
)

_RequiredCreateBackendAuthMFAConfigTypeDef = TypedDict(
    "_RequiredCreateBackendAuthMFAConfigTypeDef",
    {
        "MFAMode": MFAModeType,
    },
)
_OptionalCreateBackendAuthMFAConfigTypeDef = TypedDict(
    "_OptionalCreateBackendAuthMFAConfigTypeDef",
    {
        "Settings": "SettingsTypeDef",
    },
    total=False,
)


class CreateBackendAuthMFAConfigTypeDef(
    _RequiredCreateBackendAuthMFAConfigTypeDef, _OptionalCreateBackendAuthMFAConfigTypeDef
):
    pass


_RequiredCreateBackendAuthOAuthConfigTypeDef = TypedDict(
    "_RequiredCreateBackendAuthOAuthConfigTypeDef",
    {
        "OAuthGrantType": OAuthGrantTypeType,
        "OAuthScopes": List[OAuthScopesElementType],
        "RedirectSignInURIs": List[str],
        "RedirectSignOutURIs": List[str],
    },
)
_OptionalCreateBackendAuthOAuthConfigTypeDef = TypedDict(
    "_OptionalCreateBackendAuthOAuthConfigTypeDef",
    {
        "DomainPrefix": str,
        "SocialProviderSettings": "SocialProviderSettingsTypeDef",
    },
    total=False,
)


class CreateBackendAuthOAuthConfigTypeDef(
    _RequiredCreateBackendAuthOAuthConfigTypeDef, _OptionalCreateBackendAuthOAuthConfigTypeDef
):
    pass


_RequiredCreateBackendAuthPasswordPolicyConfigTypeDef = TypedDict(
    "_RequiredCreateBackendAuthPasswordPolicyConfigTypeDef",
    {
        "MinimumLength": float,
    },
)
_OptionalCreateBackendAuthPasswordPolicyConfigTypeDef = TypedDict(
    "_OptionalCreateBackendAuthPasswordPolicyConfigTypeDef",
    {
        "AdditionalConstraints": List[AdditionalConstraintsElementType],
    },
    total=False,
)


class CreateBackendAuthPasswordPolicyConfigTypeDef(
    _RequiredCreateBackendAuthPasswordPolicyConfigTypeDef,
    _OptionalCreateBackendAuthPasswordPolicyConfigTypeDef,
):
    pass


CreateBackendAuthRequestTypeDef = TypedDict(
    "CreateBackendAuthRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": "CreateBackendAuthResourceConfigTypeDef",
        "ResourceName": str,
    },
)

_RequiredCreateBackendAuthResourceConfigTypeDef = TypedDict(
    "_RequiredCreateBackendAuthResourceConfigTypeDef",
    {
        "AuthResources": AuthResourcesType,
        "Service": Literal["COGNITO"],
        "UserPoolConfigs": "CreateBackendAuthUserPoolConfigTypeDef",
    },
)
_OptionalCreateBackendAuthResourceConfigTypeDef = TypedDict(
    "_OptionalCreateBackendAuthResourceConfigTypeDef",
    {
        "IdentityPoolConfigs": "CreateBackendAuthIdentityPoolConfigTypeDef",
    },
    total=False,
)


class CreateBackendAuthResourceConfigTypeDef(
    _RequiredCreateBackendAuthResourceConfigTypeDef, _OptionalCreateBackendAuthResourceConfigTypeDef
):
    pass


CreateBackendAuthResponseResponseTypeDef = TypedDict(
    "CreateBackendAuthResponseResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBackendAuthUserPoolConfigTypeDef = TypedDict(
    "_RequiredCreateBackendAuthUserPoolConfigTypeDef",
    {
        "RequiredSignUpAttributes": List[RequiredSignUpAttributesElementType],
        "SignInMethod": SignInMethodType,
        "UserPoolName": str,
    },
)
_OptionalCreateBackendAuthUserPoolConfigTypeDef = TypedDict(
    "_OptionalCreateBackendAuthUserPoolConfigTypeDef",
    {
        "ForgotPassword": "CreateBackendAuthForgotPasswordConfigTypeDef",
        "Mfa": "CreateBackendAuthMFAConfigTypeDef",
        "OAuth": "CreateBackendAuthOAuthConfigTypeDef",
        "PasswordPolicy": "CreateBackendAuthPasswordPolicyConfigTypeDef",
    },
    total=False,
)


class CreateBackendAuthUserPoolConfigTypeDef(
    _RequiredCreateBackendAuthUserPoolConfigTypeDef, _OptionalCreateBackendAuthUserPoolConfigTypeDef
):
    pass


_RequiredCreateBackendConfigRequestTypeDef = TypedDict(
    "_RequiredCreateBackendConfigRequestTypeDef",
    {
        "AppId": str,
    },
)
_OptionalCreateBackendConfigRequestTypeDef = TypedDict(
    "_OptionalCreateBackendConfigRequestTypeDef",
    {
        "BackendManagerAppId": str,
    },
    total=False,
)


class CreateBackendConfigRequestTypeDef(
    _RequiredCreateBackendConfigRequestTypeDef, _OptionalCreateBackendConfigRequestTypeDef
):
    pass


CreateBackendConfigResponseResponseTypeDef = TypedDict(
    "CreateBackendConfigResponseResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBackendRequestTypeDef = TypedDict(
    "_RequiredCreateBackendRequestTypeDef",
    {
        "AppId": str,
        "AppName": str,
        "BackendEnvironmentName": str,
    },
)
_OptionalCreateBackendRequestTypeDef = TypedDict(
    "_OptionalCreateBackendRequestTypeDef",
    {
        "ResourceConfig": Dict[str, Any],
        "ResourceName": str,
    },
    total=False,
)


class CreateBackendRequestTypeDef(
    _RequiredCreateBackendRequestTypeDef, _OptionalCreateBackendRequestTypeDef
):
    pass


CreateBackendResponseResponseTypeDef = TypedDict(
    "CreateBackendResponseResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTokenRequestTypeDef = TypedDict(
    "CreateTokenRequestTypeDef",
    {
        "AppId": str,
    },
)

CreateTokenResponseResponseTypeDef = TypedDict(
    "CreateTokenResponseResponseTypeDef",
    {
        "AppId": str,
        "ChallengeCode": str,
        "SessionId": str,
        "Ttl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteBackendAPIRequestTypeDef = TypedDict(
    "_RequiredDeleteBackendAPIRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)
_OptionalDeleteBackendAPIRequestTypeDef = TypedDict(
    "_OptionalDeleteBackendAPIRequestTypeDef",
    {
        "ResourceConfig": "BackendAPIResourceConfigTypeDef",
    },
    total=False,
)


class DeleteBackendAPIRequestTypeDef(
    _RequiredDeleteBackendAPIRequestTypeDef, _OptionalDeleteBackendAPIRequestTypeDef
):
    pass


DeleteBackendAPIResponseResponseTypeDef = TypedDict(
    "DeleteBackendAPIResponseResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackendAuthRequestTypeDef = TypedDict(
    "DeleteBackendAuthRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)

DeleteBackendAuthResponseResponseTypeDef = TypedDict(
    "DeleteBackendAuthResponseResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackendRequestTypeDef = TypedDict(
    "DeleteBackendRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
    },
)

DeleteBackendResponseResponseTypeDef = TypedDict(
    "DeleteBackendResponseResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTokenRequestTypeDef = TypedDict(
    "DeleteTokenRequestTypeDef",
    {
        "AppId": str,
        "SessionId": str,
    },
)

DeleteTokenResponseResponseTypeDef = TypedDict(
    "DeleteTokenResponseResponseTypeDef",
    {
        "IsSuccess": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EmailSettingsTypeDef = TypedDict(
    "EmailSettingsTypeDef",
    {
        "EmailMessage": str,
        "EmailSubject": str,
    },
    total=False,
)

GenerateBackendAPIModelsRequestTypeDef = TypedDict(
    "GenerateBackendAPIModelsRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)

GenerateBackendAPIModelsResponseResponseTypeDef = TypedDict(
    "GenerateBackendAPIModelsResponseResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackendAPIModelsRequestTypeDef = TypedDict(
    "GetBackendAPIModelsRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)

GetBackendAPIModelsResponseResponseTypeDef = TypedDict(
    "GetBackendAPIModelsResponseResponseTypeDef",
    {
        "Models": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBackendAPIRequestTypeDef = TypedDict(
    "_RequiredGetBackendAPIRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)
_OptionalGetBackendAPIRequestTypeDef = TypedDict(
    "_OptionalGetBackendAPIRequestTypeDef",
    {
        "ResourceConfig": "BackendAPIResourceConfigTypeDef",
    },
    total=False,
)


class GetBackendAPIRequestTypeDef(
    _RequiredGetBackendAPIRequestTypeDef, _OptionalGetBackendAPIRequestTypeDef
):
    pass


GetBackendAPIResponseResponseTypeDef = TypedDict(
    "GetBackendAPIResponseResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "ResourceConfig": "BackendAPIResourceConfigTypeDef",
        "ResourceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackendAuthRequestTypeDef = TypedDict(
    "GetBackendAuthRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)

GetBackendAuthResponseResponseTypeDef = TypedDict(
    "GetBackendAuthResponseResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "ResourceConfig": "CreateBackendAuthResourceConfigTypeDef",
        "ResourceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackendJobRequestTypeDef = TypedDict(
    "GetBackendJobRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
    },
)

GetBackendJobResponseResponseTypeDef = TypedDict(
    "GetBackendJobResponseResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "CreateTime": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "UpdateTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBackendRequestTypeDef = TypedDict(
    "_RequiredGetBackendRequestTypeDef",
    {
        "AppId": str,
    },
)
_OptionalGetBackendRequestTypeDef = TypedDict(
    "_OptionalGetBackendRequestTypeDef",
    {
        "BackendEnvironmentName": str,
    },
    total=False,
)


class GetBackendRequestTypeDef(
    _RequiredGetBackendRequestTypeDef, _OptionalGetBackendRequestTypeDef
):
    pass


GetBackendResponseResponseTypeDef = TypedDict(
    "GetBackendResponseResponseTypeDef",
    {
        "AmplifyMetaConfig": str,
        "AppId": str,
        "AppName": str,
        "BackendEnvironmentList": List[str],
        "BackendEnvironmentName": str,
        "Error": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTokenRequestTypeDef = TypedDict(
    "GetTokenRequestTypeDef",
    {
        "AppId": str,
        "SessionId": str,
    },
)

GetTokenResponseResponseTypeDef = TypedDict(
    "GetTokenResponseResponseTypeDef",
    {
        "AppId": str,
        "ChallengeCode": str,
        "SessionId": str,
        "Ttl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportBackendAuthRequestTypeDef = TypedDict(
    "_RequiredImportBackendAuthRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "NativeClientId": str,
        "UserPoolId": str,
        "WebClientId": str,
    },
)
_OptionalImportBackendAuthRequestTypeDef = TypedDict(
    "_OptionalImportBackendAuthRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
    total=False,
)


class ImportBackendAuthRequestTypeDef(
    _RequiredImportBackendAuthRequestTypeDef, _OptionalImportBackendAuthRequestTypeDef
):
    pass


ImportBackendAuthResponseResponseTypeDef = TypedDict(
    "ImportBackendAuthResponseResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBackendJobsRequestTypeDef = TypedDict(
    "_RequiredListBackendJobsRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
    },
)
_OptionalListBackendJobsRequestTypeDef = TypedDict(
    "_OptionalListBackendJobsRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": int,
        "NextToken": str,
        "Operation": str,
        "Status": str,
    },
    total=False,
)


class ListBackendJobsRequestTypeDef(
    _RequiredListBackendJobsRequestTypeDef, _OptionalListBackendJobsRequestTypeDef
):
    pass


ListBackendJobsResponseResponseTypeDef = TypedDict(
    "ListBackendJobsResponseResponseTypeDef",
    {
        "Jobs": List["BackendJobRespObjTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoginAuthConfigReqObjTypeDef = TypedDict(
    "LoginAuthConfigReqObjTypeDef",
    {
        "AwsCognitoIdentityPoolId": str,
        "AwsCognitoRegion": str,
        "AwsUserPoolsId": str,
        "AwsUserPoolsWebClientId": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredRemoveAllBackendsRequestTypeDef = TypedDict(
    "_RequiredRemoveAllBackendsRequestTypeDef",
    {
        "AppId": str,
    },
)
_OptionalRemoveAllBackendsRequestTypeDef = TypedDict(
    "_OptionalRemoveAllBackendsRequestTypeDef",
    {
        "CleanAmplifyApp": bool,
    },
    total=False,
)


class RemoveAllBackendsRequestTypeDef(
    _RequiredRemoveAllBackendsRequestTypeDef, _OptionalRemoveAllBackendsRequestTypeDef
):
    pass


RemoveAllBackendsResponseResponseTypeDef = TypedDict(
    "RemoveAllBackendsResponseResponseTypeDef",
    {
        "AppId": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveBackendConfigRequestTypeDef = TypedDict(
    "RemoveBackendConfigRequestTypeDef",
    {
        "AppId": str,
    },
)

RemoveBackendConfigResponseResponseTypeDef = TypedDict(
    "RemoveBackendConfigResponseResponseTypeDef",
    {
        "Error": str,
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

SettingsTypeDef = TypedDict(
    "SettingsTypeDef",
    {
        "MfaTypes": List[MfaTypesElementType],
        "SmsMessage": str,
    },
    total=False,
)

SmsSettingsTypeDef = TypedDict(
    "SmsSettingsTypeDef",
    {
        "SmsMessage": str,
    },
    total=False,
)

SocialProviderSettingsTypeDef = TypedDict(
    "SocialProviderSettingsTypeDef",
    {
        "Facebook": "BackendAuthSocialProviderConfigTypeDef",
        "Google": "BackendAuthSocialProviderConfigTypeDef",
        "LoginWithAmazon": "BackendAuthSocialProviderConfigTypeDef",
    },
    total=False,
)

_RequiredUpdateBackendAPIRequestTypeDef = TypedDict(
    "_RequiredUpdateBackendAPIRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)
_OptionalUpdateBackendAPIRequestTypeDef = TypedDict(
    "_OptionalUpdateBackendAPIRequestTypeDef",
    {
        "ResourceConfig": "BackendAPIResourceConfigTypeDef",
    },
    total=False,
)


class UpdateBackendAPIRequestTypeDef(
    _RequiredUpdateBackendAPIRequestTypeDef, _OptionalUpdateBackendAPIRequestTypeDef
):
    pass


UpdateBackendAPIResponseResponseTypeDef = TypedDict(
    "UpdateBackendAPIResponseResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBackendAuthForgotPasswordConfigTypeDef = TypedDict(
    "UpdateBackendAuthForgotPasswordConfigTypeDef",
    {
        "DeliveryMethod": DeliveryMethodType,
        "EmailSettings": "EmailSettingsTypeDef",
        "SmsSettings": "SmsSettingsTypeDef",
    },
    total=False,
)

UpdateBackendAuthIdentityPoolConfigTypeDef = TypedDict(
    "UpdateBackendAuthIdentityPoolConfigTypeDef",
    {
        "UnauthenticatedLogin": bool,
    },
    total=False,
)

UpdateBackendAuthMFAConfigTypeDef = TypedDict(
    "UpdateBackendAuthMFAConfigTypeDef",
    {
        "MFAMode": MFAModeType,
        "Settings": "SettingsTypeDef",
    },
    total=False,
)

UpdateBackendAuthOAuthConfigTypeDef = TypedDict(
    "UpdateBackendAuthOAuthConfigTypeDef",
    {
        "DomainPrefix": str,
        "OAuthGrantType": OAuthGrantTypeType,
        "OAuthScopes": List[OAuthScopesElementType],
        "RedirectSignInURIs": List[str],
        "RedirectSignOutURIs": List[str],
        "SocialProviderSettings": "SocialProviderSettingsTypeDef",
    },
    total=False,
)

UpdateBackendAuthPasswordPolicyConfigTypeDef = TypedDict(
    "UpdateBackendAuthPasswordPolicyConfigTypeDef",
    {
        "AdditionalConstraints": List[AdditionalConstraintsElementType],
        "MinimumLength": float,
    },
    total=False,
)

UpdateBackendAuthRequestTypeDef = TypedDict(
    "UpdateBackendAuthRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": "UpdateBackendAuthResourceConfigTypeDef",
        "ResourceName": str,
    },
)

_RequiredUpdateBackendAuthResourceConfigTypeDef = TypedDict(
    "_RequiredUpdateBackendAuthResourceConfigTypeDef",
    {
        "AuthResources": AuthResourcesType,
        "Service": Literal["COGNITO"],
        "UserPoolConfigs": "UpdateBackendAuthUserPoolConfigTypeDef",
    },
)
_OptionalUpdateBackendAuthResourceConfigTypeDef = TypedDict(
    "_OptionalUpdateBackendAuthResourceConfigTypeDef",
    {
        "IdentityPoolConfigs": "UpdateBackendAuthIdentityPoolConfigTypeDef",
    },
    total=False,
)


class UpdateBackendAuthResourceConfigTypeDef(
    _RequiredUpdateBackendAuthResourceConfigTypeDef, _OptionalUpdateBackendAuthResourceConfigTypeDef
):
    pass


UpdateBackendAuthResponseResponseTypeDef = TypedDict(
    "UpdateBackendAuthResponseResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBackendAuthUserPoolConfigTypeDef = TypedDict(
    "UpdateBackendAuthUserPoolConfigTypeDef",
    {
        "ForgotPassword": "UpdateBackendAuthForgotPasswordConfigTypeDef",
        "Mfa": "UpdateBackendAuthMFAConfigTypeDef",
        "OAuth": "UpdateBackendAuthOAuthConfigTypeDef",
        "PasswordPolicy": "UpdateBackendAuthPasswordPolicyConfigTypeDef",
    },
    total=False,
)

_RequiredUpdateBackendConfigRequestTypeDef = TypedDict(
    "_RequiredUpdateBackendConfigRequestTypeDef",
    {
        "AppId": str,
    },
)
_OptionalUpdateBackendConfigRequestTypeDef = TypedDict(
    "_OptionalUpdateBackendConfigRequestTypeDef",
    {
        "LoginAuthConfig": "LoginAuthConfigReqObjTypeDef",
    },
    total=False,
)


class UpdateBackendConfigRequestTypeDef(
    _RequiredUpdateBackendConfigRequestTypeDef, _OptionalUpdateBackendConfigRequestTypeDef
):
    pass


UpdateBackendConfigResponseResponseTypeDef = TypedDict(
    "UpdateBackendConfigResponseResponseTypeDef",
    {
        "AppId": str,
        "BackendManagerAppId": str,
        "Error": str,
        "LoginAuthConfig": "LoginAuthConfigReqObjTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateBackendJobRequestTypeDef = TypedDict(
    "_RequiredUpdateBackendJobRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
    },
)
_OptionalUpdateBackendJobRequestTypeDef = TypedDict(
    "_OptionalUpdateBackendJobRequestTypeDef",
    {
        "Operation": str,
        "Status": str,
    },
    total=False,
)


class UpdateBackendJobRequestTypeDef(
    _RequiredUpdateBackendJobRequestTypeDef, _OptionalUpdateBackendJobRequestTypeDef
):
    pass


UpdateBackendJobResponseResponseTypeDef = TypedDict(
    "UpdateBackendJobResponseResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "CreateTime": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "UpdateTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
