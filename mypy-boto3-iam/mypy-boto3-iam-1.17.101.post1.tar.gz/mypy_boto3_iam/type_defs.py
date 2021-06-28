"""
Type annotations for iam service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iam.type_defs import AccessDetailTypeDef

    data: AccessDetailTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AccessAdvisorUsageGranularityTypeType,
    ContextKeyTypeEnumType,
    DeletionTaskStatusTypeType,
    EntityTypeType,
    PolicyEvaluationDecisionTypeType,
    PolicySourceTypeType,
    PolicyUsageTypeType,
    ReportStateTypeType,
    assignmentStatusTypeType,
    encodingTypeType,
    globalEndpointTokenVersionType,
    jobStatusTypeType,
    policyOwnerEntityTypeType,
    policyScopeTypeType,
    policyTypeType,
    sortKeyTypeType,
    statusTypeType,
    summaryKeyTypeType,
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
    "AccessDetailTypeDef",
    "AccessKeyLastUsedTypeDef",
    "AccessKeyMetadataTypeDef",
    "AccessKeyTypeDef",
    "AddClientIDToOpenIDConnectProviderRequestTypeDef",
    "AddRoleToInstanceProfileRequestInstanceProfileTypeDef",
    "AddRoleToInstanceProfileRequestTypeDef",
    "AddUserToGroupRequestGroupTypeDef",
    "AddUserToGroupRequestTypeDef",
    "AddUserToGroupRequestUserTypeDef",
    "AttachGroupPolicyRequestGroupTypeDef",
    "AttachGroupPolicyRequestPolicyTypeDef",
    "AttachGroupPolicyRequestTypeDef",
    "AttachRolePolicyRequestPolicyTypeDef",
    "AttachRolePolicyRequestRoleTypeDef",
    "AttachRolePolicyRequestTypeDef",
    "AttachUserPolicyRequestPolicyTypeDef",
    "AttachUserPolicyRequestTypeDef",
    "AttachUserPolicyRequestUserTypeDef",
    "AttachedPermissionsBoundaryTypeDef",
    "AttachedPolicyTypeDef",
    "ChangePasswordRequestServiceResourceTypeDef",
    "ChangePasswordRequestTypeDef",
    "ContextEntryTypeDef",
    "CreateAccessKeyRequestTypeDef",
    "CreateAccessKeyResponseResponseTypeDef",
    "CreateAccountAliasRequestServiceResourceTypeDef",
    "CreateAccountAliasRequestTypeDef",
    "CreateGroupRequestGroupTypeDef",
    "CreateGroupRequestServiceResourceTypeDef",
    "CreateGroupRequestTypeDef",
    "CreateGroupResponseResponseTypeDef",
    "CreateInstanceProfileRequestServiceResourceTypeDef",
    "CreateInstanceProfileRequestTypeDef",
    "CreateInstanceProfileResponseResponseTypeDef",
    "CreateLoginProfileRequestLoginProfileTypeDef",
    "CreateLoginProfileRequestTypeDef",
    "CreateLoginProfileRequestUserTypeDef",
    "CreateLoginProfileResponseResponseTypeDef",
    "CreateOpenIDConnectProviderRequestTypeDef",
    "CreateOpenIDConnectProviderResponseResponseTypeDef",
    "CreatePolicyRequestServiceResourceTypeDef",
    "CreatePolicyRequestTypeDef",
    "CreatePolicyResponseResponseTypeDef",
    "CreatePolicyVersionRequestPolicyTypeDef",
    "CreatePolicyVersionRequestTypeDef",
    "CreatePolicyVersionResponseResponseTypeDef",
    "CreateRoleRequestServiceResourceTypeDef",
    "CreateRoleRequestTypeDef",
    "CreateRoleResponseResponseTypeDef",
    "CreateSAMLProviderRequestServiceResourceTypeDef",
    "CreateSAMLProviderRequestTypeDef",
    "CreateSAMLProviderResponseResponseTypeDef",
    "CreateServiceLinkedRoleRequestTypeDef",
    "CreateServiceLinkedRoleResponseResponseTypeDef",
    "CreateServiceSpecificCredentialRequestTypeDef",
    "CreateServiceSpecificCredentialResponseResponseTypeDef",
    "CreateUserRequestServiceResourceTypeDef",
    "CreateUserRequestTypeDef",
    "CreateUserRequestUserTypeDef",
    "CreateUserResponseResponseTypeDef",
    "CreateVirtualMFADeviceRequestServiceResourceTypeDef",
    "CreateVirtualMFADeviceRequestTypeDef",
    "CreateVirtualMFADeviceResponseResponseTypeDef",
    "DeactivateMFADeviceRequestTypeDef",
    "DeleteAccessKeyRequestTypeDef",
    "DeleteAccountAliasRequestTypeDef",
    "DeleteGroupPolicyRequestTypeDef",
    "DeleteGroupRequestTypeDef",
    "DeleteInstanceProfileRequestTypeDef",
    "DeleteLoginProfileRequestTypeDef",
    "DeleteOpenIDConnectProviderRequestTypeDef",
    "DeletePolicyRequestTypeDef",
    "DeletePolicyVersionRequestTypeDef",
    "DeleteRolePermissionsBoundaryRequestTypeDef",
    "DeleteRolePolicyRequestTypeDef",
    "DeleteRoleRequestTypeDef",
    "DeleteSAMLProviderRequestTypeDef",
    "DeleteSSHPublicKeyRequestTypeDef",
    "DeleteServerCertificateRequestTypeDef",
    "DeleteServiceLinkedRoleRequestTypeDef",
    "DeleteServiceLinkedRoleResponseResponseTypeDef",
    "DeleteServiceSpecificCredentialRequestTypeDef",
    "DeleteSigningCertificateRequestTypeDef",
    "DeleteUserPermissionsBoundaryRequestTypeDef",
    "DeleteUserPolicyRequestTypeDef",
    "DeleteUserRequestTypeDef",
    "DeleteVirtualMFADeviceRequestTypeDef",
    "DeletionTaskFailureReasonTypeTypeDef",
    "DetachGroupPolicyRequestGroupTypeDef",
    "DetachGroupPolicyRequestPolicyTypeDef",
    "DetachGroupPolicyRequestTypeDef",
    "DetachRolePolicyRequestPolicyTypeDef",
    "DetachRolePolicyRequestRoleTypeDef",
    "DetachRolePolicyRequestTypeDef",
    "DetachUserPolicyRequestPolicyTypeDef",
    "DetachUserPolicyRequestTypeDef",
    "DetachUserPolicyRequestUserTypeDef",
    "EnableMFADeviceRequestMfaDeviceTypeDef",
    "EnableMFADeviceRequestTypeDef",
    "EnableMFADeviceRequestUserTypeDef",
    "EntityDetailsTypeDef",
    "EntityInfoTypeDef",
    "ErrorDetailsTypeDef",
    "EvaluationResultTypeDef",
    "GenerateCredentialReportResponseResponseTypeDef",
    "GenerateOrganizationsAccessReportRequestTypeDef",
    "GenerateOrganizationsAccessReportResponseResponseTypeDef",
    "GenerateServiceLastAccessedDetailsRequestTypeDef",
    "GenerateServiceLastAccessedDetailsResponseResponseTypeDef",
    "GetAccessKeyLastUsedRequestTypeDef",
    "GetAccessKeyLastUsedResponseResponseTypeDef",
    "GetAccountAuthorizationDetailsRequestTypeDef",
    "GetAccountAuthorizationDetailsResponseResponseTypeDef",
    "GetAccountPasswordPolicyResponseResponseTypeDef",
    "GetAccountSummaryResponseResponseTypeDef",
    "GetContextKeysForCustomPolicyRequestTypeDef",
    "GetContextKeysForPolicyResponseResponseTypeDef",
    "GetContextKeysForPrincipalPolicyRequestTypeDef",
    "GetCredentialReportResponseResponseTypeDef",
    "GetGroupPolicyRequestTypeDef",
    "GetGroupPolicyResponseResponseTypeDef",
    "GetGroupRequestTypeDef",
    "GetGroupResponseResponseTypeDef",
    "GetInstanceProfileRequestTypeDef",
    "GetInstanceProfileResponseResponseTypeDef",
    "GetLoginProfileRequestTypeDef",
    "GetLoginProfileResponseResponseTypeDef",
    "GetOpenIDConnectProviderRequestTypeDef",
    "GetOpenIDConnectProviderResponseResponseTypeDef",
    "GetOrganizationsAccessReportRequestTypeDef",
    "GetOrganizationsAccessReportResponseResponseTypeDef",
    "GetPolicyRequestTypeDef",
    "GetPolicyResponseResponseTypeDef",
    "GetPolicyVersionRequestTypeDef",
    "GetPolicyVersionResponseResponseTypeDef",
    "GetRolePolicyRequestTypeDef",
    "GetRolePolicyResponseResponseTypeDef",
    "GetRoleRequestTypeDef",
    "GetRoleResponseResponseTypeDef",
    "GetSAMLProviderRequestTypeDef",
    "GetSAMLProviderResponseResponseTypeDef",
    "GetSSHPublicKeyRequestTypeDef",
    "GetSSHPublicKeyResponseResponseTypeDef",
    "GetServerCertificateRequestTypeDef",
    "GetServerCertificateResponseResponseTypeDef",
    "GetServiceLastAccessedDetailsRequestTypeDef",
    "GetServiceLastAccessedDetailsResponseResponseTypeDef",
    "GetServiceLastAccessedDetailsWithEntitiesRequestTypeDef",
    "GetServiceLastAccessedDetailsWithEntitiesResponseResponseTypeDef",
    "GetServiceLinkedRoleDeletionStatusRequestTypeDef",
    "GetServiceLinkedRoleDeletionStatusResponseResponseTypeDef",
    "GetUserPolicyRequestTypeDef",
    "GetUserPolicyResponseResponseTypeDef",
    "GetUserRequestTypeDef",
    "GetUserResponseResponseTypeDef",
    "GroupDetailTypeDef",
    "GroupPolicyRequestTypeDef",
    "GroupTypeDef",
    "InstanceProfileTypeDef",
    "ListAccessKeysRequestTypeDef",
    "ListAccessKeysResponseResponseTypeDef",
    "ListAccountAliasesRequestTypeDef",
    "ListAccountAliasesResponseResponseTypeDef",
    "ListAttachedGroupPoliciesRequestTypeDef",
    "ListAttachedGroupPoliciesResponseResponseTypeDef",
    "ListAttachedRolePoliciesRequestTypeDef",
    "ListAttachedRolePoliciesResponseResponseTypeDef",
    "ListAttachedUserPoliciesRequestTypeDef",
    "ListAttachedUserPoliciesResponseResponseTypeDef",
    "ListEntitiesForPolicyRequestTypeDef",
    "ListEntitiesForPolicyResponseResponseTypeDef",
    "ListGroupPoliciesRequestTypeDef",
    "ListGroupPoliciesResponseResponseTypeDef",
    "ListGroupsForUserRequestTypeDef",
    "ListGroupsForUserResponseResponseTypeDef",
    "ListGroupsRequestTypeDef",
    "ListGroupsResponseResponseTypeDef",
    "ListInstanceProfileTagsRequestTypeDef",
    "ListInstanceProfileTagsResponseResponseTypeDef",
    "ListInstanceProfilesForRoleRequestTypeDef",
    "ListInstanceProfilesForRoleResponseResponseTypeDef",
    "ListInstanceProfilesRequestTypeDef",
    "ListInstanceProfilesResponseResponseTypeDef",
    "ListMFADeviceTagsRequestTypeDef",
    "ListMFADeviceTagsResponseResponseTypeDef",
    "ListMFADevicesRequestTypeDef",
    "ListMFADevicesResponseResponseTypeDef",
    "ListOpenIDConnectProviderTagsRequestTypeDef",
    "ListOpenIDConnectProviderTagsResponseResponseTypeDef",
    "ListOpenIDConnectProvidersResponseResponseTypeDef",
    "ListPoliciesGrantingServiceAccessEntryTypeDef",
    "ListPoliciesGrantingServiceAccessRequestTypeDef",
    "ListPoliciesGrantingServiceAccessResponseResponseTypeDef",
    "ListPoliciesRequestTypeDef",
    "ListPoliciesResponseResponseTypeDef",
    "ListPolicyTagsRequestTypeDef",
    "ListPolicyTagsResponseResponseTypeDef",
    "ListPolicyVersionsRequestTypeDef",
    "ListPolicyVersionsResponseResponseTypeDef",
    "ListRolePoliciesRequestTypeDef",
    "ListRolePoliciesResponseResponseTypeDef",
    "ListRoleTagsRequestTypeDef",
    "ListRoleTagsResponseResponseTypeDef",
    "ListRolesRequestTypeDef",
    "ListRolesResponseResponseTypeDef",
    "ListSAMLProviderTagsRequestTypeDef",
    "ListSAMLProviderTagsResponseResponseTypeDef",
    "ListSAMLProvidersResponseResponseTypeDef",
    "ListSSHPublicKeysRequestTypeDef",
    "ListSSHPublicKeysResponseResponseTypeDef",
    "ListServerCertificateTagsRequestTypeDef",
    "ListServerCertificateTagsResponseResponseTypeDef",
    "ListServerCertificatesRequestTypeDef",
    "ListServerCertificatesResponseResponseTypeDef",
    "ListServiceSpecificCredentialsRequestTypeDef",
    "ListServiceSpecificCredentialsResponseResponseTypeDef",
    "ListSigningCertificatesRequestTypeDef",
    "ListSigningCertificatesResponseResponseTypeDef",
    "ListUserPoliciesRequestTypeDef",
    "ListUserPoliciesResponseResponseTypeDef",
    "ListUserTagsRequestTypeDef",
    "ListUserTagsResponseResponseTypeDef",
    "ListUsersRequestTypeDef",
    "ListUsersResponseResponseTypeDef",
    "ListVirtualMFADevicesRequestTypeDef",
    "ListVirtualMFADevicesResponseResponseTypeDef",
    "LoginProfileTypeDef",
    "MFADeviceTypeDef",
    "ManagedPolicyDetailTypeDef",
    "OpenIDConnectProviderListEntryTypeDef",
    "OrganizationsDecisionDetailTypeDef",
    "PaginatorConfigTypeDef",
    "PasswordPolicyTypeDef",
    "PermissionsBoundaryDecisionDetailTypeDef",
    "PolicyDetailTypeDef",
    "PolicyGrantingServiceAccessTypeDef",
    "PolicyGroupTypeDef",
    "PolicyRoleTypeDef",
    "PolicyTypeDef",
    "PolicyUserTypeDef",
    "PolicyVersionTypeDef",
    "PositionTypeDef",
    "PutGroupPolicyRequestGroupPolicyTypeDef",
    "PutGroupPolicyRequestGroupTypeDef",
    "PutGroupPolicyRequestTypeDef",
    "PutRolePermissionsBoundaryRequestTypeDef",
    "PutRolePolicyRequestRolePolicyTypeDef",
    "PutRolePolicyRequestTypeDef",
    "PutUserPermissionsBoundaryRequestTypeDef",
    "PutUserPolicyRequestTypeDef",
    "PutUserPolicyRequestUserPolicyTypeDef",
    "PutUserPolicyRequestUserTypeDef",
    "RemoveClientIDFromOpenIDConnectProviderRequestTypeDef",
    "RemoveRoleFromInstanceProfileRequestInstanceProfileTypeDef",
    "RemoveRoleFromInstanceProfileRequestTypeDef",
    "RemoveUserFromGroupRequestGroupTypeDef",
    "RemoveUserFromGroupRequestTypeDef",
    "RemoveUserFromGroupRequestUserTypeDef",
    "ResetServiceSpecificCredentialRequestTypeDef",
    "ResetServiceSpecificCredentialResponseResponseTypeDef",
    "ResourceSpecificResultTypeDef",
    "ResponseMetadataTypeDef",
    "ResyncMFADeviceRequestMfaDeviceTypeDef",
    "ResyncMFADeviceRequestTypeDef",
    "RoleDetailTypeDef",
    "RoleLastUsedTypeDef",
    "RolePolicyRequestTypeDef",
    "RoleTypeDef",
    "RoleUsageTypeTypeDef",
    "SAMLProviderListEntryTypeDef",
    "SSHPublicKeyMetadataTypeDef",
    "SSHPublicKeyTypeDef",
    "ServerCertificateMetadataTypeDef",
    "ServerCertificateTypeDef",
    "ServiceLastAccessedTypeDef",
    "ServiceResourceAccessKeyPairRequestTypeDef",
    "ServiceResourceAccessKeyRequestTypeDef",
    "ServiceResourceAssumeRolePolicyRequestTypeDef",
    "ServiceResourceGroupPolicyRequestTypeDef",
    "ServiceResourceGroupRequestTypeDef",
    "ServiceResourceInstanceProfileRequestTypeDef",
    "ServiceResourceLoginProfileRequestTypeDef",
    "ServiceResourceMfaDeviceRequestTypeDef",
    "ServiceResourcePolicyRequestTypeDef",
    "ServiceResourcePolicyVersionRequestTypeDef",
    "ServiceResourceRolePolicyRequestTypeDef",
    "ServiceResourceRoleRequestTypeDef",
    "ServiceResourceSamlProviderRequestTypeDef",
    "ServiceResourceServerCertificateRequestTypeDef",
    "ServiceResourceSigningCertificateRequestTypeDef",
    "ServiceResourceUserPolicyRequestTypeDef",
    "ServiceResourceUserRequestTypeDef",
    "ServiceResourceVirtualMfaDeviceRequestTypeDef",
    "ServiceSpecificCredentialMetadataTypeDef",
    "ServiceSpecificCredentialTypeDef",
    "SetDefaultPolicyVersionRequestTypeDef",
    "SetSecurityTokenServicePreferencesRequestTypeDef",
    "SigningCertificateTypeDef",
    "SimulateCustomPolicyRequestTypeDef",
    "SimulatePolicyResponseResponseTypeDef",
    "SimulatePrincipalPolicyRequestTypeDef",
    "StatementTypeDef",
    "TagInstanceProfileRequestTypeDef",
    "TagMFADeviceRequestTypeDef",
    "TagOpenIDConnectProviderRequestTypeDef",
    "TagPolicyRequestTypeDef",
    "TagRoleRequestTypeDef",
    "TagSAMLProviderRequestTypeDef",
    "TagServerCertificateRequestTypeDef",
    "TagTypeDef",
    "TagUserRequestTypeDef",
    "TrackedActionLastAccessedTypeDef",
    "UntagInstanceProfileRequestTypeDef",
    "UntagMFADeviceRequestTypeDef",
    "UntagOpenIDConnectProviderRequestTypeDef",
    "UntagPolicyRequestTypeDef",
    "UntagRoleRequestTypeDef",
    "UntagSAMLProviderRequestTypeDef",
    "UntagServerCertificateRequestTypeDef",
    "UntagUserRequestTypeDef",
    "UpdateAccessKeyRequestAccessKeyPairTypeDef",
    "UpdateAccessKeyRequestAccessKeyTypeDef",
    "UpdateAccessKeyRequestTypeDef",
    "UpdateAccountPasswordPolicyRequestAccountPasswordPolicyTypeDef",
    "UpdateAccountPasswordPolicyRequestServiceResourceTypeDef",
    "UpdateAccountPasswordPolicyRequestTypeDef",
    "UpdateAssumeRolePolicyRequestAssumeRolePolicyTypeDef",
    "UpdateAssumeRolePolicyRequestTypeDef",
    "UpdateGroupRequestGroupTypeDef",
    "UpdateGroupRequestTypeDef",
    "UpdateLoginProfileRequestLoginProfileTypeDef",
    "UpdateLoginProfileRequestTypeDef",
    "UpdateOpenIDConnectProviderThumbprintRequestTypeDef",
    "UpdateRoleDescriptionRequestTypeDef",
    "UpdateRoleDescriptionResponseResponseTypeDef",
    "UpdateRoleRequestTypeDef",
    "UpdateSAMLProviderRequestSamlProviderTypeDef",
    "UpdateSAMLProviderRequestTypeDef",
    "UpdateSAMLProviderResponseResponseTypeDef",
    "UpdateSSHPublicKeyRequestTypeDef",
    "UpdateServerCertificateRequestServerCertificateTypeDef",
    "UpdateServerCertificateRequestTypeDef",
    "UpdateServiceSpecificCredentialRequestTypeDef",
    "UpdateSigningCertificateRequestSigningCertificateTypeDef",
    "UpdateSigningCertificateRequestTypeDef",
    "UpdateUserRequestTypeDef",
    "UpdateUserRequestUserTypeDef",
    "UploadSSHPublicKeyRequestTypeDef",
    "UploadSSHPublicKeyResponseResponseTypeDef",
    "UploadServerCertificateRequestServiceResourceTypeDef",
    "UploadServerCertificateRequestTypeDef",
    "UploadServerCertificateResponseResponseTypeDef",
    "UploadSigningCertificateRequestServiceResourceTypeDef",
    "UploadSigningCertificateRequestTypeDef",
    "UploadSigningCertificateResponseResponseTypeDef",
    "UserAccessKeyRequestTypeDef",
    "UserDetailTypeDef",
    "UserMfaDeviceRequestTypeDef",
    "UserPolicyRequestTypeDef",
    "UserSigningCertificateRequestTypeDef",
    "UserTypeDef",
    "VirtualMFADeviceTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAccessDetailTypeDef = TypedDict(
    "_RequiredAccessDetailTypeDef",
    {
        "ServiceName": str,
        "ServiceNamespace": str,
    },
)
_OptionalAccessDetailTypeDef = TypedDict(
    "_OptionalAccessDetailTypeDef",
    {
        "Region": str,
        "EntityPath": str,
        "LastAuthenticatedTime": datetime,
        "TotalAuthenticatedEntities": int,
    },
    total=False,
)


class AccessDetailTypeDef(_RequiredAccessDetailTypeDef, _OptionalAccessDetailTypeDef):
    pass


AccessKeyLastUsedTypeDef = TypedDict(
    "AccessKeyLastUsedTypeDef",
    {
        "LastUsedDate": datetime,
        "ServiceName": str,
        "Region": str,
    },
)

AccessKeyMetadataTypeDef = TypedDict(
    "AccessKeyMetadataTypeDef",
    {
        "UserName": str,
        "AccessKeyId": str,
        "Status": statusTypeType,
        "CreateDate": datetime,
    },
    total=False,
)

_RequiredAccessKeyTypeDef = TypedDict(
    "_RequiredAccessKeyTypeDef",
    {
        "UserName": str,
        "AccessKeyId": str,
        "Status": statusTypeType,
        "SecretAccessKey": str,
    },
)
_OptionalAccessKeyTypeDef = TypedDict(
    "_OptionalAccessKeyTypeDef",
    {
        "CreateDate": datetime,
    },
    total=False,
)


class AccessKeyTypeDef(_RequiredAccessKeyTypeDef, _OptionalAccessKeyTypeDef):
    pass


AddClientIDToOpenIDConnectProviderRequestTypeDef = TypedDict(
    "AddClientIDToOpenIDConnectProviderRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "ClientID": str,
    },
)

AddRoleToInstanceProfileRequestInstanceProfileTypeDef = TypedDict(
    "AddRoleToInstanceProfileRequestInstanceProfileTypeDef",
    {
        "RoleName": str,
    },
)

AddRoleToInstanceProfileRequestTypeDef = TypedDict(
    "AddRoleToInstanceProfileRequestTypeDef",
    {
        "InstanceProfileName": str,
        "RoleName": str,
    },
)

AddUserToGroupRequestGroupTypeDef = TypedDict(
    "AddUserToGroupRequestGroupTypeDef",
    {
        "UserName": str,
    },
)

AddUserToGroupRequestTypeDef = TypedDict(
    "AddUserToGroupRequestTypeDef",
    {
        "GroupName": str,
        "UserName": str,
    },
)

AddUserToGroupRequestUserTypeDef = TypedDict(
    "AddUserToGroupRequestUserTypeDef",
    {
        "GroupName": str,
    },
)

AttachGroupPolicyRequestGroupTypeDef = TypedDict(
    "AttachGroupPolicyRequestGroupTypeDef",
    {
        "PolicyArn": str,
    },
)

AttachGroupPolicyRequestPolicyTypeDef = TypedDict(
    "AttachGroupPolicyRequestPolicyTypeDef",
    {
        "GroupName": str,
    },
)

AttachGroupPolicyRequestTypeDef = TypedDict(
    "AttachGroupPolicyRequestTypeDef",
    {
        "GroupName": str,
        "PolicyArn": str,
    },
)

AttachRolePolicyRequestPolicyTypeDef = TypedDict(
    "AttachRolePolicyRequestPolicyTypeDef",
    {
        "RoleName": str,
    },
)

AttachRolePolicyRequestRoleTypeDef = TypedDict(
    "AttachRolePolicyRequestRoleTypeDef",
    {
        "PolicyArn": str,
    },
)

AttachRolePolicyRequestTypeDef = TypedDict(
    "AttachRolePolicyRequestTypeDef",
    {
        "RoleName": str,
        "PolicyArn": str,
    },
)

AttachUserPolicyRequestPolicyTypeDef = TypedDict(
    "AttachUserPolicyRequestPolicyTypeDef",
    {
        "UserName": str,
    },
)

AttachUserPolicyRequestTypeDef = TypedDict(
    "AttachUserPolicyRequestTypeDef",
    {
        "UserName": str,
        "PolicyArn": str,
    },
)

AttachUserPolicyRequestUserTypeDef = TypedDict(
    "AttachUserPolicyRequestUserTypeDef",
    {
        "PolicyArn": str,
    },
)

AttachedPermissionsBoundaryTypeDef = TypedDict(
    "AttachedPermissionsBoundaryTypeDef",
    {
        "PermissionsBoundaryType": Literal["PermissionsBoundaryPolicy"],
        "PermissionsBoundaryArn": str,
    },
    total=False,
)

AttachedPolicyTypeDef = TypedDict(
    "AttachedPolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyArn": str,
    },
    total=False,
)

ChangePasswordRequestServiceResourceTypeDef = TypedDict(
    "ChangePasswordRequestServiceResourceTypeDef",
    {
        "OldPassword": str,
        "NewPassword": str,
    },
)

ChangePasswordRequestTypeDef = TypedDict(
    "ChangePasswordRequestTypeDef",
    {
        "OldPassword": str,
        "NewPassword": str,
    },
)

ContextEntryTypeDef = TypedDict(
    "ContextEntryTypeDef",
    {
        "ContextKeyName": str,
        "ContextKeyValues": List[str],
        "ContextKeyType": ContextKeyTypeEnumType,
    },
    total=False,
)

CreateAccessKeyRequestTypeDef = TypedDict(
    "CreateAccessKeyRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)

CreateAccessKeyResponseResponseTypeDef = TypedDict(
    "CreateAccessKeyResponseResponseTypeDef",
    {
        "AccessKey": "AccessKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAccountAliasRequestServiceResourceTypeDef = TypedDict(
    "CreateAccountAliasRequestServiceResourceTypeDef",
    {
        "AccountAlias": str,
    },
)

CreateAccountAliasRequestTypeDef = TypedDict(
    "CreateAccountAliasRequestTypeDef",
    {
        "AccountAlias": str,
    },
)

CreateGroupRequestGroupTypeDef = TypedDict(
    "CreateGroupRequestGroupTypeDef",
    {
        "Path": str,
    },
    total=False,
)

_RequiredCreateGroupRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateGroupRequestServiceResourceTypeDef",
    {
        "GroupName": str,
    },
)
_OptionalCreateGroupRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateGroupRequestServiceResourceTypeDef",
    {
        "Path": str,
    },
    total=False,
)


class CreateGroupRequestServiceResourceTypeDef(
    _RequiredCreateGroupRequestServiceResourceTypeDef,
    _OptionalCreateGroupRequestServiceResourceTypeDef,
):
    pass


_RequiredCreateGroupRequestTypeDef = TypedDict(
    "_RequiredCreateGroupRequestTypeDef",
    {
        "GroupName": str,
    },
)
_OptionalCreateGroupRequestTypeDef = TypedDict(
    "_OptionalCreateGroupRequestTypeDef",
    {
        "Path": str,
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
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInstanceProfileRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateInstanceProfileRequestServiceResourceTypeDef",
    {
        "InstanceProfileName": str,
    },
)
_OptionalCreateInstanceProfileRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateInstanceProfileRequestServiceResourceTypeDef",
    {
        "Path": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateInstanceProfileRequestServiceResourceTypeDef(
    _RequiredCreateInstanceProfileRequestServiceResourceTypeDef,
    _OptionalCreateInstanceProfileRequestServiceResourceTypeDef,
):
    pass


_RequiredCreateInstanceProfileRequestTypeDef = TypedDict(
    "_RequiredCreateInstanceProfileRequestTypeDef",
    {
        "InstanceProfileName": str,
    },
)
_OptionalCreateInstanceProfileRequestTypeDef = TypedDict(
    "_OptionalCreateInstanceProfileRequestTypeDef",
    {
        "Path": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateInstanceProfileRequestTypeDef(
    _RequiredCreateInstanceProfileRequestTypeDef, _OptionalCreateInstanceProfileRequestTypeDef
):
    pass


CreateInstanceProfileResponseResponseTypeDef = TypedDict(
    "CreateInstanceProfileResponseResponseTypeDef",
    {
        "InstanceProfile": "InstanceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLoginProfileRequestLoginProfileTypeDef = TypedDict(
    "_RequiredCreateLoginProfileRequestLoginProfileTypeDef",
    {
        "Password": str,
    },
)
_OptionalCreateLoginProfileRequestLoginProfileTypeDef = TypedDict(
    "_OptionalCreateLoginProfileRequestLoginProfileTypeDef",
    {
        "PasswordResetRequired": bool,
    },
    total=False,
)


class CreateLoginProfileRequestLoginProfileTypeDef(
    _RequiredCreateLoginProfileRequestLoginProfileTypeDef,
    _OptionalCreateLoginProfileRequestLoginProfileTypeDef,
):
    pass


_RequiredCreateLoginProfileRequestTypeDef = TypedDict(
    "_RequiredCreateLoginProfileRequestTypeDef",
    {
        "UserName": str,
        "Password": str,
    },
)
_OptionalCreateLoginProfileRequestTypeDef = TypedDict(
    "_OptionalCreateLoginProfileRequestTypeDef",
    {
        "PasswordResetRequired": bool,
    },
    total=False,
)


class CreateLoginProfileRequestTypeDef(
    _RequiredCreateLoginProfileRequestTypeDef, _OptionalCreateLoginProfileRequestTypeDef
):
    pass


_RequiredCreateLoginProfileRequestUserTypeDef = TypedDict(
    "_RequiredCreateLoginProfileRequestUserTypeDef",
    {
        "Password": str,
    },
)
_OptionalCreateLoginProfileRequestUserTypeDef = TypedDict(
    "_OptionalCreateLoginProfileRequestUserTypeDef",
    {
        "PasswordResetRequired": bool,
    },
    total=False,
)


class CreateLoginProfileRequestUserTypeDef(
    _RequiredCreateLoginProfileRequestUserTypeDef, _OptionalCreateLoginProfileRequestUserTypeDef
):
    pass


CreateLoginProfileResponseResponseTypeDef = TypedDict(
    "CreateLoginProfileResponseResponseTypeDef",
    {
        "LoginProfile": "LoginProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateOpenIDConnectProviderRequestTypeDef = TypedDict(
    "_RequiredCreateOpenIDConnectProviderRequestTypeDef",
    {
        "Url": str,
        "ThumbprintList": List[str],
    },
)
_OptionalCreateOpenIDConnectProviderRequestTypeDef = TypedDict(
    "_OptionalCreateOpenIDConnectProviderRequestTypeDef",
    {
        "ClientIDList": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateOpenIDConnectProviderRequestTypeDef(
    _RequiredCreateOpenIDConnectProviderRequestTypeDef,
    _OptionalCreateOpenIDConnectProviderRequestTypeDef,
):
    pass


CreateOpenIDConnectProviderResponseResponseTypeDef = TypedDict(
    "CreateOpenIDConnectProviderResponseResponseTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePolicyRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreatePolicyRequestServiceResourceTypeDef",
    {
        "PolicyName": str,
        "PolicyDocument": str,
    },
)
_OptionalCreatePolicyRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreatePolicyRequestServiceResourceTypeDef",
    {
        "Path": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreatePolicyRequestServiceResourceTypeDef(
    _RequiredCreatePolicyRequestServiceResourceTypeDef,
    _OptionalCreatePolicyRequestServiceResourceTypeDef,
):
    pass


_RequiredCreatePolicyRequestTypeDef = TypedDict(
    "_RequiredCreatePolicyRequestTypeDef",
    {
        "PolicyName": str,
        "PolicyDocument": str,
    },
)
_OptionalCreatePolicyRequestTypeDef = TypedDict(
    "_OptionalCreatePolicyRequestTypeDef",
    {
        "Path": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreatePolicyRequestTypeDef(
    _RequiredCreatePolicyRequestTypeDef, _OptionalCreatePolicyRequestTypeDef
):
    pass


CreatePolicyResponseResponseTypeDef = TypedDict(
    "CreatePolicyResponseResponseTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePolicyVersionRequestPolicyTypeDef = TypedDict(
    "_RequiredCreatePolicyVersionRequestPolicyTypeDef",
    {
        "PolicyDocument": str,
    },
)
_OptionalCreatePolicyVersionRequestPolicyTypeDef = TypedDict(
    "_OptionalCreatePolicyVersionRequestPolicyTypeDef",
    {
        "SetAsDefault": bool,
    },
    total=False,
)


class CreatePolicyVersionRequestPolicyTypeDef(
    _RequiredCreatePolicyVersionRequestPolicyTypeDef,
    _OptionalCreatePolicyVersionRequestPolicyTypeDef,
):
    pass


_RequiredCreatePolicyVersionRequestTypeDef = TypedDict(
    "_RequiredCreatePolicyVersionRequestTypeDef",
    {
        "PolicyArn": str,
        "PolicyDocument": str,
    },
)
_OptionalCreatePolicyVersionRequestTypeDef = TypedDict(
    "_OptionalCreatePolicyVersionRequestTypeDef",
    {
        "SetAsDefault": bool,
    },
    total=False,
)


class CreatePolicyVersionRequestTypeDef(
    _RequiredCreatePolicyVersionRequestTypeDef, _OptionalCreatePolicyVersionRequestTypeDef
):
    pass


CreatePolicyVersionResponseResponseTypeDef = TypedDict(
    "CreatePolicyVersionResponseResponseTypeDef",
    {
        "PolicyVersion": "PolicyVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRoleRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateRoleRequestServiceResourceTypeDef",
    {
        "RoleName": str,
        "AssumeRolePolicyDocument": str,
    },
)
_OptionalCreateRoleRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateRoleRequestServiceResourceTypeDef",
    {
        "Path": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateRoleRequestServiceResourceTypeDef(
    _RequiredCreateRoleRequestServiceResourceTypeDef,
    _OptionalCreateRoleRequestServiceResourceTypeDef,
):
    pass


_RequiredCreateRoleRequestTypeDef = TypedDict(
    "_RequiredCreateRoleRequestTypeDef",
    {
        "RoleName": str,
        "AssumeRolePolicyDocument": str,
    },
)
_OptionalCreateRoleRequestTypeDef = TypedDict(
    "_OptionalCreateRoleRequestTypeDef",
    {
        "Path": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateRoleRequestTypeDef(
    _RequiredCreateRoleRequestTypeDef, _OptionalCreateRoleRequestTypeDef
):
    pass


CreateRoleResponseResponseTypeDef = TypedDict(
    "CreateRoleResponseResponseTypeDef",
    {
        "Role": "RoleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSAMLProviderRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateSAMLProviderRequestServiceResourceTypeDef",
    {
        "SAMLMetadataDocument": str,
        "Name": str,
    },
)
_OptionalCreateSAMLProviderRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateSAMLProviderRequestServiceResourceTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateSAMLProviderRequestServiceResourceTypeDef(
    _RequiredCreateSAMLProviderRequestServiceResourceTypeDef,
    _OptionalCreateSAMLProviderRequestServiceResourceTypeDef,
):
    pass


_RequiredCreateSAMLProviderRequestTypeDef = TypedDict(
    "_RequiredCreateSAMLProviderRequestTypeDef",
    {
        "SAMLMetadataDocument": str,
        "Name": str,
    },
)
_OptionalCreateSAMLProviderRequestTypeDef = TypedDict(
    "_OptionalCreateSAMLProviderRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateSAMLProviderRequestTypeDef(
    _RequiredCreateSAMLProviderRequestTypeDef, _OptionalCreateSAMLProviderRequestTypeDef
):
    pass


CreateSAMLProviderResponseResponseTypeDef = TypedDict(
    "CreateSAMLProviderResponseResponseTypeDef",
    {
        "SAMLProviderArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceLinkedRoleRequestTypeDef = TypedDict(
    "_RequiredCreateServiceLinkedRoleRequestTypeDef",
    {
        "AWSServiceName": str,
    },
)
_OptionalCreateServiceLinkedRoleRequestTypeDef = TypedDict(
    "_OptionalCreateServiceLinkedRoleRequestTypeDef",
    {
        "Description": str,
        "CustomSuffix": str,
    },
    total=False,
)


class CreateServiceLinkedRoleRequestTypeDef(
    _RequiredCreateServiceLinkedRoleRequestTypeDef, _OptionalCreateServiceLinkedRoleRequestTypeDef
):
    pass


CreateServiceLinkedRoleResponseResponseTypeDef = TypedDict(
    "CreateServiceLinkedRoleResponseResponseTypeDef",
    {
        "Role": "RoleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServiceSpecificCredentialRequestTypeDef = TypedDict(
    "CreateServiceSpecificCredentialRequestTypeDef",
    {
        "UserName": str,
        "ServiceName": str,
    },
)

CreateServiceSpecificCredentialResponseResponseTypeDef = TypedDict(
    "CreateServiceSpecificCredentialResponseResponseTypeDef",
    {
        "ServiceSpecificCredential": "ServiceSpecificCredentialTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateUserRequestServiceResourceTypeDef",
    {
        "UserName": str,
    },
)
_OptionalCreateUserRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateUserRequestServiceResourceTypeDef",
    {
        "Path": str,
        "PermissionsBoundary": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateUserRequestServiceResourceTypeDef(
    _RequiredCreateUserRequestServiceResourceTypeDef,
    _OptionalCreateUserRequestServiceResourceTypeDef,
):
    pass


_RequiredCreateUserRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestTypeDef",
    {
        "UserName": str,
    },
)
_OptionalCreateUserRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestTypeDef",
    {
        "Path": str,
        "PermissionsBoundary": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateUserRequestTypeDef(
    _RequiredCreateUserRequestTypeDef, _OptionalCreateUserRequestTypeDef
):
    pass


CreateUserRequestUserTypeDef = TypedDict(
    "CreateUserRequestUserTypeDef",
    {
        "Path": str,
        "PermissionsBoundary": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CreateUserResponseResponseTypeDef = TypedDict(
    "CreateUserResponseResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVirtualMFADeviceRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateVirtualMFADeviceRequestServiceResourceTypeDef",
    {
        "VirtualMFADeviceName": str,
    },
)
_OptionalCreateVirtualMFADeviceRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateVirtualMFADeviceRequestServiceResourceTypeDef",
    {
        "Path": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateVirtualMFADeviceRequestServiceResourceTypeDef(
    _RequiredCreateVirtualMFADeviceRequestServiceResourceTypeDef,
    _OptionalCreateVirtualMFADeviceRequestServiceResourceTypeDef,
):
    pass


_RequiredCreateVirtualMFADeviceRequestTypeDef = TypedDict(
    "_RequiredCreateVirtualMFADeviceRequestTypeDef",
    {
        "VirtualMFADeviceName": str,
    },
)
_OptionalCreateVirtualMFADeviceRequestTypeDef = TypedDict(
    "_OptionalCreateVirtualMFADeviceRequestTypeDef",
    {
        "Path": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateVirtualMFADeviceRequestTypeDef(
    _RequiredCreateVirtualMFADeviceRequestTypeDef, _OptionalCreateVirtualMFADeviceRequestTypeDef
):
    pass


CreateVirtualMFADeviceResponseResponseTypeDef = TypedDict(
    "CreateVirtualMFADeviceResponseResponseTypeDef",
    {
        "VirtualMFADevice": "VirtualMFADeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeactivateMFADeviceRequestTypeDef = TypedDict(
    "DeactivateMFADeviceRequestTypeDef",
    {
        "UserName": str,
        "SerialNumber": str,
    },
)

_RequiredDeleteAccessKeyRequestTypeDef = TypedDict(
    "_RequiredDeleteAccessKeyRequestTypeDef",
    {
        "AccessKeyId": str,
    },
)
_OptionalDeleteAccessKeyRequestTypeDef = TypedDict(
    "_OptionalDeleteAccessKeyRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)


class DeleteAccessKeyRequestTypeDef(
    _RequiredDeleteAccessKeyRequestTypeDef, _OptionalDeleteAccessKeyRequestTypeDef
):
    pass


DeleteAccountAliasRequestTypeDef = TypedDict(
    "DeleteAccountAliasRequestTypeDef",
    {
        "AccountAlias": str,
    },
)

DeleteGroupPolicyRequestTypeDef = TypedDict(
    "DeleteGroupPolicyRequestTypeDef",
    {
        "GroupName": str,
        "PolicyName": str,
    },
)

DeleteGroupRequestTypeDef = TypedDict(
    "DeleteGroupRequestTypeDef",
    {
        "GroupName": str,
    },
)

DeleteInstanceProfileRequestTypeDef = TypedDict(
    "DeleteInstanceProfileRequestTypeDef",
    {
        "InstanceProfileName": str,
    },
)

DeleteLoginProfileRequestTypeDef = TypedDict(
    "DeleteLoginProfileRequestTypeDef",
    {
        "UserName": str,
    },
)

DeleteOpenIDConnectProviderRequestTypeDef = TypedDict(
    "DeleteOpenIDConnectProviderRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
    },
)

DeletePolicyRequestTypeDef = TypedDict(
    "DeletePolicyRequestTypeDef",
    {
        "PolicyArn": str,
    },
)

DeletePolicyVersionRequestTypeDef = TypedDict(
    "DeletePolicyVersionRequestTypeDef",
    {
        "PolicyArn": str,
        "VersionId": str,
    },
)

DeleteRolePermissionsBoundaryRequestTypeDef = TypedDict(
    "DeleteRolePermissionsBoundaryRequestTypeDef",
    {
        "RoleName": str,
    },
)

DeleteRolePolicyRequestTypeDef = TypedDict(
    "DeleteRolePolicyRequestTypeDef",
    {
        "RoleName": str,
        "PolicyName": str,
    },
)

DeleteRoleRequestTypeDef = TypedDict(
    "DeleteRoleRequestTypeDef",
    {
        "RoleName": str,
    },
)

DeleteSAMLProviderRequestTypeDef = TypedDict(
    "DeleteSAMLProviderRequestTypeDef",
    {
        "SAMLProviderArn": str,
    },
)

DeleteSSHPublicKeyRequestTypeDef = TypedDict(
    "DeleteSSHPublicKeyRequestTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
    },
)

DeleteServerCertificateRequestTypeDef = TypedDict(
    "DeleteServerCertificateRequestTypeDef",
    {
        "ServerCertificateName": str,
    },
)

DeleteServiceLinkedRoleRequestTypeDef = TypedDict(
    "DeleteServiceLinkedRoleRequestTypeDef",
    {
        "RoleName": str,
    },
)

DeleteServiceLinkedRoleResponseResponseTypeDef = TypedDict(
    "DeleteServiceLinkedRoleResponseResponseTypeDef",
    {
        "DeletionTaskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteServiceSpecificCredentialRequestTypeDef = TypedDict(
    "_RequiredDeleteServiceSpecificCredentialRequestTypeDef",
    {
        "ServiceSpecificCredentialId": str,
    },
)
_OptionalDeleteServiceSpecificCredentialRequestTypeDef = TypedDict(
    "_OptionalDeleteServiceSpecificCredentialRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)


class DeleteServiceSpecificCredentialRequestTypeDef(
    _RequiredDeleteServiceSpecificCredentialRequestTypeDef,
    _OptionalDeleteServiceSpecificCredentialRequestTypeDef,
):
    pass


_RequiredDeleteSigningCertificateRequestTypeDef = TypedDict(
    "_RequiredDeleteSigningCertificateRequestTypeDef",
    {
        "CertificateId": str,
    },
)
_OptionalDeleteSigningCertificateRequestTypeDef = TypedDict(
    "_OptionalDeleteSigningCertificateRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)


class DeleteSigningCertificateRequestTypeDef(
    _RequiredDeleteSigningCertificateRequestTypeDef, _OptionalDeleteSigningCertificateRequestTypeDef
):
    pass


DeleteUserPermissionsBoundaryRequestTypeDef = TypedDict(
    "DeleteUserPermissionsBoundaryRequestTypeDef",
    {
        "UserName": str,
    },
)

DeleteUserPolicyRequestTypeDef = TypedDict(
    "DeleteUserPolicyRequestTypeDef",
    {
        "UserName": str,
        "PolicyName": str,
    },
)

DeleteUserRequestTypeDef = TypedDict(
    "DeleteUserRequestTypeDef",
    {
        "UserName": str,
    },
)

DeleteVirtualMFADeviceRequestTypeDef = TypedDict(
    "DeleteVirtualMFADeviceRequestTypeDef",
    {
        "SerialNumber": str,
    },
)

DeletionTaskFailureReasonTypeTypeDef = TypedDict(
    "DeletionTaskFailureReasonTypeTypeDef",
    {
        "Reason": str,
        "RoleUsageList": List["RoleUsageTypeTypeDef"],
    },
    total=False,
)

DetachGroupPolicyRequestGroupTypeDef = TypedDict(
    "DetachGroupPolicyRequestGroupTypeDef",
    {
        "PolicyArn": str,
    },
)

DetachGroupPolicyRequestPolicyTypeDef = TypedDict(
    "DetachGroupPolicyRequestPolicyTypeDef",
    {
        "GroupName": str,
    },
)

DetachGroupPolicyRequestTypeDef = TypedDict(
    "DetachGroupPolicyRequestTypeDef",
    {
        "GroupName": str,
        "PolicyArn": str,
    },
)

DetachRolePolicyRequestPolicyTypeDef = TypedDict(
    "DetachRolePolicyRequestPolicyTypeDef",
    {
        "RoleName": str,
    },
)

DetachRolePolicyRequestRoleTypeDef = TypedDict(
    "DetachRolePolicyRequestRoleTypeDef",
    {
        "PolicyArn": str,
    },
)

DetachRolePolicyRequestTypeDef = TypedDict(
    "DetachRolePolicyRequestTypeDef",
    {
        "RoleName": str,
        "PolicyArn": str,
    },
)

DetachUserPolicyRequestPolicyTypeDef = TypedDict(
    "DetachUserPolicyRequestPolicyTypeDef",
    {
        "UserName": str,
    },
)

DetachUserPolicyRequestTypeDef = TypedDict(
    "DetachUserPolicyRequestTypeDef",
    {
        "UserName": str,
        "PolicyArn": str,
    },
)

DetachUserPolicyRequestUserTypeDef = TypedDict(
    "DetachUserPolicyRequestUserTypeDef",
    {
        "PolicyArn": str,
    },
)

EnableMFADeviceRequestMfaDeviceTypeDef = TypedDict(
    "EnableMFADeviceRequestMfaDeviceTypeDef",
    {
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)

EnableMFADeviceRequestTypeDef = TypedDict(
    "EnableMFADeviceRequestTypeDef",
    {
        "UserName": str,
        "SerialNumber": str,
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)

EnableMFADeviceRequestUserTypeDef = TypedDict(
    "EnableMFADeviceRequestUserTypeDef",
    {
        "SerialNumber": str,
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)

_RequiredEntityDetailsTypeDef = TypedDict(
    "_RequiredEntityDetailsTypeDef",
    {
        "EntityInfo": "EntityInfoTypeDef",
    },
)
_OptionalEntityDetailsTypeDef = TypedDict(
    "_OptionalEntityDetailsTypeDef",
    {
        "LastAuthenticated": datetime,
    },
    total=False,
)


class EntityDetailsTypeDef(_RequiredEntityDetailsTypeDef, _OptionalEntityDetailsTypeDef):
    pass


_RequiredEntityInfoTypeDef = TypedDict(
    "_RequiredEntityInfoTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": policyOwnerEntityTypeType,
        "Id": str,
    },
)
_OptionalEntityInfoTypeDef = TypedDict(
    "_OptionalEntityInfoTypeDef",
    {
        "Path": str,
    },
    total=False,
)


class EntityInfoTypeDef(_RequiredEntityInfoTypeDef, _OptionalEntityInfoTypeDef):
    pass


ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "Message": str,
        "Code": str,
    },
)

_RequiredEvaluationResultTypeDef = TypedDict(
    "_RequiredEvaluationResultTypeDef",
    {
        "EvalActionName": str,
        "EvalDecision": PolicyEvaluationDecisionTypeType,
    },
)
_OptionalEvaluationResultTypeDef = TypedDict(
    "_OptionalEvaluationResultTypeDef",
    {
        "EvalResourceName": str,
        "MatchedStatements": List["StatementTypeDef"],
        "MissingContextValues": List[str],
        "OrganizationsDecisionDetail": "OrganizationsDecisionDetailTypeDef",
        "PermissionsBoundaryDecisionDetail": "PermissionsBoundaryDecisionDetailTypeDef",
        "EvalDecisionDetails": Dict[str, PolicyEvaluationDecisionTypeType],
        "ResourceSpecificResults": List["ResourceSpecificResultTypeDef"],
    },
    total=False,
)


class EvaluationResultTypeDef(_RequiredEvaluationResultTypeDef, _OptionalEvaluationResultTypeDef):
    pass


GenerateCredentialReportResponseResponseTypeDef = TypedDict(
    "GenerateCredentialReportResponseResponseTypeDef",
    {
        "State": ReportStateTypeType,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGenerateOrganizationsAccessReportRequestTypeDef = TypedDict(
    "_RequiredGenerateOrganizationsAccessReportRequestTypeDef",
    {
        "EntityPath": str,
    },
)
_OptionalGenerateOrganizationsAccessReportRequestTypeDef = TypedDict(
    "_OptionalGenerateOrganizationsAccessReportRequestTypeDef",
    {
        "OrganizationsPolicyId": str,
    },
    total=False,
)


class GenerateOrganizationsAccessReportRequestTypeDef(
    _RequiredGenerateOrganizationsAccessReportRequestTypeDef,
    _OptionalGenerateOrganizationsAccessReportRequestTypeDef,
):
    pass


GenerateOrganizationsAccessReportResponseResponseTypeDef = TypedDict(
    "GenerateOrganizationsAccessReportResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGenerateServiceLastAccessedDetailsRequestTypeDef = TypedDict(
    "_RequiredGenerateServiceLastAccessedDetailsRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalGenerateServiceLastAccessedDetailsRequestTypeDef = TypedDict(
    "_OptionalGenerateServiceLastAccessedDetailsRequestTypeDef",
    {
        "Granularity": AccessAdvisorUsageGranularityTypeType,
    },
    total=False,
)


class GenerateServiceLastAccessedDetailsRequestTypeDef(
    _RequiredGenerateServiceLastAccessedDetailsRequestTypeDef,
    _OptionalGenerateServiceLastAccessedDetailsRequestTypeDef,
):
    pass


GenerateServiceLastAccessedDetailsResponseResponseTypeDef = TypedDict(
    "GenerateServiceLastAccessedDetailsResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessKeyLastUsedRequestTypeDef = TypedDict(
    "GetAccessKeyLastUsedRequestTypeDef",
    {
        "AccessKeyId": str,
    },
)

GetAccessKeyLastUsedResponseResponseTypeDef = TypedDict(
    "GetAccessKeyLastUsedResponseResponseTypeDef",
    {
        "UserName": str,
        "AccessKeyLastUsed": "AccessKeyLastUsedTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccountAuthorizationDetailsRequestTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsRequestTypeDef",
    {
        "Filter": List[EntityTypeType],
        "MaxItems": int,
        "Marker": str,
    },
    total=False,
)

GetAccountAuthorizationDetailsResponseResponseTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsResponseResponseTypeDef",
    {
        "UserDetailList": List["UserDetailTypeDef"],
        "GroupDetailList": List["GroupDetailTypeDef"],
        "RoleDetailList": List["RoleDetailTypeDef"],
        "Policies": List["ManagedPolicyDetailTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccountPasswordPolicyResponseResponseTypeDef = TypedDict(
    "GetAccountPasswordPolicyResponseResponseTypeDef",
    {
        "PasswordPolicy": "PasswordPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccountSummaryResponseResponseTypeDef = TypedDict(
    "GetAccountSummaryResponseResponseTypeDef",
    {
        "SummaryMap": Dict[summaryKeyTypeType, int],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContextKeysForCustomPolicyRequestTypeDef = TypedDict(
    "GetContextKeysForCustomPolicyRequestTypeDef",
    {
        "PolicyInputList": List[str],
    },
)

GetContextKeysForPolicyResponseResponseTypeDef = TypedDict(
    "GetContextKeysForPolicyResponseResponseTypeDef",
    {
        "ContextKeyNames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetContextKeysForPrincipalPolicyRequestTypeDef = TypedDict(
    "_RequiredGetContextKeysForPrincipalPolicyRequestTypeDef",
    {
        "PolicySourceArn": str,
    },
)
_OptionalGetContextKeysForPrincipalPolicyRequestTypeDef = TypedDict(
    "_OptionalGetContextKeysForPrincipalPolicyRequestTypeDef",
    {
        "PolicyInputList": List[str],
    },
    total=False,
)


class GetContextKeysForPrincipalPolicyRequestTypeDef(
    _RequiredGetContextKeysForPrincipalPolicyRequestTypeDef,
    _OptionalGetContextKeysForPrincipalPolicyRequestTypeDef,
):
    pass


GetCredentialReportResponseResponseTypeDef = TypedDict(
    "GetCredentialReportResponseResponseTypeDef",
    {
        "Content": bytes,
        "ReportFormat": Literal["text/csv"],
        "GeneratedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupPolicyRequestTypeDef = TypedDict(
    "GetGroupPolicyRequestTypeDef",
    {
        "GroupName": str,
        "PolicyName": str,
    },
)

GetGroupPolicyResponseResponseTypeDef = TypedDict(
    "GetGroupPolicyResponseResponseTypeDef",
    {
        "GroupName": str,
        "PolicyName": str,
        "PolicyDocument": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetGroupRequestTypeDef = TypedDict(
    "_RequiredGetGroupRequestTypeDef",
    {
        "GroupName": str,
    },
)
_OptionalGetGroupRequestTypeDef = TypedDict(
    "_OptionalGetGroupRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class GetGroupRequestTypeDef(_RequiredGetGroupRequestTypeDef, _OptionalGetGroupRequestTypeDef):
    pass


GetGroupResponseResponseTypeDef = TypedDict(
    "GetGroupResponseResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "Users": List["UserTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceProfileRequestTypeDef = TypedDict(
    "GetInstanceProfileRequestTypeDef",
    {
        "InstanceProfileName": str,
    },
)

GetInstanceProfileResponseResponseTypeDef = TypedDict(
    "GetInstanceProfileResponseResponseTypeDef",
    {
        "InstanceProfile": "InstanceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoginProfileRequestTypeDef = TypedDict(
    "GetLoginProfileRequestTypeDef",
    {
        "UserName": str,
    },
)

GetLoginProfileResponseResponseTypeDef = TypedDict(
    "GetLoginProfileResponseResponseTypeDef",
    {
        "LoginProfile": "LoginProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOpenIDConnectProviderRequestTypeDef = TypedDict(
    "GetOpenIDConnectProviderRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
    },
)

GetOpenIDConnectProviderResponseResponseTypeDef = TypedDict(
    "GetOpenIDConnectProviderResponseResponseTypeDef",
    {
        "Url": str,
        "ClientIDList": List[str],
        "ThumbprintList": List[str],
        "CreateDate": datetime,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetOrganizationsAccessReportRequestTypeDef = TypedDict(
    "_RequiredGetOrganizationsAccessReportRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetOrganizationsAccessReportRequestTypeDef = TypedDict(
    "_OptionalGetOrganizationsAccessReportRequestTypeDef",
    {
        "MaxItems": int,
        "Marker": str,
        "SortKey": sortKeyTypeType,
    },
    total=False,
)


class GetOrganizationsAccessReportRequestTypeDef(
    _RequiredGetOrganizationsAccessReportRequestTypeDef,
    _OptionalGetOrganizationsAccessReportRequestTypeDef,
):
    pass


GetOrganizationsAccessReportResponseResponseTypeDef = TypedDict(
    "GetOrganizationsAccessReportResponseResponseTypeDef",
    {
        "JobStatus": jobStatusTypeType,
        "JobCreationDate": datetime,
        "JobCompletionDate": datetime,
        "NumberOfServicesAccessible": int,
        "NumberOfServicesNotAccessed": int,
        "AccessDetails": List["AccessDetailTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ErrorDetails": "ErrorDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyRequestTypeDef = TypedDict(
    "GetPolicyRequestTypeDef",
    {
        "PolicyArn": str,
    },
)

GetPolicyResponseResponseTypeDef = TypedDict(
    "GetPolicyResponseResponseTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyVersionRequestTypeDef = TypedDict(
    "GetPolicyVersionRequestTypeDef",
    {
        "PolicyArn": str,
        "VersionId": str,
    },
)

GetPolicyVersionResponseResponseTypeDef = TypedDict(
    "GetPolicyVersionResponseResponseTypeDef",
    {
        "PolicyVersion": "PolicyVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRolePolicyRequestTypeDef = TypedDict(
    "GetRolePolicyRequestTypeDef",
    {
        "RoleName": str,
        "PolicyName": str,
    },
)

GetRolePolicyResponseResponseTypeDef = TypedDict(
    "GetRolePolicyResponseResponseTypeDef",
    {
        "RoleName": str,
        "PolicyName": str,
        "PolicyDocument": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRoleRequestTypeDef = TypedDict(
    "GetRoleRequestTypeDef",
    {
        "RoleName": str,
    },
)

GetRoleResponseResponseTypeDef = TypedDict(
    "GetRoleResponseResponseTypeDef",
    {
        "Role": "RoleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSAMLProviderRequestTypeDef = TypedDict(
    "GetSAMLProviderRequestTypeDef",
    {
        "SAMLProviderArn": str,
    },
)

GetSAMLProviderResponseResponseTypeDef = TypedDict(
    "GetSAMLProviderResponseResponseTypeDef",
    {
        "SAMLMetadataDocument": str,
        "CreateDate": datetime,
        "ValidUntil": datetime,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSSHPublicKeyRequestTypeDef = TypedDict(
    "GetSSHPublicKeyRequestTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Encoding": encodingTypeType,
    },
)

GetSSHPublicKeyResponseResponseTypeDef = TypedDict(
    "GetSSHPublicKeyResponseResponseTypeDef",
    {
        "SSHPublicKey": "SSHPublicKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServerCertificateRequestTypeDef = TypedDict(
    "GetServerCertificateRequestTypeDef",
    {
        "ServerCertificateName": str,
    },
)

GetServerCertificateResponseResponseTypeDef = TypedDict(
    "GetServerCertificateResponseResponseTypeDef",
    {
        "ServerCertificate": "ServerCertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetServiceLastAccessedDetailsRequestTypeDef = TypedDict(
    "_RequiredGetServiceLastAccessedDetailsRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetServiceLastAccessedDetailsRequestTypeDef = TypedDict(
    "_OptionalGetServiceLastAccessedDetailsRequestTypeDef",
    {
        "MaxItems": int,
        "Marker": str,
    },
    total=False,
)


class GetServiceLastAccessedDetailsRequestTypeDef(
    _RequiredGetServiceLastAccessedDetailsRequestTypeDef,
    _OptionalGetServiceLastAccessedDetailsRequestTypeDef,
):
    pass


GetServiceLastAccessedDetailsResponseResponseTypeDef = TypedDict(
    "GetServiceLastAccessedDetailsResponseResponseTypeDef",
    {
        "JobStatus": jobStatusTypeType,
        "JobType": AccessAdvisorUsageGranularityTypeType,
        "JobCreationDate": datetime,
        "ServicesLastAccessed": List["ServiceLastAccessedTypeDef"],
        "JobCompletionDate": datetime,
        "IsTruncated": bool,
        "Marker": str,
        "Error": "ErrorDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetServiceLastAccessedDetailsWithEntitiesRequestTypeDef = TypedDict(
    "_RequiredGetServiceLastAccessedDetailsWithEntitiesRequestTypeDef",
    {
        "JobId": str,
        "ServiceNamespace": str,
    },
)
_OptionalGetServiceLastAccessedDetailsWithEntitiesRequestTypeDef = TypedDict(
    "_OptionalGetServiceLastAccessedDetailsWithEntitiesRequestTypeDef",
    {
        "MaxItems": int,
        "Marker": str,
    },
    total=False,
)


class GetServiceLastAccessedDetailsWithEntitiesRequestTypeDef(
    _RequiredGetServiceLastAccessedDetailsWithEntitiesRequestTypeDef,
    _OptionalGetServiceLastAccessedDetailsWithEntitiesRequestTypeDef,
):
    pass


GetServiceLastAccessedDetailsWithEntitiesResponseResponseTypeDef = TypedDict(
    "GetServiceLastAccessedDetailsWithEntitiesResponseResponseTypeDef",
    {
        "JobStatus": jobStatusTypeType,
        "JobCreationDate": datetime,
        "JobCompletionDate": datetime,
        "EntityDetailsList": List["EntityDetailsTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "Error": "ErrorDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceLinkedRoleDeletionStatusRequestTypeDef = TypedDict(
    "GetServiceLinkedRoleDeletionStatusRequestTypeDef",
    {
        "DeletionTaskId": str,
    },
)

GetServiceLinkedRoleDeletionStatusResponseResponseTypeDef = TypedDict(
    "GetServiceLinkedRoleDeletionStatusResponseResponseTypeDef",
    {
        "Status": DeletionTaskStatusTypeType,
        "Reason": "DeletionTaskFailureReasonTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserPolicyRequestTypeDef = TypedDict(
    "GetUserPolicyRequestTypeDef",
    {
        "UserName": str,
        "PolicyName": str,
    },
)

GetUserPolicyResponseResponseTypeDef = TypedDict(
    "GetUserPolicyResponseResponseTypeDef",
    {
        "UserName": str,
        "PolicyName": str,
        "PolicyDocument": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserRequestTypeDef = TypedDict(
    "GetUserRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)

GetUserResponseResponseTypeDef = TypedDict(
    "GetUserResponseResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupDetailTypeDef = TypedDict(
    "GroupDetailTypeDef",
    {
        "Path": str,
        "GroupName": str,
        "GroupId": str,
        "Arn": str,
        "CreateDate": datetime,
        "GroupPolicyList": List["PolicyDetailTypeDef"],
        "AttachedManagedPolicies": List["AttachedPolicyTypeDef"],
    },
    total=False,
)

GroupPolicyRequestTypeDef = TypedDict(
    "GroupPolicyRequestTypeDef",
    {
        "name": str,
    },
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Path": str,
        "GroupName": str,
        "GroupId": str,
        "Arn": str,
        "CreateDate": datetime,
    },
)

_RequiredInstanceProfileTypeDef = TypedDict(
    "_RequiredInstanceProfileTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List["RoleTypeDef"],
    },
)
_OptionalInstanceProfileTypeDef = TypedDict(
    "_OptionalInstanceProfileTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class InstanceProfileTypeDef(_RequiredInstanceProfileTypeDef, _OptionalInstanceProfileTypeDef):
    pass


ListAccessKeysRequestTypeDef = TypedDict(
    "ListAccessKeysRequestTypeDef",
    {
        "UserName": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListAccessKeysResponseResponseTypeDef = TypedDict(
    "ListAccessKeysResponseResponseTypeDef",
    {
        "AccessKeyMetadata": List["AccessKeyMetadataTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAccountAliasesRequestTypeDef = TypedDict(
    "ListAccountAliasesRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListAccountAliasesResponseResponseTypeDef = TypedDict(
    "ListAccountAliasesResponseResponseTypeDef",
    {
        "AccountAliases": List[str],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAttachedGroupPoliciesRequestTypeDef = TypedDict(
    "_RequiredListAttachedGroupPoliciesRequestTypeDef",
    {
        "GroupName": str,
    },
)
_OptionalListAttachedGroupPoliciesRequestTypeDef = TypedDict(
    "_OptionalListAttachedGroupPoliciesRequestTypeDef",
    {
        "PathPrefix": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListAttachedGroupPoliciesRequestTypeDef(
    _RequiredListAttachedGroupPoliciesRequestTypeDef,
    _OptionalListAttachedGroupPoliciesRequestTypeDef,
):
    pass


ListAttachedGroupPoliciesResponseResponseTypeDef = TypedDict(
    "ListAttachedGroupPoliciesResponseResponseTypeDef",
    {
        "AttachedPolicies": List["AttachedPolicyTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAttachedRolePoliciesRequestTypeDef = TypedDict(
    "_RequiredListAttachedRolePoliciesRequestTypeDef",
    {
        "RoleName": str,
    },
)
_OptionalListAttachedRolePoliciesRequestTypeDef = TypedDict(
    "_OptionalListAttachedRolePoliciesRequestTypeDef",
    {
        "PathPrefix": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListAttachedRolePoliciesRequestTypeDef(
    _RequiredListAttachedRolePoliciesRequestTypeDef, _OptionalListAttachedRolePoliciesRequestTypeDef
):
    pass


ListAttachedRolePoliciesResponseResponseTypeDef = TypedDict(
    "ListAttachedRolePoliciesResponseResponseTypeDef",
    {
        "AttachedPolicies": List["AttachedPolicyTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAttachedUserPoliciesRequestTypeDef = TypedDict(
    "_RequiredListAttachedUserPoliciesRequestTypeDef",
    {
        "UserName": str,
    },
)
_OptionalListAttachedUserPoliciesRequestTypeDef = TypedDict(
    "_OptionalListAttachedUserPoliciesRequestTypeDef",
    {
        "PathPrefix": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListAttachedUserPoliciesRequestTypeDef(
    _RequiredListAttachedUserPoliciesRequestTypeDef, _OptionalListAttachedUserPoliciesRequestTypeDef
):
    pass


ListAttachedUserPoliciesResponseResponseTypeDef = TypedDict(
    "ListAttachedUserPoliciesResponseResponseTypeDef",
    {
        "AttachedPolicies": List["AttachedPolicyTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEntitiesForPolicyRequestTypeDef = TypedDict(
    "_RequiredListEntitiesForPolicyRequestTypeDef",
    {
        "PolicyArn": str,
    },
)
_OptionalListEntitiesForPolicyRequestTypeDef = TypedDict(
    "_OptionalListEntitiesForPolicyRequestTypeDef",
    {
        "EntityFilter": EntityTypeType,
        "PathPrefix": str,
        "PolicyUsageFilter": PolicyUsageTypeType,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListEntitiesForPolicyRequestTypeDef(
    _RequiredListEntitiesForPolicyRequestTypeDef, _OptionalListEntitiesForPolicyRequestTypeDef
):
    pass


ListEntitiesForPolicyResponseResponseTypeDef = TypedDict(
    "ListEntitiesForPolicyResponseResponseTypeDef",
    {
        "PolicyGroups": List["PolicyGroupTypeDef"],
        "PolicyUsers": List["PolicyUserTypeDef"],
        "PolicyRoles": List["PolicyRoleTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupPoliciesRequestTypeDef = TypedDict(
    "_RequiredListGroupPoliciesRequestTypeDef",
    {
        "GroupName": str,
    },
)
_OptionalListGroupPoliciesRequestTypeDef = TypedDict(
    "_OptionalListGroupPoliciesRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListGroupPoliciesRequestTypeDef(
    _RequiredListGroupPoliciesRequestTypeDef, _OptionalListGroupPoliciesRequestTypeDef
):
    pass


ListGroupPoliciesResponseResponseTypeDef = TypedDict(
    "ListGroupPoliciesResponseResponseTypeDef",
    {
        "PolicyNames": List[str],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupsForUserRequestTypeDef = TypedDict(
    "_RequiredListGroupsForUserRequestTypeDef",
    {
        "UserName": str,
    },
)
_OptionalListGroupsForUserRequestTypeDef = TypedDict(
    "_OptionalListGroupsForUserRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListGroupsForUserRequestTypeDef(
    _RequiredListGroupsForUserRequestTypeDef, _OptionalListGroupsForUserRequestTypeDef
):
    pass


ListGroupsForUserResponseResponseTypeDef = TypedDict(
    "ListGroupsForUserResponseResponseTypeDef",
    {
        "Groups": List["GroupTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupsRequestTypeDef = TypedDict(
    "ListGroupsRequestTypeDef",
    {
        "PathPrefix": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListGroupsResponseResponseTypeDef = TypedDict(
    "ListGroupsResponseResponseTypeDef",
    {
        "Groups": List["GroupTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstanceProfileTagsRequestTypeDef = TypedDict(
    "_RequiredListInstanceProfileTagsRequestTypeDef",
    {
        "InstanceProfileName": str,
    },
)
_OptionalListInstanceProfileTagsRequestTypeDef = TypedDict(
    "_OptionalListInstanceProfileTagsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListInstanceProfileTagsRequestTypeDef(
    _RequiredListInstanceProfileTagsRequestTypeDef, _OptionalListInstanceProfileTagsRequestTypeDef
):
    pass


ListInstanceProfileTagsResponseResponseTypeDef = TypedDict(
    "ListInstanceProfileTagsResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstanceProfilesForRoleRequestTypeDef = TypedDict(
    "_RequiredListInstanceProfilesForRoleRequestTypeDef",
    {
        "RoleName": str,
    },
)
_OptionalListInstanceProfilesForRoleRequestTypeDef = TypedDict(
    "_OptionalListInstanceProfilesForRoleRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListInstanceProfilesForRoleRequestTypeDef(
    _RequiredListInstanceProfilesForRoleRequestTypeDef,
    _OptionalListInstanceProfilesForRoleRequestTypeDef,
):
    pass


ListInstanceProfilesForRoleResponseResponseTypeDef = TypedDict(
    "ListInstanceProfilesForRoleResponseResponseTypeDef",
    {
        "InstanceProfiles": List["InstanceProfileTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstanceProfilesRequestTypeDef = TypedDict(
    "ListInstanceProfilesRequestTypeDef",
    {
        "PathPrefix": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListInstanceProfilesResponseResponseTypeDef = TypedDict(
    "ListInstanceProfilesResponseResponseTypeDef",
    {
        "InstanceProfiles": List["InstanceProfileTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMFADeviceTagsRequestTypeDef = TypedDict(
    "_RequiredListMFADeviceTagsRequestTypeDef",
    {
        "SerialNumber": str,
    },
)
_OptionalListMFADeviceTagsRequestTypeDef = TypedDict(
    "_OptionalListMFADeviceTagsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListMFADeviceTagsRequestTypeDef(
    _RequiredListMFADeviceTagsRequestTypeDef, _OptionalListMFADeviceTagsRequestTypeDef
):
    pass


ListMFADeviceTagsResponseResponseTypeDef = TypedDict(
    "ListMFADeviceTagsResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMFADevicesRequestTypeDef = TypedDict(
    "ListMFADevicesRequestTypeDef",
    {
        "UserName": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListMFADevicesResponseResponseTypeDef = TypedDict(
    "ListMFADevicesResponseResponseTypeDef",
    {
        "MFADevices": List["MFADeviceTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListOpenIDConnectProviderTagsRequestTypeDef = TypedDict(
    "_RequiredListOpenIDConnectProviderTagsRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
    },
)
_OptionalListOpenIDConnectProviderTagsRequestTypeDef = TypedDict(
    "_OptionalListOpenIDConnectProviderTagsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListOpenIDConnectProviderTagsRequestTypeDef(
    _RequiredListOpenIDConnectProviderTagsRequestTypeDef,
    _OptionalListOpenIDConnectProviderTagsRequestTypeDef,
):
    pass


ListOpenIDConnectProviderTagsResponseResponseTypeDef = TypedDict(
    "ListOpenIDConnectProviderTagsResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOpenIDConnectProvidersResponseResponseTypeDef = TypedDict(
    "ListOpenIDConnectProvidersResponseResponseTypeDef",
    {
        "OpenIDConnectProviderList": List["OpenIDConnectProviderListEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPoliciesGrantingServiceAccessEntryTypeDef = TypedDict(
    "ListPoliciesGrantingServiceAccessEntryTypeDef",
    {
        "ServiceNamespace": str,
        "Policies": List["PolicyGrantingServiceAccessTypeDef"],
    },
    total=False,
)

_RequiredListPoliciesGrantingServiceAccessRequestTypeDef = TypedDict(
    "_RequiredListPoliciesGrantingServiceAccessRequestTypeDef",
    {
        "Arn": str,
        "ServiceNamespaces": List[str],
    },
)
_OptionalListPoliciesGrantingServiceAccessRequestTypeDef = TypedDict(
    "_OptionalListPoliciesGrantingServiceAccessRequestTypeDef",
    {
        "Marker": str,
    },
    total=False,
)


class ListPoliciesGrantingServiceAccessRequestTypeDef(
    _RequiredListPoliciesGrantingServiceAccessRequestTypeDef,
    _OptionalListPoliciesGrantingServiceAccessRequestTypeDef,
):
    pass


ListPoliciesGrantingServiceAccessResponseResponseTypeDef = TypedDict(
    "ListPoliciesGrantingServiceAccessResponseResponseTypeDef",
    {
        "PoliciesGrantingServiceAccess": List["ListPoliciesGrantingServiceAccessEntryTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPoliciesRequestTypeDef = TypedDict(
    "ListPoliciesRequestTypeDef",
    {
        "Scope": policyScopeTypeType,
        "OnlyAttached": bool,
        "PathPrefix": str,
        "PolicyUsageFilter": PolicyUsageTypeType,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListPoliciesResponseResponseTypeDef = TypedDict(
    "ListPoliciesResponseResponseTypeDef",
    {
        "Policies": List["PolicyTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPolicyTagsRequestTypeDef = TypedDict(
    "_RequiredListPolicyTagsRequestTypeDef",
    {
        "PolicyArn": str,
    },
)
_OptionalListPolicyTagsRequestTypeDef = TypedDict(
    "_OptionalListPolicyTagsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListPolicyTagsRequestTypeDef(
    _RequiredListPolicyTagsRequestTypeDef, _OptionalListPolicyTagsRequestTypeDef
):
    pass


ListPolicyTagsResponseResponseTypeDef = TypedDict(
    "ListPolicyTagsResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPolicyVersionsRequestTypeDef = TypedDict(
    "_RequiredListPolicyVersionsRequestTypeDef",
    {
        "PolicyArn": str,
    },
)
_OptionalListPolicyVersionsRequestTypeDef = TypedDict(
    "_OptionalListPolicyVersionsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListPolicyVersionsRequestTypeDef(
    _RequiredListPolicyVersionsRequestTypeDef, _OptionalListPolicyVersionsRequestTypeDef
):
    pass


ListPolicyVersionsResponseResponseTypeDef = TypedDict(
    "ListPolicyVersionsResponseResponseTypeDef",
    {
        "Versions": List["PolicyVersionTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRolePoliciesRequestTypeDef = TypedDict(
    "_RequiredListRolePoliciesRequestTypeDef",
    {
        "RoleName": str,
    },
)
_OptionalListRolePoliciesRequestTypeDef = TypedDict(
    "_OptionalListRolePoliciesRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListRolePoliciesRequestTypeDef(
    _RequiredListRolePoliciesRequestTypeDef, _OptionalListRolePoliciesRequestTypeDef
):
    pass


ListRolePoliciesResponseResponseTypeDef = TypedDict(
    "ListRolePoliciesResponseResponseTypeDef",
    {
        "PolicyNames": List[str],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRoleTagsRequestTypeDef = TypedDict(
    "_RequiredListRoleTagsRequestTypeDef",
    {
        "RoleName": str,
    },
)
_OptionalListRoleTagsRequestTypeDef = TypedDict(
    "_OptionalListRoleTagsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListRoleTagsRequestTypeDef(
    _RequiredListRoleTagsRequestTypeDef, _OptionalListRoleTagsRequestTypeDef
):
    pass


ListRoleTagsResponseResponseTypeDef = TypedDict(
    "ListRoleTagsResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRolesRequestTypeDef = TypedDict(
    "ListRolesRequestTypeDef",
    {
        "PathPrefix": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListRolesResponseResponseTypeDef = TypedDict(
    "ListRolesResponseResponseTypeDef",
    {
        "Roles": List["RoleTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSAMLProviderTagsRequestTypeDef = TypedDict(
    "_RequiredListSAMLProviderTagsRequestTypeDef",
    {
        "SAMLProviderArn": str,
    },
)
_OptionalListSAMLProviderTagsRequestTypeDef = TypedDict(
    "_OptionalListSAMLProviderTagsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListSAMLProviderTagsRequestTypeDef(
    _RequiredListSAMLProviderTagsRequestTypeDef, _OptionalListSAMLProviderTagsRequestTypeDef
):
    pass


ListSAMLProviderTagsResponseResponseTypeDef = TypedDict(
    "ListSAMLProviderTagsResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSAMLProvidersResponseResponseTypeDef = TypedDict(
    "ListSAMLProvidersResponseResponseTypeDef",
    {
        "SAMLProviderList": List["SAMLProviderListEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSSHPublicKeysRequestTypeDef = TypedDict(
    "ListSSHPublicKeysRequestTypeDef",
    {
        "UserName": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListSSHPublicKeysResponseResponseTypeDef = TypedDict(
    "ListSSHPublicKeysResponseResponseTypeDef",
    {
        "SSHPublicKeys": List["SSHPublicKeyMetadataTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServerCertificateTagsRequestTypeDef = TypedDict(
    "_RequiredListServerCertificateTagsRequestTypeDef",
    {
        "ServerCertificateName": str,
    },
)
_OptionalListServerCertificateTagsRequestTypeDef = TypedDict(
    "_OptionalListServerCertificateTagsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListServerCertificateTagsRequestTypeDef(
    _RequiredListServerCertificateTagsRequestTypeDef,
    _OptionalListServerCertificateTagsRequestTypeDef,
):
    pass


ListServerCertificateTagsResponseResponseTypeDef = TypedDict(
    "ListServerCertificateTagsResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServerCertificatesRequestTypeDef = TypedDict(
    "ListServerCertificatesRequestTypeDef",
    {
        "PathPrefix": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListServerCertificatesResponseResponseTypeDef = TypedDict(
    "ListServerCertificatesResponseResponseTypeDef",
    {
        "ServerCertificateMetadataList": List["ServerCertificateMetadataTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceSpecificCredentialsRequestTypeDef = TypedDict(
    "ListServiceSpecificCredentialsRequestTypeDef",
    {
        "UserName": str,
        "ServiceName": str,
    },
    total=False,
)

ListServiceSpecificCredentialsResponseResponseTypeDef = TypedDict(
    "ListServiceSpecificCredentialsResponseResponseTypeDef",
    {
        "ServiceSpecificCredentials": List["ServiceSpecificCredentialMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSigningCertificatesRequestTypeDef = TypedDict(
    "ListSigningCertificatesRequestTypeDef",
    {
        "UserName": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListSigningCertificatesResponseResponseTypeDef = TypedDict(
    "ListSigningCertificatesResponseResponseTypeDef",
    {
        "Certificates": List["SigningCertificateTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUserPoliciesRequestTypeDef = TypedDict(
    "_RequiredListUserPoliciesRequestTypeDef",
    {
        "UserName": str,
    },
)
_OptionalListUserPoliciesRequestTypeDef = TypedDict(
    "_OptionalListUserPoliciesRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListUserPoliciesRequestTypeDef(
    _RequiredListUserPoliciesRequestTypeDef, _OptionalListUserPoliciesRequestTypeDef
):
    pass


ListUserPoliciesResponseResponseTypeDef = TypedDict(
    "ListUserPoliciesResponseResponseTypeDef",
    {
        "PolicyNames": List[str],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUserTagsRequestTypeDef = TypedDict(
    "_RequiredListUserTagsRequestTypeDef",
    {
        "UserName": str,
    },
)
_OptionalListUserTagsRequestTypeDef = TypedDict(
    "_OptionalListUserTagsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)


class ListUserTagsRequestTypeDef(
    _RequiredListUserTagsRequestTypeDef, _OptionalListUserTagsRequestTypeDef
):
    pass


ListUserTagsResponseResponseTypeDef = TypedDict(
    "ListUserTagsResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUsersRequestTypeDef = TypedDict(
    "ListUsersRequestTypeDef",
    {
        "PathPrefix": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListUsersResponseResponseTypeDef = TypedDict(
    "ListUsersResponseResponseTypeDef",
    {
        "Users": List["UserTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVirtualMFADevicesRequestTypeDef = TypedDict(
    "ListVirtualMFADevicesRequestTypeDef",
    {
        "AssignmentStatus": assignmentStatusTypeType,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListVirtualMFADevicesResponseResponseTypeDef = TypedDict(
    "ListVirtualMFADevicesResponseResponseTypeDef",
    {
        "VirtualMFADevices": List["VirtualMFADeviceTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLoginProfileTypeDef = TypedDict(
    "_RequiredLoginProfileTypeDef",
    {
        "UserName": str,
        "CreateDate": datetime,
    },
)
_OptionalLoginProfileTypeDef = TypedDict(
    "_OptionalLoginProfileTypeDef",
    {
        "PasswordResetRequired": bool,
    },
    total=False,
)


class LoginProfileTypeDef(_RequiredLoginProfileTypeDef, _OptionalLoginProfileTypeDef):
    pass


MFADeviceTypeDef = TypedDict(
    "MFADeviceTypeDef",
    {
        "UserName": str,
        "SerialNumber": str,
        "EnableDate": datetime,
    },
)

ManagedPolicyDetailTypeDef = TypedDict(
    "ManagedPolicyDetailTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
        "PolicyVersionList": List["PolicyVersionTypeDef"],
    },
    total=False,
)

OpenIDConnectProviderListEntryTypeDef = TypedDict(
    "OpenIDConnectProviderListEntryTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

OrganizationsDecisionDetailTypeDef = TypedDict(
    "OrganizationsDecisionDetailTypeDef",
    {
        "AllowedByOrganizations": bool,
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

PasswordPolicyTypeDef = TypedDict(
    "PasswordPolicyTypeDef",
    {
        "MinimumPasswordLength": int,
        "RequireSymbols": bool,
        "RequireNumbers": bool,
        "RequireUppercaseCharacters": bool,
        "RequireLowercaseCharacters": bool,
        "AllowUsersToChangePassword": bool,
        "ExpirePasswords": bool,
        "MaxPasswordAge": int,
        "PasswordReusePrevention": int,
        "HardExpiry": bool,
    },
    total=False,
)

PermissionsBoundaryDecisionDetailTypeDef = TypedDict(
    "PermissionsBoundaryDecisionDetailTypeDef",
    {
        "AllowedByPermissionsBoundary": bool,
    },
    total=False,
)

PolicyDetailTypeDef = TypedDict(
    "PolicyDetailTypeDef",
    {
        "PolicyName": str,
        "PolicyDocument": str,
    },
    total=False,
)

_RequiredPolicyGrantingServiceAccessTypeDef = TypedDict(
    "_RequiredPolicyGrantingServiceAccessTypeDef",
    {
        "PolicyName": str,
        "PolicyType": policyTypeType,
    },
)
_OptionalPolicyGrantingServiceAccessTypeDef = TypedDict(
    "_OptionalPolicyGrantingServiceAccessTypeDef",
    {
        "PolicyArn": str,
        "EntityType": policyOwnerEntityTypeType,
        "EntityName": str,
    },
    total=False,
)


class PolicyGrantingServiceAccessTypeDef(
    _RequiredPolicyGrantingServiceAccessTypeDef, _OptionalPolicyGrantingServiceAccessTypeDef
):
    pass


PolicyGroupTypeDef = TypedDict(
    "PolicyGroupTypeDef",
    {
        "GroupName": str,
        "GroupId": str,
    },
    total=False,
)

PolicyRoleTypeDef = TypedDict(
    "PolicyRoleTypeDef",
    {
        "RoleName": str,
        "RoleId": str,
    },
    total=False,
)

PolicyTypeDef = TypedDict(
    "PolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

PolicyUserTypeDef = TypedDict(
    "PolicyUserTypeDef",
    {
        "UserName": str,
        "UserId": str,
    },
    total=False,
)

PolicyVersionTypeDef = TypedDict(
    "PolicyVersionTypeDef",
    {
        "Document": str,
        "VersionId": str,
        "IsDefaultVersion": bool,
        "CreateDate": datetime,
    },
    total=False,
)

PositionTypeDef = TypedDict(
    "PositionTypeDef",
    {
        "Line": int,
        "Column": int,
    },
    total=False,
)

PutGroupPolicyRequestGroupPolicyTypeDef = TypedDict(
    "PutGroupPolicyRequestGroupPolicyTypeDef",
    {
        "PolicyDocument": str,
    },
)

PutGroupPolicyRequestGroupTypeDef = TypedDict(
    "PutGroupPolicyRequestGroupTypeDef",
    {
        "PolicyName": str,
        "PolicyDocument": str,
    },
)

PutGroupPolicyRequestTypeDef = TypedDict(
    "PutGroupPolicyRequestTypeDef",
    {
        "GroupName": str,
        "PolicyName": str,
        "PolicyDocument": str,
    },
)

PutRolePermissionsBoundaryRequestTypeDef = TypedDict(
    "PutRolePermissionsBoundaryRequestTypeDef",
    {
        "RoleName": str,
        "PermissionsBoundary": str,
    },
)

PutRolePolicyRequestRolePolicyTypeDef = TypedDict(
    "PutRolePolicyRequestRolePolicyTypeDef",
    {
        "PolicyDocument": str,
    },
)

PutRolePolicyRequestTypeDef = TypedDict(
    "PutRolePolicyRequestTypeDef",
    {
        "RoleName": str,
        "PolicyName": str,
        "PolicyDocument": str,
    },
)

PutUserPermissionsBoundaryRequestTypeDef = TypedDict(
    "PutUserPermissionsBoundaryRequestTypeDef",
    {
        "UserName": str,
        "PermissionsBoundary": str,
    },
)

PutUserPolicyRequestTypeDef = TypedDict(
    "PutUserPolicyRequestTypeDef",
    {
        "UserName": str,
        "PolicyName": str,
        "PolicyDocument": str,
    },
)

PutUserPolicyRequestUserPolicyTypeDef = TypedDict(
    "PutUserPolicyRequestUserPolicyTypeDef",
    {
        "PolicyDocument": str,
    },
)

PutUserPolicyRequestUserTypeDef = TypedDict(
    "PutUserPolicyRequestUserTypeDef",
    {
        "PolicyName": str,
        "PolicyDocument": str,
    },
)

RemoveClientIDFromOpenIDConnectProviderRequestTypeDef = TypedDict(
    "RemoveClientIDFromOpenIDConnectProviderRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "ClientID": str,
    },
)

RemoveRoleFromInstanceProfileRequestInstanceProfileTypeDef = TypedDict(
    "RemoveRoleFromInstanceProfileRequestInstanceProfileTypeDef",
    {
        "RoleName": str,
    },
)

RemoveRoleFromInstanceProfileRequestTypeDef = TypedDict(
    "RemoveRoleFromInstanceProfileRequestTypeDef",
    {
        "InstanceProfileName": str,
        "RoleName": str,
    },
)

RemoveUserFromGroupRequestGroupTypeDef = TypedDict(
    "RemoveUserFromGroupRequestGroupTypeDef",
    {
        "UserName": str,
    },
)

RemoveUserFromGroupRequestTypeDef = TypedDict(
    "RemoveUserFromGroupRequestTypeDef",
    {
        "GroupName": str,
        "UserName": str,
    },
)

RemoveUserFromGroupRequestUserTypeDef = TypedDict(
    "RemoveUserFromGroupRequestUserTypeDef",
    {
        "GroupName": str,
    },
)

_RequiredResetServiceSpecificCredentialRequestTypeDef = TypedDict(
    "_RequiredResetServiceSpecificCredentialRequestTypeDef",
    {
        "ServiceSpecificCredentialId": str,
    },
)
_OptionalResetServiceSpecificCredentialRequestTypeDef = TypedDict(
    "_OptionalResetServiceSpecificCredentialRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)


class ResetServiceSpecificCredentialRequestTypeDef(
    _RequiredResetServiceSpecificCredentialRequestTypeDef,
    _OptionalResetServiceSpecificCredentialRequestTypeDef,
):
    pass


ResetServiceSpecificCredentialResponseResponseTypeDef = TypedDict(
    "ResetServiceSpecificCredentialResponseResponseTypeDef",
    {
        "ServiceSpecificCredential": "ServiceSpecificCredentialTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredResourceSpecificResultTypeDef = TypedDict(
    "_RequiredResourceSpecificResultTypeDef",
    {
        "EvalResourceName": str,
        "EvalResourceDecision": PolicyEvaluationDecisionTypeType,
    },
)
_OptionalResourceSpecificResultTypeDef = TypedDict(
    "_OptionalResourceSpecificResultTypeDef",
    {
        "MatchedStatements": List["StatementTypeDef"],
        "MissingContextValues": List[str],
        "EvalDecisionDetails": Dict[str, PolicyEvaluationDecisionTypeType],
        "PermissionsBoundaryDecisionDetail": "PermissionsBoundaryDecisionDetailTypeDef",
    },
    total=False,
)


class ResourceSpecificResultTypeDef(
    _RequiredResourceSpecificResultTypeDef, _OptionalResourceSpecificResultTypeDef
):
    pass


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

ResyncMFADeviceRequestMfaDeviceTypeDef = TypedDict(
    "ResyncMFADeviceRequestMfaDeviceTypeDef",
    {
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)

ResyncMFADeviceRequestTypeDef = TypedDict(
    "ResyncMFADeviceRequestTypeDef",
    {
        "UserName": str,
        "SerialNumber": str,
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)

RoleDetailTypeDef = TypedDict(
    "RoleDetailTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "InstanceProfileList": List["InstanceProfileTypeDef"],
        "RolePolicyList": List["PolicyDetailTypeDef"],
        "AttachedManagedPolicies": List["AttachedPolicyTypeDef"],
        "PermissionsBoundary": "AttachedPermissionsBoundaryTypeDef",
        "Tags": List["TagTypeDef"],
        "RoleLastUsed": "RoleLastUsedTypeDef",
    },
    total=False,
)

RoleLastUsedTypeDef = TypedDict(
    "RoleLastUsedTypeDef",
    {
        "LastUsedDate": datetime,
        "Region": str,
    },
    total=False,
)

RolePolicyRequestTypeDef = TypedDict(
    "RolePolicyRequestTypeDef",
    {
        "name": str,
    },
)

_RequiredRoleTypeDef = TypedDict(
    "_RequiredRoleTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
    },
)
_OptionalRoleTypeDef = TypedDict(
    "_OptionalRoleTypeDef",
    {
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": "AttachedPermissionsBoundaryTypeDef",
        "Tags": List["TagTypeDef"],
        "RoleLastUsed": "RoleLastUsedTypeDef",
    },
    total=False,
)


class RoleTypeDef(_RequiredRoleTypeDef, _OptionalRoleTypeDef):
    pass


RoleUsageTypeTypeDef = TypedDict(
    "RoleUsageTypeTypeDef",
    {
        "Region": str,
        "Resources": List[str],
    },
    total=False,
)

SAMLProviderListEntryTypeDef = TypedDict(
    "SAMLProviderListEntryTypeDef",
    {
        "Arn": str,
        "ValidUntil": datetime,
        "CreateDate": datetime,
    },
    total=False,
)

SSHPublicKeyMetadataTypeDef = TypedDict(
    "SSHPublicKeyMetadataTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Status": statusTypeType,
        "UploadDate": datetime,
    },
)

_RequiredSSHPublicKeyTypeDef = TypedDict(
    "_RequiredSSHPublicKeyTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Fingerprint": str,
        "SSHPublicKeyBody": str,
        "Status": statusTypeType,
    },
)
_OptionalSSHPublicKeyTypeDef = TypedDict(
    "_OptionalSSHPublicKeyTypeDef",
    {
        "UploadDate": datetime,
    },
    total=False,
)


class SSHPublicKeyTypeDef(_RequiredSSHPublicKeyTypeDef, _OptionalSSHPublicKeyTypeDef):
    pass


_RequiredServerCertificateMetadataTypeDef = TypedDict(
    "_RequiredServerCertificateMetadataTypeDef",
    {
        "Path": str,
        "ServerCertificateName": str,
        "ServerCertificateId": str,
        "Arn": str,
    },
)
_OptionalServerCertificateMetadataTypeDef = TypedDict(
    "_OptionalServerCertificateMetadataTypeDef",
    {
        "UploadDate": datetime,
        "Expiration": datetime,
    },
    total=False,
)


class ServerCertificateMetadataTypeDef(
    _RequiredServerCertificateMetadataTypeDef, _OptionalServerCertificateMetadataTypeDef
):
    pass


_RequiredServerCertificateTypeDef = TypedDict(
    "_RequiredServerCertificateTypeDef",
    {
        "ServerCertificateMetadata": "ServerCertificateMetadataTypeDef",
        "CertificateBody": str,
    },
)
_OptionalServerCertificateTypeDef = TypedDict(
    "_OptionalServerCertificateTypeDef",
    {
        "CertificateChain": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class ServerCertificateTypeDef(
    _RequiredServerCertificateTypeDef, _OptionalServerCertificateTypeDef
):
    pass


_RequiredServiceLastAccessedTypeDef = TypedDict(
    "_RequiredServiceLastAccessedTypeDef",
    {
        "ServiceName": str,
        "ServiceNamespace": str,
    },
)
_OptionalServiceLastAccessedTypeDef = TypedDict(
    "_OptionalServiceLastAccessedTypeDef",
    {
        "LastAuthenticated": datetime,
        "LastAuthenticatedEntity": str,
        "LastAuthenticatedRegion": str,
        "TotalAuthenticatedEntities": int,
        "TrackedActionsLastAccessed": List["TrackedActionLastAccessedTypeDef"],
    },
    total=False,
)


class ServiceLastAccessedTypeDef(
    _RequiredServiceLastAccessedTypeDef, _OptionalServiceLastAccessedTypeDef
):
    pass


ServiceResourceAccessKeyPairRequestTypeDef = TypedDict(
    "ServiceResourceAccessKeyPairRequestTypeDef",
    {
        "user_name": str,
        "id": str,
        "secret": str,
    },
)

ServiceResourceAccessKeyRequestTypeDef = TypedDict(
    "ServiceResourceAccessKeyRequestTypeDef",
    {
        "user_name": str,
        "id": str,
    },
)

ServiceResourceAssumeRolePolicyRequestTypeDef = TypedDict(
    "ServiceResourceAssumeRolePolicyRequestTypeDef",
    {
        "role_name": str,
    },
)

ServiceResourceGroupPolicyRequestTypeDef = TypedDict(
    "ServiceResourceGroupPolicyRequestTypeDef",
    {
        "group_name": str,
        "name": str,
    },
)

ServiceResourceGroupRequestTypeDef = TypedDict(
    "ServiceResourceGroupRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceInstanceProfileRequestTypeDef = TypedDict(
    "ServiceResourceInstanceProfileRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceLoginProfileRequestTypeDef = TypedDict(
    "ServiceResourceLoginProfileRequestTypeDef",
    {
        "user_name": str,
    },
)

ServiceResourceMfaDeviceRequestTypeDef = TypedDict(
    "ServiceResourceMfaDeviceRequestTypeDef",
    {
        "user_name": str,
        "serial_number": str,
    },
)

ServiceResourcePolicyRequestTypeDef = TypedDict(
    "ServiceResourcePolicyRequestTypeDef",
    {
        "policy_arn": str,
    },
)

ServiceResourcePolicyVersionRequestTypeDef = TypedDict(
    "ServiceResourcePolicyVersionRequestTypeDef",
    {
        "arn": str,
        "version_id": str,
    },
)

ServiceResourceRolePolicyRequestTypeDef = TypedDict(
    "ServiceResourceRolePolicyRequestTypeDef",
    {
        "role_name": str,
        "name": str,
    },
)

ServiceResourceRoleRequestTypeDef = TypedDict(
    "ServiceResourceRoleRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceSamlProviderRequestTypeDef = TypedDict(
    "ServiceResourceSamlProviderRequestTypeDef",
    {
        "arn": str,
    },
)

ServiceResourceServerCertificateRequestTypeDef = TypedDict(
    "ServiceResourceServerCertificateRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceSigningCertificateRequestTypeDef = TypedDict(
    "ServiceResourceSigningCertificateRequestTypeDef",
    {
        "user_name": str,
        "id": str,
    },
)

ServiceResourceUserPolicyRequestTypeDef = TypedDict(
    "ServiceResourceUserPolicyRequestTypeDef",
    {
        "user_name": str,
        "name": str,
    },
)

ServiceResourceUserRequestTypeDef = TypedDict(
    "ServiceResourceUserRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceVirtualMfaDeviceRequestTypeDef = TypedDict(
    "ServiceResourceVirtualMfaDeviceRequestTypeDef",
    {
        "serial_number": str,
    },
)

ServiceSpecificCredentialMetadataTypeDef = TypedDict(
    "ServiceSpecificCredentialMetadataTypeDef",
    {
        "UserName": str,
        "Status": statusTypeType,
        "ServiceUserName": str,
        "CreateDate": datetime,
        "ServiceSpecificCredentialId": str,
        "ServiceName": str,
    },
)

ServiceSpecificCredentialTypeDef = TypedDict(
    "ServiceSpecificCredentialTypeDef",
    {
        "CreateDate": datetime,
        "ServiceName": str,
        "ServiceUserName": str,
        "ServicePassword": str,
        "ServiceSpecificCredentialId": str,
        "UserName": str,
        "Status": statusTypeType,
    },
)

SetDefaultPolicyVersionRequestTypeDef = TypedDict(
    "SetDefaultPolicyVersionRequestTypeDef",
    {
        "PolicyArn": str,
        "VersionId": str,
    },
)

SetSecurityTokenServicePreferencesRequestTypeDef = TypedDict(
    "SetSecurityTokenServicePreferencesRequestTypeDef",
    {
        "GlobalEndpointTokenVersion": globalEndpointTokenVersionType,
    },
)

_RequiredSigningCertificateTypeDef = TypedDict(
    "_RequiredSigningCertificateTypeDef",
    {
        "UserName": str,
        "CertificateId": str,
        "CertificateBody": str,
        "Status": statusTypeType,
    },
)
_OptionalSigningCertificateTypeDef = TypedDict(
    "_OptionalSigningCertificateTypeDef",
    {
        "UploadDate": datetime,
    },
    total=False,
)


class SigningCertificateTypeDef(
    _RequiredSigningCertificateTypeDef, _OptionalSigningCertificateTypeDef
):
    pass


_RequiredSimulateCustomPolicyRequestTypeDef = TypedDict(
    "_RequiredSimulateCustomPolicyRequestTypeDef",
    {
        "PolicyInputList": List[str],
        "ActionNames": List[str],
    },
)
_OptionalSimulateCustomPolicyRequestTypeDef = TypedDict(
    "_OptionalSimulateCustomPolicyRequestTypeDef",
    {
        "PermissionsBoundaryPolicyInputList": List[str],
        "ResourceArns": List[str],
        "ResourcePolicy": str,
        "ResourceOwner": str,
        "CallerArn": str,
        "ContextEntries": List["ContextEntryTypeDef"],
        "ResourceHandlingOption": str,
        "MaxItems": int,
        "Marker": str,
    },
    total=False,
)


class SimulateCustomPolicyRequestTypeDef(
    _RequiredSimulateCustomPolicyRequestTypeDef, _OptionalSimulateCustomPolicyRequestTypeDef
):
    pass


SimulatePolicyResponseResponseTypeDef = TypedDict(
    "SimulatePolicyResponseResponseTypeDef",
    {
        "EvaluationResults": List["EvaluationResultTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSimulatePrincipalPolicyRequestTypeDef = TypedDict(
    "_RequiredSimulatePrincipalPolicyRequestTypeDef",
    {
        "PolicySourceArn": str,
        "ActionNames": List[str],
    },
)
_OptionalSimulatePrincipalPolicyRequestTypeDef = TypedDict(
    "_OptionalSimulatePrincipalPolicyRequestTypeDef",
    {
        "PolicyInputList": List[str],
        "PermissionsBoundaryPolicyInputList": List[str],
        "ResourceArns": List[str],
        "ResourcePolicy": str,
        "ResourceOwner": str,
        "CallerArn": str,
        "ContextEntries": List["ContextEntryTypeDef"],
        "ResourceHandlingOption": str,
        "MaxItems": int,
        "Marker": str,
    },
    total=False,
)


class SimulatePrincipalPolicyRequestTypeDef(
    _RequiredSimulatePrincipalPolicyRequestTypeDef, _OptionalSimulatePrincipalPolicyRequestTypeDef
):
    pass


StatementTypeDef = TypedDict(
    "StatementTypeDef",
    {
        "SourcePolicyId": str,
        "SourcePolicyType": PolicySourceTypeType,
        "StartPosition": "PositionTypeDef",
        "EndPosition": "PositionTypeDef",
    },
    total=False,
)

TagInstanceProfileRequestTypeDef = TypedDict(
    "TagInstanceProfileRequestTypeDef",
    {
        "InstanceProfileName": str,
        "Tags": List["TagTypeDef"],
    },
)

TagMFADeviceRequestTypeDef = TypedDict(
    "TagMFADeviceRequestTypeDef",
    {
        "SerialNumber": str,
        "Tags": List["TagTypeDef"],
    },
)

TagOpenIDConnectProviderRequestTypeDef = TypedDict(
    "TagOpenIDConnectProviderRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagPolicyRequestTypeDef = TypedDict(
    "TagPolicyRequestTypeDef",
    {
        "PolicyArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagRoleRequestTypeDef = TypedDict(
    "TagRoleRequestTypeDef",
    {
        "RoleName": str,
        "Tags": List["TagTypeDef"],
    },
)

TagSAMLProviderRequestTypeDef = TypedDict(
    "TagSAMLProviderRequestTypeDef",
    {
        "SAMLProviderArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagServerCertificateRequestTypeDef = TypedDict(
    "TagServerCertificateRequestTypeDef",
    {
        "ServerCertificateName": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TagUserRequestTypeDef = TypedDict(
    "TagUserRequestTypeDef",
    {
        "UserName": str,
        "Tags": List["TagTypeDef"],
    },
)

TrackedActionLastAccessedTypeDef = TypedDict(
    "TrackedActionLastAccessedTypeDef",
    {
        "ActionName": str,
        "LastAccessedEntity": str,
        "LastAccessedTime": datetime,
        "LastAccessedRegion": str,
    },
    total=False,
)

UntagInstanceProfileRequestTypeDef = TypedDict(
    "UntagInstanceProfileRequestTypeDef",
    {
        "InstanceProfileName": str,
        "TagKeys": List[str],
    },
)

UntagMFADeviceRequestTypeDef = TypedDict(
    "UntagMFADeviceRequestTypeDef",
    {
        "SerialNumber": str,
        "TagKeys": List[str],
    },
)

UntagOpenIDConnectProviderRequestTypeDef = TypedDict(
    "UntagOpenIDConnectProviderRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "TagKeys": List[str],
    },
)

UntagPolicyRequestTypeDef = TypedDict(
    "UntagPolicyRequestTypeDef",
    {
        "PolicyArn": str,
        "TagKeys": List[str],
    },
)

UntagRoleRequestTypeDef = TypedDict(
    "UntagRoleRequestTypeDef",
    {
        "RoleName": str,
        "TagKeys": List[str],
    },
)

UntagSAMLProviderRequestTypeDef = TypedDict(
    "UntagSAMLProviderRequestTypeDef",
    {
        "SAMLProviderArn": str,
        "TagKeys": List[str],
    },
)

UntagServerCertificateRequestTypeDef = TypedDict(
    "UntagServerCertificateRequestTypeDef",
    {
        "ServerCertificateName": str,
        "TagKeys": List[str],
    },
)

UntagUserRequestTypeDef = TypedDict(
    "UntagUserRequestTypeDef",
    {
        "UserName": str,
        "TagKeys": List[str],
    },
)

UpdateAccessKeyRequestAccessKeyPairTypeDef = TypedDict(
    "UpdateAccessKeyRequestAccessKeyPairTypeDef",
    {
        "Status": statusTypeType,
    },
)

UpdateAccessKeyRequestAccessKeyTypeDef = TypedDict(
    "UpdateAccessKeyRequestAccessKeyTypeDef",
    {
        "Status": statusTypeType,
    },
)

_RequiredUpdateAccessKeyRequestTypeDef = TypedDict(
    "_RequiredUpdateAccessKeyRequestTypeDef",
    {
        "AccessKeyId": str,
        "Status": statusTypeType,
    },
)
_OptionalUpdateAccessKeyRequestTypeDef = TypedDict(
    "_OptionalUpdateAccessKeyRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)


class UpdateAccessKeyRequestTypeDef(
    _RequiredUpdateAccessKeyRequestTypeDef, _OptionalUpdateAccessKeyRequestTypeDef
):
    pass


UpdateAccountPasswordPolicyRequestAccountPasswordPolicyTypeDef = TypedDict(
    "UpdateAccountPasswordPolicyRequestAccountPasswordPolicyTypeDef",
    {
        "MinimumPasswordLength": int,
        "RequireSymbols": bool,
        "RequireNumbers": bool,
        "RequireUppercaseCharacters": bool,
        "RequireLowercaseCharacters": bool,
        "AllowUsersToChangePassword": bool,
        "MaxPasswordAge": int,
        "PasswordReusePrevention": int,
        "HardExpiry": bool,
    },
    total=False,
)

UpdateAccountPasswordPolicyRequestServiceResourceTypeDef = TypedDict(
    "UpdateAccountPasswordPolicyRequestServiceResourceTypeDef",
    {
        "MinimumPasswordLength": int,
        "RequireSymbols": bool,
        "RequireNumbers": bool,
        "RequireUppercaseCharacters": bool,
        "RequireLowercaseCharacters": bool,
        "AllowUsersToChangePassword": bool,
        "MaxPasswordAge": int,
        "PasswordReusePrevention": int,
        "HardExpiry": bool,
    },
    total=False,
)

UpdateAccountPasswordPolicyRequestTypeDef = TypedDict(
    "UpdateAccountPasswordPolicyRequestTypeDef",
    {
        "MinimumPasswordLength": int,
        "RequireSymbols": bool,
        "RequireNumbers": bool,
        "RequireUppercaseCharacters": bool,
        "RequireLowercaseCharacters": bool,
        "AllowUsersToChangePassword": bool,
        "MaxPasswordAge": int,
        "PasswordReusePrevention": int,
        "HardExpiry": bool,
    },
    total=False,
)

UpdateAssumeRolePolicyRequestAssumeRolePolicyTypeDef = TypedDict(
    "UpdateAssumeRolePolicyRequestAssumeRolePolicyTypeDef",
    {
        "PolicyDocument": str,
    },
)

UpdateAssumeRolePolicyRequestTypeDef = TypedDict(
    "UpdateAssumeRolePolicyRequestTypeDef",
    {
        "RoleName": str,
        "PolicyDocument": str,
    },
)

UpdateGroupRequestGroupTypeDef = TypedDict(
    "UpdateGroupRequestGroupTypeDef",
    {
        "NewPath": str,
        "NewGroupName": str,
    },
    total=False,
)

_RequiredUpdateGroupRequestTypeDef = TypedDict(
    "_RequiredUpdateGroupRequestTypeDef",
    {
        "GroupName": str,
    },
)
_OptionalUpdateGroupRequestTypeDef = TypedDict(
    "_OptionalUpdateGroupRequestTypeDef",
    {
        "NewPath": str,
        "NewGroupName": str,
    },
    total=False,
)


class UpdateGroupRequestTypeDef(
    _RequiredUpdateGroupRequestTypeDef, _OptionalUpdateGroupRequestTypeDef
):
    pass


UpdateLoginProfileRequestLoginProfileTypeDef = TypedDict(
    "UpdateLoginProfileRequestLoginProfileTypeDef",
    {
        "Password": str,
        "PasswordResetRequired": bool,
    },
    total=False,
)

_RequiredUpdateLoginProfileRequestTypeDef = TypedDict(
    "_RequiredUpdateLoginProfileRequestTypeDef",
    {
        "UserName": str,
    },
)
_OptionalUpdateLoginProfileRequestTypeDef = TypedDict(
    "_OptionalUpdateLoginProfileRequestTypeDef",
    {
        "Password": str,
        "PasswordResetRequired": bool,
    },
    total=False,
)


class UpdateLoginProfileRequestTypeDef(
    _RequiredUpdateLoginProfileRequestTypeDef, _OptionalUpdateLoginProfileRequestTypeDef
):
    pass


UpdateOpenIDConnectProviderThumbprintRequestTypeDef = TypedDict(
    "UpdateOpenIDConnectProviderThumbprintRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "ThumbprintList": List[str],
    },
)

UpdateRoleDescriptionRequestTypeDef = TypedDict(
    "UpdateRoleDescriptionRequestTypeDef",
    {
        "RoleName": str,
        "Description": str,
    },
)

UpdateRoleDescriptionResponseResponseTypeDef = TypedDict(
    "UpdateRoleDescriptionResponseResponseTypeDef",
    {
        "Role": "RoleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRoleRequestTypeDef = TypedDict(
    "_RequiredUpdateRoleRequestTypeDef",
    {
        "RoleName": str,
    },
)
_OptionalUpdateRoleRequestTypeDef = TypedDict(
    "_OptionalUpdateRoleRequestTypeDef",
    {
        "Description": str,
        "MaxSessionDuration": int,
    },
    total=False,
)


class UpdateRoleRequestTypeDef(
    _RequiredUpdateRoleRequestTypeDef, _OptionalUpdateRoleRequestTypeDef
):
    pass


UpdateSAMLProviderRequestSamlProviderTypeDef = TypedDict(
    "UpdateSAMLProviderRequestSamlProviderTypeDef",
    {
        "SAMLMetadataDocument": str,
    },
)

UpdateSAMLProviderRequestTypeDef = TypedDict(
    "UpdateSAMLProviderRequestTypeDef",
    {
        "SAMLMetadataDocument": str,
        "SAMLProviderArn": str,
    },
)

UpdateSAMLProviderResponseResponseTypeDef = TypedDict(
    "UpdateSAMLProviderResponseResponseTypeDef",
    {
        "SAMLProviderArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSSHPublicKeyRequestTypeDef = TypedDict(
    "UpdateSSHPublicKeyRequestTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Status": statusTypeType,
    },
)

UpdateServerCertificateRequestServerCertificateTypeDef = TypedDict(
    "UpdateServerCertificateRequestServerCertificateTypeDef",
    {
        "NewPath": str,
        "NewServerCertificateName": str,
    },
    total=False,
)

_RequiredUpdateServerCertificateRequestTypeDef = TypedDict(
    "_RequiredUpdateServerCertificateRequestTypeDef",
    {
        "ServerCertificateName": str,
    },
)
_OptionalUpdateServerCertificateRequestTypeDef = TypedDict(
    "_OptionalUpdateServerCertificateRequestTypeDef",
    {
        "NewPath": str,
        "NewServerCertificateName": str,
    },
    total=False,
)


class UpdateServerCertificateRequestTypeDef(
    _RequiredUpdateServerCertificateRequestTypeDef, _OptionalUpdateServerCertificateRequestTypeDef
):
    pass


_RequiredUpdateServiceSpecificCredentialRequestTypeDef = TypedDict(
    "_RequiredUpdateServiceSpecificCredentialRequestTypeDef",
    {
        "ServiceSpecificCredentialId": str,
        "Status": statusTypeType,
    },
)
_OptionalUpdateServiceSpecificCredentialRequestTypeDef = TypedDict(
    "_OptionalUpdateServiceSpecificCredentialRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)


class UpdateServiceSpecificCredentialRequestTypeDef(
    _RequiredUpdateServiceSpecificCredentialRequestTypeDef,
    _OptionalUpdateServiceSpecificCredentialRequestTypeDef,
):
    pass


UpdateSigningCertificateRequestSigningCertificateTypeDef = TypedDict(
    "UpdateSigningCertificateRequestSigningCertificateTypeDef",
    {
        "Status": statusTypeType,
    },
)

_RequiredUpdateSigningCertificateRequestTypeDef = TypedDict(
    "_RequiredUpdateSigningCertificateRequestTypeDef",
    {
        "CertificateId": str,
        "Status": statusTypeType,
    },
)
_OptionalUpdateSigningCertificateRequestTypeDef = TypedDict(
    "_OptionalUpdateSigningCertificateRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)


class UpdateSigningCertificateRequestTypeDef(
    _RequiredUpdateSigningCertificateRequestTypeDef, _OptionalUpdateSigningCertificateRequestTypeDef
):
    pass


_RequiredUpdateUserRequestTypeDef = TypedDict(
    "_RequiredUpdateUserRequestTypeDef",
    {
        "UserName": str,
    },
)
_OptionalUpdateUserRequestTypeDef = TypedDict(
    "_OptionalUpdateUserRequestTypeDef",
    {
        "NewPath": str,
        "NewUserName": str,
    },
    total=False,
)


class UpdateUserRequestTypeDef(
    _RequiredUpdateUserRequestTypeDef, _OptionalUpdateUserRequestTypeDef
):
    pass


UpdateUserRequestUserTypeDef = TypedDict(
    "UpdateUserRequestUserTypeDef",
    {
        "NewPath": str,
        "NewUserName": str,
    },
    total=False,
)

UploadSSHPublicKeyRequestTypeDef = TypedDict(
    "UploadSSHPublicKeyRequestTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyBody": str,
    },
)

UploadSSHPublicKeyResponseResponseTypeDef = TypedDict(
    "UploadSSHPublicKeyResponseResponseTypeDef",
    {
        "SSHPublicKey": "SSHPublicKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUploadServerCertificateRequestServiceResourceTypeDef = TypedDict(
    "_RequiredUploadServerCertificateRequestServiceResourceTypeDef",
    {
        "ServerCertificateName": str,
        "CertificateBody": str,
        "PrivateKey": str,
    },
)
_OptionalUploadServerCertificateRequestServiceResourceTypeDef = TypedDict(
    "_OptionalUploadServerCertificateRequestServiceResourceTypeDef",
    {
        "Path": str,
        "CertificateChain": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class UploadServerCertificateRequestServiceResourceTypeDef(
    _RequiredUploadServerCertificateRequestServiceResourceTypeDef,
    _OptionalUploadServerCertificateRequestServiceResourceTypeDef,
):
    pass


_RequiredUploadServerCertificateRequestTypeDef = TypedDict(
    "_RequiredUploadServerCertificateRequestTypeDef",
    {
        "ServerCertificateName": str,
        "CertificateBody": str,
        "PrivateKey": str,
    },
)
_OptionalUploadServerCertificateRequestTypeDef = TypedDict(
    "_OptionalUploadServerCertificateRequestTypeDef",
    {
        "Path": str,
        "CertificateChain": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class UploadServerCertificateRequestTypeDef(
    _RequiredUploadServerCertificateRequestTypeDef, _OptionalUploadServerCertificateRequestTypeDef
):
    pass


UploadServerCertificateResponseResponseTypeDef = TypedDict(
    "UploadServerCertificateResponseResponseTypeDef",
    {
        "ServerCertificateMetadata": "ServerCertificateMetadataTypeDef",
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUploadSigningCertificateRequestServiceResourceTypeDef = TypedDict(
    "_RequiredUploadSigningCertificateRequestServiceResourceTypeDef",
    {
        "CertificateBody": str,
    },
)
_OptionalUploadSigningCertificateRequestServiceResourceTypeDef = TypedDict(
    "_OptionalUploadSigningCertificateRequestServiceResourceTypeDef",
    {
        "UserName": str,
    },
    total=False,
)


class UploadSigningCertificateRequestServiceResourceTypeDef(
    _RequiredUploadSigningCertificateRequestServiceResourceTypeDef,
    _OptionalUploadSigningCertificateRequestServiceResourceTypeDef,
):
    pass


_RequiredUploadSigningCertificateRequestTypeDef = TypedDict(
    "_RequiredUploadSigningCertificateRequestTypeDef",
    {
        "CertificateBody": str,
    },
)
_OptionalUploadSigningCertificateRequestTypeDef = TypedDict(
    "_OptionalUploadSigningCertificateRequestTypeDef",
    {
        "UserName": str,
    },
    total=False,
)


class UploadSigningCertificateRequestTypeDef(
    _RequiredUploadSigningCertificateRequestTypeDef, _OptionalUploadSigningCertificateRequestTypeDef
):
    pass


UploadSigningCertificateResponseResponseTypeDef = TypedDict(
    "UploadSigningCertificateResponseResponseTypeDef",
    {
        "Certificate": "SigningCertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserAccessKeyRequestTypeDef = TypedDict(
    "UserAccessKeyRequestTypeDef",
    {
        "id": str,
    },
)

UserDetailTypeDef = TypedDict(
    "UserDetailTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "UserPolicyList": List["PolicyDetailTypeDef"],
        "GroupList": List[str],
        "AttachedManagedPolicies": List["AttachedPolicyTypeDef"],
        "PermissionsBoundary": "AttachedPermissionsBoundaryTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

UserMfaDeviceRequestTypeDef = TypedDict(
    "UserMfaDeviceRequestTypeDef",
    {
        "serial_number": str,
    },
)

UserPolicyRequestTypeDef = TypedDict(
    "UserPolicyRequestTypeDef",
    {
        "name": str,
    },
)

UserSigningCertificateRequestTypeDef = TypedDict(
    "UserSigningCertificateRequestTypeDef",
    {
        "id": str,
    },
)

_RequiredUserTypeDef = TypedDict(
    "_RequiredUserTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
    },
)
_OptionalUserTypeDef = TypedDict(
    "_OptionalUserTypeDef",
    {
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": "AttachedPermissionsBoundaryTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class UserTypeDef(_RequiredUserTypeDef, _OptionalUserTypeDef):
    pass


_RequiredVirtualMFADeviceTypeDef = TypedDict(
    "_RequiredVirtualMFADeviceTypeDef",
    {
        "SerialNumber": str,
    },
)
_OptionalVirtualMFADeviceTypeDef = TypedDict(
    "_OptionalVirtualMFADeviceTypeDef",
    {
        "Base32StringSeed": bytes,
        "QRCodePNG": bytes,
        "User": "UserTypeDef",
        "EnableDate": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class VirtualMFADeviceTypeDef(_RequiredVirtualMFADeviceTypeDef, _OptionalVirtualMFADeviceTypeDef):
    pass


WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
