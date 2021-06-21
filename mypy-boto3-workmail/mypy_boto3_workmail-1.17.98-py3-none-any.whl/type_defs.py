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
from typing import List

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
    "BookingOptionsTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateMobileDeviceAccessRuleResponseTypeDef",
    "CreateOrganizationResponseTypeDef",
    "CreateResourceResponseTypeDef",
    "CreateUserResponseTypeDef",
    "DelegateTypeDef",
    "DeleteOrganizationResponseTypeDef",
    "DescribeGroupResponseTypeDef",
    "DescribeMailboxExportJobResponseTypeDef",
    "DescribeOrganizationResponseTypeDef",
    "DescribeResourceResponseTypeDef",
    "DescribeUserResponseTypeDef",
    "DomainTypeDef",
    "FolderConfigurationTypeDef",
    "GetAccessControlEffectResponseTypeDef",
    "GetDefaultRetentionPolicyResponseTypeDef",
    "GetMailboxDetailsResponseTypeDef",
    "GetMobileDeviceAccessEffectResponseTypeDef",
    "GroupTypeDef",
    "ListAccessControlRulesResponseTypeDef",
    "ListAliasesResponseTypeDef",
    "ListGroupMembersResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "ListMailboxExportJobsResponseTypeDef",
    "ListMailboxPermissionsResponseTypeDef",
    "ListMobileDeviceAccessRulesResponseTypeDef",
    "ListOrganizationsResponseTypeDef",
    "ListResourceDelegatesResponseTypeDef",
    "ListResourcesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsersResponseTypeDef",
    "MailboxExportJobTypeDef",
    "MemberTypeDef",
    "MobileDeviceAccessMatchedRuleTypeDef",
    "MobileDeviceAccessRuleTypeDef",
    "OrganizationSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "ResourceTypeDef",
    "StartMailboxExportJobResponseTypeDef",
    "TagTypeDef",
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

BookingOptionsTypeDef = TypedDict(
    "BookingOptionsTypeDef",
    {
        "AutoAcceptRequests": bool,
        "AutoDeclineRecurringRequests": bool,
        "AutoDeclineConflictingRequests": bool,
    },
    total=False,
)

CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "GroupId": str,
    },
    total=False,
)

CreateMobileDeviceAccessRuleResponseTypeDef = TypedDict(
    "CreateMobileDeviceAccessRuleResponseTypeDef",
    {
        "MobileDeviceAccessRuleId": str,
    },
    total=False,
)

CreateOrganizationResponseTypeDef = TypedDict(
    "CreateOrganizationResponseTypeDef",
    {
        "OrganizationId": str,
    },
    total=False,
)

CreateResourceResponseTypeDef = TypedDict(
    "CreateResourceResponseTypeDef",
    {
        "ResourceId": str,
    },
    total=False,
)

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "UserId": str,
    },
    total=False,
)

DelegateTypeDef = TypedDict(
    "DelegateTypeDef",
    {
        "Id": str,
        "Type": MemberTypeType,
    },
)

DeleteOrganizationResponseTypeDef = TypedDict(
    "DeleteOrganizationResponseTypeDef",
    {
        "OrganizationId": str,
        "State": str,
    },
    total=False,
)

DescribeGroupResponseTypeDef = TypedDict(
    "DescribeGroupResponseTypeDef",
    {
        "GroupId": str,
        "Name": str,
        "Email": str,
        "State": EntityStateType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

DescribeMailboxExportJobResponseTypeDef = TypedDict(
    "DescribeMailboxExportJobResponseTypeDef",
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
    },
    total=False,
)

DescribeOrganizationResponseTypeDef = TypedDict(
    "DescribeOrganizationResponseTypeDef",
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
    },
    total=False,
)

DescribeResourceResponseTypeDef = TypedDict(
    "DescribeResourceResponseTypeDef",
    {
        "ResourceId": str,
        "Email": str,
        "Name": str,
        "Type": ResourceTypeType,
        "BookingOptions": "BookingOptionsTypeDef",
        "State": EntityStateType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "UserId": str,
        "Name": str,
        "Email": str,
        "DisplayName": str,
        "State": EntityStateType,
        "UserRole": UserRoleType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
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


GetAccessControlEffectResponseTypeDef = TypedDict(
    "GetAccessControlEffectResponseTypeDef",
    {
        "Effect": AccessControlRuleEffectType,
        "MatchedRules": List[str],
    },
    total=False,
)

GetDefaultRetentionPolicyResponseTypeDef = TypedDict(
    "GetDefaultRetentionPolicyResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "FolderConfigurations": List["FolderConfigurationTypeDef"],
    },
    total=False,
)

GetMailboxDetailsResponseTypeDef = TypedDict(
    "GetMailboxDetailsResponseTypeDef",
    {
        "MailboxQuota": int,
        "MailboxSize": float,
    },
    total=False,
)

GetMobileDeviceAccessEffectResponseTypeDef = TypedDict(
    "GetMobileDeviceAccessEffectResponseTypeDef",
    {
        "Effect": MobileDeviceAccessRuleEffectType,
        "MatchedRules": List["MobileDeviceAccessMatchedRuleTypeDef"],
    },
    total=False,
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

ListAccessControlRulesResponseTypeDef = TypedDict(
    "ListAccessControlRulesResponseTypeDef",
    {
        "Rules": List["AccessControlRuleTypeDef"],
    },
    total=False,
)

ListAliasesResponseTypeDef = TypedDict(
    "ListAliasesResponseTypeDef",
    {
        "Aliases": List[str],
        "NextToken": str,
    },
    total=False,
)

ListGroupMembersResponseTypeDef = TypedDict(
    "ListGroupMembersResponseTypeDef",
    {
        "Members": List["MemberTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "Groups": List["GroupTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListMailboxExportJobsResponseTypeDef = TypedDict(
    "ListMailboxExportJobsResponseTypeDef",
    {
        "Jobs": List["MailboxExportJobTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListMailboxPermissionsResponseTypeDef = TypedDict(
    "ListMailboxPermissionsResponseTypeDef",
    {
        "Permissions": List["PermissionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListMobileDeviceAccessRulesResponseTypeDef = TypedDict(
    "ListMobileDeviceAccessRulesResponseTypeDef",
    {
        "Rules": List["MobileDeviceAccessRuleTypeDef"],
    },
    total=False,
)

ListOrganizationsResponseTypeDef = TypedDict(
    "ListOrganizationsResponseTypeDef",
    {
        "OrganizationSummaries": List["OrganizationSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListResourceDelegatesResponseTypeDef = TypedDict(
    "ListResourceDelegatesResponseTypeDef",
    {
        "Delegates": List["DelegateTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListResourcesResponseTypeDef = TypedDict(
    "ListResourcesResponseTypeDef",
    {
        "Resources": List["ResourceTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "Users": List["UserTypeDef"],
        "NextToken": str,
    },
    total=False,
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

StartMailboxExportJobResponseTypeDef = TypedDict(
    "StartMailboxExportJobResponseTypeDef",
    {
        "JobId": str,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

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
