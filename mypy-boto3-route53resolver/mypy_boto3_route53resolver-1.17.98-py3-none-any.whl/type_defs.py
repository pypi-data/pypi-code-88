"""
Type annotations for route53resolver service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/type_defs.html)

Usage::

    ```python
    from mypy_boto3_route53resolver.type_defs import AssociateFirewallRuleGroupResponseTypeDef

    data: AssociateFirewallRuleGroupResponseTypeDef = {...}
    ```
"""
import sys
from typing import List

from .literals import (
    ActionType,
    BlockResponseType,
    FirewallDomainListStatusType,
    FirewallFailOpenStatusType,
    FirewallRuleGroupAssociationStatusType,
    FirewallRuleGroupStatusType,
    IpAddressStatusType,
    MutationProtectionStatusType,
    ResolverDNSSECValidationStatusType,
    ResolverEndpointDirectionType,
    ResolverEndpointStatusType,
    ResolverQueryLogConfigAssociationErrorType,
    ResolverQueryLogConfigAssociationStatusType,
    ResolverQueryLogConfigStatusType,
    ResolverRuleAssociationStatusType,
    ResolverRuleStatusType,
    RuleTypeOptionType,
    ShareStatusType,
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
    "AssociateFirewallRuleGroupResponseTypeDef",
    "AssociateResolverEndpointIpAddressResponseTypeDef",
    "AssociateResolverQueryLogConfigResponseTypeDef",
    "AssociateResolverRuleResponseTypeDef",
    "CreateFirewallDomainListResponseTypeDef",
    "CreateFirewallRuleGroupResponseTypeDef",
    "CreateFirewallRuleResponseTypeDef",
    "CreateResolverEndpointResponseTypeDef",
    "CreateResolverQueryLogConfigResponseTypeDef",
    "CreateResolverRuleResponseTypeDef",
    "DeleteFirewallDomainListResponseTypeDef",
    "DeleteFirewallRuleGroupResponseTypeDef",
    "DeleteFirewallRuleResponseTypeDef",
    "DeleteResolverEndpointResponseTypeDef",
    "DeleteResolverQueryLogConfigResponseTypeDef",
    "DeleteResolverRuleResponseTypeDef",
    "DisassociateFirewallRuleGroupResponseTypeDef",
    "DisassociateResolverEndpointIpAddressResponseTypeDef",
    "DisassociateResolverQueryLogConfigResponseTypeDef",
    "DisassociateResolverRuleResponseTypeDef",
    "FilterTypeDef",
    "FirewallConfigTypeDef",
    "FirewallDomainListMetadataTypeDef",
    "FirewallDomainListTypeDef",
    "FirewallRuleGroupAssociationTypeDef",
    "FirewallRuleGroupMetadataTypeDef",
    "FirewallRuleGroupTypeDef",
    "FirewallRuleTypeDef",
    "GetFirewallConfigResponseTypeDef",
    "GetFirewallDomainListResponseTypeDef",
    "GetFirewallRuleGroupAssociationResponseTypeDef",
    "GetFirewallRuleGroupPolicyResponseTypeDef",
    "GetFirewallRuleGroupResponseTypeDef",
    "GetResolverDnssecConfigResponseTypeDef",
    "GetResolverEndpointResponseTypeDef",
    "GetResolverQueryLogConfigAssociationResponseTypeDef",
    "GetResolverQueryLogConfigPolicyResponseTypeDef",
    "GetResolverQueryLogConfigResponseTypeDef",
    "GetResolverRuleAssociationResponseTypeDef",
    "GetResolverRulePolicyResponseTypeDef",
    "GetResolverRuleResponseTypeDef",
    "ImportFirewallDomainsResponseTypeDef",
    "IpAddressRequestTypeDef",
    "IpAddressResponseTypeDef",
    "IpAddressUpdateTypeDef",
    "ListFirewallConfigsResponseTypeDef",
    "ListFirewallDomainListsResponseTypeDef",
    "ListFirewallDomainsResponseTypeDef",
    "ListFirewallRuleGroupAssociationsResponseTypeDef",
    "ListFirewallRuleGroupsResponseTypeDef",
    "ListFirewallRulesResponseTypeDef",
    "ListResolverDnssecConfigsResponseTypeDef",
    "ListResolverEndpointIpAddressesResponseTypeDef",
    "ListResolverEndpointsResponseTypeDef",
    "ListResolverQueryLogConfigAssociationsResponseTypeDef",
    "ListResolverQueryLogConfigsResponseTypeDef",
    "ListResolverRuleAssociationsResponseTypeDef",
    "ListResolverRulesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutFirewallRuleGroupPolicyResponseTypeDef",
    "PutResolverQueryLogConfigPolicyResponseTypeDef",
    "PutResolverRulePolicyResponseTypeDef",
    "ResolverDnssecConfigTypeDef",
    "ResolverEndpointTypeDef",
    "ResolverQueryLogConfigAssociationTypeDef",
    "ResolverQueryLogConfigTypeDef",
    "ResolverRuleAssociationTypeDef",
    "ResolverRuleConfigTypeDef",
    "ResolverRuleTypeDef",
    "TagTypeDef",
    "TargetAddressTypeDef",
    "UpdateFirewallConfigResponseTypeDef",
    "UpdateFirewallDomainsResponseTypeDef",
    "UpdateFirewallRuleGroupAssociationResponseTypeDef",
    "UpdateFirewallRuleResponseTypeDef",
    "UpdateResolverDnssecConfigResponseTypeDef",
    "UpdateResolverEndpointResponseTypeDef",
    "UpdateResolverRuleResponseTypeDef",
)

AssociateFirewallRuleGroupResponseTypeDef = TypedDict(
    "AssociateFirewallRuleGroupResponseTypeDef",
    {
        "FirewallRuleGroupAssociation": "FirewallRuleGroupAssociationTypeDef",
    },
    total=False,
)

AssociateResolverEndpointIpAddressResponseTypeDef = TypedDict(
    "AssociateResolverEndpointIpAddressResponseTypeDef",
    {
        "ResolverEndpoint": "ResolverEndpointTypeDef",
    },
    total=False,
)

AssociateResolverQueryLogConfigResponseTypeDef = TypedDict(
    "AssociateResolverQueryLogConfigResponseTypeDef",
    {
        "ResolverQueryLogConfigAssociation": "ResolverQueryLogConfigAssociationTypeDef",
    },
    total=False,
)

AssociateResolverRuleResponseTypeDef = TypedDict(
    "AssociateResolverRuleResponseTypeDef",
    {
        "ResolverRuleAssociation": "ResolverRuleAssociationTypeDef",
    },
    total=False,
)

CreateFirewallDomainListResponseTypeDef = TypedDict(
    "CreateFirewallDomainListResponseTypeDef",
    {
        "FirewallDomainList": "FirewallDomainListTypeDef",
    },
    total=False,
)

CreateFirewallRuleGroupResponseTypeDef = TypedDict(
    "CreateFirewallRuleGroupResponseTypeDef",
    {
        "FirewallRuleGroup": "FirewallRuleGroupTypeDef",
    },
    total=False,
)

CreateFirewallRuleResponseTypeDef = TypedDict(
    "CreateFirewallRuleResponseTypeDef",
    {
        "FirewallRule": "FirewallRuleTypeDef",
    },
    total=False,
)

CreateResolverEndpointResponseTypeDef = TypedDict(
    "CreateResolverEndpointResponseTypeDef",
    {
        "ResolverEndpoint": "ResolverEndpointTypeDef",
    },
    total=False,
)

CreateResolverQueryLogConfigResponseTypeDef = TypedDict(
    "CreateResolverQueryLogConfigResponseTypeDef",
    {
        "ResolverQueryLogConfig": "ResolverQueryLogConfigTypeDef",
    },
    total=False,
)

CreateResolverRuleResponseTypeDef = TypedDict(
    "CreateResolverRuleResponseTypeDef",
    {
        "ResolverRule": "ResolverRuleTypeDef",
    },
    total=False,
)

DeleteFirewallDomainListResponseTypeDef = TypedDict(
    "DeleteFirewallDomainListResponseTypeDef",
    {
        "FirewallDomainList": "FirewallDomainListTypeDef",
    },
    total=False,
)

DeleteFirewallRuleGroupResponseTypeDef = TypedDict(
    "DeleteFirewallRuleGroupResponseTypeDef",
    {
        "FirewallRuleGroup": "FirewallRuleGroupTypeDef",
    },
    total=False,
)

DeleteFirewallRuleResponseTypeDef = TypedDict(
    "DeleteFirewallRuleResponseTypeDef",
    {
        "FirewallRule": "FirewallRuleTypeDef",
    },
    total=False,
)

DeleteResolverEndpointResponseTypeDef = TypedDict(
    "DeleteResolverEndpointResponseTypeDef",
    {
        "ResolverEndpoint": "ResolverEndpointTypeDef",
    },
    total=False,
)

DeleteResolverQueryLogConfigResponseTypeDef = TypedDict(
    "DeleteResolverQueryLogConfigResponseTypeDef",
    {
        "ResolverQueryLogConfig": "ResolverQueryLogConfigTypeDef",
    },
    total=False,
)

DeleteResolverRuleResponseTypeDef = TypedDict(
    "DeleteResolverRuleResponseTypeDef",
    {
        "ResolverRule": "ResolverRuleTypeDef",
    },
    total=False,
)

DisassociateFirewallRuleGroupResponseTypeDef = TypedDict(
    "DisassociateFirewallRuleGroupResponseTypeDef",
    {
        "FirewallRuleGroupAssociation": "FirewallRuleGroupAssociationTypeDef",
    },
    total=False,
)

DisassociateResolverEndpointIpAddressResponseTypeDef = TypedDict(
    "DisassociateResolverEndpointIpAddressResponseTypeDef",
    {
        "ResolverEndpoint": "ResolverEndpointTypeDef",
    },
    total=False,
)

DisassociateResolverQueryLogConfigResponseTypeDef = TypedDict(
    "DisassociateResolverQueryLogConfigResponseTypeDef",
    {
        "ResolverQueryLogConfigAssociation": "ResolverQueryLogConfigAssociationTypeDef",
    },
    total=False,
)

DisassociateResolverRuleResponseTypeDef = TypedDict(
    "DisassociateResolverRuleResponseTypeDef",
    {
        "ResolverRuleAssociation": "ResolverRuleAssociationTypeDef",
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
    total=False,
)

FirewallConfigTypeDef = TypedDict(
    "FirewallConfigTypeDef",
    {
        "Id": str,
        "ResourceId": str,
        "OwnerId": str,
        "FirewallFailOpen": FirewallFailOpenStatusType,
    },
    total=False,
)

FirewallDomainListMetadataTypeDef = TypedDict(
    "FirewallDomainListMetadataTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "CreatorRequestId": str,
        "ManagedOwnerName": str,
    },
    total=False,
)

FirewallDomainListTypeDef = TypedDict(
    "FirewallDomainListTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "DomainCount": int,
        "Status": FirewallDomainListStatusType,
        "StatusMessage": str,
        "ManagedOwnerName": str,
        "CreatorRequestId": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)

FirewallRuleGroupAssociationTypeDef = TypedDict(
    "FirewallRuleGroupAssociationTypeDef",
    {
        "Id": str,
        "Arn": str,
        "FirewallRuleGroupId": str,
        "VpcId": str,
        "Name": str,
        "Priority": int,
        "MutationProtection": MutationProtectionStatusType,
        "ManagedOwnerName": str,
        "Status": FirewallRuleGroupAssociationStatusType,
        "StatusMessage": str,
        "CreatorRequestId": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)

FirewallRuleGroupMetadataTypeDef = TypedDict(
    "FirewallRuleGroupMetadataTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "OwnerId": str,
        "CreatorRequestId": str,
        "ShareStatus": ShareStatusType,
    },
    total=False,
)

FirewallRuleGroupTypeDef = TypedDict(
    "FirewallRuleGroupTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "RuleCount": int,
        "Status": FirewallRuleGroupStatusType,
        "StatusMessage": str,
        "OwnerId": str,
        "CreatorRequestId": str,
        "ShareStatus": ShareStatusType,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)

FirewallRuleTypeDef = TypedDict(
    "FirewallRuleTypeDef",
    {
        "FirewallRuleGroupId": str,
        "FirewallDomainListId": str,
        "Name": str,
        "Priority": int,
        "Action": ActionType,
        "BlockResponse": BlockResponseType,
        "BlockOverrideDomain": str,
        "BlockOverrideDnsType": Literal["CNAME"],
        "BlockOverrideTtl": int,
        "CreatorRequestId": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)

GetFirewallConfigResponseTypeDef = TypedDict(
    "GetFirewallConfigResponseTypeDef",
    {
        "FirewallConfig": "FirewallConfigTypeDef",
    },
    total=False,
)

GetFirewallDomainListResponseTypeDef = TypedDict(
    "GetFirewallDomainListResponseTypeDef",
    {
        "FirewallDomainList": "FirewallDomainListTypeDef",
    },
    total=False,
)

GetFirewallRuleGroupAssociationResponseTypeDef = TypedDict(
    "GetFirewallRuleGroupAssociationResponseTypeDef",
    {
        "FirewallRuleGroupAssociation": "FirewallRuleGroupAssociationTypeDef",
    },
    total=False,
)

GetFirewallRuleGroupPolicyResponseTypeDef = TypedDict(
    "GetFirewallRuleGroupPolicyResponseTypeDef",
    {
        "FirewallRuleGroupPolicy": str,
    },
    total=False,
)

GetFirewallRuleGroupResponseTypeDef = TypedDict(
    "GetFirewallRuleGroupResponseTypeDef",
    {
        "FirewallRuleGroup": "FirewallRuleGroupTypeDef",
    },
    total=False,
)

GetResolverDnssecConfigResponseTypeDef = TypedDict(
    "GetResolverDnssecConfigResponseTypeDef",
    {
        "ResolverDNSSECConfig": "ResolverDnssecConfigTypeDef",
    },
    total=False,
)

GetResolverEndpointResponseTypeDef = TypedDict(
    "GetResolverEndpointResponseTypeDef",
    {
        "ResolverEndpoint": "ResolverEndpointTypeDef",
    },
    total=False,
)

GetResolverQueryLogConfigAssociationResponseTypeDef = TypedDict(
    "GetResolverQueryLogConfigAssociationResponseTypeDef",
    {
        "ResolverQueryLogConfigAssociation": "ResolverQueryLogConfigAssociationTypeDef",
    },
    total=False,
)

GetResolverQueryLogConfigPolicyResponseTypeDef = TypedDict(
    "GetResolverQueryLogConfigPolicyResponseTypeDef",
    {
        "ResolverQueryLogConfigPolicy": str,
    },
    total=False,
)

GetResolverQueryLogConfigResponseTypeDef = TypedDict(
    "GetResolverQueryLogConfigResponseTypeDef",
    {
        "ResolverQueryLogConfig": "ResolverQueryLogConfigTypeDef",
    },
    total=False,
)

GetResolverRuleAssociationResponseTypeDef = TypedDict(
    "GetResolverRuleAssociationResponseTypeDef",
    {
        "ResolverRuleAssociation": "ResolverRuleAssociationTypeDef",
    },
    total=False,
)

GetResolverRulePolicyResponseTypeDef = TypedDict(
    "GetResolverRulePolicyResponseTypeDef",
    {
        "ResolverRulePolicy": str,
    },
    total=False,
)

GetResolverRuleResponseTypeDef = TypedDict(
    "GetResolverRuleResponseTypeDef",
    {
        "ResolverRule": "ResolverRuleTypeDef",
    },
    total=False,
)

ImportFirewallDomainsResponseTypeDef = TypedDict(
    "ImportFirewallDomainsResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": FirewallDomainListStatusType,
        "StatusMessage": str,
    },
    total=False,
)

_RequiredIpAddressRequestTypeDef = TypedDict(
    "_RequiredIpAddressRequestTypeDef",
    {
        "SubnetId": str,
    },
)
_OptionalIpAddressRequestTypeDef = TypedDict(
    "_OptionalIpAddressRequestTypeDef",
    {
        "Ip": str,
    },
    total=False,
)


class IpAddressRequestTypeDef(_RequiredIpAddressRequestTypeDef, _OptionalIpAddressRequestTypeDef):
    pass


IpAddressResponseTypeDef = TypedDict(
    "IpAddressResponseTypeDef",
    {
        "IpId": str,
        "SubnetId": str,
        "Ip": str,
        "Status": IpAddressStatusType,
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)

IpAddressUpdateTypeDef = TypedDict(
    "IpAddressUpdateTypeDef",
    {
        "IpId": str,
        "SubnetId": str,
        "Ip": str,
    },
    total=False,
)

ListFirewallConfigsResponseTypeDef = TypedDict(
    "ListFirewallConfigsResponseTypeDef",
    {
        "NextToken": str,
        "FirewallConfigs": List["FirewallConfigTypeDef"],
    },
    total=False,
)

ListFirewallDomainListsResponseTypeDef = TypedDict(
    "ListFirewallDomainListsResponseTypeDef",
    {
        "NextToken": str,
        "FirewallDomainLists": List["FirewallDomainListMetadataTypeDef"],
    },
    total=False,
)

ListFirewallDomainsResponseTypeDef = TypedDict(
    "ListFirewallDomainsResponseTypeDef",
    {
        "NextToken": str,
        "Domains": List[str],
    },
    total=False,
)

ListFirewallRuleGroupAssociationsResponseTypeDef = TypedDict(
    "ListFirewallRuleGroupAssociationsResponseTypeDef",
    {
        "NextToken": str,
        "FirewallRuleGroupAssociations": List["FirewallRuleGroupAssociationTypeDef"],
    },
    total=False,
)

ListFirewallRuleGroupsResponseTypeDef = TypedDict(
    "ListFirewallRuleGroupsResponseTypeDef",
    {
        "NextToken": str,
        "FirewallRuleGroups": List["FirewallRuleGroupMetadataTypeDef"],
    },
    total=False,
)

ListFirewallRulesResponseTypeDef = TypedDict(
    "ListFirewallRulesResponseTypeDef",
    {
        "NextToken": str,
        "FirewallRules": List["FirewallRuleTypeDef"],
    },
    total=False,
)

ListResolverDnssecConfigsResponseTypeDef = TypedDict(
    "ListResolverDnssecConfigsResponseTypeDef",
    {
        "NextToken": str,
        "ResolverDnssecConfigs": List["ResolverDnssecConfigTypeDef"],
    },
    total=False,
)

ListResolverEndpointIpAddressesResponseTypeDef = TypedDict(
    "ListResolverEndpointIpAddressesResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "IpAddresses": List["IpAddressResponseTypeDef"],
    },
    total=False,
)

ListResolverEndpointsResponseTypeDef = TypedDict(
    "ListResolverEndpointsResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResolverEndpoints": List["ResolverEndpointTypeDef"],
    },
    total=False,
)

ListResolverQueryLogConfigAssociationsResponseTypeDef = TypedDict(
    "ListResolverQueryLogConfigAssociationsResponseTypeDef",
    {
        "NextToken": str,
        "TotalCount": int,
        "TotalFilteredCount": int,
        "ResolverQueryLogConfigAssociations": List["ResolverQueryLogConfigAssociationTypeDef"],
    },
    total=False,
)

ListResolverQueryLogConfigsResponseTypeDef = TypedDict(
    "ListResolverQueryLogConfigsResponseTypeDef",
    {
        "NextToken": str,
        "TotalCount": int,
        "TotalFilteredCount": int,
        "ResolverQueryLogConfigs": List["ResolverQueryLogConfigTypeDef"],
    },
    total=False,
)

ListResolverRuleAssociationsResponseTypeDef = TypedDict(
    "ListResolverRuleAssociationsResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResolverRuleAssociations": List["ResolverRuleAssociationTypeDef"],
    },
    total=False,
)

ListResolverRulesResponseTypeDef = TypedDict(
    "ListResolverRulesResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResolverRules": List["ResolverRuleTypeDef"],
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
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

PutFirewallRuleGroupPolicyResponseTypeDef = TypedDict(
    "PutFirewallRuleGroupPolicyResponseTypeDef",
    {
        "ReturnValue": bool,
    },
    total=False,
)

PutResolverQueryLogConfigPolicyResponseTypeDef = TypedDict(
    "PutResolverQueryLogConfigPolicyResponseTypeDef",
    {
        "ReturnValue": bool,
    },
    total=False,
)

PutResolverRulePolicyResponseTypeDef = TypedDict(
    "PutResolverRulePolicyResponseTypeDef",
    {
        "ReturnValue": bool,
    },
    total=False,
)

ResolverDnssecConfigTypeDef = TypedDict(
    "ResolverDnssecConfigTypeDef",
    {
        "Id": str,
        "OwnerId": str,
        "ResourceId": str,
        "ValidationStatus": ResolverDNSSECValidationStatusType,
    },
    total=False,
)

ResolverEndpointTypeDef = TypedDict(
    "ResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": ResolverEndpointDirectionType,
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": ResolverEndpointStatusType,
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)

ResolverQueryLogConfigAssociationTypeDef = TypedDict(
    "ResolverQueryLogConfigAssociationTypeDef",
    {
        "Id": str,
        "ResolverQueryLogConfigId": str,
        "ResourceId": str,
        "Status": ResolverQueryLogConfigAssociationStatusType,
        "Error": ResolverQueryLogConfigAssociationErrorType,
        "ErrorMessage": str,
        "CreationTime": str,
    },
    total=False,
)

ResolverQueryLogConfigTypeDef = TypedDict(
    "ResolverQueryLogConfigTypeDef",
    {
        "Id": str,
        "OwnerId": str,
        "Status": ResolverQueryLogConfigStatusType,
        "ShareStatus": ShareStatusType,
        "AssociationCount": int,
        "Arn": str,
        "Name": str,
        "DestinationArn": str,
        "CreatorRequestId": str,
        "CreationTime": str,
    },
    total=False,
)

ResolverRuleAssociationTypeDef = TypedDict(
    "ResolverRuleAssociationTypeDef",
    {
        "Id": str,
        "ResolverRuleId": str,
        "Name": str,
        "VPCId": str,
        "Status": ResolverRuleAssociationStatusType,
        "StatusMessage": str,
    },
    total=False,
)

ResolverRuleConfigTypeDef = TypedDict(
    "ResolverRuleConfigTypeDef",
    {
        "Name": str,
        "TargetIps": List["TargetAddressTypeDef"],
        "ResolverEndpointId": str,
    },
    total=False,
)

ResolverRuleTypeDef = TypedDict(
    "ResolverRuleTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "DomainName": str,
        "Status": ResolverRuleStatusType,
        "StatusMessage": str,
        "RuleType": RuleTypeOptionType,
        "Name": str,
        "TargetIps": List["TargetAddressTypeDef"],
        "ResolverEndpointId": str,
        "OwnerId": str,
        "ShareStatus": ShareStatusType,
        "CreationTime": str,
        "ModificationTime": str,
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

_RequiredTargetAddressTypeDef = TypedDict(
    "_RequiredTargetAddressTypeDef",
    {
        "Ip": str,
    },
)
_OptionalTargetAddressTypeDef = TypedDict(
    "_OptionalTargetAddressTypeDef",
    {
        "Port": int,
    },
    total=False,
)


class TargetAddressTypeDef(_RequiredTargetAddressTypeDef, _OptionalTargetAddressTypeDef):
    pass


UpdateFirewallConfigResponseTypeDef = TypedDict(
    "UpdateFirewallConfigResponseTypeDef",
    {
        "FirewallConfig": "FirewallConfigTypeDef",
    },
    total=False,
)

UpdateFirewallDomainsResponseTypeDef = TypedDict(
    "UpdateFirewallDomainsResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": FirewallDomainListStatusType,
        "StatusMessage": str,
    },
    total=False,
)

UpdateFirewallRuleGroupAssociationResponseTypeDef = TypedDict(
    "UpdateFirewallRuleGroupAssociationResponseTypeDef",
    {
        "FirewallRuleGroupAssociation": "FirewallRuleGroupAssociationTypeDef",
    },
    total=False,
)

UpdateFirewallRuleResponseTypeDef = TypedDict(
    "UpdateFirewallRuleResponseTypeDef",
    {
        "FirewallRule": "FirewallRuleTypeDef",
    },
    total=False,
)

UpdateResolverDnssecConfigResponseTypeDef = TypedDict(
    "UpdateResolverDnssecConfigResponseTypeDef",
    {
        "ResolverDNSSECConfig": "ResolverDnssecConfigTypeDef",
    },
    total=False,
)

UpdateResolverEndpointResponseTypeDef = TypedDict(
    "UpdateResolverEndpointResponseTypeDef",
    {
        "ResolverEndpoint": "ResolverEndpointTypeDef",
    },
    total=False,
)

UpdateResolverRuleResponseTypeDef = TypedDict(
    "UpdateResolverRuleResponseTypeDef",
    {
        "ResolverRule": "ResolverRuleTypeDef",
    },
    total=False,
)
