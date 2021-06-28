"""
Type annotations for waf service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_waf import WAFClient

    client: WAFClient = boto3.client("waf")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .paginator import (
    GetRateBasedRuleManagedKeysPaginator,
    ListActivatedRulesInRuleGroupPaginator,
    ListByteMatchSetsPaginator,
    ListGeoMatchSetsPaginator,
    ListIPSetsPaginator,
    ListLoggingConfigurationsPaginator,
    ListRateBasedRulesPaginator,
    ListRegexMatchSetsPaginator,
    ListRegexPatternSetsPaginator,
    ListRuleGroupsPaginator,
    ListRulesPaginator,
    ListSizeConstraintSetsPaginator,
    ListSqlInjectionMatchSetsPaginator,
    ListSubscribedRuleGroupsPaginator,
    ListWebACLsPaginator,
    ListXssMatchSetsPaginator,
)
from .type_defs import (
    ByteMatchSetUpdateTypeDef,
    CreateByteMatchSetResponseResponseTypeDef,
    CreateGeoMatchSetResponseResponseTypeDef,
    CreateIPSetResponseResponseTypeDef,
    CreateRateBasedRuleResponseResponseTypeDef,
    CreateRegexMatchSetResponseResponseTypeDef,
    CreateRegexPatternSetResponseResponseTypeDef,
    CreateRuleGroupResponseResponseTypeDef,
    CreateRuleResponseResponseTypeDef,
    CreateSizeConstraintSetResponseResponseTypeDef,
    CreateSqlInjectionMatchSetResponseResponseTypeDef,
    CreateWebACLMigrationStackResponseResponseTypeDef,
    CreateWebACLResponseResponseTypeDef,
    CreateXssMatchSetResponseResponseTypeDef,
    DeleteByteMatchSetResponseResponseTypeDef,
    DeleteGeoMatchSetResponseResponseTypeDef,
    DeleteIPSetResponseResponseTypeDef,
    DeleteRateBasedRuleResponseResponseTypeDef,
    DeleteRegexMatchSetResponseResponseTypeDef,
    DeleteRegexPatternSetResponseResponseTypeDef,
    DeleteRuleGroupResponseResponseTypeDef,
    DeleteRuleResponseResponseTypeDef,
    DeleteSizeConstraintSetResponseResponseTypeDef,
    DeleteSqlInjectionMatchSetResponseResponseTypeDef,
    DeleteWebACLResponseResponseTypeDef,
    DeleteXssMatchSetResponseResponseTypeDef,
    GeoMatchSetUpdateTypeDef,
    GetByteMatchSetResponseResponseTypeDef,
    GetChangeTokenResponseResponseTypeDef,
    GetChangeTokenStatusResponseResponseTypeDef,
    GetGeoMatchSetResponseResponseTypeDef,
    GetIPSetResponseResponseTypeDef,
    GetLoggingConfigurationResponseResponseTypeDef,
    GetPermissionPolicyResponseResponseTypeDef,
    GetRateBasedRuleManagedKeysResponseResponseTypeDef,
    GetRateBasedRuleResponseResponseTypeDef,
    GetRegexMatchSetResponseResponseTypeDef,
    GetRegexPatternSetResponseResponseTypeDef,
    GetRuleGroupResponseResponseTypeDef,
    GetRuleResponseResponseTypeDef,
    GetSampledRequestsResponseResponseTypeDef,
    GetSizeConstraintSetResponseResponseTypeDef,
    GetSqlInjectionMatchSetResponseResponseTypeDef,
    GetWebACLResponseResponseTypeDef,
    GetXssMatchSetResponseResponseTypeDef,
    IPSetUpdateTypeDef,
    ListActivatedRulesInRuleGroupResponseResponseTypeDef,
    ListByteMatchSetsResponseResponseTypeDef,
    ListGeoMatchSetsResponseResponseTypeDef,
    ListIPSetsResponseResponseTypeDef,
    ListLoggingConfigurationsResponseResponseTypeDef,
    ListRateBasedRulesResponseResponseTypeDef,
    ListRegexMatchSetsResponseResponseTypeDef,
    ListRegexPatternSetsResponseResponseTypeDef,
    ListRuleGroupsResponseResponseTypeDef,
    ListRulesResponseResponseTypeDef,
    ListSizeConstraintSetsResponseResponseTypeDef,
    ListSqlInjectionMatchSetsResponseResponseTypeDef,
    ListSubscribedRuleGroupsResponseResponseTypeDef,
    ListTagsForResourceResponseResponseTypeDef,
    ListWebACLsResponseResponseTypeDef,
    ListXssMatchSetsResponseResponseTypeDef,
    LoggingConfigurationTypeDef,
    PutLoggingConfigurationResponseResponseTypeDef,
    RegexMatchSetUpdateTypeDef,
    RegexPatternSetUpdateTypeDef,
    RuleGroupUpdateTypeDef,
    RuleUpdateTypeDef,
    SizeConstraintSetUpdateTypeDef,
    SqlInjectionMatchSetUpdateTypeDef,
    TagTypeDef,
    TimeWindowTypeDef,
    UpdateByteMatchSetResponseResponseTypeDef,
    UpdateGeoMatchSetResponseResponseTypeDef,
    UpdateIPSetResponseResponseTypeDef,
    UpdateRateBasedRuleResponseResponseTypeDef,
    UpdateRegexMatchSetResponseResponseTypeDef,
    UpdateRegexPatternSetResponseResponseTypeDef,
    UpdateRuleGroupResponseResponseTypeDef,
    UpdateRuleResponseResponseTypeDef,
    UpdateSizeConstraintSetResponseResponseTypeDef,
    UpdateSqlInjectionMatchSetResponseResponseTypeDef,
    UpdateWebACLResponseResponseTypeDef,
    UpdateXssMatchSetResponseResponseTypeDef,
    WafActionTypeDef,
    WebACLUpdateTypeDef,
    XssMatchSetUpdateTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("WAFClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    WAFBadRequestException: Type[BotocoreClientError]
    WAFDisallowedNameException: Type[BotocoreClientError]
    WAFEntityMigrationException: Type[BotocoreClientError]
    WAFInternalErrorException: Type[BotocoreClientError]
    WAFInvalidAccountException: Type[BotocoreClientError]
    WAFInvalidOperationException: Type[BotocoreClientError]
    WAFInvalidParameterException: Type[BotocoreClientError]
    WAFInvalidPermissionPolicyException: Type[BotocoreClientError]
    WAFInvalidRegexPatternException: Type[BotocoreClientError]
    WAFLimitsExceededException: Type[BotocoreClientError]
    WAFNonEmptyEntityException: Type[BotocoreClientError]
    WAFNonexistentContainerException: Type[BotocoreClientError]
    WAFNonexistentItemException: Type[BotocoreClientError]
    WAFReferencedItemException: Type[BotocoreClientError]
    WAFServiceLinkedRoleErrorException: Type[BotocoreClientError]
    WAFStaleDataException: Type[BotocoreClientError]
    WAFSubscriptionNotFoundException: Type[BotocoreClientError]
    WAFTagOperationException: Type[BotocoreClientError]
    WAFTagOperationInternalErrorException: Type[BotocoreClientError]


class WAFClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#can_paginate)
        """

    def create_byte_match_set(
        self, *, Name: str, ChangeToken: str
    ) -> CreateByteMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.create_byte_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#create_byte_match_set)
        """

    def create_geo_match_set(
        self, *, Name: str, ChangeToken: str
    ) -> CreateGeoMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.create_geo_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#create_geo_match_set)
        """

    def create_ip_set(self, *, Name: str, ChangeToken: str) -> CreateIPSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.create_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#create_ip_set)
        """

    def create_rate_based_rule(
        self,
        *,
        Name: str,
        MetricName: str,
        RateKey: Literal["IP"],
        RateLimit: int,
        ChangeToken: str,
        Tags: List["TagTypeDef"] = None
    ) -> CreateRateBasedRuleResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.create_rate_based_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#create_rate_based_rule)
        """

    def create_regex_match_set(
        self, *, Name: str, ChangeToken: str
    ) -> CreateRegexMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.create_regex_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#create_regex_match_set)
        """

    def create_regex_pattern_set(
        self, *, Name: str, ChangeToken: str
    ) -> CreateRegexPatternSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.create_regex_pattern_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#create_regex_pattern_set)
        """

    def create_rule(
        self, *, Name: str, MetricName: str, ChangeToken: str, Tags: List["TagTypeDef"] = None
    ) -> CreateRuleResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.create_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#create_rule)
        """

    def create_rule_group(
        self, *, Name: str, MetricName: str, ChangeToken: str, Tags: List["TagTypeDef"] = None
    ) -> CreateRuleGroupResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.create_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#create_rule_group)
        """

    def create_size_constraint_set(
        self, *, Name: str, ChangeToken: str
    ) -> CreateSizeConstraintSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.create_size_constraint_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#create_size_constraint_set)
        """

    def create_sql_injection_match_set(
        self, *, Name: str, ChangeToken: str
    ) -> CreateSqlInjectionMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.create_sql_injection_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#create_sql_injection_match_set)
        """

    def create_web_acl(
        self,
        *,
        Name: str,
        MetricName: str,
        DefaultAction: "WafActionTypeDef",
        ChangeToken: str,
        Tags: List["TagTypeDef"] = None
    ) -> CreateWebACLResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.create_web_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#create_web_acl)
        """

    def create_web_acl_migration_stack(
        self, *, WebACLId: str, S3BucketName: str, IgnoreUnsupportedType: bool
    ) -> CreateWebACLMigrationStackResponseResponseTypeDef:
        """
        Creates an AWS CloudFormation WAFV2 template for the specified web ACL in the
        specified Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.create_web_acl_migration_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#create_web_acl_migration_stack)
        """

    def create_xss_match_set(
        self, *, Name: str, ChangeToken: str
    ) -> CreateXssMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.create_xss_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#create_xss_match_set)
        """

    def delete_byte_match_set(
        self, *, ByteMatchSetId: str, ChangeToken: str
    ) -> DeleteByteMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.delete_byte_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#delete_byte_match_set)
        """

    def delete_geo_match_set(
        self, *, GeoMatchSetId: str, ChangeToken: str
    ) -> DeleteGeoMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.delete_geo_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#delete_geo_match_set)
        """

    def delete_ip_set(
        self, *, IPSetId: str, ChangeToken: str
    ) -> DeleteIPSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.delete_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#delete_ip_set)
        """

    def delete_logging_configuration(self, *, ResourceArn: str) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.delete_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#delete_logging_configuration)
        """

    def delete_permission_policy(self, *, ResourceArn: str) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.delete_permission_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#delete_permission_policy)
        """

    def delete_rate_based_rule(
        self, *, RuleId: str, ChangeToken: str
    ) -> DeleteRateBasedRuleResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.delete_rate_based_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#delete_rate_based_rule)
        """

    def delete_regex_match_set(
        self, *, RegexMatchSetId: str, ChangeToken: str
    ) -> DeleteRegexMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.delete_regex_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#delete_regex_match_set)
        """

    def delete_regex_pattern_set(
        self, *, RegexPatternSetId: str, ChangeToken: str
    ) -> DeleteRegexPatternSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.delete_regex_pattern_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#delete_regex_pattern_set)
        """

    def delete_rule(self, *, RuleId: str, ChangeToken: str) -> DeleteRuleResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.delete_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#delete_rule)
        """

    def delete_rule_group(
        self, *, RuleGroupId: str, ChangeToken: str
    ) -> DeleteRuleGroupResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.delete_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#delete_rule_group)
        """

    def delete_size_constraint_set(
        self, *, SizeConstraintSetId: str, ChangeToken: str
    ) -> DeleteSizeConstraintSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.delete_size_constraint_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#delete_size_constraint_set)
        """

    def delete_sql_injection_match_set(
        self, *, SqlInjectionMatchSetId: str, ChangeToken: str
    ) -> DeleteSqlInjectionMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.delete_sql_injection_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#delete_sql_injection_match_set)
        """

    def delete_web_acl(
        self, *, WebACLId: str, ChangeToken: str
    ) -> DeleteWebACLResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.delete_web_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#delete_web_acl)
        """

    def delete_xss_match_set(
        self, *, XssMatchSetId: str, ChangeToken: str
    ) -> DeleteXssMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.delete_xss_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#delete_xss_match_set)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#generate_presigned_url)
        """

    def get_byte_match_set(self, *, ByteMatchSetId: str) -> GetByteMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.get_byte_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#get_byte_match_set)
        """

    def get_change_token(self) -> GetChangeTokenResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.get_change_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#get_change_token)
        """

    def get_change_token_status(
        self, *, ChangeToken: str
    ) -> GetChangeTokenStatusResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.get_change_token_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#get_change_token_status)
        """

    def get_geo_match_set(self, *, GeoMatchSetId: str) -> GetGeoMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.get_geo_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#get_geo_match_set)
        """

    def get_ip_set(self, *, IPSetId: str) -> GetIPSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.get_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#get_ip_set)
        """

    def get_logging_configuration(
        self, *, ResourceArn: str
    ) -> GetLoggingConfigurationResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.get_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#get_logging_configuration)
        """

    def get_permission_policy(
        self, *, ResourceArn: str
    ) -> GetPermissionPolicyResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.get_permission_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#get_permission_policy)
        """

    def get_rate_based_rule(self, *, RuleId: str) -> GetRateBasedRuleResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.get_rate_based_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#get_rate_based_rule)
        """

    def get_rate_based_rule_managed_keys(
        self, *, RuleId: str, NextMarker: str = None
    ) -> GetRateBasedRuleManagedKeysResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.get_rate_based_rule_managed_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#get_rate_based_rule_managed_keys)
        """

    def get_regex_match_set(
        self, *, RegexMatchSetId: str
    ) -> GetRegexMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.get_regex_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#get_regex_match_set)
        """

    def get_regex_pattern_set(
        self, *, RegexPatternSetId: str
    ) -> GetRegexPatternSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.get_regex_pattern_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#get_regex_pattern_set)
        """

    def get_rule(self, *, RuleId: str) -> GetRuleResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.get_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#get_rule)
        """

    def get_rule_group(self, *, RuleGroupId: str) -> GetRuleGroupResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.get_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#get_rule_group)
        """

    def get_sampled_requests(
        self, *, WebAclId: str, RuleId: str, TimeWindow: "TimeWindowTypeDef", MaxItems: int
    ) -> GetSampledRequestsResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.get_sampled_requests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#get_sampled_requests)
        """

    def get_size_constraint_set(
        self, *, SizeConstraintSetId: str
    ) -> GetSizeConstraintSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.get_size_constraint_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#get_size_constraint_set)
        """

    def get_sql_injection_match_set(
        self, *, SqlInjectionMatchSetId: str
    ) -> GetSqlInjectionMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.get_sql_injection_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#get_sql_injection_match_set)
        """

    def get_web_acl(self, *, WebACLId: str) -> GetWebACLResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.get_web_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#get_web_acl)
        """

    def get_xss_match_set(self, *, XssMatchSetId: str) -> GetXssMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.get_xss_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#get_xss_match_set)
        """

    def list_activated_rules_in_rule_group(
        self, *, RuleGroupId: str = None, NextMarker: str = None, Limit: int = None
    ) -> ListActivatedRulesInRuleGroupResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.list_activated_rules_in_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#list_activated_rules_in_rule_group)
        """

    def list_byte_match_sets(
        self, *, NextMarker: str = None, Limit: int = None
    ) -> ListByteMatchSetsResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.list_byte_match_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#list_byte_match_sets)
        """

    def list_geo_match_sets(
        self, *, NextMarker: str = None, Limit: int = None
    ) -> ListGeoMatchSetsResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.list_geo_match_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#list_geo_match_sets)
        """

    def list_ip_sets(
        self, *, NextMarker: str = None, Limit: int = None
    ) -> ListIPSetsResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.list_ip_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#list_ip_sets)
        """

    def list_logging_configurations(
        self, *, NextMarker: str = None, Limit: int = None
    ) -> ListLoggingConfigurationsResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.list_logging_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#list_logging_configurations)
        """

    def list_rate_based_rules(
        self, *, NextMarker: str = None, Limit: int = None
    ) -> ListRateBasedRulesResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.list_rate_based_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#list_rate_based_rules)
        """

    def list_regex_match_sets(
        self, *, NextMarker: str = None, Limit: int = None
    ) -> ListRegexMatchSetsResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.list_regex_match_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#list_regex_match_sets)
        """

    def list_regex_pattern_sets(
        self, *, NextMarker: str = None, Limit: int = None
    ) -> ListRegexPatternSetsResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.list_regex_pattern_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#list_regex_pattern_sets)
        """

    def list_rule_groups(
        self, *, NextMarker: str = None, Limit: int = None
    ) -> ListRuleGroupsResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.list_rule_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#list_rule_groups)
        """

    def list_rules(
        self, *, NextMarker: str = None, Limit: int = None
    ) -> ListRulesResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.list_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#list_rules)
        """

    def list_size_constraint_sets(
        self, *, NextMarker: str = None, Limit: int = None
    ) -> ListSizeConstraintSetsResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.list_size_constraint_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#list_size_constraint_sets)
        """

    def list_sql_injection_match_sets(
        self, *, NextMarker: str = None, Limit: int = None
    ) -> ListSqlInjectionMatchSetsResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.list_sql_injection_match_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#list_sql_injection_match_sets)
        """

    def list_subscribed_rule_groups(
        self, *, NextMarker: str = None, Limit: int = None
    ) -> ListSubscribedRuleGroupsResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.list_subscribed_rule_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#list_subscribed_rule_groups)
        """

    def list_tags_for_resource(
        self, *, ResourceARN: str, NextMarker: str = None, Limit: int = None
    ) -> ListTagsForResourceResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#list_tags_for_resource)
        """

    def list_web_acls(
        self, *, NextMarker: str = None, Limit: int = None
    ) -> ListWebACLsResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.list_web_acls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#list_web_acls)
        """

    def list_xss_match_sets(
        self, *, NextMarker: str = None, Limit: int = None
    ) -> ListXssMatchSetsResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.list_xss_match_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#list_xss_match_sets)
        """

    def put_logging_configuration(
        self, *, LoggingConfiguration: "LoggingConfigurationTypeDef"
    ) -> PutLoggingConfigurationResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.put_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#put_logging_configuration)
        """

    def put_permission_policy(self, *, ResourceArn: str, Policy: str) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.put_permission_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#put_permission_policy)
        """

    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#untag_resource)
        """

    def update_byte_match_set(
        self, *, ByteMatchSetId: str, ChangeToken: str, Updates: List["ByteMatchSetUpdateTypeDef"]
    ) -> UpdateByteMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.update_byte_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#update_byte_match_set)
        """

    def update_geo_match_set(
        self, *, GeoMatchSetId: str, ChangeToken: str, Updates: List["GeoMatchSetUpdateTypeDef"]
    ) -> UpdateGeoMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.update_geo_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#update_geo_match_set)
        """

    def update_ip_set(
        self, *, IPSetId: str, ChangeToken: str, Updates: List["IPSetUpdateTypeDef"]
    ) -> UpdateIPSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.update_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#update_ip_set)
        """

    def update_rate_based_rule(
        self, *, RuleId: str, ChangeToken: str, Updates: List["RuleUpdateTypeDef"], RateLimit: int
    ) -> UpdateRateBasedRuleResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.update_rate_based_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#update_rate_based_rule)
        """

    def update_regex_match_set(
        self, *, RegexMatchSetId: str, Updates: List["RegexMatchSetUpdateTypeDef"], ChangeToken: str
    ) -> UpdateRegexMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.update_regex_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#update_regex_match_set)
        """

    def update_regex_pattern_set(
        self,
        *,
        RegexPatternSetId: str,
        Updates: List["RegexPatternSetUpdateTypeDef"],
        ChangeToken: str
    ) -> UpdateRegexPatternSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.update_regex_pattern_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#update_regex_pattern_set)
        """

    def update_rule(
        self, *, RuleId: str, ChangeToken: str, Updates: List["RuleUpdateTypeDef"]
    ) -> UpdateRuleResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.update_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#update_rule)
        """

    def update_rule_group(
        self, *, RuleGroupId: str, Updates: List["RuleGroupUpdateTypeDef"], ChangeToken: str
    ) -> UpdateRuleGroupResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.update_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#update_rule_group)
        """

    def update_size_constraint_set(
        self,
        *,
        SizeConstraintSetId: str,
        ChangeToken: str,
        Updates: List["SizeConstraintSetUpdateTypeDef"]
    ) -> UpdateSizeConstraintSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.update_size_constraint_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#update_size_constraint_set)
        """

    def update_sql_injection_match_set(
        self,
        *,
        SqlInjectionMatchSetId: str,
        ChangeToken: str,
        Updates: List["SqlInjectionMatchSetUpdateTypeDef"]
    ) -> UpdateSqlInjectionMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.update_sql_injection_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#update_sql_injection_match_set)
        """

    def update_web_acl(
        self,
        *,
        WebACLId: str,
        ChangeToken: str,
        Updates: List["WebACLUpdateTypeDef"] = None,
        DefaultAction: "WafActionTypeDef" = None
    ) -> UpdateWebACLResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.update_web_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#update_web_acl)
        """

    def update_xss_match_set(
        self, *, XssMatchSetId: str, ChangeToken: str, Updates: List["XssMatchSetUpdateTypeDef"]
    ) -> UpdateXssMatchSetResponseResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Client.update_xss_match_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/client.html#update_xss_match_set)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_rate_based_rule_managed_keys"]
    ) -> GetRateBasedRuleManagedKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Paginator.GetRateBasedRuleManagedKeys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/paginators.html#getratebasedrulemanagedkeyspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_activated_rules_in_rule_group"]
    ) -> ListActivatedRulesInRuleGroupPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Paginator.ListActivatedRulesInRuleGroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/paginators.html#listactivatedrulesinrulegrouppaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_byte_match_sets"]
    ) -> ListByteMatchSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Paginator.ListByteMatchSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/paginators.html#listbytematchsetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_geo_match_sets"]
    ) -> ListGeoMatchSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Paginator.ListGeoMatchSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/paginators.html#listgeomatchsetspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_ip_sets"]) -> ListIPSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Paginator.ListIPSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/paginators.html#listipsetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_logging_configurations"]
    ) -> ListLoggingConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Paginator.ListLoggingConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/paginators.html#listloggingconfigurationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_rate_based_rules"]
    ) -> ListRateBasedRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Paginator.ListRateBasedRules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/paginators.html#listratebasedrulespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_regex_match_sets"]
    ) -> ListRegexMatchSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Paginator.ListRegexMatchSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/paginators.html#listregexmatchsetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_regex_pattern_sets"]
    ) -> ListRegexPatternSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Paginator.ListRegexPatternSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/paginators.html#listregexpatternsetspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_rule_groups"]) -> ListRuleGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Paginator.ListRuleGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/paginators.html#listrulegroupspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_rules"]) -> ListRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Paginator.ListRules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/paginators.html#listrulespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_size_constraint_sets"]
    ) -> ListSizeConstraintSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Paginator.ListSizeConstraintSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/paginators.html#listsizeconstraintsetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_sql_injection_match_sets"]
    ) -> ListSqlInjectionMatchSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Paginator.ListSqlInjectionMatchSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/paginators.html#listsqlinjectionmatchsetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscribed_rule_groups"]
    ) -> ListSubscribedRuleGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Paginator.ListSubscribedRuleGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/paginators.html#listsubscribedrulegroupspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_web_acls"]) -> ListWebACLsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Paginator.ListWebACLs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/paginators.html#listwebaclspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_xss_match_sets"]
    ) -> ListXssMatchSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/waf.html#WAF.Paginator.ListXssMatchSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/paginators.html#listxssmatchsetspaginator)
        """
