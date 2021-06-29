"""
Type annotations for fms service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/type_defs.html)

Usage::

    ```python
    from mypy_boto3_fms.type_defs import AppTypeDef

    data: AppTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AccountRoleStatusType,
    CustomerPolicyScopeIdTypeType,
    DependentServiceNameType,
    PolicyComplianceStatusTypeType,
    RemediationActionTypeType,
    SecurityServiceTypeType,
    ViolationReasonType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AppTypeDef",
    "AppsListDataSummaryTypeDef",
    "AppsListDataTypeDef",
    "AssociateAdminAccountRequestRequestTypeDef",
    "AwsEc2InstanceViolationTypeDef",
    "AwsEc2NetworkInterfaceViolationTypeDef",
    "AwsVPCSecurityGroupViolationTypeDef",
    "ComplianceViolatorTypeDef",
    "DeleteAppsListRequestRequestTypeDef",
    "DeletePolicyRequestRequestTypeDef",
    "DeleteProtocolsListRequestRequestTypeDef",
    "DnsDuplicateRuleGroupViolationTypeDef",
    "DnsRuleGroupLimitExceededViolationTypeDef",
    "DnsRuleGroupPriorityConflictViolationTypeDef",
    "EvaluationResultTypeDef",
    "GetAdminAccountResponseTypeDef",
    "GetAppsListRequestRequestTypeDef",
    "GetAppsListResponseTypeDef",
    "GetComplianceDetailRequestRequestTypeDef",
    "GetComplianceDetailResponseTypeDef",
    "GetNotificationChannelResponseTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "GetPolicyResponseTypeDef",
    "GetProtectionStatusRequestRequestTypeDef",
    "GetProtectionStatusResponseTypeDef",
    "GetProtocolsListRequestRequestTypeDef",
    "GetProtocolsListResponseTypeDef",
    "GetViolationDetailsRequestRequestTypeDef",
    "GetViolationDetailsResponseTypeDef",
    "ListAppsListsRequestRequestTypeDef",
    "ListAppsListsResponseTypeDef",
    "ListComplianceStatusRequestRequestTypeDef",
    "ListComplianceStatusResponseTypeDef",
    "ListMemberAccountsRequestRequestTypeDef",
    "ListMemberAccountsResponseTypeDef",
    "ListPoliciesRequestRequestTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListProtocolsListsRequestRequestTypeDef",
    "ListProtocolsListsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NetworkFirewallMissingExpectedRTViolationTypeDef",
    "NetworkFirewallMissingFirewallViolationTypeDef",
    "NetworkFirewallMissingSubnetViolationTypeDef",
    "NetworkFirewallPolicyDescriptionTypeDef",
    "NetworkFirewallPolicyModifiedViolationTypeDef",
    "PaginatorConfigTypeDef",
    "PartialMatchTypeDef",
    "PolicyComplianceDetailTypeDef",
    "PolicyComplianceStatusTypeDef",
    "PolicySummaryTypeDef",
    "PolicyTypeDef",
    "ProtocolsListDataSummaryTypeDef",
    "ProtocolsListDataTypeDef",
    "PutAppsListRequestRequestTypeDef",
    "PutAppsListResponseTypeDef",
    "PutNotificationChannelRequestRequestTypeDef",
    "PutPolicyRequestRequestTypeDef",
    "PutPolicyResponseTypeDef",
    "PutProtocolsListRequestRequestTypeDef",
    "PutProtocolsListResponseTypeDef",
    "ResourceTagTypeDef",
    "ResourceViolationTypeDef",
    "ResponseMetadataTypeDef",
    "SecurityGroupRemediationActionTypeDef",
    "SecurityGroupRuleDescriptionTypeDef",
    "SecurityServicePolicyDataTypeDef",
    "StatefulRuleGroupTypeDef",
    "StatelessRuleGroupTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ViolationDetailTypeDef",
)

AppTypeDef = TypedDict(
    "AppTypeDef",
    {
        "AppName": str,
        "Protocol": str,
        "Port": int,
    },
)

AppsListDataSummaryTypeDef = TypedDict(
    "AppsListDataSummaryTypeDef",
    {
        "ListArn": str,
        "ListId": str,
        "ListName": str,
        "AppsList": List["AppTypeDef"],
    },
    total=False,
)

_RequiredAppsListDataTypeDef = TypedDict(
    "_RequiredAppsListDataTypeDef",
    {
        "ListName": str,
        "AppsList": List["AppTypeDef"],
    },
)
_OptionalAppsListDataTypeDef = TypedDict(
    "_OptionalAppsListDataTypeDef",
    {
        "ListId": str,
        "ListUpdateToken": str,
        "CreateTime": datetime,
        "LastUpdateTime": datetime,
        "PreviousAppsList": Dict[str, List["AppTypeDef"]],
    },
    total=False,
)


class AppsListDataTypeDef(_RequiredAppsListDataTypeDef, _OptionalAppsListDataTypeDef):
    pass


AssociateAdminAccountRequestRequestTypeDef = TypedDict(
    "AssociateAdminAccountRequestRequestTypeDef",
    {
        "AdminAccount": str,
    },
)

AwsEc2InstanceViolationTypeDef = TypedDict(
    "AwsEc2InstanceViolationTypeDef",
    {
        "ViolationTarget": str,
        "AwsEc2NetworkInterfaceViolations": List["AwsEc2NetworkInterfaceViolationTypeDef"],
    },
    total=False,
)

AwsEc2NetworkInterfaceViolationTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceViolationTypeDef",
    {
        "ViolationTarget": str,
        "ViolatingSecurityGroups": List[str],
    },
    total=False,
)

AwsVPCSecurityGroupViolationTypeDef = TypedDict(
    "AwsVPCSecurityGroupViolationTypeDef",
    {
        "ViolationTarget": str,
        "ViolationTargetDescription": str,
        "PartialMatches": List["PartialMatchTypeDef"],
        "PossibleSecurityGroupRemediationActions": List["SecurityGroupRemediationActionTypeDef"],
    },
    total=False,
)

ComplianceViolatorTypeDef = TypedDict(
    "ComplianceViolatorTypeDef",
    {
        "ResourceId": str,
        "ViolationReason": ViolationReasonType,
        "ResourceType": str,
    },
    total=False,
)

DeleteAppsListRequestRequestTypeDef = TypedDict(
    "DeleteAppsListRequestRequestTypeDef",
    {
        "ListId": str,
    },
)

_RequiredDeletePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)
_OptionalDeletePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePolicyRequestRequestTypeDef",
    {
        "DeleteAllPolicyResources": bool,
    },
    total=False,
)


class DeletePolicyRequestRequestTypeDef(
    _RequiredDeletePolicyRequestRequestTypeDef, _OptionalDeletePolicyRequestRequestTypeDef
):
    pass


DeleteProtocolsListRequestRequestTypeDef = TypedDict(
    "DeleteProtocolsListRequestRequestTypeDef",
    {
        "ListId": str,
    },
)

DnsDuplicateRuleGroupViolationTypeDef = TypedDict(
    "DnsDuplicateRuleGroupViolationTypeDef",
    {
        "ViolationTarget": str,
        "ViolationTargetDescription": str,
    },
    total=False,
)

DnsRuleGroupLimitExceededViolationTypeDef = TypedDict(
    "DnsRuleGroupLimitExceededViolationTypeDef",
    {
        "ViolationTarget": str,
        "ViolationTargetDescription": str,
        "NumberOfRuleGroupsAlreadyAssociated": int,
    },
    total=False,
)

DnsRuleGroupPriorityConflictViolationTypeDef = TypedDict(
    "DnsRuleGroupPriorityConflictViolationTypeDef",
    {
        "ViolationTarget": str,
        "ViolationTargetDescription": str,
        "ConflictingPriority": int,
        "ConflictingPolicyId": str,
        "UnavailablePriorities": List[int],
    },
    total=False,
)

EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "ComplianceStatus": PolicyComplianceStatusTypeType,
        "ViolatorCount": int,
        "EvaluationLimitExceeded": bool,
    },
    total=False,
)

GetAdminAccountResponseTypeDef = TypedDict(
    "GetAdminAccountResponseTypeDef",
    {
        "AdminAccount": str,
        "RoleStatus": AccountRoleStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetAppsListRequestRequestTypeDef = TypedDict(
    "_RequiredGetAppsListRequestRequestTypeDef",
    {
        "ListId": str,
    },
)
_OptionalGetAppsListRequestRequestTypeDef = TypedDict(
    "_OptionalGetAppsListRequestRequestTypeDef",
    {
        "DefaultList": bool,
    },
    total=False,
)


class GetAppsListRequestRequestTypeDef(
    _RequiredGetAppsListRequestRequestTypeDef, _OptionalGetAppsListRequestRequestTypeDef
):
    pass


GetAppsListResponseTypeDef = TypedDict(
    "GetAppsListResponseTypeDef",
    {
        "AppsList": "AppsListDataTypeDef",
        "AppsListArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComplianceDetailRequestRequestTypeDef = TypedDict(
    "GetComplianceDetailRequestRequestTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
    },
)

GetComplianceDetailResponseTypeDef = TypedDict(
    "GetComplianceDetailResponseTypeDef",
    {
        "PolicyComplianceDetail": "PolicyComplianceDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNotificationChannelResponseTypeDef = TypedDict(
    "GetNotificationChannelResponseTypeDef",
    {
        "SnsTopicArn": str,
        "SnsRoleName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyRequestRequestTypeDef = TypedDict(
    "GetPolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)

GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "PolicyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetProtectionStatusRequestRequestTypeDef = TypedDict(
    "_RequiredGetProtectionStatusRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)
_OptionalGetProtectionStatusRequestRequestTypeDef = TypedDict(
    "_OptionalGetProtectionStatusRequestRequestTypeDef",
    {
        "MemberAccountId": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetProtectionStatusRequestRequestTypeDef(
    _RequiredGetProtectionStatusRequestRequestTypeDef,
    _OptionalGetProtectionStatusRequestRequestTypeDef,
):
    pass


GetProtectionStatusResponseTypeDef = TypedDict(
    "GetProtectionStatusResponseTypeDef",
    {
        "AdminAccountId": str,
        "ServiceType": SecurityServiceTypeType,
        "Data": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetProtocolsListRequestRequestTypeDef = TypedDict(
    "_RequiredGetProtocolsListRequestRequestTypeDef",
    {
        "ListId": str,
    },
)
_OptionalGetProtocolsListRequestRequestTypeDef = TypedDict(
    "_OptionalGetProtocolsListRequestRequestTypeDef",
    {
        "DefaultList": bool,
    },
    total=False,
)


class GetProtocolsListRequestRequestTypeDef(
    _RequiredGetProtocolsListRequestRequestTypeDef, _OptionalGetProtocolsListRequestRequestTypeDef
):
    pass


GetProtocolsListResponseTypeDef = TypedDict(
    "GetProtocolsListResponseTypeDef",
    {
        "ProtocolsList": "ProtocolsListDataTypeDef",
        "ProtocolsListArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetViolationDetailsRequestRequestTypeDef = TypedDict(
    "GetViolationDetailsRequestRequestTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
        "ResourceId": str,
        "ResourceType": str,
    },
)

GetViolationDetailsResponseTypeDef = TypedDict(
    "GetViolationDetailsResponseTypeDef",
    {
        "ViolationDetail": "ViolationDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAppsListsRequestRequestTypeDef = TypedDict(
    "_RequiredListAppsListsRequestRequestTypeDef",
    {
        "MaxResults": int,
    },
)
_OptionalListAppsListsRequestRequestTypeDef = TypedDict(
    "_OptionalListAppsListsRequestRequestTypeDef",
    {
        "DefaultLists": bool,
        "NextToken": str,
    },
    total=False,
)


class ListAppsListsRequestRequestTypeDef(
    _RequiredListAppsListsRequestRequestTypeDef, _OptionalListAppsListsRequestRequestTypeDef
):
    pass


ListAppsListsResponseTypeDef = TypedDict(
    "ListAppsListsResponseTypeDef",
    {
        "AppsLists": List["AppsListDataSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListComplianceStatusRequestRequestTypeDef = TypedDict(
    "_RequiredListComplianceStatusRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)
_OptionalListComplianceStatusRequestRequestTypeDef = TypedDict(
    "_OptionalListComplianceStatusRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListComplianceStatusRequestRequestTypeDef(
    _RequiredListComplianceStatusRequestRequestTypeDef,
    _OptionalListComplianceStatusRequestRequestTypeDef,
):
    pass


ListComplianceStatusResponseTypeDef = TypedDict(
    "ListComplianceStatusResponseTypeDef",
    {
        "PolicyComplianceStatusList": List["PolicyComplianceStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMemberAccountsRequestRequestTypeDef = TypedDict(
    "ListMemberAccountsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListMemberAccountsResponseTypeDef = TypedDict(
    "ListMemberAccountsResponseTypeDef",
    {
        "MemberAccounts": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPoliciesRequestRequestTypeDef = TypedDict(
    "ListPoliciesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPoliciesResponseTypeDef = TypedDict(
    "ListPoliciesResponseTypeDef",
    {
        "PolicyList": List["PolicySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProtocolsListsRequestRequestTypeDef = TypedDict(
    "_RequiredListProtocolsListsRequestRequestTypeDef",
    {
        "MaxResults": int,
    },
)
_OptionalListProtocolsListsRequestRequestTypeDef = TypedDict(
    "_OptionalListProtocolsListsRequestRequestTypeDef",
    {
        "DefaultLists": bool,
        "NextToken": str,
    },
    total=False,
)


class ListProtocolsListsRequestRequestTypeDef(
    _RequiredListProtocolsListsRequestRequestTypeDef,
    _OptionalListProtocolsListsRequestRequestTypeDef,
):
    pass


ListProtocolsListsResponseTypeDef = TypedDict(
    "ListProtocolsListsResponseTypeDef",
    {
        "ProtocolsLists": List["ProtocolsListDataSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkFirewallMissingExpectedRTViolationTypeDef = TypedDict(
    "NetworkFirewallMissingExpectedRTViolationTypeDef",
    {
        "ViolationTarget": str,
        "VPC": str,
        "AvailabilityZone": str,
        "CurrentRouteTable": str,
        "ExpectedRouteTable": str,
    },
    total=False,
)

NetworkFirewallMissingFirewallViolationTypeDef = TypedDict(
    "NetworkFirewallMissingFirewallViolationTypeDef",
    {
        "ViolationTarget": str,
        "VPC": str,
        "AvailabilityZone": str,
        "TargetViolationReason": str,
    },
    total=False,
)

NetworkFirewallMissingSubnetViolationTypeDef = TypedDict(
    "NetworkFirewallMissingSubnetViolationTypeDef",
    {
        "ViolationTarget": str,
        "VPC": str,
        "AvailabilityZone": str,
        "TargetViolationReason": str,
    },
    total=False,
)

NetworkFirewallPolicyDescriptionTypeDef = TypedDict(
    "NetworkFirewallPolicyDescriptionTypeDef",
    {
        "StatelessRuleGroups": List["StatelessRuleGroupTypeDef"],
        "StatelessDefaultActions": List[str],
        "StatelessFragmentDefaultActions": List[str],
        "StatelessCustomActions": List[str],
        "StatefulRuleGroups": List["StatefulRuleGroupTypeDef"],
    },
    total=False,
)

NetworkFirewallPolicyModifiedViolationTypeDef = TypedDict(
    "NetworkFirewallPolicyModifiedViolationTypeDef",
    {
        "ViolationTarget": str,
        "CurrentPolicyDescription": "NetworkFirewallPolicyDescriptionTypeDef",
        "ExpectedPolicyDescription": "NetworkFirewallPolicyDescriptionTypeDef",
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

PartialMatchTypeDef = TypedDict(
    "PartialMatchTypeDef",
    {
        "Reference": str,
        "TargetViolationReasons": List[str],
    },
    total=False,
)

PolicyComplianceDetailTypeDef = TypedDict(
    "PolicyComplianceDetailTypeDef",
    {
        "PolicyOwner": str,
        "PolicyId": str,
        "MemberAccount": str,
        "Violators": List["ComplianceViolatorTypeDef"],
        "EvaluationLimitExceeded": bool,
        "ExpiredAt": datetime,
        "IssueInfoMap": Dict[DependentServiceNameType, str],
    },
    total=False,
)

PolicyComplianceStatusTypeDef = TypedDict(
    "PolicyComplianceStatusTypeDef",
    {
        "PolicyOwner": str,
        "PolicyId": str,
        "PolicyName": str,
        "MemberAccount": str,
        "EvaluationResults": List["EvaluationResultTypeDef"],
        "LastUpdated": datetime,
        "IssueInfoMap": Dict[DependentServiceNameType, str],
    },
    total=False,
)

PolicySummaryTypeDef = TypedDict(
    "PolicySummaryTypeDef",
    {
        "PolicyArn": str,
        "PolicyId": str,
        "PolicyName": str,
        "ResourceType": str,
        "SecurityServiceType": SecurityServiceTypeType,
        "RemediationEnabled": bool,
    },
    total=False,
)

_RequiredPolicyTypeDef = TypedDict(
    "_RequiredPolicyTypeDef",
    {
        "PolicyName": str,
        "SecurityServicePolicyData": "SecurityServicePolicyDataTypeDef",
        "ResourceType": str,
        "ExcludeResourceTags": bool,
        "RemediationEnabled": bool,
    },
)
_OptionalPolicyTypeDef = TypedDict(
    "_OptionalPolicyTypeDef",
    {
        "PolicyId": str,
        "PolicyUpdateToken": str,
        "ResourceTypeList": List[str],
        "ResourceTags": List["ResourceTagTypeDef"],
        "IncludeMap": Dict[CustomerPolicyScopeIdTypeType, List[str]],
        "ExcludeMap": Dict[CustomerPolicyScopeIdTypeType, List[str]],
    },
    total=False,
)


class PolicyTypeDef(_RequiredPolicyTypeDef, _OptionalPolicyTypeDef):
    pass


ProtocolsListDataSummaryTypeDef = TypedDict(
    "ProtocolsListDataSummaryTypeDef",
    {
        "ListArn": str,
        "ListId": str,
        "ListName": str,
        "ProtocolsList": List[str],
    },
    total=False,
)

_RequiredProtocolsListDataTypeDef = TypedDict(
    "_RequiredProtocolsListDataTypeDef",
    {
        "ListName": str,
        "ProtocolsList": List[str],
    },
)
_OptionalProtocolsListDataTypeDef = TypedDict(
    "_OptionalProtocolsListDataTypeDef",
    {
        "ListId": str,
        "ListUpdateToken": str,
        "CreateTime": datetime,
        "LastUpdateTime": datetime,
        "PreviousProtocolsList": Dict[str, List[str]],
    },
    total=False,
)


class ProtocolsListDataTypeDef(
    _RequiredProtocolsListDataTypeDef, _OptionalProtocolsListDataTypeDef
):
    pass


_RequiredPutAppsListRequestRequestTypeDef = TypedDict(
    "_RequiredPutAppsListRequestRequestTypeDef",
    {
        "AppsList": "AppsListDataTypeDef",
    },
)
_OptionalPutAppsListRequestRequestTypeDef = TypedDict(
    "_OptionalPutAppsListRequestRequestTypeDef",
    {
        "TagList": List["TagTypeDef"],
    },
    total=False,
)


class PutAppsListRequestRequestTypeDef(
    _RequiredPutAppsListRequestRequestTypeDef, _OptionalPutAppsListRequestRequestTypeDef
):
    pass


PutAppsListResponseTypeDef = TypedDict(
    "PutAppsListResponseTypeDef",
    {
        "AppsList": "AppsListDataTypeDef",
        "AppsListArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutNotificationChannelRequestRequestTypeDef = TypedDict(
    "PutNotificationChannelRequestRequestTypeDef",
    {
        "SnsTopicArn": str,
        "SnsRoleName": str,
    },
)

_RequiredPutPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutPolicyRequestRequestTypeDef",
    {
        "Policy": "PolicyTypeDef",
    },
)
_OptionalPutPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutPolicyRequestRequestTypeDef",
    {
        "TagList": List["TagTypeDef"],
    },
    total=False,
)


class PutPolicyRequestRequestTypeDef(
    _RequiredPutPolicyRequestRequestTypeDef, _OptionalPutPolicyRequestRequestTypeDef
):
    pass


PutPolicyResponseTypeDef = TypedDict(
    "PutPolicyResponseTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "PolicyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutProtocolsListRequestRequestTypeDef = TypedDict(
    "_RequiredPutProtocolsListRequestRequestTypeDef",
    {
        "ProtocolsList": "ProtocolsListDataTypeDef",
    },
)
_OptionalPutProtocolsListRequestRequestTypeDef = TypedDict(
    "_OptionalPutProtocolsListRequestRequestTypeDef",
    {
        "TagList": List["TagTypeDef"],
    },
    total=False,
)


class PutProtocolsListRequestRequestTypeDef(
    _RequiredPutProtocolsListRequestRequestTypeDef, _OptionalPutProtocolsListRequestRequestTypeDef
):
    pass


PutProtocolsListResponseTypeDef = TypedDict(
    "PutProtocolsListResponseTypeDef",
    {
        "ProtocolsList": "ProtocolsListDataTypeDef",
        "ProtocolsListArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredResourceTagTypeDef = TypedDict(
    "_RequiredResourceTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalResourceTagTypeDef = TypedDict(
    "_OptionalResourceTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class ResourceTagTypeDef(_RequiredResourceTagTypeDef, _OptionalResourceTagTypeDef):
    pass


ResourceViolationTypeDef = TypedDict(
    "ResourceViolationTypeDef",
    {
        "AwsVPCSecurityGroupViolation": "AwsVPCSecurityGroupViolationTypeDef",
        "AwsEc2NetworkInterfaceViolation": "AwsEc2NetworkInterfaceViolationTypeDef",
        "AwsEc2InstanceViolation": "AwsEc2InstanceViolationTypeDef",
        "NetworkFirewallMissingFirewallViolation": "NetworkFirewallMissingFirewallViolationTypeDef",
        "NetworkFirewallMissingSubnetViolation": "NetworkFirewallMissingSubnetViolationTypeDef",
        "NetworkFirewallMissingExpectedRTViolation": "NetworkFirewallMissingExpectedRTViolationTypeDef",
        "NetworkFirewallPolicyModifiedViolation": "NetworkFirewallPolicyModifiedViolationTypeDef",
        "DnsRuleGroupPriorityConflictViolation": "DnsRuleGroupPriorityConflictViolationTypeDef",
        "DnsDuplicateRuleGroupViolation": "DnsDuplicateRuleGroupViolationTypeDef",
        "DnsRuleGroupLimitExceededViolation": "DnsRuleGroupLimitExceededViolationTypeDef",
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

SecurityGroupRemediationActionTypeDef = TypedDict(
    "SecurityGroupRemediationActionTypeDef",
    {
        "RemediationActionType": RemediationActionTypeType,
        "Description": str,
        "RemediationResult": "SecurityGroupRuleDescriptionTypeDef",
        "IsDefaultAction": bool,
    },
    total=False,
)

SecurityGroupRuleDescriptionTypeDef = TypedDict(
    "SecurityGroupRuleDescriptionTypeDef",
    {
        "IPV4Range": str,
        "IPV6Range": str,
        "PrefixListId": str,
        "Protocol": str,
        "FromPort": int,
        "ToPort": int,
    },
    total=False,
)

_RequiredSecurityServicePolicyDataTypeDef = TypedDict(
    "_RequiredSecurityServicePolicyDataTypeDef",
    {
        "Type": SecurityServiceTypeType,
    },
)
_OptionalSecurityServicePolicyDataTypeDef = TypedDict(
    "_OptionalSecurityServicePolicyDataTypeDef",
    {
        "ManagedServiceData": str,
    },
    total=False,
)


class SecurityServicePolicyDataTypeDef(
    _RequiredSecurityServicePolicyDataTypeDef, _OptionalSecurityServicePolicyDataTypeDef
):
    pass


StatefulRuleGroupTypeDef = TypedDict(
    "StatefulRuleGroupTypeDef",
    {
        "RuleGroupName": str,
        "ResourceId": str,
    },
    total=False,
)

StatelessRuleGroupTypeDef = TypedDict(
    "StatelessRuleGroupTypeDef",
    {
        "RuleGroupName": str,
        "ResourceId": str,
        "Priority": int,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagList": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredViolationDetailTypeDef = TypedDict(
    "_RequiredViolationDetailTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
        "ResourceId": str,
        "ResourceType": str,
        "ResourceViolations": List["ResourceViolationTypeDef"],
    },
)
_OptionalViolationDetailTypeDef = TypedDict(
    "_OptionalViolationDetailTypeDef",
    {
        "ResourceTags": List["TagTypeDef"],
        "ResourceDescription": str,
    },
    total=False,
)


class ViolationDetailTypeDef(_RequiredViolationDetailTypeDef, _OptionalViolationDetailTypeDef):
    pass
