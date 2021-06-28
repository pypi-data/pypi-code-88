"""
Type annotations for workmail service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/type_defs.html)

Usage::

    ```python
    from mypy_boto3_workmail.type_defs import AccessControlRuleTypeDef

    data: AccessControlRuleTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AccessControlRuleEffectType,
    EntityStateType,
    FolderNameType,
    MailboxExportJobStateType,
    MemberTypeType,
    MobileDeviceAccessRuleEffectType,
    PermissionTypeType,
    ResourceTypeType,
    RetentionActionType,
    UserRoleType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessControlRuleTypeDef",
    "AssociateDelegateToResourceRequestTypeDef",
    "AssociateMemberToGroupRequestTypeDef",
    "BookingOptionsTypeDef",
    "CancelMailboxExportJobRequestTypeDef",
    "CreateAliasRequestTypeDef",
    "CreateGroupRequestTypeDef",
    "CreateGroupResponseResponseTypeDef",
    "CreateMobileDeviceAccessRuleRequestTypeDef",
    "CreateMobileDeviceAccessRuleResponseResponseTypeDef",
    "CreateOrganizationRequestTypeDef",
    "CreateOrganizationResponseResponseTypeDef",
    "CreateResourceRequestTypeDef",
    "CreateResourceResponseResponseTypeDef",
    "CreateUserRequestTypeDef",
    "CreateUserResponseResponseTypeDef",
    "DelegateTypeDef",
    "DeleteAccessControlRuleRequestTypeDef",
    "DeleteAliasRequestTypeDef",
    "DeleteGroupRequestTypeDef",
    "DeleteMailboxPermissionsRequestTypeDef",
    "DeleteMobileDeviceAccessRuleRequestTypeDef",
    "DeleteOrganizationRequestTypeDef",
    "DeleteOrganizationResponseResponseTypeDef",
    "DeleteResourceRequestTypeDef",
    "DeleteRetentionPolicyRequestTypeDef",
    "DeleteUserRequestTypeDef",
    "DeregisterFromWorkMailRequestTypeDef",
    "DescribeGroupRequestTypeDef",
    "DescribeGroupResponseResponseTypeDef",
    "DescribeMailboxExportJobRequestTypeDef",
    "DescribeMailboxExportJobResponseResponseTypeDef",
    "DescribeOrganizationRequestTypeDef",
    "DescribeOrganizationResponseResponseTypeDef",
    "DescribeResourceRequestTypeDef",
    "DescribeResourceResponseResponseTypeDef",
    "DescribeUserRequestTypeDef",
    "DescribeUserResponseResponseTypeDef",
    "DisassociateDelegateFromResourceRequestTypeDef",
    "DisassociateMemberFromGroupRequestTypeDef",
    "DomainTypeDef",
    "FolderConfigurationTypeDef",
    "GetAccessControlEffectRequestTypeDef",
    "GetAccessControlEffectResponseResponseTypeDef",
    "GetDefaultRetentionPolicyRequestTypeDef",
    "GetDefaultRetentionPolicyResponseResponseTypeDef",
    "GetMailboxDetailsRequestTypeDef",
    "GetMailboxDetailsResponseResponseTypeDef",
    "GetMobileDeviceAccessEffectRequestTypeDef",
    "GetMobileDeviceAccessEffectResponseResponseTypeDef",
    "GroupTypeDef",
    "ListAccessControlRulesRequestTypeDef",
    "ListAccessControlRulesResponseResponseTypeDef",
    "ListAliasesRequestTypeDef",
    "ListAliasesResponseResponseTypeDef",
    "ListGroupMembersRequestTypeDef",
    "ListGroupMembersResponseResponseTypeDef",
    "ListGroupsRequestTypeDef",
    "ListGroupsResponseResponseTypeDef",
    "ListMailboxExportJobsRequestTypeDef",
    "ListMailboxExportJobsResponseResponseTypeDef",
    "ListMailboxPermissionsRequestTypeDef",
    "ListMailboxPermissionsResponseResponseTypeDef",
    "ListMobileDeviceAccessRulesRequestTypeDef",
    "ListMobileDeviceAccessRulesResponseResponseTypeDef",
    "ListOrganizationsRequestTypeDef",
    "ListOrganizationsResponseResponseTypeDef",
    "ListResourceDelegatesRequestTypeDef",
    "ListResourceDelegatesResponseResponseTypeDef",
    "ListResourcesRequestTypeDef",
    "ListResourcesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListUsersRequestTypeDef",
    "ListUsersResponseResponseTypeDef",
    "MailboxExportJobTypeDef",
    "MemberTypeDef",
    "MobileDeviceAccessMatchedRuleTypeDef",
    "MobileDeviceAccessRuleTypeDef",
    "OrganizationSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "PutAccessControlRuleRequestTypeDef",
    "PutMailboxPermissionsRequestTypeDef",
    "PutRetentionPolicyRequestTypeDef",
    "RegisterToWorkMailRequestTypeDef",
    "ResetPasswordRequestTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "StartMailboxExportJobRequestTypeDef",
    "StartMailboxExportJobResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateMailboxQuotaRequestTypeDef",
    "UpdateMobileDeviceAccessRuleRequestTypeDef",
    "UpdatePrimaryEmailAddressRequestTypeDef",
    "UpdateResourceRequestTypeDef",
    "UserTypeDef",
)

AccessControlRuleTypeDef = TypedDict(
    "AccessControlRuleTypeDef",
    {
        "Name": str,
        "Effect": AccessControlRuleEffectType,
        "Description": str,
        "IpRanges": List[str],
        "NotIpRanges": List[str],
        "Actions": List[str],
        "NotActions": List[str],
        "UserIds": List[str],
        "NotUserIds": List[str],
        "DateCreated": datetime,
        "DateModified": datetime,
    },
    total=False,
)

AssociateDelegateToResourceRequestTypeDef = TypedDict(
    "AssociateDelegateToResourceRequestTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
        "EntityId": str,
    },
)

AssociateMemberToGroupRequestTypeDef = TypedDict(
    "AssociateMemberToGroupRequestTypeDef",
    {
        "OrganizationId": str,
        "GroupId": str,
        "MemberId": str,
    },
)

BookingOptionsTypeDef = TypedDict(
    "BookingOptionsTypeDef",
    {
        "AutoAcceptRequests": bool,
        "AutoDeclineRecurringRequests": bool,
        "AutoDeclineConflictingRequests": bool,
    },
    total=False,
)

CancelMailboxExportJobRequestTypeDef = TypedDict(
    "CancelMailboxExportJobRequestTypeDef",
    {
        "ClientToken": str,
        "JobId": str,
        "OrganizationId": str,
    },
)

CreateAliasRequestTypeDef = TypedDict(
    "CreateAliasRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "Alias": str,
    },
)

CreateGroupRequestTypeDef = TypedDict(
    "CreateGroupRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
    },
)

CreateGroupResponseResponseTypeDef = TypedDict(
    "CreateGroupResponseResponseTypeDef",
    {
        "GroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMobileDeviceAccessRuleRequestTypeDef = TypedDict(
    "_RequiredCreateMobileDeviceAccessRuleRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
        "Effect": MobileDeviceAccessRuleEffectType,
    },
)
_OptionalCreateMobileDeviceAccessRuleRequestTypeDef = TypedDict(
    "_OptionalCreateMobileDeviceAccessRuleRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "DeviceTypes": List[str],
        "NotDeviceTypes": List[str],
        "DeviceModels": List[str],
        "NotDeviceModels": List[str],
        "DeviceOperatingSystems": List[str],
        "NotDeviceOperatingSystems": List[str],
        "DeviceUserAgents": List[str],
        "NotDeviceUserAgents": List[str],
    },
    total=False,
)


class CreateMobileDeviceAccessRuleRequestTypeDef(
    _RequiredCreateMobileDeviceAccessRuleRequestTypeDef,
    _OptionalCreateMobileDeviceAccessRuleRequestTypeDef,
):
    pass


CreateMobileDeviceAccessRuleResponseResponseTypeDef = TypedDict(
    "CreateMobileDeviceAccessRuleResponseResponseTypeDef",
    {
        "MobileDeviceAccessRuleId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateOrganizationRequestTypeDef = TypedDict(
    "_RequiredCreateOrganizationRequestTypeDef",
    {
        "Alias": str,
    },
)
_OptionalCreateOrganizationRequestTypeDef = TypedDict(
    "_OptionalCreateOrganizationRequestTypeDef",
    {
        "DirectoryId": str,
        "ClientToken": str,
        "Domains": List["DomainTypeDef"],
        "KmsKeyArn": str,
        "EnableInteroperability": bool,
    },
    total=False,
)


class CreateOrganizationRequestTypeDef(
    _RequiredCreateOrganizationRequestTypeDef, _OptionalCreateOrganizationRequestTypeDef
):
    pass


CreateOrganizationResponseResponseTypeDef = TypedDict(
    "CreateOrganizationResponseResponseTypeDef",
    {
        "OrganizationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResourceRequestTypeDef = TypedDict(
    "CreateResourceRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
        "Type": ResourceTypeType,
    },
)

CreateResourceResponseResponseTypeDef = TypedDict(
    "CreateResourceResponseResponseTypeDef",
    {
        "ResourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserRequestTypeDef = TypedDict(
    "CreateUserRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
        "DisplayName": str,
        "Password": str,
    },
)

CreateUserResponseResponseTypeDef = TypedDict(
    "CreateUserResponseResponseTypeDef",
    {
        "UserId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DelegateTypeDef = TypedDict(
    "DelegateTypeDef",
    {
        "Id": str,
        "Type": MemberTypeType,
    },
)

DeleteAccessControlRuleRequestTypeDef = TypedDict(
    "DeleteAccessControlRuleRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
    },
)

DeleteAliasRequestTypeDef = TypedDict(
    "DeleteAliasRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "Alias": str,
    },
)

DeleteGroupRequestTypeDef = TypedDict(
    "DeleteGroupRequestTypeDef",
    {
        "OrganizationId": str,
        "GroupId": str,
    },
)

DeleteMailboxPermissionsRequestTypeDef = TypedDict(
    "DeleteMailboxPermissionsRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "GranteeId": str,
    },
)

DeleteMobileDeviceAccessRuleRequestTypeDef = TypedDict(
    "DeleteMobileDeviceAccessRuleRequestTypeDef",
    {
        "OrganizationId": str,
        "MobileDeviceAccessRuleId": str,
    },
)

_RequiredDeleteOrganizationRequestTypeDef = TypedDict(
    "_RequiredDeleteOrganizationRequestTypeDef",
    {
        "OrganizationId": str,
        "DeleteDirectory": bool,
    },
)
_OptionalDeleteOrganizationRequestTypeDef = TypedDict(
    "_OptionalDeleteOrganizationRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class DeleteOrganizationRequestTypeDef(
    _RequiredDeleteOrganizationRequestTypeDef, _OptionalDeleteOrganizationRequestTypeDef
):
    pass


DeleteOrganizationResponseResponseTypeDef = TypedDict(
    "DeleteOrganizationResponseResponseTypeDef",
    {
        "OrganizationId": str,
        "State": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourceRequestTypeDef = TypedDict(
    "DeleteResourceRequestTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
    },
)

DeleteRetentionPolicyRequestTypeDef = TypedDict(
    "DeleteRetentionPolicyRequestTypeDef",
    {
        "OrganizationId": str,
        "Id": str,
    },
)

DeleteUserRequestTypeDef = TypedDict(
    "DeleteUserRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
    },
)

DeregisterFromWorkMailRequestTypeDef = TypedDict(
    "DeregisterFromWorkMailRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
    },
)

DescribeGroupRequestTypeDef = TypedDict(
    "DescribeGroupRequestTypeDef",
    {
        "OrganizationId": str,
        "GroupId": str,
    },
)

DescribeGroupResponseResponseTypeDef = TypedDict(
    "DescribeGroupResponseResponseTypeDef",
    {
        "GroupId": str,
        "Name": str,
        "Email": str,
        "State": EntityStateType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMailboxExportJobRequestTypeDef = TypedDict(
    "DescribeMailboxExportJobRequestTypeDef",
    {
        "JobId": str,
        "OrganizationId": str,
    },
)

DescribeMailboxExportJobResponseResponseTypeDef = TypedDict(
    "DescribeMailboxExportJobResponseResponseTypeDef",
    {
        "EntityId": str,
        "Description": str,
        "RoleArn": str,
        "KmsKeyArn": str,
        "S3BucketName": str,
        "S3Prefix": str,
        "S3Path": str,
        "EstimatedProgress": int,
        "State": MailboxExportJobStateType,
        "ErrorInfo": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationRequestTypeDef = TypedDict(
    "DescribeOrganizationRequestTypeDef",
    {
        "OrganizationId": str,
    },
)

DescribeOrganizationResponseResponseTypeDef = TypedDict(
    "DescribeOrganizationResponseResponseTypeDef",
    {
        "OrganizationId": str,
        "Alias": str,
        "State": str,
        "DirectoryId": str,
        "DirectoryType": str,
        "DefaultMailDomain": str,
        "CompletedDate": datetime,
        "ErrorMessage": str,
        "ARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourceRequestTypeDef = TypedDict(
    "DescribeResourceRequestTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
    },
)

DescribeResourceResponseResponseTypeDef = TypedDict(
    "DescribeResourceResponseResponseTypeDef",
    {
        "ResourceId": str,
        "Email": str,
        "Name": str,
        "Type": ResourceTypeType,
        "BookingOptions": "BookingOptionsTypeDef",
        "State": EntityStateType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestTypeDef = TypedDict(
    "DescribeUserRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
    },
)

DescribeUserResponseResponseTypeDef = TypedDict(
    "DescribeUserResponseResponseTypeDef",
    {
        "UserId": str,
        "Name": str,
        "Email": str,
        "DisplayName": str,
        "State": EntityStateType,
        "UserRole": UserRoleType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateDelegateFromResourceRequestTypeDef = TypedDict(
    "DisassociateDelegateFromResourceRequestTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
        "EntityId": str,
    },
)

DisassociateMemberFromGroupRequestTypeDef = TypedDict(
    "DisassociateMemberFromGroupRequestTypeDef",
    {
        "OrganizationId": str,
        "GroupId": str,
        "MemberId": str,
    },
)

DomainTypeDef = TypedDict(
    "DomainTypeDef",
    {
        "DomainName": str,
        "HostedZoneId": str,
    },
    total=False,
)

_RequiredFolderConfigurationTypeDef = TypedDict(
    "_RequiredFolderConfigurationTypeDef",
    {
        "Name": FolderNameType,
        "Action": RetentionActionType,
    },
)
_OptionalFolderConfigurationTypeDef = TypedDict(
    "_OptionalFolderConfigurationTypeDef",
    {
        "Period": int,
    },
    total=False,
)


class FolderConfigurationTypeDef(
    _RequiredFolderConfigurationTypeDef, _OptionalFolderConfigurationTypeDef
):
    pass


GetAccessControlEffectRequestTypeDef = TypedDict(
    "GetAccessControlEffectRequestTypeDef",
    {
        "OrganizationId": str,
        "IpAddress": str,
        "Action": str,
        "UserId": str,
    },
)

GetAccessControlEffectResponseResponseTypeDef = TypedDict(
    "GetAccessControlEffectResponseResponseTypeDef",
    {
        "Effect": AccessControlRuleEffectType,
        "MatchedRules": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDefaultRetentionPolicyRequestTypeDef = TypedDict(
    "GetDefaultRetentionPolicyRequestTypeDef",
    {
        "OrganizationId": str,
    },
)

GetDefaultRetentionPolicyResponseResponseTypeDef = TypedDict(
    "GetDefaultRetentionPolicyResponseResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "FolderConfigurations": List["FolderConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMailboxDetailsRequestTypeDef = TypedDict(
    "GetMailboxDetailsRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
    },
)

GetMailboxDetailsResponseResponseTypeDef = TypedDict(
    "GetMailboxDetailsResponseResponseTypeDef",
    {
        "MailboxQuota": int,
        "MailboxSize": float,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMobileDeviceAccessEffectRequestTypeDef = TypedDict(
    "_RequiredGetMobileDeviceAccessEffectRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
_OptionalGetMobileDeviceAccessEffectRequestTypeDef = TypedDict(
    "_OptionalGetMobileDeviceAccessEffectRequestTypeDef",
    {
        "DeviceType": str,
        "DeviceModel": str,
        "DeviceOperatingSystem": str,
        "DeviceUserAgent": str,
    },
    total=False,
)


class GetMobileDeviceAccessEffectRequestTypeDef(
    _RequiredGetMobileDeviceAccessEffectRequestTypeDef,
    _OptionalGetMobileDeviceAccessEffectRequestTypeDef,
):
    pass


GetMobileDeviceAccessEffectResponseResponseTypeDef = TypedDict(
    "GetMobileDeviceAccessEffectResponseResponseTypeDef",
    {
        "Effect": MobileDeviceAccessRuleEffectType,
        "MatchedRules": List["MobileDeviceAccessMatchedRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "State": EntityStateType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

ListAccessControlRulesRequestTypeDef = TypedDict(
    "ListAccessControlRulesRequestTypeDef",
    {
        "OrganizationId": str,
    },
)

ListAccessControlRulesResponseResponseTypeDef = TypedDict(
    "ListAccessControlRulesResponseResponseTypeDef",
    {
        "Rules": List["AccessControlRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAliasesRequestTypeDef = TypedDict(
    "_RequiredListAliasesRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
    },
)
_OptionalListAliasesRequestTypeDef = TypedDict(
    "_OptionalListAliasesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListAliasesRequestTypeDef(
    _RequiredListAliasesRequestTypeDef, _OptionalListAliasesRequestTypeDef
):
    pass


ListAliasesResponseResponseTypeDef = TypedDict(
    "ListAliasesResponseResponseTypeDef",
    {
        "Aliases": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupMembersRequestTypeDef = TypedDict(
    "_RequiredListGroupMembersRequestTypeDef",
    {
        "OrganizationId": str,
        "GroupId": str,
    },
)
_OptionalListGroupMembersRequestTypeDef = TypedDict(
    "_OptionalListGroupMembersRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListGroupMembersRequestTypeDef(
    _RequiredListGroupMembersRequestTypeDef, _OptionalListGroupMembersRequestTypeDef
):
    pass


ListGroupMembersResponseResponseTypeDef = TypedDict(
    "ListGroupMembersResponseResponseTypeDef",
    {
        "Members": List["MemberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupsRequestTypeDef = TypedDict(
    "_RequiredListGroupsRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
_OptionalListGroupsRequestTypeDef = TypedDict(
    "_OptionalListGroupsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
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
        "Groups": List["GroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMailboxExportJobsRequestTypeDef = TypedDict(
    "_RequiredListMailboxExportJobsRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
_OptionalListMailboxExportJobsRequestTypeDef = TypedDict(
    "_OptionalListMailboxExportJobsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListMailboxExportJobsRequestTypeDef(
    _RequiredListMailboxExportJobsRequestTypeDef, _OptionalListMailboxExportJobsRequestTypeDef
):
    pass


ListMailboxExportJobsResponseResponseTypeDef = TypedDict(
    "ListMailboxExportJobsResponseResponseTypeDef",
    {
        "Jobs": List["MailboxExportJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMailboxPermissionsRequestTypeDef = TypedDict(
    "_RequiredListMailboxPermissionsRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
    },
)
_OptionalListMailboxPermissionsRequestTypeDef = TypedDict(
    "_OptionalListMailboxPermissionsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListMailboxPermissionsRequestTypeDef(
    _RequiredListMailboxPermissionsRequestTypeDef, _OptionalListMailboxPermissionsRequestTypeDef
):
    pass


ListMailboxPermissionsResponseResponseTypeDef = TypedDict(
    "ListMailboxPermissionsResponseResponseTypeDef",
    {
        "Permissions": List["PermissionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMobileDeviceAccessRulesRequestTypeDef = TypedDict(
    "ListMobileDeviceAccessRulesRequestTypeDef",
    {
        "OrganizationId": str,
    },
)

ListMobileDeviceAccessRulesResponseResponseTypeDef = TypedDict(
    "ListMobileDeviceAccessRulesResponseResponseTypeDef",
    {
        "Rules": List["MobileDeviceAccessRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOrganizationsRequestTypeDef = TypedDict(
    "ListOrganizationsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListOrganizationsResponseResponseTypeDef = TypedDict(
    "ListOrganizationsResponseResponseTypeDef",
    {
        "OrganizationSummaries": List["OrganizationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourceDelegatesRequestTypeDef = TypedDict(
    "_RequiredListResourceDelegatesRequestTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
    },
)
_OptionalListResourceDelegatesRequestTypeDef = TypedDict(
    "_OptionalListResourceDelegatesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListResourceDelegatesRequestTypeDef(
    _RequiredListResourceDelegatesRequestTypeDef, _OptionalListResourceDelegatesRequestTypeDef
):
    pass


ListResourceDelegatesResponseResponseTypeDef = TypedDict(
    "ListResourceDelegatesResponseResponseTypeDef",
    {
        "Delegates": List["DelegateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourcesRequestTypeDef = TypedDict(
    "_RequiredListResourcesRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
_OptionalListResourcesRequestTypeDef = TypedDict(
    "_OptionalListResourcesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListResourcesRequestTypeDef(
    _RequiredListResourcesRequestTypeDef, _OptionalListResourcesRequestTypeDef
):
    pass


ListResourcesResponseResponseTypeDef = TypedDict(
    "ListResourcesResponseResponseTypeDef",
    {
        "Resources": List["ResourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
_OptionalListUsersRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListUsersRequestTypeDef(_RequiredListUsersRequestTypeDef, _OptionalListUsersRequestTypeDef):
    pass


ListUsersResponseResponseTypeDef = TypedDict(
    "ListUsersResponseResponseTypeDef",
    {
        "Users": List["UserTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MailboxExportJobTypeDef = TypedDict(
    "MailboxExportJobTypeDef",
    {
        "JobId": str,
        "EntityId": str,
        "Description": str,
        "S3BucketName": str,
        "S3Path": str,
        "EstimatedProgress": int,
        "State": MailboxExportJobStateType,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "Id": str,
        "Name": str,
        "Type": MemberTypeType,
        "State": EntityStateType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

MobileDeviceAccessMatchedRuleTypeDef = TypedDict(
    "MobileDeviceAccessMatchedRuleTypeDef",
    {
        "MobileDeviceAccessRuleId": str,
        "Name": str,
    },
    total=False,
)

MobileDeviceAccessRuleTypeDef = TypedDict(
    "MobileDeviceAccessRuleTypeDef",
    {
        "MobileDeviceAccessRuleId": str,
        "Name": str,
        "Description": str,
        "Effect": MobileDeviceAccessRuleEffectType,
        "DeviceTypes": List[str],
        "NotDeviceTypes": List[str],
        "DeviceModels": List[str],
        "NotDeviceModels": List[str],
        "DeviceOperatingSystems": List[str],
        "NotDeviceOperatingSystems": List[str],
        "DeviceUserAgents": List[str],
        "NotDeviceUserAgents": List[str],
        "DateCreated": datetime,
        "DateModified": datetime,
    },
    total=False,
)

OrganizationSummaryTypeDef = TypedDict(
    "OrganizationSummaryTypeDef",
    {
        "OrganizationId": str,
        "Alias": str,
        "DefaultMailDomain": str,
        "ErrorMessage": str,
        "State": str,
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

PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "GranteeId": str,
        "GranteeType": MemberTypeType,
        "PermissionValues": List[PermissionTypeType],
    },
)

_RequiredPutAccessControlRuleRequestTypeDef = TypedDict(
    "_RequiredPutAccessControlRuleRequestTypeDef",
    {
        "Name": str,
        "Effect": AccessControlRuleEffectType,
        "Description": str,
        "OrganizationId": str,
    },
)
_OptionalPutAccessControlRuleRequestTypeDef = TypedDict(
    "_OptionalPutAccessControlRuleRequestTypeDef",
    {
        "IpRanges": List[str],
        "NotIpRanges": List[str],
        "Actions": List[str],
        "NotActions": List[str],
        "UserIds": List[str],
        "NotUserIds": List[str],
    },
    total=False,
)


class PutAccessControlRuleRequestTypeDef(
    _RequiredPutAccessControlRuleRequestTypeDef, _OptionalPutAccessControlRuleRequestTypeDef
):
    pass


PutMailboxPermissionsRequestTypeDef = TypedDict(
    "PutMailboxPermissionsRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "GranteeId": str,
        "PermissionValues": List[PermissionTypeType],
    },
)

_RequiredPutRetentionPolicyRequestTypeDef = TypedDict(
    "_RequiredPutRetentionPolicyRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
        "FolderConfigurations": List["FolderConfigurationTypeDef"],
    },
)
_OptionalPutRetentionPolicyRequestTypeDef = TypedDict(
    "_OptionalPutRetentionPolicyRequestTypeDef",
    {
        "Id": str,
        "Description": str,
    },
    total=False,
)


class PutRetentionPolicyRequestTypeDef(
    _RequiredPutRetentionPolicyRequestTypeDef, _OptionalPutRetentionPolicyRequestTypeDef
):
    pass


RegisterToWorkMailRequestTypeDef = TypedDict(
    "RegisterToWorkMailRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "Email": str,
    },
)

ResetPasswordRequestTypeDef = TypedDict(
    "ResetPasswordRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
        "Password": str,
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "Type": ResourceTypeType,
        "State": EntityStateType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
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

_RequiredStartMailboxExportJobRequestTypeDef = TypedDict(
    "_RequiredStartMailboxExportJobRequestTypeDef",
    {
        "ClientToken": str,
        "OrganizationId": str,
        "EntityId": str,
        "RoleArn": str,
        "KmsKeyArn": str,
        "S3BucketName": str,
        "S3Prefix": str,
    },
)
_OptionalStartMailboxExportJobRequestTypeDef = TypedDict(
    "_OptionalStartMailboxExportJobRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class StartMailboxExportJobRequestTypeDef(
    _RequiredStartMailboxExportJobRequestTypeDef, _OptionalStartMailboxExportJobRequestTypeDef
):
    pass


StartMailboxExportJobResponseResponseTypeDef = TypedDict(
    "StartMailboxExportJobResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceARN": str,
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

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

UpdateMailboxQuotaRequestTypeDef = TypedDict(
    "UpdateMailboxQuotaRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
        "MailboxQuota": int,
    },
)

_RequiredUpdateMobileDeviceAccessRuleRequestTypeDef = TypedDict(
    "_RequiredUpdateMobileDeviceAccessRuleRequestTypeDef",
    {
        "OrganizationId": str,
        "MobileDeviceAccessRuleId": str,
        "Name": str,
        "Effect": MobileDeviceAccessRuleEffectType,
    },
)
_OptionalUpdateMobileDeviceAccessRuleRequestTypeDef = TypedDict(
    "_OptionalUpdateMobileDeviceAccessRuleRequestTypeDef",
    {
        "Description": str,
        "DeviceTypes": List[str],
        "NotDeviceTypes": List[str],
        "DeviceModels": List[str],
        "NotDeviceModels": List[str],
        "DeviceOperatingSystems": List[str],
        "NotDeviceOperatingSystems": List[str],
        "DeviceUserAgents": List[str],
        "NotDeviceUserAgents": List[str],
    },
    total=False,
)


class UpdateMobileDeviceAccessRuleRequestTypeDef(
    _RequiredUpdateMobileDeviceAccessRuleRequestTypeDef,
    _OptionalUpdateMobileDeviceAccessRuleRequestTypeDef,
):
    pass


UpdatePrimaryEmailAddressRequestTypeDef = TypedDict(
    "UpdatePrimaryEmailAddressRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "Email": str,
    },
)

_RequiredUpdateResourceRequestTypeDef = TypedDict(
    "_RequiredUpdateResourceRequestTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
    },
)
_OptionalUpdateResourceRequestTypeDef = TypedDict(
    "_OptionalUpdateResourceRequestTypeDef",
    {
        "Name": str,
        "BookingOptions": "BookingOptionsTypeDef",
    },
    total=False,
)


class UpdateResourceRequestTypeDef(
    _RequiredUpdateResourceRequestTypeDef, _OptionalUpdateResourceRequestTypeDef
):
    pass


UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "DisplayName": str,
        "State": EntityStateType,
        "UserRole": UserRoleType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)
