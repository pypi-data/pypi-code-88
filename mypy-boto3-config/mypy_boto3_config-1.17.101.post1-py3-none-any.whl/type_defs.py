"""
Type annotations for config service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/type_defs.html)

Usage::

    ```python
    from mypy_boto3_config.type_defs import AccountAggregationSourceTypeDef

    data: AccountAggregationSourceTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AggregateConformancePackComplianceSummaryGroupKeyType,
    AggregatedSourceStatusTypeType,
    AggregatedSourceTypeType,
    ChronologicalOrderType,
    ComplianceTypeType,
    ConfigRuleComplianceSummaryGroupKeyType,
    ConfigRuleStateType,
    ConfigurationItemStatusType,
    ConformancePackComplianceTypeType,
    ConformancePackStateType,
    DeliveryStatusType,
    MaximumExecutionFrequencyType,
    MemberAccountRuleStatusType,
    MessageTypeType,
    OrganizationConfigRuleTriggerTypeType,
    OrganizationResourceDetailedStatusType,
    OrganizationResourceStatusType,
    OrganizationRuleStatusType,
    OwnerType,
    RecorderStatusType,
    RemediationExecutionStateType,
    RemediationExecutionStepStateType,
    ResourceCountGroupKeyType,
    ResourceTypeType,
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
    "AccountAggregationSourceTypeDef",
    "AggregateComplianceByConfigRuleTypeDef",
    "AggregateComplianceByConformancePackTypeDef",
    "AggregateComplianceCountTypeDef",
    "AggregateConformancePackComplianceCountTypeDef",
    "AggregateConformancePackComplianceFiltersTypeDef",
    "AggregateConformancePackComplianceSummaryFiltersTypeDef",
    "AggregateConformancePackComplianceSummaryTypeDef",
    "AggregateConformancePackComplianceTypeDef",
    "AggregateEvaluationResultTypeDef",
    "AggregateResourceIdentifierTypeDef",
    "AggregatedSourceStatusTypeDef",
    "AggregationAuthorizationTypeDef",
    "BaseConfigurationItemTypeDef",
    "BatchGetAggregateResourceConfigRequestTypeDef",
    "BatchGetAggregateResourceConfigResponseResponseTypeDef",
    "BatchGetResourceConfigRequestTypeDef",
    "BatchGetResourceConfigResponseResponseTypeDef",
    "ComplianceByConfigRuleTypeDef",
    "ComplianceByResourceTypeDef",
    "ComplianceContributorCountTypeDef",
    "ComplianceSummaryByResourceTypeTypeDef",
    "ComplianceSummaryTypeDef",
    "ComplianceTypeDef",
    "ConfigExportDeliveryInfoTypeDef",
    "ConfigRuleComplianceFiltersTypeDef",
    "ConfigRuleComplianceSummaryFiltersTypeDef",
    "ConfigRuleEvaluationStatusTypeDef",
    "ConfigRuleTypeDef",
    "ConfigSnapshotDeliveryPropertiesTypeDef",
    "ConfigStreamDeliveryInfoTypeDef",
    "ConfigurationAggregatorTypeDef",
    "ConfigurationItemTypeDef",
    "ConfigurationRecorderStatusTypeDef",
    "ConfigurationRecorderTypeDef",
    "ConformancePackComplianceFiltersTypeDef",
    "ConformancePackComplianceSummaryTypeDef",
    "ConformancePackDetailTypeDef",
    "ConformancePackEvaluationFiltersTypeDef",
    "ConformancePackEvaluationResultTypeDef",
    "ConformancePackInputParameterTypeDef",
    "ConformancePackRuleComplianceTypeDef",
    "ConformancePackStatusDetailTypeDef",
    "DeleteAggregationAuthorizationRequestTypeDef",
    "DeleteConfigRuleRequestTypeDef",
    "DeleteConfigurationAggregatorRequestTypeDef",
    "DeleteConfigurationRecorderRequestTypeDef",
    "DeleteConformancePackRequestTypeDef",
    "DeleteDeliveryChannelRequestTypeDef",
    "DeleteEvaluationResultsRequestTypeDef",
    "DeleteOrganizationConfigRuleRequestTypeDef",
    "DeleteOrganizationConformancePackRequestTypeDef",
    "DeletePendingAggregationRequestRequestTypeDef",
    "DeleteRemediationConfigurationRequestTypeDef",
    "DeleteRemediationExceptionsRequestTypeDef",
    "DeleteRemediationExceptionsResponseResponseTypeDef",
    "DeleteResourceConfigRequestTypeDef",
    "DeleteRetentionConfigurationRequestTypeDef",
    "DeleteStoredQueryRequestTypeDef",
    "DeliverConfigSnapshotRequestTypeDef",
    "DeliverConfigSnapshotResponseResponseTypeDef",
    "DeliveryChannelStatusTypeDef",
    "DeliveryChannelTypeDef",
    "DescribeAggregateComplianceByConfigRulesRequestTypeDef",
    "DescribeAggregateComplianceByConfigRulesResponseResponseTypeDef",
    "DescribeAggregateComplianceByConformancePacksRequestTypeDef",
    "DescribeAggregateComplianceByConformancePacksResponseResponseTypeDef",
    "DescribeAggregationAuthorizationsRequestTypeDef",
    "DescribeAggregationAuthorizationsResponseResponseTypeDef",
    "DescribeComplianceByConfigRuleRequestTypeDef",
    "DescribeComplianceByConfigRuleResponseResponseTypeDef",
    "DescribeComplianceByResourceRequestTypeDef",
    "DescribeComplianceByResourceResponseResponseTypeDef",
    "DescribeConfigRuleEvaluationStatusRequestTypeDef",
    "DescribeConfigRuleEvaluationStatusResponseResponseTypeDef",
    "DescribeConfigRulesRequestTypeDef",
    "DescribeConfigRulesResponseResponseTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusRequestTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusResponseResponseTypeDef",
    "DescribeConfigurationAggregatorsRequestTypeDef",
    "DescribeConfigurationAggregatorsResponseResponseTypeDef",
    "DescribeConfigurationRecorderStatusRequestTypeDef",
    "DescribeConfigurationRecorderStatusResponseResponseTypeDef",
    "DescribeConfigurationRecordersRequestTypeDef",
    "DescribeConfigurationRecordersResponseResponseTypeDef",
    "DescribeConformancePackComplianceRequestTypeDef",
    "DescribeConformancePackComplianceResponseResponseTypeDef",
    "DescribeConformancePackStatusRequestTypeDef",
    "DescribeConformancePackStatusResponseResponseTypeDef",
    "DescribeConformancePacksRequestTypeDef",
    "DescribeConformancePacksResponseResponseTypeDef",
    "DescribeDeliveryChannelStatusRequestTypeDef",
    "DescribeDeliveryChannelStatusResponseResponseTypeDef",
    "DescribeDeliveryChannelsRequestTypeDef",
    "DescribeDeliveryChannelsResponseResponseTypeDef",
    "DescribeOrganizationConfigRuleStatusesRequestTypeDef",
    "DescribeOrganizationConfigRuleStatusesResponseResponseTypeDef",
    "DescribeOrganizationConfigRulesRequestTypeDef",
    "DescribeOrganizationConfigRulesResponseResponseTypeDef",
    "DescribeOrganizationConformancePackStatusesRequestTypeDef",
    "DescribeOrganizationConformancePackStatusesResponseResponseTypeDef",
    "DescribeOrganizationConformancePacksRequestTypeDef",
    "DescribeOrganizationConformancePacksResponseResponseTypeDef",
    "DescribePendingAggregationRequestsRequestTypeDef",
    "DescribePendingAggregationRequestsResponseResponseTypeDef",
    "DescribeRemediationConfigurationsRequestTypeDef",
    "DescribeRemediationConfigurationsResponseResponseTypeDef",
    "DescribeRemediationExceptionsRequestTypeDef",
    "DescribeRemediationExceptionsResponseResponseTypeDef",
    "DescribeRemediationExecutionStatusRequestTypeDef",
    "DescribeRemediationExecutionStatusResponseResponseTypeDef",
    "DescribeRetentionConfigurationsRequestTypeDef",
    "DescribeRetentionConfigurationsResponseResponseTypeDef",
    "EvaluationResultIdentifierTypeDef",
    "EvaluationResultQualifierTypeDef",
    "EvaluationResultTypeDef",
    "EvaluationTypeDef",
    "ExecutionControlsTypeDef",
    "ExternalEvaluationTypeDef",
    "FailedDeleteRemediationExceptionsBatchTypeDef",
    "FailedRemediationBatchTypeDef",
    "FailedRemediationExceptionBatchTypeDef",
    "FieldInfoTypeDef",
    "GetAggregateComplianceDetailsByConfigRuleRequestTypeDef",
    "GetAggregateComplianceDetailsByConfigRuleResponseResponseTypeDef",
    "GetAggregateConfigRuleComplianceSummaryRequestTypeDef",
    "GetAggregateConfigRuleComplianceSummaryResponseResponseTypeDef",
    "GetAggregateConformancePackComplianceSummaryRequestTypeDef",
    "GetAggregateConformancePackComplianceSummaryResponseResponseTypeDef",
    "GetAggregateDiscoveredResourceCountsRequestTypeDef",
    "GetAggregateDiscoveredResourceCountsResponseResponseTypeDef",
    "GetAggregateResourceConfigRequestTypeDef",
    "GetAggregateResourceConfigResponseResponseTypeDef",
    "GetComplianceDetailsByConfigRuleRequestTypeDef",
    "GetComplianceDetailsByConfigRuleResponseResponseTypeDef",
    "GetComplianceDetailsByResourceRequestTypeDef",
    "GetComplianceDetailsByResourceResponseResponseTypeDef",
    "GetComplianceSummaryByConfigRuleResponseResponseTypeDef",
    "GetComplianceSummaryByResourceTypeRequestTypeDef",
    "GetComplianceSummaryByResourceTypeResponseResponseTypeDef",
    "GetConformancePackComplianceDetailsRequestTypeDef",
    "GetConformancePackComplianceDetailsResponseResponseTypeDef",
    "GetConformancePackComplianceSummaryRequestTypeDef",
    "GetConformancePackComplianceSummaryResponseResponseTypeDef",
    "GetDiscoveredResourceCountsRequestTypeDef",
    "GetDiscoveredResourceCountsResponseResponseTypeDef",
    "GetOrganizationConfigRuleDetailedStatusRequestTypeDef",
    "GetOrganizationConfigRuleDetailedStatusResponseResponseTypeDef",
    "GetOrganizationConformancePackDetailedStatusRequestTypeDef",
    "GetOrganizationConformancePackDetailedStatusResponseResponseTypeDef",
    "GetResourceConfigHistoryRequestTypeDef",
    "GetResourceConfigHistoryResponseResponseTypeDef",
    "GetStoredQueryRequestTypeDef",
    "GetStoredQueryResponseResponseTypeDef",
    "GroupedResourceCountTypeDef",
    "ListAggregateDiscoveredResourcesRequestTypeDef",
    "ListAggregateDiscoveredResourcesResponseResponseTypeDef",
    "ListDiscoveredResourcesRequestTypeDef",
    "ListDiscoveredResourcesResponseResponseTypeDef",
    "ListStoredQueriesRequestTypeDef",
    "ListStoredQueriesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "MemberAccountStatusTypeDef",
    "OrganizationAggregationSourceTypeDef",
    "OrganizationConfigRuleStatusTypeDef",
    "OrganizationConfigRuleTypeDef",
    "OrganizationConformancePackDetailedStatusTypeDef",
    "OrganizationConformancePackStatusTypeDef",
    "OrganizationConformancePackTypeDef",
    "OrganizationCustomRuleMetadataTypeDef",
    "OrganizationManagedRuleMetadataTypeDef",
    "OrganizationResourceDetailedStatusFiltersTypeDef",
    "PaginatorConfigTypeDef",
    "PendingAggregationRequestTypeDef",
    "PutAggregationAuthorizationRequestTypeDef",
    "PutAggregationAuthorizationResponseResponseTypeDef",
    "PutConfigRuleRequestTypeDef",
    "PutConfigurationAggregatorRequestTypeDef",
    "PutConfigurationAggregatorResponseResponseTypeDef",
    "PutConfigurationRecorderRequestTypeDef",
    "PutConformancePackRequestTypeDef",
    "PutConformancePackResponseResponseTypeDef",
    "PutDeliveryChannelRequestTypeDef",
    "PutEvaluationsRequestTypeDef",
    "PutEvaluationsResponseResponseTypeDef",
    "PutExternalEvaluationRequestTypeDef",
    "PutOrganizationConfigRuleRequestTypeDef",
    "PutOrganizationConfigRuleResponseResponseTypeDef",
    "PutOrganizationConformancePackRequestTypeDef",
    "PutOrganizationConformancePackResponseResponseTypeDef",
    "PutRemediationConfigurationsRequestTypeDef",
    "PutRemediationConfigurationsResponseResponseTypeDef",
    "PutRemediationExceptionsRequestTypeDef",
    "PutRemediationExceptionsResponseResponseTypeDef",
    "PutResourceConfigRequestTypeDef",
    "PutRetentionConfigurationRequestTypeDef",
    "PutRetentionConfigurationResponseResponseTypeDef",
    "PutStoredQueryRequestTypeDef",
    "PutStoredQueryResponseResponseTypeDef",
    "QueryInfoTypeDef",
    "RecordingGroupTypeDef",
    "RelationshipTypeDef",
    "RemediationConfigurationTypeDef",
    "RemediationExceptionResourceKeyTypeDef",
    "RemediationExceptionTypeDef",
    "RemediationExecutionStatusTypeDef",
    "RemediationExecutionStepTypeDef",
    "RemediationParameterValueTypeDef",
    "ResourceCountFiltersTypeDef",
    "ResourceCountTypeDef",
    "ResourceFiltersTypeDef",
    "ResourceIdentifierTypeDef",
    "ResourceKeyTypeDef",
    "ResourceValueTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionConfigurationTypeDef",
    "ScopeTypeDef",
    "SelectAggregateResourceConfigRequestTypeDef",
    "SelectAggregateResourceConfigResponseResponseTypeDef",
    "SelectResourceConfigRequestTypeDef",
    "SelectResourceConfigResponseResponseTypeDef",
    "SourceDetailTypeDef",
    "SourceTypeDef",
    "SsmControlsTypeDef",
    "StartConfigRulesEvaluationRequestTypeDef",
    "StartConfigurationRecorderRequestTypeDef",
    "StartRemediationExecutionRequestTypeDef",
    "StartRemediationExecutionResponseResponseTypeDef",
    "StaticValueTypeDef",
    "StatusDetailFiltersTypeDef",
    "StopConfigurationRecorderRequestTypeDef",
    "StoredQueryMetadataTypeDef",
    "StoredQueryTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
)

_RequiredAccountAggregationSourceTypeDef = TypedDict(
    "_RequiredAccountAggregationSourceTypeDef",
    {
        "AccountIds": List[str],
    },
)
_OptionalAccountAggregationSourceTypeDef = TypedDict(
    "_OptionalAccountAggregationSourceTypeDef",
    {
        "AllAwsRegions": bool,
        "AwsRegions": List[str],
    },
    total=False,
)


class AccountAggregationSourceTypeDef(
    _RequiredAccountAggregationSourceTypeDef, _OptionalAccountAggregationSourceTypeDef
):
    pass


AggregateComplianceByConfigRuleTypeDef = TypedDict(
    "AggregateComplianceByConfigRuleTypeDef",
    {
        "ConfigRuleName": str,
        "Compliance": "ComplianceTypeDef",
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

AggregateComplianceByConformancePackTypeDef = TypedDict(
    "AggregateComplianceByConformancePackTypeDef",
    {
        "ConformancePackName": str,
        "Compliance": "AggregateConformancePackComplianceTypeDef",
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

AggregateComplianceCountTypeDef = TypedDict(
    "AggregateComplianceCountTypeDef",
    {
        "GroupName": str,
        "ComplianceSummary": "ComplianceSummaryTypeDef",
    },
    total=False,
)

AggregateConformancePackComplianceCountTypeDef = TypedDict(
    "AggregateConformancePackComplianceCountTypeDef",
    {
        "CompliantConformancePackCount": int,
        "NonCompliantConformancePackCount": int,
    },
    total=False,
)

AggregateConformancePackComplianceFiltersTypeDef = TypedDict(
    "AggregateConformancePackComplianceFiltersTypeDef",
    {
        "ConformancePackName": str,
        "ComplianceType": ConformancePackComplianceTypeType,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

AggregateConformancePackComplianceSummaryFiltersTypeDef = TypedDict(
    "AggregateConformancePackComplianceSummaryFiltersTypeDef",
    {
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

AggregateConformancePackComplianceSummaryTypeDef = TypedDict(
    "AggregateConformancePackComplianceSummaryTypeDef",
    {
        "ComplianceSummary": "AggregateConformancePackComplianceCountTypeDef",
        "GroupName": str,
    },
    total=False,
)

AggregateConformancePackComplianceTypeDef = TypedDict(
    "AggregateConformancePackComplianceTypeDef",
    {
        "ComplianceType": ConformancePackComplianceTypeType,
        "CompliantRuleCount": int,
        "NonCompliantRuleCount": int,
        "TotalRuleCount": int,
    },
    total=False,
)

AggregateEvaluationResultTypeDef = TypedDict(
    "AggregateEvaluationResultTypeDef",
    {
        "EvaluationResultIdentifier": "EvaluationResultIdentifierTypeDef",
        "ComplianceType": ComplianceTypeType,
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

_RequiredAggregateResourceIdentifierTypeDef = TypedDict(
    "_RequiredAggregateResourceIdentifierTypeDef",
    {
        "SourceAccountId": str,
        "SourceRegion": str,
        "ResourceId": str,
        "ResourceType": ResourceTypeType,
    },
)
_OptionalAggregateResourceIdentifierTypeDef = TypedDict(
    "_OptionalAggregateResourceIdentifierTypeDef",
    {
        "ResourceName": str,
    },
    total=False,
)


class AggregateResourceIdentifierTypeDef(
    _RequiredAggregateResourceIdentifierTypeDef, _OptionalAggregateResourceIdentifierTypeDef
):
    pass


AggregatedSourceStatusTypeDef = TypedDict(
    "AggregatedSourceStatusTypeDef",
    {
        "SourceId": str,
        "SourceType": AggregatedSourceTypeType,
        "AwsRegion": str,
        "LastUpdateStatus": AggregatedSourceStatusTypeType,
        "LastUpdateTime": datetime,
        "LastErrorCode": str,
        "LastErrorMessage": str,
    },
    total=False,
)

AggregationAuthorizationTypeDef = TypedDict(
    "AggregationAuthorizationTypeDef",
    {
        "AggregationAuthorizationArn": str,
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
        "CreationTime": datetime,
    },
    total=False,
)

BaseConfigurationItemTypeDef = TypedDict(
    "BaseConfigurationItemTypeDef",
    {
        "version": str,
        "accountId": str,
        "configurationItemCaptureTime": datetime,
        "configurationItemStatus": ConfigurationItemStatusType,
        "configurationStateId": str,
        "arn": str,
        "resourceType": ResourceTypeType,
        "resourceId": str,
        "resourceName": str,
        "awsRegion": str,
        "availabilityZone": str,
        "resourceCreationTime": datetime,
        "configuration": str,
        "supplementaryConfiguration": Dict[str, str],
    },
    total=False,
)

BatchGetAggregateResourceConfigRequestTypeDef = TypedDict(
    "BatchGetAggregateResourceConfigRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ResourceIdentifiers": List["AggregateResourceIdentifierTypeDef"],
    },
)

BatchGetAggregateResourceConfigResponseResponseTypeDef = TypedDict(
    "BatchGetAggregateResourceConfigResponseResponseTypeDef",
    {
        "BaseConfigurationItems": List["BaseConfigurationItemTypeDef"],
        "UnprocessedResourceIdentifiers": List["AggregateResourceIdentifierTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetResourceConfigRequestTypeDef = TypedDict(
    "BatchGetResourceConfigRequestTypeDef",
    {
        "resourceKeys": List["ResourceKeyTypeDef"],
    },
)

BatchGetResourceConfigResponseResponseTypeDef = TypedDict(
    "BatchGetResourceConfigResponseResponseTypeDef",
    {
        "baseConfigurationItems": List["BaseConfigurationItemTypeDef"],
        "unprocessedResourceKeys": List["ResourceKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ComplianceByConfigRuleTypeDef = TypedDict(
    "ComplianceByConfigRuleTypeDef",
    {
        "ConfigRuleName": str,
        "Compliance": "ComplianceTypeDef",
    },
    total=False,
)

ComplianceByResourceTypeDef = TypedDict(
    "ComplianceByResourceTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
        "Compliance": "ComplianceTypeDef",
    },
    total=False,
)

ComplianceContributorCountTypeDef = TypedDict(
    "ComplianceContributorCountTypeDef",
    {
        "CappedCount": int,
        "CapExceeded": bool,
    },
    total=False,
)

ComplianceSummaryByResourceTypeTypeDef = TypedDict(
    "ComplianceSummaryByResourceTypeTypeDef",
    {
        "ResourceType": str,
        "ComplianceSummary": "ComplianceSummaryTypeDef",
    },
    total=False,
)

ComplianceSummaryTypeDef = TypedDict(
    "ComplianceSummaryTypeDef",
    {
        "CompliantResourceCount": "ComplianceContributorCountTypeDef",
        "NonCompliantResourceCount": "ComplianceContributorCountTypeDef",
        "ComplianceSummaryTimestamp": datetime,
    },
    total=False,
)

ComplianceTypeDef = TypedDict(
    "ComplianceTypeDef",
    {
        "ComplianceType": ComplianceTypeType,
        "ComplianceContributorCount": "ComplianceContributorCountTypeDef",
    },
    total=False,
)

ConfigExportDeliveryInfoTypeDef = TypedDict(
    "ConfigExportDeliveryInfoTypeDef",
    {
        "lastStatus": DeliveryStatusType,
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastAttemptTime": datetime,
        "lastSuccessfulTime": datetime,
        "nextDeliveryTime": datetime,
    },
    total=False,
)

ConfigRuleComplianceFiltersTypeDef = TypedDict(
    "ConfigRuleComplianceFiltersTypeDef",
    {
        "ConfigRuleName": str,
        "ComplianceType": ComplianceTypeType,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

ConfigRuleComplianceSummaryFiltersTypeDef = TypedDict(
    "ConfigRuleComplianceSummaryFiltersTypeDef",
    {
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

ConfigRuleEvaluationStatusTypeDef = TypedDict(
    "ConfigRuleEvaluationStatusTypeDef",
    {
        "ConfigRuleName": str,
        "ConfigRuleArn": str,
        "ConfigRuleId": str,
        "LastSuccessfulInvocationTime": datetime,
        "LastFailedInvocationTime": datetime,
        "LastSuccessfulEvaluationTime": datetime,
        "LastFailedEvaluationTime": datetime,
        "FirstActivatedTime": datetime,
        "LastDeactivatedTime": datetime,
        "LastErrorCode": str,
        "LastErrorMessage": str,
        "FirstEvaluationStarted": bool,
    },
    total=False,
)

_RequiredConfigRuleTypeDef = TypedDict(
    "_RequiredConfigRuleTypeDef",
    {
        "Source": "SourceTypeDef",
    },
)
_OptionalConfigRuleTypeDef = TypedDict(
    "_OptionalConfigRuleTypeDef",
    {
        "ConfigRuleName": str,
        "ConfigRuleArn": str,
        "ConfigRuleId": str,
        "Description": str,
        "Scope": "ScopeTypeDef",
        "InputParameters": str,
        "MaximumExecutionFrequency": MaximumExecutionFrequencyType,
        "ConfigRuleState": ConfigRuleStateType,
        "CreatedBy": str,
    },
    total=False,
)


class ConfigRuleTypeDef(_RequiredConfigRuleTypeDef, _OptionalConfigRuleTypeDef):
    pass


ConfigSnapshotDeliveryPropertiesTypeDef = TypedDict(
    "ConfigSnapshotDeliveryPropertiesTypeDef",
    {
        "deliveryFrequency": MaximumExecutionFrequencyType,
    },
    total=False,
)

ConfigStreamDeliveryInfoTypeDef = TypedDict(
    "ConfigStreamDeliveryInfoTypeDef",
    {
        "lastStatus": DeliveryStatusType,
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastStatusChangeTime": datetime,
    },
    total=False,
)

ConfigurationAggregatorTypeDef = TypedDict(
    "ConfigurationAggregatorTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ConfigurationAggregatorArn": str,
        "AccountAggregationSources": List["AccountAggregationSourceTypeDef"],
        "OrganizationAggregationSource": "OrganizationAggregationSourceTypeDef",
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "CreatedBy": str,
    },
    total=False,
)

ConfigurationItemTypeDef = TypedDict(
    "ConfigurationItemTypeDef",
    {
        "version": str,
        "accountId": str,
        "configurationItemCaptureTime": datetime,
        "configurationItemStatus": ConfigurationItemStatusType,
        "configurationStateId": str,
        "configurationItemMD5Hash": str,
        "arn": str,
        "resourceType": ResourceTypeType,
        "resourceId": str,
        "resourceName": str,
        "awsRegion": str,
        "availabilityZone": str,
        "resourceCreationTime": datetime,
        "tags": Dict[str, str],
        "relatedEvents": List[str],
        "relationships": List["RelationshipTypeDef"],
        "configuration": str,
        "supplementaryConfiguration": Dict[str, str],
    },
    total=False,
)

ConfigurationRecorderStatusTypeDef = TypedDict(
    "ConfigurationRecorderStatusTypeDef",
    {
        "name": str,
        "lastStartTime": datetime,
        "lastStopTime": datetime,
        "recording": bool,
        "lastStatus": RecorderStatusType,
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastStatusChangeTime": datetime,
    },
    total=False,
)

ConfigurationRecorderTypeDef = TypedDict(
    "ConfigurationRecorderTypeDef",
    {
        "name": str,
        "roleARN": str,
        "recordingGroup": "RecordingGroupTypeDef",
    },
    total=False,
)

ConformancePackComplianceFiltersTypeDef = TypedDict(
    "ConformancePackComplianceFiltersTypeDef",
    {
        "ConfigRuleNames": List[str],
        "ComplianceType": ConformancePackComplianceTypeType,
    },
    total=False,
)

ConformancePackComplianceSummaryTypeDef = TypedDict(
    "ConformancePackComplianceSummaryTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackComplianceStatus": ConformancePackComplianceTypeType,
    },
)

_RequiredConformancePackDetailTypeDef = TypedDict(
    "_RequiredConformancePackDetailTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackArn": str,
        "ConformancePackId": str,
    },
)
_OptionalConformancePackDetailTypeDef = TypedDict(
    "_OptionalConformancePackDetailTypeDef",
    {
        "DeliveryS3Bucket": str,
        "DeliveryS3KeyPrefix": str,
        "ConformancePackInputParameters": List["ConformancePackInputParameterTypeDef"],
        "LastUpdateRequestedTime": datetime,
        "CreatedBy": str,
    },
    total=False,
)


class ConformancePackDetailTypeDef(
    _RequiredConformancePackDetailTypeDef, _OptionalConformancePackDetailTypeDef
):
    pass


ConformancePackEvaluationFiltersTypeDef = TypedDict(
    "ConformancePackEvaluationFiltersTypeDef",
    {
        "ConfigRuleNames": List[str],
        "ComplianceType": ConformancePackComplianceTypeType,
        "ResourceType": str,
        "ResourceIds": List[str],
    },
    total=False,
)

_RequiredConformancePackEvaluationResultTypeDef = TypedDict(
    "_RequiredConformancePackEvaluationResultTypeDef",
    {
        "ComplianceType": ConformancePackComplianceTypeType,
        "EvaluationResultIdentifier": "EvaluationResultIdentifierTypeDef",
        "ConfigRuleInvokedTime": datetime,
        "ResultRecordedTime": datetime,
    },
)
_OptionalConformancePackEvaluationResultTypeDef = TypedDict(
    "_OptionalConformancePackEvaluationResultTypeDef",
    {
        "Annotation": str,
    },
    total=False,
)


class ConformancePackEvaluationResultTypeDef(
    _RequiredConformancePackEvaluationResultTypeDef, _OptionalConformancePackEvaluationResultTypeDef
):
    pass


ConformancePackInputParameterTypeDef = TypedDict(
    "ConformancePackInputParameterTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
    },
)

ConformancePackRuleComplianceTypeDef = TypedDict(
    "ConformancePackRuleComplianceTypeDef",
    {
        "ConfigRuleName": str,
        "ComplianceType": ConformancePackComplianceTypeType,
        "Controls": List[str],
    },
    total=False,
)

_RequiredConformancePackStatusDetailTypeDef = TypedDict(
    "_RequiredConformancePackStatusDetailTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackId": str,
        "ConformancePackArn": str,
        "ConformancePackState": ConformancePackStateType,
        "StackArn": str,
        "LastUpdateRequestedTime": datetime,
    },
)
_OptionalConformancePackStatusDetailTypeDef = TypedDict(
    "_OptionalConformancePackStatusDetailTypeDef",
    {
        "ConformancePackStatusReason": str,
        "LastUpdateCompletedTime": datetime,
    },
    total=False,
)


class ConformancePackStatusDetailTypeDef(
    _RequiredConformancePackStatusDetailTypeDef, _OptionalConformancePackStatusDetailTypeDef
):
    pass


DeleteAggregationAuthorizationRequestTypeDef = TypedDict(
    "DeleteAggregationAuthorizationRequestTypeDef",
    {
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
    },
)

DeleteConfigRuleRequestTypeDef = TypedDict(
    "DeleteConfigRuleRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)

DeleteConfigurationAggregatorRequestTypeDef = TypedDict(
    "DeleteConfigurationAggregatorRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)

DeleteConfigurationRecorderRequestTypeDef = TypedDict(
    "DeleteConfigurationRecorderRequestTypeDef",
    {
        "ConfigurationRecorderName": str,
    },
)

DeleteConformancePackRequestTypeDef = TypedDict(
    "DeleteConformancePackRequestTypeDef",
    {
        "ConformancePackName": str,
    },
)

DeleteDeliveryChannelRequestTypeDef = TypedDict(
    "DeleteDeliveryChannelRequestTypeDef",
    {
        "DeliveryChannelName": str,
    },
)

DeleteEvaluationResultsRequestTypeDef = TypedDict(
    "DeleteEvaluationResultsRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)

DeleteOrganizationConfigRuleRequestTypeDef = TypedDict(
    "DeleteOrganizationConfigRuleRequestTypeDef",
    {
        "OrganizationConfigRuleName": str,
    },
)

DeleteOrganizationConformancePackRequestTypeDef = TypedDict(
    "DeleteOrganizationConformancePackRequestTypeDef",
    {
        "OrganizationConformancePackName": str,
    },
)

DeletePendingAggregationRequestRequestTypeDef = TypedDict(
    "DeletePendingAggregationRequestRequestTypeDef",
    {
        "RequesterAccountId": str,
        "RequesterAwsRegion": str,
    },
)

_RequiredDeleteRemediationConfigurationRequestTypeDef = TypedDict(
    "_RequiredDeleteRemediationConfigurationRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)
_OptionalDeleteRemediationConfigurationRequestTypeDef = TypedDict(
    "_OptionalDeleteRemediationConfigurationRequestTypeDef",
    {
        "ResourceType": str,
    },
    total=False,
)


class DeleteRemediationConfigurationRequestTypeDef(
    _RequiredDeleteRemediationConfigurationRequestTypeDef,
    _OptionalDeleteRemediationConfigurationRequestTypeDef,
):
    pass


DeleteRemediationExceptionsRequestTypeDef = TypedDict(
    "DeleteRemediationExceptionsRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": List["RemediationExceptionResourceKeyTypeDef"],
    },
)

DeleteRemediationExceptionsResponseResponseTypeDef = TypedDict(
    "DeleteRemediationExceptionsResponseResponseTypeDef",
    {
        "FailedBatches": List["FailedDeleteRemediationExceptionsBatchTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourceConfigRequestTypeDef = TypedDict(
    "DeleteResourceConfigRequestTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
    },
)

DeleteRetentionConfigurationRequestTypeDef = TypedDict(
    "DeleteRetentionConfigurationRequestTypeDef",
    {
        "RetentionConfigurationName": str,
    },
)

DeleteStoredQueryRequestTypeDef = TypedDict(
    "DeleteStoredQueryRequestTypeDef",
    {
        "QueryName": str,
    },
)

DeliverConfigSnapshotRequestTypeDef = TypedDict(
    "DeliverConfigSnapshotRequestTypeDef",
    {
        "deliveryChannelName": str,
    },
)

DeliverConfigSnapshotResponseResponseTypeDef = TypedDict(
    "DeliverConfigSnapshotResponseResponseTypeDef",
    {
        "configSnapshotId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeliveryChannelStatusTypeDef = TypedDict(
    "DeliveryChannelStatusTypeDef",
    {
        "name": str,
        "configSnapshotDeliveryInfo": "ConfigExportDeliveryInfoTypeDef",
        "configHistoryDeliveryInfo": "ConfigExportDeliveryInfoTypeDef",
        "configStreamDeliveryInfo": "ConfigStreamDeliveryInfoTypeDef",
    },
    total=False,
)

DeliveryChannelTypeDef = TypedDict(
    "DeliveryChannelTypeDef",
    {
        "name": str,
        "s3BucketName": str,
        "s3KeyPrefix": str,
        "s3KmsKeyArn": str,
        "snsTopicARN": str,
        "configSnapshotDeliveryProperties": "ConfigSnapshotDeliveryPropertiesTypeDef",
    },
    total=False,
)

_RequiredDescribeAggregateComplianceByConfigRulesRequestTypeDef = TypedDict(
    "_RequiredDescribeAggregateComplianceByConfigRulesRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalDescribeAggregateComplianceByConfigRulesRequestTypeDef = TypedDict(
    "_OptionalDescribeAggregateComplianceByConfigRulesRequestTypeDef",
    {
        "Filters": "ConfigRuleComplianceFiltersTypeDef",
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeAggregateComplianceByConfigRulesRequestTypeDef(
    _RequiredDescribeAggregateComplianceByConfigRulesRequestTypeDef,
    _OptionalDescribeAggregateComplianceByConfigRulesRequestTypeDef,
):
    pass


DescribeAggregateComplianceByConfigRulesResponseResponseTypeDef = TypedDict(
    "DescribeAggregateComplianceByConfigRulesResponseResponseTypeDef",
    {
        "AggregateComplianceByConfigRules": List["AggregateComplianceByConfigRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAggregateComplianceByConformancePacksRequestTypeDef = TypedDict(
    "_RequiredDescribeAggregateComplianceByConformancePacksRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalDescribeAggregateComplianceByConformancePacksRequestTypeDef = TypedDict(
    "_OptionalDescribeAggregateComplianceByConformancePacksRequestTypeDef",
    {
        "Filters": "AggregateConformancePackComplianceFiltersTypeDef",
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeAggregateComplianceByConformancePacksRequestTypeDef(
    _RequiredDescribeAggregateComplianceByConformancePacksRequestTypeDef,
    _OptionalDescribeAggregateComplianceByConformancePacksRequestTypeDef,
):
    pass


DescribeAggregateComplianceByConformancePacksResponseResponseTypeDef = TypedDict(
    "DescribeAggregateComplianceByConformancePacksResponseResponseTypeDef",
    {
        "AggregateComplianceByConformancePacks": List[
            "AggregateComplianceByConformancePackTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAggregationAuthorizationsRequestTypeDef = TypedDict(
    "DescribeAggregationAuthorizationsRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeAggregationAuthorizationsResponseResponseTypeDef = TypedDict(
    "DescribeAggregationAuthorizationsResponseResponseTypeDef",
    {
        "AggregationAuthorizations": List["AggregationAuthorizationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeComplianceByConfigRuleRequestTypeDef = TypedDict(
    "DescribeComplianceByConfigRuleRequestTypeDef",
    {
        "ConfigRuleNames": List[str],
        "ComplianceTypes": List[ComplianceTypeType],
        "NextToken": str,
    },
    total=False,
)

DescribeComplianceByConfigRuleResponseResponseTypeDef = TypedDict(
    "DescribeComplianceByConfigRuleResponseResponseTypeDef",
    {
        "ComplianceByConfigRules": List["ComplianceByConfigRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeComplianceByResourceRequestTypeDef = TypedDict(
    "DescribeComplianceByResourceRequestTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
        "ComplianceTypes": List[ComplianceTypeType],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeComplianceByResourceResponseResponseTypeDef = TypedDict(
    "DescribeComplianceByResourceResponseResponseTypeDef",
    {
        "ComplianceByResources": List["ComplianceByResourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigRuleEvaluationStatusRequestTypeDef = TypedDict(
    "DescribeConfigRuleEvaluationStatusRequestTypeDef",
    {
        "ConfigRuleNames": List[str],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeConfigRuleEvaluationStatusResponseResponseTypeDef = TypedDict(
    "DescribeConfigRuleEvaluationStatusResponseResponseTypeDef",
    {
        "ConfigRulesEvaluationStatus": List["ConfigRuleEvaluationStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigRulesRequestTypeDef = TypedDict(
    "DescribeConfigRulesRequestTypeDef",
    {
        "ConfigRuleNames": List[str],
        "NextToken": str,
    },
    total=False,
)

DescribeConfigRulesResponseResponseTypeDef = TypedDict(
    "DescribeConfigRulesResponseResponseTypeDef",
    {
        "ConfigRules": List["ConfigRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeConfigurationAggregatorSourcesStatusRequestTypeDef = TypedDict(
    "_RequiredDescribeConfigurationAggregatorSourcesStatusRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalDescribeConfigurationAggregatorSourcesStatusRequestTypeDef = TypedDict(
    "_OptionalDescribeConfigurationAggregatorSourcesStatusRequestTypeDef",
    {
        "UpdateStatus": List[AggregatedSourceStatusTypeType],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)


class DescribeConfigurationAggregatorSourcesStatusRequestTypeDef(
    _RequiredDescribeConfigurationAggregatorSourcesStatusRequestTypeDef,
    _OptionalDescribeConfigurationAggregatorSourcesStatusRequestTypeDef,
):
    pass


DescribeConfigurationAggregatorSourcesStatusResponseResponseTypeDef = TypedDict(
    "DescribeConfigurationAggregatorSourcesStatusResponseResponseTypeDef",
    {
        "AggregatedSourceStatusList": List["AggregatedSourceStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationAggregatorsRequestTypeDef = TypedDict(
    "DescribeConfigurationAggregatorsRequestTypeDef",
    {
        "ConfigurationAggregatorNames": List[str],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeConfigurationAggregatorsResponseResponseTypeDef = TypedDict(
    "DescribeConfigurationAggregatorsResponseResponseTypeDef",
    {
        "ConfigurationAggregators": List["ConfigurationAggregatorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationRecorderStatusRequestTypeDef = TypedDict(
    "DescribeConfigurationRecorderStatusRequestTypeDef",
    {
        "ConfigurationRecorderNames": List[str],
    },
    total=False,
)

DescribeConfigurationRecorderStatusResponseResponseTypeDef = TypedDict(
    "DescribeConfigurationRecorderStatusResponseResponseTypeDef",
    {
        "ConfigurationRecordersStatus": List["ConfigurationRecorderStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationRecordersRequestTypeDef = TypedDict(
    "DescribeConfigurationRecordersRequestTypeDef",
    {
        "ConfigurationRecorderNames": List[str],
    },
    total=False,
)

DescribeConfigurationRecordersResponseResponseTypeDef = TypedDict(
    "DescribeConfigurationRecordersResponseResponseTypeDef",
    {
        "ConfigurationRecorders": List["ConfigurationRecorderTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeConformancePackComplianceRequestTypeDef = TypedDict(
    "_RequiredDescribeConformancePackComplianceRequestTypeDef",
    {
        "ConformancePackName": str,
    },
)
_OptionalDescribeConformancePackComplianceRequestTypeDef = TypedDict(
    "_OptionalDescribeConformancePackComplianceRequestTypeDef",
    {
        "Filters": "ConformancePackComplianceFiltersTypeDef",
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeConformancePackComplianceRequestTypeDef(
    _RequiredDescribeConformancePackComplianceRequestTypeDef,
    _OptionalDescribeConformancePackComplianceRequestTypeDef,
):
    pass


DescribeConformancePackComplianceResponseResponseTypeDef = TypedDict(
    "DescribeConformancePackComplianceResponseResponseTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackRuleComplianceList": List["ConformancePackRuleComplianceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConformancePackStatusRequestTypeDef = TypedDict(
    "DescribeConformancePackStatusRequestTypeDef",
    {
        "ConformancePackNames": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeConformancePackStatusResponseResponseTypeDef = TypedDict(
    "DescribeConformancePackStatusResponseResponseTypeDef",
    {
        "ConformancePackStatusDetails": List["ConformancePackStatusDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConformancePacksRequestTypeDef = TypedDict(
    "DescribeConformancePacksRequestTypeDef",
    {
        "ConformancePackNames": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeConformancePacksResponseResponseTypeDef = TypedDict(
    "DescribeConformancePacksResponseResponseTypeDef",
    {
        "ConformancePackDetails": List["ConformancePackDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeliveryChannelStatusRequestTypeDef = TypedDict(
    "DescribeDeliveryChannelStatusRequestTypeDef",
    {
        "DeliveryChannelNames": List[str],
    },
    total=False,
)

DescribeDeliveryChannelStatusResponseResponseTypeDef = TypedDict(
    "DescribeDeliveryChannelStatusResponseResponseTypeDef",
    {
        "DeliveryChannelsStatus": List["DeliveryChannelStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeliveryChannelsRequestTypeDef = TypedDict(
    "DescribeDeliveryChannelsRequestTypeDef",
    {
        "DeliveryChannelNames": List[str],
    },
    total=False,
)

DescribeDeliveryChannelsResponseResponseTypeDef = TypedDict(
    "DescribeDeliveryChannelsResponseResponseTypeDef",
    {
        "DeliveryChannels": List["DeliveryChannelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConfigRuleStatusesRequestTypeDef = TypedDict(
    "DescribeOrganizationConfigRuleStatusesRequestTypeDef",
    {
        "OrganizationConfigRuleNames": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeOrganizationConfigRuleStatusesResponseResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigRuleStatusesResponseResponseTypeDef",
    {
        "OrganizationConfigRuleStatuses": List["OrganizationConfigRuleStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConfigRulesRequestTypeDef = TypedDict(
    "DescribeOrganizationConfigRulesRequestTypeDef",
    {
        "OrganizationConfigRuleNames": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeOrganizationConfigRulesResponseResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigRulesResponseResponseTypeDef",
    {
        "OrganizationConfigRules": List["OrganizationConfigRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConformancePackStatusesRequestTypeDef = TypedDict(
    "DescribeOrganizationConformancePackStatusesRequestTypeDef",
    {
        "OrganizationConformancePackNames": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeOrganizationConformancePackStatusesResponseResponseTypeDef = TypedDict(
    "DescribeOrganizationConformancePackStatusesResponseResponseTypeDef",
    {
        "OrganizationConformancePackStatuses": List["OrganizationConformancePackStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConformancePacksRequestTypeDef = TypedDict(
    "DescribeOrganizationConformancePacksRequestTypeDef",
    {
        "OrganizationConformancePackNames": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeOrganizationConformancePacksResponseResponseTypeDef = TypedDict(
    "DescribeOrganizationConformancePacksResponseResponseTypeDef",
    {
        "OrganizationConformancePacks": List["OrganizationConformancePackTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePendingAggregationRequestsRequestTypeDef = TypedDict(
    "DescribePendingAggregationRequestsRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribePendingAggregationRequestsResponseResponseTypeDef = TypedDict(
    "DescribePendingAggregationRequestsResponseResponseTypeDef",
    {
        "PendingAggregationRequests": List["PendingAggregationRequestTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRemediationConfigurationsRequestTypeDef = TypedDict(
    "DescribeRemediationConfigurationsRequestTypeDef",
    {
        "ConfigRuleNames": List[str],
    },
)

DescribeRemediationConfigurationsResponseResponseTypeDef = TypedDict(
    "DescribeRemediationConfigurationsResponseResponseTypeDef",
    {
        "RemediationConfigurations": List["RemediationConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRemediationExceptionsRequestTypeDef = TypedDict(
    "_RequiredDescribeRemediationExceptionsRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)
_OptionalDescribeRemediationExceptionsRequestTypeDef = TypedDict(
    "_OptionalDescribeRemediationExceptionsRequestTypeDef",
    {
        "ResourceKeys": List["RemediationExceptionResourceKeyTypeDef"],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeRemediationExceptionsRequestTypeDef(
    _RequiredDescribeRemediationExceptionsRequestTypeDef,
    _OptionalDescribeRemediationExceptionsRequestTypeDef,
):
    pass


DescribeRemediationExceptionsResponseResponseTypeDef = TypedDict(
    "DescribeRemediationExceptionsResponseResponseTypeDef",
    {
        "RemediationExceptions": List["RemediationExceptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRemediationExecutionStatusRequestTypeDef = TypedDict(
    "_RequiredDescribeRemediationExecutionStatusRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)
_OptionalDescribeRemediationExecutionStatusRequestTypeDef = TypedDict(
    "_OptionalDescribeRemediationExecutionStatusRequestTypeDef",
    {
        "ResourceKeys": List["ResourceKeyTypeDef"],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeRemediationExecutionStatusRequestTypeDef(
    _RequiredDescribeRemediationExecutionStatusRequestTypeDef,
    _OptionalDescribeRemediationExecutionStatusRequestTypeDef,
):
    pass


DescribeRemediationExecutionStatusResponseResponseTypeDef = TypedDict(
    "DescribeRemediationExecutionStatusResponseResponseTypeDef",
    {
        "RemediationExecutionStatuses": List["RemediationExecutionStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRetentionConfigurationsRequestTypeDef = TypedDict(
    "DescribeRetentionConfigurationsRequestTypeDef",
    {
        "RetentionConfigurationNames": List[str],
        "NextToken": str,
    },
    total=False,
)

DescribeRetentionConfigurationsResponseResponseTypeDef = TypedDict(
    "DescribeRetentionConfigurationsResponseResponseTypeDef",
    {
        "RetentionConfigurations": List["RetentionConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EvaluationResultIdentifierTypeDef = TypedDict(
    "EvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": "EvaluationResultQualifierTypeDef",
        "OrderingTimestamp": datetime,
    },
    total=False,
)

EvaluationResultQualifierTypeDef = TypedDict(
    "EvaluationResultQualifierTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceType": str,
        "ResourceId": str,
    },
    total=False,
)

EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "EvaluationResultIdentifier": "EvaluationResultIdentifierTypeDef",
        "ComplianceType": ComplianceTypeType,
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "ResultToken": str,
    },
    total=False,
)

_RequiredEvaluationTypeDef = TypedDict(
    "_RequiredEvaluationTypeDef",
    {
        "ComplianceResourceType": str,
        "ComplianceResourceId": str,
        "ComplianceType": ComplianceTypeType,
        "OrderingTimestamp": Union[datetime, str],
    },
)
_OptionalEvaluationTypeDef = TypedDict(
    "_OptionalEvaluationTypeDef",
    {
        "Annotation": str,
    },
    total=False,
)


class EvaluationTypeDef(_RequiredEvaluationTypeDef, _OptionalEvaluationTypeDef):
    pass


ExecutionControlsTypeDef = TypedDict(
    "ExecutionControlsTypeDef",
    {
        "SsmControls": "SsmControlsTypeDef",
    },
    total=False,
)

_RequiredExternalEvaluationTypeDef = TypedDict(
    "_RequiredExternalEvaluationTypeDef",
    {
        "ComplianceResourceType": str,
        "ComplianceResourceId": str,
        "ComplianceType": ComplianceTypeType,
        "OrderingTimestamp": Union[datetime, str],
    },
)
_OptionalExternalEvaluationTypeDef = TypedDict(
    "_OptionalExternalEvaluationTypeDef",
    {
        "Annotation": str,
    },
    total=False,
)


class ExternalEvaluationTypeDef(
    _RequiredExternalEvaluationTypeDef, _OptionalExternalEvaluationTypeDef
):
    pass


FailedDeleteRemediationExceptionsBatchTypeDef = TypedDict(
    "FailedDeleteRemediationExceptionsBatchTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List["RemediationExceptionResourceKeyTypeDef"],
    },
    total=False,
)

FailedRemediationBatchTypeDef = TypedDict(
    "FailedRemediationBatchTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List["RemediationConfigurationTypeDef"],
    },
    total=False,
)

FailedRemediationExceptionBatchTypeDef = TypedDict(
    "FailedRemediationExceptionBatchTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List["RemediationExceptionTypeDef"],
    },
    total=False,
)

FieldInfoTypeDef = TypedDict(
    "FieldInfoTypeDef",
    {
        "Name": str,
    },
    total=False,
)

_RequiredGetAggregateComplianceDetailsByConfigRuleRequestTypeDef = TypedDict(
    "_RequiredGetAggregateComplianceDetailsByConfigRuleRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ConfigRuleName": str,
        "AccountId": str,
        "AwsRegion": str,
    },
)
_OptionalGetAggregateComplianceDetailsByConfigRuleRequestTypeDef = TypedDict(
    "_OptionalGetAggregateComplianceDetailsByConfigRuleRequestTypeDef",
    {
        "ComplianceType": ComplianceTypeType,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class GetAggregateComplianceDetailsByConfigRuleRequestTypeDef(
    _RequiredGetAggregateComplianceDetailsByConfigRuleRequestTypeDef,
    _OptionalGetAggregateComplianceDetailsByConfigRuleRequestTypeDef,
):
    pass


GetAggregateComplianceDetailsByConfigRuleResponseResponseTypeDef = TypedDict(
    "GetAggregateComplianceDetailsByConfigRuleResponseResponseTypeDef",
    {
        "AggregateEvaluationResults": List["AggregateEvaluationResultTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetAggregateConfigRuleComplianceSummaryRequestTypeDef = TypedDict(
    "_RequiredGetAggregateConfigRuleComplianceSummaryRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalGetAggregateConfigRuleComplianceSummaryRequestTypeDef = TypedDict(
    "_OptionalGetAggregateConfigRuleComplianceSummaryRequestTypeDef",
    {
        "Filters": "ConfigRuleComplianceSummaryFiltersTypeDef",
        "GroupByKey": ConfigRuleComplianceSummaryGroupKeyType,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class GetAggregateConfigRuleComplianceSummaryRequestTypeDef(
    _RequiredGetAggregateConfigRuleComplianceSummaryRequestTypeDef,
    _OptionalGetAggregateConfigRuleComplianceSummaryRequestTypeDef,
):
    pass


GetAggregateConfigRuleComplianceSummaryResponseResponseTypeDef = TypedDict(
    "GetAggregateConfigRuleComplianceSummaryResponseResponseTypeDef",
    {
        "GroupByKey": str,
        "AggregateComplianceCounts": List["AggregateComplianceCountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetAggregateConformancePackComplianceSummaryRequestTypeDef = TypedDict(
    "_RequiredGetAggregateConformancePackComplianceSummaryRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalGetAggregateConformancePackComplianceSummaryRequestTypeDef = TypedDict(
    "_OptionalGetAggregateConformancePackComplianceSummaryRequestTypeDef",
    {
        "Filters": "AggregateConformancePackComplianceSummaryFiltersTypeDef",
        "GroupByKey": AggregateConformancePackComplianceSummaryGroupKeyType,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class GetAggregateConformancePackComplianceSummaryRequestTypeDef(
    _RequiredGetAggregateConformancePackComplianceSummaryRequestTypeDef,
    _OptionalGetAggregateConformancePackComplianceSummaryRequestTypeDef,
):
    pass


GetAggregateConformancePackComplianceSummaryResponseResponseTypeDef = TypedDict(
    "GetAggregateConformancePackComplianceSummaryResponseResponseTypeDef",
    {
        "AggregateConformancePackComplianceSummaries": List[
            "AggregateConformancePackComplianceSummaryTypeDef"
        ],
        "GroupByKey": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetAggregateDiscoveredResourceCountsRequestTypeDef = TypedDict(
    "_RequiredGetAggregateDiscoveredResourceCountsRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalGetAggregateDiscoveredResourceCountsRequestTypeDef = TypedDict(
    "_OptionalGetAggregateDiscoveredResourceCountsRequestTypeDef",
    {
        "Filters": "ResourceCountFiltersTypeDef",
        "GroupByKey": ResourceCountGroupKeyType,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class GetAggregateDiscoveredResourceCountsRequestTypeDef(
    _RequiredGetAggregateDiscoveredResourceCountsRequestTypeDef,
    _OptionalGetAggregateDiscoveredResourceCountsRequestTypeDef,
):
    pass


GetAggregateDiscoveredResourceCountsResponseResponseTypeDef = TypedDict(
    "GetAggregateDiscoveredResourceCountsResponseResponseTypeDef",
    {
        "TotalDiscoveredResources": int,
        "GroupByKey": str,
        "GroupedResourceCounts": List["GroupedResourceCountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAggregateResourceConfigRequestTypeDef = TypedDict(
    "GetAggregateResourceConfigRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ResourceIdentifier": "AggregateResourceIdentifierTypeDef",
    },
)

GetAggregateResourceConfigResponseResponseTypeDef = TypedDict(
    "GetAggregateResourceConfigResponseResponseTypeDef",
    {
        "ConfigurationItem": "ConfigurationItemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetComplianceDetailsByConfigRuleRequestTypeDef = TypedDict(
    "_RequiredGetComplianceDetailsByConfigRuleRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)
_OptionalGetComplianceDetailsByConfigRuleRequestTypeDef = TypedDict(
    "_OptionalGetComplianceDetailsByConfigRuleRequestTypeDef",
    {
        "ComplianceTypes": List[ComplianceTypeType],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class GetComplianceDetailsByConfigRuleRequestTypeDef(
    _RequiredGetComplianceDetailsByConfigRuleRequestTypeDef,
    _OptionalGetComplianceDetailsByConfigRuleRequestTypeDef,
):
    pass


GetComplianceDetailsByConfigRuleResponseResponseTypeDef = TypedDict(
    "GetComplianceDetailsByConfigRuleResponseResponseTypeDef",
    {
        "EvaluationResults": List["EvaluationResultTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetComplianceDetailsByResourceRequestTypeDef = TypedDict(
    "_RequiredGetComplianceDetailsByResourceRequestTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
    },
)
_OptionalGetComplianceDetailsByResourceRequestTypeDef = TypedDict(
    "_OptionalGetComplianceDetailsByResourceRequestTypeDef",
    {
        "ComplianceTypes": List[ComplianceTypeType],
        "NextToken": str,
    },
    total=False,
)


class GetComplianceDetailsByResourceRequestTypeDef(
    _RequiredGetComplianceDetailsByResourceRequestTypeDef,
    _OptionalGetComplianceDetailsByResourceRequestTypeDef,
):
    pass


GetComplianceDetailsByResourceResponseResponseTypeDef = TypedDict(
    "GetComplianceDetailsByResourceResponseResponseTypeDef",
    {
        "EvaluationResults": List["EvaluationResultTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComplianceSummaryByConfigRuleResponseResponseTypeDef = TypedDict(
    "GetComplianceSummaryByConfigRuleResponseResponseTypeDef",
    {
        "ComplianceSummary": "ComplianceSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComplianceSummaryByResourceTypeRequestTypeDef = TypedDict(
    "GetComplianceSummaryByResourceTypeRequestTypeDef",
    {
        "ResourceTypes": List[str],
    },
    total=False,
)

GetComplianceSummaryByResourceTypeResponseResponseTypeDef = TypedDict(
    "GetComplianceSummaryByResourceTypeResponseResponseTypeDef",
    {
        "ComplianceSummariesByResourceType": List["ComplianceSummaryByResourceTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetConformancePackComplianceDetailsRequestTypeDef = TypedDict(
    "_RequiredGetConformancePackComplianceDetailsRequestTypeDef",
    {
        "ConformancePackName": str,
    },
)
_OptionalGetConformancePackComplianceDetailsRequestTypeDef = TypedDict(
    "_OptionalGetConformancePackComplianceDetailsRequestTypeDef",
    {
        "Filters": "ConformancePackEvaluationFiltersTypeDef",
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class GetConformancePackComplianceDetailsRequestTypeDef(
    _RequiredGetConformancePackComplianceDetailsRequestTypeDef,
    _OptionalGetConformancePackComplianceDetailsRequestTypeDef,
):
    pass


GetConformancePackComplianceDetailsResponseResponseTypeDef = TypedDict(
    "GetConformancePackComplianceDetailsResponseResponseTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackRuleEvaluationResults": List["ConformancePackEvaluationResultTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetConformancePackComplianceSummaryRequestTypeDef = TypedDict(
    "_RequiredGetConformancePackComplianceSummaryRequestTypeDef",
    {
        "ConformancePackNames": List[str],
    },
)
_OptionalGetConformancePackComplianceSummaryRequestTypeDef = TypedDict(
    "_OptionalGetConformancePackComplianceSummaryRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class GetConformancePackComplianceSummaryRequestTypeDef(
    _RequiredGetConformancePackComplianceSummaryRequestTypeDef,
    _OptionalGetConformancePackComplianceSummaryRequestTypeDef,
):
    pass


GetConformancePackComplianceSummaryResponseResponseTypeDef = TypedDict(
    "GetConformancePackComplianceSummaryResponseResponseTypeDef",
    {
        "ConformancePackComplianceSummaryList": List["ConformancePackComplianceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDiscoveredResourceCountsRequestTypeDef = TypedDict(
    "GetDiscoveredResourceCountsRequestTypeDef",
    {
        "resourceTypes": List[str],
        "limit": int,
        "nextToken": str,
    },
    total=False,
)

GetDiscoveredResourceCountsResponseResponseTypeDef = TypedDict(
    "GetDiscoveredResourceCountsResponseResponseTypeDef",
    {
        "totalDiscoveredResources": int,
        "resourceCounts": List["ResourceCountTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetOrganizationConfigRuleDetailedStatusRequestTypeDef = TypedDict(
    "_RequiredGetOrganizationConfigRuleDetailedStatusRequestTypeDef",
    {
        "OrganizationConfigRuleName": str,
    },
)
_OptionalGetOrganizationConfigRuleDetailedStatusRequestTypeDef = TypedDict(
    "_OptionalGetOrganizationConfigRuleDetailedStatusRequestTypeDef",
    {
        "Filters": "StatusDetailFiltersTypeDef",
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class GetOrganizationConfigRuleDetailedStatusRequestTypeDef(
    _RequiredGetOrganizationConfigRuleDetailedStatusRequestTypeDef,
    _OptionalGetOrganizationConfigRuleDetailedStatusRequestTypeDef,
):
    pass


GetOrganizationConfigRuleDetailedStatusResponseResponseTypeDef = TypedDict(
    "GetOrganizationConfigRuleDetailedStatusResponseResponseTypeDef",
    {
        "OrganizationConfigRuleDetailedStatus": List["MemberAccountStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetOrganizationConformancePackDetailedStatusRequestTypeDef = TypedDict(
    "_RequiredGetOrganizationConformancePackDetailedStatusRequestTypeDef",
    {
        "OrganizationConformancePackName": str,
    },
)
_OptionalGetOrganizationConformancePackDetailedStatusRequestTypeDef = TypedDict(
    "_OptionalGetOrganizationConformancePackDetailedStatusRequestTypeDef",
    {
        "Filters": "OrganizationResourceDetailedStatusFiltersTypeDef",
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class GetOrganizationConformancePackDetailedStatusRequestTypeDef(
    _RequiredGetOrganizationConformancePackDetailedStatusRequestTypeDef,
    _OptionalGetOrganizationConformancePackDetailedStatusRequestTypeDef,
):
    pass


GetOrganizationConformancePackDetailedStatusResponseResponseTypeDef = TypedDict(
    "GetOrganizationConformancePackDetailedStatusResponseResponseTypeDef",
    {
        "OrganizationConformancePackDetailedStatuses": List[
            "OrganizationConformancePackDetailedStatusTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourceConfigHistoryRequestTypeDef = TypedDict(
    "_RequiredGetResourceConfigHistoryRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceId": str,
    },
)
_OptionalGetResourceConfigHistoryRequestTypeDef = TypedDict(
    "_OptionalGetResourceConfigHistoryRequestTypeDef",
    {
        "laterTime": Union[datetime, str],
        "earlierTime": Union[datetime, str],
        "chronologicalOrder": ChronologicalOrderType,
        "limit": int,
        "nextToken": str,
    },
    total=False,
)


class GetResourceConfigHistoryRequestTypeDef(
    _RequiredGetResourceConfigHistoryRequestTypeDef, _OptionalGetResourceConfigHistoryRequestTypeDef
):
    pass


GetResourceConfigHistoryResponseResponseTypeDef = TypedDict(
    "GetResourceConfigHistoryResponseResponseTypeDef",
    {
        "configurationItems": List["ConfigurationItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStoredQueryRequestTypeDef = TypedDict(
    "GetStoredQueryRequestTypeDef",
    {
        "QueryName": str,
    },
)

GetStoredQueryResponseResponseTypeDef = TypedDict(
    "GetStoredQueryResponseResponseTypeDef",
    {
        "StoredQuery": "StoredQueryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupedResourceCountTypeDef = TypedDict(
    "GroupedResourceCountTypeDef",
    {
        "GroupName": str,
        "ResourceCount": int,
    },
)

_RequiredListAggregateDiscoveredResourcesRequestTypeDef = TypedDict(
    "_RequiredListAggregateDiscoveredResourcesRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ResourceType": ResourceTypeType,
    },
)
_OptionalListAggregateDiscoveredResourcesRequestTypeDef = TypedDict(
    "_OptionalListAggregateDiscoveredResourcesRequestTypeDef",
    {
        "Filters": "ResourceFiltersTypeDef",
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class ListAggregateDiscoveredResourcesRequestTypeDef(
    _RequiredListAggregateDiscoveredResourcesRequestTypeDef,
    _OptionalListAggregateDiscoveredResourcesRequestTypeDef,
):
    pass


ListAggregateDiscoveredResourcesResponseResponseTypeDef = TypedDict(
    "ListAggregateDiscoveredResourcesResponseResponseTypeDef",
    {
        "ResourceIdentifiers": List["AggregateResourceIdentifierTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDiscoveredResourcesRequestTypeDef = TypedDict(
    "_RequiredListDiscoveredResourcesRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
    },
)
_OptionalListDiscoveredResourcesRequestTypeDef = TypedDict(
    "_OptionalListDiscoveredResourcesRequestTypeDef",
    {
        "resourceIds": List[str],
        "resourceName": str,
        "limit": int,
        "includeDeletedResources": bool,
        "nextToken": str,
    },
    total=False,
)


class ListDiscoveredResourcesRequestTypeDef(
    _RequiredListDiscoveredResourcesRequestTypeDef, _OptionalListDiscoveredResourcesRequestTypeDef
):
    pass


ListDiscoveredResourcesResponseResponseTypeDef = TypedDict(
    "ListDiscoveredResourcesResponseResponseTypeDef",
    {
        "resourceIdentifiers": List["ResourceIdentifierTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStoredQueriesRequestTypeDef = TypedDict(
    "ListStoredQueriesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListStoredQueriesResponseResponseTypeDef = TypedDict(
    "ListStoredQueriesResponseResponseTypeDef",
    {
        "StoredQueryMetadata": List["StoredQueryMetadataTypeDef"],
        "NextToken": str,
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
        "Limit": int,
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

_RequiredMemberAccountStatusTypeDef = TypedDict(
    "_RequiredMemberAccountStatusTypeDef",
    {
        "AccountId": str,
        "ConfigRuleName": str,
        "MemberAccountRuleStatus": MemberAccountRuleStatusType,
    },
)
_OptionalMemberAccountStatusTypeDef = TypedDict(
    "_OptionalMemberAccountStatusTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)


class MemberAccountStatusTypeDef(
    _RequiredMemberAccountStatusTypeDef, _OptionalMemberAccountStatusTypeDef
):
    pass


_RequiredOrganizationAggregationSourceTypeDef = TypedDict(
    "_RequiredOrganizationAggregationSourceTypeDef",
    {
        "RoleArn": str,
    },
)
_OptionalOrganizationAggregationSourceTypeDef = TypedDict(
    "_OptionalOrganizationAggregationSourceTypeDef",
    {
        "AwsRegions": List[str],
        "AllAwsRegions": bool,
    },
    total=False,
)


class OrganizationAggregationSourceTypeDef(
    _RequiredOrganizationAggregationSourceTypeDef, _OptionalOrganizationAggregationSourceTypeDef
):
    pass


_RequiredOrganizationConfigRuleStatusTypeDef = TypedDict(
    "_RequiredOrganizationConfigRuleStatusTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "OrganizationRuleStatus": OrganizationRuleStatusType,
    },
)
_OptionalOrganizationConfigRuleStatusTypeDef = TypedDict(
    "_OptionalOrganizationConfigRuleStatusTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)


class OrganizationConfigRuleStatusTypeDef(
    _RequiredOrganizationConfigRuleStatusTypeDef, _OptionalOrganizationConfigRuleStatusTypeDef
):
    pass


_RequiredOrganizationConfigRuleTypeDef = TypedDict(
    "_RequiredOrganizationConfigRuleTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "OrganizationConfigRuleArn": str,
    },
)
_OptionalOrganizationConfigRuleTypeDef = TypedDict(
    "_OptionalOrganizationConfigRuleTypeDef",
    {
        "OrganizationManagedRuleMetadata": "OrganizationManagedRuleMetadataTypeDef",
        "OrganizationCustomRuleMetadata": "OrganizationCustomRuleMetadataTypeDef",
        "ExcludedAccounts": List[str],
        "LastUpdateTime": datetime,
    },
    total=False,
)


class OrganizationConfigRuleTypeDef(
    _RequiredOrganizationConfigRuleTypeDef, _OptionalOrganizationConfigRuleTypeDef
):
    pass


_RequiredOrganizationConformancePackDetailedStatusTypeDef = TypedDict(
    "_RequiredOrganizationConformancePackDetailedStatusTypeDef",
    {
        "AccountId": str,
        "ConformancePackName": str,
        "Status": OrganizationResourceDetailedStatusType,
    },
)
_OptionalOrganizationConformancePackDetailedStatusTypeDef = TypedDict(
    "_OptionalOrganizationConformancePackDetailedStatusTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)


class OrganizationConformancePackDetailedStatusTypeDef(
    _RequiredOrganizationConformancePackDetailedStatusTypeDef,
    _OptionalOrganizationConformancePackDetailedStatusTypeDef,
):
    pass


_RequiredOrganizationConformancePackStatusTypeDef = TypedDict(
    "_RequiredOrganizationConformancePackStatusTypeDef",
    {
        "OrganizationConformancePackName": str,
        "Status": OrganizationResourceStatusType,
    },
)
_OptionalOrganizationConformancePackStatusTypeDef = TypedDict(
    "_OptionalOrganizationConformancePackStatusTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)


class OrganizationConformancePackStatusTypeDef(
    _RequiredOrganizationConformancePackStatusTypeDef,
    _OptionalOrganizationConformancePackStatusTypeDef,
):
    pass


_RequiredOrganizationConformancePackTypeDef = TypedDict(
    "_RequiredOrganizationConformancePackTypeDef",
    {
        "OrganizationConformancePackName": str,
        "OrganizationConformancePackArn": str,
        "LastUpdateTime": datetime,
    },
)
_OptionalOrganizationConformancePackTypeDef = TypedDict(
    "_OptionalOrganizationConformancePackTypeDef",
    {
        "DeliveryS3Bucket": str,
        "DeliveryS3KeyPrefix": str,
        "ConformancePackInputParameters": List["ConformancePackInputParameterTypeDef"],
        "ExcludedAccounts": List[str],
    },
    total=False,
)


class OrganizationConformancePackTypeDef(
    _RequiredOrganizationConformancePackTypeDef, _OptionalOrganizationConformancePackTypeDef
):
    pass


_RequiredOrganizationCustomRuleMetadataTypeDef = TypedDict(
    "_RequiredOrganizationCustomRuleMetadataTypeDef",
    {
        "LambdaFunctionArn": str,
        "OrganizationConfigRuleTriggerTypes": List[OrganizationConfigRuleTriggerTypeType],
    },
)
_OptionalOrganizationCustomRuleMetadataTypeDef = TypedDict(
    "_OptionalOrganizationCustomRuleMetadataTypeDef",
    {
        "Description": str,
        "InputParameters": str,
        "MaximumExecutionFrequency": MaximumExecutionFrequencyType,
        "ResourceTypesScope": List[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
    },
    total=False,
)


class OrganizationCustomRuleMetadataTypeDef(
    _RequiredOrganizationCustomRuleMetadataTypeDef, _OptionalOrganizationCustomRuleMetadataTypeDef
):
    pass


_RequiredOrganizationManagedRuleMetadataTypeDef = TypedDict(
    "_RequiredOrganizationManagedRuleMetadataTypeDef",
    {
        "RuleIdentifier": str,
    },
)
_OptionalOrganizationManagedRuleMetadataTypeDef = TypedDict(
    "_OptionalOrganizationManagedRuleMetadataTypeDef",
    {
        "Description": str,
        "InputParameters": str,
        "MaximumExecutionFrequency": MaximumExecutionFrequencyType,
        "ResourceTypesScope": List[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
    },
    total=False,
)


class OrganizationManagedRuleMetadataTypeDef(
    _RequiredOrganizationManagedRuleMetadataTypeDef, _OptionalOrganizationManagedRuleMetadataTypeDef
):
    pass


OrganizationResourceDetailedStatusFiltersTypeDef = TypedDict(
    "OrganizationResourceDetailedStatusFiltersTypeDef",
    {
        "AccountId": str,
        "Status": OrganizationResourceDetailedStatusType,
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

PendingAggregationRequestTypeDef = TypedDict(
    "PendingAggregationRequestTypeDef",
    {
        "RequesterAccountId": str,
        "RequesterAwsRegion": str,
    },
    total=False,
)

_RequiredPutAggregationAuthorizationRequestTypeDef = TypedDict(
    "_RequiredPutAggregationAuthorizationRequestTypeDef",
    {
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
    },
)
_OptionalPutAggregationAuthorizationRequestTypeDef = TypedDict(
    "_OptionalPutAggregationAuthorizationRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class PutAggregationAuthorizationRequestTypeDef(
    _RequiredPutAggregationAuthorizationRequestTypeDef,
    _OptionalPutAggregationAuthorizationRequestTypeDef,
):
    pass


PutAggregationAuthorizationResponseResponseTypeDef = TypedDict(
    "PutAggregationAuthorizationResponseResponseTypeDef",
    {
        "AggregationAuthorization": "AggregationAuthorizationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutConfigRuleRequestTypeDef = TypedDict(
    "_RequiredPutConfigRuleRequestTypeDef",
    {
        "ConfigRule": "ConfigRuleTypeDef",
    },
)
_OptionalPutConfigRuleRequestTypeDef = TypedDict(
    "_OptionalPutConfigRuleRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class PutConfigRuleRequestTypeDef(
    _RequiredPutConfigRuleRequestTypeDef, _OptionalPutConfigRuleRequestTypeDef
):
    pass


_RequiredPutConfigurationAggregatorRequestTypeDef = TypedDict(
    "_RequiredPutConfigurationAggregatorRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalPutConfigurationAggregatorRequestTypeDef = TypedDict(
    "_OptionalPutConfigurationAggregatorRequestTypeDef",
    {
        "AccountAggregationSources": List["AccountAggregationSourceTypeDef"],
        "OrganizationAggregationSource": "OrganizationAggregationSourceTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class PutConfigurationAggregatorRequestTypeDef(
    _RequiredPutConfigurationAggregatorRequestTypeDef,
    _OptionalPutConfigurationAggregatorRequestTypeDef,
):
    pass


PutConfigurationAggregatorResponseResponseTypeDef = TypedDict(
    "PutConfigurationAggregatorResponseResponseTypeDef",
    {
        "ConfigurationAggregator": "ConfigurationAggregatorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutConfigurationRecorderRequestTypeDef = TypedDict(
    "PutConfigurationRecorderRequestTypeDef",
    {
        "ConfigurationRecorder": "ConfigurationRecorderTypeDef",
    },
)

_RequiredPutConformancePackRequestTypeDef = TypedDict(
    "_RequiredPutConformancePackRequestTypeDef",
    {
        "ConformancePackName": str,
    },
)
_OptionalPutConformancePackRequestTypeDef = TypedDict(
    "_OptionalPutConformancePackRequestTypeDef",
    {
        "TemplateS3Uri": str,
        "TemplateBody": str,
        "DeliveryS3Bucket": str,
        "DeliveryS3KeyPrefix": str,
        "ConformancePackInputParameters": List["ConformancePackInputParameterTypeDef"],
    },
    total=False,
)


class PutConformancePackRequestTypeDef(
    _RequiredPutConformancePackRequestTypeDef, _OptionalPutConformancePackRequestTypeDef
):
    pass


PutConformancePackResponseResponseTypeDef = TypedDict(
    "PutConformancePackResponseResponseTypeDef",
    {
        "ConformancePackArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutDeliveryChannelRequestTypeDef = TypedDict(
    "PutDeliveryChannelRequestTypeDef",
    {
        "DeliveryChannel": "DeliveryChannelTypeDef",
    },
)

_RequiredPutEvaluationsRequestTypeDef = TypedDict(
    "_RequiredPutEvaluationsRequestTypeDef",
    {
        "ResultToken": str,
    },
)
_OptionalPutEvaluationsRequestTypeDef = TypedDict(
    "_OptionalPutEvaluationsRequestTypeDef",
    {
        "Evaluations": List["EvaluationTypeDef"],
        "TestMode": bool,
    },
    total=False,
)


class PutEvaluationsRequestTypeDef(
    _RequiredPutEvaluationsRequestTypeDef, _OptionalPutEvaluationsRequestTypeDef
):
    pass


PutEvaluationsResponseResponseTypeDef = TypedDict(
    "PutEvaluationsResponseResponseTypeDef",
    {
        "FailedEvaluations": List["EvaluationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutExternalEvaluationRequestTypeDef = TypedDict(
    "PutExternalEvaluationRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ExternalEvaluation": "ExternalEvaluationTypeDef",
    },
)

_RequiredPutOrganizationConfigRuleRequestTypeDef = TypedDict(
    "_RequiredPutOrganizationConfigRuleRequestTypeDef",
    {
        "OrganizationConfigRuleName": str,
    },
)
_OptionalPutOrganizationConfigRuleRequestTypeDef = TypedDict(
    "_OptionalPutOrganizationConfigRuleRequestTypeDef",
    {
        "OrganizationManagedRuleMetadata": "OrganizationManagedRuleMetadataTypeDef",
        "OrganizationCustomRuleMetadata": "OrganizationCustomRuleMetadataTypeDef",
        "ExcludedAccounts": List[str],
    },
    total=False,
)


class PutOrganizationConfigRuleRequestTypeDef(
    _RequiredPutOrganizationConfigRuleRequestTypeDef,
    _OptionalPutOrganizationConfigRuleRequestTypeDef,
):
    pass


PutOrganizationConfigRuleResponseResponseTypeDef = TypedDict(
    "PutOrganizationConfigRuleResponseResponseTypeDef",
    {
        "OrganizationConfigRuleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutOrganizationConformancePackRequestTypeDef = TypedDict(
    "_RequiredPutOrganizationConformancePackRequestTypeDef",
    {
        "OrganizationConformancePackName": str,
    },
)
_OptionalPutOrganizationConformancePackRequestTypeDef = TypedDict(
    "_OptionalPutOrganizationConformancePackRequestTypeDef",
    {
        "TemplateS3Uri": str,
        "TemplateBody": str,
        "DeliveryS3Bucket": str,
        "DeliveryS3KeyPrefix": str,
        "ConformancePackInputParameters": List["ConformancePackInputParameterTypeDef"],
        "ExcludedAccounts": List[str],
    },
    total=False,
)


class PutOrganizationConformancePackRequestTypeDef(
    _RequiredPutOrganizationConformancePackRequestTypeDef,
    _OptionalPutOrganizationConformancePackRequestTypeDef,
):
    pass


PutOrganizationConformancePackResponseResponseTypeDef = TypedDict(
    "PutOrganizationConformancePackResponseResponseTypeDef",
    {
        "OrganizationConformancePackArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRemediationConfigurationsRequestTypeDef = TypedDict(
    "PutRemediationConfigurationsRequestTypeDef",
    {
        "RemediationConfigurations": List["RemediationConfigurationTypeDef"],
    },
)

PutRemediationConfigurationsResponseResponseTypeDef = TypedDict(
    "PutRemediationConfigurationsResponseResponseTypeDef",
    {
        "FailedBatches": List["FailedRemediationBatchTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutRemediationExceptionsRequestTypeDef = TypedDict(
    "_RequiredPutRemediationExceptionsRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": List["RemediationExceptionResourceKeyTypeDef"],
    },
)
_OptionalPutRemediationExceptionsRequestTypeDef = TypedDict(
    "_OptionalPutRemediationExceptionsRequestTypeDef",
    {
        "Message": str,
        "ExpirationTime": Union[datetime, str],
    },
    total=False,
)


class PutRemediationExceptionsRequestTypeDef(
    _RequiredPutRemediationExceptionsRequestTypeDef, _OptionalPutRemediationExceptionsRequestTypeDef
):
    pass


PutRemediationExceptionsResponseResponseTypeDef = TypedDict(
    "PutRemediationExceptionsResponseResponseTypeDef",
    {
        "FailedBatches": List["FailedRemediationExceptionBatchTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutResourceConfigRequestTypeDef = TypedDict(
    "_RequiredPutResourceConfigRequestTypeDef",
    {
        "ResourceType": str,
        "SchemaVersionId": str,
        "ResourceId": str,
        "Configuration": str,
    },
)
_OptionalPutResourceConfigRequestTypeDef = TypedDict(
    "_OptionalPutResourceConfigRequestTypeDef",
    {
        "ResourceName": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class PutResourceConfigRequestTypeDef(
    _RequiredPutResourceConfigRequestTypeDef, _OptionalPutResourceConfigRequestTypeDef
):
    pass


PutRetentionConfigurationRequestTypeDef = TypedDict(
    "PutRetentionConfigurationRequestTypeDef",
    {
        "RetentionPeriodInDays": int,
    },
)

PutRetentionConfigurationResponseResponseTypeDef = TypedDict(
    "PutRetentionConfigurationResponseResponseTypeDef",
    {
        "RetentionConfiguration": "RetentionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutStoredQueryRequestTypeDef = TypedDict(
    "_RequiredPutStoredQueryRequestTypeDef",
    {
        "StoredQuery": "StoredQueryTypeDef",
    },
)
_OptionalPutStoredQueryRequestTypeDef = TypedDict(
    "_OptionalPutStoredQueryRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class PutStoredQueryRequestTypeDef(
    _RequiredPutStoredQueryRequestTypeDef, _OptionalPutStoredQueryRequestTypeDef
):
    pass


PutStoredQueryResponseResponseTypeDef = TypedDict(
    "PutStoredQueryResponseResponseTypeDef",
    {
        "QueryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryInfoTypeDef = TypedDict(
    "QueryInfoTypeDef",
    {
        "SelectFields": List["FieldInfoTypeDef"],
    },
    total=False,
)

RecordingGroupTypeDef = TypedDict(
    "RecordingGroupTypeDef",
    {
        "allSupported": bool,
        "includeGlobalResourceTypes": bool,
        "resourceTypes": List[ResourceTypeType],
    },
    total=False,
)

RelationshipTypeDef = TypedDict(
    "RelationshipTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceId": str,
        "resourceName": str,
        "relationshipName": str,
    },
    total=False,
)

_RequiredRemediationConfigurationTypeDef = TypedDict(
    "_RequiredRemediationConfigurationTypeDef",
    {
        "ConfigRuleName": str,
        "TargetType": Literal["SSM_DOCUMENT"],
        "TargetId": str,
    },
)
_OptionalRemediationConfigurationTypeDef = TypedDict(
    "_OptionalRemediationConfigurationTypeDef",
    {
        "TargetVersion": str,
        "Parameters": Dict[str, "RemediationParameterValueTypeDef"],
        "ResourceType": str,
        "Automatic": bool,
        "ExecutionControls": "ExecutionControlsTypeDef",
        "MaximumAutomaticAttempts": int,
        "RetryAttemptSeconds": int,
        "Arn": str,
        "CreatedByService": str,
    },
    total=False,
)


class RemediationConfigurationTypeDef(
    _RequiredRemediationConfigurationTypeDef, _OptionalRemediationConfigurationTypeDef
):
    pass


RemediationExceptionResourceKeyTypeDef = TypedDict(
    "RemediationExceptionResourceKeyTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
    },
    total=False,
)

_RequiredRemediationExceptionTypeDef = TypedDict(
    "_RequiredRemediationExceptionTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceType": str,
        "ResourceId": str,
    },
)
_OptionalRemediationExceptionTypeDef = TypedDict(
    "_OptionalRemediationExceptionTypeDef",
    {
        "Message": str,
        "ExpirationTime": datetime,
    },
    total=False,
)


class RemediationExceptionTypeDef(
    _RequiredRemediationExceptionTypeDef, _OptionalRemediationExceptionTypeDef
):
    pass


RemediationExecutionStatusTypeDef = TypedDict(
    "RemediationExecutionStatusTypeDef",
    {
        "ResourceKey": "ResourceKeyTypeDef",
        "State": RemediationExecutionStateType,
        "StepDetails": List["RemediationExecutionStepTypeDef"],
        "InvocationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

RemediationExecutionStepTypeDef = TypedDict(
    "RemediationExecutionStepTypeDef",
    {
        "Name": str,
        "State": RemediationExecutionStepStateType,
        "ErrorMessage": str,
        "StartTime": datetime,
        "StopTime": datetime,
    },
    total=False,
)

RemediationParameterValueTypeDef = TypedDict(
    "RemediationParameterValueTypeDef",
    {
        "ResourceValue": "ResourceValueTypeDef",
        "StaticValue": "StaticValueTypeDef",
    },
    total=False,
)

ResourceCountFiltersTypeDef = TypedDict(
    "ResourceCountFiltersTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "AccountId": str,
        "Region": str,
    },
    total=False,
)

ResourceCountTypeDef = TypedDict(
    "ResourceCountTypeDef",
    {
        "resourceType": ResourceTypeType,
        "count": int,
    },
    total=False,
)

ResourceFiltersTypeDef = TypedDict(
    "ResourceFiltersTypeDef",
    {
        "AccountId": str,
        "ResourceId": str,
        "ResourceName": str,
        "Region": str,
    },
    total=False,
)

ResourceIdentifierTypeDef = TypedDict(
    "ResourceIdentifierTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceId": str,
        "resourceName": str,
        "resourceDeletionTime": datetime,
    },
    total=False,
)

ResourceKeyTypeDef = TypedDict(
    "ResourceKeyTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceId": str,
    },
)

ResourceValueTypeDef = TypedDict(
    "ResourceValueTypeDef",
    {
        "Value": Literal["RESOURCE_ID"],
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

RetentionConfigurationTypeDef = TypedDict(
    "RetentionConfigurationTypeDef",
    {
        "Name": str,
        "RetentionPeriodInDays": int,
    },
)

ScopeTypeDef = TypedDict(
    "ScopeTypeDef",
    {
        "ComplianceResourceTypes": List[str],
        "TagKey": str,
        "TagValue": str,
        "ComplianceResourceId": str,
    },
    total=False,
)

_RequiredSelectAggregateResourceConfigRequestTypeDef = TypedDict(
    "_RequiredSelectAggregateResourceConfigRequestTypeDef",
    {
        "Expression": str,
        "ConfigurationAggregatorName": str,
    },
)
_OptionalSelectAggregateResourceConfigRequestTypeDef = TypedDict(
    "_OptionalSelectAggregateResourceConfigRequestTypeDef",
    {
        "Limit": int,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class SelectAggregateResourceConfigRequestTypeDef(
    _RequiredSelectAggregateResourceConfigRequestTypeDef,
    _OptionalSelectAggregateResourceConfigRequestTypeDef,
):
    pass


SelectAggregateResourceConfigResponseResponseTypeDef = TypedDict(
    "SelectAggregateResourceConfigResponseResponseTypeDef",
    {
        "Results": List[str],
        "QueryInfo": "QueryInfoTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSelectResourceConfigRequestTypeDef = TypedDict(
    "_RequiredSelectResourceConfigRequestTypeDef",
    {
        "Expression": str,
    },
)
_OptionalSelectResourceConfigRequestTypeDef = TypedDict(
    "_OptionalSelectResourceConfigRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class SelectResourceConfigRequestTypeDef(
    _RequiredSelectResourceConfigRequestTypeDef, _OptionalSelectResourceConfigRequestTypeDef
):
    pass


SelectResourceConfigResponseResponseTypeDef = TypedDict(
    "SelectResourceConfigResponseResponseTypeDef",
    {
        "Results": List[str],
        "QueryInfo": "QueryInfoTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceDetailTypeDef = TypedDict(
    "SourceDetailTypeDef",
    {
        "EventSource": Literal["aws.config"],
        "MessageType": MessageTypeType,
        "MaximumExecutionFrequency": MaximumExecutionFrequencyType,
    },
    total=False,
)

_RequiredSourceTypeDef = TypedDict(
    "_RequiredSourceTypeDef",
    {
        "Owner": OwnerType,
        "SourceIdentifier": str,
    },
)
_OptionalSourceTypeDef = TypedDict(
    "_OptionalSourceTypeDef",
    {
        "SourceDetails": List["SourceDetailTypeDef"],
    },
    total=False,
)


class SourceTypeDef(_RequiredSourceTypeDef, _OptionalSourceTypeDef):
    pass


SsmControlsTypeDef = TypedDict(
    "SsmControlsTypeDef",
    {
        "ConcurrentExecutionRatePercentage": int,
        "ErrorPercentage": int,
    },
    total=False,
)

StartConfigRulesEvaluationRequestTypeDef = TypedDict(
    "StartConfigRulesEvaluationRequestTypeDef",
    {
        "ConfigRuleNames": List[str],
    },
    total=False,
)

StartConfigurationRecorderRequestTypeDef = TypedDict(
    "StartConfigurationRecorderRequestTypeDef",
    {
        "ConfigurationRecorderName": str,
    },
)

StartRemediationExecutionRequestTypeDef = TypedDict(
    "StartRemediationExecutionRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": List["ResourceKeyTypeDef"],
    },
)

StartRemediationExecutionResponseResponseTypeDef = TypedDict(
    "StartRemediationExecutionResponseResponseTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List["ResourceKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StaticValueTypeDef = TypedDict(
    "StaticValueTypeDef",
    {
        "Values": List[str],
    },
)

StatusDetailFiltersTypeDef = TypedDict(
    "StatusDetailFiltersTypeDef",
    {
        "AccountId": str,
        "MemberAccountRuleStatus": MemberAccountRuleStatusType,
    },
    total=False,
)

StopConfigurationRecorderRequestTypeDef = TypedDict(
    "StopConfigurationRecorderRequestTypeDef",
    {
        "ConfigurationRecorderName": str,
    },
)

_RequiredStoredQueryMetadataTypeDef = TypedDict(
    "_RequiredStoredQueryMetadataTypeDef",
    {
        "QueryId": str,
        "QueryArn": str,
        "QueryName": str,
    },
)
_OptionalStoredQueryMetadataTypeDef = TypedDict(
    "_OptionalStoredQueryMetadataTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class StoredQueryMetadataTypeDef(
    _RequiredStoredQueryMetadataTypeDef, _OptionalStoredQueryMetadataTypeDef
):
    pass


_RequiredStoredQueryTypeDef = TypedDict(
    "_RequiredStoredQueryTypeDef",
    {
        "QueryName": str,
    },
)
_OptionalStoredQueryTypeDef = TypedDict(
    "_OptionalStoredQueryTypeDef",
    {
        "QueryId": str,
        "QueryArn": str,
        "Description": str,
        "Expression": str,
    },
    total=False,
)


class StoredQueryTypeDef(_RequiredStoredQueryTypeDef, _OptionalStoredQueryTypeDef):
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
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)
