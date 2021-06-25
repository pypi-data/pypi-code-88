"""
Type annotations for network-firewall service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_network_firewall import NetworkFirewallClient

    client: NetworkFirewallClient = boto3.client("network-firewall")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import RuleGroupTypeType
from .paginator import (
    ListFirewallPoliciesPaginator,
    ListFirewallsPaginator,
    ListRuleGroupsPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    AssociateFirewallPolicyResponseTypeDef,
    AssociateSubnetsResponseTypeDef,
    CreateFirewallPolicyResponseTypeDef,
    CreateFirewallResponseTypeDef,
    CreateRuleGroupResponseTypeDef,
    DeleteFirewallPolicyResponseTypeDef,
    DeleteFirewallResponseTypeDef,
    DeleteRuleGroupResponseTypeDef,
    DescribeFirewallPolicyResponseTypeDef,
    DescribeFirewallResponseTypeDef,
    DescribeLoggingConfigurationResponseTypeDef,
    DescribeResourcePolicyResponseTypeDef,
    DescribeRuleGroupResponseTypeDef,
    DisassociateSubnetsResponseTypeDef,
    FirewallPolicyTypeDef,
    ListFirewallPoliciesResponseTypeDef,
    ListFirewallsResponseTypeDef,
    ListRuleGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggingConfigurationTypeDef,
    RuleGroupTypeDef,
    SubnetMappingTypeDef,
    TagTypeDef,
    UpdateFirewallDeleteProtectionResponseTypeDef,
    UpdateFirewallDescriptionResponseTypeDef,
    UpdateFirewallPolicyChangeProtectionResponseTypeDef,
    UpdateFirewallPolicyResponseTypeDef,
    UpdateLoggingConfigurationResponseTypeDef,
    UpdateRuleGroupResponseTypeDef,
    UpdateSubnetChangeProtectionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("NetworkFirewallClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InsufficientCapacityException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidOperationException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidResourcePolicyException: Type[BotocoreClientError]
    InvalidTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    LogDestinationPermissionException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceOwnerCheckException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]


class NetworkFirewallClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_firewall_policy(
        self,
        *,
        FirewallPolicyArn: str,
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None
    ) -> AssociateFirewallPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.associate_firewall_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#associate_firewall_policy)
        """

    def associate_subnets(
        self,
        *,
        SubnetMappings: List["SubnetMappingTypeDef"],
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None
    ) -> AssociateSubnetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.associate_subnets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#associate_subnets)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#can_paginate)
        """

    def create_firewall(
        self,
        *,
        FirewallName: str,
        FirewallPolicyArn: str,
        VpcId: str,
        SubnetMappings: List["SubnetMappingTypeDef"],
        DeleteProtection: bool = None,
        SubnetChangeProtection: bool = None,
        FirewallPolicyChangeProtection: bool = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateFirewallResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.create_firewall)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#create_firewall)
        """

    def create_firewall_policy(
        self,
        *,
        FirewallPolicyName: str,
        FirewallPolicy: "FirewallPolicyTypeDef",
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateFirewallPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.create_firewall_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#create_firewall_policy)
        """

    def create_rule_group(
        self,
        *,
        RuleGroupName: str,
        Type: RuleGroupTypeType,
        Capacity: int,
        RuleGroup: "RuleGroupTypeDef" = None,
        Rules: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateRuleGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.create_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#create_rule_group)
        """

    def delete_firewall(
        self, *, FirewallName: str = None, FirewallArn: str = None
    ) -> DeleteFirewallResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.delete_firewall)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#delete_firewall)
        """

    def delete_firewall_policy(
        self, *, FirewallPolicyName: str = None, FirewallPolicyArn: str = None
    ) -> DeleteFirewallPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.delete_firewall_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#delete_firewall_policy)
        """

    def delete_resource_policy(self, *, ResourceArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#delete_resource_policy)
        """

    def delete_rule_group(
        self, *, RuleGroupName: str = None, RuleGroupArn: str = None, Type: RuleGroupTypeType = None
    ) -> DeleteRuleGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.delete_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#delete_rule_group)
        """

    def describe_firewall(
        self, *, FirewallName: str = None, FirewallArn: str = None
    ) -> DescribeFirewallResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.describe_firewall)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#describe_firewall)
        """

    def describe_firewall_policy(
        self, *, FirewallPolicyName: str = None, FirewallPolicyArn: str = None
    ) -> DescribeFirewallPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.describe_firewall_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#describe_firewall_policy)
        """

    def describe_logging_configuration(
        self, *, FirewallArn: str = None, FirewallName: str = None
    ) -> DescribeLoggingConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.describe_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#describe_logging_configuration)
        """

    def describe_resource_policy(
        self, *, ResourceArn: str
    ) -> DescribeResourcePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.describe_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#describe_resource_policy)
        """

    def describe_rule_group(
        self, *, RuleGroupName: str = None, RuleGroupArn: str = None, Type: RuleGroupTypeType = None
    ) -> DescribeRuleGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.describe_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#describe_rule_group)
        """

    def disassociate_subnets(
        self,
        *,
        SubnetIds: List[str],
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None
    ) -> DisassociateSubnetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.disassociate_subnets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#disassociate_subnets)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#generate_presigned_url)
        """

    def list_firewall_policies(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListFirewallPoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.list_firewall_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#list_firewall_policies)
        """

    def list_firewalls(
        self, *, NextToken: str = None, VpcIds: List[str] = None, MaxResults: int = None
    ) -> ListFirewallsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.list_firewalls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#list_firewalls)
        """

    def list_rule_groups(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListRuleGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.list_rule_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#list_rule_groups)
        """

    def list_tags_for_resource(
        self, *, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#list_tags_for_resource)
        """

    def put_resource_policy(self, *, ResourceArn: str, Policy: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#put_resource_policy)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#untag_resource)
        """

    def update_firewall_delete_protection(
        self,
        *,
        DeleteProtection: bool,
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None
    ) -> UpdateFirewallDeleteProtectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_delete_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_firewall_delete_protection)
        """

    def update_firewall_description(
        self,
        *,
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None,
        Description: str = None
    ) -> UpdateFirewallDescriptionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_description)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_firewall_description)
        """

    def update_firewall_policy(
        self,
        *,
        UpdateToken: str,
        FirewallPolicy: "FirewallPolicyTypeDef",
        FirewallPolicyArn: str = None,
        FirewallPolicyName: str = None,
        Description: str = None,
        DryRun: bool = None
    ) -> UpdateFirewallPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_firewall_policy)
        """

    def update_firewall_policy_change_protection(
        self,
        *,
        FirewallPolicyChangeProtection: bool,
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None
    ) -> UpdateFirewallPolicyChangeProtectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_policy_change_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_firewall_policy_change_protection)
        """

    def update_logging_configuration(
        self,
        *,
        FirewallArn: str = None,
        FirewallName: str = None,
        LoggingConfiguration: "LoggingConfigurationTypeDef" = None
    ) -> UpdateLoggingConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.update_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_logging_configuration)
        """

    def update_rule_group(
        self,
        *,
        UpdateToken: str,
        RuleGroupArn: str = None,
        RuleGroupName: str = None,
        RuleGroup: "RuleGroupTypeDef" = None,
        Rules: str = None,
        Type: RuleGroupTypeType = None,
        Description: str = None,
        DryRun: bool = None
    ) -> UpdateRuleGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.update_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_rule_group)
        """

    def update_subnet_change_protection(
        self,
        *,
        SubnetChangeProtection: bool,
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None
    ) -> UpdateSubnetChangeProtectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Client.update_subnet_change_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_subnet_change_protection)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_firewall_policies"]
    ) -> ListFirewallPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewallPolicies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listfirewallpoliciespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_firewalls"]) -> ListFirewallsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewalls)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listfirewallspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_rule_groups"]) -> ListRuleGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListRuleGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listrulegroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListTagsForResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listtagsforresourcepaginator)
        """
