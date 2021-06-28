"""
Type annotations for iot service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iot.type_defs import AbortConfigTypeDef

    data: AbortConfigTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ActionTypeType,
    AuditCheckRunStatusType,
    AuditFindingSeverityType,
    AuditFrequencyType,
    AuditMitigationActionsExecutionStatusType,
    AuditMitigationActionsTaskStatusType,
    AuditTaskStatusType,
    AuditTaskTypeType,
    AuthDecisionType,
    AuthorizerStatusType,
    AutoRegistrationStatusType,
    AwsJobAbortCriteriaFailureTypeType,
    BehaviorCriteriaTypeType,
    CACertificateStatusType,
    CannedAccessControlListType,
    CertificateModeType,
    CertificateStatusType,
    ComparisonOperatorType,
    ConfidenceLevelType,
    CustomMetricTypeType,
    DayOfWeekType,
    DetectMitigationActionExecutionStatusType,
    DetectMitigationActionsTaskStatusType,
    DimensionValueOperatorType,
    DomainConfigurationStatusType,
    DomainTypeType,
    DynamicGroupStatusType,
    DynamoKeyTypeType,
    EventTypeType,
    FieldTypeType,
    IndexStatusType,
    JobExecutionFailureTypeType,
    JobExecutionStatusType,
    JobStatusType,
    LogLevelType,
    LogTargetTypeType,
    MessageFormatType,
    MitigationActionTypeType,
    ModelStatusType,
    OTAUpdateStatusType,
    ProtocolType,
    ReportTypeType,
    ResourceTypeType,
    ServerCertificateStatusType,
    ServiceTypeType,
    StatusType,
    TargetSelectionType,
    ThingConnectivityIndexingModeType,
    ThingGroupIndexingModeType,
    ThingIndexingModeType,
    TopicRuleDestinationStatusType,
    ViolationEventTypeType,
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
    "AbortConfigTypeDef",
    "AbortCriteriaTypeDef",
    "AcceptCertificateTransferRequestTypeDef",
    "ActionTypeDef",
    "ActiveViolationTypeDef",
    "AddThingToBillingGroupRequestTypeDef",
    "AddThingToThingGroupRequestTypeDef",
    "AddThingsToThingGroupParamsTypeDef",
    "AlertTargetTypeDef",
    "AllowedTypeDef",
    "AssetPropertyTimestampTypeDef",
    "AssetPropertyValueTypeDef",
    "AssetPropertyVariantTypeDef",
    "AssociateTargetsWithJobRequestTypeDef",
    "AssociateTargetsWithJobResponseResponseTypeDef",
    "AttachPolicyRequestTypeDef",
    "AttachPrincipalPolicyRequestTypeDef",
    "AttachSecurityProfileRequestTypeDef",
    "AttachThingPrincipalRequestTypeDef",
    "AttributePayloadTypeDef",
    "AuditCheckConfigurationTypeDef",
    "AuditCheckDetailsTypeDef",
    "AuditFindingTypeDef",
    "AuditMitigationActionExecutionMetadataTypeDef",
    "AuditMitigationActionsTaskMetadataTypeDef",
    "AuditMitigationActionsTaskTargetTypeDef",
    "AuditNotificationTargetTypeDef",
    "AuditSuppressionTypeDef",
    "AuditTaskMetadataTypeDef",
    "AuthInfoTypeDef",
    "AuthResultTypeDef",
    "AuthorizerConfigTypeDef",
    "AuthorizerDescriptionTypeDef",
    "AuthorizerSummaryTypeDef",
    "AwsJobAbortConfigTypeDef",
    "AwsJobAbortCriteriaTypeDef",
    "AwsJobExecutionsRolloutConfigTypeDef",
    "AwsJobExponentialRolloutRateTypeDef",
    "AwsJobPresignedUrlConfigTypeDef",
    "AwsJobRateIncreaseCriteriaTypeDef",
    "AwsJobTimeoutConfigTypeDef",
    "BehaviorCriteriaTypeDef",
    "BehaviorModelTrainingSummaryTypeDef",
    "BehaviorTypeDef",
    "BillingGroupMetadataTypeDef",
    "BillingGroupPropertiesTypeDef",
    "CACertificateDescriptionTypeDef",
    "CACertificateTypeDef",
    "CancelAuditMitigationActionsTaskRequestTypeDef",
    "CancelAuditTaskRequestTypeDef",
    "CancelCertificateTransferRequestTypeDef",
    "CancelDetectMitigationActionsTaskRequestTypeDef",
    "CancelJobExecutionRequestTypeDef",
    "CancelJobRequestTypeDef",
    "CancelJobResponseResponseTypeDef",
    "CertificateDescriptionTypeDef",
    "CertificateTypeDef",
    "CertificateValidityTypeDef",
    "CloudwatchAlarmActionTypeDef",
    "CloudwatchLogsActionTypeDef",
    "CloudwatchMetricActionTypeDef",
    "CodeSigningCertificateChainTypeDef",
    "CodeSigningSignatureTypeDef",
    "CodeSigningTypeDef",
    "ConfigurationTypeDef",
    "ConfirmTopicRuleDestinationRequestTypeDef",
    "CreateAuditSuppressionRequestTypeDef",
    "CreateAuthorizerRequestTypeDef",
    "CreateAuthorizerResponseResponseTypeDef",
    "CreateBillingGroupRequestTypeDef",
    "CreateBillingGroupResponseResponseTypeDef",
    "CreateCertificateFromCsrRequestTypeDef",
    "CreateCertificateFromCsrResponseResponseTypeDef",
    "CreateCustomMetricRequestTypeDef",
    "CreateCustomMetricResponseResponseTypeDef",
    "CreateDimensionRequestTypeDef",
    "CreateDimensionResponseResponseTypeDef",
    "CreateDomainConfigurationRequestTypeDef",
    "CreateDomainConfigurationResponseResponseTypeDef",
    "CreateDynamicThingGroupRequestTypeDef",
    "CreateDynamicThingGroupResponseResponseTypeDef",
    "CreateJobRequestTypeDef",
    "CreateJobResponseResponseTypeDef",
    "CreateJobTemplateRequestTypeDef",
    "CreateJobTemplateResponseResponseTypeDef",
    "CreateKeysAndCertificateRequestTypeDef",
    "CreateKeysAndCertificateResponseResponseTypeDef",
    "CreateMitigationActionRequestTypeDef",
    "CreateMitigationActionResponseResponseTypeDef",
    "CreateOTAUpdateRequestTypeDef",
    "CreateOTAUpdateResponseResponseTypeDef",
    "CreatePolicyRequestTypeDef",
    "CreatePolicyResponseResponseTypeDef",
    "CreatePolicyVersionRequestTypeDef",
    "CreatePolicyVersionResponseResponseTypeDef",
    "CreateProvisioningClaimRequestTypeDef",
    "CreateProvisioningClaimResponseResponseTypeDef",
    "CreateProvisioningTemplateRequestTypeDef",
    "CreateProvisioningTemplateResponseResponseTypeDef",
    "CreateProvisioningTemplateVersionRequestTypeDef",
    "CreateProvisioningTemplateVersionResponseResponseTypeDef",
    "CreateRoleAliasRequestTypeDef",
    "CreateRoleAliasResponseResponseTypeDef",
    "CreateScheduledAuditRequestTypeDef",
    "CreateScheduledAuditResponseResponseTypeDef",
    "CreateSecurityProfileRequestTypeDef",
    "CreateSecurityProfileResponseResponseTypeDef",
    "CreateStreamRequestTypeDef",
    "CreateStreamResponseResponseTypeDef",
    "CreateThingGroupRequestTypeDef",
    "CreateThingGroupResponseResponseTypeDef",
    "CreateThingRequestTypeDef",
    "CreateThingResponseResponseTypeDef",
    "CreateThingTypeRequestTypeDef",
    "CreateThingTypeResponseResponseTypeDef",
    "CreateTopicRuleDestinationRequestTypeDef",
    "CreateTopicRuleDestinationResponseResponseTypeDef",
    "CreateTopicRuleRequestTypeDef",
    "CustomCodeSigningTypeDef",
    "DeleteAccountAuditConfigurationRequestTypeDef",
    "DeleteAuditSuppressionRequestTypeDef",
    "DeleteAuthorizerRequestTypeDef",
    "DeleteBillingGroupRequestTypeDef",
    "DeleteCACertificateRequestTypeDef",
    "DeleteCertificateRequestTypeDef",
    "DeleteCustomMetricRequestTypeDef",
    "DeleteDimensionRequestTypeDef",
    "DeleteDomainConfigurationRequestTypeDef",
    "DeleteDynamicThingGroupRequestTypeDef",
    "DeleteJobExecutionRequestTypeDef",
    "DeleteJobRequestTypeDef",
    "DeleteJobTemplateRequestTypeDef",
    "DeleteMitigationActionRequestTypeDef",
    "DeleteOTAUpdateRequestTypeDef",
    "DeletePolicyRequestTypeDef",
    "DeletePolicyVersionRequestTypeDef",
    "DeleteProvisioningTemplateRequestTypeDef",
    "DeleteProvisioningTemplateVersionRequestTypeDef",
    "DeleteRoleAliasRequestTypeDef",
    "DeleteScheduledAuditRequestTypeDef",
    "DeleteSecurityProfileRequestTypeDef",
    "DeleteStreamRequestTypeDef",
    "DeleteThingGroupRequestTypeDef",
    "DeleteThingRequestTypeDef",
    "DeleteThingTypeRequestTypeDef",
    "DeleteTopicRuleDestinationRequestTypeDef",
    "DeleteTopicRuleRequestTypeDef",
    "DeleteV2LoggingLevelRequestTypeDef",
    "DeniedTypeDef",
    "DeprecateThingTypeRequestTypeDef",
    "DescribeAccountAuditConfigurationResponseResponseTypeDef",
    "DescribeAuditFindingRequestTypeDef",
    "DescribeAuditFindingResponseResponseTypeDef",
    "DescribeAuditMitigationActionsTaskRequestTypeDef",
    "DescribeAuditMitigationActionsTaskResponseResponseTypeDef",
    "DescribeAuditSuppressionRequestTypeDef",
    "DescribeAuditSuppressionResponseResponseTypeDef",
    "DescribeAuditTaskRequestTypeDef",
    "DescribeAuditTaskResponseResponseTypeDef",
    "DescribeAuthorizerRequestTypeDef",
    "DescribeAuthorizerResponseResponseTypeDef",
    "DescribeBillingGroupRequestTypeDef",
    "DescribeBillingGroupResponseResponseTypeDef",
    "DescribeCACertificateRequestTypeDef",
    "DescribeCACertificateResponseResponseTypeDef",
    "DescribeCertificateRequestTypeDef",
    "DescribeCertificateResponseResponseTypeDef",
    "DescribeCustomMetricRequestTypeDef",
    "DescribeCustomMetricResponseResponseTypeDef",
    "DescribeDefaultAuthorizerResponseResponseTypeDef",
    "DescribeDetectMitigationActionsTaskRequestTypeDef",
    "DescribeDetectMitigationActionsTaskResponseResponseTypeDef",
    "DescribeDimensionRequestTypeDef",
    "DescribeDimensionResponseResponseTypeDef",
    "DescribeDomainConfigurationRequestTypeDef",
    "DescribeDomainConfigurationResponseResponseTypeDef",
    "DescribeEndpointRequestTypeDef",
    "DescribeEndpointResponseResponseTypeDef",
    "DescribeEventConfigurationsResponseResponseTypeDef",
    "DescribeIndexRequestTypeDef",
    "DescribeIndexResponseResponseTypeDef",
    "DescribeJobExecutionRequestTypeDef",
    "DescribeJobExecutionResponseResponseTypeDef",
    "DescribeJobRequestTypeDef",
    "DescribeJobResponseResponseTypeDef",
    "DescribeJobTemplateRequestTypeDef",
    "DescribeJobTemplateResponseResponseTypeDef",
    "DescribeMitigationActionRequestTypeDef",
    "DescribeMitigationActionResponseResponseTypeDef",
    "DescribeProvisioningTemplateRequestTypeDef",
    "DescribeProvisioningTemplateResponseResponseTypeDef",
    "DescribeProvisioningTemplateVersionRequestTypeDef",
    "DescribeProvisioningTemplateVersionResponseResponseTypeDef",
    "DescribeRoleAliasRequestTypeDef",
    "DescribeRoleAliasResponseResponseTypeDef",
    "DescribeScheduledAuditRequestTypeDef",
    "DescribeScheduledAuditResponseResponseTypeDef",
    "DescribeSecurityProfileRequestTypeDef",
    "DescribeSecurityProfileResponseResponseTypeDef",
    "DescribeStreamRequestTypeDef",
    "DescribeStreamResponseResponseTypeDef",
    "DescribeThingGroupRequestTypeDef",
    "DescribeThingGroupResponseResponseTypeDef",
    "DescribeThingRegistrationTaskRequestTypeDef",
    "DescribeThingRegistrationTaskResponseResponseTypeDef",
    "DescribeThingRequestTypeDef",
    "DescribeThingResponseResponseTypeDef",
    "DescribeThingTypeRequestTypeDef",
    "DescribeThingTypeResponseResponseTypeDef",
    "DestinationTypeDef",
    "DetachPolicyRequestTypeDef",
    "DetachPrincipalPolicyRequestTypeDef",
    "DetachSecurityProfileRequestTypeDef",
    "DetachThingPrincipalRequestTypeDef",
    "DetectMitigationActionExecutionTypeDef",
    "DetectMitigationActionsTaskStatisticsTypeDef",
    "DetectMitigationActionsTaskSummaryTypeDef",
    "DetectMitigationActionsTaskTargetTypeDef",
    "DisableTopicRuleRequestTypeDef",
    "DomainConfigurationSummaryTypeDef",
    "DynamoDBActionTypeDef",
    "DynamoDBv2ActionTypeDef",
    "EffectivePolicyTypeDef",
    "ElasticsearchActionTypeDef",
    "EnableIoTLoggingParamsTypeDef",
    "EnableTopicRuleRequestTypeDef",
    "ErrorInfoTypeDef",
    "ExplicitDenyTypeDef",
    "ExponentialRolloutRateTypeDef",
    "FieldTypeDef",
    "FileLocationTypeDef",
    "FirehoseActionTypeDef",
    "GetBehaviorModelTrainingSummariesRequestTypeDef",
    "GetBehaviorModelTrainingSummariesResponseResponseTypeDef",
    "GetCardinalityRequestTypeDef",
    "GetCardinalityResponseResponseTypeDef",
    "GetEffectivePoliciesRequestTypeDef",
    "GetEffectivePoliciesResponseResponseTypeDef",
    "GetIndexingConfigurationResponseResponseTypeDef",
    "GetJobDocumentRequestTypeDef",
    "GetJobDocumentResponseResponseTypeDef",
    "GetLoggingOptionsResponseResponseTypeDef",
    "GetOTAUpdateRequestTypeDef",
    "GetOTAUpdateResponseResponseTypeDef",
    "GetPercentilesRequestTypeDef",
    "GetPercentilesResponseResponseTypeDef",
    "GetPolicyRequestTypeDef",
    "GetPolicyResponseResponseTypeDef",
    "GetPolicyVersionRequestTypeDef",
    "GetPolicyVersionResponseResponseTypeDef",
    "GetRegistrationCodeResponseResponseTypeDef",
    "GetStatisticsRequestTypeDef",
    "GetStatisticsResponseResponseTypeDef",
    "GetTopicRuleDestinationRequestTypeDef",
    "GetTopicRuleDestinationResponseResponseTypeDef",
    "GetTopicRuleRequestTypeDef",
    "GetTopicRuleResponseResponseTypeDef",
    "GetV2LoggingOptionsResponseResponseTypeDef",
    "GroupNameAndArnTypeDef",
    "HttpActionHeaderTypeDef",
    "HttpActionTypeDef",
    "HttpAuthorizationTypeDef",
    "HttpContextTypeDef",
    "HttpUrlDestinationConfigurationTypeDef",
    "HttpUrlDestinationPropertiesTypeDef",
    "HttpUrlDestinationSummaryTypeDef",
    "ImplicitDenyTypeDef",
    "IotAnalyticsActionTypeDef",
    "IotEventsActionTypeDef",
    "IotSiteWiseActionTypeDef",
    "JobExecutionStatusDetailsTypeDef",
    "JobExecutionSummaryForJobTypeDef",
    "JobExecutionSummaryForThingTypeDef",
    "JobExecutionSummaryTypeDef",
    "JobExecutionTypeDef",
    "JobExecutionsRolloutConfigTypeDef",
    "JobProcessDetailsTypeDef",
    "JobSummaryTypeDef",
    "JobTemplateSummaryTypeDef",
    "JobTypeDef",
    "KafkaActionTypeDef",
    "KeyPairTypeDef",
    "KinesisActionTypeDef",
    "LambdaActionTypeDef",
    "ListActiveViolationsRequestTypeDef",
    "ListActiveViolationsResponseResponseTypeDef",
    "ListAttachedPoliciesRequestTypeDef",
    "ListAttachedPoliciesResponseResponseTypeDef",
    "ListAuditFindingsRequestTypeDef",
    "ListAuditFindingsResponseResponseTypeDef",
    "ListAuditMitigationActionsExecutionsRequestTypeDef",
    "ListAuditMitigationActionsExecutionsResponseResponseTypeDef",
    "ListAuditMitigationActionsTasksRequestTypeDef",
    "ListAuditMitigationActionsTasksResponseResponseTypeDef",
    "ListAuditSuppressionsRequestTypeDef",
    "ListAuditSuppressionsResponseResponseTypeDef",
    "ListAuditTasksRequestTypeDef",
    "ListAuditTasksResponseResponseTypeDef",
    "ListAuthorizersRequestTypeDef",
    "ListAuthorizersResponseResponseTypeDef",
    "ListBillingGroupsRequestTypeDef",
    "ListBillingGroupsResponseResponseTypeDef",
    "ListCACertificatesRequestTypeDef",
    "ListCACertificatesResponseResponseTypeDef",
    "ListCertificatesByCARequestTypeDef",
    "ListCertificatesByCAResponseResponseTypeDef",
    "ListCertificatesRequestTypeDef",
    "ListCertificatesResponseResponseTypeDef",
    "ListCustomMetricsRequestTypeDef",
    "ListCustomMetricsResponseResponseTypeDef",
    "ListDetectMitigationActionsExecutionsRequestTypeDef",
    "ListDetectMitigationActionsExecutionsResponseResponseTypeDef",
    "ListDetectMitigationActionsTasksRequestTypeDef",
    "ListDetectMitigationActionsTasksResponseResponseTypeDef",
    "ListDimensionsRequestTypeDef",
    "ListDimensionsResponseResponseTypeDef",
    "ListDomainConfigurationsRequestTypeDef",
    "ListDomainConfigurationsResponseResponseTypeDef",
    "ListIndicesRequestTypeDef",
    "ListIndicesResponseResponseTypeDef",
    "ListJobExecutionsForJobRequestTypeDef",
    "ListJobExecutionsForJobResponseResponseTypeDef",
    "ListJobExecutionsForThingRequestTypeDef",
    "ListJobExecutionsForThingResponseResponseTypeDef",
    "ListJobTemplatesRequestTypeDef",
    "ListJobTemplatesResponseResponseTypeDef",
    "ListJobsRequestTypeDef",
    "ListJobsResponseResponseTypeDef",
    "ListMitigationActionsRequestTypeDef",
    "ListMitigationActionsResponseResponseTypeDef",
    "ListOTAUpdatesRequestTypeDef",
    "ListOTAUpdatesResponseResponseTypeDef",
    "ListOutgoingCertificatesRequestTypeDef",
    "ListOutgoingCertificatesResponseResponseTypeDef",
    "ListPoliciesRequestTypeDef",
    "ListPoliciesResponseResponseTypeDef",
    "ListPolicyPrincipalsRequestTypeDef",
    "ListPolicyPrincipalsResponseResponseTypeDef",
    "ListPolicyVersionsRequestTypeDef",
    "ListPolicyVersionsResponseResponseTypeDef",
    "ListPrincipalPoliciesRequestTypeDef",
    "ListPrincipalPoliciesResponseResponseTypeDef",
    "ListPrincipalThingsRequestTypeDef",
    "ListPrincipalThingsResponseResponseTypeDef",
    "ListProvisioningTemplateVersionsRequestTypeDef",
    "ListProvisioningTemplateVersionsResponseResponseTypeDef",
    "ListProvisioningTemplatesRequestTypeDef",
    "ListProvisioningTemplatesResponseResponseTypeDef",
    "ListRoleAliasesRequestTypeDef",
    "ListRoleAliasesResponseResponseTypeDef",
    "ListScheduledAuditsRequestTypeDef",
    "ListScheduledAuditsResponseResponseTypeDef",
    "ListSecurityProfilesForTargetRequestTypeDef",
    "ListSecurityProfilesForTargetResponseResponseTypeDef",
    "ListSecurityProfilesRequestTypeDef",
    "ListSecurityProfilesResponseResponseTypeDef",
    "ListStreamsRequestTypeDef",
    "ListStreamsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListTargetsForPolicyRequestTypeDef",
    "ListTargetsForPolicyResponseResponseTypeDef",
    "ListTargetsForSecurityProfileRequestTypeDef",
    "ListTargetsForSecurityProfileResponseResponseTypeDef",
    "ListThingGroupsForThingRequestTypeDef",
    "ListThingGroupsForThingResponseResponseTypeDef",
    "ListThingGroupsRequestTypeDef",
    "ListThingGroupsResponseResponseTypeDef",
    "ListThingPrincipalsRequestTypeDef",
    "ListThingPrincipalsResponseResponseTypeDef",
    "ListThingRegistrationTaskReportsRequestTypeDef",
    "ListThingRegistrationTaskReportsResponseResponseTypeDef",
    "ListThingRegistrationTasksRequestTypeDef",
    "ListThingRegistrationTasksResponseResponseTypeDef",
    "ListThingTypesRequestTypeDef",
    "ListThingTypesResponseResponseTypeDef",
    "ListThingsInBillingGroupRequestTypeDef",
    "ListThingsInBillingGroupResponseResponseTypeDef",
    "ListThingsInThingGroupRequestTypeDef",
    "ListThingsInThingGroupResponseResponseTypeDef",
    "ListThingsRequestTypeDef",
    "ListThingsResponseResponseTypeDef",
    "ListTopicRuleDestinationsRequestTypeDef",
    "ListTopicRuleDestinationsResponseResponseTypeDef",
    "ListTopicRulesRequestTypeDef",
    "ListTopicRulesResponseResponseTypeDef",
    "ListV2LoggingLevelsRequestTypeDef",
    "ListV2LoggingLevelsResponseResponseTypeDef",
    "ListViolationEventsRequestTypeDef",
    "ListViolationEventsResponseResponseTypeDef",
    "LogTargetConfigurationTypeDef",
    "LogTargetTypeDef",
    "LoggingOptionsPayloadTypeDef",
    "MachineLearningDetectionConfigTypeDef",
    "MetricDimensionTypeDef",
    "MetricToRetainTypeDef",
    "MetricValueTypeDef",
    "MitigationActionIdentifierTypeDef",
    "MitigationActionParamsTypeDef",
    "MitigationActionTypeDef",
    "MqttContextTypeDef",
    "NonCompliantResourceTypeDef",
    "OTAUpdateFileTypeDef",
    "OTAUpdateInfoTypeDef",
    "OTAUpdateSummaryTypeDef",
    "OutgoingCertificateTypeDef",
    "PaginatorConfigTypeDef",
    "PercentPairTypeDef",
    "PolicyTypeDef",
    "PolicyVersionIdentifierTypeDef",
    "PolicyVersionTypeDef",
    "PresignedUrlConfigTypeDef",
    "ProvisioningHookTypeDef",
    "ProvisioningTemplateSummaryTypeDef",
    "ProvisioningTemplateVersionSummaryTypeDef",
    "PublishFindingToSnsParamsTypeDef",
    "PutAssetPropertyValueEntryTypeDef",
    "PutItemInputTypeDef",
    "RateIncreaseCriteriaTypeDef",
    "RegisterCACertificateRequestTypeDef",
    "RegisterCACertificateResponseResponseTypeDef",
    "RegisterCertificateRequestTypeDef",
    "RegisterCertificateResponseResponseTypeDef",
    "RegisterCertificateWithoutCARequestTypeDef",
    "RegisterCertificateWithoutCAResponseResponseTypeDef",
    "RegisterThingRequestTypeDef",
    "RegisterThingResponseResponseTypeDef",
    "RegistrationConfigTypeDef",
    "RejectCertificateTransferRequestTypeDef",
    "RelatedResourceTypeDef",
    "RemoveThingFromBillingGroupRequestTypeDef",
    "RemoveThingFromThingGroupRequestTypeDef",
    "ReplaceDefaultPolicyVersionParamsTypeDef",
    "ReplaceTopicRuleRequestTypeDef",
    "RepublishActionTypeDef",
    "ResourceIdentifierTypeDef",
    "ResponseMetadataTypeDef",
    "RoleAliasDescriptionTypeDef",
    "S3ActionTypeDef",
    "S3DestinationTypeDef",
    "S3LocationTypeDef",
    "SalesforceActionTypeDef",
    "ScheduledAuditMetadataTypeDef",
    "SearchIndexRequestTypeDef",
    "SearchIndexResponseResponseTypeDef",
    "SecurityProfileIdentifierTypeDef",
    "SecurityProfileTargetMappingTypeDef",
    "SecurityProfileTargetTypeDef",
    "ServerCertificateSummaryTypeDef",
    "SetDefaultAuthorizerRequestTypeDef",
    "SetDefaultAuthorizerResponseResponseTypeDef",
    "SetDefaultPolicyVersionRequestTypeDef",
    "SetLoggingOptionsRequestTypeDef",
    "SetV2LoggingLevelRequestTypeDef",
    "SetV2LoggingOptionsRequestTypeDef",
    "SigV4AuthorizationTypeDef",
    "SigningProfileParameterTypeDef",
    "SnsActionTypeDef",
    "SqsActionTypeDef",
    "StartAuditMitigationActionsTaskRequestTypeDef",
    "StartAuditMitigationActionsTaskResponseResponseTypeDef",
    "StartDetectMitigationActionsTaskRequestTypeDef",
    "StartDetectMitigationActionsTaskResponseResponseTypeDef",
    "StartOnDemandAuditTaskRequestTypeDef",
    "StartOnDemandAuditTaskResponseResponseTypeDef",
    "StartSigningJobParameterTypeDef",
    "StartThingRegistrationTaskRequestTypeDef",
    "StartThingRegistrationTaskResponseResponseTypeDef",
    "StatisticalThresholdTypeDef",
    "StatisticsTypeDef",
    "StepFunctionsActionTypeDef",
    "StopThingRegistrationTaskRequestTypeDef",
    "StreamFileTypeDef",
    "StreamInfoTypeDef",
    "StreamSummaryTypeDef",
    "StreamTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TaskStatisticsForAuditCheckTypeDef",
    "TaskStatisticsTypeDef",
    "TestAuthorizationRequestTypeDef",
    "TestAuthorizationResponseResponseTypeDef",
    "TestInvokeAuthorizerRequestTypeDef",
    "TestInvokeAuthorizerResponseResponseTypeDef",
    "ThingAttributeTypeDef",
    "ThingConnectivityTypeDef",
    "ThingDocumentTypeDef",
    "ThingGroupDocumentTypeDef",
    "ThingGroupIndexingConfigurationTypeDef",
    "ThingGroupMetadataTypeDef",
    "ThingGroupPropertiesTypeDef",
    "ThingIndexingConfigurationTypeDef",
    "ThingTypeDefinitionTypeDef",
    "ThingTypeMetadataTypeDef",
    "ThingTypePropertiesTypeDef",
    "TimeoutConfigTypeDef",
    "TimestreamActionTypeDef",
    "TimestreamDimensionTypeDef",
    "TimestreamTimestampTypeDef",
    "TlsContextTypeDef",
    "TopicRuleDestinationConfigurationTypeDef",
    "TopicRuleDestinationSummaryTypeDef",
    "TopicRuleDestinationTypeDef",
    "TopicRuleListItemTypeDef",
    "TopicRulePayloadTypeDef",
    "TopicRuleTypeDef",
    "TransferCertificateRequestTypeDef",
    "TransferCertificateResponseResponseTypeDef",
    "TransferDataTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAccountAuditConfigurationRequestTypeDef",
    "UpdateAuditSuppressionRequestTypeDef",
    "UpdateAuthorizerRequestTypeDef",
    "UpdateAuthorizerResponseResponseTypeDef",
    "UpdateBillingGroupRequestTypeDef",
    "UpdateBillingGroupResponseResponseTypeDef",
    "UpdateCACertificateParamsTypeDef",
    "UpdateCACertificateRequestTypeDef",
    "UpdateCertificateRequestTypeDef",
    "UpdateCustomMetricRequestTypeDef",
    "UpdateCustomMetricResponseResponseTypeDef",
    "UpdateDeviceCertificateParamsTypeDef",
    "UpdateDimensionRequestTypeDef",
    "UpdateDimensionResponseResponseTypeDef",
    "UpdateDomainConfigurationRequestTypeDef",
    "UpdateDomainConfigurationResponseResponseTypeDef",
    "UpdateDynamicThingGroupRequestTypeDef",
    "UpdateDynamicThingGroupResponseResponseTypeDef",
    "UpdateEventConfigurationsRequestTypeDef",
    "UpdateIndexingConfigurationRequestTypeDef",
    "UpdateJobRequestTypeDef",
    "UpdateMitigationActionRequestTypeDef",
    "UpdateMitigationActionResponseResponseTypeDef",
    "UpdateProvisioningTemplateRequestTypeDef",
    "UpdateRoleAliasRequestTypeDef",
    "UpdateRoleAliasResponseResponseTypeDef",
    "UpdateScheduledAuditRequestTypeDef",
    "UpdateScheduledAuditResponseResponseTypeDef",
    "UpdateSecurityProfileRequestTypeDef",
    "UpdateSecurityProfileResponseResponseTypeDef",
    "UpdateStreamRequestTypeDef",
    "UpdateStreamResponseResponseTypeDef",
    "UpdateThingGroupRequestTypeDef",
    "UpdateThingGroupResponseResponseTypeDef",
    "UpdateThingGroupsForThingRequestTypeDef",
    "UpdateThingRequestTypeDef",
    "UpdateTopicRuleDestinationRequestTypeDef",
    "ValidateSecurityProfileBehaviorsRequestTypeDef",
    "ValidateSecurityProfileBehaviorsResponseResponseTypeDef",
    "ValidationErrorTypeDef",
    "ViolationEventAdditionalInfoTypeDef",
    "ViolationEventOccurrenceRangeTypeDef",
    "ViolationEventTypeDef",
    "VpcDestinationConfigurationTypeDef",
    "VpcDestinationPropertiesTypeDef",
    "VpcDestinationSummaryTypeDef",
)

AbortConfigTypeDef = TypedDict(
    "AbortConfigTypeDef",
    {
        "criteriaList": List["AbortCriteriaTypeDef"],
    },
)

AbortCriteriaTypeDef = TypedDict(
    "AbortCriteriaTypeDef",
    {
        "failureType": JobExecutionFailureTypeType,
        "action": Literal["CANCEL"],
        "thresholdPercentage": float,
        "minNumberOfExecutedThings": int,
    },
)

_RequiredAcceptCertificateTransferRequestTypeDef = TypedDict(
    "_RequiredAcceptCertificateTransferRequestTypeDef",
    {
        "certificateId": str,
    },
)
_OptionalAcceptCertificateTransferRequestTypeDef = TypedDict(
    "_OptionalAcceptCertificateTransferRequestTypeDef",
    {
        "setAsActive": bool,
    },
    total=False,
)


class AcceptCertificateTransferRequestTypeDef(
    _RequiredAcceptCertificateTransferRequestTypeDef,
    _OptionalAcceptCertificateTransferRequestTypeDef,
):
    pass


ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "dynamoDB": "DynamoDBActionTypeDef",
        "dynamoDBv2": "DynamoDBv2ActionTypeDef",
        "lambda": "LambdaActionTypeDef",
        "sns": "SnsActionTypeDef",
        "sqs": "SqsActionTypeDef",
        "kinesis": "KinesisActionTypeDef",
        "republish": "RepublishActionTypeDef",
        "s3": "S3ActionTypeDef",
        "firehose": "FirehoseActionTypeDef",
        "cloudwatchMetric": "CloudwatchMetricActionTypeDef",
        "cloudwatchAlarm": "CloudwatchAlarmActionTypeDef",
        "cloudwatchLogs": "CloudwatchLogsActionTypeDef",
        "elasticsearch": "ElasticsearchActionTypeDef",
        "salesforce": "SalesforceActionTypeDef",
        "iotAnalytics": "IotAnalyticsActionTypeDef",
        "iotEvents": "IotEventsActionTypeDef",
        "iotSiteWise": "IotSiteWiseActionTypeDef",
        "stepFunctions": "StepFunctionsActionTypeDef",
        "timestream": "TimestreamActionTypeDef",
        "http": "HttpActionTypeDef",
        "kafka": "KafkaActionTypeDef",
    },
    total=False,
)

ActiveViolationTypeDef = TypedDict(
    "ActiveViolationTypeDef",
    {
        "violationId": str,
        "thingName": str,
        "securityProfileName": str,
        "behavior": "BehaviorTypeDef",
        "lastViolationValue": "MetricValueTypeDef",
        "violationEventAdditionalInfo": "ViolationEventAdditionalInfoTypeDef",
        "lastViolationTime": datetime,
        "violationStartTime": datetime,
    },
    total=False,
)

AddThingToBillingGroupRequestTypeDef = TypedDict(
    "AddThingToBillingGroupRequestTypeDef",
    {
        "billingGroupName": str,
        "billingGroupArn": str,
        "thingName": str,
        "thingArn": str,
    },
    total=False,
)

AddThingToThingGroupRequestTypeDef = TypedDict(
    "AddThingToThingGroupRequestTypeDef",
    {
        "thingGroupName": str,
        "thingGroupArn": str,
        "thingName": str,
        "thingArn": str,
        "overrideDynamicGroups": bool,
    },
    total=False,
)

_RequiredAddThingsToThingGroupParamsTypeDef = TypedDict(
    "_RequiredAddThingsToThingGroupParamsTypeDef",
    {
        "thingGroupNames": List[str],
    },
)
_OptionalAddThingsToThingGroupParamsTypeDef = TypedDict(
    "_OptionalAddThingsToThingGroupParamsTypeDef",
    {
        "overrideDynamicGroups": bool,
    },
    total=False,
)


class AddThingsToThingGroupParamsTypeDef(
    _RequiredAddThingsToThingGroupParamsTypeDef, _OptionalAddThingsToThingGroupParamsTypeDef
):
    pass


AlertTargetTypeDef = TypedDict(
    "AlertTargetTypeDef",
    {
        "alertTargetArn": str,
        "roleArn": str,
    },
)

AllowedTypeDef = TypedDict(
    "AllowedTypeDef",
    {
        "policies": List["PolicyTypeDef"],
    },
    total=False,
)

_RequiredAssetPropertyTimestampTypeDef = TypedDict(
    "_RequiredAssetPropertyTimestampTypeDef",
    {
        "timeInSeconds": str,
    },
)
_OptionalAssetPropertyTimestampTypeDef = TypedDict(
    "_OptionalAssetPropertyTimestampTypeDef",
    {
        "offsetInNanos": str,
    },
    total=False,
)


class AssetPropertyTimestampTypeDef(
    _RequiredAssetPropertyTimestampTypeDef, _OptionalAssetPropertyTimestampTypeDef
):
    pass


_RequiredAssetPropertyValueTypeDef = TypedDict(
    "_RequiredAssetPropertyValueTypeDef",
    {
        "value": "AssetPropertyVariantTypeDef",
        "timestamp": "AssetPropertyTimestampTypeDef",
    },
)
_OptionalAssetPropertyValueTypeDef = TypedDict(
    "_OptionalAssetPropertyValueTypeDef",
    {
        "quality": str,
    },
    total=False,
)


class AssetPropertyValueTypeDef(
    _RequiredAssetPropertyValueTypeDef, _OptionalAssetPropertyValueTypeDef
):
    pass


AssetPropertyVariantTypeDef = TypedDict(
    "AssetPropertyVariantTypeDef",
    {
        "stringValue": str,
        "integerValue": str,
        "doubleValue": str,
        "booleanValue": str,
    },
    total=False,
)

_RequiredAssociateTargetsWithJobRequestTypeDef = TypedDict(
    "_RequiredAssociateTargetsWithJobRequestTypeDef",
    {
        "targets": List[str],
        "jobId": str,
    },
)
_OptionalAssociateTargetsWithJobRequestTypeDef = TypedDict(
    "_OptionalAssociateTargetsWithJobRequestTypeDef",
    {
        "comment": str,
        "namespaceId": str,
    },
    total=False,
)


class AssociateTargetsWithJobRequestTypeDef(
    _RequiredAssociateTargetsWithJobRequestTypeDef, _OptionalAssociateTargetsWithJobRequestTypeDef
):
    pass


AssociateTargetsWithJobResponseResponseTypeDef = TypedDict(
    "AssociateTargetsWithJobResponseResponseTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachPolicyRequestTypeDef = TypedDict(
    "AttachPolicyRequestTypeDef",
    {
        "policyName": str,
        "target": str,
    },
)

AttachPrincipalPolicyRequestTypeDef = TypedDict(
    "AttachPrincipalPolicyRequestTypeDef",
    {
        "policyName": str,
        "principal": str,
    },
)

AttachSecurityProfileRequestTypeDef = TypedDict(
    "AttachSecurityProfileRequestTypeDef",
    {
        "securityProfileName": str,
        "securityProfileTargetArn": str,
    },
)

AttachThingPrincipalRequestTypeDef = TypedDict(
    "AttachThingPrincipalRequestTypeDef",
    {
        "thingName": str,
        "principal": str,
    },
)

AttributePayloadTypeDef = TypedDict(
    "AttributePayloadTypeDef",
    {
        "attributes": Dict[str, str],
        "merge": bool,
    },
    total=False,
)

AuditCheckConfigurationTypeDef = TypedDict(
    "AuditCheckConfigurationTypeDef",
    {
        "enabled": bool,
    },
    total=False,
)

AuditCheckDetailsTypeDef = TypedDict(
    "AuditCheckDetailsTypeDef",
    {
        "checkRunStatus": AuditCheckRunStatusType,
        "checkCompliant": bool,
        "totalResourcesCount": int,
        "nonCompliantResourcesCount": int,
        "suppressedNonCompliantResourcesCount": int,
        "errorCode": str,
        "message": str,
    },
    total=False,
)

AuditFindingTypeDef = TypedDict(
    "AuditFindingTypeDef",
    {
        "findingId": str,
        "taskId": str,
        "checkName": str,
        "taskStartTime": datetime,
        "findingTime": datetime,
        "severity": AuditFindingSeverityType,
        "nonCompliantResource": "NonCompliantResourceTypeDef",
        "relatedResources": List["RelatedResourceTypeDef"],
        "reasonForNonCompliance": str,
        "reasonForNonComplianceCode": str,
        "isSuppressed": bool,
    },
    total=False,
)

AuditMitigationActionExecutionMetadataTypeDef = TypedDict(
    "AuditMitigationActionExecutionMetadataTypeDef",
    {
        "taskId": str,
        "findingId": str,
        "actionName": str,
        "actionId": str,
        "status": AuditMitigationActionsExecutionStatusType,
        "startTime": datetime,
        "endTime": datetime,
        "errorCode": str,
        "message": str,
    },
    total=False,
)

AuditMitigationActionsTaskMetadataTypeDef = TypedDict(
    "AuditMitigationActionsTaskMetadataTypeDef",
    {
        "taskId": str,
        "startTime": datetime,
        "taskStatus": AuditMitigationActionsTaskStatusType,
    },
    total=False,
)

AuditMitigationActionsTaskTargetTypeDef = TypedDict(
    "AuditMitigationActionsTaskTargetTypeDef",
    {
        "auditTaskId": str,
        "findingIds": List[str],
        "auditCheckToReasonCodeFilter": Dict[str, List[str]],
    },
    total=False,
)

AuditNotificationTargetTypeDef = TypedDict(
    "AuditNotificationTargetTypeDef",
    {
        "targetArn": str,
        "roleArn": str,
        "enabled": bool,
    },
    total=False,
)

_RequiredAuditSuppressionTypeDef = TypedDict(
    "_RequiredAuditSuppressionTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
    },
)
_OptionalAuditSuppressionTypeDef = TypedDict(
    "_OptionalAuditSuppressionTypeDef",
    {
        "expirationDate": datetime,
        "suppressIndefinitely": bool,
        "description": str,
    },
    total=False,
)


class AuditSuppressionTypeDef(_RequiredAuditSuppressionTypeDef, _OptionalAuditSuppressionTypeDef):
    pass


AuditTaskMetadataTypeDef = TypedDict(
    "AuditTaskMetadataTypeDef",
    {
        "taskId": str,
        "taskStatus": AuditTaskStatusType,
        "taskType": AuditTaskTypeType,
    },
    total=False,
)

_RequiredAuthInfoTypeDef = TypedDict(
    "_RequiredAuthInfoTypeDef",
    {
        "resources": List[str],
    },
)
_OptionalAuthInfoTypeDef = TypedDict(
    "_OptionalAuthInfoTypeDef",
    {
        "actionType": ActionTypeType,
    },
    total=False,
)


class AuthInfoTypeDef(_RequiredAuthInfoTypeDef, _OptionalAuthInfoTypeDef):
    pass


AuthResultTypeDef = TypedDict(
    "AuthResultTypeDef",
    {
        "authInfo": "AuthInfoTypeDef",
        "allowed": "AllowedTypeDef",
        "denied": "DeniedTypeDef",
        "authDecision": AuthDecisionType,
        "missingContextValues": List[str],
    },
    total=False,
)

AuthorizerConfigTypeDef = TypedDict(
    "AuthorizerConfigTypeDef",
    {
        "defaultAuthorizerName": str,
        "allowAuthorizerOverride": bool,
    },
    total=False,
)

AuthorizerDescriptionTypeDef = TypedDict(
    "AuthorizerDescriptionTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
        "authorizerFunctionArn": str,
        "tokenKeyName": str,
        "tokenSigningPublicKeys": Dict[str, str],
        "status": AuthorizerStatusType,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "signingDisabled": bool,
    },
    total=False,
)

AuthorizerSummaryTypeDef = TypedDict(
    "AuthorizerSummaryTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
    },
    total=False,
)

AwsJobAbortConfigTypeDef = TypedDict(
    "AwsJobAbortConfigTypeDef",
    {
        "abortCriteriaList": List["AwsJobAbortCriteriaTypeDef"],
    },
)

AwsJobAbortCriteriaTypeDef = TypedDict(
    "AwsJobAbortCriteriaTypeDef",
    {
        "failureType": AwsJobAbortCriteriaFailureTypeType,
        "action": Literal["CANCEL"],
        "thresholdPercentage": float,
        "minNumberOfExecutedThings": int,
    },
)

AwsJobExecutionsRolloutConfigTypeDef = TypedDict(
    "AwsJobExecutionsRolloutConfigTypeDef",
    {
        "maximumPerMinute": int,
        "exponentialRate": "AwsJobExponentialRolloutRateTypeDef",
    },
    total=False,
)

AwsJobExponentialRolloutRateTypeDef = TypedDict(
    "AwsJobExponentialRolloutRateTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": "AwsJobRateIncreaseCriteriaTypeDef",
    },
)

AwsJobPresignedUrlConfigTypeDef = TypedDict(
    "AwsJobPresignedUrlConfigTypeDef",
    {
        "expiresInSec": int,
    },
    total=False,
)

AwsJobRateIncreaseCriteriaTypeDef = TypedDict(
    "AwsJobRateIncreaseCriteriaTypeDef",
    {
        "numberOfNotifiedThings": int,
        "numberOfSucceededThings": int,
    },
    total=False,
)

AwsJobTimeoutConfigTypeDef = TypedDict(
    "AwsJobTimeoutConfigTypeDef",
    {
        "inProgressTimeoutInMinutes": int,
    },
    total=False,
)

BehaviorCriteriaTypeDef = TypedDict(
    "BehaviorCriteriaTypeDef",
    {
        "comparisonOperator": ComparisonOperatorType,
        "value": "MetricValueTypeDef",
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": "StatisticalThresholdTypeDef",
        "mlDetectionConfig": "MachineLearningDetectionConfigTypeDef",
    },
    total=False,
)

BehaviorModelTrainingSummaryTypeDef = TypedDict(
    "BehaviorModelTrainingSummaryTypeDef",
    {
        "securityProfileName": str,
        "behaviorName": str,
        "trainingDataCollectionStartDate": datetime,
        "modelStatus": ModelStatusType,
        "datapointsCollectionPercentage": float,
        "lastModelRefreshDate": datetime,
    },
    total=False,
)

_RequiredBehaviorTypeDef = TypedDict(
    "_RequiredBehaviorTypeDef",
    {
        "name": str,
    },
)
_OptionalBehaviorTypeDef = TypedDict(
    "_OptionalBehaviorTypeDef",
    {
        "metric": str,
        "metricDimension": "MetricDimensionTypeDef",
        "criteria": "BehaviorCriteriaTypeDef",
        "suppressAlerts": bool,
    },
    total=False,
)


class BehaviorTypeDef(_RequiredBehaviorTypeDef, _OptionalBehaviorTypeDef):
    pass


BillingGroupMetadataTypeDef = TypedDict(
    "BillingGroupMetadataTypeDef",
    {
        "creationDate": datetime,
    },
    total=False,
)

BillingGroupPropertiesTypeDef = TypedDict(
    "BillingGroupPropertiesTypeDef",
    {
        "billingGroupDescription": str,
    },
    total=False,
)

CACertificateDescriptionTypeDef = TypedDict(
    "CACertificateDescriptionTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": CACertificateStatusType,
        "certificatePem": str,
        "ownedBy": str,
        "creationDate": datetime,
        "autoRegistrationStatus": AutoRegistrationStatusType,
        "lastModifiedDate": datetime,
        "customerVersion": int,
        "generationId": str,
        "validity": "CertificateValidityTypeDef",
    },
    total=False,
)

CACertificateTypeDef = TypedDict(
    "CACertificateTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": CACertificateStatusType,
        "creationDate": datetime,
    },
    total=False,
)

CancelAuditMitigationActionsTaskRequestTypeDef = TypedDict(
    "CancelAuditMitigationActionsTaskRequestTypeDef",
    {
        "taskId": str,
    },
)

CancelAuditTaskRequestTypeDef = TypedDict(
    "CancelAuditTaskRequestTypeDef",
    {
        "taskId": str,
    },
)

CancelCertificateTransferRequestTypeDef = TypedDict(
    "CancelCertificateTransferRequestTypeDef",
    {
        "certificateId": str,
    },
)

CancelDetectMitigationActionsTaskRequestTypeDef = TypedDict(
    "CancelDetectMitigationActionsTaskRequestTypeDef",
    {
        "taskId": str,
    },
)

_RequiredCancelJobExecutionRequestTypeDef = TypedDict(
    "_RequiredCancelJobExecutionRequestTypeDef",
    {
        "jobId": str,
        "thingName": str,
    },
)
_OptionalCancelJobExecutionRequestTypeDef = TypedDict(
    "_OptionalCancelJobExecutionRequestTypeDef",
    {
        "force": bool,
        "expectedVersion": int,
        "statusDetails": Dict[str, str],
    },
    total=False,
)


class CancelJobExecutionRequestTypeDef(
    _RequiredCancelJobExecutionRequestTypeDef, _OptionalCancelJobExecutionRequestTypeDef
):
    pass


_RequiredCancelJobRequestTypeDef = TypedDict(
    "_RequiredCancelJobRequestTypeDef",
    {
        "jobId": str,
    },
)
_OptionalCancelJobRequestTypeDef = TypedDict(
    "_OptionalCancelJobRequestTypeDef",
    {
        "reasonCode": str,
        "comment": str,
        "force": bool,
    },
    total=False,
)


class CancelJobRequestTypeDef(_RequiredCancelJobRequestTypeDef, _OptionalCancelJobRequestTypeDef):
    pass


CancelJobResponseResponseTypeDef = TypedDict(
    "CancelJobResponseResponseTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CertificateDescriptionTypeDef = TypedDict(
    "CertificateDescriptionTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "caCertificateId": str,
        "status": CertificateStatusType,
        "certificatePem": str,
        "ownedBy": str,
        "previousOwnedBy": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "customerVersion": int,
        "transferData": "TransferDataTypeDef",
        "generationId": str,
        "validity": "CertificateValidityTypeDef",
        "certificateMode": CertificateModeType,
    },
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": CertificateStatusType,
        "certificateMode": CertificateModeType,
        "creationDate": datetime,
    },
    total=False,
)

CertificateValidityTypeDef = TypedDict(
    "CertificateValidityTypeDef",
    {
        "notBefore": datetime,
        "notAfter": datetime,
    },
    total=False,
)

CloudwatchAlarmActionTypeDef = TypedDict(
    "CloudwatchAlarmActionTypeDef",
    {
        "roleArn": str,
        "alarmName": str,
        "stateReason": str,
        "stateValue": str,
    },
)

CloudwatchLogsActionTypeDef = TypedDict(
    "CloudwatchLogsActionTypeDef",
    {
        "roleArn": str,
        "logGroupName": str,
    },
)

_RequiredCloudwatchMetricActionTypeDef = TypedDict(
    "_RequiredCloudwatchMetricActionTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
    },
)
_OptionalCloudwatchMetricActionTypeDef = TypedDict(
    "_OptionalCloudwatchMetricActionTypeDef",
    {
        "metricTimestamp": str,
    },
    total=False,
)


class CloudwatchMetricActionTypeDef(
    _RequiredCloudwatchMetricActionTypeDef, _OptionalCloudwatchMetricActionTypeDef
):
    pass


CodeSigningCertificateChainTypeDef = TypedDict(
    "CodeSigningCertificateChainTypeDef",
    {
        "certificateName": str,
        "inlineDocument": str,
    },
    total=False,
)

CodeSigningSignatureTypeDef = TypedDict(
    "CodeSigningSignatureTypeDef",
    {
        "inlineDocument": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

CodeSigningTypeDef = TypedDict(
    "CodeSigningTypeDef",
    {
        "awsSignerJobId": str,
        "startSigningJobParameter": "StartSigningJobParameterTypeDef",
        "customCodeSigning": "CustomCodeSigningTypeDef",
    },
    total=False,
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

ConfirmTopicRuleDestinationRequestTypeDef = TypedDict(
    "ConfirmTopicRuleDestinationRequestTypeDef",
    {
        "confirmationToken": str,
    },
)

_RequiredCreateAuditSuppressionRequestTypeDef = TypedDict(
    "_RequiredCreateAuditSuppressionRequestTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
        "clientRequestToken": str,
    },
)
_OptionalCreateAuditSuppressionRequestTypeDef = TypedDict(
    "_OptionalCreateAuditSuppressionRequestTypeDef",
    {
        "expirationDate": Union[datetime, str],
        "suppressIndefinitely": bool,
        "description": str,
    },
    total=False,
)


class CreateAuditSuppressionRequestTypeDef(
    _RequiredCreateAuditSuppressionRequestTypeDef, _OptionalCreateAuditSuppressionRequestTypeDef
):
    pass


_RequiredCreateAuthorizerRequestTypeDef = TypedDict(
    "_RequiredCreateAuthorizerRequestTypeDef",
    {
        "authorizerName": str,
        "authorizerFunctionArn": str,
    },
)
_OptionalCreateAuthorizerRequestTypeDef = TypedDict(
    "_OptionalCreateAuthorizerRequestTypeDef",
    {
        "tokenKeyName": str,
        "tokenSigningPublicKeys": Dict[str, str],
        "status": AuthorizerStatusType,
        "tags": List["TagTypeDef"],
        "signingDisabled": bool,
    },
    total=False,
)


class CreateAuthorizerRequestTypeDef(
    _RequiredCreateAuthorizerRequestTypeDef, _OptionalCreateAuthorizerRequestTypeDef
):
    pass


CreateAuthorizerResponseResponseTypeDef = TypedDict(
    "CreateAuthorizerResponseResponseTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBillingGroupRequestTypeDef = TypedDict(
    "_RequiredCreateBillingGroupRequestTypeDef",
    {
        "billingGroupName": str,
    },
)
_OptionalCreateBillingGroupRequestTypeDef = TypedDict(
    "_OptionalCreateBillingGroupRequestTypeDef",
    {
        "billingGroupProperties": "BillingGroupPropertiesTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateBillingGroupRequestTypeDef(
    _RequiredCreateBillingGroupRequestTypeDef, _OptionalCreateBillingGroupRequestTypeDef
):
    pass


CreateBillingGroupResponseResponseTypeDef = TypedDict(
    "CreateBillingGroupResponseResponseTypeDef",
    {
        "billingGroupName": str,
        "billingGroupArn": str,
        "billingGroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCertificateFromCsrRequestTypeDef = TypedDict(
    "_RequiredCreateCertificateFromCsrRequestTypeDef",
    {
        "certificateSigningRequest": str,
    },
)
_OptionalCreateCertificateFromCsrRequestTypeDef = TypedDict(
    "_OptionalCreateCertificateFromCsrRequestTypeDef",
    {
        "setAsActive": bool,
    },
    total=False,
)


class CreateCertificateFromCsrRequestTypeDef(
    _RequiredCreateCertificateFromCsrRequestTypeDef, _OptionalCreateCertificateFromCsrRequestTypeDef
):
    pass


CreateCertificateFromCsrResponseResponseTypeDef = TypedDict(
    "CreateCertificateFromCsrResponseResponseTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "certificatePem": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCustomMetricRequestTypeDef = TypedDict(
    "_RequiredCreateCustomMetricRequestTypeDef",
    {
        "metricName": str,
        "metricType": CustomMetricTypeType,
        "clientRequestToken": str,
    },
)
_OptionalCreateCustomMetricRequestTypeDef = TypedDict(
    "_OptionalCreateCustomMetricRequestTypeDef",
    {
        "displayName": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateCustomMetricRequestTypeDef(
    _RequiredCreateCustomMetricRequestTypeDef, _OptionalCreateCustomMetricRequestTypeDef
):
    pass


CreateCustomMetricResponseResponseTypeDef = TypedDict(
    "CreateCustomMetricResponseResponseTypeDef",
    {
        "metricName": str,
        "metricArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDimensionRequestTypeDef = TypedDict(
    "_RequiredCreateDimensionRequestTypeDef",
    {
        "name": str,
        "type": Literal["TOPIC_FILTER"],
        "stringValues": List[str],
        "clientRequestToken": str,
    },
)
_OptionalCreateDimensionRequestTypeDef = TypedDict(
    "_OptionalCreateDimensionRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDimensionRequestTypeDef(
    _RequiredCreateDimensionRequestTypeDef, _OptionalCreateDimensionRequestTypeDef
):
    pass


CreateDimensionResponseResponseTypeDef = TypedDict(
    "CreateDimensionResponseResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDomainConfigurationRequestTypeDef = TypedDict(
    "_RequiredCreateDomainConfigurationRequestTypeDef",
    {
        "domainConfigurationName": str,
    },
)
_OptionalCreateDomainConfigurationRequestTypeDef = TypedDict(
    "_OptionalCreateDomainConfigurationRequestTypeDef",
    {
        "domainName": str,
        "serverCertificateArns": List[str],
        "validationCertificateArn": str,
        "authorizerConfig": "AuthorizerConfigTypeDef",
        "serviceType": ServiceTypeType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDomainConfigurationRequestTypeDef(
    _RequiredCreateDomainConfigurationRequestTypeDef,
    _OptionalCreateDomainConfigurationRequestTypeDef,
):
    pass


CreateDomainConfigurationResponseResponseTypeDef = TypedDict(
    "CreateDomainConfigurationResponseResponseTypeDef",
    {
        "domainConfigurationName": str,
        "domainConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDynamicThingGroupRequestTypeDef = TypedDict(
    "_RequiredCreateDynamicThingGroupRequestTypeDef",
    {
        "thingGroupName": str,
        "queryString": str,
    },
)
_OptionalCreateDynamicThingGroupRequestTypeDef = TypedDict(
    "_OptionalCreateDynamicThingGroupRequestTypeDef",
    {
        "thingGroupProperties": "ThingGroupPropertiesTypeDef",
        "indexName": str,
        "queryVersion": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDynamicThingGroupRequestTypeDef(
    _RequiredCreateDynamicThingGroupRequestTypeDef, _OptionalCreateDynamicThingGroupRequestTypeDef
):
    pass


CreateDynamicThingGroupResponseResponseTypeDef = TypedDict(
    "CreateDynamicThingGroupResponseResponseTypeDef",
    {
        "thingGroupName": str,
        "thingGroupArn": str,
        "thingGroupId": str,
        "indexName": str,
        "queryString": str,
        "queryVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateJobRequestTypeDef = TypedDict(
    "_RequiredCreateJobRequestTypeDef",
    {
        "jobId": str,
        "targets": List[str],
    },
)
_OptionalCreateJobRequestTypeDef = TypedDict(
    "_OptionalCreateJobRequestTypeDef",
    {
        "documentSource": str,
        "document": str,
        "description": str,
        "presignedUrlConfig": "PresignedUrlConfigTypeDef",
        "targetSelection": TargetSelectionType,
        "jobExecutionsRolloutConfig": "JobExecutionsRolloutConfigTypeDef",
        "abortConfig": "AbortConfigTypeDef",
        "timeoutConfig": "TimeoutConfigTypeDef",
        "tags": List["TagTypeDef"],
        "namespaceId": str,
        "jobTemplateArn": str,
    },
    total=False,
)


class CreateJobRequestTypeDef(_RequiredCreateJobRequestTypeDef, _OptionalCreateJobRequestTypeDef):
    pass


CreateJobResponseResponseTypeDef = TypedDict(
    "CreateJobResponseResponseTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateJobTemplateRequestTypeDef = TypedDict(
    "_RequiredCreateJobTemplateRequestTypeDef",
    {
        "jobTemplateId": str,
        "description": str,
    },
)
_OptionalCreateJobTemplateRequestTypeDef = TypedDict(
    "_OptionalCreateJobTemplateRequestTypeDef",
    {
        "jobArn": str,
        "documentSource": str,
        "document": str,
        "presignedUrlConfig": "PresignedUrlConfigTypeDef",
        "jobExecutionsRolloutConfig": "JobExecutionsRolloutConfigTypeDef",
        "abortConfig": "AbortConfigTypeDef",
        "timeoutConfig": "TimeoutConfigTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateJobTemplateRequestTypeDef(
    _RequiredCreateJobTemplateRequestTypeDef, _OptionalCreateJobTemplateRequestTypeDef
):
    pass


CreateJobTemplateResponseResponseTypeDef = TypedDict(
    "CreateJobTemplateResponseResponseTypeDef",
    {
        "jobTemplateArn": str,
        "jobTemplateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateKeysAndCertificateRequestTypeDef = TypedDict(
    "CreateKeysAndCertificateRequestTypeDef",
    {
        "setAsActive": bool,
    },
    total=False,
)

CreateKeysAndCertificateResponseResponseTypeDef = TypedDict(
    "CreateKeysAndCertificateResponseResponseTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "certificatePem": str,
        "keyPair": "KeyPairTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMitigationActionRequestTypeDef = TypedDict(
    "_RequiredCreateMitigationActionRequestTypeDef",
    {
        "actionName": str,
        "roleArn": str,
        "actionParams": "MitigationActionParamsTypeDef",
    },
)
_OptionalCreateMitigationActionRequestTypeDef = TypedDict(
    "_OptionalCreateMitigationActionRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateMitigationActionRequestTypeDef(
    _RequiredCreateMitigationActionRequestTypeDef, _OptionalCreateMitigationActionRequestTypeDef
):
    pass


CreateMitigationActionResponseResponseTypeDef = TypedDict(
    "CreateMitigationActionResponseResponseTypeDef",
    {
        "actionArn": str,
        "actionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateOTAUpdateRequestTypeDef = TypedDict(
    "_RequiredCreateOTAUpdateRequestTypeDef",
    {
        "otaUpdateId": str,
        "targets": List[str],
        "files": List["OTAUpdateFileTypeDef"],
        "roleArn": str,
    },
)
_OptionalCreateOTAUpdateRequestTypeDef = TypedDict(
    "_OptionalCreateOTAUpdateRequestTypeDef",
    {
        "description": str,
        "protocols": List[ProtocolType],
        "targetSelection": TargetSelectionType,
        "awsJobExecutionsRolloutConfig": "AwsJobExecutionsRolloutConfigTypeDef",
        "awsJobPresignedUrlConfig": "AwsJobPresignedUrlConfigTypeDef",
        "awsJobAbortConfig": "AwsJobAbortConfigTypeDef",
        "awsJobTimeoutConfig": "AwsJobTimeoutConfigTypeDef",
        "additionalParameters": Dict[str, str],
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateOTAUpdateRequestTypeDef(
    _RequiredCreateOTAUpdateRequestTypeDef, _OptionalCreateOTAUpdateRequestTypeDef
):
    pass


CreateOTAUpdateResponseResponseTypeDef = TypedDict(
    "CreateOTAUpdateResponseResponseTypeDef",
    {
        "otaUpdateId": str,
        "awsIotJobId": str,
        "otaUpdateArn": str,
        "awsIotJobArn": str,
        "otaUpdateStatus": OTAUpdateStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePolicyRequestTypeDef = TypedDict(
    "_RequiredCreatePolicyRequestTypeDef",
    {
        "policyName": str,
        "policyDocument": str,
    },
)
_OptionalCreatePolicyRequestTypeDef = TypedDict(
    "_OptionalCreatePolicyRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreatePolicyRequestTypeDef(
    _RequiredCreatePolicyRequestTypeDef, _OptionalCreatePolicyRequestTypeDef
):
    pass


CreatePolicyResponseResponseTypeDef = TypedDict(
    "CreatePolicyResponseResponseTypeDef",
    {
        "policyName": str,
        "policyArn": str,
        "policyDocument": str,
        "policyVersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePolicyVersionRequestTypeDef = TypedDict(
    "_RequiredCreatePolicyVersionRequestTypeDef",
    {
        "policyName": str,
        "policyDocument": str,
    },
)
_OptionalCreatePolicyVersionRequestTypeDef = TypedDict(
    "_OptionalCreatePolicyVersionRequestTypeDef",
    {
        "setAsDefault": bool,
    },
    total=False,
)


class CreatePolicyVersionRequestTypeDef(
    _RequiredCreatePolicyVersionRequestTypeDef, _OptionalCreatePolicyVersionRequestTypeDef
):
    pass


CreatePolicyVersionResponseResponseTypeDef = TypedDict(
    "CreatePolicyVersionResponseResponseTypeDef",
    {
        "policyArn": str,
        "policyDocument": str,
        "policyVersionId": str,
        "isDefaultVersion": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProvisioningClaimRequestTypeDef = TypedDict(
    "CreateProvisioningClaimRequestTypeDef",
    {
        "templateName": str,
    },
)

CreateProvisioningClaimResponseResponseTypeDef = TypedDict(
    "CreateProvisioningClaimResponseResponseTypeDef",
    {
        "certificateId": str,
        "certificatePem": str,
        "keyPair": "KeyPairTypeDef",
        "expiration": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProvisioningTemplateRequestTypeDef = TypedDict(
    "_RequiredCreateProvisioningTemplateRequestTypeDef",
    {
        "templateName": str,
        "templateBody": str,
        "provisioningRoleArn": str,
    },
)
_OptionalCreateProvisioningTemplateRequestTypeDef = TypedDict(
    "_OptionalCreateProvisioningTemplateRequestTypeDef",
    {
        "description": str,
        "enabled": bool,
        "preProvisioningHook": "ProvisioningHookTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateProvisioningTemplateRequestTypeDef(
    _RequiredCreateProvisioningTemplateRequestTypeDef,
    _OptionalCreateProvisioningTemplateRequestTypeDef,
):
    pass


CreateProvisioningTemplateResponseResponseTypeDef = TypedDict(
    "CreateProvisioningTemplateResponseResponseTypeDef",
    {
        "templateArn": str,
        "templateName": str,
        "defaultVersionId": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProvisioningTemplateVersionRequestTypeDef = TypedDict(
    "_RequiredCreateProvisioningTemplateVersionRequestTypeDef",
    {
        "templateName": str,
        "templateBody": str,
    },
)
_OptionalCreateProvisioningTemplateVersionRequestTypeDef = TypedDict(
    "_OptionalCreateProvisioningTemplateVersionRequestTypeDef",
    {
        "setAsDefault": bool,
    },
    total=False,
)


class CreateProvisioningTemplateVersionRequestTypeDef(
    _RequiredCreateProvisioningTemplateVersionRequestTypeDef,
    _OptionalCreateProvisioningTemplateVersionRequestTypeDef,
):
    pass


CreateProvisioningTemplateVersionResponseResponseTypeDef = TypedDict(
    "CreateProvisioningTemplateVersionResponseResponseTypeDef",
    {
        "templateArn": str,
        "templateName": str,
        "versionId": int,
        "isDefaultVersion": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRoleAliasRequestTypeDef = TypedDict(
    "_RequiredCreateRoleAliasRequestTypeDef",
    {
        "roleAlias": str,
        "roleArn": str,
    },
)
_OptionalCreateRoleAliasRequestTypeDef = TypedDict(
    "_OptionalCreateRoleAliasRequestTypeDef",
    {
        "credentialDurationSeconds": int,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateRoleAliasRequestTypeDef(
    _RequiredCreateRoleAliasRequestTypeDef, _OptionalCreateRoleAliasRequestTypeDef
):
    pass


CreateRoleAliasResponseResponseTypeDef = TypedDict(
    "CreateRoleAliasResponseResponseTypeDef",
    {
        "roleAlias": str,
        "roleAliasArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateScheduledAuditRequestTypeDef = TypedDict(
    "_RequiredCreateScheduledAuditRequestTypeDef",
    {
        "frequency": AuditFrequencyType,
        "targetCheckNames": List[str],
        "scheduledAuditName": str,
    },
)
_OptionalCreateScheduledAuditRequestTypeDef = TypedDict(
    "_OptionalCreateScheduledAuditRequestTypeDef",
    {
        "dayOfMonth": str,
        "dayOfWeek": DayOfWeekType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateScheduledAuditRequestTypeDef(
    _RequiredCreateScheduledAuditRequestTypeDef, _OptionalCreateScheduledAuditRequestTypeDef
):
    pass


CreateScheduledAuditResponseResponseTypeDef = TypedDict(
    "CreateScheduledAuditResponseResponseTypeDef",
    {
        "scheduledAuditArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSecurityProfileRequestTypeDef = TypedDict(
    "_RequiredCreateSecurityProfileRequestTypeDef",
    {
        "securityProfileName": str,
    },
)
_OptionalCreateSecurityProfileRequestTypeDef = TypedDict(
    "_OptionalCreateSecurityProfileRequestTypeDef",
    {
        "securityProfileDescription": str,
        "behaviors": List["BehaviorTypeDef"],
        "alertTargets": Dict[Literal["SNS"], "AlertTargetTypeDef"],
        "additionalMetricsToRetain": List[str],
        "additionalMetricsToRetainV2": List["MetricToRetainTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateSecurityProfileRequestTypeDef(
    _RequiredCreateSecurityProfileRequestTypeDef, _OptionalCreateSecurityProfileRequestTypeDef
):
    pass


CreateSecurityProfileResponseResponseTypeDef = TypedDict(
    "CreateSecurityProfileResponseResponseTypeDef",
    {
        "securityProfileName": str,
        "securityProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStreamRequestTypeDef = TypedDict(
    "_RequiredCreateStreamRequestTypeDef",
    {
        "streamId": str,
        "files": List["StreamFileTypeDef"],
        "roleArn": str,
    },
)
_OptionalCreateStreamRequestTypeDef = TypedDict(
    "_OptionalCreateStreamRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateStreamRequestTypeDef(
    _RequiredCreateStreamRequestTypeDef, _OptionalCreateStreamRequestTypeDef
):
    pass


CreateStreamResponseResponseTypeDef = TypedDict(
    "CreateStreamResponseResponseTypeDef",
    {
        "streamId": str,
        "streamArn": str,
        "description": str,
        "streamVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateThingGroupRequestTypeDef = TypedDict(
    "_RequiredCreateThingGroupRequestTypeDef",
    {
        "thingGroupName": str,
    },
)
_OptionalCreateThingGroupRequestTypeDef = TypedDict(
    "_OptionalCreateThingGroupRequestTypeDef",
    {
        "parentGroupName": str,
        "thingGroupProperties": "ThingGroupPropertiesTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateThingGroupRequestTypeDef(
    _RequiredCreateThingGroupRequestTypeDef, _OptionalCreateThingGroupRequestTypeDef
):
    pass


CreateThingGroupResponseResponseTypeDef = TypedDict(
    "CreateThingGroupResponseResponseTypeDef",
    {
        "thingGroupName": str,
        "thingGroupArn": str,
        "thingGroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateThingRequestTypeDef = TypedDict(
    "_RequiredCreateThingRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalCreateThingRequestTypeDef = TypedDict(
    "_OptionalCreateThingRequestTypeDef",
    {
        "thingTypeName": str,
        "attributePayload": "AttributePayloadTypeDef",
        "billingGroupName": str,
    },
    total=False,
)


class CreateThingRequestTypeDef(
    _RequiredCreateThingRequestTypeDef, _OptionalCreateThingRequestTypeDef
):
    pass


CreateThingResponseResponseTypeDef = TypedDict(
    "CreateThingResponseResponseTypeDef",
    {
        "thingName": str,
        "thingArn": str,
        "thingId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateThingTypeRequestTypeDef = TypedDict(
    "_RequiredCreateThingTypeRequestTypeDef",
    {
        "thingTypeName": str,
    },
)
_OptionalCreateThingTypeRequestTypeDef = TypedDict(
    "_OptionalCreateThingTypeRequestTypeDef",
    {
        "thingTypeProperties": "ThingTypePropertiesTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateThingTypeRequestTypeDef(
    _RequiredCreateThingTypeRequestTypeDef, _OptionalCreateThingTypeRequestTypeDef
):
    pass


CreateThingTypeResponseResponseTypeDef = TypedDict(
    "CreateThingTypeResponseResponseTypeDef",
    {
        "thingTypeName": str,
        "thingTypeArn": str,
        "thingTypeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTopicRuleDestinationRequestTypeDef = TypedDict(
    "CreateTopicRuleDestinationRequestTypeDef",
    {
        "destinationConfiguration": "TopicRuleDestinationConfigurationTypeDef",
    },
)

CreateTopicRuleDestinationResponseResponseTypeDef = TypedDict(
    "CreateTopicRuleDestinationResponseResponseTypeDef",
    {
        "topicRuleDestination": "TopicRuleDestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTopicRuleRequestTypeDef = TypedDict(
    "_RequiredCreateTopicRuleRequestTypeDef",
    {
        "ruleName": str,
        "topicRulePayload": "TopicRulePayloadTypeDef",
    },
)
_OptionalCreateTopicRuleRequestTypeDef = TypedDict(
    "_OptionalCreateTopicRuleRequestTypeDef",
    {
        "tags": str,
    },
    total=False,
)


class CreateTopicRuleRequestTypeDef(
    _RequiredCreateTopicRuleRequestTypeDef, _OptionalCreateTopicRuleRequestTypeDef
):
    pass


CustomCodeSigningTypeDef = TypedDict(
    "CustomCodeSigningTypeDef",
    {
        "signature": "CodeSigningSignatureTypeDef",
        "certificateChain": "CodeSigningCertificateChainTypeDef",
        "hashAlgorithm": str,
        "signatureAlgorithm": str,
    },
    total=False,
)

DeleteAccountAuditConfigurationRequestTypeDef = TypedDict(
    "DeleteAccountAuditConfigurationRequestTypeDef",
    {
        "deleteScheduledAudits": bool,
    },
    total=False,
)

DeleteAuditSuppressionRequestTypeDef = TypedDict(
    "DeleteAuditSuppressionRequestTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
    },
)

DeleteAuthorizerRequestTypeDef = TypedDict(
    "DeleteAuthorizerRequestTypeDef",
    {
        "authorizerName": str,
    },
)

_RequiredDeleteBillingGroupRequestTypeDef = TypedDict(
    "_RequiredDeleteBillingGroupRequestTypeDef",
    {
        "billingGroupName": str,
    },
)
_OptionalDeleteBillingGroupRequestTypeDef = TypedDict(
    "_OptionalDeleteBillingGroupRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)


class DeleteBillingGroupRequestTypeDef(
    _RequiredDeleteBillingGroupRequestTypeDef, _OptionalDeleteBillingGroupRequestTypeDef
):
    pass


DeleteCACertificateRequestTypeDef = TypedDict(
    "DeleteCACertificateRequestTypeDef",
    {
        "certificateId": str,
    },
)

_RequiredDeleteCertificateRequestTypeDef = TypedDict(
    "_RequiredDeleteCertificateRequestTypeDef",
    {
        "certificateId": str,
    },
)
_OptionalDeleteCertificateRequestTypeDef = TypedDict(
    "_OptionalDeleteCertificateRequestTypeDef",
    {
        "forceDelete": bool,
    },
    total=False,
)


class DeleteCertificateRequestTypeDef(
    _RequiredDeleteCertificateRequestTypeDef, _OptionalDeleteCertificateRequestTypeDef
):
    pass


DeleteCustomMetricRequestTypeDef = TypedDict(
    "DeleteCustomMetricRequestTypeDef",
    {
        "metricName": str,
    },
)

DeleteDimensionRequestTypeDef = TypedDict(
    "DeleteDimensionRequestTypeDef",
    {
        "name": str,
    },
)

DeleteDomainConfigurationRequestTypeDef = TypedDict(
    "DeleteDomainConfigurationRequestTypeDef",
    {
        "domainConfigurationName": str,
    },
)

_RequiredDeleteDynamicThingGroupRequestTypeDef = TypedDict(
    "_RequiredDeleteDynamicThingGroupRequestTypeDef",
    {
        "thingGroupName": str,
    },
)
_OptionalDeleteDynamicThingGroupRequestTypeDef = TypedDict(
    "_OptionalDeleteDynamicThingGroupRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)


class DeleteDynamicThingGroupRequestTypeDef(
    _RequiredDeleteDynamicThingGroupRequestTypeDef, _OptionalDeleteDynamicThingGroupRequestTypeDef
):
    pass


_RequiredDeleteJobExecutionRequestTypeDef = TypedDict(
    "_RequiredDeleteJobExecutionRequestTypeDef",
    {
        "jobId": str,
        "thingName": str,
        "executionNumber": int,
    },
)
_OptionalDeleteJobExecutionRequestTypeDef = TypedDict(
    "_OptionalDeleteJobExecutionRequestTypeDef",
    {
        "force": bool,
        "namespaceId": str,
    },
    total=False,
)


class DeleteJobExecutionRequestTypeDef(
    _RequiredDeleteJobExecutionRequestTypeDef, _OptionalDeleteJobExecutionRequestTypeDef
):
    pass


_RequiredDeleteJobRequestTypeDef = TypedDict(
    "_RequiredDeleteJobRequestTypeDef",
    {
        "jobId": str,
    },
)
_OptionalDeleteJobRequestTypeDef = TypedDict(
    "_OptionalDeleteJobRequestTypeDef",
    {
        "force": bool,
        "namespaceId": str,
    },
    total=False,
)


class DeleteJobRequestTypeDef(_RequiredDeleteJobRequestTypeDef, _OptionalDeleteJobRequestTypeDef):
    pass


DeleteJobTemplateRequestTypeDef = TypedDict(
    "DeleteJobTemplateRequestTypeDef",
    {
        "jobTemplateId": str,
    },
)

DeleteMitigationActionRequestTypeDef = TypedDict(
    "DeleteMitigationActionRequestTypeDef",
    {
        "actionName": str,
    },
)

_RequiredDeleteOTAUpdateRequestTypeDef = TypedDict(
    "_RequiredDeleteOTAUpdateRequestTypeDef",
    {
        "otaUpdateId": str,
    },
)
_OptionalDeleteOTAUpdateRequestTypeDef = TypedDict(
    "_OptionalDeleteOTAUpdateRequestTypeDef",
    {
        "deleteStream": bool,
        "forceDeleteAWSJob": bool,
    },
    total=False,
)


class DeleteOTAUpdateRequestTypeDef(
    _RequiredDeleteOTAUpdateRequestTypeDef, _OptionalDeleteOTAUpdateRequestTypeDef
):
    pass


DeletePolicyRequestTypeDef = TypedDict(
    "DeletePolicyRequestTypeDef",
    {
        "policyName": str,
    },
)

DeletePolicyVersionRequestTypeDef = TypedDict(
    "DeletePolicyVersionRequestTypeDef",
    {
        "policyName": str,
        "policyVersionId": str,
    },
)

DeleteProvisioningTemplateRequestTypeDef = TypedDict(
    "DeleteProvisioningTemplateRequestTypeDef",
    {
        "templateName": str,
    },
)

DeleteProvisioningTemplateVersionRequestTypeDef = TypedDict(
    "DeleteProvisioningTemplateVersionRequestTypeDef",
    {
        "templateName": str,
        "versionId": int,
    },
)

DeleteRoleAliasRequestTypeDef = TypedDict(
    "DeleteRoleAliasRequestTypeDef",
    {
        "roleAlias": str,
    },
)

DeleteScheduledAuditRequestTypeDef = TypedDict(
    "DeleteScheduledAuditRequestTypeDef",
    {
        "scheduledAuditName": str,
    },
)

_RequiredDeleteSecurityProfileRequestTypeDef = TypedDict(
    "_RequiredDeleteSecurityProfileRequestTypeDef",
    {
        "securityProfileName": str,
    },
)
_OptionalDeleteSecurityProfileRequestTypeDef = TypedDict(
    "_OptionalDeleteSecurityProfileRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)


class DeleteSecurityProfileRequestTypeDef(
    _RequiredDeleteSecurityProfileRequestTypeDef, _OptionalDeleteSecurityProfileRequestTypeDef
):
    pass


DeleteStreamRequestTypeDef = TypedDict(
    "DeleteStreamRequestTypeDef",
    {
        "streamId": str,
    },
)

_RequiredDeleteThingGroupRequestTypeDef = TypedDict(
    "_RequiredDeleteThingGroupRequestTypeDef",
    {
        "thingGroupName": str,
    },
)
_OptionalDeleteThingGroupRequestTypeDef = TypedDict(
    "_OptionalDeleteThingGroupRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)


class DeleteThingGroupRequestTypeDef(
    _RequiredDeleteThingGroupRequestTypeDef, _OptionalDeleteThingGroupRequestTypeDef
):
    pass


_RequiredDeleteThingRequestTypeDef = TypedDict(
    "_RequiredDeleteThingRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalDeleteThingRequestTypeDef = TypedDict(
    "_OptionalDeleteThingRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)


class DeleteThingRequestTypeDef(
    _RequiredDeleteThingRequestTypeDef, _OptionalDeleteThingRequestTypeDef
):
    pass


DeleteThingTypeRequestTypeDef = TypedDict(
    "DeleteThingTypeRequestTypeDef",
    {
        "thingTypeName": str,
    },
)

DeleteTopicRuleDestinationRequestTypeDef = TypedDict(
    "DeleteTopicRuleDestinationRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteTopicRuleRequestTypeDef = TypedDict(
    "DeleteTopicRuleRequestTypeDef",
    {
        "ruleName": str,
    },
)

DeleteV2LoggingLevelRequestTypeDef = TypedDict(
    "DeleteV2LoggingLevelRequestTypeDef",
    {
        "targetType": LogTargetTypeType,
        "targetName": str,
    },
)

DeniedTypeDef = TypedDict(
    "DeniedTypeDef",
    {
        "implicitDeny": "ImplicitDenyTypeDef",
        "explicitDeny": "ExplicitDenyTypeDef",
    },
    total=False,
)

_RequiredDeprecateThingTypeRequestTypeDef = TypedDict(
    "_RequiredDeprecateThingTypeRequestTypeDef",
    {
        "thingTypeName": str,
    },
)
_OptionalDeprecateThingTypeRequestTypeDef = TypedDict(
    "_OptionalDeprecateThingTypeRequestTypeDef",
    {
        "undoDeprecate": bool,
    },
    total=False,
)


class DeprecateThingTypeRequestTypeDef(
    _RequiredDeprecateThingTypeRequestTypeDef, _OptionalDeprecateThingTypeRequestTypeDef
):
    pass


DescribeAccountAuditConfigurationResponseResponseTypeDef = TypedDict(
    "DescribeAccountAuditConfigurationResponseResponseTypeDef",
    {
        "roleArn": str,
        "auditNotificationTargetConfigurations": Dict[
            Literal["SNS"], "AuditNotificationTargetTypeDef"
        ],
        "auditCheckConfigurations": Dict[str, "AuditCheckConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAuditFindingRequestTypeDef = TypedDict(
    "DescribeAuditFindingRequestTypeDef",
    {
        "findingId": str,
    },
)

DescribeAuditFindingResponseResponseTypeDef = TypedDict(
    "DescribeAuditFindingResponseResponseTypeDef",
    {
        "finding": "AuditFindingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAuditMitigationActionsTaskRequestTypeDef = TypedDict(
    "DescribeAuditMitigationActionsTaskRequestTypeDef",
    {
        "taskId": str,
    },
)

DescribeAuditMitigationActionsTaskResponseResponseTypeDef = TypedDict(
    "DescribeAuditMitigationActionsTaskResponseResponseTypeDef",
    {
        "taskStatus": AuditMitigationActionsTaskStatusType,
        "startTime": datetime,
        "endTime": datetime,
        "taskStatistics": Dict[str, "TaskStatisticsForAuditCheckTypeDef"],
        "target": "AuditMitigationActionsTaskTargetTypeDef",
        "auditCheckToActionsMapping": Dict[str, List[str]],
        "actionsDefinition": List["MitigationActionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAuditSuppressionRequestTypeDef = TypedDict(
    "DescribeAuditSuppressionRequestTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
    },
)

DescribeAuditSuppressionResponseResponseTypeDef = TypedDict(
    "DescribeAuditSuppressionResponseResponseTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
        "expirationDate": datetime,
        "suppressIndefinitely": bool,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAuditTaskRequestTypeDef = TypedDict(
    "DescribeAuditTaskRequestTypeDef",
    {
        "taskId": str,
    },
)

DescribeAuditTaskResponseResponseTypeDef = TypedDict(
    "DescribeAuditTaskResponseResponseTypeDef",
    {
        "taskStatus": AuditTaskStatusType,
        "taskType": AuditTaskTypeType,
        "taskStartTime": datetime,
        "taskStatistics": "TaskStatisticsTypeDef",
        "scheduledAuditName": str,
        "auditDetails": Dict[str, "AuditCheckDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAuthorizerRequestTypeDef = TypedDict(
    "DescribeAuthorizerRequestTypeDef",
    {
        "authorizerName": str,
    },
)

DescribeAuthorizerResponseResponseTypeDef = TypedDict(
    "DescribeAuthorizerResponseResponseTypeDef",
    {
        "authorizerDescription": "AuthorizerDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBillingGroupRequestTypeDef = TypedDict(
    "DescribeBillingGroupRequestTypeDef",
    {
        "billingGroupName": str,
    },
)

DescribeBillingGroupResponseResponseTypeDef = TypedDict(
    "DescribeBillingGroupResponseResponseTypeDef",
    {
        "billingGroupName": str,
        "billingGroupId": str,
        "billingGroupArn": str,
        "version": int,
        "billingGroupProperties": "BillingGroupPropertiesTypeDef",
        "billingGroupMetadata": "BillingGroupMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCACertificateRequestTypeDef = TypedDict(
    "DescribeCACertificateRequestTypeDef",
    {
        "certificateId": str,
    },
)

DescribeCACertificateResponseResponseTypeDef = TypedDict(
    "DescribeCACertificateResponseResponseTypeDef",
    {
        "certificateDescription": "CACertificateDescriptionTypeDef",
        "registrationConfig": "RegistrationConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCertificateRequestTypeDef = TypedDict(
    "DescribeCertificateRequestTypeDef",
    {
        "certificateId": str,
    },
)

DescribeCertificateResponseResponseTypeDef = TypedDict(
    "DescribeCertificateResponseResponseTypeDef",
    {
        "certificateDescription": "CertificateDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomMetricRequestTypeDef = TypedDict(
    "DescribeCustomMetricRequestTypeDef",
    {
        "metricName": str,
    },
)

DescribeCustomMetricResponseResponseTypeDef = TypedDict(
    "DescribeCustomMetricResponseResponseTypeDef",
    {
        "metricName": str,
        "metricArn": str,
        "metricType": CustomMetricTypeType,
        "displayName": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDefaultAuthorizerResponseResponseTypeDef = TypedDict(
    "DescribeDefaultAuthorizerResponseResponseTypeDef",
    {
        "authorizerDescription": "AuthorizerDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDetectMitigationActionsTaskRequestTypeDef = TypedDict(
    "DescribeDetectMitigationActionsTaskRequestTypeDef",
    {
        "taskId": str,
    },
)

DescribeDetectMitigationActionsTaskResponseResponseTypeDef = TypedDict(
    "DescribeDetectMitigationActionsTaskResponseResponseTypeDef",
    {
        "taskSummary": "DetectMitigationActionsTaskSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDimensionRequestTypeDef = TypedDict(
    "DescribeDimensionRequestTypeDef",
    {
        "name": str,
    },
)

DescribeDimensionResponseResponseTypeDef = TypedDict(
    "DescribeDimensionResponseResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "type": Literal["TOPIC_FILTER"],
        "stringValues": List[str],
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainConfigurationRequestTypeDef = TypedDict(
    "DescribeDomainConfigurationRequestTypeDef",
    {
        "domainConfigurationName": str,
    },
)

DescribeDomainConfigurationResponseResponseTypeDef = TypedDict(
    "DescribeDomainConfigurationResponseResponseTypeDef",
    {
        "domainConfigurationName": str,
        "domainConfigurationArn": str,
        "domainName": str,
        "serverCertificates": List["ServerCertificateSummaryTypeDef"],
        "authorizerConfig": "AuthorizerConfigTypeDef",
        "domainConfigurationStatus": DomainConfigurationStatusType,
        "serviceType": ServiceTypeType,
        "domainType": DomainTypeType,
        "lastStatusChangeDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointRequestTypeDef = TypedDict(
    "DescribeEndpointRequestTypeDef",
    {
        "endpointType": str,
    },
    total=False,
)

DescribeEndpointResponseResponseTypeDef = TypedDict(
    "DescribeEndpointResponseResponseTypeDef",
    {
        "endpointAddress": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventConfigurationsResponseResponseTypeDef = TypedDict(
    "DescribeEventConfigurationsResponseResponseTypeDef",
    {
        "eventConfigurations": Dict[EventTypeType, "ConfigurationTypeDef"],
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIndexRequestTypeDef = TypedDict(
    "DescribeIndexRequestTypeDef",
    {
        "indexName": str,
    },
)

DescribeIndexResponseResponseTypeDef = TypedDict(
    "DescribeIndexResponseResponseTypeDef",
    {
        "indexName": str,
        "indexStatus": IndexStatusType,
        "schema": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeJobExecutionRequestTypeDef = TypedDict(
    "_RequiredDescribeJobExecutionRequestTypeDef",
    {
        "jobId": str,
        "thingName": str,
    },
)
_OptionalDescribeJobExecutionRequestTypeDef = TypedDict(
    "_OptionalDescribeJobExecutionRequestTypeDef",
    {
        "executionNumber": int,
    },
    total=False,
)


class DescribeJobExecutionRequestTypeDef(
    _RequiredDescribeJobExecutionRequestTypeDef, _OptionalDescribeJobExecutionRequestTypeDef
):
    pass


DescribeJobExecutionResponseResponseTypeDef = TypedDict(
    "DescribeJobExecutionResponseResponseTypeDef",
    {
        "execution": "JobExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobRequestTypeDef = TypedDict(
    "DescribeJobRequestTypeDef",
    {
        "jobId": str,
    },
)

DescribeJobResponseResponseTypeDef = TypedDict(
    "DescribeJobResponseResponseTypeDef",
    {
        "documentSource": str,
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobTemplateRequestTypeDef = TypedDict(
    "DescribeJobTemplateRequestTypeDef",
    {
        "jobTemplateId": str,
    },
)

DescribeJobTemplateResponseResponseTypeDef = TypedDict(
    "DescribeJobTemplateResponseResponseTypeDef",
    {
        "jobTemplateArn": str,
        "jobTemplateId": str,
        "description": str,
        "documentSource": str,
        "document": str,
        "createdAt": datetime,
        "presignedUrlConfig": "PresignedUrlConfigTypeDef",
        "jobExecutionsRolloutConfig": "JobExecutionsRolloutConfigTypeDef",
        "abortConfig": "AbortConfigTypeDef",
        "timeoutConfig": "TimeoutConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMitigationActionRequestTypeDef = TypedDict(
    "DescribeMitigationActionRequestTypeDef",
    {
        "actionName": str,
    },
)

DescribeMitigationActionResponseResponseTypeDef = TypedDict(
    "DescribeMitigationActionResponseResponseTypeDef",
    {
        "actionName": str,
        "actionType": MitigationActionTypeType,
        "actionArn": str,
        "actionId": str,
        "roleArn": str,
        "actionParams": "MitigationActionParamsTypeDef",
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProvisioningTemplateRequestTypeDef = TypedDict(
    "DescribeProvisioningTemplateRequestTypeDef",
    {
        "templateName": str,
    },
)

DescribeProvisioningTemplateResponseResponseTypeDef = TypedDict(
    "DescribeProvisioningTemplateResponseResponseTypeDef",
    {
        "templateArn": str,
        "templateName": str,
        "description": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "defaultVersionId": int,
        "templateBody": str,
        "enabled": bool,
        "provisioningRoleArn": str,
        "preProvisioningHook": "ProvisioningHookTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProvisioningTemplateVersionRequestTypeDef = TypedDict(
    "DescribeProvisioningTemplateVersionRequestTypeDef",
    {
        "templateName": str,
        "versionId": int,
    },
)

DescribeProvisioningTemplateVersionResponseResponseTypeDef = TypedDict(
    "DescribeProvisioningTemplateVersionResponseResponseTypeDef",
    {
        "versionId": int,
        "creationDate": datetime,
        "templateBody": str,
        "isDefaultVersion": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRoleAliasRequestTypeDef = TypedDict(
    "DescribeRoleAliasRequestTypeDef",
    {
        "roleAlias": str,
    },
)

DescribeRoleAliasResponseResponseTypeDef = TypedDict(
    "DescribeRoleAliasResponseResponseTypeDef",
    {
        "roleAliasDescription": "RoleAliasDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScheduledAuditRequestTypeDef = TypedDict(
    "DescribeScheduledAuditRequestTypeDef",
    {
        "scheduledAuditName": str,
    },
)

DescribeScheduledAuditResponseResponseTypeDef = TypedDict(
    "DescribeScheduledAuditResponseResponseTypeDef",
    {
        "frequency": AuditFrequencyType,
        "dayOfMonth": str,
        "dayOfWeek": DayOfWeekType,
        "targetCheckNames": List[str],
        "scheduledAuditName": str,
        "scheduledAuditArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityProfileRequestTypeDef = TypedDict(
    "DescribeSecurityProfileRequestTypeDef",
    {
        "securityProfileName": str,
    },
)

DescribeSecurityProfileResponseResponseTypeDef = TypedDict(
    "DescribeSecurityProfileResponseResponseTypeDef",
    {
        "securityProfileName": str,
        "securityProfileArn": str,
        "securityProfileDescription": str,
        "behaviors": List["BehaviorTypeDef"],
        "alertTargets": Dict[Literal["SNS"], "AlertTargetTypeDef"],
        "additionalMetricsToRetain": List[str],
        "additionalMetricsToRetainV2": List["MetricToRetainTypeDef"],
        "version": int,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStreamRequestTypeDef = TypedDict(
    "DescribeStreamRequestTypeDef",
    {
        "streamId": str,
    },
)

DescribeStreamResponseResponseTypeDef = TypedDict(
    "DescribeStreamResponseResponseTypeDef",
    {
        "streamInfo": "StreamInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThingGroupRequestTypeDef = TypedDict(
    "DescribeThingGroupRequestTypeDef",
    {
        "thingGroupName": str,
    },
)

DescribeThingGroupResponseResponseTypeDef = TypedDict(
    "DescribeThingGroupResponseResponseTypeDef",
    {
        "thingGroupName": str,
        "thingGroupId": str,
        "thingGroupArn": str,
        "version": int,
        "thingGroupProperties": "ThingGroupPropertiesTypeDef",
        "thingGroupMetadata": "ThingGroupMetadataTypeDef",
        "indexName": str,
        "queryString": str,
        "queryVersion": str,
        "status": DynamicGroupStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThingRegistrationTaskRequestTypeDef = TypedDict(
    "DescribeThingRegistrationTaskRequestTypeDef",
    {
        "taskId": str,
    },
)

DescribeThingRegistrationTaskResponseResponseTypeDef = TypedDict(
    "DescribeThingRegistrationTaskResponseResponseTypeDef",
    {
        "taskId": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "templateBody": str,
        "inputFileBucket": str,
        "inputFileKey": str,
        "roleArn": str,
        "status": StatusType,
        "message": str,
        "successCount": int,
        "failureCount": int,
        "percentageProgress": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThingRequestTypeDef = TypedDict(
    "DescribeThingRequestTypeDef",
    {
        "thingName": str,
    },
)

DescribeThingResponseResponseTypeDef = TypedDict(
    "DescribeThingResponseResponseTypeDef",
    {
        "defaultClientId": str,
        "thingName": str,
        "thingId": str,
        "thingArn": str,
        "thingTypeName": str,
        "attributes": Dict[str, str],
        "version": int,
        "billingGroupName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThingTypeRequestTypeDef = TypedDict(
    "DescribeThingTypeRequestTypeDef",
    {
        "thingTypeName": str,
    },
)

DescribeThingTypeResponseResponseTypeDef = TypedDict(
    "DescribeThingTypeResponseResponseTypeDef",
    {
        "thingTypeName": str,
        "thingTypeId": str,
        "thingTypeArn": str,
        "thingTypeProperties": "ThingTypePropertiesTypeDef",
        "thingTypeMetadata": "ThingTypeMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "s3Destination": "S3DestinationTypeDef",
    },
    total=False,
)

DetachPolicyRequestTypeDef = TypedDict(
    "DetachPolicyRequestTypeDef",
    {
        "policyName": str,
        "target": str,
    },
)

DetachPrincipalPolicyRequestTypeDef = TypedDict(
    "DetachPrincipalPolicyRequestTypeDef",
    {
        "policyName": str,
        "principal": str,
    },
)

DetachSecurityProfileRequestTypeDef = TypedDict(
    "DetachSecurityProfileRequestTypeDef",
    {
        "securityProfileName": str,
        "securityProfileTargetArn": str,
    },
)

DetachThingPrincipalRequestTypeDef = TypedDict(
    "DetachThingPrincipalRequestTypeDef",
    {
        "thingName": str,
        "principal": str,
    },
)

DetectMitigationActionExecutionTypeDef = TypedDict(
    "DetectMitigationActionExecutionTypeDef",
    {
        "taskId": str,
        "violationId": str,
        "actionName": str,
        "thingName": str,
        "executionStartDate": datetime,
        "executionEndDate": datetime,
        "status": DetectMitigationActionExecutionStatusType,
        "errorCode": str,
        "message": str,
    },
    total=False,
)

DetectMitigationActionsTaskStatisticsTypeDef = TypedDict(
    "DetectMitigationActionsTaskStatisticsTypeDef",
    {
        "actionsExecuted": int,
        "actionsSkipped": int,
        "actionsFailed": int,
    },
    total=False,
)

DetectMitigationActionsTaskSummaryTypeDef = TypedDict(
    "DetectMitigationActionsTaskSummaryTypeDef",
    {
        "taskId": str,
        "taskStatus": DetectMitigationActionsTaskStatusType,
        "taskStartTime": datetime,
        "taskEndTime": datetime,
        "target": "DetectMitigationActionsTaskTargetTypeDef",
        "violationEventOccurrenceRange": "ViolationEventOccurrenceRangeTypeDef",
        "onlyActiveViolationsIncluded": bool,
        "suppressedAlertsIncluded": bool,
        "actionsDefinition": List["MitigationActionTypeDef"],
        "taskStatistics": "DetectMitigationActionsTaskStatisticsTypeDef",
    },
    total=False,
)

DetectMitigationActionsTaskTargetTypeDef = TypedDict(
    "DetectMitigationActionsTaskTargetTypeDef",
    {
        "violationIds": List[str],
        "securityProfileName": str,
        "behaviorName": str,
    },
    total=False,
)

DisableTopicRuleRequestTypeDef = TypedDict(
    "DisableTopicRuleRequestTypeDef",
    {
        "ruleName": str,
    },
)

DomainConfigurationSummaryTypeDef = TypedDict(
    "DomainConfigurationSummaryTypeDef",
    {
        "domainConfigurationName": str,
        "domainConfigurationArn": str,
        "serviceType": ServiceTypeType,
    },
    total=False,
)

_RequiredDynamoDBActionTypeDef = TypedDict(
    "_RequiredDynamoDBActionTypeDef",
    {
        "tableName": str,
        "roleArn": str,
        "hashKeyField": str,
        "hashKeyValue": str,
    },
)
_OptionalDynamoDBActionTypeDef = TypedDict(
    "_OptionalDynamoDBActionTypeDef",
    {
        "operation": str,
        "hashKeyType": DynamoKeyTypeType,
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": DynamoKeyTypeType,
        "payloadField": str,
    },
    total=False,
)


class DynamoDBActionTypeDef(_RequiredDynamoDBActionTypeDef, _OptionalDynamoDBActionTypeDef):
    pass


DynamoDBv2ActionTypeDef = TypedDict(
    "DynamoDBv2ActionTypeDef",
    {
        "roleArn": str,
        "putItem": "PutItemInputTypeDef",
    },
)

EffectivePolicyTypeDef = TypedDict(
    "EffectivePolicyTypeDef",
    {
        "policyName": str,
        "policyArn": str,
        "policyDocument": str,
    },
    total=False,
)

ElasticsearchActionTypeDef = TypedDict(
    "ElasticsearchActionTypeDef",
    {
        "roleArn": str,
        "endpoint": str,
        "index": str,
        "type": str,
        "id": str,
    },
)

EnableIoTLoggingParamsTypeDef = TypedDict(
    "EnableIoTLoggingParamsTypeDef",
    {
        "roleArnForLogging": str,
        "logLevel": LogLevelType,
    },
)

EnableTopicRuleRequestTypeDef = TypedDict(
    "EnableTopicRuleRequestTypeDef",
    {
        "ruleName": str,
    },
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "code": str,
        "message": str,
    },
    total=False,
)

ExplicitDenyTypeDef = TypedDict(
    "ExplicitDenyTypeDef",
    {
        "policies": List["PolicyTypeDef"],
    },
    total=False,
)

ExponentialRolloutRateTypeDef = TypedDict(
    "ExponentialRolloutRateTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": "RateIncreaseCriteriaTypeDef",
    },
)

FieldTypeDef = TypedDict(
    "FieldTypeDef",
    {
        "name": str,
        "type": FieldTypeType,
    },
    total=False,
)

FileLocationTypeDef = TypedDict(
    "FileLocationTypeDef",
    {
        "stream": "StreamTypeDef",
        "s3Location": "S3LocationTypeDef",
    },
    total=False,
)

_RequiredFirehoseActionTypeDef = TypedDict(
    "_RequiredFirehoseActionTypeDef",
    {
        "roleArn": str,
        "deliveryStreamName": str,
    },
)
_OptionalFirehoseActionTypeDef = TypedDict(
    "_OptionalFirehoseActionTypeDef",
    {
        "separator": str,
        "batchMode": bool,
    },
    total=False,
)


class FirehoseActionTypeDef(_RequiredFirehoseActionTypeDef, _OptionalFirehoseActionTypeDef):
    pass


GetBehaviorModelTrainingSummariesRequestTypeDef = TypedDict(
    "GetBehaviorModelTrainingSummariesRequestTypeDef",
    {
        "securityProfileName": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

GetBehaviorModelTrainingSummariesResponseResponseTypeDef = TypedDict(
    "GetBehaviorModelTrainingSummariesResponseResponseTypeDef",
    {
        "summaries": List["BehaviorModelTrainingSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCardinalityRequestTypeDef = TypedDict(
    "_RequiredGetCardinalityRequestTypeDef",
    {
        "queryString": str,
    },
)
_OptionalGetCardinalityRequestTypeDef = TypedDict(
    "_OptionalGetCardinalityRequestTypeDef",
    {
        "indexName": str,
        "aggregationField": str,
        "queryVersion": str,
    },
    total=False,
)


class GetCardinalityRequestTypeDef(
    _RequiredGetCardinalityRequestTypeDef, _OptionalGetCardinalityRequestTypeDef
):
    pass


GetCardinalityResponseResponseTypeDef = TypedDict(
    "GetCardinalityResponseResponseTypeDef",
    {
        "cardinality": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEffectivePoliciesRequestTypeDef = TypedDict(
    "GetEffectivePoliciesRequestTypeDef",
    {
        "principal": str,
        "cognitoIdentityPoolId": str,
        "thingName": str,
    },
    total=False,
)

GetEffectivePoliciesResponseResponseTypeDef = TypedDict(
    "GetEffectivePoliciesResponseResponseTypeDef",
    {
        "effectivePolicies": List["EffectivePolicyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIndexingConfigurationResponseResponseTypeDef = TypedDict(
    "GetIndexingConfigurationResponseResponseTypeDef",
    {
        "thingIndexingConfiguration": "ThingIndexingConfigurationTypeDef",
        "thingGroupIndexingConfiguration": "ThingGroupIndexingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobDocumentRequestTypeDef = TypedDict(
    "GetJobDocumentRequestTypeDef",
    {
        "jobId": str,
    },
)

GetJobDocumentResponseResponseTypeDef = TypedDict(
    "GetJobDocumentResponseResponseTypeDef",
    {
        "document": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoggingOptionsResponseResponseTypeDef = TypedDict(
    "GetLoggingOptionsResponseResponseTypeDef",
    {
        "roleArn": str,
        "logLevel": LogLevelType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOTAUpdateRequestTypeDef = TypedDict(
    "GetOTAUpdateRequestTypeDef",
    {
        "otaUpdateId": str,
    },
)

GetOTAUpdateResponseResponseTypeDef = TypedDict(
    "GetOTAUpdateResponseResponseTypeDef",
    {
        "otaUpdateInfo": "OTAUpdateInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPercentilesRequestTypeDef = TypedDict(
    "_RequiredGetPercentilesRequestTypeDef",
    {
        "queryString": str,
    },
)
_OptionalGetPercentilesRequestTypeDef = TypedDict(
    "_OptionalGetPercentilesRequestTypeDef",
    {
        "indexName": str,
        "aggregationField": str,
        "queryVersion": str,
        "percents": List[float],
    },
    total=False,
)


class GetPercentilesRequestTypeDef(
    _RequiredGetPercentilesRequestTypeDef, _OptionalGetPercentilesRequestTypeDef
):
    pass


GetPercentilesResponseResponseTypeDef = TypedDict(
    "GetPercentilesResponseResponseTypeDef",
    {
        "percentiles": List["PercentPairTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyRequestTypeDef = TypedDict(
    "GetPolicyRequestTypeDef",
    {
        "policyName": str,
    },
)

GetPolicyResponseResponseTypeDef = TypedDict(
    "GetPolicyResponseResponseTypeDef",
    {
        "policyName": str,
        "policyArn": str,
        "policyDocument": str,
        "defaultVersionId": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "generationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyVersionRequestTypeDef = TypedDict(
    "GetPolicyVersionRequestTypeDef",
    {
        "policyName": str,
        "policyVersionId": str,
    },
)

GetPolicyVersionResponseResponseTypeDef = TypedDict(
    "GetPolicyVersionResponseResponseTypeDef",
    {
        "policyArn": str,
        "policyName": str,
        "policyDocument": str,
        "policyVersionId": str,
        "isDefaultVersion": bool,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "generationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegistrationCodeResponseResponseTypeDef = TypedDict(
    "GetRegistrationCodeResponseResponseTypeDef",
    {
        "registrationCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetStatisticsRequestTypeDef = TypedDict(
    "_RequiredGetStatisticsRequestTypeDef",
    {
        "queryString": str,
    },
)
_OptionalGetStatisticsRequestTypeDef = TypedDict(
    "_OptionalGetStatisticsRequestTypeDef",
    {
        "indexName": str,
        "aggregationField": str,
        "queryVersion": str,
    },
    total=False,
)


class GetStatisticsRequestTypeDef(
    _RequiredGetStatisticsRequestTypeDef, _OptionalGetStatisticsRequestTypeDef
):
    pass


GetStatisticsResponseResponseTypeDef = TypedDict(
    "GetStatisticsResponseResponseTypeDef",
    {
        "statistics": "StatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTopicRuleDestinationRequestTypeDef = TypedDict(
    "GetTopicRuleDestinationRequestTypeDef",
    {
        "arn": str,
    },
)

GetTopicRuleDestinationResponseResponseTypeDef = TypedDict(
    "GetTopicRuleDestinationResponseResponseTypeDef",
    {
        "topicRuleDestination": "TopicRuleDestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTopicRuleRequestTypeDef = TypedDict(
    "GetTopicRuleRequestTypeDef",
    {
        "ruleName": str,
    },
)

GetTopicRuleResponseResponseTypeDef = TypedDict(
    "GetTopicRuleResponseResponseTypeDef",
    {
        "ruleArn": str,
        "rule": "TopicRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetV2LoggingOptionsResponseResponseTypeDef = TypedDict(
    "GetV2LoggingOptionsResponseResponseTypeDef",
    {
        "roleArn": str,
        "defaultLogLevel": LogLevelType,
        "disableAllLogs": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupNameAndArnTypeDef = TypedDict(
    "GroupNameAndArnTypeDef",
    {
        "groupName": str,
        "groupArn": str,
    },
    total=False,
)

HttpActionHeaderTypeDef = TypedDict(
    "HttpActionHeaderTypeDef",
    {
        "key": str,
        "value": str,
    },
)

_RequiredHttpActionTypeDef = TypedDict(
    "_RequiredHttpActionTypeDef",
    {
        "url": str,
    },
)
_OptionalHttpActionTypeDef = TypedDict(
    "_OptionalHttpActionTypeDef",
    {
        "confirmationUrl": str,
        "headers": List["HttpActionHeaderTypeDef"],
        "auth": "HttpAuthorizationTypeDef",
    },
    total=False,
)


class HttpActionTypeDef(_RequiredHttpActionTypeDef, _OptionalHttpActionTypeDef):
    pass


HttpAuthorizationTypeDef = TypedDict(
    "HttpAuthorizationTypeDef",
    {
        "sigv4": "SigV4AuthorizationTypeDef",
    },
    total=False,
)

HttpContextTypeDef = TypedDict(
    "HttpContextTypeDef",
    {
        "headers": Dict[str, str],
        "queryString": str,
    },
    total=False,
)

HttpUrlDestinationConfigurationTypeDef = TypedDict(
    "HttpUrlDestinationConfigurationTypeDef",
    {
        "confirmationUrl": str,
    },
)

HttpUrlDestinationPropertiesTypeDef = TypedDict(
    "HttpUrlDestinationPropertiesTypeDef",
    {
        "confirmationUrl": str,
    },
    total=False,
)

HttpUrlDestinationSummaryTypeDef = TypedDict(
    "HttpUrlDestinationSummaryTypeDef",
    {
        "confirmationUrl": str,
    },
    total=False,
)

ImplicitDenyTypeDef = TypedDict(
    "ImplicitDenyTypeDef",
    {
        "policies": List["PolicyTypeDef"],
    },
    total=False,
)

IotAnalyticsActionTypeDef = TypedDict(
    "IotAnalyticsActionTypeDef",
    {
        "channelArn": str,
        "channelName": str,
        "batchMode": bool,
        "roleArn": str,
    },
    total=False,
)

_RequiredIotEventsActionTypeDef = TypedDict(
    "_RequiredIotEventsActionTypeDef",
    {
        "inputName": str,
        "roleArn": str,
    },
)
_OptionalIotEventsActionTypeDef = TypedDict(
    "_OptionalIotEventsActionTypeDef",
    {
        "messageId": str,
        "batchMode": bool,
    },
    total=False,
)


class IotEventsActionTypeDef(_RequiredIotEventsActionTypeDef, _OptionalIotEventsActionTypeDef):
    pass


IotSiteWiseActionTypeDef = TypedDict(
    "IotSiteWiseActionTypeDef",
    {
        "putAssetPropertyValueEntries": List["PutAssetPropertyValueEntryTypeDef"],
        "roleArn": str,
    },
)

JobExecutionStatusDetailsTypeDef = TypedDict(
    "JobExecutionStatusDetailsTypeDef",
    {
        "detailsMap": Dict[str, str],
    },
    total=False,
)

JobExecutionSummaryForJobTypeDef = TypedDict(
    "JobExecutionSummaryForJobTypeDef",
    {
        "thingArn": str,
        "jobExecutionSummary": "JobExecutionSummaryTypeDef",
    },
    total=False,
)

JobExecutionSummaryForThingTypeDef = TypedDict(
    "JobExecutionSummaryForThingTypeDef",
    {
        "jobId": str,
        "jobExecutionSummary": "JobExecutionSummaryTypeDef",
    },
    total=False,
)

JobExecutionSummaryTypeDef = TypedDict(
    "JobExecutionSummaryTypeDef",
    {
        "status": JobExecutionStatusType,
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
    },
    total=False,
)

JobExecutionTypeDef = TypedDict(
    "JobExecutionTypeDef",
    {
        "jobId": str,
        "status": JobExecutionStatusType,
        "forceCanceled": bool,
        "statusDetails": "JobExecutionStatusDetailsTypeDef",
        "thingArn": str,
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
        "versionNumber": int,
        "approximateSecondsBeforeTimedOut": int,
    },
    total=False,
)

JobExecutionsRolloutConfigTypeDef = TypedDict(
    "JobExecutionsRolloutConfigTypeDef",
    {
        "maximumPerMinute": int,
        "exponentialRate": "ExponentialRolloutRateTypeDef",
    },
    total=False,
)

JobProcessDetailsTypeDef = TypedDict(
    "JobProcessDetailsTypeDef",
    {
        "processingTargets": List[str],
        "numberOfCanceledThings": int,
        "numberOfSucceededThings": int,
        "numberOfFailedThings": int,
        "numberOfRejectedThings": int,
        "numberOfQueuedThings": int,
        "numberOfInProgressThings": int,
        "numberOfRemovedThings": int,
        "numberOfTimedOutThings": int,
    },
    total=False,
)

JobSummaryTypeDef = TypedDict(
    "JobSummaryTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "thingGroupId": str,
        "targetSelection": TargetSelectionType,
        "status": JobStatusType,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "completedAt": datetime,
    },
    total=False,
)

JobTemplateSummaryTypeDef = TypedDict(
    "JobTemplateSummaryTypeDef",
    {
        "jobTemplateArn": str,
        "jobTemplateId": str,
        "description": str,
        "createdAt": datetime,
    },
    total=False,
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "targetSelection": TargetSelectionType,
        "status": JobStatusType,
        "forceCanceled": bool,
        "reasonCode": str,
        "comment": str,
        "targets": List[str],
        "description": str,
        "presignedUrlConfig": "PresignedUrlConfigTypeDef",
        "jobExecutionsRolloutConfig": "JobExecutionsRolloutConfigTypeDef",
        "abortConfig": "AbortConfigTypeDef",
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "completedAt": datetime,
        "jobProcessDetails": "JobProcessDetailsTypeDef",
        "timeoutConfig": "TimeoutConfigTypeDef",
        "namespaceId": str,
        "jobTemplateArn": str,
    },
    total=False,
)

_RequiredKafkaActionTypeDef = TypedDict(
    "_RequiredKafkaActionTypeDef",
    {
        "destinationArn": str,
        "topic": str,
        "clientProperties": Dict[str, str],
    },
)
_OptionalKafkaActionTypeDef = TypedDict(
    "_OptionalKafkaActionTypeDef",
    {
        "key": str,
        "partition": str,
    },
    total=False,
)


class KafkaActionTypeDef(_RequiredKafkaActionTypeDef, _OptionalKafkaActionTypeDef):
    pass


KeyPairTypeDef = TypedDict(
    "KeyPairTypeDef",
    {
        "PublicKey": str,
        "PrivateKey": str,
    },
    total=False,
)

_RequiredKinesisActionTypeDef = TypedDict(
    "_RequiredKinesisActionTypeDef",
    {
        "roleArn": str,
        "streamName": str,
    },
)
_OptionalKinesisActionTypeDef = TypedDict(
    "_OptionalKinesisActionTypeDef",
    {
        "partitionKey": str,
    },
    total=False,
)


class KinesisActionTypeDef(_RequiredKinesisActionTypeDef, _OptionalKinesisActionTypeDef):
    pass


LambdaActionTypeDef = TypedDict(
    "LambdaActionTypeDef",
    {
        "functionArn": str,
    },
)

ListActiveViolationsRequestTypeDef = TypedDict(
    "ListActiveViolationsRequestTypeDef",
    {
        "thingName": str,
        "securityProfileName": str,
        "behaviorCriteriaType": BehaviorCriteriaTypeType,
        "listSuppressedAlerts": bool,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListActiveViolationsResponseResponseTypeDef = TypedDict(
    "ListActiveViolationsResponseResponseTypeDef",
    {
        "activeViolations": List["ActiveViolationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAttachedPoliciesRequestTypeDef = TypedDict(
    "_RequiredListAttachedPoliciesRequestTypeDef",
    {
        "target": str,
    },
)
_OptionalListAttachedPoliciesRequestTypeDef = TypedDict(
    "_OptionalListAttachedPoliciesRequestTypeDef",
    {
        "recursive": bool,
        "marker": str,
        "pageSize": int,
    },
    total=False,
)


class ListAttachedPoliciesRequestTypeDef(
    _RequiredListAttachedPoliciesRequestTypeDef, _OptionalListAttachedPoliciesRequestTypeDef
):
    pass


ListAttachedPoliciesResponseResponseTypeDef = TypedDict(
    "ListAttachedPoliciesResponseResponseTypeDef",
    {
        "policies": List["PolicyTypeDef"],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAuditFindingsRequestTypeDef = TypedDict(
    "ListAuditFindingsRequestTypeDef",
    {
        "taskId": str,
        "checkName": str,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
        "maxResults": int,
        "nextToken": str,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "listSuppressedFindings": bool,
    },
    total=False,
)

ListAuditFindingsResponseResponseTypeDef = TypedDict(
    "ListAuditFindingsResponseResponseTypeDef",
    {
        "findings": List["AuditFindingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAuditMitigationActionsExecutionsRequestTypeDef = TypedDict(
    "_RequiredListAuditMitigationActionsExecutionsRequestTypeDef",
    {
        "taskId": str,
        "findingId": str,
    },
)
_OptionalListAuditMitigationActionsExecutionsRequestTypeDef = TypedDict(
    "_OptionalListAuditMitigationActionsExecutionsRequestTypeDef",
    {
        "actionStatus": AuditMitigationActionsExecutionStatusType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListAuditMitigationActionsExecutionsRequestTypeDef(
    _RequiredListAuditMitigationActionsExecutionsRequestTypeDef,
    _OptionalListAuditMitigationActionsExecutionsRequestTypeDef,
):
    pass


ListAuditMitigationActionsExecutionsResponseResponseTypeDef = TypedDict(
    "ListAuditMitigationActionsExecutionsResponseResponseTypeDef",
    {
        "actionsExecutions": List["AuditMitigationActionExecutionMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAuditMitigationActionsTasksRequestTypeDef = TypedDict(
    "_RequiredListAuditMitigationActionsTasksRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalListAuditMitigationActionsTasksRequestTypeDef = TypedDict(
    "_OptionalListAuditMitigationActionsTasksRequestTypeDef",
    {
        "auditTaskId": str,
        "findingId": str,
        "taskStatus": AuditMitigationActionsTaskStatusType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListAuditMitigationActionsTasksRequestTypeDef(
    _RequiredListAuditMitigationActionsTasksRequestTypeDef,
    _OptionalListAuditMitigationActionsTasksRequestTypeDef,
):
    pass


ListAuditMitigationActionsTasksResponseResponseTypeDef = TypedDict(
    "ListAuditMitigationActionsTasksResponseResponseTypeDef",
    {
        "tasks": List["AuditMitigationActionsTaskMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAuditSuppressionsRequestTypeDef = TypedDict(
    "ListAuditSuppressionsRequestTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
        "ascendingOrder": bool,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAuditSuppressionsResponseResponseTypeDef = TypedDict(
    "ListAuditSuppressionsResponseResponseTypeDef",
    {
        "suppressions": List["AuditSuppressionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAuditTasksRequestTypeDef = TypedDict(
    "_RequiredListAuditTasksRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalListAuditTasksRequestTypeDef = TypedDict(
    "_OptionalListAuditTasksRequestTypeDef",
    {
        "taskType": AuditTaskTypeType,
        "taskStatus": AuditTaskStatusType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListAuditTasksRequestTypeDef(
    _RequiredListAuditTasksRequestTypeDef, _OptionalListAuditTasksRequestTypeDef
):
    pass


ListAuditTasksResponseResponseTypeDef = TypedDict(
    "ListAuditTasksResponseResponseTypeDef",
    {
        "tasks": List["AuditTaskMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAuthorizersRequestTypeDef = TypedDict(
    "ListAuthorizersRequestTypeDef",
    {
        "pageSize": int,
        "marker": str,
        "ascendingOrder": bool,
        "status": AuthorizerStatusType,
    },
    total=False,
)

ListAuthorizersResponseResponseTypeDef = TypedDict(
    "ListAuthorizersResponseResponseTypeDef",
    {
        "authorizers": List["AuthorizerSummaryTypeDef"],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBillingGroupsRequestTypeDef = TypedDict(
    "ListBillingGroupsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "namePrefixFilter": str,
    },
    total=False,
)

ListBillingGroupsResponseResponseTypeDef = TypedDict(
    "ListBillingGroupsResponseResponseTypeDef",
    {
        "billingGroups": List["GroupNameAndArnTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCACertificatesRequestTypeDef = TypedDict(
    "ListCACertificatesRequestTypeDef",
    {
        "pageSize": int,
        "marker": str,
        "ascendingOrder": bool,
    },
    total=False,
)

ListCACertificatesResponseResponseTypeDef = TypedDict(
    "ListCACertificatesResponseResponseTypeDef",
    {
        "certificates": List["CACertificateTypeDef"],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCertificatesByCARequestTypeDef = TypedDict(
    "_RequiredListCertificatesByCARequestTypeDef",
    {
        "caCertificateId": str,
    },
)
_OptionalListCertificatesByCARequestTypeDef = TypedDict(
    "_OptionalListCertificatesByCARequestTypeDef",
    {
        "pageSize": int,
        "marker": str,
        "ascendingOrder": bool,
    },
    total=False,
)


class ListCertificatesByCARequestTypeDef(
    _RequiredListCertificatesByCARequestTypeDef, _OptionalListCertificatesByCARequestTypeDef
):
    pass


ListCertificatesByCAResponseResponseTypeDef = TypedDict(
    "ListCertificatesByCAResponseResponseTypeDef",
    {
        "certificates": List["CertificateTypeDef"],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCertificatesRequestTypeDef = TypedDict(
    "ListCertificatesRequestTypeDef",
    {
        "pageSize": int,
        "marker": str,
        "ascendingOrder": bool,
    },
    total=False,
)

ListCertificatesResponseResponseTypeDef = TypedDict(
    "ListCertificatesResponseResponseTypeDef",
    {
        "certificates": List["CertificateTypeDef"],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomMetricsRequestTypeDef = TypedDict(
    "ListCustomMetricsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListCustomMetricsResponseResponseTypeDef = TypedDict(
    "ListCustomMetricsResponseResponseTypeDef",
    {
        "metricNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDetectMitigationActionsExecutionsRequestTypeDef = TypedDict(
    "ListDetectMitigationActionsExecutionsRequestTypeDef",
    {
        "taskId": str,
        "violationId": str,
        "thingName": str,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListDetectMitigationActionsExecutionsResponseResponseTypeDef = TypedDict(
    "ListDetectMitigationActionsExecutionsResponseResponseTypeDef",
    {
        "actionsExecutions": List["DetectMitigationActionExecutionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDetectMitigationActionsTasksRequestTypeDef = TypedDict(
    "_RequiredListDetectMitigationActionsTasksRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalListDetectMitigationActionsTasksRequestTypeDef = TypedDict(
    "_OptionalListDetectMitigationActionsTasksRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListDetectMitigationActionsTasksRequestTypeDef(
    _RequiredListDetectMitigationActionsTasksRequestTypeDef,
    _OptionalListDetectMitigationActionsTasksRequestTypeDef,
):
    pass


ListDetectMitigationActionsTasksResponseResponseTypeDef = TypedDict(
    "ListDetectMitigationActionsTasksResponseResponseTypeDef",
    {
        "tasks": List["DetectMitigationActionsTaskSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDimensionsRequestTypeDef = TypedDict(
    "ListDimensionsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDimensionsResponseResponseTypeDef = TypedDict(
    "ListDimensionsResponseResponseTypeDef",
    {
        "dimensionNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainConfigurationsRequestTypeDef = TypedDict(
    "ListDomainConfigurationsRequestTypeDef",
    {
        "marker": str,
        "pageSize": int,
        "serviceType": ServiceTypeType,
    },
    total=False,
)

ListDomainConfigurationsResponseResponseTypeDef = TypedDict(
    "ListDomainConfigurationsResponseResponseTypeDef",
    {
        "domainConfigurations": List["DomainConfigurationSummaryTypeDef"],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIndicesRequestTypeDef = TypedDict(
    "ListIndicesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListIndicesResponseResponseTypeDef = TypedDict(
    "ListIndicesResponseResponseTypeDef",
    {
        "indexNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListJobExecutionsForJobRequestTypeDef = TypedDict(
    "_RequiredListJobExecutionsForJobRequestTypeDef",
    {
        "jobId": str,
    },
)
_OptionalListJobExecutionsForJobRequestTypeDef = TypedDict(
    "_OptionalListJobExecutionsForJobRequestTypeDef",
    {
        "status": JobExecutionStatusType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListJobExecutionsForJobRequestTypeDef(
    _RequiredListJobExecutionsForJobRequestTypeDef, _OptionalListJobExecutionsForJobRequestTypeDef
):
    pass


ListJobExecutionsForJobResponseResponseTypeDef = TypedDict(
    "ListJobExecutionsForJobResponseResponseTypeDef",
    {
        "executionSummaries": List["JobExecutionSummaryForJobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListJobExecutionsForThingRequestTypeDef = TypedDict(
    "_RequiredListJobExecutionsForThingRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalListJobExecutionsForThingRequestTypeDef = TypedDict(
    "_OptionalListJobExecutionsForThingRequestTypeDef",
    {
        "status": JobExecutionStatusType,
        "namespaceId": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListJobExecutionsForThingRequestTypeDef(
    _RequiredListJobExecutionsForThingRequestTypeDef,
    _OptionalListJobExecutionsForThingRequestTypeDef,
):
    pass


ListJobExecutionsForThingResponseResponseTypeDef = TypedDict(
    "ListJobExecutionsForThingResponseResponseTypeDef",
    {
        "executionSummaries": List["JobExecutionSummaryForThingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobTemplatesRequestTypeDef = TypedDict(
    "ListJobTemplatesRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListJobTemplatesResponseResponseTypeDef = TypedDict(
    "ListJobTemplatesResponseResponseTypeDef",
    {
        "jobTemplates": List["JobTemplateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsRequestTypeDef = TypedDict(
    "ListJobsRequestTypeDef",
    {
        "status": JobStatusType,
        "targetSelection": TargetSelectionType,
        "maxResults": int,
        "nextToken": str,
        "thingGroupName": str,
        "thingGroupId": str,
        "namespaceId": str,
    },
    total=False,
)

ListJobsResponseResponseTypeDef = TypedDict(
    "ListJobsResponseResponseTypeDef",
    {
        "jobs": List["JobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMitigationActionsRequestTypeDef = TypedDict(
    "ListMitigationActionsRequestTypeDef",
    {
        "actionType": MitigationActionTypeType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListMitigationActionsResponseResponseTypeDef = TypedDict(
    "ListMitigationActionsResponseResponseTypeDef",
    {
        "actionIdentifiers": List["MitigationActionIdentifierTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOTAUpdatesRequestTypeDef = TypedDict(
    "ListOTAUpdatesRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "otaUpdateStatus": OTAUpdateStatusType,
    },
    total=False,
)

ListOTAUpdatesResponseResponseTypeDef = TypedDict(
    "ListOTAUpdatesResponseResponseTypeDef",
    {
        "otaUpdates": List["OTAUpdateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOutgoingCertificatesRequestTypeDef = TypedDict(
    "ListOutgoingCertificatesRequestTypeDef",
    {
        "pageSize": int,
        "marker": str,
        "ascendingOrder": bool,
    },
    total=False,
)

ListOutgoingCertificatesResponseResponseTypeDef = TypedDict(
    "ListOutgoingCertificatesResponseResponseTypeDef",
    {
        "outgoingCertificates": List["OutgoingCertificateTypeDef"],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPoliciesRequestTypeDef = TypedDict(
    "ListPoliciesRequestTypeDef",
    {
        "marker": str,
        "pageSize": int,
        "ascendingOrder": bool,
    },
    total=False,
)

ListPoliciesResponseResponseTypeDef = TypedDict(
    "ListPoliciesResponseResponseTypeDef",
    {
        "policies": List["PolicyTypeDef"],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPolicyPrincipalsRequestTypeDef = TypedDict(
    "_RequiredListPolicyPrincipalsRequestTypeDef",
    {
        "policyName": str,
    },
)
_OptionalListPolicyPrincipalsRequestTypeDef = TypedDict(
    "_OptionalListPolicyPrincipalsRequestTypeDef",
    {
        "marker": str,
        "pageSize": int,
        "ascendingOrder": bool,
    },
    total=False,
)


class ListPolicyPrincipalsRequestTypeDef(
    _RequiredListPolicyPrincipalsRequestTypeDef, _OptionalListPolicyPrincipalsRequestTypeDef
):
    pass


ListPolicyPrincipalsResponseResponseTypeDef = TypedDict(
    "ListPolicyPrincipalsResponseResponseTypeDef",
    {
        "principals": List[str],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPolicyVersionsRequestTypeDef = TypedDict(
    "ListPolicyVersionsRequestTypeDef",
    {
        "policyName": str,
    },
)

ListPolicyVersionsResponseResponseTypeDef = TypedDict(
    "ListPolicyVersionsResponseResponseTypeDef",
    {
        "policyVersions": List["PolicyVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPrincipalPoliciesRequestTypeDef = TypedDict(
    "_RequiredListPrincipalPoliciesRequestTypeDef",
    {
        "principal": str,
    },
)
_OptionalListPrincipalPoliciesRequestTypeDef = TypedDict(
    "_OptionalListPrincipalPoliciesRequestTypeDef",
    {
        "marker": str,
        "pageSize": int,
        "ascendingOrder": bool,
    },
    total=False,
)


class ListPrincipalPoliciesRequestTypeDef(
    _RequiredListPrincipalPoliciesRequestTypeDef, _OptionalListPrincipalPoliciesRequestTypeDef
):
    pass


ListPrincipalPoliciesResponseResponseTypeDef = TypedDict(
    "ListPrincipalPoliciesResponseResponseTypeDef",
    {
        "policies": List["PolicyTypeDef"],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPrincipalThingsRequestTypeDef = TypedDict(
    "_RequiredListPrincipalThingsRequestTypeDef",
    {
        "principal": str,
    },
)
_OptionalListPrincipalThingsRequestTypeDef = TypedDict(
    "_OptionalListPrincipalThingsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListPrincipalThingsRequestTypeDef(
    _RequiredListPrincipalThingsRequestTypeDef, _OptionalListPrincipalThingsRequestTypeDef
):
    pass


ListPrincipalThingsResponseResponseTypeDef = TypedDict(
    "ListPrincipalThingsResponseResponseTypeDef",
    {
        "things": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProvisioningTemplateVersionsRequestTypeDef = TypedDict(
    "_RequiredListProvisioningTemplateVersionsRequestTypeDef",
    {
        "templateName": str,
    },
)
_OptionalListProvisioningTemplateVersionsRequestTypeDef = TypedDict(
    "_OptionalListProvisioningTemplateVersionsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListProvisioningTemplateVersionsRequestTypeDef(
    _RequiredListProvisioningTemplateVersionsRequestTypeDef,
    _OptionalListProvisioningTemplateVersionsRequestTypeDef,
):
    pass


ListProvisioningTemplateVersionsResponseResponseTypeDef = TypedDict(
    "ListProvisioningTemplateVersionsResponseResponseTypeDef",
    {
        "versions": List["ProvisioningTemplateVersionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProvisioningTemplatesRequestTypeDef = TypedDict(
    "ListProvisioningTemplatesRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListProvisioningTemplatesResponseResponseTypeDef = TypedDict(
    "ListProvisioningTemplatesResponseResponseTypeDef",
    {
        "templates": List["ProvisioningTemplateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRoleAliasesRequestTypeDef = TypedDict(
    "ListRoleAliasesRequestTypeDef",
    {
        "pageSize": int,
        "marker": str,
        "ascendingOrder": bool,
    },
    total=False,
)

ListRoleAliasesResponseResponseTypeDef = TypedDict(
    "ListRoleAliasesResponseResponseTypeDef",
    {
        "roleAliases": List[str],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListScheduledAuditsRequestTypeDef = TypedDict(
    "ListScheduledAuditsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListScheduledAuditsResponseResponseTypeDef = TypedDict(
    "ListScheduledAuditsResponseResponseTypeDef",
    {
        "scheduledAudits": List["ScheduledAuditMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSecurityProfilesForTargetRequestTypeDef = TypedDict(
    "_RequiredListSecurityProfilesForTargetRequestTypeDef",
    {
        "securityProfileTargetArn": str,
    },
)
_OptionalListSecurityProfilesForTargetRequestTypeDef = TypedDict(
    "_OptionalListSecurityProfilesForTargetRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "recursive": bool,
    },
    total=False,
)


class ListSecurityProfilesForTargetRequestTypeDef(
    _RequiredListSecurityProfilesForTargetRequestTypeDef,
    _OptionalListSecurityProfilesForTargetRequestTypeDef,
):
    pass


ListSecurityProfilesForTargetResponseResponseTypeDef = TypedDict(
    "ListSecurityProfilesForTargetResponseResponseTypeDef",
    {
        "securityProfileTargetMappings": List["SecurityProfileTargetMappingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSecurityProfilesRequestTypeDef = TypedDict(
    "ListSecurityProfilesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "dimensionName": str,
        "metricName": str,
    },
    total=False,
)

ListSecurityProfilesResponseResponseTypeDef = TypedDict(
    "ListSecurityProfilesResponseResponseTypeDef",
    {
        "securityProfileIdentifiers": List["SecurityProfileIdentifierTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamsRequestTypeDef = TypedDict(
    "ListStreamsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "ascendingOrder": bool,
    },
    total=False,
)

ListStreamsResponseResponseTypeDef = TypedDict(
    "ListStreamsResponseResponseTypeDef",
    {
        "streams": List["StreamSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListTagsForResourceRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestTypeDef",
    {
        "nextToken": str,
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
        "tags": List["TagTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTargetsForPolicyRequestTypeDef = TypedDict(
    "_RequiredListTargetsForPolicyRequestTypeDef",
    {
        "policyName": str,
    },
)
_OptionalListTargetsForPolicyRequestTypeDef = TypedDict(
    "_OptionalListTargetsForPolicyRequestTypeDef",
    {
        "marker": str,
        "pageSize": int,
    },
    total=False,
)


class ListTargetsForPolicyRequestTypeDef(
    _RequiredListTargetsForPolicyRequestTypeDef, _OptionalListTargetsForPolicyRequestTypeDef
):
    pass


ListTargetsForPolicyResponseResponseTypeDef = TypedDict(
    "ListTargetsForPolicyResponseResponseTypeDef",
    {
        "targets": List[str],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTargetsForSecurityProfileRequestTypeDef = TypedDict(
    "_RequiredListTargetsForSecurityProfileRequestTypeDef",
    {
        "securityProfileName": str,
    },
)
_OptionalListTargetsForSecurityProfileRequestTypeDef = TypedDict(
    "_OptionalListTargetsForSecurityProfileRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListTargetsForSecurityProfileRequestTypeDef(
    _RequiredListTargetsForSecurityProfileRequestTypeDef,
    _OptionalListTargetsForSecurityProfileRequestTypeDef,
):
    pass


ListTargetsForSecurityProfileResponseResponseTypeDef = TypedDict(
    "ListTargetsForSecurityProfileResponseResponseTypeDef",
    {
        "securityProfileTargets": List["SecurityProfileTargetTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThingGroupsForThingRequestTypeDef = TypedDict(
    "_RequiredListThingGroupsForThingRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalListThingGroupsForThingRequestTypeDef = TypedDict(
    "_OptionalListThingGroupsForThingRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListThingGroupsForThingRequestTypeDef(
    _RequiredListThingGroupsForThingRequestTypeDef, _OptionalListThingGroupsForThingRequestTypeDef
):
    pass


ListThingGroupsForThingResponseResponseTypeDef = TypedDict(
    "ListThingGroupsForThingResponseResponseTypeDef",
    {
        "thingGroups": List["GroupNameAndArnTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThingGroupsRequestTypeDef = TypedDict(
    "ListThingGroupsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "parentGroup": str,
        "namePrefixFilter": str,
        "recursive": bool,
    },
    total=False,
)

ListThingGroupsResponseResponseTypeDef = TypedDict(
    "ListThingGroupsResponseResponseTypeDef",
    {
        "thingGroups": List["GroupNameAndArnTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThingPrincipalsRequestTypeDef = TypedDict(
    "_RequiredListThingPrincipalsRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalListThingPrincipalsRequestTypeDef = TypedDict(
    "_OptionalListThingPrincipalsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListThingPrincipalsRequestTypeDef(
    _RequiredListThingPrincipalsRequestTypeDef, _OptionalListThingPrincipalsRequestTypeDef
):
    pass


ListThingPrincipalsResponseResponseTypeDef = TypedDict(
    "ListThingPrincipalsResponseResponseTypeDef",
    {
        "principals": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThingRegistrationTaskReportsRequestTypeDef = TypedDict(
    "_RequiredListThingRegistrationTaskReportsRequestTypeDef",
    {
        "taskId": str,
        "reportType": ReportTypeType,
    },
)
_OptionalListThingRegistrationTaskReportsRequestTypeDef = TypedDict(
    "_OptionalListThingRegistrationTaskReportsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListThingRegistrationTaskReportsRequestTypeDef(
    _RequiredListThingRegistrationTaskReportsRequestTypeDef,
    _OptionalListThingRegistrationTaskReportsRequestTypeDef,
):
    pass


ListThingRegistrationTaskReportsResponseResponseTypeDef = TypedDict(
    "ListThingRegistrationTaskReportsResponseResponseTypeDef",
    {
        "resourceLinks": List[str],
        "reportType": ReportTypeType,
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThingRegistrationTasksRequestTypeDef = TypedDict(
    "ListThingRegistrationTasksRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "status": StatusType,
    },
    total=False,
)

ListThingRegistrationTasksResponseResponseTypeDef = TypedDict(
    "ListThingRegistrationTasksResponseResponseTypeDef",
    {
        "taskIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThingTypesRequestTypeDef = TypedDict(
    "ListThingTypesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "thingTypeName": str,
    },
    total=False,
)

ListThingTypesResponseResponseTypeDef = TypedDict(
    "ListThingTypesResponseResponseTypeDef",
    {
        "thingTypes": List["ThingTypeDefinitionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThingsInBillingGroupRequestTypeDef = TypedDict(
    "_RequiredListThingsInBillingGroupRequestTypeDef",
    {
        "billingGroupName": str,
    },
)
_OptionalListThingsInBillingGroupRequestTypeDef = TypedDict(
    "_OptionalListThingsInBillingGroupRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListThingsInBillingGroupRequestTypeDef(
    _RequiredListThingsInBillingGroupRequestTypeDef, _OptionalListThingsInBillingGroupRequestTypeDef
):
    pass


ListThingsInBillingGroupResponseResponseTypeDef = TypedDict(
    "ListThingsInBillingGroupResponseResponseTypeDef",
    {
        "things": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThingsInThingGroupRequestTypeDef = TypedDict(
    "_RequiredListThingsInThingGroupRequestTypeDef",
    {
        "thingGroupName": str,
    },
)
_OptionalListThingsInThingGroupRequestTypeDef = TypedDict(
    "_OptionalListThingsInThingGroupRequestTypeDef",
    {
        "recursive": bool,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListThingsInThingGroupRequestTypeDef(
    _RequiredListThingsInThingGroupRequestTypeDef, _OptionalListThingsInThingGroupRequestTypeDef
):
    pass


ListThingsInThingGroupResponseResponseTypeDef = TypedDict(
    "ListThingsInThingGroupResponseResponseTypeDef",
    {
        "things": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThingsRequestTypeDef = TypedDict(
    "ListThingsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "attributeName": str,
        "attributeValue": str,
        "thingTypeName": str,
        "usePrefixAttributeValue": bool,
    },
    total=False,
)

ListThingsResponseResponseTypeDef = TypedDict(
    "ListThingsResponseResponseTypeDef",
    {
        "things": List["ThingAttributeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTopicRuleDestinationsRequestTypeDef = TypedDict(
    "ListTopicRuleDestinationsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListTopicRuleDestinationsResponseResponseTypeDef = TypedDict(
    "ListTopicRuleDestinationsResponseResponseTypeDef",
    {
        "destinationSummaries": List["TopicRuleDestinationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTopicRulesRequestTypeDef = TypedDict(
    "ListTopicRulesRequestTypeDef",
    {
        "topic": str,
        "maxResults": int,
        "nextToken": str,
        "ruleDisabled": bool,
    },
    total=False,
)

ListTopicRulesResponseResponseTypeDef = TypedDict(
    "ListTopicRulesResponseResponseTypeDef",
    {
        "rules": List["TopicRuleListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListV2LoggingLevelsRequestTypeDef = TypedDict(
    "ListV2LoggingLevelsRequestTypeDef",
    {
        "targetType": LogTargetTypeType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListV2LoggingLevelsResponseResponseTypeDef = TypedDict(
    "ListV2LoggingLevelsResponseResponseTypeDef",
    {
        "logTargetConfigurations": List["LogTargetConfigurationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListViolationEventsRequestTypeDef = TypedDict(
    "_RequiredListViolationEventsRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalListViolationEventsRequestTypeDef = TypedDict(
    "_OptionalListViolationEventsRequestTypeDef",
    {
        "thingName": str,
        "securityProfileName": str,
        "behaviorCriteriaType": BehaviorCriteriaTypeType,
        "listSuppressedAlerts": bool,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListViolationEventsRequestTypeDef(
    _RequiredListViolationEventsRequestTypeDef, _OptionalListViolationEventsRequestTypeDef
):
    pass


ListViolationEventsResponseResponseTypeDef = TypedDict(
    "ListViolationEventsResponseResponseTypeDef",
    {
        "violationEvents": List["ViolationEventTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogTargetConfigurationTypeDef = TypedDict(
    "LogTargetConfigurationTypeDef",
    {
        "logTarget": "LogTargetTypeDef",
        "logLevel": LogLevelType,
    },
    total=False,
)

_RequiredLogTargetTypeDef = TypedDict(
    "_RequiredLogTargetTypeDef",
    {
        "targetType": LogTargetTypeType,
    },
)
_OptionalLogTargetTypeDef = TypedDict(
    "_OptionalLogTargetTypeDef",
    {
        "targetName": str,
    },
    total=False,
)


class LogTargetTypeDef(_RequiredLogTargetTypeDef, _OptionalLogTargetTypeDef):
    pass


_RequiredLoggingOptionsPayloadTypeDef = TypedDict(
    "_RequiredLoggingOptionsPayloadTypeDef",
    {
        "roleArn": str,
    },
)
_OptionalLoggingOptionsPayloadTypeDef = TypedDict(
    "_OptionalLoggingOptionsPayloadTypeDef",
    {
        "logLevel": LogLevelType,
    },
    total=False,
)


class LoggingOptionsPayloadTypeDef(
    _RequiredLoggingOptionsPayloadTypeDef, _OptionalLoggingOptionsPayloadTypeDef
):
    pass


MachineLearningDetectionConfigTypeDef = TypedDict(
    "MachineLearningDetectionConfigTypeDef",
    {
        "confidenceLevel": ConfidenceLevelType,
    },
)

_RequiredMetricDimensionTypeDef = TypedDict(
    "_RequiredMetricDimensionTypeDef",
    {
        "dimensionName": str,
    },
)
_OptionalMetricDimensionTypeDef = TypedDict(
    "_OptionalMetricDimensionTypeDef",
    {
        "operator": DimensionValueOperatorType,
    },
    total=False,
)


class MetricDimensionTypeDef(_RequiredMetricDimensionTypeDef, _OptionalMetricDimensionTypeDef):
    pass


_RequiredMetricToRetainTypeDef = TypedDict(
    "_RequiredMetricToRetainTypeDef",
    {
        "metric": str,
    },
)
_OptionalMetricToRetainTypeDef = TypedDict(
    "_OptionalMetricToRetainTypeDef",
    {
        "metricDimension": "MetricDimensionTypeDef",
    },
    total=False,
)


class MetricToRetainTypeDef(_RequiredMetricToRetainTypeDef, _OptionalMetricToRetainTypeDef):
    pass


MetricValueTypeDef = TypedDict(
    "MetricValueTypeDef",
    {
        "count": int,
        "cidrs": List[str],
        "ports": List[int],
        "number": float,
        "numbers": List[float],
        "strings": List[str],
    },
    total=False,
)

MitigationActionIdentifierTypeDef = TypedDict(
    "MitigationActionIdentifierTypeDef",
    {
        "actionName": str,
        "actionArn": str,
        "creationDate": datetime,
    },
    total=False,
)

MitigationActionParamsTypeDef = TypedDict(
    "MitigationActionParamsTypeDef",
    {
        "updateDeviceCertificateParams": "UpdateDeviceCertificateParamsTypeDef",
        "updateCACertificateParams": "UpdateCACertificateParamsTypeDef",
        "addThingsToThingGroupParams": "AddThingsToThingGroupParamsTypeDef",
        "replaceDefaultPolicyVersionParams": "ReplaceDefaultPolicyVersionParamsTypeDef",
        "enableIoTLoggingParams": "EnableIoTLoggingParamsTypeDef",
        "publishFindingToSnsParams": "PublishFindingToSnsParamsTypeDef",
    },
    total=False,
)

MitigationActionTypeDef = TypedDict(
    "MitigationActionTypeDef",
    {
        "name": str,
        "id": str,
        "roleArn": str,
        "actionParams": "MitigationActionParamsTypeDef",
    },
    total=False,
)

MqttContextTypeDef = TypedDict(
    "MqttContextTypeDef",
    {
        "username": str,
        "password": Union[bytes, IO[bytes], StreamingBody],
        "clientId": str,
    },
    total=False,
)

NonCompliantResourceTypeDef = TypedDict(
    "NonCompliantResourceTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
        "additionalInfo": Dict[str, str],
    },
    total=False,
)

OTAUpdateFileTypeDef = TypedDict(
    "OTAUpdateFileTypeDef",
    {
        "fileName": str,
        "fileType": int,
        "fileVersion": str,
        "fileLocation": "FileLocationTypeDef",
        "codeSigning": "CodeSigningTypeDef",
        "attributes": Dict[str, str],
    },
    total=False,
)

OTAUpdateInfoTypeDef = TypedDict(
    "OTAUpdateInfoTypeDef",
    {
        "otaUpdateId": str,
        "otaUpdateArn": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "description": str,
        "targets": List[str],
        "protocols": List[ProtocolType],
        "awsJobExecutionsRolloutConfig": "AwsJobExecutionsRolloutConfigTypeDef",
        "awsJobPresignedUrlConfig": "AwsJobPresignedUrlConfigTypeDef",
        "targetSelection": TargetSelectionType,
        "otaUpdateFiles": List["OTAUpdateFileTypeDef"],
        "otaUpdateStatus": OTAUpdateStatusType,
        "awsIotJobId": str,
        "awsIotJobArn": str,
        "errorInfo": "ErrorInfoTypeDef",
        "additionalParameters": Dict[str, str],
    },
    total=False,
)

OTAUpdateSummaryTypeDef = TypedDict(
    "OTAUpdateSummaryTypeDef",
    {
        "otaUpdateId": str,
        "otaUpdateArn": str,
        "creationDate": datetime,
    },
    total=False,
)

OutgoingCertificateTypeDef = TypedDict(
    "OutgoingCertificateTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "transferredTo": str,
        "transferDate": datetime,
        "transferMessage": str,
        "creationDate": datetime,
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

PercentPairTypeDef = TypedDict(
    "PercentPairTypeDef",
    {
        "percent": float,
        "value": float,
    },
    total=False,
)

PolicyTypeDef = TypedDict(
    "PolicyTypeDef",
    {
        "policyName": str,
        "policyArn": str,
    },
    total=False,
)

PolicyVersionIdentifierTypeDef = TypedDict(
    "PolicyVersionIdentifierTypeDef",
    {
        "policyName": str,
        "policyVersionId": str,
    },
    total=False,
)

PolicyVersionTypeDef = TypedDict(
    "PolicyVersionTypeDef",
    {
        "versionId": str,
        "isDefaultVersion": bool,
        "createDate": datetime,
    },
    total=False,
)

PresignedUrlConfigTypeDef = TypedDict(
    "PresignedUrlConfigTypeDef",
    {
        "roleArn": str,
        "expiresInSec": int,
    },
    total=False,
)

_RequiredProvisioningHookTypeDef = TypedDict(
    "_RequiredProvisioningHookTypeDef",
    {
        "targetArn": str,
    },
)
_OptionalProvisioningHookTypeDef = TypedDict(
    "_OptionalProvisioningHookTypeDef",
    {
        "payloadVersion": str,
    },
    total=False,
)


class ProvisioningHookTypeDef(_RequiredProvisioningHookTypeDef, _OptionalProvisioningHookTypeDef):
    pass


ProvisioningTemplateSummaryTypeDef = TypedDict(
    "ProvisioningTemplateSummaryTypeDef",
    {
        "templateArn": str,
        "templateName": str,
        "description": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "enabled": bool,
    },
    total=False,
)

ProvisioningTemplateVersionSummaryTypeDef = TypedDict(
    "ProvisioningTemplateVersionSummaryTypeDef",
    {
        "versionId": int,
        "creationDate": datetime,
        "isDefaultVersion": bool,
    },
    total=False,
)

PublishFindingToSnsParamsTypeDef = TypedDict(
    "PublishFindingToSnsParamsTypeDef",
    {
        "topicArn": str,
    },
)

_RequiredPutAssetPropertyValueEntryTypeDef = TypedDict(
    "_RequiredPutAssetPropertyValueEntryTypeDef",
    {
        "propertyValues": List["AssetPropertyValueTypeDef"],
    },
)
_OptionalPutAssetPropertyValueEntryTypeDef = TypedDict(
    "_OptionalPutAssetPropertyValueEntryTypeDef",
    {
        "entryId": str,
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
    },
    total=False,
)


class PutAssetPropertyValueEntryTypeDef(
    _RequiredPutAssetPropertyValueEntryTypeDef, _OptionalPutAssetPropertyValueEntryTypeDef
):
    pass


PutItemInputTypeDef = TypedDict(
    "PutItemInputTypeDef",
    {
        "tableName": str,
    },
)

RateIncreaseCriteriaTypeDef = TypedDict(
    "RateIncreaseCriteriaTypeDef",
    {
        "numberOfNotifiedThings": int,
        "numberOfSucceededThings": int,
    },
    total=False,
)

_RequiredRegisterCACertificateRequestTypeDef = TypedDict(
    "_RequiredRegisterCACertificateRequestTypeDef",
    {
        "caCertificate": str,
        "verificationCertificate": str,
    },
)
_OptionalRegisterCACertificateRequestTypeDef = TypedDict(
    "_OptionalRegisterCACertificateRequestTypeDef",
    {
        "setAsActive": bool,
        "allowAutoRegistration": bool,
        "registrationConfig": "RegistrationConfigTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class RegisterCACertificateRequestTypeDef(
    _RequiredRegisterCACertificateRequestTypeDef, _OptionalRegisterCACertificateRequestTypeDef
):
    pass


RegisterCACertificateResponseResponseTypeDef = TypedDict(
    "RegisterCACertificateResponseResponseTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterCertificateRequestTypeDef = TypedDict(
    "_RequiredRegisterCertificateRequestTypeDef",
    {
        "certificatePem": str,
    },
)
_OptionalRegisterCertificateRequestTypeDef = TypedDict(
    "_OptionalRegisterCertificateRequestTypeDef",
    {
        "caCertificatePem": str,
        "setAsActive": bool,
        "status": CertificateStatusType,
    },
    total=False,
)


class RegisterCertificateRequestTypeDef(
    _RequiredRegisterCertificateRequestTypeDef, _OptionalRegisterCertificateRequestTypeDef
):
    pass


RegisterCertificateResponseResponseTypeDef = TypedDict(
    "RegisterCertificateResponseResponseTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterCertificateWithoutCARequestTypeDef = TypedDict(
    "_RequiredRegisterCertificateWithoutCARequestTypeDef",
    {
        "certificatePem": str,
    },
)
_OptionalRegisterCertificateWithoutCARequestTypeDef = TypedDict(
    "_OptionalRegisterCertificateWithoutCARequestTypeDef",
    {
        "status": CertificateStatusType,
    },
    total=False,
)


class RegisterCertificateWithoutCARequestTypeDef(
    _RequiredRegisterCertificateWithoutCARequestTypeDef,
    _OptionalRegisterCertificateWithoutCARequestTypeDef,
):
    pass


RegisterCertificateWithoutCAResponseResponseTypeDef = TypedDict(
    "RegisterCertificateWithoutCAResponseResponseTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterThingRequestTypeDef = TypedDict(
    "_RequiredRegisterThingRequestTypeDef",
    {
        "templateBody": str,
    },
)
_OptionalRegisterThingRequestTypeDef = TypedDict(
    "_OptionalRegisterThingRequestTypeDef",
    {
        "parameters": Dict[str, str],
    },
    total=False,
)


class RegisterThingRequestTypeDef(
    _RequiredRegisterThingRequestTypeDef, _OptionalRegisterThingRequestTypeDef
):
    pass


RegisterThingResponseResponseTypeDef = TypedDict(
    "RegisterThingResponseResponseTypeDef",
    {
        "certificatePem": str,
        "resourceArns": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegistrationConfigTypeDef = TypedDict(
    "RegistrationConfigTypeDef",
    {
        "templateBody": str,
        "roleArn": str,
    },
    total=False,
)

_RequiredRejectCertificateTransferRequestTypeDef = TypedDict(
    "_RequiredRejectCertificateTransferRequestTypeDef",
    {
        "certificateId": str,
    },
)
_OptionalRejectCertificateTransferRequestTypeDef = TypedDict(
    "_OptionalRejectCertificateTransferRequestTypeDef",
    {
        "rejectReason": str,
    },
    total=False,
)


class RejectCertificateTransferRequestTypeDef(
    _RequiredRejectCertificateTransferRequestTypeDef,
    _OptionalRejectCertificateTransferRequestTypeDef,
):
    pass


RelatedResourceTypeDef = TypedDict(
    "RelatedResourceTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
        "additionalInfo": Dict[str, str],
    },
    total=False,
)

RemoveThingFromBillingGroupRequestTypeDef = TypedDict(
    "RemoveThingFromBillingGroupRequestTypeDef",
    {
        "billingGroupName": str,
        "billingGroupArn": str,
        "thingName": str,
        "thingArn": str,
    },
    total=False,
)

RemoveThingFromThingGroupRequestTypeDef = TypedDict(
    "RemoveThingFromThingGroupRequestTypeDef",
    {
        "thingGroupName": str,
        "thingGroupArn": str,
        "thingName": str,
        "thingArn": str,
    },
    total=False,
)

ReplaceDefaultPolicyVersionParamsTypeDef = TypedDict(
    "ReplaceDefaultPolicyVersionParamsTypeDef",
    {
        "templateName": Literal["BLANK_POLICY"],
    },
)

ReplaceTopicRuleRequestTypeDef = TypedDict(
    "ReplaceTopicRuleRequestTypeDef",
    {
        "ruleName": str,
        "topicRulePayload": "TopicRulePayloadTypeDef",
    },
)

_RequiredRepublishActionTypeDef = TypedDict(
    "_RequiredRepublishActionTypeDef",
    {
        "roleArn": str,
        "topic": str,
    },
)
_OptionalRepublishActionTypeDef = TypedDict(
    "_OptionalRepublishActionTypeDef",
    {
        "qos": int,
    },
    total=False,
)


class RepublishActionTypeDef(_RequiredRepublishActionTypeDef, _OptionalRepublishActionTypeDef):
    pass


ResourceIdentifierTypeDef = TypedDict(
    "ResourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": "PolicyVersionIdentifierTypeDef",
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
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

RoleAliasDescriptionTypeDef = TypedDict(
    "RoleAliasDescriptionTypeDef",
    {
        "roleAlias": str,
        "roleAliasArn": str,
        "roleArn": str,
        "owner": str,
        "credentialDurationSeconds": int,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)

_RequiredS3ActionTypeDef = TypedDict(
    "_RequiredS3ActionTypeDef",
    {
        "roleArn": str,
        "bucketName": str,
        "key": str,
    },
)
_OptionalS3ActionTypeDef = TypedDict(
    "_OptionalS3ActionTypeDef",
    {
        "cannedAcl": CannedAccessControlListType,
    },
    total=False,
)


class S3ActionTypeDef(_RequiredS3ActionTypeDef, _OptionalS3ActionTypeDef):
    pass


S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "bucket": str,
        "prefix": str,
    },
    total=False,
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "version": str,
    },
    total=False,
)

SalesforceActionTypeDef = TypedDict(
    "SalesforceActionTypeDef",
    {
        "token": str,
        "url": str,
    },
)

ScheduledAuditMetadataTypeDef = TypedDict(
    "ScheduledAuditMetadataTypeDef",
    {
        "scheduledAuditName": str,
        "scheduledAuditArn": str,
        "frequency": AuditFrequencyType,
        "dayOfMonth": str,
        "dayOfWeek": DayOfWeekType,
    },
    total=False,
)

_RequiredSearchIndexRequestTypeDef = TypedDict(
    "_RequiredSearchIndexRequestTypeDef",
    {
        "queryString": str,
    },
)
_OptionalSearchIndexRequestTypeDef = TypedDict(
    "_OptionalSearchIndexRequestTypeDef",
    {
        "indexName": str,
        "nextToken": str,
        "maxResults": int,
        "queryVersion": str,
    },
    total=False,
)


class SearchIndexRequestTypeDef(
    _RequiredSearchIndexRequestTypeDef, _OptionalSearchIndexRequestTypeDef
):
    pass


SearchIndexResponseResponseTypeDef = TypedDict(
    "SearchIndexResponseResponseTypeDef",
    {
        "nextToken": str,
        "things": List["ThingDocumentTypeDef"],
        "thingGroups": List["ThingGroupDocumentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SecurityProfileIdentifierTypeDef = TypedDict(
    "SecurityProfileIdentifierTypeDef",
    {
        "name": str,
        "arn": str,
    },
)

SecurityProfileTargetMappingTypeDef = TypedDict(
    "SecurityProfileTargetMappingTypeDef",
    {
        "securityProfileIdentifier": "SecurityProfileIdentifierTypeDef",
        "target": "SecurityProfileTargetTypeDef",
    },
    total=False,
)

SecurityProfileTargetTypeDef = TypedDict(
    "SecurityProfileTargetTypeDef",
    {
        "arn": str,
    },
)

ServerCertificateSummaryTypeDef = TypedDict(
    "ServerCertificateSummaryTypeDef",
    {
        "serverCertificateArn": str,
        "serverCertificateStatus": ServerCertificateStatusType,
        "serverCertificateStatusDetail": str,
    },
    total=False,
)

SetDefaultAuthorizerRequestTypeDef = TypedDict(
    "SetDefaultAuthorizerRequestTypeDef",
    {
        "authorizerName": str,
    },
)

SetDefaultAuthorizerResponseResponseTypeDef = TypedDict(
    "SetDefaultAuthorizerResponseResponseTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetDefaultPolicyVersionRequestTypeDef = TypedDict(
    "SetDefaultPolicyVersionRequestTypeDef",
    {
        "policyName": str,
        "policyVersionId": str,
    },
)

SetLoggingOptionsRequestTypeDef = TypedDict(
    "SetLoggingOptionsRequestTypeDef",
    {
        "loggingOptionsPayload": "LoggingOptionsPayloadTypeDef",
    },
)

SetV2LoggingLevelRequestTypeDef = TypedDict(
    "SetV2LoggingLevelRequestTypeDef",
    {
        "logTarget": "LogTargetTypeDef",
        "logLevel": LogLevelType,
    },
)

SetV2LoggingOptionsRequestTypeDef = TypedDict(
    "SetV2LoggingOptionsRequestTypeDef",
    {
        "roleArn": str,
        "defaultLogLevel": LogLevelType,
        "disableAllLogs": bool,
    },
    total=False,
)

SigV4AuthorizationTypeDef = TypedDict(
    "SigV4AuthorizationTypeDef",
    {
        "signingRegion": str,
        "serviceName": str,
        "roleArn": str,
    },
)

SigningProfileParameterTypeDef = TypedDict(
    "SigningProfileParameterTypeDef",
    {
        "certificateArn": str,
        "platform": str,
        "certificatePathOnDevice": str,
    },
    total=False,
)

_RequiredSnsActionTypeDef = TypedDict(
    "_RequiredSnsActionTypeDef",
    {
        "targetArn": str,
        "roleArn": str,
    },
)
_OptionalSnsActionTypeDef = TypedDict(
    "_OptionalSnsActionTypeDef",
    {
        "messageFormat": MessageFormatType,
    },
    total=False,
)


class SnsActionTypeDef(_RequiredSnsActionTypeDef, _OptionalSnsActionTypeDef):
    pass


_RequiredSqsActionTypeDef = TypedDict(
    "_RequiredSqsActionTypeDef",
    {
        "roleArn": str,
        "queueUrl": str,
    },
)
_OptionalSqsActionTypeDef = TypedDict(
    "_OptionalSqsActionTypeDef",
    {
        "useBase64": bool,
    },
    total=False,
)


class SqsActionTypeDef(_RequiredSqsActionTypeDef, _OptionalSqsActionTypeDef):
    pass


StartAuditMitigationActionsTaskRequestTypeDef = TypedDict(
    "StartAuditMitigationActionsTaskRequestTypeDef",
    {
        "taskId": str,
        "target": "AuditMitigationActionsTaskTargetTypeDef",
        "auditCheckToActionsMapping": Dict[str, List[str]],
        "clientRequestToken": str,
    },
)

StartAuditMitigationActionsTaskResponseResponseTypeDef = TypedDict(
    "StartAuditMitigationActionsTaskResponseResponseTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartDetectMitigationActionsTaskRequestTypeDef = TypedDict(
    "_RequiredStartDetectMitigationActionsTaskRequestTypeDef",
    {
        "taskId": str,
        "target": "DetectMitigationActionsTaskTargetTypeDef",
        "actions": List[str],
        "clientRequestToken": str,
    },
)
_OptionalStartDetectMitigationActionsTaskRequestTypeDef = TypedDict(
    "_OptionalStartDetectMitigationActionsTaskRequestTypeDef",
    {
        "violationEventOccurrenceRange": "ViolationEventOccurrenceRangeTypeDef",
        "includeOnlyActiveViolations": bool,
        "includeSuppressedAlerts": bool,
    },
    total=False,
)


class StartDetectMitigationActionsTaskRequestTypeDef(
    _RequiredStartDetectMitigationActionsTaskRequestTypeDef,
    _OptionalStartDetectMitigationActionsTaskRequestTypeDef,
):
    pass


StartDetectMitigationActionsTaskResponseResponseTypeDef = TypedDict(
    "StartDetectMitigationActionsTaskResponseResponseTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartOnDemandAuditTaskRequestTypeDef = TypedDict(
    "StartOnDemandAuditTaskRequestTypeDef",
    {
        "targetCheckNames": List[str],
    },
)

StartOnDemandAuditTaskResponseResponseTypeDef = TypedDict(
    "StartOnDemandAuditTaskResponseResponseTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartSigningJobParameterTypeDef = TypedDict(
    "StartSigningJobParameterTypeDef",
    {
        "signingProfileParameter": "SigningProfileParameterTypeDef",
        "signingProfileName": str,
        "destination": "DestinationTypeDef",
    },
    total=False,
)

StartThingRegistrationTaskRequestTypeDef = TypedDict(
    "StartThingRegistrationTaskRequestTypeDef",
    {
        "templateBody": str,
        "inputFileBucket": str,
        "inputFileKey": str,
        "roleArn": str,
    },
)

StartThingRegistrationTaskResponseResponseTypeDef = TypedDict(
    "StartThingRegistrationTaskResponseResponseTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StatisticalThresholdTypeDef = TypedDict(
    "StatisticalThresholdTypeDef",
    {
        "statistic": str,
    },
    total=False,
)

StatisticsTypeDef = TypedDict(
    "StatisticsTypeDef",
    {
        "count": int,
        "average": float,
        "sum": float,
        "minimum": float,
        "maximum": float,
        "sumOfSquares": float,
        "variance": float,
        "stdDeviation": float,
    },
    total=False,
)

_RequiredStepFunctionsActionTypeDef = TypedDict(
    "_RequiredStepFunctionsActionTypeDef",
    {
        "stateMachineName": str,
        "roleArn": str,
    },
)
_OptionalStepFunctionsActionTypeDef = TypedDict(
    "_OptionalStepFunctionsActionTypeDef",
    {
        "executionNamePrefix": str,
    },
    total=False,
)


class StepFunctionsActionTypeDef(
    _RequiredStepFunctionsActionTypeDef, _OptionalStepFunctionsActionTypeDef
):
    pass


StopThingRegistrationTaskRequestTypeDef = TypedDict(
    "StopThingRegistrationTaskRequestTypeDef",
    {
        "taskId": str,
    },
)

StreamFileTypeDef = TypedDict(
    "StreamFileTypeDef",
    {
        "fileId": int,
        "s3Location": "S3LocationTypeDef",
    },
    total=False,
)

StreamInfoTypeDef = TypedDict(
    "StreamInfoTypeDef",
    {
        "streamId": str,
        "streamArn": str,
        "streamVersion": int,
        "description": str,
        "files": List["StreamFileTypeDef"],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "roleArn": str,
    },
    total=False,
)

StreamSummaryTypeDef = TypedDict(
    "StreamSummaryTypeDef",
    {
        "streamId": str,
        "streamArn": str,
        "streamVersion": int,
        "description": str,
    },
    total=False,
)

StreamTypeDef = TypedDict(
    "StreamTypeDef",
    {
        "streamId": str,
        "fileId": int,
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


TaskStatisticsForAuditCheckTypeDef = TypedDict(
    "TaskStatisticsForAuditCheckTypeDef",
    {
        "totalFindingsCount": int,
        "failedFindingsCount": int,
        "succeededFindingsCount": int,
        "skippedFindingsCount": int,
        "canceledFindingsCount": int,
    },
    total=False,
)

TaskStatisticsTypeDef = TypedDict(
    "TaskStatisticsTypeDef",
    {
        "totalChecks": int,
        "inProgressChecks": int,
        "waitingForDataCollectionChecks": int,
        "compliantChecks": int,
        "nonCompliantChecks": int,
        "failedChecks": int,
        "canceledChecks": int,
    },
    total=False,
)

_RequiredTestAuthorizationRequestTypeDef = TypedDict(
    "_RequiredTestAuthorizationRequestTypeDef",
    {
        "authInfos": List["AuthInfoTypeDef"],
    },
)
_OptionalTestAuthorizationRequestTypeDef = TypedDict(
    "_OptionalTestAuthorizationRequestTypeDef",
    {
        "principal": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyNamesToAdd": List[str],
        "policyNamesToSkip": List[str],
    },
    total=False,
)


class TestAuthorizationRequestTypeDef(
    _RequiredTestAuthorizationRequestTypeDef, _OptionalTestAuthorizationRequestTypeDef
):
    pass


TestAuthorizationResponseResponseTypeDef = TypedDict(
    "TestAuthorizationResponseResponseTypeDef",
    {
        "authResults": List["AuthResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTestInvokeAuthorizerRequestTypeDef = TypedDict(
    "_RequiredTestInvokeAuthorizerRequestTypeDef",
    {
        "authorizerName": str,
    },
)
_OptionalTestInvokeAuthorizerRequestTypeDef = TypedDict(
    "_OptionalTestInvokeAuthorizerRequestTypeDef",
    {
        "token": str,
        "tokenSignature": str,
        "httpContext": "HttpContextTypeDef",
        "mqttContext": "MqttContextTypeDef",
        "tlsContext": "TlsContextTypeDef",
    },
    total=False,
)


class TestInvokeAuthorizerRequestTypeDef(
    _RequiredTestInvokeAuthorizerRequestTypeDef, _OptionalTestInvokeAuthorizerRequestTypeDef
):
    pass


TestInvokeAuthorizerResponseResponseTypeDef = TypedDict(
    "TestInvokeAuthorizerResponseResponseTypeDef",
    {
        "isAuthenticated": bool,
        "principalId": str,
        "policyDocuments": List[str],
        "refreshAfterInSeconds": int,
        "disconnectAfterInSeconds": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ThingAttributeTypeDef = TypedDict(
    "ThingAttributeTypeDef",
    {
        "thingName": str,
        "thingTypeName": str,
        "thingArn": str,
        "attributes": Dict[str, str],
        "version": int,
    },
    total=False,
)

ThingConnectivityTypeDef = TypedDict(
    "ThingConnectivityTypeDef",
    {
        "connected": bool,
        "timestamp": int,
    },
    total=False,
)

ThingDocumentTypeDef = TypedDict(
    "ThingDocumentTypeDef",
    {
        "thingName": str,
        "thingId": str,
        "thingTypeName": str,
        "thingGroupNames": List[str],
        "attributes": Dict[str, str],
        "shadow": str,
        "connectivity": "ThingConnectivityTypeDef",
    },
    total=False,
)

ThingGroupDocumentTypeDef = TypedDict(
    "ThingGroupDocumentTypeDef",
    {
        "thingGroupName": str,
        "thingGroupId": str,
        "thingGroupDescription": str,
        "attributes": Dict[str, str],
        "parentGroupNames": List[str],
    },
    total=False,
)

_RequiredThingGroupIndexingConfigurationTypeDef = TypedDict(
    "_RequiredThingGroupIndexingConfigurationTypeDef",
    {
        "thingGroupIndexingMode": ThingGroupIndexingModeType,
    },
)
_OptionalThingGroupIndexingConfigurationTypeDef = TypedDict(
    "_OptionalThingGroupIndexingConfigurationTypeDef",
    {
        "managedFields": List["FieldTypeDef"],
        "customFields": List["FieldTypeDef"],
    },
    total=False,
)


class ThingGroupIndexingConfigurationTypeDef(
    _RequiredThingGroupIndexingConfigurationTypeDef, _OptionalThingGroupIndexingConfigurationTypeDef
):
    pass


ThingGroupMetadataTypeDef = TypedDict(
    "ThingGroupMetadataTypeDef",
    {
        "parentGroupName": str,
        "rootToParentThingGroups": List["GroupNameAndArnTypeDef"],
        "creationDate": datetime,
    },
    total=False,
)

ThingGroupPropertiesTypeDef = TypedDict(
    "ThingGroupPropertiesTypeDef",
    {
        "thingGroupDescription": str,
        "attributePayload": "AttributePayloadTypeDef",
    },
    total=False,
)

_RequiredThingIndexingConfigurationTypeDef = TypedDict(
    "_RequiredThingIndexingConfigurationTypeDef",
    {
        "thingIndexingMode": ThingIndexingModeType,
    },
)
_OptionalThingIndexingConfigurationTypeDef = TypedDict(
    "_OptionalThingIndexingConfigurationTypeDef",
    {
        "thingConnectivityIndexingMode": ThingConnectivityIndexingModeType,
        "managedFields": List["FieldTypeDef"],
        "customFields": List["FieldTypeDef"],
    },
    total=False,
)


class ThingIndexingConfigurationTypeDef(
    _RequiredThingIndexingConfigurationTypeDef, _OptionalThingIndexingConfigurationTypeDef
):
    pass


ThingTypeDefinitionTypeDef = TypedDict(
    "ThingTypeDefinitionTypeDef",
    {
        "thingTypeName": str,
        "thingTypeArn": str,
        "thingTypeProperties": "ThingTypePropertiesTypeDef",
        "thingTypeMetadata": "ThingTypeMetadataTypeDef",
    },
    total=False,
)

ThingTypeMetadataTypeDef = TypedDict(
    "ThingTypeMetadataTypeDef",
    {
        "deprecated": bool,
        "deprecationDate": datetime,
        "creationDate": datetime,
    },
    total=False,
)

ThingTypePropertiesTypeDef = TypedDict(
    "ThingTypePropertiesTypeDef",
    {
        "thingTypeDescription": str,
        "searchableAttributes": List[str],
    },
    total=False,
)

TimeoutConfigTypeDef = TypedDict(
    "TimeoutConfigTypeDef",
    {
        "inProgressTimeoutInMinutes": int,
    },
    total=False,
)

_RequiredTimestreamActionTypeDef = TypedDict(
    "_RequiredTimestreamActionTypeDef",
    {
        "roleArn": str,
        "databaseName": str,
        "tableName": str,
        "dimensions": List["TimestreamDimensionTypeDef"],
    },
)
_OptionalTimestreamActionTypeDef = TypedDict(
    "_OptionalTimestreamActionTypeDef",
    {
        "timestamp": "TimestreamTimestampTypeDef",
    },
    total=False,
)


class TimestreamActionTypeDef(_RequiredTimestreamActionTypeDef, _OptionalTimestreamActionTypeDef):
    pass


TimestreamDimensionTypeDef = TypedDict(
    "TimestreamDimensionTypeDef",
    {
        "name": str,
        "value": str,
    },
)

TimestreamTimestampTypeDef = TypedDict(
    "TimestreamTimestampTypeDef",
    {
        "value": str,
        "unit": str,
    },
)

TlsContextTypeDef = TypedDict(
    "TlsContextTypeDef",
    {
        "serverName": str,
    },
    total=False,
)

TopicRuleDestinationConfigurationTypeDef = TypedDict(
    "TopicRuleDestinationConfigurationTypeDef",
    {
        "httpUrlConfiguration": "HttpUrlDestinationConfigurationTypeDef",
        "vpcConfiguration": "VpcDestinationConfigurationTypeDef",
    },
    total=False,
)

TopicRuleDestinationSummaryTypeDef = TypedDict(
    "TopicRuleDestinationSummaryTypeDef",
    {
        "arn": str,
        "status": TopicRuleDestinationStatusType,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "statusReason": str,
        "httpUrlSummary": "HttpUrlDestinationSummaryTypeDef",
        "vpcDestinationSummary": "VpcDestinationSummaryTypeDef",
    },
    total=False,
)

TopicRuleDestinationTypeDef = TypedDict(
    "TopicRuleDestinationTypeDef",
    {
        "arn": str,
        "status": TopicRuleDestinationStatusType,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "statusReason": str,
        "httpUrlProperties": "HttpUrlDestinationPropertiesTypeDef",
        "vpcProperties": "VpcDestinationPropertiesTypeDef",
    },
    total=False,
)

TopicRuleListItemTypeDef = TypedDict(
    "TopicRuleListItemTypeDef",
    {
        "ruleArn": str,
        "ruleName": str,
        "topicPattern": str,
        "createdAt": datetime,
        "ruleDisabled": bool,
    },
    total=False,
)

_RequiredTopicRulePayloadTypeDef = TypedDict(
    "_RequiredTopicRulePayloadTypeDef",
    {
        "sql": str,
        "actions": List["ActionTypeDef"],
    },
)
_OptionalTopicRulePayloadTypeDef = TypedDict(
    "_OptionalTopicRulePayloadTypeDef",
    {
        "description": str,
        "ruleDisabled": bool,
        "awsIotSqlVersion": str,
        "errorAction": "ActionTypeDef",
    },
    total=False,
)


class TopicRulePayloadTypeDef(_RequiredTopicRulePayloadTypeDef, _OptionalTopicRulePayloadTypeDef):
    pass


TopicRuleTypeDef = TypedDict(
    "TopicRuleTypeDef",
    {
        "ruleName": str,
        "sql": str,
        "description": str,
        "createdAt": datetime,
        "actions": List["ActionTypeDef"],
        "ruleDisabled": bool,
        "awsIotSqlVersion": str,
        "errorAction": "ActionTypeDef",
    },
    total=False,
)

_RequiredTransferCertificateRequestTypeDef = TypedDict(
    "_RequiredTransferCertificateRequestTypeDef",
    {
        "certificateId": str,
        "targetAwsAccount": str,
    },
)
_OptionalTransferCertificateRequestTypeDef = TypedDict(
    "_OptionalTransferCertificateRequestTypeDef",
    {
        "transferMessage": str,
    },
    total=False,
)


class TransferCertificateRequestTypeDef(
    _RequiredTransferCertificateRequestTypeDef, _OptionalTransferCertificateRequestTypeDef
):
    pass


TransferCertificateResponseResponseTypeDef = TypedDict(
    "TransferCertificateResponseResponseTypeDef",
    {
        "transferredCertificateArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TransferDataTypeDef = TypedDict(
    "TransferDataTypeDef",
    {
        "transferMessage": str,
        "rejectReason": str,
        "transferDate": datetime,
        "acceptDate": datetime,
        "rejectDate": datetime,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateAccountAuditConfigurationRequestTypeDef = TypedDict(
    "UpdateAccountAuditConfigurationRequestTypeDef",
    {
        "roleArn": str,
        "auditNotificationTargetConfigurations": Dict[
            Literal["SNS"], "AuditNotificationTargetTypeDef"
        ],
        "auditCheckConfigurations": Dict[str, "AuditCheckConfigurationTypeDef"],
    },
    total=False,
)

_RequiredUpdateAuditSuppressionRequestTypeDef = TypedDict(
    "_RequiredUpdateAuditSuppressionRequestTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
    },
)
_OptionalUpdateAuditSuppressionRequestTypeDef = TypedDict(
    "_OptionalUpdateAuditSuppressionRequestTypeDef",
    {
        "expirationDate": Union[datetime, str],
        "suppressIndefinitely": bool,
        "description": str,
    },
    total=False,
)


class UpdateAuditSuppressionRequestTypeDef(
    _RequiredUpdateAuditSuppressionRequestTypeDef, _OptionalUpdateAuditSuppressionRequestTypeDef
):
    pass


_RequiredUpdateAuthorizerRequestTypeDef = TypedDict(
    "_RequiredUpdateAuthorizerRequestTypeDef",
    {
        "authorizerName": str,
    },
)
_OptionalUpdateAuthorizerRequestTypeDef = TypedDict(
    "_OptionalUpdateAuthorizerRequestTypeDef",
    {
        "authorizerFunctionArn": str,
        "tokenKeyName": str,
        "tokenSigningPublicKeys": Dict[str, str],
        "status": AuthorizerStatusType,
    },
    total=False,
)


class UpdateAuthorizerRequestTypeDef(
    _RequiredUpdateAuthorizerRequestTypeDef, _OptionalUpdateAuthorizerRequestTypeDef
):
    pass


UpdateAuthorizerResponseResponseTypeDef = TypedDict(
    "UpdateAuthorizerResponseResponseTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateBillingGroupRequestTypeDef = TypedDict(
    "_RequiredUpdateBillingGroupRequestTypeDef",
    {
        "billingGroupName": str,
        "billingGroupProperties": "BillingGroupPropertiesTypeDef",
    },
)
_OptionalUpdateBillingGroupRequestTypeDef = TypedDict(
    "_OptionalUpdateBillingGroupRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)


class UpdateBillingGroupRequestTypeDef(
    _RequiredUpdateBillingGroupRequestTypeDef, _OptionalUpdateBillingGroupRequestTypeDef
):
    pass


UpdateBillingGroupResponseResponseTypeDef = TypedDict(
    "UpdateBillingGroupResponseResponseTypeDef",
    {
        "version": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCACertificateParamsTypeDef = TypedDict(
    "UpdateCACertificateParamsTypeDef",
    {
        "action": Literal["DEACTIVATE"],
    },
)

_RequiredUpdateCACertificateRequestTypeDef = TypedDict(
    "_RequiredUpdateCACertificateRequestTypeDef",
    {
        "certificateId": str,
    },
)
_OptionalUpdateCACertificateRequestTypeDef = TypedDict(
    "_OptionalUpdateCACertificateRequestTypeDef",
    {
        "newStatus": CACertificateStatusType,
        "newAutoRegistrationStatus": AutoRegistrationStatusType,
        "registrationConfig": "RegistrationConfigTypeDef",
        "removeAutoRegistration": bool,
    },
    total=False,
)


class UpdateCACertificateRequestTypeDef(
    _RequiredUpdateCACertificateRequestTypeDef, _OptionalUpdateCACertificateRequestTypeDef
):
    pass


UpdateCertificateRequestTypeDef = TypedDict(
    "UpdateCertificateRequestTypeDef",
    {
        "certificateId": str,
        "newStatus": CertificateStatusType,
    },
)

UpdateCustomMetricRequestTypeDef = TypedDict(
    "UpdateCustomMetricRequestTypeDef",
    {
        "metricName": str,
        "displayName": str,
    },
)

UpdateCustomMetricResponseResponseTypeDef = TypedDict(
    "UpdateCustomMetricResponseResponseTypeDef",
    {
        "metricName": str,
        "metricArn": str,
        "metricType": CustomMetricTypeType,
        "displayName": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDeviceCertificateParamsTypeDef = TypedDict(
    "UpdateDeviceCertificateParamsTypeDef",
    {
        "action": Literal["DEACTIVATE"],
    },
)

UpdateDimensionRequestTypeDef = TypedDict(
    "UpdateDimensionRequestTypeDef",
    {
        "name": str,
        "stringValues": List[str],
    },
)

UpdateDimensionResponseResponseTypeDef = TypedDict(
    "UpdateDimensionResponseResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "type": Literal["TOPIC_FILTER"],
        "stringValues": List[str],
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDomainConfigurationRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainConfigurationRequestTypeDef",
    {
        "domainConfigurationName": str,
    },
)
_OptionalUpdateDomainConfigurationRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainConfigurationRequestTypeDef",
    {
        "authorizerConfig": "AuthorizerConfigTypeDef",
        "domainConfigurationStatus": DomainConfigurationStatusType,
        "removeAuthorizerConfig": bool,
    },
    total=False,
)


class UpdateDomainConfigurationRequestTypeDef(
    _RequiredUpdateDomainConfigurationRequestTypeDef,
    _OptionalUpdateDomainConfigurationRequestTypeDef,
):
    pass


UpdateDomainConfigurationResponseResponseTypeDef = TypedDict(
    "UpdateDomainConfigurationResponseResponseTypeDef",
    {
        "domainConfigurationName": str,
        "domainConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDynamicThingGroupRequestTypeDef = TypedDict(
    "_RequiredUpdateDynamicThingGroupRequestTypeDef",
    {
        "thingGroupName": str,
        "thingGroupProperties": "ThingGroupPropertiesTypeDef",
    },
)
_OptionalUpdateDynamicThingGroupRequestTypeDef = TypedDict(
    "_OptionalUpdateDynamicThingGroupRequestTypeDef",
    {
        "expectedVersion": int,
        "indexName": str,
        "queryString": str,
        "queryVersion": str,
    },
    total=False,
)


class UpdateDynamicThingGroupRequestTypeDef(
    _RequiredUpdateDynamicThingGroupRequestTypeDef, _OptionalUpdateDynamicThingGroupRequestTypeDef
):
    pass


UpdateDynamicThingGroupResponseResponseTypeDef = TypedDict(
    "UpdateDynamicThingGroupResponseResponseTypeDef",
    {
        "version": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEventConfigurationsRequestTypeDef = TypedDict(
    "UpdateEventConfigurationsRequestTypeDef",
    {
        "eventConfigurations": Dict[EventTypeType, "ConfigurationTypeDef"],
    },
    total=False,
)

UpdateIndexingConfigurationRequestTypeDef = TypedDict(
    "UpdateIndexingConfigurationRequestTypeDef",
    {
        "thingIndexingConfiguration": "ThingIndexingConfigurationTypeDef",
        "thingGroupIndexingConfiguration": "ThingGroupIndexingConfigurationTypeDef",
    },
    total=False,
)

_RequiredUpdateJobRequestTypeDef = TypedDict(
    "_RequiredUpdateJobRequestTypeDef",
    {
        "jobId": str,
    },
)
_OptionalUpdateJobRequestTypeDef = TypedDict(
    "_OptionalUpdateJobRequestTypeDef",
    {
        "description": str,
        "presignedUrlConfig": "PresignedUrlConfigTypeDef",
        "jobExecutionsRolloutConfig": "JobExecutionsRolloutConfigTypeDef",
        "abortConfig": "AbortConfigTypeDef",
        "timeoutConfig": "TimeoutConfigTypeDef",
        "namespaceId": str,
    },
    total=False,
)


class UpdateJobRequestTypeDef(_RequiredUpdateJobRequestTypeDef, _OptionalUpdateJobRequestTypeDef):
    pass


_RequiredUpdateMitigationActionRequestTypeDef = TypedDict(
    "_RequiredUpdateMitigationActionRequestTypeDef",
    {
        "actionName": str,
    },
)
_OptionalUpdateMitigationActionRequestTypeDef = TypedDict(
    "_OptionalUpdateMitigationActionRequestTypeDef",
    {
        "roleArn": str,
        "actionParams": "MitigationActionParamsTypeDef",
    },
    total=False,
)


class UpdateMitigationActionRequestTypeDef(
    _RequiredUpdateMitigationActionRequestTypeDef, _OptionalUpdateMitigationActionRequestTypeDef
):
    pass


UpdateMitigationActionResponseResponseTypeDef = TypedDict(
    "UpdateMitigationActionResponseResponseTypeDef",
    {
        "actionArn": str,
        "actionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProvisioningTemplateRequestTypeDef = TypedDict(
    "_RequiredUpdateProvisioningTemplateRequestTypeDef",
    {
        "templateName": str,
    },
)
_OptionalUpdateProvisioningTemplateRequestTypeDef = TypedDict(
    "_OptionalUpdateProvisioningTemplateRequestTypeDef",
    {
        "description": str,
        "enabled": bool,
        "defaultVersionId": int,
        "provisioningRoleArn": str,
        "preProvisioningHook": "ProvisioningHookTypeDef",
        "removePreProvisioningHook": bool,
    },
    total=False,
)


class UpdateProvisioningTemplateRequestTypeDef(
    _RequiredUpdateProvisioningTemplateRequestTypeDef,
    _OptionalUpdateProvisioningTemplateRequestTypeDef,
):
    pass


_RequiredUpdateRoleAliasRequestTypeDef = TypedDict(
    "_RequiredUpdateRoleAliasRequestTypeDef",
    {
        "roleAlias": str,
    },
)
_OptionalUpdateRoleAliasRequestTypeDef = TypedDict(
    "_OptionalUpdateRoleAliasRequestTypeDef",
    {
        "roleArn": str,
        "credentialDurationSeconds": int,
    },
    total=False,
)


class UpdateRoleAliasRequestTypeDef(
    _RequiredUpdateRoleAliasRequestTypeDef, _OptionalUpdateRoleAliasRequestTypeDef
):
    pass


UpdateRoleAliasResponseResponseTypeDef = TypedDict(
    "UpdateRoleAliasResponseResponseTypeDef",
    {
        "roleAlias": str,
        "roleAliasArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateScheduledAuditRequestTypeDef = TypedDict(
    "_RequiredUpdateScheduledAuditRequestTypeDef",
    {
        "scheduledAuditName": str,
    },
)
_OptionalUpdateScheduledAuditRequestTypeDef = TypedDict(
    "_OptionalUpdateScheduledAuditRequestTypeDef",
    {
        "frequency": AuditFrequencyType,
        "dayOfMonth": str,
        "dayOfWeek": DayOfWeekType,
        "targetCheckNames": List[str],
    },
    total=False,
)


class UpdateScheduledAuditRequestTypeDef(
    _RequiredUpdateScheduledAuditRequestTypeDef, _OptionalUpdateScheduledAuditRequestTypeDef
):
    pass


UpdateScheduledAuditResponseResponseTypeDef = TypedDict(
    "UpdateScheduledAuditResponseResponseTypeDef",
    {
        "scheduledAuditArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSecurityProfileRequestTypeDef = TypedDict(
    "_RequiredUpdateSecurityProfileRequestTypeDef",
    {
        "securityProfileName": str,
    },
)
_OptionalUpdateSecurityProfileRequestTypeDef = TypedDict(
    "_OptionalUpdateSecurityProfileRequestTypeDef",
    {
        "securityProfileDescription": str,
        "behaviors": List["BehaviorTypeDef"],
        "alertTargets": Dict[Literal["SNS"], "AlertTargetTypeDef"],
        "additionalMetricsToRetain": List[str],
        "additionalMetricsToRetainV2": List["MetricToRetainTypeDef"],
        "deleteBehaviors": bool,
        "deleteAlertTargets": bool,
        "deleteAdditionalMetricsToRetain": bool,
        "expectedVersion": int,
    },
    total=False,
)


class UpdateSecurityProfileRequestTypeDef(
    _RequiredUpdateSecurityProfileRequestTypeDef, _OptionalUpdateSecurityProfileRequestTypeDef
):
    pass


UpdateSecurityProfileResponseResponseTypeDef = TypedDict(
    "UpdateSecurityProfileResponseResponseTypeDef",
    {
        "securityProfileName": str,
        "securityProfileArn": str,
        "securityProfileDescription": str,
        "behaviors": List["BehaviorTypeDef"],
        "alertTargets": Dict[Literal["SNS"], "AlertTargetTypeDef"],
        "additionalMetricsToRetain": List[str],
        "additionalMetricsToRetainV2": List["MetricToRetainTypeDef"],
        "version": int,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateStreamRequestTypeDef = TypedDict(
    "_RequiredUpdateStreamRequestTypeDef",
    {
        "streamId": str,
    },
)
_OptionalUpdateStreamRequestTypeDef = TypedDict(
    "_OptionalUpdateStreamRequestTypeDef",
    {
        "description": str,
        "files": List["StreamFileTypeDef"],
        "roleArn": str,
    },
    total=False,
)


class UpdateStreamRequestTypeDef(
    _RequiredUpdateStreamRequestTypeDef, _OptionalUpdateStreamRequestTypeDef
):
    pass


UpdateStreamResponseResponseTypeDef = TypedDict(
    "UpdateStreamResponseResponseTypeDef",
    {
        "streamId": str,
        "streamArn": str,
        "description": str,
        "streamVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateThingGroupRequestTypeDef = TypedDict(
    "_RequiredUpdateThingGroupRequestTypeDef",
    {
        "thingGroupName": str,
        "thingGroupProperties": "ThingGroupPropertiesTypeDef",
    },
)
_OptionalUpdateThingGroupRequestTypeDef = TypedDict(
    "_OptionalUpdateThingGroupRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)


class UpdateThingGroupRequestTypeDef(
    _RequiredUpdateThingGroupRequestTypeDef, _OptionalUpdateThingGroupRequestTypeDef
):
    pass


UpdateThingGroupResponseResponseTypeDef = TypedDict(
    "UpdateThingGroupResponseResponseTypeDef",
    {
        "version": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateThingGroupsForThingRequestTypeDef = TypedDict(
    "UpdateThingGroupsForThingRequestTypeDef",
    {
        "thingName": str,
        "thingGroupsToAdd": List[str],
        "thingGroupsToRemove": List[str],
        "overrideDynamicGroups": bool,
    },
    total=False,
)

_RequiredUpdateThingRequestTypeDef = TypedDict(
    "_RequiredUpdateThingRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalUpdateThingRequestTypeDef = TypedDict(
    "_OptionalUpdateThingRequestTypeDef",
    {
        "thingTypeName": str,
        "attributePayload": "AttributePayloadTypeDef",
        "expectedVersion": int,
        "removeThingType": bool,
    },
    total=False,
)


class UpdateThingRequestTypeDef(
    _RequiredUpdateThingRequestTypeDef, _OptionalUpdateThingRequestTypeDef
):
    pass


UpdateTopicRuleDestinationRequestTypeDef = TypedDict(
    "UpdateTopicRuleDestinationRequestTypeDef",
    {
        "arn": str,
        "status": TopicRuleDestinationStatusType,
    },
)

ValidateSecurityProfileBehaviorsRequestTypeDef = TypedDict(
    "ValidateSecurityProfileBehaviorsRequestTypeDef",
    {
        "behaviors": List["BehaviorTypeDef"],
    },
)

ValidateSecurityProfileBehaviorsResponseResponseTypeDef = TypedDict(
    "ValidateSecurityProfileBehaviorsResponseResponseTypeDef",
    {
        "valid": bool,
        "validationErrors": List["ValidationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidationErrorTypeDef = TypedDict(
    "ValidationErrorTypeDef",
    {
        "errorMessage": str,
    },
    total=False,
)

ViolationEventAdditionalInfoTypeDef = TypedDict(
    "ViolationEventAdditionalInfoTypeDef",
    {
        "confidenceLevel": ConfidenceLevelType,
    },
    total=False,
)

ViolationEventOccurrenceRangeTypeDef = TypedDict(
    "ViolationEventOccurrenceRangeTypeDef",
    {
        "startTime": datetime,
        "endTime": datetime,
    },
)

ViolationEventTypeDef = TypedDict(
    "ViolationEventTypeDef",
    {
        "violationId": str,
        "thingName": str,
        "securityProfileName": str,
        "behavior": "BehaviorTypeDef",
        "metricValue": "MetricValueTypeDef",
        "violationEventAdditionalInfo": "ViolationEventAdditionalInfoTypeDef",
        "violationEventType": ViolationEventTypeType,
        "violationEventTime": datetime,
    },
    total=False,
)

_RequiredVpcDestinationConfigurationTypeDef = TypedDict(
    "_RequiredVpcDestinationConfigurationTypeDef",
    {
        "subnetIds": List[str],
        "vpcId": str,
        "roleArn": str,
    },
)
_OptionalVpcDestinationConfigurationTypeDef = TypedDict(
    "_OptionalVpcDestinationConfigurationTypeDef",
    {
        "securityGroups": List[str],
    },
    total=False,
)


class VpcDestinationConfigurationTypeDef(
    _RequiredVpcDestinationConfigurationTypeDef, _OptionalVpcDestinationConfigurationTypeDef
):
    pass


VpcDestinationPropertiesTypeDef = TypedDict(
    "VpcDestinationPropertiesTypeDef",
    {
        "subnetIds": List[str],
        "securityGroups": List[str],
        "vpcId": str,
        "roleArn": str,
    },
    total=False,
)

VpcDestinationSummaryTypeDef = TypedDict(
    "VpcDestinationSummaryTypeDef",
    {
        "subnetIds": List[str],
        "securityGroups": List[str],
        "vpcId": str,
        "roleArn": str,
    },
    total=False,
)
