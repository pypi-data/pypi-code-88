"""
Type annotations for cognito-idp service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cognito_idp.type_defs import AccountRecoverySettingTypeTypeDef

    data: AccountRecoverySettingTypeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AccountTakeoverEventActionTypeType,
    AdvancedSecurityModeTypeType,
    AliasAttributeTypeType,
    AttributeDataTypeType,
    AuthFlowTypeType,
    ChallengeNameType,
    ChallengeNameTypeType,
    ChallengeResponseType,
    CompromisedCredentialsEventActionTypeType,
    DefaultEmailOptionTypeType,
    DeliveryMediumTypeType,
    DeviceRememberedStatusTypeType,
    DomainStatusTypeType,
    EmailSendingAccountTypeType,
    EventFilterTypeType,
    EventResponseTypeType,
    EventTypeType,
    ExplicitAuthFlowsTypeType,
    FeedbackValueTypeType,
    IdentityProviderTypeTypeType,
    MessageActionTypeType,
    OAuthFlowTypeType,
    PreventUserExistenceErrorTypesType,
    RecoveryOptionNameTypeType,
    RiskDecisionTypeType,
    RiskLevelTypeType,
    StatusTypeType,
    TimeUnitsTypeType,
    UserImportJobStatusTypeType,
    UsernameAttributeTypeType,
    UserPoolMfaTypeType,
    UserStatusTypeType,
    VerifiedAttributeTypeType,
    VerifySoftwareTokenResponseTypeType,
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
    "AccountRecoverySettingTypeTypeDef",
    "AccountTakeoverActionTypeTypeDef",
    "AccountTakeoverActionsTypeTypeDef",
    "AccountTakeoverRiskConfigurationTypeTypeDef",
    "AddCustomAttributesRequestTypeDef",
    "AdminAddUserToGroupRequestTypeDef",
    "AdminConfirmSignUpRequestTypeDef",
    "AdminCreateUserConfigTypeTypeDef",
    "AdminCreateUserRequestTypeDef",
    "AdminCreateUserResponseResponseTypeDef",
    "AdminDeleteUserAttributesRequestTypeDef",
    "AdminDeleteUserRequestTypeDef",
    "AdminDisableProviderForUserRequestTypeDef",
    "AdminDisableUserRequestTypeDef",
    "AdminEnableUserRequestTypeDef",
    "AdminForgetDeviceRequestTypeDef",
    "AdminGetDeviceRequestTypeDef",
    "AdminGetDeviceResponseResponseTypeDef",
    "AdminGetUserRequestTypeDef",
    "AdminGetUserResponseResponseTypeDef",
    "AdminInitiateAuthRequestTypeDef",
    "AdminInitiateAuthResponseResponseTypeDef",
    "AdminLinkProviderForUserRequestTypeDef",
    "AdminListDevicesRequestTypeDef",
    "AdminListDevicesResponseResponseTypeDef",
    "AdminListGroupsForUserRequestTypeDef",
    "AdminListGroupsForUserResponseResponseTypeDef",
    "AdminListUserAuthEventsRequestTypeDef",
    "AdminListUserAuthEventsResponseResponseTypeDef",
    "AdminRemoveUserFromGroupRequestTypeDef",
    "AdminResetUserPasswordRequestTypeDef",
    "AdminRespondToAuthChallengeRequestTypeDef",
    "AdminRespondToAuthChallengeResponseResponseTypeDef",
    "AdminSetUserMFAPreferenceRequestTypeDef",
    "AdminSetUserPasswordRequestTypeDef",
    "AdminSetUserSettingsRequestTypeDef",
    "AdminUpdateAuthEventFeedbackRequestTypeDef",
    "AdminUpdateDeviceStatusRequestTypeDef",
    "AdminUpdateUserAttributesRequestTypeDef",
    "AdminUserGlobalSignOutRequestTypeDef",
    "AnalyticsConfigurationTypeTypeDef",
    "AnalyticsMetadataTypeTypeDef",
    "AssociateSoftwareTokenRequestTypeDef",
    "AssociateSoftwareTokenResponseResponseTypeDef",
    "AttributeTypeTypeDef",
    "AuthEventTypeTypeDef",
    "AuthenticationResultTypeTypeDef",
    "ChallengeResponseTypeTypeDef",
    "ChangePasswordRequestTypeDef",
    "CodeDeliveryDetailsTypeTypeDef",
    "CompromisedCredentialsActionsTypeTypeDef",
    "CompromisedCredentialsRiskConfigurationTypeTypeDef",
    "ConfirmDeviceRequestTypeDef",
    "ConfirmDeviceResponseResponseTypeDef",
    "ConfirmForgotPasswordRequestTypeDef",
    "ConfirmSignUpRequestTypeDef",
    "ContextDataTypeTypeDef",
    "CreateGroupRequestTypeDef",
    "CreateGroupResponseResponseTypeDef",
    "CreateIdentityProviderRequestTypeDef",
    "CreateIdentityProviderResponseResponseTypeDef",
    "CreateResourceServerRequestTypeDef",
    "CreateResourceServerResponseResponseTypeDef",
    "CreateUserImportJobRequestTypeDef",
    "CreateUserImportJobResponseResponseTypeDef",
    "CreateUserPoolClientRequestTypeDef",
    "CreateUserPoolClientResponseResponseTypeDef",
    "CreateUserPoolDomainRequestTypeDef",
    "CreateUserPoolDomainResponseResponseTypeDef",
    "CreateUserPoolRequestTypeDef",
    "CreateUserPoolResponseResponseTypeDef",
    "CustomDomainConfigTypeTypeDef",
    "CustomEmailLambdaVersionConfigTypeTypeDef",
    "CustomSMSLambdaVersionConfigTypeTypeDef",
    "DeleteGroupRequestTypeDef",
    "DeleteIdentityProviderRequestTypeDef",
    "DeleteResourceServerRequestTypeDef",
    "DeleteUserAttributesRequestTypeDef",
    "DeleteUserPoolClientRequestTypeDef",
    "DeleteUserPoolDomainRequestTypeDef",
    "DeleteUserPoolRequestTypeDef",
    "DeleteUserRequestTypeDef",
    "DescribeIdentityProviderRequestTypeDef",
    "DescribeIdentityProviderResponseResponseTypeDef",
    "DescribeResourceServerRequestTypeDef",
    "DescribeResourceServerResponseResponseTypeDef",
    "DescribeRiskConfigurationRequestTypeDef",
    "DescribeRiskConfigurationResponseResponseTypeDef",
    "DescribeUserImportJobRequestTypeDef",
    "DescribeUserImportJobResponseResponseTypeDef",
    "DescribeUserPoolClientRequestTypeDef",
    "DescribeUserPoolClientResponseResponseTypeDef",
    "DescribeUserPoolDomainRequestTypeDef",
    "DescribeUserPoolDomainResponseResponseTypeDef",
    "DescribeUserPoolRequestTypeDef",
    "DescribeUserPoolResponseResponseTypeDef",
    "DeviceConfigurationTypeTypeDef",
    "DeviceSecretVerifierConfigTypeTypeDef",
    "DeviceTypeTypeDef",
    "DomainDescriptionTypeTypeDef",
    "EmailConfigurationTypeTypeDef",
    "EventContextDataTypeTypeDef",
    "EventFeedbackTypeTypeDef",
    "EventRiskTypeTypeDef",
    "ForgetDeviceRequestTypeDef",
    "ForgotPasswordRequestTypeDef",
    "ForgotPasswordResponseResponseTypeDef",
    "GetCSVHeaderRequestTypeDef",
    "GetCSVHeaderResponseResponseTypeDef",
    "GetDeviceRequestTypeDef",
    "GetDeviceResponseResponseTypeDef",
    "GetGroupRequestTypeDef",
    "GetGroupResponseResponseTypeDef",
    "GetIdentityProviderByIdentifierRequestTypeDef",
    "GetIdentityProviderByIdentifierResponseResponseTypeDef",
    "GetSigningCertificateRequestTypeDef",
    "GetSigningCertificateResponseResponseTypeDef",
    "GetUICustomizationRequestTypeDef",
    "GetUICustomizationResponseResponseTypeDef",
    "GetUserAttributeVerificationCodeRequestTypeDef",
    "GetUserAttributeVerificationCodeResponseResponseTypeDef",
    "GetUserPoolMfaConfigRequestTypeDef",
    "GetUserPoolMfaConfigResponseResponseTypeDef",
    "GetUserRequestTypeDef",
    "GetUserResponseResponseTypeDef",
    "GlobalSignOutRequestTypeDef",
    "GroupTypeTypeDef",
    "HttpHeaderTypeDef",
    "IdentityProviderTypeTypeDef",
    "InitiateAuthRequestTypeDef",
    "InitiateAuthResponseResponseTypeDef",
    "LambdaConfigTypeTypeDef",
    "ListDevicesRequestTypeDef",
    "ListDevicesResponseResponseTypeDef",
    "ListGroupsRequestTypeDef",
    "ListGroupsResponseResponseTypeDef",
    "ListIdentityProvidersRequestTypeDef",
    "ListIdentityProvidersResponseResponseTypeDef",
    "ListResourceServersRequestTypeDef",
    "ListResourceServersResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListUserImportJobsRequestTypeDef",
    "ListUserImportJobsResponseResponseTypeDef",
    "ListUserPoolClientsRequestTypeDef",
    "ListUserPoolClientsResponseResponseTypeDef",
    "ListUserPoolsRequestTypeDef",
    "ListUserPoolsResponseResponseTypeDef",
    "ListUsersInGroupRequestTypeDef",
    "ListUsersInGroupResponseResponseTypeDef",
    "ListUsersRequestTypeDef",
    "ListUsersResponseResponseTypeDef",
    "MFAOptionTypeTypeDef",
    "MessageTemplateTypeTypeDef",
    "NewDeviceMetadataTypeTypeDef",
    "NotifyConfigurationTypeTypeDef",
    "NotifyEmailTypeTypeDef",
    "NumberAttributeConstraintsTypeTypeDef",
    "PaginatorConfigTypeDef",
    "PasswordPolicyTypeTypeDef",
    "ProviderDescriptionTypeDef",
    "ProviderUserIdentifierTypeTypeDef",
    "RecoveryOptionTypeTypeDef",
    "ResendConfirmationCodeRequestTypeDef",
    "ResendConfirmationCodeResponseResponseTypeDef",
    "ResourceServerScopeTypeTypeDef",
    "ResourceServerTypeTypeDef",
    "RespondToAuthChallengeRequestTypeDef",
    "RespondToAuthChallengeResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeTokenRequestTypeDef",
    "RiskConfigurationTypeTypeDef",
    "RiskExceptionConfigurationTypeTypeDef",
    "SMSMfaSettingsTypeTypeDef",
    "SchemaAttributeTypeTypeDef",
    "SetRiskConfigurationRequestTypeDef",
    "SetRiskConfigurationResponseResponseTypeDef",
    "SetUICustomizationRequestTypeDef",
    "SetUICustomizationResponseResponseTypeDef",
    "SetUserMFAPreferenceRequestTypeDef",
    "SetUserPoolMfaConfigRequestTypeDef",
    "SetUserPoolMfaConfigResponseResponseTypeDef",
    "SetUserSettingsRequestTypeDef",
    "SignUpRequestTypeDef",
    "SignUpResponseResponseTypeDef",
    "SmsConfigurationTypeTypeDef",
    "SmsMfaConfigTypeTypeDef",
    "SoftwareTokenMfaConfigTypeTypeDef",
    "SoftwareTokenMfaSettingsTypeTypeDef",
    "StartUserImportJobRequestTypeDef",
    "StartUserImportJobResponseResponseTypeDef",
    "StopUserImportJobRequestTypeDef",
    "StopUserImportJobResponseResponseTypeDef",
    "StringAttributeConstraintsTypeTypeDef",
    "TagResourceRequestTypeDef",
    "TokenValidityUnitsTypeTypeDef",
    "UICustomizationTypeTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAuthEventFeedbackRequestTypeDef",
    "UpdateDeviceStatusRequestTypeDef",
    "UpdateGroupRequestTypeDef",
    "UpdateGroupResponseResponseTypeDef",
    "UpdateIdentityProviderRequestTypeDef",
    "UpdateIdentityProviderResponseResponseTypeDef",
    "UpdateResourceServerRequestTypeDef",
    "UpdateResourceServerResponseResponseTypeDef",
    "UpdateUserAttributesRequestTypeDef",
    "UpdateUserAttributesResponseResponseTypeDef",
    "UpdateUserPoolClientRequestTypeDef",
    "UpdateUserPoolClientResponseResponseTypeDef",
    "UpdateUserPoolDomainRequestTypeDef",
    "UpdateUserPoolDomainResponseResponseTypeDef",
    "UpdateUserPoolRequestTypeDef",
    "UserContextDataTypeTypeDef",
    "UserImportJobTypeTypeDef",
    "UserPoolAddOnsTypeTypeDef",
    "UserPoolClientDescriptionTypeDef",
    "UserPoolClientTypeTypeDef",
    "UserPoolDescriptionTypeTypeDef",
    "UserPoolPolicyTypeTypeDef",
    "UserPoolTypeTypeDef",
    "UserTypeTypeDef",
    "UsernameConfigurationTypeTypeDef",
    "VerificationMessageTemplateTypeTypeDef",
    "VerifySoftwareTokenRequestTypeDef",
    "VerifySoftwareTokenResponseResponseTypeDef",
    "VerifyUserAttributeRequestTypeDef",
)

AccountRecoverySettingTypeTypeDef = TypedDict(
    "AccountRecoverySettingTypeTypeDef",
    {
        "RecoveryMechanisms": List["RecoveryOptionTypeTypeDef"],
    },
    total=False,
)

AccountTakeoverActionTypeTypeDef = TypedDict(
    "AccountTakeoverActionTypeTypeDef",
    {
        "Notify": bool,
        "EventAction": AccountTakeoverEventActionTypeType,
    },
)

AccountTakeoverActionsTypeTypeDef = TypedDict(
    "AccountTakeoverActionsTypeTypeDef",
    {
        "LowAction": "AccountTakeoverActionTypeTypeDef",
        "MediumAction": "AccountTakeoverActionTypeTypeDef",
        "HighAction": "AccountTakeoverActionTypeTypeDef",
    },
    total=False,
)

_RequiredAccountTakeoverRiskConfigurationTypeTypeDef = TypedDict(
    "_RequiredAccountTakeoverRiskConfigurationTypeTypeDef",
    {
        "Actions": "AccountTakeoverActionsTypeTypeDef",
    },
)
_OptionalAccountTakeoverRiskConfigurationTypeTypeDef = TypedDict(
    "_OptionalAccountTakeoverRiskConfigurationTypeTypeDef",
    {
        "NotifyConfiguration": "NotifyConfigurationTypeTypeDef",
    },
    total=False,
)


class AccountTakeoverRiskConfigurationTypeTypeDef(
    _RequiredAccountTakeoverRiskConfigurationTypeTypeDef,
    _OptionalAccountTakeoverRiskConfigurationTypeTypeDef,
):
    pass


AddCustomAttributesRequestTypeDef = TypedDict(
    "AddCustomAttributesRequestTypeDef",
    {
        "UserPoolId": str,
        "CustomAttributes": List["SchemaAttributeTypeTypeDef"],
    },
)

AdminAddUserToGroupRequestTypeDef = TypedDict(
    "AdminAddUserToGroupRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "GroupName": str,
    },
)

_RequiredAdminConfirmSignUpRequestTypeDef = TypedDict(
    "_RequiredAdminConfirmSignUpRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
_OptionalAdminConfirmSignUpRequestTypeDef = TypedDict(
    "_OptionalAdminConfirmSignUpRequestTypeDef",
    {
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)


class AdminConfirmSignUpRequestTypeDef(
    _RequiredAdminConfirmSignUpRequestTypeDef, _OptionalAdminConfirmSignUpRequestTypeDef
):
    pass


AdminCreateUserConfigTypeTypeDef = TypedDict(
    "AdminCreateUserConfigTypeTypeDef",
    {
        "AllowAdminCreateUserOnly": bool,
        "UnusedAccountValidityDays": int,
        "InviteMessageTemplate": "MessageTemplateTypeTypeDef",
    },
    total=False,
)

_RequiredAdminCreateUserRequestTypeDef = TypedDict(
    "_RequiredAdminCreateUserRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
_OptionalAdminCreateUserRequestTypeDef = TypedDict(
    "_OptionalAdminCreateUserRequestTypeDef",
    {
        "UserAttributes": List["AttributeTypeTypeDef"],
        "ValidationData": List["AttributeTypeTypeDef"],
        "TemporaryPassword": str,
        "ForceAliasCreation": bool,
        "MessageAction": MessageActionTypeType,
        "DesiredDeliveryMediums": List[DeliveryMediumTypeType],
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)


class AdminCreateUserRequestTypeDef(
    _RequiredAdminCreateUserRequestTypeDef, _OptionalAdminCreateUserRequestTypeDef
):
    pass


AdminCreateUserResponseResponseTypeDef = TypedDict(
    "AdminCreateUserResponseResponseTypeDef",
    {
        "User": "UserTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminDeleteUserAttributesRequestTypeDef = TypedDict(
    "AdminDeleteUserAttributesRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "UserAttributeNames": List[str],
    },
)

AdminDeleteUserRequestTypeDef = TypedDict(
    "AdminDeleteUserRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

AdminDisableProviderForUserRequestTypeDef = TypedDict(
    "AdminDisableProviderForUserRequestTypeDef",
    {
        "UserPoolId": str,
        "User": "ProviderUserIdentifierTypeTypeDef",
    },
)

AdminDisableUserRequestTypeDef = TypedDict(
    "AdminDisableUserRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

AdminEnableUserRequestTypeDef = TypedDict(
    "AdminEnableUserRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

AdminForgetDeviceRequestTypeDef = TypedDict(
    "AdminForgetDeviceRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "DeviceKey": str,
    },
)

AdminGetDeviceRequestTypeDef = TypedDict(
    "AdminGetDeviceRequestTypeDef",
    {
        "DeviceKey": str,
        "UserPoolId": str,
        "Username": str,
    },
)

AdminGetDeviceResponseResponseTypeDef = TypedDict(
    "AdminGetDeviceResponseResponseTypeDef",
    {
        "Device": "DeviceTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminGetUserRequestTypeDef = TypedDict(
    "AdminGetUserRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

AdminGetUserResponseResponseTypeDef = TypedDict(
    "AdminGetUserResponseResponseTypeDef",
    {
        "Username": str,
        "UserAttributes": List["AttributeTypeTypeDef"],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": UserStatusTypeType,
        "MFAOptions": List["MFAOptionTypeTypeDef"],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAdminInitiateAuthRequestTypeDef = TypedDict(
    "_RequiredAdminInitiateAuthRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "AuthFlow": AuthFlowTypeType,
    },
)
_OptionalAdminInitiateAuthRequestTypeDef = TypedDict(
    "_OptionalAdminInitiateAuthRequestTypeDef",
    {
        "AuthParameters": Dict[str, str],
        "ClientMetadata": Dict[str, str],
        "AnalyticsMetadata": "AnalyticsMetadataTypeTypeDef",
        "ContextData": "ContextDataTypeTypeDef",
    },
    total=False,
)


class AdminInitiateAuthRequestTypeDef(
    _RequiredAdminInitiateAuthRequestTypeDef, _OptionalAdminInitiateAuthRequestTypeDef
):
    pass


AdminInitiateAuthResponseResponseTypeDef = TypedDict(
    "AdminInitiateAuthResponseResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminLinkProviderForUserRequestTypeDef = TypedDict(
    "AdminLinkProviderForUserRequestTypeDef",
    {
        "UserPoolId": str,
        "DestinationUser": "ProviderUserIdentifierTypeTypeDef",
        "SourceUser": "ProviderUserIdentifierTypeTypeDef",
    },
)

_RequiredAdminListDevicesRequestTypeDef = TypedDict(
    "_RequiredAdminListDevicesRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
_OptionalAdminListDevicesRequestTypeDef = TypedDict(
    "_OptionalAdminListDevicesRequestTypeDef",
    {
        "Limit": int,
        "PaginationToken": str,
    },
    total=False,
)


class AdminListDevicesRequestTypeDef(
    _RequiredAdminListDevicesRequestTypeDef, _OptionalAdminListDevicesRequestTypeDef
):
    pass


AdminListDevicesResponseResponseTypeDef = TypedDict(
    "AdminListDevicesResponseResponseTypeDef",
    {
        "Devices": List["DeviceTypeTypeDef"],
        "PaginationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAdminListGroupsForUserRequestTypeDef = TypedDict(
    "_RequiredAdminListGroupsForUserRequestTypeDef",
    {
        "Username": str,
        "UserPoolId": str,
    },
)
_OptionalAdminListGroupsForUserRequestTypeDef = TypedDict(
    "_OptionalAdminListGroupsForUserRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class AdminListGroupsForUserRequestTypeDef(
    _RequiredAdminListGroupsForUserRequestTypeDef, _OptionalAdminListGroupsForUserRequestTypeDef
):
    pass


AdminListGroupsForUserResponseResponseTypeDef = TypedDict(
    "AdminListGroupsForUserResponseResponseTypeDef",
    {
        "Groups": List["GroupTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAdminListUserAuthEventsRequestTypeDef = TypedDict(
    "_RequiredAdminListUserAuthEventsRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
_OptionalAdminListUserAuthEventsRequestTypeDef = TypedDict(
    "_OptionalAdminListUserAuthEventsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class AdminListUserAuthEventsRequestTypeDef(
    _RequiredAdminListUserAuthEventsRequestTypeDef, _OptionalAdminListUserAuthEventsRequestTypeDef
):
    pass


AdminListUserAuthEventsResponseResponseTypeDef = TypedDict(
    "AdminListUserAuthEventsResponseResponseTypeDef",
    {
        "AuthEvents": List["AuthEventTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminRemoveUserFromGroupRequestTypeDef = TypedDict(
    "AdminRemoveUserFromGroupRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "GroupName": str,
    },
)

_RequiredAdminResetUserPasswordRequestTypeDef = TypedDict(
    "_RequiredAdminResetUserPasswordRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
_OptionalAdminResetUserPasswordRequestTypeDef = TypedDict(
    "_OptionalAdminResetUserPasswordRequestTypeDef",
    {
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)


class AdminResetUserPasswordRequestTypeDef(
    _RequiredAdminResetUserPasswordRequestTypeDef, _OptionalAdminResetUserPasswordRequestTypeDef
):
    pass


_RequiredAdminRespondToAuthChallengeRequestTypeDef = TypedDict(
    "_RequiredAdminRespondToAuthChallengeRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "ChallengeName": ChallengeNameTypeType,
    },
)
_OptionalAdminRespondToAuthChallengeRequestTypeDef = TypedDict(
    "_OptionalAdminRespondToAuthChallengeRequestTypeDef",
    {
        "ChallengeResponses": Dict[str, str],
        "Session": str,
        "AnalyticsMetadata": "AnalyticsMetadataTypeTypeDef",
        "ContextData": "ContextDataTypeTypeDef",
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)


class AdminRespondToAuthChallengeRequestTypeDef(
    _RequiredAdminRespondToAuthChallengeRequestTypeDef,
    _OptionalAdminRespondToAuthChallengeRequestTypeDef,
):
    pass


AdminRespondToAuthChallengeResponseResponseTypeDef = TypedDict(
    "AdminRespondToAuthChallengeResponseResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAdminSetUserMFAPreferenceRequestTypeDef = TypedDict(
    "_RequiredAdminSetUserMFAPreferenceRequestTypeDef",
    {
        "Username": str,
        "UserPoolId": str,
    },
)
_OptionalAdminSetUserMFAPreferenceRequestTypeDef = TypedDict(
    "_OptionalAdminSetUserMFAPreferenceRequestTypeDef",
    {
        "SMSMfaSettings": "SMSMfaSettingsTypeTypeDef",
        "SoftwareTokenMfaSettings": "SoftwareTokenMfaSettingsTypeTypeDef",
    },
    total=False,
)


class AdminSetUserMFAPreferenceRequestTypeDef(
    _RequiredAdminSetUserMFAPreferenceRequestTypeDef,
    _OptionalAdminSetUserMFAPreferenceRequestTypeDef,
):
    pass


_RequiredAdminSetUserPasswordRequestTypeDef = TypedDict(
    "_RequiredAdminSetUserPasswordRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "Password": str,
    },
)
_OptionalAdminSetUserPasswordRequestTypeDef = TypedDict(
    "_OptionalAdminSetUserPasswordRequestTypeDef",
    {
        "Permanent": bool,
    },
    total=False,
)


class AdminSetUserPasswordRequestTypeDef(
    _RequiredAdminSetUserPasswordRequestTypeDef, _OptionalAdminSetUserPasswordRequestTypeDef
):
    pass


AdminSetUserSettingsRequestTypeDef = TypedDict(
    "AdminSetUserSettingsRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "MFAOptions": List["MFAOptionTypeTypeDef"],
    },
)

AdminUpdateAuthEventFeedbackRequestTypeDef = TypedDict(
    "AdminUpdateAuthEventFeedbackRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "EventId": str,
        "FeedbackValue": FeedbackValueTypeType,
    },
)

_RequiredAdminUpdateDeviceStatusRequestTypeDef = TypedDict(
    "_RequiredAdminUpdateDeviceStatusRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "DeviceKey": str,
    },
)
_OptionalAdminUpdateDeviceStatusRequestTypeDef = TypedDict(
    "_OptionalAdminUpdateDeviceStatusRequestTypeDef",
    {
        "DeviceRememberedStatus": DeviceRememberedStatusTypeType,
    },
    total=False,
)


class AdminUpdateDeviceStatusRequestTypeDef(
    _RequiredAdminUpdateDeviceStatusRequestTypeDef, _OptionalAdminUpdateDeviceStatusRequestTypeDef
):
    pass


_RequiredAdminUpdateUserAttributesRequestTypeDef = TypedDict(
    "_RequiredAdminUpdateUserAttributesRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "UserAttributes": List["AttributeTypeTypeDef"],
    },
)
_OptionalAdminUpdateUserAttributesRequestTypeDef = TypedDict(
    "_OptionalAdminUpdateUserAttributesRequestTypeDef",
    {
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)


class AdminUpdateUserAttributesRequestTypeDef(
    _RequiredAdminUpdateUserAttributesRequestTypeDef,
    _OptionalAdminUpdateUserAttributesRequestTypeDef,
):
    pass


AdminUserGlobalSignOutRequestTypeDef = TypedDict(
    "AdminUserGlobalSignOutRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

AnalyticsConfigurationTypeTypeDef = TypedDict(
    "AnalyticsConfigurationTypeTypeDef",
    {
        "ApplicationId": str,
        "ApplicationArn": str,
        "RoleArn": str,
        "ExternalId": str,
        "UserDataShared": bool,
    },
    total=False,
)

AnalyticsMetadataTypeTypeDef = TypedDict(
    "AnalyticsMetadataTypeTypeDef",
    {
        "AnalyticsEndpointId": str,
    },
    total=False,
)

AssociateSoftwareTokenRequestTypeDef = TypedDict(
    "AssociateSoftwareTokenRequestTypeDef",
    {
        "AccessToken": str,
        "Session": str,
    },
    total=False,
)

AssociateSoftwareTokenResponseResponseTypeDef = TypedDict(
    "AssociateSoftwareTokenResponseResponseTypeDef",
    {
        "SecretCode": str,
        "Session": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAttributeTypeTypeDef = TypedDict(
    "_RequiredAttributeTypeTypeDef",
    {
        "Name": str,
    },
)
_OptionalAttributeTypeTypeDef = TypedDict(
    "_OptionalAttributeTypeTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class AttributeTypeTypeDef(_RequiredAttributeTypeTypeDef, _OptionalAttributeTypeTypeDef):
    pass


AuthEventTypeTypeDef = TypedDict(
    "AuthEventTypeTypeDef",
    {
        "EventId": str,
        "EventType": EventTypeType,
        "CreationDate": datetime,
        "EventResponse": EventResponseTypeType,
        "EventRisk": "EventRiskTypeTypeDef",
        "ChallengeResponses": List["ChallengeResponseTypeTypeDef"],
        "EventContextData": "EventContextDataTypeTypeDef",
        "EventFeedback": "EventFeedbackTypeTypeDef",
    },
    total=False,
)

AuthenticationResultTypeTypeDef = TypedDict(
    "AuthenticationResultTypeTypeDef",
    {
        "AccessToken": str,
        "ExpiresIn": int,
        "TokenType": str,
        "RefreshToken": str,
        "IdToken": str,
        "NewDeviceMetadata": "NewDeviceMetadataTypeTypeDef",
    },
    total=False,
)

ChallengeResponseTypeTypeDef = TypedDict(
    "ChallengeResponseTypeTypeDef",
    {
        "ChallengeName": ChallengeNameType,
        "ChallengeResponse": ChallengeResponseType,
    },
    total=False,
)

ChangePasswordRequestTypeDef = TypedDict(
    "ChangePasswordRequestTypeDef",
    {
        "PreviousPassword": str,
        "ProposedPassword": str,
        "AccessToken": str,
    },
)

CodeDeliveryDetailsTypeTypeDef = TypedDict(
    "CodeDeliveryDetailsTypeTypeDef",
    {
        "Destination": str,
        "DeliveryMedium": DeliveryMediumTypeType,
        "AttributeName": str,
    },
    total=False,
)

CompromisedCredentialsActionsTypeTypeDef = TypedDict(
    "CompromisedCredentialsActionsTypeTypeDef",
    {
        "EventAction": CompromisedCredentialsEventActionTypeType,
    },
)

_RequiredCompromisedCredentialsRiskConfigurationTypeTypeDef = TypedDict(
    "_RequiredCompromisedCredentialsRiskConfigurationTypeTypeDef",
    {
        "Actions": "CompromisedCredentialsActionsTypeTypeDef",
    },
)
_OptionalCompromisedCredentialsRiskConfigurationTypeTypeDef = TypedDict(
    "_OptionalCompromisedCredentialsRiskConfigurationTypeTypeDef",
    {
        "EventFilter": List[EventFilterTypeType],
    },
    total=False,
)


class CompromisedCredentialsRiskConfigurationTypeTypeDef(
    _RequiredCompromisedCredentialsRiskConfigurationTypeTypeDef,
    _OptionalCompromisedCredentialsRiskConfigurationTypeTypeDef,
):
    pass


_RequiredConfirmDeviceRequestTypeDef = TypedDict(
    "_RequiredConfirmDeviceRequestTypeDef",
    {
        "AccessToken": str,
        "DeviceKey": str,
    },
)
_OptionalConfirmDeviceRequestTypeDef = TypedDict(
    "_OptionalConfirmDeviceRequestTypeDef",
    {
        "DeviceSecretVerifierConfig": "DeviceSecretVerifierConfigTypeTypeDef",
        "DeviceName": str,
    },
    total=False,
)


class ConfirmDeviceRequestTypeDef(
    _RequiredConfirmDeviceRequestTypeDef, _OptionalConfirmDeviceRequestTypeDef
):
    pass


ConfirmDeviceResponseResponseTypeDef = TypedDict(
    "ConfirmDeviceResponseResponseTypeDef",
    {
        "UserConfirmationNecessary": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredConfirmForgotPasswordRequestTypeDef = TypedDict(
    "_RequiredConfirmForgotPasswordRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
        "ConfirmationCode": str,
        "Password": str,
    },
)
_OptionalConfirmForgotPasswordRequestTypeDef = TypedDict(
    "_OptionalConfirmForgotPasswordRequestTypeDef",
    {
        "SecretHash": str,
        "AnalyticsMetadata": "AnalyticsMetadataTypeTypeDef",
        "UserContextData": "UserContextDataTypeTypeDef",
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)


class ConfirmForgotPasswordRequestTypeDef(
    _RequiredConfirmForgotPasswordRequestTypeDef, _OptionalConfirmForgotPasswordRequestTypeDef
):
    pass


_RequiredConfirmSignUpRequestTypeDef = TypedDict(
    "_RequiredConfirmSignUpRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
        "ConfirmationCode": str,
    },
)
_OptionalConfirmSignUpRequestTypeDef = TypedDict(
    "_OptionalConfirmSignUpRequestTypeDef",
    {
        "SecretHash": str,
        "ForceAliasCreation": bool,
        "AnalyticsMetadata": "AnalyticsMetadataTypeTypeDef",
        "UserContextData": "UserContextDataTypeTypeDef",
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)


class ConfirmSignUpRequestTypeDef(
    _RequiredConfirmSignUpRequestTypeDef, _OptionalConfirmSignUpRequestTypeDef
):
    pass


_RequiredContextDataTypeTypeDef = TypedDict(
    "_RequiredContextDataTypeTypeDef",
    {
        "IpAddress": str,
        "ServerName": str,
        "ServerPath": str,
        "HttpHeaders": List["HttpHeaderTypeDef"],
    },
)
_OptionalContextDataTypeTypeDef = TypedDict(
    "_OptionalContextDataTypeTypeDef",
    {
        "EncodedData": str,
    },
    total=False,
)


class ContextDataTypeTypeDef(_RequiredContextDataTypeTypeDef, _OptionalContextDataTypeTypeDef):
    pass


_RequiredCreateGroupRequestTypeDef = TypedDict(
    "_RequiredCreateGroupRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
    },
)
_OptionalCreateGroupRequestTypeDef = TypedDict(
    "_OptionalCreateGroupRequestTypeDef",
    {
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
    },
    total=False,
)


class CreateGroupRequestTypeDef(
    _RequiredCreateGroupRequestTypeDef, _OptionalCreateGroupRequestTypeDef
):
    pass


CreateGroupResponseResponseTypeDef = TypedDict(
    "CreateGroupResponseResponseTypeDef",
    {
        "Group": "GroupTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIdentityProviderRequestTypeDef = TypedDict(
    "_RequiredCreateIdentityProviderRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": IdentityProviderTypeTypeType,
        "ProviderDetails": Dict[str, str],
    },
)
_OptionalCreateIdentityProviderRequestTypeDef = TypedDict(
    "_OptionalCreateIdentityProviderRequestTypeDef",
    {
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
    },
    total=False,
)


class CreateIdentityProviderRequestTypeDef(
    _RequiredCreateIdentityProviderRequestTypeDef, _OptionalCreateIdentityProviderRequestTypeDef
):
    pass


CreateIdentityProviderResponseResponseTypeDef = TypedDict(
    "CreateIdentityProviderResponseResponseTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResourceServerRequestTypeDef = TypedDict(
    "_RequiredCreateResourceServerRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
    },
)
_OptionalCreateResourceServerRequestTypeDef = TypedDict(
    "_OptionalCreateResourceServerRequestTypeDef",
    {
        "Scopes": List["ResourceServerScopeTypeTypeDef"],
    },
    total=False,
)


class CreateResourceServerRequestTypeDef(
    _RequiredCreateResourceServerRequestTypeDef, _OptionalCreateResourceServerRequestTypeDef
):
    pass


CreateResourceServerResponseResponseTypeDef = TypedDict(
    "CreateResourceServerResponseResponseTypeDef",
    {
        "ResourceServer": "ResourceServerTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserImportJobRequestTypeDef = TypedDict(
    "CreateUserImportJobRequestTypeDef",
    {
        "JobName": str,
        "UserPoolId": str,
        "CloudWatchLogsRoleArn": str,
    },
)

CreateUserImportJobResponseResponseTypeDef = TypedDict(
    "CreateUserImportJobResponseResponseTypeDef",
    {
        "UserImportJob": "UserImportJobTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserPoolClientRequestTypeDef = TypedDict(
    "_RequiredCreateUserPoolClientRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientName": str,
    },
)
_OptionalCreateUserPoolClientRequestTypeDef = TypedDict(
    "_OptionalCreateUserPoolClientRequestTypeDef",
    {
        "GenerateSecret": bool,
        "RefreshTokenValidity": int,
        "AccessTokenValidity": int,
        "IdTokenValidity": int,
        "TokenValidityUnits": "TokenValidityUnitsTypeTypeDef",
        "ReadAttributes": List[str],
        "WriteAttributes": List[str],
        "ExplicitAuthFlows": List[ExplicitAuthFlowsTypeType],
        "SupportedIdentityProviders": List[str],
        "CallbackURLs": List[str],
        "LogoutURLs": List[str],
        "DefaultRedirectURI": str,
        "AllowedOAuthFlows": List[OAuthFlowTypeType],
        "AllowedOAuthScopes": List[str],
        "AllowedOAuthFlowsUserPoolClient": bool,
        "AnalyticsConfiguration": "AnalyticsConfigurationTypeTypeDef",
        "PreventUserExistenceErrors": PreventUserExistenceErrorTypesType,
        "EnableTokenRevocation": bool,
    },
    total=False,
)


class CreateUserPoolClientRequestTypeDef(
    _RequiredCreateUserPoolClientRequestTypeDef, _OptionalCreateUserPoolClientRequestTypeDef
):
    pass


CreateUserPoolClientResponseResponseTypeDef = TypedDict(
    "CreateUserPoolClientResponseResponseTypeDef",
    {
        "UserPoolClient": "UserPoolClientTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserPoolDomainRequestTypeDef = TypedDict(
    "_RequiredCreateUserPoolDomainRequestTypeDef",
    {
        "Domain": str,
        "UserPoolId": str,
    },
)
_OptionalCreateUserPoolDomainRequestTypeDef = TypedDict(
    "_OptionalCreateUserPoolDomainRequestTypeDef",
    {
        "CustomDomainConfig": "CustomDomainConfigTypeTypeDef",
    },
    total=False,
)


class CreateUserPoolDomainRequestTypeDef(
    _RequiredCreateUserPoolDomainRequestTypeDef, _OptionalCreateUserPoolDomainRequestTypeDef
):
    pass


CreateUserPoolDomainResponseResponseTypeDef = TypedDict(
    "CreateUserPoolDomainResponseResponseTypeDef",
    {
        "CloudFrontDomain": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserPoolRequestTypeDef = TypedDict(
    "_RequiredCreateUserPoolRequestTypeDef",
    {
        "PoolName": str,
    },
)
_OptionalCreateUserPoolRequestTypeDef = TypedDict(
    "_OptionalCreateUserPoolRequestTypeDef",
    {
        "Policies": "UserPoolPolicyTypeTypeDef",
        "LambdaConfig": "LambdaConfigTypeTypeDef",
        "AutoVerifiedAttributes": List[VerifiedAttributeTypeType],
        "AliasAttributes": List[AliasAttributeTypeType],
        "UsernameAttributes": List[UsernameAttributeTypeType],
        "SmsVerificationMessage": str,
        "EmailVerificationMessage": str,
        "EmailVerificationSubject": str,
        "VerificationMessageTemplate": "VerificationMessageTemplateTypeTypeDef",
        "SmsAuthenticationMessage": str,
        "MfaConfiguration": UserPoolMfaTypeType,
        "DeviceConfiguration": "DeviceConfigurationTypeTypeDef",
        "EmailConfiguration": "EmailConfigurationTypeTypeDef",
        "SmsConfiguration": "SmsConfigurationTypeTypeDef",
        "UserPoolTags": Dict[str, str],
        "AdminCreateUserConfig": "AdminCreateUserConfigTypeTypeDef",
        "Schema": List["SchemaAttributeTypeTypeDef"],
        "UserPoolAddOns": "UserPoolAddOnsTypeTypeDef",
        "UsernameConfiguration": "UsernameConfigurationTypeTypeDef",
        "AccountRecoverySetting": "AccountRecoverySettingTypeTypeDef",
    },
    total=False,
)


class CreateUserPoolRequestTypeDef(
    _RequiredCreateUserPoolRequestTypeDef, _OptionalCreateUserPoolRequestTypeDef
):
    pass


CreateUserPoolResponseResponseTypeDef = TypedDict(
    "CreateUserPoolResponseResponseTypeDef",
    {
        "UserPool": "UserPoolTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomDomainConfigTypeTypeDef = TypedDict(
    "CustomDomainConfigTypeTypeDef",
    {
        "CertificateArn": str,
    },
)

CustomEmailLambdaVersionConfigTypeTypeDef = TypedDict(
    "CustomEmailLambdaVersionConfigTypeTypeDef",
    {
        "LambdaVersion": Literal["V1_0"],
        "LambdaArn": str,
    },
)

CustomSMSLambdaVersionConfigTypeTypeDef = TypedDict(
    "CustomSMSLambdaVersionConfigTypeTypeDef",
    {
        "LambdaVersion": Literal["V1_0"],
        "LambdaArn": str,
    },
)

DeleteGroupRequestTypeDef = TypedDict(
    "DeleteGroupRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
    },
)

DeleteIdentityProviderRequestTypeDef = TypedDict(
    "DeleteIdentityProviderRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
    },
)

DeleteResourceServerRequestTypeDef = TypedDict(
    "DeleteResourceServerRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
    },
)

DeleteUserAttributesRequestTypeDef = TypedDict(
    "DeleteUserAttributesRequestTypeDef",
    {
        "UserAttributeNames": List[str],
        "AccessToken": str,
    },
)

DeleteUserPoolClientRequestTypeDef = TypedDict(
    "DeleteUserPoolClientRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
    },
)

DeleteUserPoolDomainRequestTypeDef = TypedDict(
    "DeleteUserPoolDomainRequestTypeDef",
    {
        "Domain": str,
        "UserPoolId": str,
    },
)

DeleteUserPoolRequestTypeDef = TypedDict(
    "DeleteUserPoolRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

DeleteUserRequestTypeDef = TypedDict(
    "DeleteUserRequestTypeDef",
    {
        "AccessToken": str,
    },
)

DescribeIdentityProviderRequestTypeDef = TypedDict(
    "DescribeIdentityProviderRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
    },
)

DescribeIdentityProviderResponseResponseTypeDef = TypedDict(
    "DescribeIdentityProviderResponseResponseTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourceServerRequestTypeDef = TypedDict(
    "DescribeResourceServerRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
    },
)

DescribeResourceServerResponseResponseTypeDef = TypedDict(
    "DescribeResourceServerResponseResponseTypeDef",
    {
        "ResourceServer": "ResourceServerTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRiskConfigurationRequestTypeDef = TypedDict(
    "_RequiredDescribeRiskConfigurationRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalDescribeRiskConfigurationRequestTypeDef = TypedDict(
    "_OptionalDescribeRiskConfigurationRequestTypeDef",
    {
        "ClientId": str,
    },
    total=False,
)


class DescribeRiskConfigurationRequestTypeDef(
    _RequiredDescribeRiskConfigurationRequestTypeDef,
    _OptionalDescribeRiskConfigurationRequestTypeDef,
):
    pass


DescribeRiskConfigurationResponseResponseTypeDef = TypedDict(
    "DescribeRiskConfigurationResponseResponseTypeDef",
    {
        "RiskConfiguration": "RiskConfigurationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserImportJobRequestTypeDef = TypedDict(
    "DescribeUserImportJobRequestTypeDef",
    {
        "UserPoolId": str,
        "JobId": str,
    },
)

DescribeUserImportJobResponseResponseTypeDef = TypedDict(
    "DescribeUserImportJobResponseResponseTypeDef",
    {
        "UserImportJob": "UserImportJobTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserPoolClientRequestTypeDef = TypedDict(
    "DescribeUserPoolClientRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
    },
)

DescribeUserPoolClientResponseResponseTypeDef = TypedDict(
    "DescribeUserPoolClientResponseResponseTypeDef",
    {
        "UserPoolClient": "UserPoolClientTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserPoolDomainRequestTypeDef = TypedDict(
    "DescribeUserPoolDomainRequestTypeDef",
    {
        "Domain": str,
    },
)

DescribeUserPoolDomainResponseResponseTypeDef = TypedDict(
    "DescribeUserPoolDomainResponseResponseTypeDef",
    {
        "DomainDescription": "DomainDescriptionTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserPoolRequestTypeDef = TypedDict(
    "DescribeUserPoolRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

DescribeUserPoolResponseResponseTypeDef = TypedDict(
    "DescribeUserPoolResponseResponseTypeDef",
    {
        "UserPool": "UserPoolTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceConfigurationTypeTypeDef = TypedDict(
    "DeviceConfigurationTypeTypeDef",
    {
        "ChallengeRequiredOnNewDevice": bool,
        "DeviceOnlyRememberedOnUserPrompt": bool,
    },
    total=False,
)

DeviceSecretVerifierConfigTypeTypeDef = TypedDict(
    "DeviceSecretVerifierConfigTypeTypeDef",
    {
        "PasswordVerifier": str,
        "Salt": str,
    },
    total=False,
)

DeviceTypeTypeDef = TypedDict(
    "DeviceTypeTypeDef",
    {
        "DeviceKey": str,
        "DeviceAttributes": List["AttributeTypeTypeDef"],
        "DeviceCreateDate": datetime,
        "DeviceLastModifiedDate": datetime,
        "DeviceLastAuthenticatedDate": datetime,
    },
    total=False,
)

DomainDescriptionTypeTypeDef = TypedDict(
    "DomainDescriptionTypeTypeDef",
    {
        "UserPoolId": str,
        "AWSAccountId": str,
        "Domain": str,
        "S3Bucket": str,
        "CloudFrontDistribution": str,
        "Version": str,
        "Status": DomainStatusTypeType,
        "CustomDomainConfig": "CustomDomainConfigTypeTypeDef",
    },
    total=False,
)

EmailConfigurationTypeTypeDef = TypedDict(
    "EmailConfigurationTypeTypeDef",
    {
        "SourceArn": str,
        "ReplyToEmailAddress": str,
        "EmailSendingAccount": EmailSendingAccountTypeType,
        "From": str,
        "ConfigurationSet": str,
    },
    total=False,
)

EventContextDataTypeTypeDef = TypedDict(
    "EventContextDataTypeTypeDef",
    {
        "IpAddress": str,
        "DeviceName": str,
        "Timezone": str,
        "City": str,
        "Country": str,
    },
    total=False,
)

_RequiredEventFeedbackTypeTypeDef = TypedDict(
    "_RequiredEventFeedbackTypeTypeDef",
    {
        "FeedbackValue": FeedbackValueTypeType,
        "Provider": str,
    },
)
_OptionalEventFeedbackTypeTypeDef = TypedDict(
    "_OptionalEventFeedbackTypeTypeDef",
    {
        "FeedbackDate": datetime,
    },
    total=False,
)


class EventFeedbackTypeTypeDef(
    _RequiredEventFeedbackTypeTypeDef, _OptionalEventFeedbackTypeTypeDef
):
    pass


EventRiskTypeTypeDef = TypedDict(
    "EventRiskTypeTypeDef",
    {
        "RiskDecision": RiskDecisionTypeType,
        "RiskLevel": RiskLevelTypeType,
        "CompromisedCredentialsDetected": bool,
    },
    total=False,
)

_RequiredForgetDeviceRequestTypeDef = TypedDict(
    "_RequiredForgetDeviceRequestTypeDef",
    {
        "DeviceKey": str,
    },
)
_OptionalForgetDeviceRequestTypeDef = TypedDict(
    "_OptionalForgetDeviceRequestTypeDef",
    {
        "AccessToken": str,
    },
    total=False,
)


class ForgetDeviceRequestTypeDef(
    _RequiredForgetDeviceRequestTypeDef, _OptionalForgetDeviceRequestTypeDef
):
    pass


_RequiredForgotPasswordRequestTypeDef = TypedDict(
    "_RequiredForgotPasswordRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
    },
)
_OptionalForgotPasswordRequestTypeDef = TypedDict(
    "_OptionalForgotPasswordRequestTypeDef",
    {
        "SecretHash": str,
        "UserContextData": "UserContextDataTypeTypeDef",
        "AnalyticsMetadata": "AnalyticsMetadataTypeTypeDef",
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)


class ForgotPasswordRequestTypeDef(
    _RequiredForgotPasswordRequestTypeDef, _OptionalForgotPasswordRequestTypeDef
):
    pass


ForgotPasswordResponseResponseTypeDef = TypedDict(
    "ForgotPasswordResponseResponseTypeDef",
    {
        "CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCSVHeaderRequestTypeDef = TypedDict(
    "GetCSVHeaderRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

GetCSVHeaderResponseResponseTypeDef = TypedDict(
    "GetCSVHeaderResponseResponseTypeDef",
    {
        "UserPoolId": str,
        "CSVHeader": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDeviceRequestTypeDef = TypedDict(
    "_RequiredGetDeviceRequestTypeDef",
    {
        "DeviceKey": str,
    },
)
_OptionalGetDeviceRequestTypeDef = TypedDict(
    "_OptionalGetDeviceRequestTypeDef",
    {
        "AccessToken": str,
    },
    total=False,
)


class GetDeviceRequestTypeDef(_RequiredGetDeviceRequestTypeDef, _OptionalGetDeviceRequestTypeDef):
    pass


GetDeviceResponseResponseTypeDef = TypedDict(
    "GetDeviceResponseResponseTypeDef",
    {
        "Device": "DeviceTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupRequestTypeDef = TypedDict(
    "GetGroupRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
    },
)

GetGroupResponseResponseTypeDef = TypedDict(
    "GetGroupResponseResponseTypeDef",
    {
        "Group": "GroupTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityProviderByIdentifierRequestTypeDef = TypedDict(
    "GetIdentityProviderByIdentifierRequestTypeDef",
    {
        "UserPoolId": str,
        "IdpIdentifier": str,
    },
)

GetIdentityProviderByIdentifierResponseResponseTypeDef = TypedDict(
    "GetIdentityProviderByIdentifierResponseResponseTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSigningCertificateRequestTypeDef = TypedDict(
    "GetSigningCertificateRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

GetSigningCertificateResponseResponseTypeDef = TypedDict(
    "GetSigningCertificateResponseResponseTypeDef",
    {
        "Certificate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetUICustomizationRequestTypeDef = TypedDict(
    "_RequiredGetUICustomizationRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalGetUICustomizationRequestTypeDef = TypedDict(
    "_OptionalGetUICustomizationRequestTypeDef",
    {
        "ClientId": str,
    },
    total=False,
)


class GetUICustomizationRequestTypeDef(
    _RequiredGetUICustomizationRequestTypeDef, _OptionalGetUICustomizationRequestTypeDef
):
    pass


GetUICustomizationResponseResponseTypeDef = TypedDict(
    "GetUICustomizationResponseResponseTypeDef",
    {
        "UICustomization": "UICustomizationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetUserAttributeVerificationCodeRequestTypeDef = TypedDict(
    "_RequiredGetUserAttributeVerificationCodeRequestTypeDef",
    {
        "AccessToken": str,
        "AttributeName": str,
    },
)
_OptionalGetUserAttributeVerificationCodeRequestTypeDef = TypedDict(
    "_OptionalGetUserAttributeVerificationCodeRequestTypeDef",
    {
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)


class GetUserAttributeVerificationCodeRequestTypeDef(
    _RequiredGetUserAttributeVerificationCodeRequestTypeDef,
    _OptionalGetUserAttributeVerificationCodeRequestTypeDef,
):
    pass


GetUserAttributeVerificationCodeResponseResponseTypeDef = TypedDict(
    "GetUserAttributeVerificationCodeResponseResponseTypeDef",
    {
        "CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserPoolMfaConfigRequestTypeDef = TypedDict(
    "GetUserPoolMfaConfigRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

GetUserPoolMfaConfigResponseResponseTypeDef = TypedDict(
    "GetUserPoolMfaConfigResponseResponseTypeDef",
    {
        "SmsMfaConfiguration": "SmsMfaConfigTypeTypeDef",
        "SoftwareTokenMfaConfiguration": "SoftwareTokenMfaConfigTypeTypeDef",
        "MfaConfiguration": UserPoolMfaTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserRequestTypeDef = TypedDict(
    "GetUserRequestTypeDef",
    {
        "AccessToken": str,
    },
)

GetUserResponseResponseTypeDef = TypedDict(
    "GetUserResponseResponseTypeDef",
    {
        "Username": str,
        "UserAttributes": List["AttributeTypeTypeDef"],
        "MFAOptions": List["MFAOptionTypeTypeDef"],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GlobalSignOutRequestTypeDef = TypedDict(
    "GlobalSignOutRequestTypeDef",
    {
        "AccessToken": str,
    },
)

GroupTypeTypeDef = TypedDict(
    "GroupTypeTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

HttpHeaderTypeDef = TypedDict(
    "HttpHeaderTypeDef",
    {
        "headerName": str,
        "headerValue": str,
    },
    total=False,
)

IdentityProviderTypeTypeDef = TypedDict(
    "IdentityProviderTypeTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": IdentityProviderTypeTypeType,
        "ProviderDetails": Dict[str, str],
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

_RequiredInitiateAuthRequestTypeDef = TypedDict(
    "_RequiredInitiateAuthRequestTypeDef",
    {
        "AuthFlow": AuthFlowTypeType,
        "ClientId": str,
    },
)
_OptionalInitiateAuthRequestTypeDef = TypedDict(
    "_OptionalInitiateAuthRequestTypeDef",
    {
        "AuthParameters": Dict[str, str],
        "ClientMetadata": Dict[str, str],
        "AnalyticsMetadata": "AnalyticsMetadataTypeTypeDef",
        "UserContextData": "UserContextDataTypeTypeDef",
    },
    total=False,
)


class InitiateAuthRequestTypeDef(
    _RequiredInitiateAuthRequestTypeDef, _OptionalInitiateAuthRequestTypeDef
):
    pass


InitiateAuthResponseResponseTypeDef = TypedDict(
    "InitiateAuthResponseResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LambdaConfigTypeTypeDef = TypedDict(
    "LambdaConfigTypeTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
        "CustomSMSSender": "CustomSMSLambdaVersionConfigTypeTypeDef",
        "CustomEmailSender": "CustomEmailLambdaVersionConfigTypeTypeDef",
        "KMSKeyID": str,
    },
    total=False,
)

_RequiredListDevicesRequestTypeDef = TypedDict(
    "_RequiredListDevicesRequestTypeDef",
    {
        "AccessToken": str,
    },
)
_OptionalListDevicesRequestTypeDef = TypedDict(
    "_OptionalListDevicesRequestTypeDef",
    {
        "Limit": int,
        "PaginationToken": str,
    },
    total=False,
)


class ListDevicesRequestTypeDef(
    _RequiredListDevicesRequestTypeDef, _OptionalListDevicesRequestTypeDef
):
    pass


ListDevicesResponseResponseTypeDef = TypedDict(
    "ListDevicesResponseResponseTypeDef",
    {
        "Devices": List["DeviceTypeTypeDef"],
        "PaginationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupsRequestTypeDef = TypedDict(
    "_RequiredListGroupsRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListGroupsRequestTypeDef = TypedDict(
    "_OptionalListGroupsRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class ListGroupsRequestTypeDef(
    _RequiredListGroupsRequestTypeDef, _OptionalListGroupsRequestTypeDef
):
    pass


ListGroupsResponseResponseTypeDef = TypedDict(
    "ListGroupsResponseResponseTypeDef",
    {
        "Groups": List["GroupTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIdentityProvidersRequestTypeDef = TypedDict(
    "_RequiredListIdentityProvidersRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListIdentityProvidersRequestTypeDef = TypedDict(
    "_OptionalListIdentityProvidersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListIdentityProvidersRequestTypeDef(
    _RequiredListIdentityProvidersRequestTypeDef, _OptionalListIdentityProvidersRequestTypeDef
):
    pass


ListIdentityProvidersResponseResponseTypeDef = TypedDict(
    "ListIdentityProvidersResponseResponseTypeDef",
    {
        "Providers": List["ProviderDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourceServersRequestTypeDef = TypedDict(
    "_RequiredListResourceServersRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListResourceServersRequestTypeDef = TypedDict(
    "_OptionalListResourceServersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListResourceServersRequestTypeDef(
    _RequiredListResourceServersRequestTypeDef, _OptionalListResourceServersRequestTypeDef
):
    pass


ListResourceServersResponseResponseTypeDef = TypedDict(
    "ListResourceServersResponseResponseTypeDef",
    {
        "ResourceServers": List["ResourceServerTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUserImportJobsRequestTypeDef = TypedDict(
    "_RequiredListUserImportJobsRequestTypeDef",
    {
        "UserPoolId": str,
        "MaxResults": int,
    },
)
_OptionalListUserImportJobsRequestTypeDef = TypedDict(
    "_OptionalListUserImportJobsRequestTypeDef",
    {
        "PaginationToken": str,
    },
    total=False,
)


class ListUserImportJobsRequestTypeDef(
    _RequiredListUserImportJobsRequestTypeDef, _OptionalListUserImportJobsRequestTypeDef
):
    pass


ListUserImportJobsResponseResponseTypeDef = TypedDict(
    "ListUserImportJobsResponseResponseTypeDef",
    {
        "UserImportJobs": List["UserImportJobTypeTypeDef"],
        "PaginationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUserPoolClientsRequestTypeDef = TypedDict(
    "_RequiredListUserPoolClientsRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListUserPoolClientsRequestTypeDef = TypedDict(
    "_OptionalListUserPoolClientsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListUserPoolClientsRequestTypeDef(
    _RequiredListUserPoolClientsRequestTypeDef, _OptionalListUserPoolClientsRequestTypeDef
):
    pass


ListUserPoolClientsResponseResponseTypeDef = TypedDict(
    "ListUserPoolClientsResponseResponseTypeDef",
    {
        "UserPoolClients": List["UserPoolClientDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUserPoolsRequestTypeDef = TypedDict(
    "_RequiredListUserPoolsRequestTypeDef",
    {
        "MaxResults": int,
    },
)
_OptionalListUserPoolsRequestTypeDef = TypedDict(
    "_OptionalListUserPoolsRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListUserPoolsRequestTypeDef(
    _RequiredListUserPoolsRequestTypeDef, _OptionalListUserPoolsRequestTypeDef
):
    pass


ListUserPoolsResponseResponseTypeDef = TypedDict(
    "ListUserPoolsResponseResponseTypeDef",
    {
        "UserPools": List["UserPoolDescriptionTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersInGroupRequestTypeDef = TypedDict(
    "_RequiredListUsersInGroupRequestTypeDef",
    {
        "UserPoolId": str,
        "GroupName": str,
    },
)
_OptionalListUsersInGroupRequestTypeDef = TypedDict(
    "_OptionalListUsersInGroupRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class ListUsersInGroupRequestTypeDef(
    _RequiredListUsersInGroupRequestTypeDef, _OptionalListUsersInGroupRequestTypeDef
):
    pass


ListUsersInGroupResponseResponseTypeDef = TypedDict(
    "ListUsersInGroupResponseResponseTypeDef",
    {
        "Users": List["UserTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListUsersRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestTypeDef",
    {
        "AttributesToGet": List[str],
        "Limit": int,
        "PaginationToken": str,
        "Filter": str,
    },
    total=False,
)


class ListUsersRequestTypeDef(_RequiredListUsersRequestTypeDef, _OptionalListUsersRequestTypeDef):
    pass


ListUsersResponseResponseTypeDef = TypedDict(
    "ListUsersResponseResponseTypeDef",
    {
        "Users": List["UserTypeTypeDef"],
        "PaginationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MFAOptionTypeTypeDef = TypedDict(
    "MFAOptionTypeTypeDef",
    {
        "DeliveryMedium": DeliveryMediumTypeType,
        "AttributeName": str,
    },
    total=False,
)

MessageTemplateTypeTypeDef = TypedDict(
    "MessageTemplateTypeTypeDef",
    {
        "SMSMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
    },
    total=False,
)

NewDeviceMetadataTypeTypeDef = TypedDict(
    "NewDeviceMetadataTypeTypeDef",
    {
        "DeviceKey": str,
        "DeviceGroupKey": str,
    },
    total=False,
)

_RequiredNotifyConfigurationTypeTypeDef = TypedDict(
    "_RequiredNotifyConfigurationTypeTypeDef",
    {
        "SourceArn": str,
    },
)
_OptionalNotifyConfigurationTypeTypeDef = TypedDict(
    "_OptionalNotifyConfigurationTypeTypeDef",
    {
        "From": str,
        "ReplyTo": str,
        "BlockEmail": "NotifyEmailTypeTypeDef",
        "NoActionEmail": "NotifyEmailTypeTypeDef",
        "MfaEmail": "NotifyEmailTypeTypeDef",
    },
    total=False,
)


class NotifyConfigurationTypeTypeDef(
    _RequiredNotifyConfigurationTypeTypeDef, _OptionalNotifyConfigurationTypeTypeDef
):
    pass


_RequiredNotifyEmailTypeTypeDef = TypedDict(
    "_RequiredNotifyEmailTypeTypeDef",
    {
        "Subject": str,
    },
)
_OptionalNotifyEmailTypeTypeDef = TypedDict(
    "_OptionalNotifyEmailTypeTypeDef",
    {
        "HtmlBody": str,
        "TextBody": str,
    },
    total=False,
)


class NotifyEmailTypeTypeDef(_RequiredNotifyEmailTypeTypeDef, _OptionalNotifyEmailTypeTypeDef):
    pass


NumberAttributeConstraintsTypeTypeDef = TypedDict(
    "NumberAttributeConstraintsTypeTypeDef",
    {
        "MinValue": str,
        "MaxValue": str,
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

PasswordPolicyTypeTypeDef = TypedDict(
    "PasswordPolicyTypeTypeDef",
    {
        "MinimumLength": int,
        "RequireUppercase": bool,
        "RequireLowercase": bool,
        "RequireNumbers": bool,
        "RequireSymbols": bool,
        "TemporaryPasswordValidityDays": int,
    },
    total=False,
)

ProviderDescriptionTypeDef = TypedDict(
    "ProviderDescriptionTypeDef",
    {
        "ProviderName": str,
        "ProviderType": IdentityProviderTypeTypeType,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

ProviderUserIdentifierTypeTypeDef = TypedDict(
    "ProviderUserIdentifierTypeTypeDef",
    {
        "ProviderName": str,
        "ProviderAttributeName": str,
        "ProviderAttributeValue": str,
    },
    total=False,
)

RecoveryOptionTypeTypeDef = TypedDict(
    "RecoveryOptionTypeTypeDef",
    {
        "Priority": int,
        "Name": RecoveryOptionNameTypeType,
    },
)

_RequiredResendConfirmationCodeRequestTypeDef = TypedDict(
    "_RequiredResendConfirmationCodeRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
    },
)
_OptionalResendConfirmationCodeRequestTypeDef = TypedDict(
    "_OptionalResendConfirmationCodeRequestTypeDef",
    {
        "SecretHash": str,
        "UserContextData": "UserContextDataTypeTypeDef",
        "AnalyticsMetadata": "AnalyticsMetadataTypeTypeDef",
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)


class ResendConfirmationCodeRequestTypeDef(
    _RequiredResendConfirmationCodeRequestTypeDef, _OptionalResendConfirmationCodeRequestTypeDef
):
    pass


ResendConfirmationCodeResponseResponseTypeDef = TypedDict(
    "ResendConfirmationCodeResponseResponseTypeDef",
    {
        "CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceServerScopeTypeTypeDef = TypedDict(
    "ResourceServerScopeTypeTypeDef",
    {
        "ScopeName": str,
        "ScopeDescription": str,
    },
)

ResourceServerTypeTypeDef = TypedDict(
    "ResourceServerTypeTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": List["ResourceServerScopeTypeTypeDef"],
    },
    total=False,
)

_RequiredRespondToAuthChallengeRequestTypeDef = TypedDict(
    "_RequiredRespondToAuthChallengeRequestTypeDef",
    {
        "ClientId": str,
        "ChallengeName": ChallengeNameTypeType,
    },
)
_OptionalRespondToAuthChallengeRequestTypeDef = TypedDict(
    "_OptionalRespondToAuthChallengeRequestTypeDef",
    {
        "Session": str,
        "ChallengeResponses": Dict[str, str],
        "AnalyticsMetadata": "AnalyticsMetadataTypeTypeDef",
        "UserContextData": "UserContextDataTypeTypeDef",
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)


class RespondToAuthChallengeRequestTypeDef(
    _RequiredRespondToAuthChallengeRequestTypeDef, _OptionalRespondToAuthChallengeRequestTypeDef
):
    pass


RespondToAuthChallengeResponseResponseTypeDef = TypedDict(
    "RespondToAuthChallengeResponseResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
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

_RequiredRevokeTokenRequestTypeDef = TypedDict(
    "_RequiredRevokeTokenRequestTypeDef",
    {
        "Token": str,
        "ClientId": str,
    },
)
_OptionalRevokeTokenRequestTypeDef = TypedDict(
    "_OptionalRevokeTokenRequestTypeDef",
    {
        "ClientSecret": str,
    },
    total=False,
)


class RevokeTokenRequestTypeDef(
    _RequiredRevokeTokenRequestTypeDef, _OptionalRevokeTokenRequestTypeDef
):
    pass


RiskConfigurationTypeTypeDef = TypedDict(
    "RiskConfigurationTypeTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "CompromisedCredentialsRiskConfiguration": "CompromisedCredentialsRiskConfigurationTypeTypeDef",
        "AccountTakeoverRiskConfiguration": "AccountTakeoverRiskConfigurationTypeTypeDef",
        "RiskExceptionConfiguration": "RiskExceptionConfigurationTypeTypeDef",
        "LastModifiedDate": datetime,
    },
    total=False,
)

RiskExceptionConfigurationTypeTypeDef = TypedDict(
    "RiskExceptionConfigurationTypeTypeDef",
    {
        "BlockedIPRangeList": List[str],
        "SkippedIPRangeList": List[str],
    },
    total=False,
)

SMSMfaSettingsTypeTypeDef = TypedDict(
    "SMSMfaSettingsTypeTypeDef",
    {
        "Enabled": bool,
        "PreferredMfa": bool,
    },
    total=False,
)

SchemaAttributeTypeTypeDef = TypedDict(
    "SchemaAttributeTypeTypeDef",
    {
        "Name": str,
        "AttributeDataType": AttributeDataTypeType,
        "DeveloperOnlyAttribute": bool,
        "Mutable": bool,
        "Required": bool,
        "NumberAttributeConstraints": "NumberAttributeConstraintsTypeTypeDef",
        "StringAttributeConstraints": "StringAttributeConstraintsTypeTypeDef",
    },
    total=False,
)

_RequiredSetRiskConfigurationRequestTypeDef = TypedDict(
    "_RequiredSetRiskConfigurationRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalSetRiskConfigurationRequestTypeDef = TypedDict(
    "_OptionalSetRiskConfigurationRequestTypeDef",
    {
        "ClientId": str,
        "CompromisedCredentialsRiskConfiguration": "CompromisedCredentialsRiskConfigurationTypeTypeDef",
        "AccountTakeoverRiskConfiguration": "AccountTakeoverRiskConfigurationTypeTypeDef",
        "RiskExceptionConfiguration": "RiskExceptionConfigurationTypeTypeDef",
    },
    total=False,
)


class SetRiskConfigurationRequestTypeDef(
    _RequiredSetRiskConfigurationRequestTypeDef, _OptionalSetRiskConfigurationRequestTypeDef
):
    pass


SetRiskConfigurationResponseResponseTypeDef = TypedDict(
    "SetRiskConfigurationResponseResponseTypeDef",
    {
        "RiskConfiguration": "RiskConfigurationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSetUICustomizationRequestTypeDef = TypedDict(
    "_RequiredSetUICustomizationRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalSetUICustomizationRequestTypeDef = TypedDict(
    "_OptionalSetUICustomizationRequestTypeDef",
    {
        "ClientId": str,
        "CSS": str,
        "ImageFile": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)


class SetUICustomizationRequestTypeDef(
    _RequiredSetUICustomizationRequestTypeDef, _OptionalSetUICustomizationRequestTypeDef
):
    pass


SetUICustomizationResponseResponseTypeDef = TypedDict(
    "SetUICustomizationResponseResponseTypeDef",
    {
        "UICustomization": "UICustomizationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSetUserMFAPreferenceRequestTypeDef = TypedDict(
    "_RequiredSetUserMFAPreferenceRequestTypeDef",
    {
        "AccessToken": str,
    },
)
_OptionalSetUserMFAPreferenceRequestTypeDef = TypedDict(
    "_OptionalSetUserMFAPreferenceRequestTypeDef",
    {
        "SMSMfaSettings": "SMSMfaSettingsTypeTypeDef",
        "SoftwareTokenMfaSettings": "SoftwareTokenMfaSettingsTypeTypeDef",
    },
    total=False,
)


class SetUserMFAPreferenceRequestTypeDef(
    _RequiredSetUserMFAPreferenceRequestTypeDef, _OptionalSetUserMFAPreferenceRequestTypeDef
):
    pass


_RequiredSetUserPoolMfaConfigRequestTypeDef = TypedDict(
    "_RequiredSetUserPoolMfaConfigRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalSetUserPoolMfaConfigRequestTypeDef = TypedDict(
    "_OptionalSetUserPoolMfaConfigRequestTypeDef",
    {
        "SmsMfaConfiguration": "SmsMfaConfigTypeTypeDef",
        "SoftwareTokenMfaConfiguration": "SoftwareTokenMfaConfigTypeTypeDef",
        "MfaConfiguration": UserPoolMfaTypeType,
    },
    total=False,
)


class SetUserPoolMfaConfigRequestTypeDef(
    _RequiredSetUserPoolMfaConfigRequestTypeDef, _OptionalSetUserPoolMfaConfigRequestTypeDef
):
    pass


SetUserPoolMfaConfigResponseResponseTypeDef = TypedDict(
    "SetUserPoolMfaConfigResponseResponseTypeDef",
    {
        "SmsMfaConfiguration": "SmsMfaConfigTypeTypeDef",
        "SoftwareTokenMfaConfiguration": "SoftwareTokenMfaConfigTypeTypeDef",
        "MfaConfiguration": UserPoolMfaTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetUserSettingsRequestTypeDef = TypedDict(
    "SetUserSettingsRequestTypeDef",
    {
        "AccessToken": str,
        "MFAOptions": List["MFAOptionTypeTypeDef"],
    },
)

_RequiredSignUpRequestTypeDef = TypedDict(
    "_RequiredSignUpRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
        "Password": str,
    },
)
_OptionalSignUpRequestTypeDef = TypedDict(
    "_OptionalSignUpRequestTypeDef",
    {
        "SecretHash": str,
        "UserAttributes": List["AttributeTypeTypeDef"],
        "ValidationData": List["AttributeTypeTypeDef"],
        "AnalyticsMetadata": "AnalyticsMetadataTypeTypeDef",
        "UserContextData": "UserContextDataTypeTypeDef",
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)


class SignUpRequestTypeDef(_RequiredSignUpRequestTypeDef, _OptionalSignUpRequestTypeDef):
    pass


SignUpResponseResponseTypeDef = TypedDict(
    "SignUpResponseResponseTypeDef",
    {
        "UserConfirmed": bool,
        "CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef",
        "UserSub": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSmsConfigurationTypeTypeDef = TypedDict(
    "_RequiredSmsConfigurationTypeTypeDef",
    {
        "SnsCallerArn": str,
    },
)
_OptionalSmsConfigurationTypeTypeDef = TypedDict(
    "_OptionalSmsConfigurationTypeTypeDef",
    {
        "ExternalId": str,
    },
    total=False,
)


class SmsConfigurationTypeTypeDef(
    _RequiredSmsConfigurationTypeTypeDef, _OptionalSmsConfigurationTypeTypeDef
):
    pass


SmsMfaConfigTypeTypeDef = TypedDict(
    "SmsMfaConfigTypeTypeDef",
    {
        "SmsAuthenticationMessage": str,
        "SmsConfiguration": "SmsConfigurationTypeTypeDef",
    },
    total=False,
)

SoftwareTokenMfaConfigTypeTypeDef = TypedDict(
    "SoftwareTokenMfaConfigTypeTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

SoftwareTokenMfaSettingsTypeTypeDef = TypedDict(
    "SoftwareTokenMfaSettingsTypeTypeDef",
    {
        "Enabled": bool,
        "PreferredMfa": bool,
    },
    total=False,
)

StartUserImportJobRequestTypeDef = TypedDict(
    "StartUserImportJobRequestTypeDef",
    {
        "UserPoolId": str,
        "JobId": str,
    },
)

StartUserImportJobResponseResponseTypeDef = TypedDict(
    "StartUserImportJobResponseResponseTypeDef",
    {
        "UserImportJob": "UserImportJobTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopUserImportJobRequestTypeDef = TypedDict(
    "StopUserImportJobRequestTypeDef",
    {
        "UserPoolId": str,
        "JobId": str,
    },
)

StopUserImportJobResponseResponseTypeDef = TypedDict(
    "StopUserImportJobResponseResponseTypeDef",
    {
        "UserImportJob": "UserImportJobTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StringAttributeConstraintsTypeTypeDef = TypedDict(
    "StringAttributeConstraintsTypeTypeDef",
    {
        "MinLength": str,
        "MaxLength": str,
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

TokenValidityUnitsTypeTypeDef = TypedDict(
    "TokenValidityUnitsTypeTypeDef",
    {
        "AccessToken": TimeUnitsTypeType,
        "IdToken": TimeUnitsTypeType,
        "RefreshToken": TimeUnitsTypeType,
    },
    total=False,
)

UICustomizationTypeTypeDef = TypedDict(
    "UICustomizationTypeTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "ImageUrl": str,
        "CSS": str,
        "CSSVersion": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateAuthEventFeedbackRequestTypeDef = TypedDict(
    "UpdateAuthEventFeedbackRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "EventId": str,
        "FeedbackToken": str,
        "FeedbackValue": FeedbackValueTypeType,
    },
)

_RequiredUpdateDeviceStatusRequestTypeDef = TypedDict(
    "_RequiredUpdateDeviceStatusRequestTypeDef",
    {
        "AccessToken": str,
        "DeviceKey": str,
    },
)
_OptionalUpdateDeviceStatusRequestTypeDef = TypedDict(
    "_OptionalUpdateDeviceStatusRequestTypeDef",
    {
        "DeviceRememberedStatus": DeviceRememberedStatusTypeType,
    },
    total=False,
)


class UpdateDeviceStatusRequestTypeDef(
    _RequiredUpdateDeviceStatusRequestTypeDef, _OptionalUpdateDeviceStatusRequestTypeDef
):
    pass


_RequiredUpdateGroupRequestTypeDef = TypedDict(
    "_RequiredUpdateGroupRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
    },
)
_OptionalUpdateGroupRequestTypeDef = TypedDict(
    "_OptionalUpdateGroupRequestTypeDef",
    {
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
    },
    total=False,
)


class UpdateGroupRequestTypeDef(
    _RequiredUpdateGroupRequestTypeDef, _OptionalUpdateGroupRequestTypeDef
):
    pass


UpdateGroupResponseResponseTypeDef = TypedDict(
    "UpdateGroupResponseResponseTypeDef",
    {
        "Group": "GroupTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateIdentityProviderRequestTypeDef = TypedDict(
    "_RequiredUpdateIdentityProviderRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
    },
)
_OptionalUpdateIdentityProviderRequestTypeDef = TypedDict(
    "_OptionalUpdateIdentityProviderRequestTypeDef",
    {
        "ProviderDetails": Dict[str, str],
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
    },
    total=False,
)


class UpdateIdentityProviderRequestTypeDef(
    _RequiredUpdateIdentityProviderRequestTypeDef, _OptionalUpdateIdentityProviderRequestTypeDef
):
    pass


UpdateIdentityProviderResponseResponseTypeDef = TypedDict(
    "UpdateIdentityProviderResponseResponseTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateResourceServerRequestTypeDef = TypedDict(
    "_RequiredUpdateResourceServerRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
    },
)
_OptionalUpdateResourceServerRequestTypeDef = TypedDict(
    "_OptionalUpdateResourceServerRequestTypeDef",
    {
        "Scopes": List["ResourceServerScopeTypeTypeDef"],
    },
    total=False,
)


class UpdateResourceServerRequestTypeDef(
    _RequiredUpdateResourceServerRequestTypeDef, _OptionalUpdateResourceServerRequestTypeDef
):
    pass


UpdateResourceServerResponseResponseTypeDef = TypedDict(
    "UpdateResourceServerResponseResponseTypeDef",
    {
        "ResourceServer": "ResourceServerTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserAttributesRequestTypeDef = TypedDict(
    "_RequiredUpdateUserAttributesRequestTypeDef",
    {
        "UserAttributes": List["AttributeTypeTypeDef"],
        "AccessToken": str,
    },
)
_OptionalUpdateUserAttributesRequestTypeDef = TypedDict(
    "_OptionalUpdateUserAttributesRequestTypeDef",
    {
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)


class UpdateUserAttributesRequestTypeDef(
    _RequiredUpdateUserAttributesRequestTypeDef, _OptionalUpdateUserAttributesRequestTypeDef
):
    pass


UpdateUserAttributesResponseResponseTypeDef = TypedDict(
    "UpdateUserAttributesResponseResponseTypeDef",
    {
        "CodeDeliveryDetailsList": List["CodeDeliveryDetailsTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserPoolClientRequestTypeDef = TypedDict(
    "_RequiredUpdateUserPoolClientRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
    },
)
_OptionalUpdateUserPoolClientRequestTypeDef = TypedDict(
    "_OptionalUpdateUserPoolClientRequestTypeDef",
    {
        "ClientName": str,
        "RefreshTokenValidity": int,
        "AccessTokenValidity": int,
        "IdTokenValidity": int,
        "TokenValidityUnits": "TokenValidityUnitsTypeTypeDef",
        "ReadAttributes": List[str],
        "WriteAttributes": List[str],
        "ExplicitAuthFlows": List[ExplicitAuthFlowsTypeType],
        "SupportedIdentityProviders": List[str],
        "CallbackURLs": List[str],
        "LogoutURLs": List[str],
        "DefaultRedirectURI": str,
        "AllowedOAuthFlows": List[OAuthFlowTypeType],
        "AllowedOAuthScopes": List[str],
        "AllowedOAuthFlowsUserPoolClient": bool,
        "AnalyticsConfiguration": "AnalyticsConfigurationTypeTypeDef",
        "PreventUserExistenceErrors": PreventUserExistenceErrorTypesType,
        "EnableTokenRevocation": bool,
    },
    total=False,
)


class UpdateUserPoolClientRequestTypeDef(
    _RequiredUpdateUserPoolClientRequestTypeDef, _OptionalUpdateUserPoolClientRequestTypeDef
):
    pass


UpdateUserPoolClientResponseResponseTypeDef = TypedDict(
    "UpdateUserPoolClientResponseResponseTypeDef",
    {
        "UserPoolClient": "UserPoolClientTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserPoolDomainRequestTypeDef = TypedDict(
    "UpdateUserPoolDomainRequestTypeDef",
    {
        "Domain": str,
        "UserPoolId": str,
        "CustomDomainConfig": "CustomDomainConfigTypeTypeDef",
    },
)

UpdateUserPoolDomainResponseResponseTypeDef = TypedDict(
    "UpdateUserPoolDomainResponseResponseTypeDef",
    {
        "CloudFrontDomain": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserPoolRequestTypeDef = TypedDict(
    "_RequiredUpdateUserPoolRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalUpdateUserPoolRequestTypeDef = TypedDict(
    "_OptionalUpdateUserPoolRequestTypeDef",
    {
        "Policies": "UserPoolPolicyTypeTypeDef",
        "LambdaConfig": "LambdaConfigTypeTypeDef",
        "AutoVerifiedAttributes": List[VerifiedAttributeTypeType],
        "SmsVerificationMessage": str,
        "EmailVerificationMessage": str,
        "EmailVerificationSubject": str,
        "VerificationMessageTemplate": "VerificationMessageTemplateTypeTypeDef",
        "SmsAuthenticationMessage": str,
        "MfaConfiguration": UserPoolMfaTypeType,
        "DeviceConfiguration": "DeviceConfigurationTypeTypeDef",
        "EmailConfiguration": "EmailConfigurationTypeTypeDef",
        "SmsConfiguration": "SmsConfigurationTypeTypeDef",
        "UserPoolTags": Dict[str, str],
        "AdminCreateUserConfig": "AdminCreateUserConfigTypeTypeDef",
        "UserPoolAddOns": "UserPoolAddOnsTypeTypeDef",
        "AccountRecoverySetting": "AccountRecoverySettingTypeTypeDef",
    },
    total=False,
)


class UpdateUserPoolRequestTypeDef(
    _RequiredUpdateUserPoolRequestTypeDef, _OptionalUpdateUserPoolRequestTypeDef
):
    pass


UserContextDataTypeTypeDef = TypedDict(
    "UserContextDataTypeTypeDef",
    {
        "EncodedData": str,
    },
    total=False,
)

UserImportJobTypeTypeDef = TypedDict(
    "UserImportJobTypeTypeDef",
    {
        "JobName": str,
        "JobId": str,
        "UserPoolId": str,
        "PreSignedUrl": str,
        "CreationDate": datetime,
        "StartDate": datetime,
        "CompletionDate": datetime,
        "Status": UserImportJobStatusTypeType,
        "CloudWatchLogsRoleArn": str,
        "ImportedUsers": int,
        "SkippedUsers": int,
        "FailedUsers": int,
        "CompletionMessage": str,
    },
    total=False,
)

UserPoolAddOnsTypeTypeDef = TypedDict(
    "UserPoolAddOnsTypeTypeDef",
    {
        "AdvancedSecurityMode": AdvancedSecurityModeTypeType,
    },
)

UserPoolClientDescriptionTypeDef = TypedDict(
    "UserPoolClientDescriptionTypeDef",
    {
        "ClientId": str,
        "UserPoolId": str,
        "ClientName": str,
    },
    total=False,
)

UserPoolClientTypeTypeDef = TypedDict(
    "UserPoolClientTypeTypeDef",
    {
        "UserPoolId": str,
        "ClientName": str,
        "ClientId": str,
        "ClientSecret": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "RefreshTokenValidity": int,
        "AccessTokenValidity": int,
        "IdTokenValidity": int,
        "TokenValidityUnits": "TokenValidityUnitsTypeTypeDef",
        "ReadAttributes": List[str],
        "WriteAttributes": List[str],
        "ExplicitAuthFlows": List[ExplicitAuthFlowsTypeType],
        "SupportedIdentityProviders": List[str],
        "CallbackURLs": List[str],
        "LogoutURLs": List[str],
        "DefaultRedirectURI": str,
        "AllowedOAuthFlows": List[OAuthFlowTypeType],
        "AllowedOAuthScopes": List[str],
        "AllowedOAuthFlowsUserPoolClient": bool,
        "AnalyticsConfiguration": "AnalyticsConfigurationTypeTypeDef",
        "PreventUserExistenceErrors": PreventUserExistenceErrorTypesType,
        "EnableTokenRevocation": bool,
    },
    total=False,
)

UserPoolDescriptionTypeTypeDef = TypedDict(
    "UserPoolDescriptionTypeTypeDef",
    {
        "Id": str,
        "Name": str,
        "LambdaConfig": "LambdaConfigTypeTypeDef",
        "Status": StatusTypeType,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

UserPoolPolicyTypeTypeDef = TypedDict(
    "UserPoolPolicyTypeTypeDef",
    {
        "PasswordPolicy": "PasswordPolicyTypeTypeDef",
    },
    total=False,
)

UserPoolTypeTypeDef = TypedDict(
    "UserPoolTypeTypeDef",
    {
        "Id": str,
        "Name": str,
        "Policies": "UserPoolPolicyTypeTypeDef",
        "LambdaConfig": "LambdaConfigTypeTypeDef",
        "Status": StatusTypeType,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "SchemaAttributes": List["SchemaAttributeTypeTypeDef"],
        "AutoVerifiedAttributes": List[VerifiedAttributeTypeType],
        "AliasAttributes": List[AliasAttributeTypeType],
        "UsernameAttributes": List[UsernameAttributeTypeType],
        "SmsVerificationMessage": str,
        "EmailVerificationMessage": str,
        "EmailVerificationSubject": str,
        "VerificationMessageTemplate": "VerificationMessageTemplateTypeTypeDef",
        "SmsAuthenticationMessage": str,
        "MfaConfiguration": UserPoolMfaTypeType,
        "DeviceConfiguration": "DeviceConfigurationTypeTypeDef",
        "EstimatedNumberOfUsers": int,
        "EmailConfiguration": "EmailConfigurationTypeTypeDef",
        "SmsConfiguration": "SmsConfigurationTypeTypeDef",
        "UserPoolTags": Dict[str, str],
        "SmsConfigurationFailure": str,
        "EmailConfigurationFailure": str,
        "Domain": str,
        "CustomDomain": str,
        "AdminCreateUserConfig": "AdminCreateUserConfigTypeTypeDef",
        "UserPoolAddOns": "UserPoolAddOnsTypeTypeDef",
        "UsernameConfiguration": "UsernameConfigurationTypeTypeDef",
        "Arn": str,
        "AccountRecoverySetting": "AccountRecoverySettingTypeTypeDef",
    },
    total=False,
)

UserTypeTypeDef = TypedDict(
    "UserTypeTypeDef",
    {
        "Username": str,
        "Attributes": List["AttributeTypeTypeDef"],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": UserStatusTypeType,
        "MFAOptions": List["MFAOptionTypeTypeDef"],
    },
    total=False,
)

UsernameConfigurationTypeTypeDef = TypedDict(
    "UsernameConfigurationTypeTypeDef",
    {
        "CaseSensitive": bool,
    },
)

VerificationMessageTemplateTypeTypeDef = TypedDict(
    "VerificationMessageTemplateTypeTypeDef",
    {
        "SmsMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
        "EmailMessageByLink": str,
        "EmailSubjectByLink": str,
        "DefaultEmailOption": DefaultEmailOptionTypeType,
    },
    total=False,
)

_RequiredVerifySoftwareTokenRequestTypeDef = TypedDict(
    "_RequiredVerifySoftwareTokenRequestTypeDef",
    {
        "UserCode": str,
    },
)
_OptionalVerifySoftwareTokenRequestTypeDef = TypedDict(
    "_OptionalVerifySoftwareTokenRequestTypeDef",
    {
        "AccessToken": str,
        "Session": str,
        "FriendlyDeviceName": str,
    },
    total=False,
)


class VerifySoftwareTokenRequestTypeDef(
    _RequiredVerifySoftwareTokenRequestTypeDef, _OptionalVerifySoftwareTokenRequestTypeDef
):
    pass


VerifySoftwareTokenResponseResponseTypeDef = TypedDict(
    "VerifySoftwareTokenResponseResponseTypeDef",
    {
        "Status": VerifySoftwareTokenResponseTypeType,
        "Session": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VerifyUserAttributeRequestTypeDef = TypedDict(
    "VerifyUserAttributeRequestTypeDef",
    {
        "AccessToken": str,
        "AttributeName": str,
        "Code": str,
    },
)
