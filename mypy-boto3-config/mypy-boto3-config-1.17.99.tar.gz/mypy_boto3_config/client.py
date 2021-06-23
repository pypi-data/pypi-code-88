"""
Type annotations for config service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_config import ConfigServiceClient

    client: ConfigServiceClient = boto3.client("config")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    AggregateConformancePackComplianceSummaryGroupKeyType,
    AggregatedSourceStatusTypeType,
    ChronologicalOrderType,
    ComplianceTypeType,
    ConfigRuleComplianceSummaryGroupKeyType,
    ResourceCountGroupKeyType,
    ResourceTypeType,
)
from .paginator import (
    DescribeAggregateComplianceByConfigRulesPaginator,
    DescribeAggregateComplianceByConformancePacksPaginator,
    DescribeAggregationAuthorizationsPaginator,
    DescribeComplianceByConfigRulePaginator,
    DescribeComplianceByResourcePaginator,
    DescribeConfigRuleEvaluationStatusPaginator,
    DescribeConfigRulesPaginator,
    DescribeConfigurationAggregatorSourcesStatusPaginator,
    DescribeConfigurationAggregatorsPaginator,
    DescribeConformancePacksPaginator,
    DescribeConformancePackStatusPaginator,
    DescribeOrganizationConfigRulesPaginator,
    DescribeOrganizationConfigRuleStatusesPaginator,
    DescribeOrganizationConformancePacksPaginator,
    DescribeOrganizationConformancePackStatusesPaginator,
    DescribePendingAggregationRequestsPaginator,
    DescribeRemediationExecutionStatusPaginator,
    DescribeRetentionConfigurationsPaginator,
    GetAggregateComplianceDetailsByConfigRulePaginator,
    GetComplianceDetailsByConfigRulePaginator,
    GetComplianceDetailsByResourcePaginator,
    GetConformancePackComplianceSummaryPaginator,
    GetOrganizationConfigRuleDetailedStatusPaginator,
    GetOrganizationConformancePackDetailedStatusPaginator,
    GetResourceConfigHistoryPaginator,
    ListAggregateDiscoveredResourcesPaginator,
    ListDiscoveredResourcesPaginator,
    ListTagsForResourcePaginator,
    SelectAggregateResourceConfigPaginator,
    SelectResourceConfigPaginator,
)
from .type_defs import (
    AccountAggregationSourceTypeDef,
    AggregateConformancePackComplianceFiltersTypeDef,
    AggregateConformancePackComplianceSummaryFiltersTypeDef,
    AggregateResourceIdentifierTypeDef,
    BatchGetAggregateResourceConfigResponseTypeDef,
    BatchGetResourceConfigResponseTypeDef,
    ConfigRuleComplianceFiltersTypeDef,
    ConfigRuleComplianceSummaryFiltersTypeDef,
    ConfigRuleTypeDef,
    ConfigurationRecorderTypeDef,
    ConformancePackComplianceFiltersTypeDef,
    ConformancePackEvaluationFiltersTypeDef,
    ConformancePackInputParameterTypeDef,
    DeleteRemediationExceptionsResponseTypeDef,
    DeliverConfigSnapshotResponseTypeDef,
    DeliveryChannelTypeDef,
    DescribeAggregateComplianceByConfigRulesResponseTypeDef,
    DescribeAggregateComplianceByConformancePacksResponseTypeDef,
    DescribeAggregationAuthorizationsResponseTypeDef,
    DescribeComplianceByConfigRuleResponseTypeDef,
    DescribeComplianceByResourceResponseTypeDef,
    DescribeConfigRuleEvaluationStatusResponseTypeDef,
    DescribeConfigRulesResponseTypeDef,
    DescribeConfigurationAggregatorSourcesStatusResponseTypeDef,
    DescribeConfigurationAggregatorsResponseTypeDef,
    DescribeConfigurationRecordersResponseTypeDef,
    DescribeConfigurationRecorderStatusResponseTypeDef,
    DescribeConformancePackComplianceResponseTypeDef,
    DescribeConformancePacksResponseTypeDef,
    DescribeConformancePackStatusResponseTypeDef,
    DescribeDeliveryChannelsResponseTypeDef,
    DescribeDeliveryChannelStatusResponseTypeDef,
    DescribeOrganizationConfigRulesResponseTypeDef,
    DescribeOrganizationConfigRuleStatusesResponseTypeDef,
    DescribeOrganizationConformancePacksResponseTypeDef,
    DescribeOrganizationConformancePackStatusesResponseTypeDef,
    DescribePendingAggregationRequestsResponseTypeDef,
    DescribeRemediationConfigurationsResponseTypeDef,
    DescribeRemediationExceptionsResponseTypeDef,
    DescribeRemediationExecutionStatusResponseTypeDef,
    DescribeRetentionConfigurationsResponseTypeDef,
    EvaluationTypeDef,
    ExternalEvaluationTypeDef,
    GetAggregateComplianceDetailsByConfigRuleResponseTypeDef,
    GetAggregateConfigRuleComplianceSummaryResponseTypeDef,
    GetAggregateConformancePackComplianceSummaryResponseTypeDef,
    GetAggregateDiscoveredResourceCountsResponseTypeDef,
    GetAggregateResourceConfigResponseTypeDef,
    GetComplianceDetailsByConfigRuleResponseTypeDef,
    GetComplianceDetailsByResourceResponseTypeDef,
    GetComplianceSummaryByConfigRuleResponseTypeDef,
    GetComplianceSummaryByResourceTypeResponseTypeDef,
    GetConformancePackComplianceDetailsResponseTypeDef,
    GetConformancePackComplianceSummaryResponseTypeDef,
    GetDiscoveredResourceCountsResponseTypeDef,
    GetOrganizationConfigRuleDetailedStatusResponseTypeDef,
    GetOrganizationConformancePackDetailedStatusResponseTypeDef,
    GetResourceConfigHistoryResponseTypeDef,
    GetStoredQueryResponseTypeDef,
    ListAggregateDiscoveredResourcesResponseTypeDef,
    ListDiscoveredResourcesResponseTypeDef,
    ListStoredQueriesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    OrganizationAggregationSourceTypeDef,
    OrganizationCustomRuleMetadataTypeDef,
    OrganizationManagedRuleMetadataTypeDef,
    OrganizationResourceDetailedStatusFiltersTypeDef,
    PutAggregationAuthorizationResponseTypeDef,
    PutConfigurationAggregatorResponseTypeDef,
    PutConformancePackResponseTypeDef,
    PutEvaluationsResponseTypeDef,
    PutOrganizationConfigRuleResponseTypeDef,
    PutOrganizationConformancePackResponseTypeDef,
    PutRemediationConfigurationsResponseTypeDef,
    PutRemediationExceptionsResponseTypeDef,
    PutRetentionConfigurationResponseTypeDef,
    PutStoredQueryResponseTypeDef,
    RemediationConfigurationTypeDef,
    RemediationExceptionResourceKeyTypeDef,
    ResourceCountFiltersTypeDef,
    ResourceFiltersTypeDef,
    ResourceKeyTypeDef,
    SelectAggregateResourceConfigResponseTypeDef,
    SelectResourceConfigResponseTypeDef,
    StartRemediationExecutionResponseTypeDef,
    StatusDetailFiltersTypeDef,
    StoredQueryTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ConfigServiceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConformancePackTemplateValidationException: Type[BotocoreClientError]
    InsufficientDeliveryPolicyException: Type[BotocoreClientError]
    InsufficientPermissionsException: Type[BotocoreClientError]
    InvalidConfigurationRecorderNameException: Type[BotocoreClientError]
    InvalidDeliveryChannelNameException: Type[BotocoreClientError]
    InvalidExpressionException: Type[BotocoreClientError]
    InvalidLimitException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidRecordingGroupException: Type[BotocoreClientError]
    InvalidResultTokenException: Type[BotocoreClientError]
    InvalidRoleException: Type[BotocoreClientError]
    InvalidS3KeyPrefixException: Type[BotocoreClientError]
    InvalidS3KmsKeyArnException: Type[BotocoreClientError]
    InvalidSNSTopicARNException: Type[BotocoreClientError]
    InvalidTimeRangeException: Type[BotocoreClientError]
    LastDeliveryChannelDeleteFailedException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MaxActiveResourcesExceededException: Type[BotocoreClientError]
    MaxNumberOfConfigRulesExceededException: Type[BotocoreClientError]
    MaxNumberOfConfigurationRecordersExceededException: Type[BotocoreClientError]
    MaxNumberOfConformancePacksExceededException: Type[BotocoreClientError]
    MaxNumberOfDeliveryChannelsExceededException: Type[BotocoreClientError]
    MaxNumberOfOrganizationConfigRulesExceededException: Type[BotocoreClientError]
    MaxNumberOfOrganizationConformancePacksExceededException: Type[BotocoreClientError]
    MaxNumberOfRetentionConfigurationsExceededException: Type[BotocoreClientError]
    NoAvailableConfigurationRecorderException: Type[BotocoreClientError]
    NoAvailableDeliveryChannelException: Type[BotocoreClientError]
    NoAvailableOrganizationException: Type[BotocoreClientError]
    NoRunningConfigurationRecorderException: Type[BotocoreClientError]
    NoSuchBucketException: Type[BotocoreClientError]
    NoSuchConfigRuleException: Type[BotocoreClientError]
    NoSuchConfigRuleInConformancePackException: Type[BotocoreClientError]
    NoSuchConfigurationAggregatorException: Type[BotocoreClientError]
    NoSuchConfigurationRecorderException: Type[BotocoreClientError]
    NoSuchConformancePackException: Type[BotocoreClientError]
    NoSuchDeliveryChannelException: Type[BotocoreClientError]
    NoSuchOrganizationConfigRuleException: Type[BotocoreClientError]
    NoSuchOrganizationConformancePackException: Type[BotocoreClientError]
    NoSuchRemediationConfigurationException: Type[BotocoreClientError]
    NoSuchRemediationExceptionException: Type[BotocoreClientError]
    NoSuchRetentionConfigurationException: Type[BotocoreClientError]
    OrganizationAccessDeniedException: Type[BotocoreClientError]
    OrganizationAllFeaturesNotEnabledException: Type[BotocoreClientError]
    OrganizationConformancePackTemplateValidationException: Type[BotocoreClientError]
    OversizedConfigurationItemException: Type[BotocoreClientError]
    RemediationInProgressException: Type[BotocoreClientError]
    ResourceConcurrentModificationException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotDiscoveredException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class ConfigServiceClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_get_aggregate_resource_config(
        self,
        *,
        ConfigurationAggregatorName: str,
        ResourceIdentifiers: List["AggregateResourceIdentifierTypeDef"]
    ) -> BatchGetAggregateResourceConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.batch_get_aggregate_resource_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#batch_get_aggregate_resource_config)
        """

    def batch_get_resource_config(
        self, *, resourceKeys: List["ResourceKeyTypeDef"]
    ) -> BatchGetResourceConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.batch_get_resource_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#batch_get_resource_config)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#can_paginate)
        """

    def delete_aggregation_authorization(
        self, *, AuthorizedAccountId: str, AuthorizedAwsRegion: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.delete_aggregation_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#delete_aggregation_authorization)
        """

    def delete_config_rule(self, *, ConfigRuleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.delete_config_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#delete_config_rule)
        """

    def delete_configuration_aggregator(self, *, ConfigurationAggregatorName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.delete_configuration_aggregator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#delete_configuration_aggregator)
        """

    def delete_configuration_recorder(self, *, ConfigurationRecorderName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.delete_configuration_recorder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#delete_configuration_recorder)
        """

    def delete_conformance_pack(self, *, ConformancePackName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.delete_conformance_pack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#delete_conformance_pack)
        """

    def delete_delivery_channel(self, *, DeliveryChannelName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.delete_delivery_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#delete_delivery_channel)
        """

    def delete_evaluation_results(self, *, ConfigRuleName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.delete_evaluation_results)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#delete_evaluation_results)
        """

    def delete_organization_config_rule(self, *, OrganizationConfigRuleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.delete_organization_config_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#delete_organization_config_rule)
        """

    def delete_organization_conformance_pack(self, *, OrganizationConformancePackName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.delete_organization_conformance_pack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#delete_organization_conformance_pack)
        """

    def delete_pending_aggregation_request(
        self, *, RequesterAccountId: str, RequesterAwsRegion: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.delete_pending_aggregation_request)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#delete_pending_aggregation_request)
        """

    def delete_remediation_configuration(
        self, *, ConfigRuleName: str, ResourceType: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.delete_remediation_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#delete_remediation_configuration)
        """

    def delete_remediation_exceptions(
        self, *, ConfigRuleName: str, ResourceKeys: List["RemediationExceptionResourceKeyTypeDef"]
    ) -> DeleteRemediationExceptionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.delete_remediation_exceptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#delete_remediation_exceptions)
        """

    def delete_resource_config(self, *, ResourceType: str, ResourceId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.delete_resource_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#delete_resource_config)
        """

    def delete_retention_configuration(self, *, RetentionConfigurationName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.delete_retention_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#delete_retention_configuration)
        """

    def delete_stored_query(self, *, QueryName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.delete_stored_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#delete_stored_query)
        """

    def deliver_config_snapshot(
        self, *, deliveryChannelName: str
    ) -> DeliverConfigSnapshotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.deliver_config_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#deliver_config_snapshot)
        """

    def describe_aggregate_compliance_by_config_rules(
        self,
        *,
        ConfigurationAggregatorName: str,
        Filters: ConfigRuleComplianceFiltersTypeDef = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribeAggregateComplianceByConfigRulesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_aggregate_compliance_by_config_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_aggregate_compliance_by_config_rules)
        """

    def describe_aggregate_compliance_by_conformance_packs(
        self,
        *,
        ConfigurationAggregatorName: str,
        Filters: AggregateConformancePackComplianceFiltersTypeDef = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribeAggregateComplianceByConformancePacksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_aggregate_compliance_by_conformance_packs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_aggregate_compliance_by_conformance_packs)
        """

    def describe_aggregation_authorizations(
        self, *, Limit: int = None, NextToken: str = None
    ) -> DescribeAggregationAuthorizationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_aggregation_authorizations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_aggregation_authorizations)
        """

    def describe_compliance_by_config_rule(
        self,
        *,
        ConfigRuleNames: List[str] = None,
        ComplianceTypes: List[ComplianceTypeType] = None,
        NextToken: str = None
    ) -> DescribeComplianceByConfigRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_compliance_by_config_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_compliance_by_config_rule)
        """

    def describe_compliance_by_resource(
        self,
        *,
        ResourceType: str = None,
        ResourceId: str = None,
        ComplianceTypes: List[ComplianceTypeType] = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribeComplianceByResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_compliance_by_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_compliance_by_resource)
        """

    def describe_config_rule_evaluation_status(
        self, *, ConfigRuleNames: List[str] = None, NextToken: str = None, Limit: int = None
    ) -> DescribeConfigRuleEvaluationStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_config_rule_evaluation_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_config_rule_evaluation_status)
        """

    def describe_config_rules(
        self, *, ConfigRuleNames: List[str] = None, NextToken: str = None
    ) -> DescribeConfigRulesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_config_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_config_rules)
        """

    def describe_configuration_aggregator_sources_status(
        self,
        *,
        ConfigurationAggregatorName: str,
        UpdateStatus: List[AggregatedSourceStatusTypeType] = None,
        NextToken: str = None,
        Limit: int = None
    ) -> DescribeConfigurationAggregatorSourcesStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_configuration_aggregator_sources_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_configuration_aggregator_sources_status)
        """

    def describe_configuration_aggregators(
        self,
        *,
        ConfigurationAggregatorNames: List[str] = None,
        NextToken: str = None,
        Limit: int = None
    ) -> DescribeConfigurationAggregatorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_configuration_aggregators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_configuration_aggregators)
        """

    def describe_configuration_recorder_status(
        self, *, ConfigurationRecorderNames: List[str] = None
    ) -> DescribeConfigurationRecorderStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_configuration_recorder_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_configuration_recorder_status)
        """

    def describe_configuration_recorders(
        self, *, ConfigurationRecorderNames: List[str] = None
    ) -> DescribeConfigurationRecordersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_configuration_recorders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_configuration_recorders)
        """

    def describe_conformance_pack_compliance(
        self,
        *,
        ConformancePackName: str,
        Filters: ConformancePackComplianceFiltersTypeDef = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribeConformancePackComplianceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_conformance_pack_compliance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_conformance_pack_compliance)
        """

    def describe_conformance_pack_status(
        self, *, ConformancePackNames: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeConformancePackStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_conformance_pack_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_conformance_pack_status)
        """

    def describe_conformance_packs(
        self, *, ConformancePackNames: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeConformancePacksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_conformance_packs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_conformance_packs)
        """

    def describe_delivery_channel_status(
        self, *, DeliveryChannelNames: List[str] = None
    ) -> DescribeDeliveryChannelStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_delivery_channel_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_delivery_channel_status)
        """

    def describe_delivery_channels(
        self, *, DeliveryChannelNames: List[str] = None
    ) -> DescribeDeliveryChannelsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_delivery_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_delivery_channels)
        """

    def describe_organization_config_rule_statuses(
        self,
        *,
        OrganizationConfigRuleNames: List[str] = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribeOrganizationConfigRuleStatusesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_organization_config_rule_statuses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_organization_config_rule_statuses)
        """

    def describe_organization_config_rules(
        self,
        *,
        OrganizationConfigRuleNames: List[str] = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribeOrganizationConfigRulesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_organization_config_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_organization_config_rules)
        """

    def describe_organization_conformance_pack_statuses(
        self,
        *,
        OrganizationConformancePackNames: List[str] = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribeOrganizationConformancePackStatusesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_organization_conformance_pack_statuses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_organization_conformance_pack_statuses)
        """

    def describe_organization_conformance_packs(
        self,
        *,
        OrganizationConformancePackNames: List[str] = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribeOrganizationConformancePacksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_organization_conformance_packs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_organization_conformance_packs)
        """

    def describe_pending_aggregation_requests(
        self, *, Limit: int = None, NextToken: str = None
    ) -> DescribePendingAggregationRequestsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_pending_aggregation_requests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_pending_aggregation_requests)
        """

    def describe_remediation_configurations(
        self, *, ConfigRuleNames: List[str]
    ) -> DescribeRemediationConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_remediation_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_remediation_configurations)
        """

    def describe_remediation_exceptions(
        self,
        *,
        ConfigRuleName: str,
        ResourceKeys: List["RemediationExceptionResourceKeyTypeDef"] = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribeRemediationExceptionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_remediation_exceptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_remediation_exceptions)
        """

    def describe_remediation_execution_status(
        self,
        *,
        ConfigRuleName: str,
        ResourceKeys: List["ResourceKeyTypeDef"] = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribeRemediationExecutionStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_remediation_execution_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_remediation_execution_status)
        """

    def describe_retention_configurations(
        self, *, RetentionConfigurationNames: List[str] = None, NextToken: str = None
    ) -> DescribeRetentionConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.describe_retention_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#describe_retention_configurations)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#generate_presigned_url)
        """

    def get_aggregate_compliance_details_by_config_rule(
        self,
        *,
        ConfigurationAggregatorName: str,
        ConfigRuleName: str,
        AccountId: str,
        AwsRegion: str,
        ComplianceType: ComplianceTypeType = None,
        Limit: int = None,
        NextToken: str = None
    ) -> GetAggregateComplianceDetailsByConfigRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.get_aggregate_compliance_details_by_config_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#get_aggregate_compliance_details_by_config_rule)
        """

    def get_aggregate_config_rule_compliance_summary(
        self,
        *,
        ConfigurationAggregatorName: str,
        Filters: ConfigRuleComplianceSummaryFiltersTypeDef = None,
        GroupByKey: ConfigRuleComplianceSummaryGroupKeyType = None,
        Limit: int = None,
        NextToken: str = None
    ) -> GetAggregateConfigRuleComplianceSummaryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.get_aggregate_config_rule_compliance_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#get_aggregate_config_rule_compliance_summary)
        """

    def get_aggregate_conformance_pack_compliance_summary(
        self,
        *,
        ConfigurationAggregatorName: str,
        Filters: AggregateConformancePackComplianceSummaryFiltersTypeDef = None,
        GroupByKey: AggregateConformancePackComplianceSummaryGroupKeyType = None,
        Limit: int = None,
        NextToken: str = None
    ) -> GetAggregateConformancePackComplianceSummaryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.get_aggregate_conformance_pack_compliance_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#get_aggregate_conformance_pack_compliance_summary)
        """

    def get_aggregate_discovered_resource_counts(
        self,
        *,
        ConfigurationAggregatorName: str,
        Filters: ResourceCountFiltersTypeDef = None,
        GroupByKey: ResourceCountGroupKeyType = None,
        Limit: int = None,
        NextToken: str = None
    ) -> GetAggregateDiscoveredResourceCountsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.get_aggregate_discovered_resource_counts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#get_aggregate_discovered_resource_counts)
        """

    def get_aggregate_resource_config(
        self,
        *,
        ConfigurationAggregatorName: str,
        ResourceIdentifier: "AggregateResourceIdentifierTypeDef"
    ) -> GetAggregateResourceConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.get_aggregate_resource_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#get_aggregate_resource_config)
        """

    def get_compliance_details_by_config_rule(
        self,
        *,
        ConfigRuleName: str,
        ComplianceTypes: List[ComplianceTypeType] = None,
        Limit: int = None,
        NextToken: str = None
    ) -> GetComplianceDetailsByConfigRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.get_compliance_details_by_config_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#get_compliance_details_by_config_rule)
        """

    def get_compliance_details_by_resource(
        self,
        *,
        ResourceType: str,
        ResourceId: str,
        ComplianceTypes: List[ComplianceTypeType] = None,
        NextToken: str = None
    ) -> GetComplianceDetailsByResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.get_compliance_details_by_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#get_compliance_details_by_resource)
        """

    def get_compliance_summary_by_config_rule(
        self,
    ) -> GetComplianceSummaryByConfigRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.get_compliance_summary_by_config_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#get_compliance_summary_by_config_rule)
        """

    def get_compliance_summary_by_resource_type(
        self, *, ResourceTypes: List[str] = None
    ) -> GetComplianceSummaryByResourceTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.get_compliance_summary_by_resource_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#get_compliance_summary_by_resource_type)
        """

    def get_conformance_pack_compliance_details(
        self,
        *,
        ConformancePackName: str,
        Filters: ConformancePackEvaluationFiltersTypeDef = None,
        Limit: int = None,
        NextToken: str = None
    ) -> GetConformancePackComplianceDetailsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.get_conformance_pack_compliance_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#get_conformance_pack_compliance_details)
        """

    def get_conformance_pack_compliance_summary(
        self, *, ConformancePackNames: List[str], Limit: int = None, NextToken: str = None
    ) -> GetConformancePackComplianceSummaryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.get_conformance_pack_compliance_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#get_conformance_pack_compliance_summary)
        """

    def get_discovered_resource_counts(
        self, *, resourceTypes: List[str] = None, limit: int = None, nextToken: str = None
    ) -> GetDiscoveredResourceCountsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.get_discovered_resource_counts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#get_discovered_resource_counts)
        """

    def get_organization_config_rule_detailed_status(
        self,
        *,
        OrganizationConfigRuleName: str,
        Filters: StatusDetailFiltersTypeDef = None,
        Limit: int = None,
        NextToken: str = None
    ) -> GetOrganizationConfigRuleDetailedStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.get_organization_config_rule_detailed_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#get_organization_config_rule_detailed_status)
        """

    def get_organization_conformance_pack_detailed_status(
        self,
        *,
        OrganizationConformancePackName: str,
        Filters: OrganizationResourceDetailedStatusFiltersTypeDef = None,
        Limit: int = None,
        NextToken: str = None
    ) -> GetOrganizationConformancePackDetailedStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.get_organization_conformance_pack_detailed_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#get_organization_conformance_pack_detailed_status)
        """

    def get_resource_config_history(
        self,
        *,
        resourceType: ResourceTypeType,
        resourceId: str,
        laterTime: datetime = None,
        earlierTime: datetime = None,
        chronologicalOrder: ChronologicalOrderType = None,
        limit: int = None,
        nextToken: str = None
    ) -> GetResourceConfigHistoryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.get_resource_config_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#get_resource_config_history)
        """

    def get_stored_query(self, *, QueryName: str) -> GetStoredQueryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.get_stored_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#get_stored_query)
        """

    def list_aggregate_discovered_resources(
        self,
        *,
        ConfigurationAggregatorName: str,
        ResourceType: ResourceTypeType,
        Filters: ResourceFiltersTypeDef = None,
        Limit: int = None,
        NextToken: str = None
    ) -> ListAggregateDiscoveredResourcesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.list_aggregate_discovered_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#list_aggregate_discovered_resources)
        """

    def list_discovered_resources(
        self,
        *,
        resourceType: ResourceTypeType,
        resourceIds: List[str] = None,
        resourceName: str = None,
        limit: int = None,
        includeDeletedResources: bool = None,
        nextToken: str = None
    ) -> ListDiscoveredResourcesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.list_discovered_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#list_discovered_resources)
        """

    def list_stored_queries(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListStoredQueriesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.list_stored_queries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#list_stored_queries)
        """

    def list_tags_for_resource(
        self, *, ResourceArn: str, Limit: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#list_tags_for_resource)
        """

    def put_aggregation_authorization(
        self, *, AuthorizedAccountId: str, AuthorizedAwsRegion: str, Tags: List["TagTypeDef"] = None
    ) -> PutAggregationAuthorizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.put_aggregation_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#put_aggregation_authorization)
        """

    def put_config_rule(
        self, *, ConfigRule: "ConfigRuleTypeDef", Tags: List["TagTypeDef"] = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.put_config_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#put_config_rule)
        """

    def put_configuration_aggregator(
        self,
        *,
        ConfigurationAggregatorName: str,
        AccountAggregationSources: List["AccountAggregationSourceTypeDef"] = None,
        OrganizationAggregationSource: "OrganizationAggregationSourceTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> PutConfigurationAggregatorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.put_configuration_aggregator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#put_configuration_aggregator)
        """

    def put_configuration_recorder(
        self, *, ConfigurationRecorder: "ConfigurationRecorderTypeDef"
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.put_configuration_recorder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#put_configuration_recorder)
        """

    def put_conformance_pack(
        self,
        *,
        ConformancePackName: str,
        TemplateS3Uri: str = None,
        TemplateBody: str = None,
        DeliveryS3Bucket: str = None,
        DeliveryS3KeyPrefix: str = None,
        ConformancePackInputParameters: List["ConformancePackInputParameterTypeDef"] = None
    ) -> PutConformancePackResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.put_conformance_pack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#put_conformance_pack)
        """

    def put_delivery_channel(self, *, DeliveryChannel: "DeliveryChannelTypeDef") -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.put_delivery_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#put_delivery_channel)
        """

    def put_evaluations(
        self,
        *,
        ResultToken: str,
        Evaluations: List["EvaluationTypeDef"] = None,
        TestMode: bool = None
    ) -> PutEvaluationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.put_evaluations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#put_evaluations)
        """

    def put_external_evaluation(
        self, *, ConfigRuleName: str, ExternalEvaluation: ExternalEvaluationTypeDef
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.put_external_evaluation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#put_external_evaluation)
        """

    def put_organization_config_rule(
        self,
        *,
        OrganizationConfigRuleName: str,
        OrganizationManagedRuleMetadata: "OrganizationManagedRuleMetadataTypeDef" = None,
        OrganizationCustomRuleMetadata: "OrganizationCustomRuleMetadataTypeDef" = None,
        ExcludedAccounts: List[str] = None
    ) -> PutOrganizationConfigRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.put_organization_config_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#put_organization_config_rule)
        """

    def put_organization_conformance_pack(
        self,
        *,
        OrganizationConformancePackName: str,
        TemplateS3Uri: str = None,
        TemplateBody: str = None,
        DeliveryS3Bucket: str = None,
        DeliveryS3KeyPrefix: str = None,
        ConformancePackInputParameters: List["ConformancePackInputParameterTypeDef"] = None,
        ExcludedAccounts: List[str] = None
    ) -> PutOrganizationConformancePackResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.put_organization_conformance_pack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#put_organization_conformance_pack)
        """

    def put_remediation_configurations(
        self, *, RemediationConfigurations: List["RemediationConfigurationTypeDef"]
    ) -> PutRemediationConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.put_remediation_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#put_remediation_configurations)
        """

    def put_remediation_exceptions(
        self,
        *,
        ConfigRuleName: str,
        ResourceKeys: List["RemediationExceptionResourceKeyTypeDef"],
        Message: str = None,
        ExpirationTime: datetime = None
    ) -> PutRemediationExceptionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.put_remediation_exceptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#put_remediation_exceptions)
        """

    def put_resource_config(
        self,
        *,
        ResourceType: str,
        SchemaVersionId: str,
        ResourceId: str,
        Configuration: str,
        ResourceName: str = None,
        Tags: Dict[str, str] = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.put_resource_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#put_resource_config)
        """

    def put_retention_configuration(
        self, *, RetentionPeriodInDays: int
    ) -> PutRetentionConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.put_retention_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#put_retention_configuration)
        """

    def put_stored_query(
        self, *, StoredQuery: "StoredQueryTypeDef", Tags: List["TagTypeDef"] = None
    ) -> PutStoredQueryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.put_stored_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#put_stored_query)
        """

    def select_aggregate_resource_config(
        self,
        *,
        Expression: str,
        ConfigurationAggregatorName: str,
        Limit: int = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> SelectAggregateResourceConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.select_aggregate_resource_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#select_aggregate_resource_config)
        """

    def select_resource_config(
        self, *, Expression: str, Limit: int = None, NextToken: str = None
    ) -> SelectResourceConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.select_resource_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#select_resource_config)
        """

    def start_config_rules_evaluation(self, *, ConfigRuleNames: List[str] = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.start_config_rules_evaluation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#start_config_rules_evaluation)
        """

    def start_configuration_recorder(self, *, ConfigurationRecorderName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.start_configuration_recorder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#start_configuration_recorder)
        """

    def start_remediation_execution(
        self, *, ConfigRuleName: str, ResourceKeys: List["ResourceKeyTypeDef"]
    ) -> StartRemediationExecutionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.start_remediation_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#start_remediation_execution)
        """

    def stop_configuration_recorder(self, *, ConfigurationRecorderName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.stop_configuration_recorder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#stop_configuration_recorder)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/client.html#untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_aggregate_compliance_by_config_rules"]
    ) -> DescribeAggregateComplianceByConfigRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.DescribeAggregateComplianceByConfigRules)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeaggregatecompliancebyconfigrulespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_aggregate_compliance_by_conformance_packs"]
    ) -> DescribeAggregateComplianceByConformancePacksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.DescribeAggregateComplianceByConformancePacks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeaggregatecompliancebyconformancepackspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_aggregation_authorizations"]
    ) -> DescribeAggregationAuthorizationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.DescribeAggregationAuthorizations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeaggregationauthorizationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_compliance_by_config_rule"]
    ) -> DescribeComplianceByConfigRulePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByConfigRule)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describecompliancebyconfigrulepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_compliance_by_resource"]
    ) -> DescribeComplianceByResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describecompliancebyresourcepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_config_rule_evaluation_status"]
    ) -> DescribeConfigRuleEvaluationStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.DescribeConfigRuleEvaluationStatus)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeconfigruleevaluationstatuspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_config_rules"]
    ) -> DescribeConfigRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.DescribeConfigRules)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeconfigrulespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_configuration_aggregator_sources_status"]
    ) -> DescribeConfigurationAggregatorSourcesStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregatorSourcesStatus)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeconfigurationaggregatorsourcesstatuspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_configuration_aggregators"]
    ) -> DescribeConfigurationAggregatorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregators)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeconfigurationaggregatorspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_conformance_pack_status"]
    ) -> DescribeConformancePackStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.DescribeConformancePackStatus)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeconformancepackstatuspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_conformance_packs"]
    ) -> DescribeConformancePacksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.DescribeConformancePacks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeconformancepackspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_organization_config_rule_statuses"]
    ) -> DescribeOrganizationConfigRuleStatusesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.DescribeOrganizationConfigRuleStatuses)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeorganizationconfigrulestatusespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_organization_config_rules"]
    ) -> DescribeOrganizationConfigRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.DescribeOrganizationConfigRules)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeorganizationconfigrulespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_organization_conformance_pack_statuses"]
    ) -> DescribeOrganizationConformancePackStatusesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.DescribeOrganizationConformancePackStatuses)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeorganizationconformancepackstatusespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_organization_conformance_packs"]
    ) -> DescribeOrganizationConformancePacksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.DescribeOrganizationConformancePacks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeorganizationconformancepackspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_pending_aggregation_requests"]
    ) -> DescribePendingAggregationRequestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.DescribePendingAggregationRequests)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describependingaggregationrequestspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_remediation_execution_status"]
    ) -> DescribeRemediationExecutionStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.DescribeRemediationExecutionStatus)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeremediationexecutionstatuspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_retention_configurations"]
    ) -> DescribeRetentionConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.DescribeRetentionConfigurations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeretentionconfigurationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_aggregate_compliance_details_by_config_rule"]
    ) -> GetAggregateComplianceDetailsByConfigRulePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.GetAggregateComplianceDetailsByConfigRule)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getaggregatecompliancedetailsbyconfigrulepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_compliance_details_by_config_rule"]
    ) -> GetComplianceDetailsByConfigRulePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByConfigRule)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getcompliancedetailsbyconfigrulepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_compliance_details_by_resource"]
    ) -> GetComplianceDetailsByResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getcompliancedetailsbyresourcepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_conformance_pack_compliance_summary"]
    ) -> GetConformancePackComplianceSummaryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.GetConformancePackComplianceSummary)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getconformancepackcompliancesummarypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_organization_config_rule_detailed_status"]
    ) -> GetOrganizationConfigRuleDetailedStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.GetOrganizationConfigRuleDetailedStatus)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getorganizationconfigruledetailedstatuspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_organization_conformance_pack_detailed_status"]
    ) -> GetOrganizationConformancePackDetailedStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.GetOrganizationConformancePackDetailedStatus)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getorganizationconformancepackdetailedstatuspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_resource_config_history"]
    ) -> GetResourceConfigHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.GetResourceConfigHistory)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getresourceconfighistorypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_aggregate_discovered_resources"]
    ) -> ListAggregateDiscoveredResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.ListAggregateDiscoveredResources)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#listaggregatediscoveredresourcespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_discovered_resources"]
    ) -> ListDiscoveredResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.ListDiscoveredResources)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#listdiscoveredresourcespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.ListTagsForResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#listtagsforresourcepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["select_aggregate_resource_config"]
    ) -> SelectAggregateResourceConfigPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.SelectAggregateResourceConfig)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#selectaggregateresourceconfigpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["select_resource_config"]
    ) -> SelectResourceConfigPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/config.html#ConfigService.Paginator.SelectResourceConfig)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#selectresourceconfigpaginator)
        """
