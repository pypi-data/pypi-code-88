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
from typing import Dict, List

from .literals import (
    AccountTakeoverEventActionTypeType,
    AdvancedSecurityModeTypeType,
    AliasAttributeTypeType,
    AttributeDataTypeType,
    ChallengeNameType,
    ChallengeNameTypeType,
    ChallengeResponseType,
    CompromisedCredentialsEventActionTypeType,
    DefaultEmailOptionTypeType,
    DeliveryMediumTypeType,
    DomainStatusTypeType,
    EmailSendingAccountTypeType,
    EventFilterTypeType,
    EventResponseTypeType,
    EventTypeType,
    ExplicitAuthFlowsTypeType,
    FeedbackValueTypeType,
    IdentityProviderTypeTypeType,
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
    "AdminCreateUserConfigTypeTypeDef",
    "AdminCreateUserResponseTypeDef",
    "AdminGetDeviceResponseTypeDef",
    "AdminGetUserResponseTypeDef",
    "AdminInitiateAuthResponseTypeDef",
    "AdminListDevicesResponseTypeDef",
    "AdminListGroupsForUserResponseTypeDef",
    "AdminListUserAuthEventsResponseTypeDef",
    "AdminRespondToAuthChallengeResponseTypeDef",
    "AnalyticsConfigurationTypeTypeDef",
    "AnalyticsMetadataTypeTypeDef",
    "AssociateSoftwareTokenResponseTypeDef",
    "AttributeTypeTypeDef",
    "AuthEventTypeTypeDef",
    "AuthenticationResultTypeTypeDef",
    "ChallengeResponseTypeTypeDef",
    "CodeDeliveryDetailsTypeTypeDef",
    "CompromisedCredentialsActionsTypeTypeDef",
    "CompromisedCredentialsRiskConfigurationTypeTypeDef",
    "ConfirmDeviceResponseTypeDef",
    "ContextDataTypeTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateIdentityProviderResponseTypeDef",
    "CreateResourceServerResponseTypeDef",
    "CreateUserImportJobResponseTypeDef",
    "CreateUserPoolClientResponseTypeDef",
    "CreateUserPoolDomainResponseTypeDef",
    "CreateUserPoolResponseTypeDef",
    "CustomDomainConfigTypeTypeDef",
    "CustomEmailLambdaVersionConfigTypeTypeDef",
    "CustomSMSLambdaVersionConfigTypeTypeDef",
    "DescribeIdentityProviderResponseTypeDef",
    "DescribeResourceServerResponseTypeDef",
    "DescribeRiskConfigurationResponseTypeDef",
    "DescribeUserImportJobResponseTypeDef",
    "DescribeUserPoolClientResponseTypeDef",
    "DescribeUserPoolDomainResponseTypeDef",
    "DescribeUserPoolResponseTypeDef",
    "DeviceConfigurationTypeTypeDef",
    "DeviceSecretVerifierConfigTypeTypeDef",
    "DeviceTypeTypeDef",
    "DomainDescriptionTypeTypeDef",
    "EmailConfigurationTypeTypeDef",
    "EventContextDataTypeTypeDef",
    "EventFeedbackTypeTypeDef",
    "EventRiskTypeTypeDef",
    "ForgotPasswordResponseTypeDef",
    "GetCSVHeaderResponseTypeDef",
    "GetDeviceResponseTypeDef",
    "GetGroupResponseTypeDef",
    "GetIdentityProviderByIdentifierResponseTypeDef",
    "GetSigningCertificateResponseTypeDef",
    "GetUICustomizationResponseTypeDef",
    "GetUserAttributeVerificationCodeResponseTypeDef",
    "GetUserPoolMfaConfigResponseTypeDef",
    "GetUserResponseTypeDef",
    "GroupTypeTypeDef",
    "HttpHeaderTypeDef",
    "IdentityProviderTypeTypeDef",
    "InitiateAuthResponseTypeDef",
    "LambdaConfigTypeTypeDef",
    "ListDevicesResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "ListIdentityProvidersResponseTypeDef",
    "ListResourceServersResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUserImportJobsResponseTypeDef",
    "ListUserPoolClientsResponseTypeDef",
    "ListUserPoolsResponseTypeDef",
    "ListUsersInGroupResponseTypeDef",
    "ListUsersResponseTypeDef",
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
    "ResendConfirmationCodeResponseTypeDef",
    "ResourceServerScopeTypeTypeDef",
    "ResourceServerTypeTypeDef",
    "RespondToAuthChallengeResponseTypeDef",
    "RiskConfigurationTypeTypeDef",
    "RiskExceptionConfigurationTypeTypeDef",
    "SMSMfaSettingsTypeTypeDef",
    "SchemaAttributeTypeTypeDef",
    "SetRiskConfigurationResponseTypeDef",
    "SetUICustomizationResponseTypeDef",
    "SetUserPoolMfaConfigResponseTypeDef",
    "SignUpResponseTypeDef",
    "SmsConfigurationTypeTypeDef",
    "SmsMfaConfigTypeTypeDef",
    "SoftwareTokenMfaConfigTypeTypeDef",
    "SoftwareTokenMfaSettingsTypeTypeDef",
    "StartUserImportJobResponseTypeDef",
    "StopUserImportJobResponseTypeDef",
    "StringAttributeConstraintsTypeTypeDef",
    "TokenValidityUnitsTypeTypeDef",
    "UICustomizationTypeTypeDef",
    "UpdateGroupResponseTypeDef",
    "UpdateIdentityProviderResponseTypeDef",
    "UpdateResourceServerResponseTypeDef",
    "UpdateUserAttributesResponseTypeDef",
    "UpdateUserPoolClientResponseTypeDef",
    "UpdateUserPoolDomainResponseTypeDef",
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
    "VerifySoftwareTokenResponseTypeDef",
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


AdminCreateUserConfigTypeTypeDef = TypedDict(
    "AdminCreateUserConfigTypeTypeDef",
    {
        "AllowAdminCreateUserOnly": bool,
        "UnusedAccountValidityDays": int,
        "InviteMessageTemplate": "MessageTemplateTypeTypeDef",
    },
    total=False,
)

AdminCreateUserResponseTypeDef = TypedDict(
    "AdminCreateUserResponseTypeDef",
    {
        "User": "UserTypeTypeDef",
    },
    total=False,
)

AdminGetDeviceResponseTypeDef = TypedDict(
    "AdminGetDeviceResponseTypeDef",
    {
        "Device": "DeviceTypeTypeDef",
    },
)

_RequiredAdminGetUserResponseTypeDef = TypedDict(
    "_RequiredAdminGetUserResponseTypeDef",
    {
        "Username": str,
    },
)
_OptionalAdminGetUserResponseTypeDef = TypedDict(
    "_OptionalAdminGetUserResponseTypeDef",
    {
        "UserAttributes": List["AttributeTypeTypeDef"],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": UserStatusTypeType,
        "MFAOptions": List["MFAOptionTypeTypeDef"],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
    },
    total=False,
)


class AdminGetUserResponseTypeDef(
    _RequiredAdminGetUserResponseTypeDef, _OptionalAdminGetUserResponseTypeDef
):
    pass


AdminInitiateAuthResponseTypeDef = TypedDict(
    "AdminInitiateAuthResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
    },
    total=False,
)

AdminListDevicesResponseTypeDef = TypedDict(
    "AdminListDevicesResponseTypeDef",
    {
        "Devices": List["DeviceTypeTypeDef"],
        "PaginationToken": str,
    },
    total=False,
)

AdminListGroupsForUserResponseTypeDef = TypedDict(
    "AdminListGroupsForUserResponseTypeDef",
    {
        "Groups": List["GroupTypeTypeDef"],
        "NextToken": str,
    },
    total=False,
)

AdminListUserAuthEventsResponseTypeDef = TypedDict(
    "AdminListUserAuthEventsResponseTypeDef",
    {
        "AuthEvents": List["AuthEventTypeTypeDef"],
        "NextToken": str,
    },
    total=False,
)

AdminRespondToAuthChallengeResponseTypeDef = TypedDict(
    "AdminRespondToAuthChallengeResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
    },
    total=False,
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

AssociateSoftwareTokenResponseTypeDef = TypedDict(
    "AssociateSoftwareTokenResponseTypeDef",
    {
        "SecretCode": str,
        "Session": str,
    },
    total=False,
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


ConfirmDeviceResponseTypeDef = TypedDict(
    "ConfirmDeviceResponseTypeDef",
    {
        "UserConfirmationNecessary": bool,
    },
    total=False,
)

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


CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "Group": "GroupTypeTypeDef",
    },
    total=False,
)

CreateIdentityProviderResponseTypeDef = TypedDict(
    "CreateIdentityProviderResponseTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeTypeDef",
    },
)

CreateResourceServerResponseTypeDef = TypedDict(
    "CreateResourceServerResponseTypeDef",
    {
        "ResourceServer": "ResourceServerTypeTypeDef",
    },
)

CreateUserImportJobResponseTypeDef = TypedDict(
    "CreateUserImportJobResponseTypeDef",
    {
        "UserImportJob": "UserImportJobTypeTypeDef",
    },
    total=False,
)

CreateUserPoolClientResponseTypeDef = TypedDict(
    "CreateUserPoolClientResponseTypeDef",
    {
        "UserPoolClient": "UserPoolClientTypeTypeDef",
    },
    total=False,
)

CreateUserPoolDomainResponseTypeDef = TypedDict(
    "CreateUserPoolDomainResponseTypeDef",
    {
        "CloudFrontDomain": str,
    },
    total=False,
)

CreateUserPoolResponseTypeDef = TypedDict(
    "CreateUserPoolResponseTypeDef",
    {
        "UserPool": "UserPoolTypeTypeDef",
    },
    total=False,
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

DescribeIdentityProviderResponseTypeDef = TypedDict(
    "DescribeIdentityProviderResponseTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeTypeDef",
    },
)

DescribeResourceServerResponseTypeDef = TypedDict(
    "DescribeResourceServerResponseTypeDef",
    {
        "ResourceServer": "ResourceServerTypeTypeDef",
    },
)

DescribeRiskConfigurationResponseTypeDef = TypedDict(
    "DescribeRiskConfigurationResponseTypeDef",
    {
        "RiskConfiguration": "RiskConfigurationTypeTypeDef",
    },
)

DescribeUserImportJobResponseTypeDef = TypedDict(
    "DescribeUserImportJobResponseTypeDef",
    {
        "UserImportJob": "UserImportJobTypeTypeDef",
    },
    total=False,
)

DescribeUserPoolClientResponseTypeDef = TypedDict(
    "DescribeUserPoolClientResponseTypeDef",
    {
        "UserPoolClient": "UserPoolClientTypeTypeDef",
    },
    total=False,
)

DescribeUserPoolDomainResponseTypeDef = TypedDict(
    "DescribeUserPoolDomainResponseTypeDef",
    {
        "DomainDescription": "DomainDescriptionTypeTypeDef",
    },
    total=False,
)

DescribeUserPoolResponseTypeDef = TypedDict(
    "DescribeUserPoolResponseTypeDef",
    {
        "UserPool": "UserPoolTypeTypeDef",
    },
    total=False,
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

ForgotPasswordResponseTypeDef = TypedDict(
    "ForgotPasswordResponseTypeDef",
    {
        "CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef",
    },
    total=False,
)

GetCSVHeaderResponseTypeDef = TypedDict(
    "GetCSVHeaderResponseTypeDef",
    {
        "UserPoolId": str,
        "CSVHeader": List[str],
    },
    total=False,
)

GetDeviceResponseTypeDef = TypedDict(
    "GetDeviceResponseTypeDef",
    {
        "Device": "DeviceTypeTypeDef",
    },
)

GetGroupResponseTypeDef = TypedDict(
    "GetGroupResponseTypeDef",
    {
        "Group": "GroupTypeTypeDef",
    },
    total=False,
)

GetIdentityProviderByIdentifierResponseTypeDef = TypedDict(
    "GetIdentityProviderByIdentifierResponseTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeTypeDef",
    },
)

GetSigningCertificateResponseTypeDef = TypedDict(
    "GetSigningCertificateResponseTypeDef",
    {
        "Certificate": str,
    },
    total=False,
)

GetUICustomizationResponseTypeDef = TypedDict(
    "GetUICustomizationResponseTypeDef",
    {
        "UICustomization": "UICustomizationTypeTypeDef",
    },
)

GetUserAttributeVerificationCodeResponseTypeDef = TypedDict(
    "GetUserAttributeVerificationCodeResponseTypeDef",
    {
        "CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef",
    },
    total=False,
)

GetUserPoolMfaConfigResponseTypeDef = TypedDict(
    "GetUserPoolMfaConfigResponseTypeDef",
    {
        "SmsMfaConfiguration": "SmsMfaConfigTypeTypeDef",
        "SoftwareTokenMfaConfiguration": "SoftwareTokenMfaConfigTypeTypeDef",
        "MfaConfiguration": UserPoolMfaTypeType,
    },
    total=False,
)

_RequiredGetUserResponseTypeDef = TypedDict(
    "_RequiredGetUserResponseTypeDef",
    {
        "Username": str,
        "UserAttributes": List["AttributeTypeTypeDef"],
    },
)
_OptionalGetUserResponseTypeDef = TypedDict(
    "_OptionalGetUserResponseTypeDef",
    {
        "MFAOptions": List["MFAOptionTypeTypeDef"],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
    },
    total=False,
)


class GetUserResponseTypeDef(_RequiredGetUserResponseTypeDef, _OptionalGetUserResponseTypeDef):
    pass


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

InitiateAuthResponseTypeDef = TypedDict(
    "InitiateAuthResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
    },
    total=False,
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

ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {
        "Devices": List["DeviceTypeTypeDef"],
        "PaginationToken": str,
    },
    total=False,
)

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "Groups": List["GroupTypeTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredListIdentityProvidersResponseTypeDef = TypedDict(
    "_RequiredListIdentityProvidersResponseTypeDef",
    {
        "Providers": List["ProviderDescriptionTypeDef"],
    },
)
_OptionalListIdentityProvidersResponseTypeDef = TypedDict(
    "_OptionalListIdentityProvidersResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListIdentityProvidersResponseTypeDef(
    _RequiredListIdentityProvidersResponseTypeDef, _OptionalListIdentityProvidersResponseTypeDef
):
    pass


_RequiredListResourceServersResponseTypeDef = TypedDict(
    "_RequiredListResourceServersResponseTypeDef",
    {
        "ResourceServers": List["ResourceServerTypeTypeDef"],
    },
)
_OptionalListResourceServersResponseTypeDef = TypedDict(
    "_OptionalListResourceServersResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListResourceServersResponseTypeDef(
    _RequiredListResourceServersResponseTypeDef, _OptionalListResourceServersResponseTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

ListUserImportJobsResponseTypeDef = TypedDict(
    "ListUserImportJobsResponseTypeDef",
    {
        "UserImportJobs": List["UserImportJobTypeTypeDef"],
        "PaginationToken": str,
    },
    total=False,
)

ListUserPoolClientsResponseTypeDef = TypedDict(
    "ListUserPoolClientsResponseTypeDef",
    {
        "UserPoolClients": List["UserPoolClientDescriptionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListUserPoolsResponseTypeDef = TypedDict(
    "ListUserPoolsResponseTypeDef",
    {
        "UserPools": List["UserPoolDescriptionTypeTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListUsersInGroupResponseTypeDef = TypedDict(
    "ListUsersInGroupResponseTypeDef",
    {
        "Users": List["UserTypeTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "Users": List["UserTypeTypeDef"],
        "PaginationToken": str,
    },
    total=False,
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

ResendConfirmationCodeResponseTypeDef = TypedDict(
    "ResendConfirmationCodeResponseTypeDef",
    {
        "CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef",
    },
    total=False,
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

RespondToAuthChallengeResponseTypeDef = TypedDict(
    "RespondToAuthChallengeResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
    },
    total=False,
)

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

SetRiskConfigurationResponseTypeDef = TypedDict(
    "SetRiskConfigurationResponseTypeDef",
    {
        "RiskConfiguration": "RiskConfigurationTypeTypeDef",
    },
)

SetUICustomizationResponseTypeDef = TypedDict(
    "SetUICustomizationResponseTypeDef",
    {
        "UICustomization": "UICustomizationTypeTypeDef",
    },
)

SetUserPoolMfaConfigResponseTypeDef = TypedDict(
    "SetUserPoolMfaConfigResponseTypeDef",
    {
        "SmsMfaConfiguration": "SmsMfaConfigTypeTypeDef",
        "SoftwareTokenMfaConfiguration": "SoftwareTokenMfaConfigTypeTypeDef",
        "MfaConfiguration": UserPoolMfaTypeType,
    },
    total=False,
)

_RequiredSignUpResponseTypeDef = TypedDict(
    "_RequiredSignUpResponseTypeDef",
    {
        "UserConfirmed": bool,
        "UserSub": str,
    },
)
_OptionalSignUpResponseTypeDef = TypedDict(
    "_OptionalSignUpResponseTypeDef",
    {
        "CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef",
    },
    total=False,
)


class SignUpResponseTypeDef(_RequiredSignUpResponseTypeDef, _OptionalSignUpResponseTypeDef):
    pass


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

StartUserImportJobResponseTypeDef = TypedDict(
    "StartUserImportJobResponseTypeDef",
    {
        "UserImportJob": "UserImportJobTypeTypeDef",
    },
    total=False,
)

StopUserImportJobResponseTypeDef = TypedDict(
    "StopUserImportJobResponseTypeDef",
    {
        "UserImportJob": "UserImportJobTypeTypeDef",
    },
    total=False,
)

StringAttributeConstraintsTypeTypeDef = TypedDict(
    "StringAttributeConstraintsTypeTypeDef",
    {
        "MinLength": str,
        "MaxLength": str,
    },
    total=False,
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

UpdateGroupResponseTypeDef = TypedDict(
    "UpdateGroupResponseTypeDef",
    {
        "Group": "GroupTypeTypeDef",
    },
    total=False,
)

UpdateIdentityProviderResponseTypeDef = TypedDict(
    "UpdateIdentityProviderResponseTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeTypeDef",
    },
)

UpdateResourceServerResponseTypeDef = TypedDict(
    "UpdateResourceServerResponseTypeDef",
    {
        "ResourceServer": "ResourceServerTypeTypeDef",
    },
)

UpdateUserAttributesResponseTypeDef = TypedDict(
    "UpdateUserAttributesResponseTypeDef",
    {
        "CodeDeliveryDetailsList": List["CodeDeliveryDetailsTypeTypeDef"],
    },
    total=False,
)

UpdateUserPoolClientResponseTypeDef = TypedDict(
    "UpdateUserPoolClientResponseTypeDef",
    {
        "UserPoolClient": "UserPoolClientTypeTypeDef",
    },
    total=False,
)

UpdateUserPoolDomainResponseTypeDef = TypedDict(
    "UpdateUserPoolDomainResponseTypeDef",
    {
        "CloudFrontDomain": str,
    },
    total=False,
)

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

VerifySoftwareTokenResponseTypeDef = TypedDict(
    "VerifySoftwareTokenResponseTypeDef",
    {
        "Status": VerifySoftwareTokenResponseTypeType,
        "Session": str,
    },
    total=False,
)
