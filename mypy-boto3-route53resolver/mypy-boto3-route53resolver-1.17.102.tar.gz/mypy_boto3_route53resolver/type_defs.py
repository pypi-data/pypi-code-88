"""
Type annotations for route53resolver service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/type_defs.html)

Usage::

    ```python
    from mypy_boto3_route53resolver.type_defs import AssociateFirewallRuleGroupRequestTypeDef

    data: AssociateFirewallRuleGroupRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    ActionType,
    BlockResponseType,
    FirewallDomainListStatusType,
    FirewallDomainUpdateOperationType,
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
    SortOrderType,
    ValidationType,
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
    "AssociateFirewallRuleGroupRequestTypeDef",
    "AssociateFirewallRuleGroupResponseResponseTypeDef",
    "AssociateResolverEndpointIpAddressRequestTypeDef",
    "AssociateResolverEndpointIpAddressResponseResponseTypeDef",
    "AssociateResolverQueryLogConfigRequestTypeDef",
    "AssociateResolverQueryLogConfigResponseResponseTypeDef",
    "AssociateResolverRuleRequestTypeDef",
    "AssociateResolverRuleResponseResponseTypeDef",
    "CreateFirewallDomainListRequestTypeDef",
    "CreateFirewallDomainListResponseResponseTypeDef",
    "CreateFirewallRuleGroupRequestTypeDef",
    "CreateFirewallRuleGroupResponseResponseTypeDef",
    "CreateFirewallRuleRequestTypeDef",
    "CreateFirewallRuleResponseResponseTypeDef",
    "CreateResolverEndpointRequestTypeDef",
    "CreateResolverEndpointResponseResponseTypeDef",
    "CreateResolverQueryLogConfigRequestTypeDef",
    "CreateResolverQueryLogConfigResponseResponseTypeDef",
    "CreateResolverRuleRequestTypeDef",
    "CreateResolverRuleResponseResponseTypeDef",
    "DeleteFirewallDomainListRequestTypeDef",
    "DeleteFirewallDomainListResponseResponseTypeDef",
    "DeleteFirewallRuleGroupRequestTypeDef",
    "DeleteFirewallRuleGroupResponseResponseTypeDef",
    "DeleteFirewallRuleRequestTypeDef",
    "DeleteFirewallRuleResponseResponseTypeDef",
    "DeleteResolverEndpointRequestTypeDef",
    "DeleteResolverEndpointResponseResponseTypeDef",
    "DeleteResolverQueryLogConfigRequestTypeDef",
    "DeleteResolverQueryLogConfigResponseResponseTypeDef",
    "DeleteResolverRuleRequestTypeDef",
    "DeleteResolverRuleResponseResponseTypeDef",
    "DisassociateFirewallRuleGroupRequestTypeDef",
    "DisassociateFirewallRuleGroupResponseResponseTypeDef",
    "DisassociateResolverEndpointIpAddressRequestTypeDef",
    "DisassociateResolverEndpointIpAddressResponseResponseTypeDef",
    "DisassociateResolverQueryLogConfigRequestTypeDef",
    "DisassociateResolverQueryLogConfigResponseResponseTypeDef",
    "DisassociateResolverRuleRequestTypeDef",
    "DisassociateResolverRuleResponseResponseTypeDef",
    "FilterTypeDef",
    "FirewallConfigTypeDef",
    "FirewallDomainListMetadataTypeDef",
    "FirewallDomainListTypeDef",
    "FirewallRuleGroupAssociationTypeDef",
    "FirewallRuleGroupMetadataTypeDef",
    "FirewallRuleGroupTypeDef",
    "FirewallRuleTypeDef",
    "GetFirewallConfigRequestTypeDef",
    "GetFirewallConfigResponseResponseTypeDef",
    "GetFirewallDomainListRequestTypeDef",
    "GetFirewallDomainListResponseResponseTypeDef",
    "GetFirewallRuleGroupAssociationRequestTypeDef",
    "GetFirewallRuleGroupAssociationResponseResponseTypeDef",
    "GetFirewallRuleGroupPolicyRequestTypeDef",
    "GetFirewallRuleGroupPolicyResponseResponseTypeDef",
    "GetFirewallRuleGroupRequestTypeDef",
    "GetFirewallRuleGroupResponseResponseTypeDef",
    "GetResolverDnssecConfigRequestTypeDef",
    "GetResolverDnssecConfigResponseResponseTypeDef",
    "GetResolverEndpointRequestTypeDef",
    "GetResolverEndpointResponseResponseTypeDef",
    "GetResolverQueryLogConfigAssociationRequestTypeDef",
    "GetResolverQueryLogConfigAssociationResponseResponseTypeDef",
    "GetResolverQueryLogConfigPolicyRequestTypeDef",
    "GetResolverQueryLogConfigPolicyResponseResponseTypeDef",
    "GetResolverQueryLogConfigRequestTypeDef",
    "GetResolverQueryLogConfigResponseResponseTypeDef",
    "GetResolverRuleAssociationRequestTypeDef",
    "GetResolverRuleAssociationResponseResponseTypeDef",
    "GetResolverRulePolicyRequestTypeDef",
    "GetResolverRulePolicyResponseResponseTypeDef",
    "GetResolverRuleRequestTypeDef",
    "GetResolverRuleResponseResponseTypeDef",
    "ImportFirewallDomainsRequestTypeDef",
    "ImportFirewallDomainsResponseResponseTypeDef",
    "IpAddressRequestTypeDef",
    "IpAddressResponseTypeDef",
    "IpAddressUpdateTypeDef",
    "ListFirewallConfigsRequestTypeDef",
    "ListFirewallConfigsResponseResponseTypeDef",
    "ListFirewallDomainListsRequestTypeDef",
    "ListFirewallDomainListsResponseResponseTypeDef",
    "ListFirewallDomainsRequestTypeDef",
    "ListFirewallDomainsResponseResponseTypeDef",
    "ListFirewallRuleGroupAssociationsRequestTypeDef",
    "ListFirewallRuleGroupAssociationsResponseResponseTypeDef",
    "ListFirewallRuleGroupsRequestTypeDef",
    "ListFirewallRuleGroupsResponseResponseTypeDef",
    "ListFirewallRulesRequestTypeDef",
    "ListFirewallRulesResponseResponseTypeDef",
    "ListResolverDnssecConfigsRequestTypeDef",
    "ListResolverDnssecConfigsResponseResponseTypeDef",
    "ListResolverEndpointIpAddressesRequestTypeDef",
    "ListResolverEndpointIpAddressesResponseResponseTypeDef",
    "ListResolverEndpointsRequestTypeDef",
    "ListResolverEndpointsResponseResponseTypeDef",
    "ListResolverQueryLogConfigAssociationsRequestTypeDef",
    "ListResolverQueryLogConfigAssociationsResponseResponseTypeDef",
    "ListResolverQueryLogConfigsRequestTypeDef",
    "ListResolverQueryLogConfigsResponseResponseTypeDef",
    "ListResolverRuleAssociationsRequestTypeDef",
    "ListResolverRuleAssociationsResponseResponseTypeDef",
    "ListResolverRulesRequestTypeDef",
    "ListResolverRulesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutFirewallRuleGroupPolicyRequestTypeDef",
    "PutFirewallRuleGroupPolicyResponseResponseTypeDef",
    "PutResolverQueryLogConfigPolicyRequestTypeDef",
    "PutResolverQueryLogConfigPolicyResponseResponseTypeDef",
    "PutResolverRulePolicyRequestTypeDef",
    "PutResolverRulePolicyResponseResponseTypeDef",
    "ResolverDnssecConfigTypeDef",
    "ResolverEndpointTypeDef",
    "ResolverQueryLogConfigAssociationTypeDef",
    "ResolverQueryLogConfigTypeDef",
    "ResolverRuleAssociationTypeDef",
    "ResolverRuleConfigTypeDef",
    "ResolverRuleTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TargetAddressTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateFirewallConfigRequestTypeDef",
    "UpdateFirewallConfigResponseResponseTypeDef",
    "UpdateFirewallDomainsRequestTypeDef",
    "UpdateFirewallDomainsResponseResponseTypeDef",
    "UpdateFirewallRuleGroupAssociationRequestTypeDef",
    "UpdateFirewallRuleGroupAssociationResponseResponseTypeDef",
    "UpdateFirewallRuleRequestTypeDef",
    "UpdateFirewallRuleResponseResponseTypeDef",
    "UpdateResolverDnssecConfigRequestTypeDef",
    "UpdateResolverDnssecConfigResponseResponseTypeDef",
    "UpdateResolverEndpointRequestTypeDef",
    "UpdateResolverEndpointResponseResponseTypeDef",
    "UpdateResolverRuleRequestTypeDef",
    "UpdateResolverRuleResponseResponseTypeDef",
)

_RequiredAssociateFirewallRuleGroupRequestTypeDef = TypedDict(
    "_RequiredAssociateFirewallRuleGroupRequestTypeDef",
    {
        "CreatorRequestId": str,
        "FirewallRuleGroupId": str,
        "VpcId": str,
        "Priority": int,
        "Name": str,
    },
)
_OptionalAssociateFirewallRuleGroupRequestTypeDef = TypedDict(
    "_OptionalAssociateFirewallRuleGroupRequestTypeDef",
    {
        "MutationProtection": MutationProtectionStatusType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class AssociateFirewallRuleGroupRequestTypeDef(
    _RequiredAssociateFirewallRuleGroupRequestTypeDef,
    _OptionalAssociateFirewallRuleGroupRequestTypeDef,
):
    pass


AssociateFirewallRuleGroupResponseResponseTypeDef = TypedDict(
    "AssociateFirewallRuleGroupResponseResponseTypeDef",
    {
        "FirewallRuleGroupAssociation": "FirewallRuleGroupAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateResolverEndpointIpAddressRequestTypeDef = TypedDict(
    "AssociateResolverEndpointIpAddressRequestTypeDef",
    {
        "ResolverEndpointId": str,
        "IpAddress": "IpAddressUpdateTypeDef",
    },
)

AssociateResolverEndpointIpAddressResponseResponseTypeDef = TypedDict(
    "AssociateResolverEndpointIpAddressResponseResponseTypeDef",
    {
        "ResolverEndpoint": "ResolverEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateResolverQueryLogConfigRequestTypeDef = TypedDict(
    "AssociateResolverQueryLogConfigRequestTypeDef",
    {
        "ResolverQueryLogConfigId": str,
        "ResourceId": str,
    },
)

AssociateResolverQueryLogConfigResponseResponseTypeDef = TypedDict(
    "AssociateResolverQueryLogConfigResponseResponseTypeDef",
    {
        "ResolverQueryLogConfigAssociation": "ResolverQueryLogConfigAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateResolverRuleRequestTypeDef = TypedDict(
    "_RequiredAssociateResolverRuleRequestTypeDef",
    {
        "ResolverRuleId": str,
        "VPCId": str,
    },
)
_OptionalAssociateResolverRuleRequestTypeDef = TypedDict(
    "_OptionalAssociateResolverRuleRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class AssociateResolverRuleRequestTypeDef(
    _RequiredAssociateResolverRuleRequestTypeDef, _OptionalAssociateResolverRuleRequestTypeDef
):
    pass


AssociateResolverRuleResponseResponseTypeDef = TypedDict(
    "AssociateResolverRuleResponseResponseTypeDef",
    {
        "ResolverRuleAssociation": "ResolverRuleAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFirewallDomainListRequestTypeDef = TypedDict(
    "_RequiredCreateFirewallDomainListRequestTypeDef",
    {
        "CreatorRequestId": str,
        "Name": str,
    },
)
_OptionalCreateFirewallDomainListRequestTypeDef = TypedDict(
    "_OptionalCreateFirewallDomainListRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateFirewallDomainListRequestTypeDef(
    _RequiredCreateFirewallDomainListRequestTypeDef, _OptionalCreateFirewallDomainListRequestTypeDef
):
    pass


CreateFirewallDomainListResponseResponseTypeDef = TypedDict(
    "CreateFirewallDomainListResponseResponseTypeDef",
    {
        "FirewallDomainList": "FirewallDomainListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFirewallRuleGroupRequestTypeDef = TypedDict(
    "_RequiredCreateFirewallRuleGroupRequestTypeDef",
    {
        "CreatorRequestId": str,
        "Name": str,
    },
)
_OptionalCreateFirewallRuleGroupRequestTypeDef = TypedDict(
    "_OptionalCreateFirewallRuleGroupRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateFirewallRuleGroupRequestTypeDef(
    _RequiredCreateFirewallRuleGroupRequestTypeDef, _OptionalCreateFirewallRuleGroupRequestTypeDef
):
    pass


CreateFirewallRuleGroupResponseResponseTypeDef = TypedDict(
    "CreateFirewallRuleGroupResponseResponseTypeDef",
    {
        "FirewallRuleGroup": "FirewallRuleGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFirewallRuleRequestTypeDef = TypedDict(
    "_RequiredCreateFirewallRuleRequestTypeDef",
    {
        "CreatorRequestId": str,
        "FirewallRuleGroupId": str,
        "FirewallDomainListId": str,
        "Priority": int,
        "Action": ActionType,
        "Name": str,
    },
)
_OptionalCreateFirewallRuleRequestTypeDef = TypedDict(
    "_OptionalCreateFirewallRuleRequestTypeDef",
    {
        "BlockResponse": BlockResponseType,
        "BlockOverrideDomain": str,
        "BlockOverrideDnsType": Literal["CNAME"],
        "BlockOverrideTtl": int,
    },
    total=False,
)


class CreateFirewallRuleRequestTypeDef(
    _RequiredCreateFirewallRuleRequestTypeDef, _OptionalCreateFirewallRuleRequestTypeDef
):
    pass


CreateFirewallRuleResponseResponseTypeDef = TypedDict(
    "CreateFirewallRuleResponseResponseTypeDef",
    {
        "FirewallRule": "FirewallRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResolverEndpointRequestTypeDef = TypedDict(
    "_RequiredCreateResolverEndpointRequestTypeDef",
    {
        "CreatorRequestId": str,
        "SecurityGroupIds": List[str],
        "Direction": ResolverEndpointDirectionType,
        "IpAddresses": List["IpAddressRequestTypeDef"],
    },
)
_OptionalCreateResolverEndpointRequestTypeDef = TypedDict(
    "_OptionalCreateResolverEndpointRequestTypeDef",
    {
        "Name": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateResolverEndpointRequestTypeDef(
    _RequiredCreateResolverEndpointRequestTypeDef, _OptionalCreateResolverEndpointRequestTypeDef
):
    pass


CreateResolverEndpointResponseResponseTypeDef = TypedDict(
    "CreateResolverEndpointResponseResponseTypeDef",
    {
        "ResolverEndpoint": "ResolverEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResolverQueryLogConfigRequestTypeDef = TypedDict(
    "_RequiredCreateResolverQueryLogConfigRequestTypeDef",
    {
        "Name": str,
        "DestinationArn": str,
        "CreatorRequestId": str,
    },
)
_OptionalCreateResolverQueryLogConfigRequestTypeDef = TypedDict(
    "_OptionalCreateResolverQueryLogConfigRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateResolverQueryLogConfigRequestTypeDef(
    _RequiredCreateResolverQueryLogConfigRequestTypeDef,
    _OptionalCreateResolverQueryLogConfigRequestTypeDef,
):
    pass


CreateResolverQueryLogConfigResponseResponseTypeDef = TypedDict(
    "CreateResolverQueryLogConfigResponseResponseTypeDef",
    {
        "ResolverQueryLogConfig": "ResolverQueryLogConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResolverRuleRequestTypeDef = TypedDict(
    "_RequiredCreateResolverRuleRequestTypeDef",
    {
        "CreatorRequestId": str,
        "RuleType": RuleTypeOptionType,
        "DomainName": str,
    },
)
_OptionalCreateResolverRuleRequestTypeDef = TypedDict(
    "_OptionalCreateResolverRuleRequestTypeDef",
    {
        "Name": str,
        "TargetIps": List["TargetAddressTypeDef"],
        "ResolverEndpointId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateResolverRuleRequestTypeDef(
    _RequiredCreateResolverRuleRequestTypeDef, _OptionalCreateResolverRuleRequestTypeDef
):
    pass


CreateResolverRuleResponseResponseTypeDef = TypedDict(
    "CreateResolverRuleResponseResponseTypeDef",
    {
        "ResolverRule": "ResolverRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFirewallDomainListRequestTypeDef = TypedDict(
    "DeleteFirewallDomainListRequestTypeDef",
    {
        "FirewallDomainListId": str,
    },
)

DeleteFirewallDomainListResponseResponseTypeDef = TypedDict(
    "DeleteFirewallDomainListResponseResponseTypeDef",
    {
        "FirewallDomainList": "FirewallDomainListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFirewallRuleGroupRequestTypeDef = TypedDict(
    "DeleteFirewallRuleGroupRequestTypeDef",
    {
        "FirewallRuleGroupId": str,
    },
)

DeleteFirewallRuleGroupResponseResponseTypeDef = TypedDict(
    "DeleteFirewallRuleGroupResponseResponseTypeDef",
    {
        "FirewallRuleGroup": "FirewallRuleGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFirewallRuleRequestTypeDef = TypedDict(
    "DeleteFirewallRuleRequestTypeDef",
    {
        "FirewallRuleGroupId": str,
        "FirewallDomainListId": str,
    },
)

DeleteFirewallRuleResponseResponseTypeDef = TypedDict(
    "DeleteFirewallRuleResponseResponseTypeDef",
    {
        "FirewallRule": "FirewallRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResolverEndpointRequestTypeDef = TypedDict(
    "DeleteResolverEndpointRequestTypeDef",
    {
        "ResolverEndpointId": str,
    },
)

DeleteResolverEndpointResponseResponseTypeDef = TypedDict(
    "DeleteResolverEndpointResponseResponseTypeDef",
    {
        "ResolverEndpoint": "ResolverEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResolverQueryLogConfigRequestTypeDef = TypedDict(
    "DeleteResolverQueryLogConfigRequestTypeDef",
    {
        "ResolverQueryLogConfigId": str,
    },
)

DeleteResolverQueryLogConfigResponseResponseTypeDef = TypedDict(
    "DeleteResolverQueryLogConfigResponseResponseTypeDef",
    {
        "ResolverQueryLogConfig": "ResolverQueryLogConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResolverRuleRequestTypeDef = TypedDict(
    "DeleteResolverRuleRequestTypeDef",
    {
        "ResolverRuleId": str,
    },
)

DeleteResolverRuleResponseResponseTypeDef = TypedDict(
    "DeleteResolverRuleResponseResponseTypeDef",
    {
        "ResolverRule": "ResolverRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateFirewallRuleGroupRequestTypeDef = TypedDict(
    "DisassociateFirewallRuleGroupRequestTypeDef",
    {
        "FirewallRuleGroupAssociationId": str,
    },
)

DisassociateFirewallRuleGroupResponseResponseTypeDef = TypedDict(
    "DisassociateFirewallRuleGroupResponseResponseTypeDef",
    {
        "FirewallRuleGroupAssociation": "FirewallRuleGroupAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateResolverEndpointIpAddressRequestTypeDef = TypedDict(
    "DisassociateResolverEndpointIpAddressRequestTypeDef",
    {
        "ResolverEndpointId": str,
        "IpAddress": "IpAddressUpdateTypeDef",
    },
)

DisassociateResolverEndpointIpAddressResponseResponseTypeDef = TypedDict(
    "DisassociateResolverEndpointIpAddressResponseResponseTypeDef",
    {
        "ResolverEndpoint": "ResolverEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateResolverQueryLogConfigRequestTypeDef = TypedDict(
    "DisassociateResolverQueryLogConfigRequestTypeDef",
    {
        "ResolverQueryLogConfigId": str,
        "ResourceId": str,
    },
)

DisassociateResolverQueryLogConfigResponseResponseTypeDef = TypedDict(
    "DisassociateResolverQueryLogConfigResponseResponseTypeDef",
    {
        "ResolverQueryLogConfigAssociation": "ResolverQueryLogConfigAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateResolverRuleRequestTypeDef = TypedDict(
    "DisassociateResolverRuleRequestTypeDef",
    {
        "VPCId": str,
        "ResolverRuleId": str,
    },
)

DisassociateResolverRuleResponseResponseTypeDef = TypedDict(
    "DisassociateResolverRuleResponseResponseTypeDef",
    {
        "ResolverRuleAssociation": "ResolverRuleAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

GetFirewallConfigRequestTypeDef = TypedDict(
    "GetFirewallConfigRequestTypeDef",
    {
        "ResourceId": str,
    },
)

GetFirewallConfigResponseResponseTypeDef = TypedDict(
    "GetFirewallConfigResponseResponseTypeDef",
    {
        "FirewallConfig": "FirewallConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFirewallDomainListRequestTypeDef = TypedDict(
    "GetFirewallDomainListRequestTypeDef",
    {
        "FirewallDomainListId": str,
    },
)

GetFirewallDomainListResponseResponseTypeDef = TypedDict(
    "GetFirewallDomainListResponseResponseTypeDef",
    {
        "FirewallDomainList": "FirewallDomainListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFirewallRuleGroupAssociationRequestTypeDef = TypedDict(
    "GetFirewallRuleGroupAssociationRequestTypeDef",
    {
        "FirewallRuleGroupAssociationId": str,
    },
)

GetFirewallRuleGroupAssociationResponseResponseTypeDef = TypedDict(
    "GetFirewallRuleGroupAssociationResponseResponseTypeDef",
    {
        "FirewallRuleGroupAssociation": "FirewallRuleGroupAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFirewallRuleGroupPolicyRequestTypeDef = TypedDict(
    "GetFirewallRuleGroupPolicyRequestTypeDef",
    {
        "Arn": str,
    },
)

GetFirewallRuleGroupPolicyResponseResponseTypeDef = TypedDict(
    "GetFirewallRuleGroupPolicyResponseResponseTypeDef",
    {
        "FirewallRuleGroupPolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFirewallRuleGroupRequestTypeDef = TypedDict(
    "GetFirewallRuleGroupRequestTypeDef",
    {
        "FirewallRuleGroupId": str,
    },
)

GetFirewallRuleGroupResponseResponseTypeDef = TypedDict(
    "GetFirewallRuleGroupResponseResponseTypeDef",
    {
        "FirewallRuleGroup": "FirewallRuleGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverDnssecConfigRequestTypeDef = TypedDict(
    "GetResolverDnssecConfigRequestTypeDef",
    {
        "ResourceId": str,
    },
)

GetResolverDnssecConfigResponseResponseTypeDef = TypedDict(
    "GetResolverDnssecConfigResponseResponseTypeDef",
    {
        "ResolverDNSSECConfig": "ResolverDnssecConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverEndpointRequestTypeDef = TypedDict(
    "GetResolverEndpointRequestTypeDef",
    {
        "ResolverEndpointId": str,
    },
)

GetResolverEndpointResponseResponseTypeDef = TypedDict(
    "GetResolverEndpointResponseResponseTypeDef",
    {
        "ResolverEndpoint": "ResolverEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverQueryLogConfigAssociationRequestTypeDef = TypedDict(
    "GetResolverQueryLogConfigAssociationRequestTypeDef",
    {
        "ResolverQueryLogConfigAssociationId": str,
    },
)

GetResolverQueryLogConfigAssociationResponseResponseTypeDef = TypedDict(
    "GetResolverQueryLogConfigAssociationResponseResponseTypeDef",
    {
        "ResolverQueryLogConfigAssociation": "ResolverQueryLogConfigAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverQueryLogConfigPolicyRequestTypeDef = TypedDict(
    "GetResolverQueryLogConfigPolicyRequestTypeDef",
    {
        "Arn": str,
    },
)

GetResolverQueryLogConfigPolicyResponseResponseTypeDef = TypedDict(
    "GetResolverQueryLogConfigPolicyResponseResponseTypeDef",
    {
        "ResolverQueryLogConfigPolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverQueryLogConfigRequestTypeDef = TypedDict(
    "GetResolverQueryLogConfigRequestTypeDef",
    {
        "ResolverQueryLogConfigId": str,
    },
)

GetResolverQueryLogConfigResponseResponseTypeDef = TypedDict(
    "GetResolverQueryLogConfigResponseResponseTypeDef",
    {
        "ResolverQueryLogConfig": "ResolverQueryLogConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverRuleAssociationRequestTypeDef = TypedDict(
    "GetResolverRuleAssociationRequestTypeDef",
    {
        "ResolverRuleAssociationId": str,
    },
)

GetResolverRuleAssociationResponseResponseTypeDef = TypedDict(
    "GetResolverRuleAssociationResponseResponseTypeDef",
    {
        "ResolverRuleAssociation": "ResolverRuleAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverRulePolicyRequestTypeDef = TypedDict(
    "GetResolverRulePolicyRequestTypeDef",
    {
        "Arn": str,
    },
)

GetResolverRulePolicyResponseResponseTypeDef = TypedDict(
    "GetResolverRulePolicyResponseResponseTypeDef",
    {
        "ResolverRulePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverRuleRequestTypeDef = TypedDict(
    "GetResolverRuleRequestTypeDef",
    {
        "ResolverRuleId": str,
    },
)

GetResolverRuleResponseResponseTypeDef = TypedDict(
    "GetResolverRuleResponseResponseTypeDef",
    {
        "ResolverRule": "ResolverRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportFirewallDomainsRequestTypeDef = TypedDict(
    "ImportFirewallDomainsRequestTypeDef",
    {
        "FirewallDomainListId": str,
        "Operation": Literal["REPLACE"],
        "DomainFileUrl": str,
    },
)

ImportFirewallDomainsResponseResponseTypeDef = TypedDict(
    "ImportFirewallDomainsResponseResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": FirewallDomainListStatusType,
        "StatusMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ListFirewallConfigsRequestTypeDef = TypedDict(
    "ListFirewallConfigsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListFirewallConfigsResponseResponseTypeDef = TypedDict(
    "ListFirewallConfigsResponseResponseTypeDef",
    {
        "NextToken": str,
        "FirewallConfigs": List["FirewallConfigTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFirewallDomainListsRequestTypeDef = TypedDict(
    "ListFirewallDomainListsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListFirewallDomainListsResponseResponseTypeDef = TypedDict(
    "ListFirewallDomainListsResponseResponseTypeDef",
    {
        "NextToken": str,
        "FirewallDomainLists": List["FirewallDomainListMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFirewallDomainsRequestTypeDef = TypedDict(
    "_RequiredListFirewallDomainsRequestTypeDef",
    {
        "FirewallDomainListId": str,
    },
)
_OptionalListFirewallDomainsRequestTypeDef = TypedDict(
    "_OptionalListFirewallDomainsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListFirewallDomainsRequestTypeDef(
    _RequiredListFirewallDomainsRequestTypeDef, _OptionalListFirewallDomainsRequestTypeDef
):
    pass


ListFirewallDomainsResponseResponseTypeDef = TypedDict(
    "ListFirewallDomainsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Domains": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFirewallRuleGroupAssociationsRequestTypeDef = TypedDict(
    "ListFirewallRuleGroupAssociationsRequestTypeDef",
    {
        "FirewallRuleGroupId": str,
        "VpcId": str,
        "Priority": int,
        "Status": FirewallRuleGroupAssociationStatusType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListFirewallRuleGroupAssociationsResponseResponseTypeDef = TypedDict(
    "ListFirewallRuleGroupAssociationsResponseResponseTypeDef",
    {
        "NextToken": str,
        "FirewallRuleGroupAssociations": List["FirewallRuleGroupAssociationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFirewallRuleGroupsRequestTypeDef = TypedDict(
    "ListFirewallRuleGroupsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListFirewallRuleGroupsResponseResponseTypeDef = TypedDict(
    "ListFirewallRuleGroupsResponseResponseTypeDef",
    {
        "NextToken": str,
        "FirewallRuleGroups": List["FirewallRuleGroupMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFirewallRulesRequestTypeDef = TypedDict(
    "_RequiredListFirewallRulesRequestTypeDef",
    {
        "FirewallRuleGroupId": str,
    },
)
_OptionalListFirewallRulesRequestTypeDef = TypedDict(
    "_OptionalListFirewallRulesRequestTypeDef",
    {
        "Priority": int,
        "Action": ActionType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListFirewallRulesRequestTypeDef(
    _RequiredListFirewallRulesRequestTypeDef, _OptionalListFirewallRulesRequestTypeDef
):
    pass


ListFirewallRulesResponseResponseTypeDef = TypedDict(
    "ListFirewallRulesResponseResponseTypeDef",
    {
        "NextToken": str,
        "FirewallRules": List["FirewallRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResolverDnssecConfigsRequestTypeDef = TypedDict(
    "ListResolverDnssecConfigsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListResolverDnssecConfigsResponseResponseTypeDef = TypedDict(
    "ListResolverDnssecConfigsResponseResponseTypeDef",
    {
        "NextToken": str,
        "ResolverDnssecConfigs": List["ResolverDnssecConfigTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResolverEndpointIpAddressesRequestTypeDef = TypedDict(
    "_RequiredListResolverEndpointIpAddressesRequestTypeDef",
    {
        "ResolverEndpointId": str,
    },
)
_OptionalListResolverEndpointIpAddressesRequestTypeDef = TypedDict(
    "_OptionalListResolverEndpointIpAddressesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListResolverEndpointIpAddressesRequestTypeDef(
    _RequiredListResolverEndpointIpAddressesRequestTypeDef,
    _OptionalListResolverEndpointIpAddressesRequestTypeDef,
):
    pass


ListResolverEndpointIpAddressesResponseResponseTypeDef = TypedDict(
    "ListResolverEndpointIpAddressesResponseResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "IpAddresses": List["IpAddressResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResolverEndpointsRequestTypeDef = TypedDict(
    "ListResolverEndpointsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListResolverEndpointsResponseResponseTypeDef = TypedDict(
    "ListResolverEndpointsResponseResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResolverEndpoints": List["ResolverEndpointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResolverQueryLogConfigAssociationsRequestTypeDef = TypedDict(
    "ListResolverQueryLogConfigAssociationsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
        "SortBy": str,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListResolverQueryLogConfigAssociationsResponseResponseTypeDef = TypedDict(
    "ListResolverQueryLogConfigAssociationsResponseResponseTypeDef",
    {
        "NextToken": str,
        "TotalCount": int,
        "TotalFilteredCount": int,
        "ResolverQueryLogConfigAssociations": List["ResolverQueryLogConfigAssociationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResolverQueryLogConfigsRequestTypeDef = TypedDict(
    "ListResolverQueryLogConfigsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
        "SortBy": str,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListResolverQueryLogConfigsResponseResponseTypeDef = TypedDict(
    "ListResolverQueryLogConfigsResponseResponseTypeDef",
    {
        "NextToken": str,
        "TotalCount": int,
        "TotalFilteredCount": int,
        "ResolverQueryLogConfigs": List["ResolverQueryLogConfigTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResolverRuleAssociationsRequestTypeDef = TypedDict(
    "ListResolverRuleAssociationsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListResolverRuleAssociationsResponseResponseTypeDef = TypedDict(
    "ListResolverRuleAssociationsResponseResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResolverRuleAssociations": List["ResolverRuleAssociationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResolverRulesRequestTypeDef = TypedDict(
    "ListResolverRulesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListResolverRulesResponseResponseTypeDef = TypedDict(
    "ListResolverRulesResponseResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResolverRules": List["ResolverRuleTypeDef"],
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
        "MaxResults": int,
        "NextToken": str,
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
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

PutFirewallRuleGroupPolicyRequestTypeDef = TypedDict(
    "PutFirewallRuleGroupPolicyRequestTypeDef",
    {
        "Arn": str,
        "FirewallRuleGroupPolicy": str,
    },
)

PutFirewallRuleGroupPolicyResponseResponseTypeDef = TypedDict(
    "PutFirewallRuleGroupPolicyResponseResponseTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutResolverQueryLogConfigPolicyRequestTypeDef = TypedDict(
    "PutResolverQueryLogConfigPolicyRequestTypeDef",
    {
        "Arn": str,
        "ResolverQueryLogConfigPolicy": str,
    },
)

PutResolverQueryLogConfigPolicyResponseResponseTypeDef = TypedDict(
    "PutResolverQueryLogConfigPolicyResponseResponseTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutResolverRulePolicyRequestTypeDef = TypedDict(
    "PutResolverRulePolicyRequestTypeDef",
    {
        "Arn": str,
        "ResolverRulePolicy": str,
    },
)

PutResolverRulePolicyResponseResponseTypeDef = TypedDict(
    "PutResolverRulePolicyResponseResponseTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateFirewallConfigRequestTypeDef = TypedDict(
    "UpdateFirewallConfigRequestTypeDef",
    {
        "ResourceId": str,
        "FirewallFailOpen": FirewallFailOpenStatusType,
    },
)

UpdateFirewallConfigResponseResponseTypeDef = TypedDict(
    "UpdateFirewallConfigResponseResponseTypeDef",
    {
        "FirewallConfig": "FirewallConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFirewallDomainsRequestTypeDef = TypedDict(
    "UpdateFirewallDomainsRequestTypeDef",
    {
        "FirewallDomainListId": str,
        "Operation": FirewallDomainUpdateOperationType,
        "Domains": List[str],
    },
)

UpdateFirewallDomainsResponseResponseTypeDef = TypedDict(
    "UpdateFirewallDomainsResponseResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": FirewallDomainListStatusType,
        "StatusMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFirewallRuleGroupAssociationRequestTypeDef = TypedDict(
    "_RequiredUpdateFirewallRuleGroupAssociationRequestTypeDef",
    {
        "FirewallRuleGroupAssociationId": str,
    },
)
_OptionalUpdateFirewallRuleGroupAssociationRequestTypeDef = TypedDict(
    "_OptionalUpdateFirewallRuleGroupAssociationRequestTypeDef",
    {
        "Priority": int,
        "MutationProtection": MutationProtectionStatusType,
        "Name": str,
    },
    total=False,
)


class UpdateFirewallRuleGroupAssociationRequestTypeDef(
    _RequiredUpdateFirewallRuleGroupAssociationRequestTypeDef,
    _OptionalUpdateFirewallRuleGroupAssociationRequestTypeDef,
):
    pass


UpdateFirewallRuleGroupAssociationResponseResponseTypeDef = TypedDict(
    "UpdateFirewallRuleGroupAssociationResponseResponseTypeDef",
    {
        "FirewallRuleGroupAssociation": "FirewallRuleGroupAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFirewallRuleRequestTypeDef = TypedDict(
    "_RequiredUpdateFirewallRuleRequestTypeDef",
    {
        "FirewallRuleGroupId": str,
        "FirewallDomainListId": str,
    },
)
_OptionalUpdateFirewallRuleRequestTypeDef = TypedDict(
    "_OptionalUpdateFirewallRuleRequestTypeDef",
    {
        "Priority": int,
        "Action": ActionType,
        "BlockResponse": BlockResponseType,
        "BlockOverrideDomain": str,
        "BlockOverrideDnsType": Literal["CNAME"],
        "BlockOverrideTtl": int,
        "Name": str,
    },
    total=False,
)


class UpdateFirewallRuleRequestTypeDef(
    _RequiredUpdateFirewallRuleRequestTypeDef, _OptionalUpdateFirewallRuleRequestTypeDef
):
    pass


UpdateFirewallRuleResponseResponseTypeDef = TypedDict(
    "UpdateFirewallRuleResponseResponseTypeDef",
    {
        "FirewallRule": "FirewallRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateResolverDnssecConfigRequestTypeDef = TypedDict(
    "UpdateResolverDnssecConfigRequestTypeDef",
    {
        "ResourceId": str,
        "Validation": ValidationType,
    },
)

UpdateResolverDnssecConfigResponseResponseTypeDef = TypedDict(
    "UpdateResolverDnssecConfigResponseResponseTypeDef",
    {
        "ResolverDNSSECConfig": "ResolverDnssecConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateResolverEndpointRequestTypeDef = TypedDict(
    "_RequiredUpdateResolverEndpointRequestTypeDef",
    {
        "ResolverEndpointId": str,
    },
)
_OptionalUpdateResolverEndpointRequestTypeDef = TypedDict(
    "_OptionalUpdateResolverEndpointRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class UpdateResolverEndpointRequestTypeDef(
    _RequiredUpdateResolverEndpointRequestTypeDef, _OptionalUpdateResolverEndpointRequestTypeDef
):
    pass


UpdateResolverEndpointResponseResponseTypeDef = TypedDict(
    "UpdateResolverEndpointResponseResponseTypeDef",
    {
        "ResolverEndpoint": "ResolverEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateResolverRuleRequestTypeDef = TypedDict(
    "UpdateResolverRuleRequestTypeDef",
    {
        "ResolverRuleId": str,
        "Config": "ResolverRuleConfigTypeDef",
    },
)

UpdateResolverRuleResponseResponseTypeDef = TypedDict(
    "UpdateResolverRuleResponseResponseTypeDef",
    {
        "ResolverRule": "ResolverRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
