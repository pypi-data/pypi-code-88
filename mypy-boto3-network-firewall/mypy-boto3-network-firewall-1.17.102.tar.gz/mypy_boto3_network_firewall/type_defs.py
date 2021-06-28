"""
Type annotations for network-firewall service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/type_defs.html)

Usage::

    ```python
    from mypy_boto3_network_firewall.type_defs import ActionDefinitionTypeDef

    data: ActionDefinitionTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    AttachmentStatusType,
    ConfigurationSyncStateType,
    FirewallStatusValueType,
    GeneratedRulesTypeType,
    LogDestinationTypeType,
    LogTypeType,
    PerObjectSyncStatusType,
    ResourceStatusType,
    RuleGroupTypeType,
    StatefulActionType,
    StatefulRuleDirectionType,
    StatefulRuleProtocolType,
    TargetTypeType,
    TCPFlagType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionDefinitionTypeDef",
    "AddressTypeDef",
    "AssociateFirewallPolicyRequestTypeDef",
    "AssociateFirewallPolicyResponseResponseTypeDef",
    "AssociateSubnetsRequestTypeDef",
    "AssociateSubnetsResponseResponseTypeDef",
    "AttachmentTypeDef",
    "CreateFirewallPolicyRequestTypeDef",
    "CreateFirewallPolicyResponseResponseTypeDef",
    "CreateFirewallRequestTypeDef",
    "CreateFirewallResponseResponseTypeDef",
    "CreateRuleGroupRequestTypeDef",
    "CreateRuleGroupResponseResponseTypeDef",
    "CustomActionTypeDef",
    "DeleteFirewallPolicyRequestTypeDef",
    "DeleteFirewallPolicyResponseResponseTypeDef",
    "DeleteFirewallRequestTypeDef",
    "DeleteFirewallResponseResponseTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DeleteRuleGroupRequestTypeDef",
    "DeleteRuleGroupResponseResponseTypeDef",
    "DescribeFirewallPolicyRequestTypeDef",
    "DescribeFirewallPolicyResponseResponseTypeDef",
    "DescribeFirewallRequestTypeDef",
    "DescribeFirewallResponseResponseTypeDef",
    "DescribeLoggingConfigurationRequestTypeDef",
    "DescribeLoggingConfigurationResponseResponseTypeDef",
    "DescribeResourcePolicyRequestTypeDef",
    "DescribeResourcePolicyResponseResponseTypeDef",
    "DescribeRuleGroupRequestTypeDef",
    "DescribeRuleGroupResponseResponseTypeDef",
    "DimensionTypeDef",
    "DisassociateSubnetsRequestTypeDef",
    "DisassociateSubnetsResponseResponseTypeDef",
    "FirewallMetadataTypeDef",
    "FirewallPolicyMetadataTypeDef",
    "FirewallPolicyResponseTypeDef",
    "FirewallPolicyTypeDef",
    "FirewallStatusTypeDef",
    "FirewallTypeDef",
    "HeaderTypeDef",
    "IPSetTypeDef",
    "ListFirewallPoliciesRequestTypeDef",
    "ListFirewallPoliciesResponseResponseTypeDef",
    "ListFirewallsRequestTypeDef",
    "ListFirewallsResponseResponseTypeDef",
    "ListRuleGroupsRequestTypeDef",
    "ListRuleGroupsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "LogDestinationConfigTypeDef",
    "LoggingConfigurationTypeDef",
    "MatchAttributesTypeDef",
    "PaginatorConfigTypeDef",
    "PerObjectStatusTypeDef",
    "PortRangeTypeDef",
    "PortSetTypeDef",
    "PublishMetricActionTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RuleDefinitionTypeDef",
    "RuleGroupMetadataTypeDef",
    "RuleGroupResponseTypeDef",
    "RuleGroupTypeDef",
    "RuleOptionTypeDef",
    "RuleVariablesTypeDef",
    "RulesSourceListTypeDef",
    "RulesSourceTypeDef",
    "StatefulRuleGroupReferenceTypeDef",
    "StatefulRuleTypeDef",
    "StatelessRuleGroupReferenceTypeDef",
    "StatelessRuleTypeDef",
    "StatelessRulesAndCustomActionsTypeDef",
    "SubnetMappingTypeDef",
    "SyncStateTypeDef",
    "TCPFlagFieldTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateFirewallDeleteProtectionRequestTypeDef",
    "UpdateFirewallDeleteProtectionResponseResponseTypeDef",
    "UpdateFirewallDescriptionRequestTypeDef",
    "UpdateFirewallDescriptionResponseResponseTypeDef",
    "UpdateFirewallPolicyChangeProtectionRequestTypeDef",
    "UpdateFirewallPolicyChangeProtectionResponseResponseTypeDef",
    "UpdateFirewallPolicyRequestTypeDef",
    "UpdateFirewallPolicyResponseResponseTypeDef",
    "UpdateLoggingConfigurationRequestTypeDef",
    "UpdateLoggingConfigurationResponseResponseTypeDef",
    "UpdateRuleGroupRequestTypeDef",
    "UpdateRuleGroupResponseResponseTypeDef",
    "UpdateSubnetChangeProtectionRequestTypeDef",
    "UpdateSubnetChangeProtectionResponseResponseTypeDef",
)

ActionDefinitionTypeDef = TypedDict(
    "ActionDefinitionTypeDef",
    {
        "PublishMetricAction": "PublishMetricActionTypeDef",
    },
    total=False,
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "AddressDefinition": str,
    },
)

_RequiredAssociateFirewallPolicyRequestTypeDef = TypedDict(
    "_RequiredAssociateFirewallPolicyRequestTypeDef",
    {
        "FirewallPolicyArn": str,
    },
)
_OptionalAssociateFirewallPolicyRequestTypeDef = TypedDict(
    "_OptionalAssociateFirewallPolicyRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)


class AssociateFirewallPolicyRequestTypeDef(
    _RequiredAssociateFirewallPolicyRequestTypeDef, _OptionalAssociateFirewallPolicyRequestTypeDef
):
    pass


AssociateFirewallPolicyResponseResponseTypeDef = TypedDict(
    "AssociateFirewallPolicyResponseResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "FirewallPolicyArn": str,
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateSubnetsRequestTypeDef = TypedDict(
    "_RequiredAssociateSubnetsRequestTypeDef",
    {
        "SubnetMappings": List["SubnetMappingTypeDef"],
    },
)
_OptionalAssociateSubnetsRequestTypeDef = TypedDict(
    "_OptionalAssociateSubnetsRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)


class AssociateSubnetsRequestTypeDef(
    _RequiredAssociateSubnetsRequestTypeDef, _OptionalAssociateSubnetsRequestTypeDef
):
    pass


AssociateSubnetsResponseResponseTypeDef = TypedDict(
    "AssociateSubnetsResponseResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "SubnetMappings": List["SubnetMappingTypeDef"],
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef",
    {
        "SubnetId": str,
        "EndpointId": str,
        "Status": AttachmentStatusType,
    },
    total=False,
)

_RequiredCreateFirewallPolicyRequestTypeDef = TypedDict(
    "_RequiredCreateFirewallPolicyRequestTypeDef",
    {
        "FirewallPolicyName": str,
        "FirewallPolicy": "FirewallPolicyTypeDef",
    },
)
_OptionalCreateFirewallPolicyRequestTypeDef = TypedDict(
    "_OptionalCreateFirewallPolicyRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CreateFirewallPolicyRequestTypeDef(
    _RequiredCreateFirewallPolicyRequestTypeDef, _OptionalCreateFirewallPolicyRequestTypeDef
):
    pass


CreateFirewallPolicyResponseResponseTypeDef = TypedDict(
    "CreateFirewallPolicyResponseResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallPolicyResponse": "FirewallPolicyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFirewallRequestTypeDef = TypedDict(
    "_RequiredCreateFirewallRequestTypeDef",
    {
        "FirewallName": str,
        "FirewallPolicyArn": str,
        "VpcId": str,
        "SubnetMappings": List["SubnetMappingTypeDef"],
    },
)
_OptionalCreateFirewallRequestTypeDef = TypedDict(
    "_OptionalCreateFirewallRequestTypeDef",
    {
        "DeleteProtection": bool,
        "SubnetChangeProtection": bool,
        "FirewallPolicyChangeProtection": bool,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateFirewallRequestTypeDef(
    _RequiredCreateFirewallRequestTypeDef, _OptionalCreateFirewallRequestTypeDef
):
    pass


CreateFirewallResponseResponseTypeDef = TypedDict(
    "CreateFirewallResponseResponseTypeDef",
    {
        "Firewall": "FirewallTypeDef",
        "FirewallStatus": "FirewallStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRuleGroupRequestTypeDef = TypedDict(
    "_RequiredCreateRuleGroupRequestTypeDef",
    {
        "RuleGroupName": str,
        "Type": RuleGroupTypeType,
        "Capacity": int,
    },
)
_OptionalCreateRuleGroupRequestTypeDef = TypedDict(
    "_OptionalCreateRuleGroupRequestTypeDef",
    {
        "RuleGroup": "RuleGroupTypeDef",
        "Rules": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CreateRuleGroupRequestTypeDef(
    _RequiredCreateRuleGroupRequestTypeDef, _OptionalCreateRuleGroupRequestTypeDef
):
    pass


CreateRuleGroupResponseResponseTypeDef = TypedDict(
    "CreateRuleGroupResponseResponseTypeDef",
    {
        "UpdateToken": str,
        "RuleGroupResponse": "RuleGroupResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomActionTypeDef = TypedDict(
    "CustomActionTypeDef",
    {
        "ActionName": str,
        "ActionDefinition": "ActionDefinitionTypeDef",
    },
)

DeleteFirewallPolicyRequestTypeDef = TypedDict(
    "DeleteFirewallPolicyRequestTypeDef",
    {
        "FirewallPolicyName": str,
        "FirewallPolicyArn": str,
    },
    total=False,
)

DeleteFirewallPolicyResponseResponseTypeDef = TypedDict(
    "DeleteFirewallPolicyResponseResponseTypeDef",
    {
        "FirewallPolicyResponse": "FirewallPolicyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFirewallRequestTypeDef = TypedDict(
    "DeleteFirewallRequestTypeDef",
    {
        "FirewallName": str,
        "FirewallArn": str,
    },
    total=False,
)

DeleteFirewallResponseResponseTypeDef = TypedDict(
    "DeleteFirewallResponseResponseTypeDef",
    {
        "Firewall": "FirewallTypeDef",
        "FirewallStatus": "FirewallStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcePolicyRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DeleteRuleGroupRequestTypeDef = TypedDict(
    "DeleteRuleGroupRequestTypeDef",
    {
        "RuleGroupName": str,
        "RuleGroupArn": str,
        "Type": RuleGroupTypeType,
    },
    total=False,
)

DeleteRuleGroupResponseResponseTypeDef = TypedDict(
    "DeleteRuleGroupResponseResponseTypeDef",
    {
        "RuleGroupResponse": "RuleGroupResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFirewallPolicyRequestTypeDef = TypedDict(
    "DescribeFirewallPolicyRequestTypeDef",
    {
        "FirewallPolicyName": str,
        "FirewallPolicyArn": str,
    },
    total=False,
)

DescribeFirewallPolicyResponseResponseTypeDef = TypedDict(
    "DescribeFirewallPolicyResponseResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallPolicyResponse": "FirewallPolicyResponseTypeDef",
        "FirewallPolicy": "FirewallPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFirewallRequestTypeDef = TypedDict(
    "DescribeFirewallRequestTypeDef",
    {
        "FirewallName": str,
        "FirewallArn": str,
    },
    total=False,
)

DescribeFirewallResponseResponseTypeDef = TypedDict(
    "DescribeFirewallResponseResponseTypeDef",
    {
        "UpdateToken": str,
        "Firewall": "FirewallTypeDef",
        "FirewallStatus": "FirewallStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoggingConfigurationRequestTypeDef = TypedDict(
    "DescribeLoggingConfigurationRequestTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)

DescribeLoggingConfigurationResponseResponseTypeDef = TypedDict(
    "DescribeLoggingConfigurationResponseResponseTypeDef",
    {
        "FirewallArn": str,
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourcePolicyRequestTypeDef = TypedDict(
    "DescribeResourcePolicyRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeResourcePolicyResponseResponseTypeDef = TypedDict(
    "DescribeResourcePolicyResponseResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRuleGroupRequestTypeDef = TypedDict(
    "DescribeRuleGroupRequestTypeDef",
    {
        "RuleGroupName": str,
        "RuleGroupArn": str,
        "Type": RuleGroupTypeType,
    },
    total=False,
)

DescribeRuleGroupResponseResponseTypeDef = TypedDict(
    "DescribeRuleGroupResponseResponseTypeDef",
    {
        "UpdateToken": str,
        "RuleGroup": "RuleGroupTypeDef",
        "RuleGroupResponse": "RuleGroupResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Value": str,
    },
)

_RequiredDisassociateSubnetsRequestTypeDef = TypedDict(
    "_RequiredDisassociateSubnetsRequestTypeDef",
    {
        "SubnetIds": List[str],
    },
)
_OptionalDisassociateSubnetsRequestTypeDef = TypedDict(
    "_OptionalDisassociateSubnetsRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)


class DisassociateSubnetsRequestTypeDef(
    _RequiredDisassociateSubnetsRequestTypeDef, _OptionalDisassociateSubnetsRequestTypeDef
):
    pass


DisassociateSubnetsResponseResponseTypeDef = TypedDict(
    "DisassociateSubnetsResponseResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "SubnetMappings": List["SubnetMappingTypeDef"],
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FirewallMetadataTypeDef = TypedDict(
    "FirewallMetadataTypeDef",
    {
        "FirewallName": str,
        "FirewallArn": str,
    },
    total=False,
)

FirewallPolicyMetadataTypeDef = TypedDict(
    "FirewallPolicyMetadataTypeDef",
    {
        "Name": str,
        "Arn": str,
    },
    total=False,
)

_RequiredFirewallPolicyResponseTypeDef = TypedDict(
    "_RequiredFirewallPolicyResponseTypeDef",
    {
        "FirewallPolicyName": str,
        "FirewallPolicyArn": str,
        "FirewallPolicyId": str,
    },
)
_OptionalFirewallPolicyResponseTypeDef = TypedDict(
    "_OptionalFirewallPolicyResponseTypeDef",
    {
        "Description": str,
        "FirewallPolicyStatus": ResourceStatusType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class FirewallPolicyResponseTypeDef(
    _RequiredFirewallPolicyResponseTypeDef, _OptionalFirewallPolicyResponseTypeDef
):
    pass


_RequiredFirewallPolicyTypeDef = TypedDict(
    "_RequiredFirewallPolicyTypeDef",
    {
        "StatelessDefaultActions": List[str],
        "StatelessFragmentDefaultActions": List[str],
    },
)
_OptionalFirewallPolicyTypeDef = TypedDict(
    "_OptionalFirewallPolicyTypeDef",
    {
        "StatelessRuleGroupReferences": List["StatelessRuleGroupReferenceTypeDef"],
        "StatelessCustomActions": List["CustomActionTypeDef"],
        "StatefulRuleGroupReferences": List["StatefulRuleGroupReferenceTypeDef"],
    },
    total=False,
)


class FirewallPolicyTypeDef(_RequiredFirewallPolicyTypeDef, _OptionalFirewallPolicyTypeDef):
    pass


_RequiredFirewallStatusTypeDef = TypedDict(
    "_RequiredFirewallStatusTypeDef",
    {
        "Status": FirewallStatusValueType,
        "ConfigurationSyncStateSummary": ConfigurationSyncStateType,
    },
)
_OptionalFirewallStatusTypeDef = TypedDict(
    "_OptionalFirewallStatusTypeDef",
    {
        "SyncStates": Dict[str, "SyncStateTypeDef"],
    },
    total=False,
)


class FirewallStatusTypeDef(_RequiredFirewallStatusTypeDef, _OptionalFirewallStatusTypeDef):
    pass


_RequiredFirewallTypeDef = TypedDict(
    "_RequiredFirewallTypeDef",
    {
        "FirewallPolicyArn": str,
        "VpcId": str,
        "SubnetMappings": List["SubnetMappingTypeDef"],
        "FirewallId": str,
    },
)
_OptionalFirewallTypeDef = TypedDict(
    "_OptionalFirewallTypeDef",
    {
        "FirewallName": str,
        "FirewallArn": str,
        "DeleteProtection": bool,
        "SubnetChangeProtection": bool,
        "FirewallPolicyChangeProtection": bool,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class FirewallTypeDef(_RequiredFirewallTypeDef, _OptionalFirewallTypeDef):
    pass


HeaderTypeDef = TypedDict(
    "HeaderTypeDef",
    {
        "Protocol": StatefulRuleProtocolType,
        "Source": str,
        "SourcePort": str,
        "Direction": StatefulRuleDirectionType,
        "Destination": str,
        "DestinationPort": str,
    },
)

IPSetTypeDef = TypedDict(
    "IPSetTypeDef",
    {
        "Definition": List[str],
    },
)

ListFirewallPoliciesRequestTypeDef = TypedDict(
    "ListFirewallPoliciesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListFirewallPoliciesResponseResponseTypeDef = TypedDict(
    "ListFirewallPoliciesResponseResponseTypeDef",
    {
        "NextToken": str,
        "FirewallPolicies": List["FirewallPolicyMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFirewallsRequestTypeDef = TypedDict(
    "ListFirewallsRequestTypeDef",
    {
        "NextToken": str,
        "VpcIds": List[str],
        "MaxResults": int,
    },
    total=False,
)

ListFirewallsResponseResponseTypeDef = TypedDict(
    "ListFirewallsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Firewalls": List["FirewallMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRuleGroupsRequestTypeDef = TypedDict(
    "ListRuleGroupsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListRuleGroupsResponseResponseTypeDef = TypedDict(
    "ListRuleGroupsResponseResponseTypeDef",
    {
        "NextToken": str,
        "RuleGroups": List["RuleGroupMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTagsForResourceRequestTypeDef(
    _RequiredListTagsForResourceRequestTypeDef, _OptionalListTagsForResourceRequestTypeDef
):
    pass


ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "NextToken": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogDestinationConfigTypeDef = TypedDict(
    "LogDestinationConfigTypeDef",
    {
        "LogType": LogTypeType,
        "LogDestinationType": LogDestinationTypeType,
        "LogDestination": Dict[str, str],
    },
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "LogDestinationConfigs": List["LogDestinationConfigTypeDef"],
    },
)

MatchAttributesTypeDef = TypedDict(
    "MatchAttributesTypeDef",
    {
        "Sources": List["AddressTypeDef"],
        "Destinations": List["AddressTypeDef"],
        "SourcePorts": List["PortRangeTypeDef"],
        "DestinationPorts": List["PortRangeTypeDef"],
        "Protocols": List[int],
        "TCPFlags": List["TCPFlagFieldTypeDef"],
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

PerObjectStatusTypeDef = TypedDict(
    "PerObjectStatusTypeDef",
    {
        "SyncStatus": PerObjectSyncStatusType,
        "UpdateToken": str,
    },
    total=False,
)

PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
    },
)

PortSetTypeDef = TypedDict(
    "PortSetTypeDef",
    {
        "Definition": List[str],
    },
    total=False,
)

PublishMetricActionTypeDef = TypedDict(
    "PublishMetricActionTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
    },
)

PutResourcePolicyRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
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

RuleDefinitionTypeDef = TypedDict(
    "RuleDefinitionTypeDef",
    {
        "MatchAttributes": "MatchAttributesTypeDef",
        "Actions": List[str],
    },
)

RuleGroupMetadataTypeDef = TypedDict(
    "RuleGroupMetadataTypeDef",
    {
        "Name": str,
        "Arn": str,
    },
    total=False,
)

_RequiredRuleGroupResponseTypeDef = TypedDict(
    "_RequiredRuleGroupResponseTypeDef",
    {
        "RuleGroupArn": str,
        "RuleGroupName": str,
        "RuleGroupId": str,
    },
)
_OptionalRuleGroupResponseTypeDef = TypedDict(
    "_OptionalRuleGroupResponseTypeDef",
    {
        "Description": str,
        "Type": RuleGroupTypeType,
        "Capacity": int,
        "RuleGroupStatus": ResourceStatusType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class RuleGroupResponseTypeDef(
    _RequiredRuleGroupResponseTypeDef, _OptionalRuleGroupResponseTypeDef
):
    pass


_RequiredRuleGroupTypeDef = TypedDict(
    "_RequiredRuleGroupTypeDef",
    {
        "RulesSource": "RulesSourceTypeDef",
    },
)
_OptionalRuleGroupTypeDef = TypedDict(
    "_OptionalRuleGroupTypeDef",
    {
        "RuleVariables": "RuleVariablesTypeDef",
    },
    total=False,
)


class RuleGroupTypeDef(_RequiredRuleGroupTypeDef, _OptionalRuleGroupTypeDef):
    pass


_RequiredRuleOptionTypeDef = TypedDict(
    "_RequiredRuleOptionTypeDef",
    {
        "Keyword": str,
    },
)
_OptionalRuleOptionTypeDef = TypedDict(
    "_OptionalRuleOptionTypeDef",
    {
        "Settings": List[str],
    },
    total=False,
)


class RuleOptionTypeDef(_RequiredRuleOptionTypeDef, _OptionalRuleOptionTypeDef):
    pass


RuleVariablesTypeDef = TypedDict(
    "RuleVariablesTypeDef",
    {
        "IPSets": Dict[str, "IPSetTypeDef"],
        "PortSets": Dict[str, "PortSetTypeDef"],
    },
    total=False,
)

RulesSourceListTypeDef = TypedDict(
    "RulesSourceListTypeDef",
    {
        "Targets": List[str],
        "TargetTypes": List[TargetTypeType],
        "GeneratedRulesType": GeneratedRulesTypeType,
    },
)

RulesSourceTypeDef = TypedDict(
    "RulesSourceTypeDef",
    {
        "RulesString": str,
        "RulesSourceList": "RulesSourceListTypeDef",
        "StatefulRules": List["StatefulRuleTypeDef"],
        "StatelessRulesAndCustomActions": "StatelessRulesAndCustomActionsTypeDef",
    },
    total=False,
)

StatefulRuleGroupReferenceTypeDef = TypedDict(
    "StatefulRuleGroupReferenceTypeDef",
    {
        "ResourceArn": str,
    },
)

StatefulRuleTypeDef = TypedDict(
    "StatefulRuleTypeDef",
    {
        "Action": StatefulActionType,
        "Header": "HeaderTypeDef",
        "RuleOptions": List["RuleOptionTypeDef"],
    },
)

StatelessRuleGroupReferenceTypeDef = TypedDict(
    "StatelessRuleGroupReferenceTypeDef",
    {
        "ResourceArn": str,
        "Priority": int,
    },
)

StatelessRuleTypeDef = TypedDict(
    "StatelessRuleTypeDef",
    {
        "RuleDefinition": "RuleDefinitionTypeDef",
        "Priority": int,
    },
)

_RequiredStatelessRulesAndCustomActionsTypeDef = TypedDict(
    "_RequiredStatelessRulesAndCustomActionsTypeDef",
    {
        "StatelessRules": List["StatelessRuleTypeDef"],
    },
)
_OptionalStatelessRulesAndCustomActionsTypeDef = TypedDict(
    "_OptionalStatelessRulesAndCustomActionsTypeDef",
    {
        "CustomActions": List["CustomActionTypeDef"],
    },
    total=False,
)


class StatelessRulesAndCustomActionsTypeDef(
    _RequiredStatelessRulesAndCustomActionsTypeDef, _OptionalStatelessRulesAndCustomActionsTypeDef
):
    pass


SubnetMappingTypeDef = TypedDict(
    "SubnetMappingTypeDef",
    {
        "SubnetId": str,
    },
)

SyncStateTypeDef = TypedDict(
    "SyncStateTypeDef",
    {
        "Attachment": "AttachmentTypeDef",
        "Config": Dict[str, "PerObjectStatusTypeDef"],
    },
    total=False,
)

_RequiredTCPFlagFieldTypeDef = TypedDict(
    "_RequiredTCPFlagFieldTypeDef",
    {
        "Flags": List[TCPFlagType],
    },
)
_OptionalTCPFlagFieldTypeDef = TypedDict(
    "_OptionalTCPFlagFieldTypeDef",
    {
        "Masks": List[TCPFlagType],
    },
    total=False,
)


class TCPFlagFieldTypeDef(_RequiredTCPFlagFieldTypeDef, _OptionalTCPFlagFieldTypeDef):
    pass


TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
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
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateFirewallDeleteProtectionRequestTypeDef = TypedDict(
    "_RequiredUpdateFirewallDeleteProtectionRequestTypeDef",
    {
        "DeleteProtection": bool,
    },
)
_OptionalUpdateFirewallDeleteProtectionRequestTypeDef = TypedDict(
    "_OptionalUpdateFirewallDeleteProtectionRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)


class UpdateFirewallDeleteProtectionRequestTypeDef(
    _RequiredUpdateFirewallDeleteProtectionRequestTypeDef,
    _OptionalUpdateFirewallDeleteProtectionRequestTypeDef,
):
    pass


UpdateFirewallDeleteProtectionResponseResponseTypeDef = TypedDict(
    "UpdateFirewallDeleteProtectionResponseResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "DeleteProtection": bool,
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFirewallDescriptionRequestTypeDef = TypedDict(
    "UpdateFirewallDescriptionRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
        "Description": str,
    },
    total=False,
)

UpdateFirewallDescriptionResponseResponseTypeDef = TypedDict(
    "UpdateFirewallDescriptionResponseResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "Description": str,
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFirewallPolicyChangeProtectionRequestTypeDef = TypedDict(
    "_RequiredUpdateFirewallPolicyChangeProtectionRequestTypeDef",
    {
        "FirewallPolicyChangeProtection": bool,
    },
)
_OptionalUpdateFirewallPolicyChangeProtectionRequestTypeDef = TypedDict(
    "_OptionalUpdateFirewallPolicyChangeProtectionRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)


class UpdateFirewallPolicyChangeProtectionRequestTypeDef(
    _RequiredUpdateFirewallPolicyChangeProtectionRequestTypeDef,
    _OptionalUpdateFirewallPolicyChangeProtectionRequestTypeDef,
):
    pass


UpdateFirewallPolicyChangeProtectionResponseResponseTypeDef = TypedDict(
    "UpdateFirewallPolicyChangeProtectionResponseResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
        "FirewallPolicyChangeProtection": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFirewallPolicyRequestTypeDef = TypedDict(
    "_RequiredUpdateFirewallPolicyRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallPolicy": "FirewallPolicyTypeDef",
    },
)
_OptionalUpdateFirewallPolicyRequestTypeDef = TypedDict(
    "_OptionalUpdateFirewallPolicyRequestTypeDef",
    {
        "FirewallPolicyArn": str,
        "FirewallPolicyName": str,
        "Description": str,
        "DryRun": bool,
    },
    total=False,
)


class UpdateFirewallPolicyRequestTypeDef(
    _RequiredUpdateFirewallPolicyRequestTypeDef, _OptionalUpdateFirewallPolicyRequestTypeDef
):
    pass


UpdateFirewallPolicyResponseResponseTypeDef = TypedDict(
    "UpdateFirewallPolicyResponseResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallPolicyResponse": "FirewallPolicyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateLoggingConfigurationRequestTypeDef = TypedDict(
    "UpdateLoggingConfigurationRequestTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
    },
    total=False,
)

UpdateLoggingConfigurationResponseResponseTypeDef = TypedDict(
    "UpdateLoggingConfigurationResponseResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRuleGroupRequestTypeDef = TypedDict(
    "_RequiredUpdateRuleGroupRequestTypeDef",
    {
        "UpdateToken": str,
    },
)
_OptionalUpdateRuleGroupRequestTypeDef = TypedDict(
    "_OptionalUpdateRuleGroupRequestTypeDef",
    {
        "RuleGroupArn": str,
        "RuleGroupName": str,
        "RuleGroup": "RuleGroupTypeDef",
        "Rules": str,
        "Type": RuleGroupTypeType,
        "Description": str,
        "DryRun": bool,
    },
    total=False,
)


class UpdateRuleGroupRequestTypeDef(
    _RequiredUpdateRuleGroupRequestTypeDef, _OptionalUpdateRuleGroupRequestTypeDef
):
    pass


UpdateRuleGroupResponseResponseTypeDef = TypedDict(
    "UpdateRuleGroupResponseResponseTypeDef",
    {
        "UpdateToken": str,
        "RuleGroupResponse": "RuleGroupResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSubnetChangeProtectionRequestTypeDef = TypedDict(
    "_RequiredUpdateSubnetChangeProtectionRequestTypeDef",
    {
        "SubnetChangeProtection": bool,
    },
)
_OptionalUpdateSubnetChangeProtectionRequestTypeDef = TypedDict(
    "_OptionalUpdateSubnetChangeProtectionRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)


class UpdateSubnetChangeProtectionRequestTypeDef(
    _RequiredUpdateSubnetChangeProtectionRequestTypeDef,
    _OptionalUpdateSubnetChangeProtectionRequestTypeDef,
):
    pass


UpdateSubnetChangeProtectionResponseResponseTypeDef = TypedDict(
    "UpdateSubnetChangeProtectionResponseResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
        "SubnetChangeProtection": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
