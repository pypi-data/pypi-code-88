"""
Type annotations for route53resolver service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_route53resolver import Route53ResolverClient

    client: Route53ResolverClient = boto3.client("route53resolver")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    ActionType,
    BlockResponseType,
    FirewallDomainUpdateOperationType,
    FirewallFailOpenStatusType,
    FirewallRuleGroupAssociationStatusType,
    MutationProtectionStatusType,
    ResolverEndpointDirectionType,
    RuleTypeOptionType,
    SortOrderType,
    ValidationType,
)
from .paginator import (
    ListFirewallConfigsPaginator,
    ListFirewallDomainListsPaginator,
    ListFirewallDomainsPaginator,
    ListFirewallRuleGroupAssociationsPaginator,
    ListFirewallRuleGroupsPaginator,
    ListFirewallRulesPaginator,
    ListResolverDnssecConfigsPaginator,
    ListResolverEndpointIpAddressesPaginator,
    ListResolverEndpointsPaginator,
    ListResolverQueryLogConfigAssociationsPaginator,
    ListResolverQueryLogConfigsPaginator,
    ListResolverRuleAssociationsPaginator,
    ListResolverRulesPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    AssociateFirewallRuleGroupResponseTypeDef,
    AssociateResolverEndpointIpAddressResponseTypeDef,
    AssociateResolverQueryLogConfigResponseTypeDef,
    AssociateResolverRuleResponseTypeDef,
    CreateFirewallDomainListResponseTypeDef,
    CreateFirewallRuleGroupResponseTypeDef,
    CreateFirewallRuleResponseTypeDef,
    CreateResolverEndpointResponseTypeDef,
    CreateResolverQueryLogConfigResponseTypeDef,
    CreateResolverRuleResponseTypeDef,
    DeleteFirewallDomainListResponseTypeDef,
    DeleteFirewallRuleGroupResponseTypeDef,
    DeleteFirewallRuleResponseTypeDef,
    DeleteResolverEndpointResponseTypeDef,
    DeleteResolverQueryLogConfigResponseTypeDef,
    DeleteResolverRuleResponseTypeDef,
    DisassociateFirewallRuleGroupResponseTypeDef,
    DisassociateResolverEndpointIpAddressResponseTypeDef,
    DisassociateResolverQueryLogConfigResponseTypeDef,
    DisassociateResolverRuleResponseTypeDef,
    FilterTypeDef,
    GetFirewallConfigResponseTypeDef,
    GetFirewallDomainListResponseTypeDef,
    GetFirewallRuleGroupAssociationResponseTypeDef,
    GetFirewallRuleGroupPolicyResponseTypeDef,
    GetFirewallRuleGroupResponseTypeDef,
    GetResolverDnssecConfigResponseTypeDef,
    GetResolverEndpointResponseTypeDef,
    GetResolverQueryLogConfigAssociationResponseTypeDef,
    GetResolverQueryLogConfigPolicyResponseTypeDef,
    GetResolverQueryLogConfigResponseTypeDef,
    GetResolverRuleAssociationResponseTypeDef,
    GetResolverRulePolicyResponseTypeDef,
    GetResolverRuleResponseTypeDef,
    ImportFirewallDomainsResponseTypeDef,
    IpAddressRequestTypeDef,
    IpAddressUpdateTypeDef,
    ListFirewallConfigsResponseTypeDef,
    ListFirewallDomainListsResponseTypeDef,
    ListFirewallDomainsResponseTypeDef,
    ListFirewallRuleGroupAssociationsResponseTypeDef,
    ListFirewallRuleGroupsResponseTypeDef,
    ListFirewallRulesResponseTypeDef,
    ListResolverDnssecConfigsResponseTypeDef,
    ListResolverEndpointIpAddressesResponseTypeDef,
    ListResolverEndpointsResponseTypeDef,
    ListResolverQueryLogConfigAssociationsResponseTypeDef,
    ListResolverQueryLogConfigsResponseTypeDef,
    ListResolverRuleAssociationsResponseTypeDef,
    ListResolverRulesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutFirewallRuleGroupPolicyResponseTypeDef,
    PutResolverQueryLogConfigPolicyResponseTypeDef,
    PutResolverRulePolicyResponseTypeDef,
    ResolverRuleConfigTypeDef,
    TagTypeDef,
    TargetAddressTypeDef,
    UpdateFirewallConfigResponseTypeDef,
    UpdateFirewallDomainsResponseTypeDef,
    UpdateFirewallRuleGroupAssociationResponseTypeDef,
    UpdateFirewallRuleResponseTypeDef,
    UpdateResolverDnssecConfigResponseTypeDef,
    UpdateResolverEndpointResponseTypeDef,
    UpdateResolverRuleResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Route53ResolverClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidPolicyDocument: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidTagException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnknownResourceException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class Route53ResolverClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_firewall_rule_group(
        self,
        *,
        CreatorRequestId: str,
        FirewallRuleGroupId: str,
        VpcId: str,
        Priority: int,
        Name: str,
        MutationProtection: MutationProtectionStatusType = None,
        Tags: List["TagTypeDef"] = None
    ) -> AssociateFirewallRuleGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.associate_firewall_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#associate_firewall_rule_group)
        """

    def associate_resolver_endpoint_ip_address(
        self, *, ResolverEndpointId: str, IpAddress: IpAddressUpdateTypeDef
    ) -> AssociateResolverEndpointIpAddressResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.associate_resolver_endpoint_ip_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#associate_resolver_endpoint_ip_address)
        """

    def associate_resolver_query_log_config(
        self, *, ResolverQueryLogConfigId: str, ResourceId: str
    ) -> AssociateResolverQueryLogConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.associate_resolver_query_log_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#associate_resolver_query_log_config)
        """

    def associate_resolver_rule(
        self, *, ResolverRuleId: str, VPCId: str, Name: str = None
    ) -> AssociateResolverRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.associate_resolver_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#associate_resolver_rule)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#can_paginate)
        """

    def create_firewall_domain_list(
        self, *, CreatorRequestId: str, Name: str, Tags: List["TagTypeDef"] = None
    ) -> CreateFirewallDomainListResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.create_firewall_domain_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#create_firewall_domain_list)
        """

    def create_firewall_rule(
        self,
        *,
        CreatorRequestId: str,
        FirewallRuleGroupId: str,
        FirewallDomainListId: str,
        Priority: int,
        Action: ActionType,
        Name: str,
        BlockResponse: BlockResponseType = None,
        BlockOverrideDomain: str = None,
        BlockOverrideDnsType: Literal["CNAME"] = None,
        BlockOverrideTtl: int = None
    ) -> CreateFirewallRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.create_firewall_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#create_firewall_rule)
        """

    def create_firewall_rule_group(
        self, *, CreatorRequestId: str, Name: str, Tags: List["TagTypeDef"] = None
    ) -> CreateFirewallRuleGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.create_firewall_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#create_firewall_rule_group)
        """

    def create_resolver_endpoint(
        self,
        *,
        CreatorRequestId: str,
        SecurityGroupIds: List[str],
        Direction: ResolverEndpointDirectionType,
        IpAddresses: List[IpAddressRequestTypeDef],
        Name: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateResolverEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.create_resolver_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#create_resolver_endpoint)
        """

    def create_resolver_query_log_config(
        self,
        *,
        Name: str,
        DestinationArn: str,
        CreatorRequestId: str,
        Tags: List["TagTypeDef"] = None
    ) -> CreateResolverQueryLogConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.create_resolver_query_log_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#create_resolver_query_log_config)
        """

    def create_resolver_rule(
        self,
        *,
        CreatorRequestId: str,
        RuleType: RuleTypeOptionType,
        DomainName: str,
        Name: str = None,
        TargetIps: List["TargetAddressTypeDef"] = None,
        ResolverEndpointId: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateResolverRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.create_resolver_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#create_resolver_rule)
        """

    def delete_firewall_domain_list(
        self, *, FirewallDomainListId: str
    ) -> DeleteFirewallDomainListResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.delete_firewall_domain_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#delete_firewall_domain_list)
        """

    def delete_firewall_rule(
        self, *, FirewallRuleGroupId: str, FirewallDomainListId: str
    ) -> DeleteFirewallRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.delete_firewall_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#delete_firewall_rule)
        """

    def delete_firewall_rule_group(
        self, *, FirewallRuleGroupId: str
    ) -> DeleteFirewallRuleGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.delete_firewall_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#delete_firewall_rule_group)
        """

    def delete_resolver_endpoint(
        self, *, ResolverEndpointId: str
    ) -> DeleteResolverEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.delete_resolver_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#delete_resolver_endpoint)
        """

    def delete_resolver_query_log_config(
        self, *, ResolverQueryLogConfigId: str
    ) -> DeleteResolverQueryLogConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.delete_resolver_query_log_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#delete_resolver_query_log_config)
        """

    def delete_resolver_rule(self, *, ResolverRuleId: str) -> DeleteResolverRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.delete_resolver_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#delete_resolver_rule)
        """

    def disassociate_firewall_rule_group(
        self, *, FirewallRuleGroupAssociationId: str
    ) -> DisassociateFirewallRuleGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.disassociate_firewall_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#disassociate_firewall_rule_group)
        """

    def disassociate_resolver_endpoint_ip_address(
        self, *, ResolverEndpointId: str, IpAddress: IpAddressUpdateTypeDef
    ) -> DisassociateResolverEndpointIpAddressResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.disassociate_resolver_endpoint_ip_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#disassociate_resolver_endpoint_ip_address)
        """

    def disassociate_resolver_query_log_config(
        self, *, ResolverQueryLogConfigId: str, ResourceId: str
    ) -> DisassociateResolverQueryLogConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.disassociate_resolver_query_log_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#disassociate_resolver_query_log_config)
        """

    def disassociate_resolver_rule(
        self, *, VPCId: str, ResolverRuleId: str
    ) -> DisassociateResolverRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.disassociate_resolver_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#disassociate_resolver_rule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#generate_presigned_url)
        """

    def get_firewall_config(self, *, ResourceId: str) -> GetFirewallConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.get_firewall_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#get_firewall_config)
        """

    def get_firewall_domain_list(
        self, *, FirewallDomainListId: str
    ) -> GetFirewallDomainListResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.get_firewall_domain_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#get_firewall_domain_list)
        """

    def get_firewall_rule_group(
        self, *, FirewallRuleGroupId: str
    ) -> GetFirewallRuleGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.get_firewall_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#get_firewall_rule_group)
        """

    def get_firewall_rule_group_association(
        self, *, FirewallRuleGroupAssociationId: str
    ) -> GetFirewallRuleGroupAssociationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.get_firewall_rule_group_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#get_firewall_rule_group_association)
        """

    def get_firewall_rule_group_policy(
        self, *, Arn: str
    ) -> GetFirewallRuleGroupPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.get_firewall_rule_group_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#get_firewall_rule_group_policy)
        """

    def get_resolver_dnssec_config(
        self, *, ResourceId: str
    ) -> GetResolverDnssecConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_dnssec_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#get_resolver_dnssec_config)
        """

    def get_resolver_endpoint(
        self, *, ResolverEndpointId: str
    ) -> GetResolverEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#get_resolver_endpoint)
        """

    def get_resolver_query_log_config(
        self, *, ResolverQueryLogConfigId: str
    ) -> GetResolverQueryLogConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_query_log_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#get_resolver_query_log_config)
        """

    def get_resolver_query_log_config_association(
        self, *, ResolverQueryLogConfigAssociationId: str
    ) -> GetResolverQueryLogConfigAssociationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_query_log_config_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#get_resolver_query_log_config_association)
        """

    def get_resolver_query_log_config_policy(
        self, *, Arn: str
    ) -> GetResolverQueryLogConfigPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_query_log_config_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#get_resolver_query_log_config_policy)
        """

    def get_resolver_rule(self, *, ResolverRuleId: str) -> GetResolverRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#get_resolver_rule)
        """

    def get_resolver_rule_association(
        self, *, ResolverRuleAssociationId: str
    ) -> GetResolverRuleAssociationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_rule_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#get_resolver_rule_association)
        """

    def get_resolver_rule_policy(self, *, Arn: str) -> GetResolverRulePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_rule_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#get_resolver_rule_policy)
        """

    def import_firewall_domains(
        self, *, FirewallDomainListId: str, Operation: Literal["REPLACE"], DomainFileUrl: str
    ) -> ImportFirewallDomainsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.import_firewall_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#import_firewall_domains)
        """

    def list_firewall_configs(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListFirewallConfigsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.list_firewall_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#list_firewall_configs)
        """

    def list_firewall_domain_lists(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListFirewallDomainListsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.list_firewall_domain_lists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#list_firewall_domain_lists)
        """

    def list_firewall_domains(
        self, *, FirewallDomainListId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListFirewallDomainsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.list_firewall_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#list_firewall_domains)
        """

    def list_firewall_rule_group_associations(
        self,
        *,
        FirewallRuleGroupId: str = None,
        VpcId: str = None,
        Priority: int = None,
        Status: FirewallRuleGroupAssociationStatusType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListFirewallRuleGroupAssociationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.list_firewall_rule_group_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#list_firewall_rule_group_associations)
        """

    def list_firewall_rule_groups(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListFirewallRuleGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.list_firewall_rule_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#list_firewall_rule_groups)
        """

    def list_firewall_rules(
        self,
        *,
        FirewallRuleGroupId: str,
        Priority: int = None,
        Action: ActionType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListFirewallRulesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.list_firewall_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#list_firewall_rules)
        """

    def list_resolver_dnssec_configs(
        self, *, MaxResults: int = None, NextToken: str = None, Filters: List[FilterTypeDef] = None
    ) -> ListResolverDnssecConfigsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_dnssec_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#list_resolver_dnssec_configs)
        """

    def list_resolver_endpoint_ip_addresses(
        self, *, ResolverEndpointId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListResolverEndpointIpAddressesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_endpoint_ip_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#list_resolver_endpoint_ip_addresses)
        """

    def list_resolver_endpoints(
        self, *, MaxResults: int = None, NextToken: str = None, Filters: List[FilterTypeDef] = None
    ) -> ListResolverEndpointsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#list_resolver_endpoints)
        """

    def list_resolver_query_log_config_associations(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
        SortBy: str = None,
        SortOrder: SortOrderType = None
    ) -> ListResolverQueryLogConfigAssociationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_query_log_config_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#list_resolver_query_log_config_associations)
        """

    def list_resolver_query_log_configs(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
        SortBy: str = None,
        SortOrder: SortOrderType = None
    ) -> ListResolverQueryLogConfigsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_query_log_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#list_resolver_query_log_configs)
        """

    def list_resolver_rule_associations(
        self, *, MaxResults: int = None, NextToken: str = None, Filters: List[FilterTypeDef] = None
    ) -> ListResolverRuleAssociationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_rule_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#list_resolver_rule_associations)
        """

    def list_resolver_rules(
        self, *, MaxResults: int = None, NextToken: str = None, Filters: List[FilterTypeDef] = None
    ) -> ListResolverRulesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#list_resolver_rules)
        """

    def list_tags_for_resource(
        self, *, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#list_tags_for_resource)
        """

    def put_firewall_rule_group_policy(
        self, *, Arn: str, FirewallRuleGroupPolicy: str
    ) -> PutFirewallRuleGroupPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.put_firewall_rule_group_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#put_firewall_rule_group_policy)
        """

    def put_resolver_query_log_config_policy(
        self, *, Arn: str, ResolverQueryLogConfigPolicy: str
    ) -> PutResolverQueryLogConfigPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.put_resolver_query_log_config_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#put_resolver_query_log_config_policy)
        """

    def put_resolver_rule_policy(
        self, *, Arn: str, ResolverRulePolicy: str
    ) -> PutResolverRulePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.put_resolver_rule_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#put_resolver_rule_policy)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#untag_resource)
        """

    def update_firewall_config(
        self, *, ResourceId: str, FirewallFailOpen: FirewallFailOpenStatusType
    ) -> UpdateFirewallConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.update_firewall_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#update_firewall_config)
        """

    def update_firewall_domains(
        self,
        *,
        FirewallDomainListId: str,
        Operation: FirewallDomainUpdateOperationType,
        Domains: List[str]
    ) -> UpdateFirewallDomainsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.update_firewall_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#update_firewall_domains)
        """

    def update_firewall_rule(
        self,
        *,
        FirewallRuleGroupId: str,
        FirewallDomainListId: str,
        Priority: int = None,
        Action: ActionType = None,
        BlockResponse: BlockResponseType = None,
        BlockOverrideDomain: str = None,
        BlockOverrideDnsType: Literal["CNAME"] = None,
        BlockOverrideTtl: int = None,
        Name: str = None
    ) -> UpdateFirewallRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.update_firewall_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#update_firewall_rule)
        """

    def update_firewall_rule_group_association(
        self,
        *,
        FirewallRuleGroupAssociationId: str,
        Priority: int = None,
        MutationProtection: MutationProtectionStatusType = None,
        Name: str = None
    ) -> UpdateFirewallRuleGroupAssociationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.update_firewall_rule_group_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#update_firewall_rule_group_association)
        """

    def update_resolver_dnssec_config(
        self, *, ResourceId: str, Validation: ValidationType
    ) -> UpdateResolverDnssecConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.update_resolver_dnssec_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#update_resolver_dnssec_config)
        """

    def update_resolver_endpoint(
        self, *, ResolverEndpointId: str, Name: str = None
    ) -> UpdateResolverEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.update_resolver_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#update_resolver_endpoint)
        """

    def update_resolver_rule(
        self, *, ResolverRuleId: str, Config: ResolverRuleConfigTypeDef
    ) -> UpdateResolverRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Client.update_resolver_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/client.html#update_resolver_rule)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_firewall_configs"]
    ) -> ListFirewallConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Paginator.ListFirewallConfigs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators.html#listfirewallconfigspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_firewall_domain_lists"]
    ) -> ListFirewallDomainListsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Paginator.ListFirewallDomainLists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators.html#listfirewalldomainlistspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_firewall_domains"]
    ) -> ListFirewallDomainsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Paginator.ListFirewallDomains)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators.html#listfirewalldomainspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_firewall_rule_group_associations"]
    ) -> ListFirewallRuleGroupAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Paginator.ListFirewallRuleGroupAssociations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators.html#listfirewallrulegroupassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_firewall_rule_groups"]
    ) -> ListFirewallRuleGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Paginator.ListFirewallRuleGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators.html#listfirewallrulegroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_firewall_rules"]
    ) -> ListFirewallRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Paginator.ListFirewallRules)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators.html#listfirewallrulespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resolver_dnssec_configs"]
    ) -> ListResolverDnssecConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverDnssecConfigs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators.html#listresolverdnssecconfigspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resolver_endpoint_ip_addresses"]
    ) -> ListResolverEndpointIpAddressesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverEndpointIpAddresses)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators.html#listresolverendpointipaddressespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resolver_endpoints"]
    ) -> ListResolverEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverEndpoints)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators.html#listresolverendpointspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resolver_query_log_config_associations"]
    ) -> ListResolverQueryLogConfigAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverQueryLogConfigAssociations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators.html#listresolverquerylogconfigassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resolver_query_log_configs"]
    ) -> ListResolverQueryLogConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverQueryLogConfigs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators.html#listresolverquerylogconfigspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resolver_rule_associations"]
    ) -> ListResolverRuleAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverRuleAssociations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators.html#listresolverruleassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resolver_rules"]
    ) -> ListResolverRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverRules)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators.html#listresolverrulespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/route53resolver.html#Route53Resolver.Paginator.ListTagsForResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators.html#listtagsforresourcepaginator)
        """
