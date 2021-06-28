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
    "AssociateAdminAccountRequestTypeDef",
    "AwsEc2InstanceViolationTypeDef",
    "AwsEc2NetworkInterfaceViolationTypeDef",
    "AwsVPCSecurityGroupViolationTypeDef",
    "ComplianceViolatorTypeDef",
    "DeleteAppsListRequestTypeDef",
    "DeletePolicyRequestTypeDef",
    "DeleteProtocolsListRequestTypeDef",
    "DnsDuplicateRuleGroupViolationTypeDef",
    "DnsRuleGroupLimitExceededViolationTypeDef",
    "DnsRuleGroupPriorityConflictViolationTypeDef",
    "EvaluationResultTypeDef",
    "GetAdminAccountResponseResponseTypeDef",
    "GetAppsListRequestTypeDef",
    "GetAppsListResponseResponseTypeDef",
    "GetComplianceDetailRequestTypeDef",
    "GetComplianceDetailResponseResponseTypeDef",
    "GetNotificationChannelResponseResponseTypeDef",
    "GetPolicyRequestTypeDef",
    "GetPolicyResponseResponseTypeDef",
    "GetProtectionStatusRequestTypeDef",
    "GetProtectionStatusResponseResponseTypeDef",
    "GetProtocolsListRequestTypeDef",
    "GetProtocolsListResponseResponseTypeDef",
    "GetViolationDetailsRequestTypeDef",
    "GetViolationDetailsResponseResponseTypeDef",
    "ListAppsListsRequestTypeDef",
    "ListAppsListsResponseResponseTypeDef",
    "ListComplianceStatusRequestTypeDef",
    "ListComplianceStatusResponseResponseTypeDef",
    "ListMemberAccountsRequestTypeDef",
    "ListMemberAccountsResponseResponseTypeDef",
    "ListPoliciesRequestTypeDef",
    "ListPoliciesResponseResponseTypeDef",
    "ListProtocolsListsRequestTypeDef",
    "ListProtocolsListsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
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
    "PutAppsListRequestTypeDef",
    "PutAppsListResponseResponseTypeDef",
    "PutNotificationChannelRequestTypeDef",
    "PutPolicyRequestTypeDef",
    "PutPolicyResponseResponseTypeDef",
    "PutProtocolsListRequestTypeDef",
    "PutProtocolsListResponseResponseTypeDef",
    "ResourceTagTypeDef",
    "ResourceViolationTypeDef",
    "ResponseMetadataTypeDef",
    "SecurityGroupRemediationActionTypeDef",
    "SecurityGroupRuleDescriptionTypeDef",
    "SecurityServicePolicyDataTypeDef",
    "StatefulRuleGroupTypeDef",
    "StatelessRuleGroupTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
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


AssociateAdminAccountRequestTypeDef = TypedDict(
    "AssociateAdminAccountRequestTypeDef",
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

DeleteAppsListRequestTypeDef = TypedDict(
    "DeleteAppsListRequestTypeDef",
    {
        "ListId": str,
    },
)

_RequiredDeletePolicyRequestTypeDef = TypedDict(
    "_RequiredDeletePolicyRequestTypeDef",
    {
        "PolicyId": str,
    },
)
_OptionalDeletePolicyRequestTypeDef = TypedDict(
    "_OptionalDeletePolicyRequestTypeDef",
    {
        "DeleteAllPolicyResources": bool,
    },
    total=False,
)


class DeletePolicyRequestTypeDef(
    _RequiredDeletePolicyRequestTypeDef, _OptionalDeletePolicyRequestTypeDef
):
    pass


DeleteProtocolsListRequestTypeDef = TypedDict(
    "DeleteProtocolsListRequestTypeDef",
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

GetAdminAccountResponseResponseTypeDef = TypedDict(
    "GetAdminAccountResponseResponseTypeDef",
    {
        "AdminAccount": str,
        "RoleStatus": AccountRoleStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetAppsListRequestTypeDef = TypedDict(
    "_RequiredGetAppsListRequestTypeDef",
    {
        "ListId": str,
    },
)
_OptionalGetAppsListRequestTypeDef = TypedDict(
    "_OptionalGetAppsListRequestTypeDef",
    {
        "DefaultList": bool,
    },
    total=False,
)


class GetAppsListRequestTypeDef(
    _RequiredGetAppsListRequestTypeDef, _OptionalGetAppsListRequestTypeDef
):
    pass


GetAppsListResponseResponseTypeDef = TypedDict(
    "GetAppsListResponseResponseTypeDef",
    {
        "AppsList": "AppsListDataTypeDef",
        "AppsListArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComplianceDetailRequestTypeDef = TypedDict(
    "GetComplianceDetailRequestTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
    },
)

GetComplianceDetailResponseResponseTypeDef = TypedDict(
    "GetComplianceDetailResponseResponseTypeDef",
    {
        "PolicyComplianceDetail": "PolicyComplianceDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNotificationChannelResponseResponseTypeDef = TypedDict(
    "GetNotificationChannelResponseResponseTypeDef",
    {
        "SnsTopicArn": str,
        "SnsRoleName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyRequestTypeDef = TypedDict(
    "GetPolicyRequestTypeDef",
    {
        "PolicyId": str,
    },
)

GetPolicyResponseResponseTypeDef = TypedDict(
    "GetPolicyResponseResponseTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "PolicyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetProtectionStatusRequestTypeDef = TypedDict(
    "_RequiredGetProtectionStatusRequestTypeDef",
    {
        "PolicyId": str,
    },
)
_OptionalGetProtectionStatusRequestTypeDef = TypedDict(
    "_OptionalGetProtectionStatusRequestTypeDef",
    {
        "MemberAccountId": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetProtectionStatusRequestTypeDef(
    _RequiredGetProtectionStatusRequestTypeDef, _OptionalGetProtectionStatusRequestTypeDef
):
    pass


GetProtectionStatusResponseResponseTypeDef = TypedDict(
    "GetProtectionStatusResponseResponseTypeDef",
    {
        "AdminAccountId": str,
        "ServiceType": SecurityServiceTypeType,
        "Data": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetProtocolsListRequestTypeDef = TypedDict(
    "_RequiredGetProtocolsListRequestTypeDef",
    {
        "ListId": str,
    },
)
_OptionalGetProtocolsListRequestTypeDef = TypedDict(
    "_OptionalGetProtocolsListRequestTypeDef",
    {
        "DefaultList": bool,
    },
    total=False,
)


class GetProtocolsListRequestTypeDef(
    _RequiredGetProtocolsListRequestTypeDef, _OptionalGetProtocolsListRequestTypeDef
):
    pass


GetProtocolsListResponseResponseTypeDef = TypedDict(
    "GetProtocolsListResponseResponseTypeDef",
    {
        "ProtocolsList": "ProtocolsListDataTypeDef",
        "ProtocolsListArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetViolationDetailsRequestTypeDef = TypedDict(
    "GetViolationDetailsRequestTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
        "ResourceId": str,
        "ResourceType": str,
    },
)

GetViolationDetailsResponseResponseTypeDef = TypedDict(
    "GetViolationDetailsResponseResponseTypeDef",
    {
        "ViolationDetail": "ViolationDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAppsListsRequestTypeDef = TypedDict(
    "_RequiredListAppsListsRequestTypeDef",
    {
        "MaxResults": int,
    },
)
_OptionalListAppsListsRequestTypeDef = TypedDict(
    "_OptionalListAppsListsRequestTypeDef",
    {
        "DefaultLists": bool,
        "NextToken": str,
    },
    total=False,
)


class ListAppsListsRequestTypeDef(
    _RequiredListAppsListsRequestTypeDef, _OptionalListAppsListsRequestTypeDef
):
    pass


ListAppsListsResponseResponseTypeDef = TypedDict(
    "ListAppsListsResponseResponseTypeDef",
    {
        "AppsLists": List["AppsListDataSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListComplianceStatusRequestTypeDef = TypedDict(
    "_RequiredListComplianceStatusRequestTypeDef",
    {
        "PolicyId": str,
    },
)
_OptionalListComplianceStatusRequestTypeDef = TypedDict(
    "_OptionalListComplianceStatusRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListComplianceStatusRequestTypeDef(
    _RequiredListComplianceStatusRequestTypeDef, _OptionalListComplianceStatusRequestTypeDef
):
    pass


ListComplianceStatusResponseResponseTypeDef = TypedDict(
    "ListComplianceStatusResponseResponseTypeDef",
    {
        "PolicyComplianceStatusList": List["PolicyComplianceStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMemberAccountsRequestTypeDef = TypedDict(
    "ListMemberAccountsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListMemberAccountsResponseResponseTypeDef = TypedDict(
    "ListMemberAccountsResponseResponseTypeDef",
    {
        "MemberAccounts": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPoliciesRequestTypeDef = TypedDict(
    "ListPoliciesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPoliciesResponseResponseTypeDef = TypedDict(
    "ListPoliciesResponseResponseTypeDef",
    {
        "PolicyList": List["PolicySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProtocolsListsRequestTypeDef = TypedDict(
    "_RequiredListProtocolsListsRequestTypeDef",
    {
        "MaxResults": int,
    },
)
_OptionalListProtocolsListsRequestTypeDef = TypedDict(
    "_OptionalListProtocolsListsRequestTypeDef",
    {
        "DefaultLists": bool,
        "NextToken": str,
    },
    total=False,
)


class ListProtocolsListsRequestTypeDef(
    _RequiredListProtocolsListsRequestTypeDef, _OptionalListProtocolsListsRequestTypeDef
):
    pass


ListProtocolsListsResponseResponseTypeDef = TypedDict(
    "ListProtocolsListsResponseResponseTypeDef",
    {
        "ProtocolsLists": List["ProtocolsListDataSummaryTypeDef"],
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


_RequiredPutAppsListRequestTypeDef = TypedDict(
    "_RequiredPutAppsListRequestTypeDef",
    {
        "AppsList": "AppsListDataTypeDef",
    },
)
_OptionalPutAppsListRequestTypeDef = TypedDict(
    "_OptionalPutAppsListRequestTypeDef",
    {
        "TagList": List["TagTypeDef"],
    },
    total=False,
)


class PutAppsListRequestTypeDef(
    _RequiredPutAppsListRequestTypeDef, _OptionalPutAppsListRequestTypeDef
):
    pass


PutAppsListResponseResponseTypeDef = TypedDict(
    "PutAppsListResponseResponseTypeDef",
    {
        "AppsList": "AppsListDataTypeDef",
        "AppsListArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutNotificationChannelRequestTypeDef = TypedDict(
    "PutNotificationChannelRequestTypeDef",
    {
        "SnsTopicArn": str,
        "SnsRoleName": str,
    },
)

_RequiredPutPolicyRequestTypeDef = TypedDict(
    "_RequiredPutPolicyRequestTypeDef",
    {
        "Policy": "PolicyTypeDef",
    },
)
_OptionalPutPolicyRequestTypeDef = TypedDict(
    "_OptionalPutPolicyRequestTypeDef",
    {
        "TagList": List["TagTypeDef"],
    },
    total=False,
)


class PutPolicyRequestTypeDef(_RequiredPutPolicyRequestTypeDef, _OptionalPutPolicyRequestTypeDef):
    pass


PutPolicyResponseResponseTypeDef = TypedDict(
    "PutPolicyResponseResponseTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "PolicyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutProtocolsListRequestTypeDef = TypedDict(
    "_RequiredPutProtocolsListRequestTypeDef",
    {
        "ProtocolsList": "ProtocolsListDataTypeDef",
    },
)
_OptionalPutProtocolsListRequestTypeDef = TypedDict(
    "_OptionalPutProtocolsListRequestTypeDef",
    {
        "TagList": List["TagTypeDef"],
    },
    total=False,
)


class PutProtocolsListRequestTypeDef(
    _RequiredPutProtocolsListRequestTypeDef, _OptionalPutProtocolsListRequestTypeDef
):
    pass


PutProtocolsListResponseResponseTypeDef = TypedDict(
    "PutProtocolsListResponseResponseTypeDef",
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
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

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
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
