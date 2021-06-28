"""
Type annotations for ssm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ssm.type_defs import AccountSharingInfoTypeDef

    data: AccountSharingInfoTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AssociationComplianceSeverityType,
    AssociationExecutionFilterKeyType,
    AssociationExecutionTargetsFilterKeyType,
    AssociationFilterKeyType,
    AssociationFilterOperatorTypeType,
    AssociationStatusNameType,
    AssociationSyncComplianceType,
    AttachmentsSourceKeyType,
    AutomationExecutionFilterKeyType,
    AutomationExecutionStatusType,
    AutomationTypeType,
    CalendarStateType,
    CommandFilterKeyType,
    CommandInvocationStatusType,
    CommandPluginStatusType,
    CommandStatusType,
    ComplianceQueryOperatorTypeType,
    ComplianceSeverityType,
    ComplianceStatusType,
    ComplianceUploadTypeType,
    ConnectionStatusType,
    DescribeActivationsFilterKeysType,
    DocumentFilterKeyType,
    DocumentFormatType,
    DocumentHashTypeType,
    DocumentParameterTypeType,
    DocumentReviewActionType,
    DocumentStatusType,
    DocumentTypeType,
    ExecutionModeType,
    FaultType,
    InstanceInformationFilterKeyType,
    InstancePatchStateOperatorTypeType,
    InventoryAttributeDataTypeType,
    InventoryDeletionStatusType,
    InventoryQueryOperatorTypeType,
    InventorySchemaDeleteOptionType,
    LastResourceDataSyncStatusType,
    MaintenanceWindowExecutionStatusType,
    MaintenanceWindowResourceTypeType,
    MaintenanceWindowTaskTypeType,
    NotificationEventType,
    NotificationTypeType,
    OperatingSystemType,
    OpsFilterOperatorTypeType,
    OpsItemDataTypeType,
    OpsItemFilterKeyType,
    OpsItemFilterOperatorType,
    OpsItemRelatedItemsFilterKeyType,
    OpsItemStatusType,
    ParametersFilterKeyType,
    ParameterTierType,
    ParameterTypeType,
    PatchActionType,
    PatchComplianceDataStateType,
    PatchComplianceLevelType,
    PatchDeploymentStatusType,
    PatchFilterKeyType,
    PatchOperationTypeType,
    PatchPropertyType,
    PatchSetType,
    PingStatusType,
    PlatformTypeType,
    RebootOptionType,
    ResourceTypeForTaggingType,
    ResourceTypeType,
    ReviewStatusType,
    SessionFilterKeyType,
    SessionStateType,
    SessionStatusType,
    SignalTypeType,
    StepExecutionFilterKeyType,
    StopTypeType,
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
    "AccountSharingInfoTypeDef",
    "ActivationTypeDef",
    "AddTagsToResourceRequestTypeDef",
    "AssociateOpsItemRelatedItemRequestTypeDef",
    "AssociateOpsItemRelatedItemResponseResponseTypeDef",
    "AssociationDescriptionTypeDef",
    "AssociationExecutionFilterTypeDef",
    "AssociationExecutionTargetTypeDef",
    "AssociationExecutionTargetsFilterTypeDef",
    "AssociationExecutionTypeDef",
    "AssociationFilterTypeDef",
    "AssociationOverviewTypeDef",
    "AssociationStatusTypeDef",
    "AssociationTypeDef",
    "AssociationVersionInfoTypeDef",
    "AttachmentContentTypeDef",
    "AttachmentInformationTypeDef",
    "AttachmentsSourceTypeDef",
    "AutomationExecutionFilterTypeDef",
    "AutomationExecutionMetadataTypeDef",
    "AutomationExecutionTypeDef",
    "BaselineOverrideTypeDef",
    "CancelCommandRequestTypeDef",
    "CancelMaintenanceWindowExecutionRequestTypeDef",
    "CancelMaintenanceWindowExecutionResultResponseTypeDef",
    "CloudWatchOutputConfigTypeDef",
    "CommandFilterTypeDef",
    "CommandInvocationTypeDef",
    "CommandPluginTypeDef",
    "CommandTypeDef",
    "ComplianceExecutionSummaryTypeDef",
    "ComplianceItemEntryTypeDef",
    "ComplianceItemTypeDef",
    "ComplianceStringFilterTypeDef",
    "ComplianceSummaryItemTypeDef",
    "CompliantSummaryTypeDef",
    "CreateActivationRequestTypeDef",
    "CreateActivationResultResponseTypeDef",
    "CreateAssociationBatchRequestEntryTypeDef",
    "CreateAssociationBatchRequestTypeDef",
    "CreateAssociationBatchResultResponseTypeDef",
    "CreateAssociationRequestTypeDef",
    "CreateAssociationResultResponseTypeDef",
    "CreateDocumentRequestTypeDef",
    "CreateDocumentResultResponseTypeDef",
    "CreateMaintenanceWindowRequestTypeDef",
    "CreateMaintenanceWindowResultResponseTypeDef",
    "CreateOpsItemRequestTypeDef",
    "CreateOpsItemResponseResponseTypeDef",
    "CreateOpsMetadataRequestTypeDef",
    "CreateOpsMetadataResultResponseTypeDef",
    "CreatePatchBaselineRequestTypeDef",
    "CreatePatchBaselineResultResponseTypeDef",
    "CreateResourceDataSyncRequestTypeDef",
    "DeleteActivationRequestTypeDef",
    "DeleteAssociationRequestTypeDef",
    "DeleteDocumentRequestTypeDef",
    "DeleteInventoryRequestTypeDef",
    "DeleteInventoryResultResponseTypeDef",
    "DeleteMaintenanceWindowRequestTypeDef",
    "DeleteMaintenanceWindowResultResponseTypeDef",
    "DeleteOpsMetadataRequestTypeDef",
    "DeleteParameterRequestTypeDef",
    "DeleteParametersRequestTypeDef",
    "DeleteParametersResultResponseTypeDef",
    "DeletePatchBaselineRequestTypeDef",
    "DeletePatchBaselineResultResponseTypeDef",
    "DeleteResourceDataSyncRequestTypeDef",
    "DeregisterManagedInstanceRequestTypeDef",
    "DeregisterPatchBaselineForPatchGroupRequestTypeDef",
    "DeregisterPatchBaselineForPatchGroupResultResponseTypeDef",
    "DeregisterTargetFromMaintenanceWindowRequestTypeDef",
    "DeregisterTargetFromMaintenanceWindowResultResponseTypeDef",
    "DeregisterTaskFromMaintenanceWindowRequestTypeDef",
    "DeregisterTaskFromMaintenanceWindowResultResponseTypeDef",
    "DescribeActivationsFilterTypeDef",
    "DescribeActivationsRequestTypeDef",
    "DescribeActivationsResultResponseTypeDef",
    "DescribeAssociationExecutionTargetsRequestTypeDef",
    "DescribeAssociationExecutionTargetsResultResponseTypeDef",
    "DescribeAssociationExecutionsRequestTypeDef",
    "DescribeAssociationExecutionsResultResponseTypeDef",
    "DescribeAssociationRequestTypeDef",
    "DescribeAssociationResultResponseTypeDef",
    "DescribeAutomationExecutionsRequestTypeDef",
    "DescribeAutomationExecutionsResultResponseTypeDef",
    "DescribeAutomationStepExecutionsRequestTypeDef",
    "DescribeAutomationStepExecutionsResultResponseTypeDef",
    "DescribeAvailablePatchesRequestTypeDef",
    "DescribeAvailablePatchesResultResponseTypeDef",
    "DescribeDocumentPermissionRequestTypeDef",
    "DescribeDocumentPermissionResponseResponseTypeDef",
    "DescribeDocumentRequestTypeDef",
    "DescribeDocumentResultResponseTypeDef",
    "DescribeEffectiveInstanceAssociationsRequestTypeDef",
    "DescribeEffectiveInstanceAssociationsResultResponseTypeDef",
    "DescribeEffectivePatchesForPatchBaselineRequestTypeDef",
    "DescribeEffectivePatchesForPatchBaselineResultResponseTypeDef",
    "DescribeInstanceAssociationsStatusRequestTypeDef",
    "DescribeInstanceAssociationsStatusResultResponseTypeDef",
    "DescribeInstanceInformationRequestTypeDef",
    "DescribeInstanceInformationResultResponseTypeDef",
    "DescribeInstancePatchStatesForPatchGroupRequestTypeDef",
    "DescribeInstancePatchStatesForPatchGroupResultResponseTypeDef",
    "DescribeInstancePatchStatesRequestTypeDef",
    "DescribeInstancePatchStatesResultResponseTypeDef",
    "DescribeInstancePatchesRequestTypeDef",
    "DescribeInstancePatchesResultResponseTypeDef",
    "DescribeInventoryDeletionsRequestTypeDef",
    "DescribeInventoryDeletionsResultResponseTypeDef",
    "DescribeMaintenanceWindowExecutionTaskInvocationsRequestTypeDef",
    "DescribeMaintenanceWindowExecutionTaskInvocationsResultResponseTypeDef",
    "DescribeMaintenanceWindowExecutionTasksRequestTypeDef",
    "DescribeMaintenanceWindowExecutionTasksResultResponseTypeDef",
    "DescribeMaintenanceWindowExecutionsRequestTypeDef",
    "DescribeMaintenanceWindowExecutionsResultResponseTypeDef",
    "DescribeMaintenanceWindowScheduleRequestTypeDef",
    "DescribeMaintenanceWindowScheduleResultResponseTypeDef",
    "DescribeMaintenanceWindowTargetsRequestTypeDef",
    "DescribeMaintenanceWindowTargetsResultResponseTypeDef",
    "DescribeMaintenanceWindowTasksRequestTypeDef",
    "DescribeMaintenanceWindowTasksResultResponseTypeDef",
    "DescribeMaintenanceWindowsForTargetRequestTypeDef",
    "DescribeMaintenanceWindowsForTargetResultResponseTypeDef",
    "DescribeMaintenanceWindowsRequestTypeDef",
    "DescribeMaintenanceWindowsResultResponseTypeDef",
    "DescribeOpsItemsRequestTypeDef",
    "DescribeOpsItemsResponseResponseTypeDef",
    "DescribeParametersRequestTypeDef",
    "DescribeParametersResultResponseTypeDef",
    "DescribePatchBaselinesRequestTypeDef",
    "DescribePatchBaselinesResultResponseTypeDef",
    "DescribePatchGroupStateRequestTypeDef",
    "DescribePatchGroupStateResultResponseTypeDef",
    "DescribePatchGroupsRequestTypeDef",
    "DescribePatchGroupsResultResponseTypeDef",
    "DescribePatchPropertiesRequestTypeDef",
    "DescribePatchPropertiesResultResponseTypeDef",
    "DescribeSessionsRequestTypeDef",
    "DescribeSessionsResponseResponseTypeDef",
    "DisassociateOpsItemRelatedItemRequestTypeDef",
    "DocumentDefaultVersionDescriptionTypeDef",
    "DocumentDescriptionTypeDef",
    "DocumentFilterTypeDef",
    "DocumentIdentifierTypeDef",
    "DocumentKeyValuesFilterTypeDef",
    "DocumentMetadataResponseInfoTypeDef",
    "DocumentParameterTypeDef",
    "DocumentRequiresTypeDef",
    "DocumentReviewCommentSourceTypeDef",
    "DocumentReviewerResponseSourceTypeDef",
    "DocumentReviewsTypeDef",
    "DocumentVersionInfoTypeDef",
    "EffectivePatchTypeDef",
    "FailedCreateAssociationTypeDef",
    "FailureDetailsTypeDef",
    "GetAutomationExecutionRequestTypeDef",
    "GetAutomationExecutionResultResponseTypeDef",
    "GetCalendarStateRequestTypeDef",
    "GetCalendarStateResponseResponseTypeDef",
    "GetCommandInvocationRequestTypeDef",
    "GetCommandInvocationResultResponseTypeDef",
    "GetConnectionStatusRequestTypeDef",
    "GetConnectionStatusResponseResponseTypeDef",
    "GetDefaultPatchBaselineRequestTypeDef",
    "GetDefaultPatchBaselineResultResponseTypeDef",
    "GetDeployablePatchSnapshotForInstanceRequestTypeDef",
    "GetDeployablePatchSnapshotForInstanceResultResponseTypeDef",
    "GetDocumentRequestTypeDef",
    "GetDocumentResultResponseTypeDef",
    "GetInventoryRequestTypeDef",
    "GetInventoryResultResponseTypeDef",
    "GetInventorySchemaRequestTypeDef",
    "GetInventorySchemaResultResponseTypeDef",
    "GetMaintenanceWindowExecutionRequestTypeDef",
    "GetMaintenanceWindowExecutionResultResponseTypeDef",
    "GetMaintenanceWindowExecutionTaskInvocationRequestTypeDef",
    "GetMaintenanceWindowExecutionTaskInvocationResultResponseTypeDef",
    "GetMaintenanceWindowExecutionTaskRequestTypeDef",
    "GetMaintenanceWindowExecutionTaskResultResponseTypeDef",
    "GetMaintenanceWindowRequestTypeDef",
    "GetMaintenanceWindowResultResponseTypeDef",
    "GetMaintenanceWindowTaskRequestTypeDef",
    "GetMaintenanceWindowTaskResultResponseTypeDef",
    "GetOpsItemRequestTypeDef",
    "GetOpsItemResponseResponseTypeDef",
    "GetOpsMetadataRequestTypeDef",
    "GetOpsMetadataResultResponseTypeDef",
    "GetOpsSummaryRequestTypeDef",
    "GetOpsSummaryResultResponseTypeDef",
    "GetParameterHistoryRequestTypeDef",
    "GetParameterHistoryResultResponseTypeDef",
    "GetParameterRequestTypeDef",
    "GetParameterResultResponseTypeDef",
    "GetParametersByPathRequestTypeDef",
    "GetParametersByPathResultResponseTypeDef",
    "GetParametersRequestTypeDef",
    "GetParametersResultResponseTypeDef",
    "GetPatchBaselineForPatchGroupRequestTypeDef",
    "GetPatchBaselineForPatchGroupResultResponseTypeDef",
    "GetPatchBaselineRequestTypeDef",
    "GetPatchBaselineResultResponseTypeDef",
    "GetServiceSettingRequestTypeDef",
    "GetServiceSettingResultResponseTypeDef",
    "InstanceAggregatedAssociationOverviewTypeDef",
    "InstanceAssociationOutputLocationTypeDef",
    "InstanceAssociationOutputUrlTypeDef",
    "InstanceAssociationStatusInfoTypeDef",
    "InstanceAssociationTypeDef",
    "InstanceInformationFilterTypeDef",
    "InstanceInformationStringFilterTypeDef",
    "InstanceInformationTypeDef",
    "InstancePatchStateFilterTypeDef",
    "InstancePatchStateTypeDef",
    "InventoryAggregatorTypeDef",
    "InventoryDeletionStatusItemTypeDef",
    "InventoryDeletionSummaryItemTypeDef",
    "InventoryDeletionSummaryTypeDef",
    "InventoryFilterTypeDef",
    "InventoryGroupTypeDef",
    "InventoryItemAttributeTypeDef",
    "InventoryItemSchemaTypeDef",
    "InventoryItemTypeDef",
    "InventoryResultEntityTypeDef",
    "InventoryResultItemTypeDef",
    "LabelParameterVersionRequestTypeDef",
    "LabelParameterVersionResultResponseTypeDef",
    "ListAssociationVersionsRequestTypeDef",
    "ListAssociationVersionsResultResponseTypeDef",
    "ListAssociationsRequestTypeDef",
    "ListAssociationsResultResponseTypeDef",
    "ListCommandInvocationsRequestTypeDef",
    "ListCommandInvocationsResultResponseTypeDef",
    "ListCommandsRequestTypeDef",
    "ListCommandsResultResponseTypeDef",
    "ListComplianceItemsRequestTypeDef",
    "ListComplianceItemsResultResponseTypeDef",
    "ListComplianceSummariesRequestTypeDef",
    "ListComplianceSummariesResultResponseTypeDef",
    "ListDocumentMetadataHistoryRequestTypeDef",
    "ListDocumentMetadataHistoryResponseResponseTypeDef",
    "ListDocumentVersionsRequestTypeDef",
    "ListDocumentVersionsResultResponseTypeDef",
    "ListDocumentsRequestTypeDef",
    "ListDocumentsResultResponseTypeDef",
    "ListInventoryEntriesRequestTypeDef",
    "ListInventoryEntriesResultResponseTypeDef",
    "ListOpsItemEventsRequestTypeDef",
    "ListOpsItemEventsResponseResponseTypeDef",
    "ListOpsItemRelatedItemsRequestTypeDef",
    "ListOpsItemRelatedItemsResponseResponseTypeDef",
    "ListOpsMetadataRequestTypeDef",
    "ListOpsMetadataResultResponseTypeDef",
    "ListResourceComplianceSummariesRequestTypeDef",
    "ListResourceComplianceSummariesResultResponseTypeDef",
    "ListResourceDataSyncRequestTypeDef",
    "ListResourceDataSyncResultResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResultResponseTypeDef",
    "LoggingInfoTypeDef",
    "MaintenanceWindowAutomationParametersTypeDef",
    "MaintenanceWindowExecutionTaskIdentityTypeDef",
    "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef",
    "MaintenanceWindowExecutionTypeDef",
    "MaintenanceWindowFilterTypeDef",
    "MaintenanceWindowIdentityForTargetTypeDef",
    "MaintenanceWindowIdentityTypeDef",
    "MaintenanceWindowLambdaParametersTypeDef",
    "MaintenanceWindowRunCommandParametersTypeDef",
    "MaintenanceWindowStepFunctionsParametersTypeDef",
    "MaintenanceWindowTargetTypeDef",
    "MaintenanceWindowTaskInvocationParametersTypeDef",
    "MaintenanceWindowTaskParameterValueExpressionTypeDef",
    "MaintenanceWindowTaskTypeDef",
    "MetadataValueTypeDef",
    "ModifyDocumentPermissionRequestTypeDef",
    "NonCompliantSummaryTypeDef",
    "NotificationConfigTypeDef",
    "OpsAggregatorTypeDef",
    "OpsEntityItemTypeDef",
    "OpsEntityTypeDef",
    "OpsFilterTypeDef",
    "OpsItemDataValueTypeDef",
    "OpsItemEventFilterTypeDef",
    "OpsItemEventSummaryTypeDef",
    "OpsItemFilterTypeDef",
    "OpsItemIdentityTypeDef",
    "OpsItemNotificationTypeDef",
    "OpsItemRelatedItemSummaryTypeDef",
    "OpsItemRelatedItemsFilterTypeDef",
    "OpsItemSummaryTypeDef",
    "OpsItemTypeDef",
    "OpsMetadataFilterTypeDef",
    "OpsMetadataTypeDef",
    "OpsResultAttributeTypeDef",
    "OutputSourceTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterHistoryTypeDef",
    "ParameterInlinePolicyTypeDef",
    "ParameterMetadataTypeDef",
    "ParameterStringFilterTypeDef",
    "ParameterTypeDef",
    "ParametersFilterTypeDef",
    "PatchBaselineIdentityTypeDef",
    "PatchComplianceDataTypeDef",
    "PatchFilterGroupTypeDef",
    "PatchFilterTypeDef",
    "PatchGroupPatchBaselineMappingTypeDef",
    "PatchOrchestratorFilterTypeDef",
    "PatchRuleGroupTypeDef",
    "PatchRuleTypeDef",
    "PatchSourceTypeDef",
    "PatchStatusTypeDef",
    "PatchTypeDef",
    "ProgressCountersTypeDef",
    "PutComplianceItemsRequestTypeDef",
    "PutInventoryRequestTypeDef",
    "PutInventoryResultResponseTypeDef",
    "PutParameterRequestTypeDef",
    "PutParameterResultResponseTypeDef",
    "RegisterDefaultPatchBaselineRequestTypeDef",
    "RegisterDefaultPatchBaselineResultResponseTypeDef",
    "RegisterPatchBaselineForPatchGroupRequestTypeDef",
    "RegisterPatchBaselineForPatchGroupResultResponseTypeDef",
    "RegisterTargetWithMaintenanceWindowRequestTypeDef",
    "RegisterTargetWithMaintenanceWindowResultResponseTypeDef",
    "RegisterTaskWithMaintenanceWindowRequestTypeDef",
    "RegisterTaskWithMaintenanceWindowResultResponseTypeDef",
    "RelatedOpsItemTypeDef",
    "RemoveTagsFromResourceRequestTypeDef",
    "ResetServiceSettingRequestTypeDef",
    "ResetServiceSettingResultResponseTypeDef",
    "ResolvedTargetsTypeDef",
    "ResourceComplianceSummaryItemTypeDef",
    "ResourceDataSyncAwsOrganizationsSourceTypeDef",
    "ResourceDataSyncDestinationDataSharingTypeDef",
    "ResourceDataSyncItemTypeDef",
    "ResourceDataSyncOrganizationalUnitTypeDef",
    "ResourceDataSyncS3DestinationTypeDef",
    "ResourceDataSyncSourceTypeDef",
    "ResourceDataSyncSourceWithStateTypeDef",
    "ResponseMetadataTypeDef",
    "ResultAttributeTypeDef",
    "ResumeSessionRequestTypeDef",
    "ResumeSessionResponseResponseTypeDef",
    "ReviewInformationTypeDef",
    "RunbookTypeDef",
    "S3OutputLocationTypeDef",
    "S3OutputUrlTypeDef",
    "ScheduledWindowExecutionTypeDef",
    "SendAutomationSignalRequestTypeDef",
    "SendCommandRequestTypeDef",
    "SendCommandResultResponseTypeDef",
    "ServiceSettingTypeDef",
    "SessionFilterTypeDef",
    "SessionManagerOutputUrlTypeDef",
    "SessionTypeDef",
    "SeveritySummaryTypeDef",
    "StartAssociationsOnceRequestTypeDef",
    "StartAutomationExecutionRequestTypeDef",
    "StartAutomationExecutionResultResponseTypeDef",
    "StartChangeRequestExecutionRequestTypeDef",
    "StartChangeRequestExecutionResultResponseTypeDef",
    "StartSessionRequestTypeDef",
    "StartSessionResponseResponseTypeDef",
    "StepExecutionFilterTypeDef",
    "StepExecutionTypeDef",
    "StopAutomationExecutionRequestTypeDef",
    "TagTypeDef",
    "TargetLocationTypeDef",
    "TargetTypeDef",
    "TerminateSessionRequestTypeDef",
    "TerminateSessionResponseResponseTypeDef",
    "UnlabelParameterVersionRequestTypeDef",
    "UnlabelParameterVersionResultResponseTypeDef",
    "UpdateAssociationRequestTypeDef",
    "UpdateAssociationResultResponseTypeDef",
    "UpdateAssociationStatusRequestTypeDef",
    "UpdateAssociationStatusResultResponseTypeDef",
    "UpdateDocumentDefaultVersionRequestTypeDef",
    "UpdateDocumentDefaultVersionResultResponseTypeDef",
    "UpdateDocumentMetadataRequestTypeDef",
    "UpdateDocumentRequestTypeDef",
    "UpdateDocumentResultResponseTypeDef",
    "UpdateMaintenanceWindowRequestTypeDef",
    "UpdateMaintenanceWindowResultResponseTypeDef",
    "UpdateMaintenanceWindowTargetRequestTypeDef",
    "UpdateMaintenanceWindowTargetResultResponseTypeDef",
    "UpdateMaintenanceWindowTaskRequestTypeDef",
    "UpdateMaintenanceWindowTaskResultResponseTypeDef",
    "UpdateManagedInstanceRoleRequestTypeDef",
    "UpdateOpsItemRequestTypeDef",
    "UpdateOpsMetadataRequestTypeDef",
    "UpdateOpsMetadataResultResponseTypeDef",
    "UpdatePatchBaselineRequestTypeDef",
    "UpdatePatchBaselineResultResponseTypeDef",
    "UpdateResourceDataSyncRequestTypeDef",
    "UpdateServiceSettingRequestTypeDef",
    "WaiterConfigTypeDef",
)

AccountSharingInfoTypeDef = TypedDict(
    "AccountSharingInfoTypeDef",
    {
        "AccountId": str,
        "SharedDocumentVersion": str,
    },
    total=False,
)

ActivationTypeDef = TypedDict(
    "ActivationTypeDef",
    {
        "ActivationId": str,
        "Description": str,
        "DefaultInstanceName": str,
        "IamRole": str,
        "RegistrationLimit": int,
        "RegistrationsCount": int,
        "ExpirationDate": datetime,
        "Expired": bool,
        "CreatedDate": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

AddTagsToResourceRequestTypeDef = TypedDict(
    "AddTagsToResourceRequestTypeDef",
    {
        "ResourceType": ResourceTypeForTaggingType,
        "ResourceId": str,
        "Tags": List["TagTypeDef"],
    },
)

AssociateOpsItemRelatedItemRequestTypeDef = TypedDict(
    "AssociateOpsItemRelatedItemRequestTypeDef",
    {
        "OpsItemId": str,
        "AssociationType": str,
        "ResourceType": str,
        "ResourceUri": str,
    },
)

AssociateOpsItemRelatedItemResponseResponseTypeDef = TypedDict(
    "AssociateOpsItemRelatedItemResponseResponseTypeDef",
    {
        "AssociationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociationDescriptionTypeDef = TypedDict(
    "AssociationDescriptionTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationVersion": str,
        "Date": datetime,
        "LastUpdateAssociationDate": datetime,
        "Status": "AssociationStatusTypeDef",
        "Overview": "AssociationOverviewTypeDef",
        "DocumentVersion": str,
        "AutomationTargetParameterName": str,
        "Parameters": Dict[str, List[str]],
        "AssociationId": str,
        "Targets": List["TargetTypeDef"],
        "ScheduleExpression": str,
        "OutputLocation": "InstanceAssociationOutputLocationTypeDef",
        "LastExecutionDate": datetime,
        "LastSuccessfulExecutionDate": datetime,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": AssociationComplianceSeverityType,
        "SyncCompliance": AssociationSyncComplianceType,
        "ApplyOnlyAtCronInterval": bool,
        "CalendarNames": List[str],
        "TargetLocations": List["TargetLocationTypeDef"],
    },
    total=False,
)

AssociationExecutionFilterTypeDef = TypedDict(
    "AssociationExecutionFilterTypeDef",
    {
        "Key": AssociationExecutionFilterKeyType,
        "Value": str,
        "Type": AssociationFilterOperatorTypeType,
    },
)

AssociationExecutionTargetTypeDef = TypedDict(
    "AssociationExecutionTargetTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "ExecutionId": str,
        "ResourceId": str,
        "ResourceType": str,
        "Status": str,
        "DetailedStatus": str,
        "LastExecutionDate": datetime,
        "OutputSource": "OutputSourceTypeDef",
    },
    total=False,
)

AssociationExecutionTargetsFilterTypeDef = TypedDict(
    "AssociationExecutionTargetsFilterTypeDef",
    {
        "Key": AssociationExecutionTargetsFilterKeyType,
        "Value": str,
    },
)

AssociationExecutionTypeDef = TypedDict(
    "AssociationExecutionTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "ExecutionId": str,
        "Status": str,
        "DetailedStatus": str,
        "CreatedTime": datetime,
        "LastExecutionDate": datetime,
        "ResourceCountByStatus": str,
    },
    total=False,
)

AssociationFilterTypeDef = TypedDict(
    "AssociationFilterTypeDef",
    {
        "key": AssociationFilterKeyType,
        "value": str,
    },
)

AssociationOverviewTypeDef = TypedDict(
    "AssociationOverviewTypeDef",
    {
        "Status": str,
        "DetailedStatus": str,
        "AssociationStatusAggregatedCount": Dict[str, int],
    },
    total=False,
)

_RequiredAssociationStatusTypeDef = TypedDict(
    "_RequiredAssociationStatusTypeDef",
    {
        "Date": datetime,
        "Name": AssociationStatusNameType,
        "Message": str,
    },
)
_OptionalAssociationStatusTypeDef = TypedDict(
    "_OptionalAssociationStatusTypeDef",
    {
        "AdditionalInfo": str,
    },
    total=False,
)


class AssociationStatusTypeDef(
    _RequiredAssociationStatusTypeDef, _OptionalAssociationStatusTypeDef
):
    pass


AssociationTypeDef = TypedDict(
    "AssociationTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationId": str,
        "AssociationVersion": str,
        "DocumentVersion": str,
        "Targets": List["TargetTypeDef"],
        "LastExecutionDate": datetime,
        "Overview": "AssociationOverviewTypeDef",
        "ScheduleExpression": str,
        "AssociationName": str,
    },
    total=False,
)

AssociationVersionInfoTypeDef = TypedDict(
    "AssociationVersionInfoTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "CreatedDate": datetime,
        "Name": str,
        "DocumentVersion": str,
        "Parameters": Dict[str, List[str]],
        "Targets": List["TargetTypeDef"],
        "ScheduleExpression": str,
        "OutputLocation": "InstanceAssociationOutputLocationTypeDef",
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": AssociationComplianceSeverityType,
        "SyncCompliance": AssociationSyncComplianceType,
        "ApplyOnlyAtCronInterval": bool,
        "CalendarNames": List[str],
        "TargetLocations": List["TargetLocationTypeDef"],
    },
    total=False,
)

AttachmentContentTypeDef = TypedDict(
    "AttachmentContentTypeDef",
    {
        "Name": str,
        "Size": int,
        "Hash": str,
        "HashType": Literal["Sha256"],
        "Url": str,
    },
    total=False,
)

AttachmentInformationTypeDef = TypedDict(
    "AttachmentInformationTypeDef",
    {
        "Name": str,
    },
    total=False,
)

AttachmentsSourceTypeDef = TypedDict(
    "AttachmentsSourceTypeDef",
    {
        "Key": AttachmentsSourceKeyType,
        "Values": List[str],
        "Name": str,
    },
    total=False,
)

AutomationExecutionFilterTypeDef = TypedDict(
    "AutomationExecutionFilterTypeDef",
    {
        "Key": AutomationExecutionFilterKeyType,
        "Values": List[str],
    },
)

AutomationExecutionMetadataTypeDef = TypedDict(
    "AutomationExecutionMetadataTypeDef",
    {
        "AutomationExecutionId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "AutomationExecutionStatus": AutomationExecutionStatusType,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "ExecutedBy": str,
        "LogFile": str,
        "Outputs": Dict[str, List[str]],
        "Mode": ExecutionModeType,
        "ParentAutomationExecutionId": str,
        "CurrentStepName": str,
        "CurrentAction": str,
        "FailureMessage": str,
        "TargetParameterName": str,
        "Targets": List["TargetTypeDef"],
        "TargetMaps": List[Dict[str, List[str]]],
        "ResolvedTargets": "ResolvedTargetsTypeDef",
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Target": str,
        "AutomationType": AutomationTypeType,
        "AutomationSubtype": Literal["ChangeRequest"],
        "ScheduledTime": datetime,
        "Runbooks": List["RunbookTypeDef"],
        "OpsItemId": str,
        "AssociationId": str,
        "ChangeRequestName": str,
    },
    total=False,
)

AutomationExecutionTypeDef = TypedDict(
    "AutomationExecutionTypeDef",
    {
        "AutomationExecutionId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "AutomationExecutionStatus": AutomationExecutionStatusType,
        "StepExecutions": List["StepExecutionTypeDef"],
        "StepExecutionsTruncated": bool,
        "Parameters": Dict[str, List[str]],
        "Outputs": Dict[str, List[str]],
        "FailureMessage": str,
        "Mode": ExecutionModeType,
        "ParentAutomationExecutionId": str,
        "ExecutedBy": str,
        "CurrentStepName": str,
        "CurrentAction": str,
        "TargetParameterName": str,
        "Targets": List["TargetTypeDef"],
        "TargetMaps": List[Dict[str, List[str]]],
        "ResolvedTargets": "ResolvedTargetsTypeDef",
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Target": str,
        "TargetLocations": List["TargetLocationTypeDef"],
        "ProgressCounters": "ProgressCountersTypeDef",
        "AutomationSubtype": Literal["ChangeRequest"],
        "ScheduledTime": datetime,
        "Runbooks": List["RunbookTypeDef"],
        "OpsItemId": str,
        "AssociationId": str,
        "ChangeRequestName": str,
    },
    total=False,
)

BaselineOverrideTypeDef = TypedDict(
    "BaselineOverrideTypeDef",
    {
        "OperatingSystem": OperatingSystemType,
        "GlobalFilters": "PatchFilterGroupTypeDef",
        "ApprovalRules": "PatchRuleGroupTypeDef",
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": PatchComplianceLevelType,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": PatchActionType,
        "ApprovedPatchesEnableNonSecurity": bool,
        "Sources": List["PatchSourceTypeDef"],
    },
    total=False,
)

_RequiredCancelCommandRequestTypeDef = TypedDict(
    "_RequiredCancelCommandRequestTypeDef",
    {
        "CommandId": str,
    },
)
_OptionalCancelCommandRequestTypeDef = TypedDict(
    "_OptionalCancelCommandRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
    total=False,
)


class CancelCommandRequestTypeDef(
    _RequiredCancelCommandRequestTypeDef, _OptionalCancelCommandRequestTypeDef
):
    pass


CancelMaintenanceWindowExecutionRequestTypeDef = TypedDict(
    "CancelMaintenanceWindowExecutionRequestTypeDef",
    {
        "WindowExecutionId": str,
    },
)

CancelMaintenanceWindowExecutionResultResponseTypeDef = TypedDict(
    "CancelMaintenanceWindowExecutionResultResponseTypeDef",
    {
        "WindowExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CloudWatchOutputConfigTypeDef = TypedDict(
    "CloudWatchOutputConfigTypeDef",
    {
        "CloudWatchLogGroupName": str,
        "CloudWatchOutputEnabled": bool,
    },
    total=False,
)

CommandFilterTypeDef = TypedDict(
    "CommandFilterTypeDef",
    {
        "key": CommandFilterKeyType,
        "value": str,
    },
)

CommandInvocationTypeDef = TypedDict(
    "CommandInvocationTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "InstanceName": str,
        "Comment": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "RequestedDateTime": datetime,
        "Status": CommandInvocationStatusType,
        "StatusDetails": str,
        "TraceOutput": str,
        "StandardOutputUrl": str,
        "StandardErrorUrl": str,
        "CommandPlugins": List["CommandPluginTypeDef"],
        "ServiceRole": str,
        "NotificationConfig": "NotificationConfigTypeDef",
        "CloudWatchOutputConfig": "CloudWatchOutputConfigTypeDef",
    },
    total=False,
)

CommandPluginTypeDef = TypedDict(
    "CommandPluginTypeDef",
    {
        "Name": str,
        "Status": CommandPluginStatusType,
        "StatusDetails": str,
        "ResponseCode": int,
        "ResponseStartDateTime": datetime,
        "ResponseFinishDateTime": datetime,
        "Output": str,
        "StandardOutputUrl": str,
        "StandardErrorUrl": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
    },
    total=False,
)

CommandTypeDef = TypedDict(
    "CommandTypeDef",
    {
        "CommandId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "Comment": str,
        "ExpiresAfter": datetime,
        "Parameters": Dict[str, List[str]],
        "InstanceIds": List[str],
        "Targets": List["TargetTypeDef"],
        "RequestedDateTime": datetime,
        "Status": CommandStatusType,
        "StatusDetails": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "TargetCount": int,
        "CompletedCount": int,
        "ErrorCount": int,
        "DeliveryTimedOutCount": int,
        "ServiceRole": str,
        "NotificationConfig": "NotificationConfigTypeDef",
        "CloudWatchOutputConfig": "CloudWatchOutputConfigTypeDef",
        "TimeoutSeconds": int,
    },
    total=False,
)

_RequiredComplianceExecutionSummaryTypeDef = TypedDict(
    "_RequiredComplianceExecutionSummaryTypeDef",
    {
        "ExecutionTime": datetime,
    },
)
_OptionalComplianceExecutionSummaryTypeDef = TypedDict(
    "_OptionalComplianceExecutionSummaryTypeDef",
    {
        "ExecutionId": str,
        "ExecutionType": str,
    },
    total=False,
)


class ComplianceExecutionSummaryTypeDef(
    _RequiredComplianceExecutionSummaryTypeDef, _OptionalComplianceExecutionSummaryTypeDef
):
    pass


_RequiredComplianceItemEntryTypeDef = TypedDict(
    "_RequiredComplianceItemEntryTypeDef",
    {
        "Severity": ComplianceSeverityType,
        "Status": ComplianceStatusType,
    },
)
_OptionalComplianceItemEntryTypeDef = TypedDict(
    "_OptionalComplianceItemEntryTypeDef",
    {
        "Id": str,
        "Title": str,
        "Details": Dict[str, str],
    },
    total=False,
)


class ComplianceItemEntryTypeDef(
    _RequiredComplianceItemEntryTypeDef, _OptionalComplianceItemEntryTypeDef
):
    pass


ComplianceItemTypeDef = TypedDict(
    "ComplianceItemTypeDef",
    {
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceId": str,
        "Id": str,
        "Title": str,
        "Status": ComplianceStatusType,
        "Severity": ComplianceSeverityType,
        "ExecutionSummary": "ComplianceExecutionSummaryTypeDef",
        "Details": Dict[str, str],
    },
    total=False,
)

ComplianceStringFilterTypeDef = TypedDict(
    "ComplianceStringFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": ComplianceQueryOperatorTypeType,
    },
    total=False,
)

ComplianceSummaryItemTypeDef = TypedDict(
    "ComplianceSummaryItemTypeDef",
    {
        "ComplianceType": str,
        "CompliantSummary": "CompliantSummaryTypeDef",
        "NonCompliantSummary": "NonCompliantSummaryTypeDef",
    },
    total=False,
)

CompliantSummaryTypeDef = TypedDict(
    "CompliantSummaryTypeDef",
    {
        "CompliantCount": int,
        "SeveritySummary": "SeveritySummaryTypeDef",
    },
    total=False,
)

_RequiredCreateActivationRequestTypeDef = TypedDict(
    "_RequiredCreateActivationRequestTypeDef",
    {
        "IamRole": str,
    },
)
_OptionalCreateActivationRequestTypeDef = TypedDict(
    "_OptionalCreateActivationRequestTypeDef",
    {
        "Description": str,
        "DefaultInstanceName": str,
        "RegistrationLimit": int,
        "ExpirationDate": Union[datetime, str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateActivationRequestTypeDef(
    _RequiredCreateActivationRequestTypeDef, _OptionalCreateActivationRequestTypeDef
):
    pass


CreateActivationResultResponseTypeDef = TypedDict(
    "CreateActivationResultResponseTypeDef",
    {
        "ActivationId": str,
        "ActivationCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssociationBatchRequestEntryTypeDef = TypedDict(
    "_RequiredCreateAssociationBatchRequestEntryTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateAssociationBatchRequestEntryTypeDef = TypedDict(
    "_OptionalCreateAssociationBatchRequestEntryTypeDef",
    {
        "InstanceId": str,
        "Parameters": Dict[str, List[str]],
        "AutomationTargetParameterName": str,
        "DocumentVersion": str,
        "Targets": List["TargetTypeDef"],
        "ScheduleExpression": str,
        "OutputLocation": "InstanceAssociationOutputLocationTypeDef",
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": AssociationComplianceSeverityType,
        "SyncCompliance": AssociationSyncComplianceType,
        "ApplyOnlyAtCronInterval": bool,
        "CalendarNames": List[str],
        "TargetLocations": List["TargetLocationTypeDef"],
    },
    total=False,
)


class CreateAssociationBatchRequestEntryTypeDef(
    _RequiredCreateAssociationBatchRequestEntryTypeDef,
    _OptionalCreateAssociationBatchRequestEntryTypeDef,
):
    pass


CreateAssociationBatchRequestTypeDef = TypedDict(
    "CreateAssociationBatchRequestTypeDef",
    {
        "Entries": List["CreateAssociationBatchRequestEntryTypeDef"],
    },
)

CreateAssociationBatchResultResponseTypeDef = TypedDict(
    "CreateAssociationBatchResultResponseTypeDef",
    {
        "Successful": List["AssociationDescriptionTypeDef"],
        "Failed": List["FailedCreateAssociationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssociationRequestTypeDef = TypedDict(
    "_RequiredCreateAssociationRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateAssociationRequestTypeDef = TypedDict(
    "_OptionalCreateAssociationRequestTypeDef",
    {
        "DocumentVersion": str,
        "InstanceId": str,
        "Parameters": Dict[str, List[str]],
        "Targets": List["TargetTypeDef"],
        "ScheduleExpression": str,
        "OutputLocation": "InstanceAssociationOutputLocationTypeDef",
        "AssociationName": str,
        "AutomationTargetParameterName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": AssociationComplianceSeverityType,
        "SyncCompliance": AssociationSyncComplianceType,
        "ApplyOnlyAtCronInterval": bool,
        "CalendarNames": List[str],
        "TargetLocations": List["TargetLocationTypeDef"],
    },
    total=False,
)


class CreateAssociationRequestTypeDef(
    _RequiredCreateAssociationRequestTypeDef, _OptionalCreateAssociationRequestTypeDef
):
    pass


CreateAssociationResultResponseTypeDef = TypedDict(
    "CreateAssociationResultResponseTypeDef",
    {
        "AssociationDescription": "AssociationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDocumentRequestTypeDef = TypedDict(
    "_RequiredCreateDocumentRequestTypeDef",
    {
        "Content": str,
        "Name": str,
    },
)
_OptionalCreateDocumentRequestTypeDef = TypedDict(
    "_OptionalCreateDocumentRequestTypeDef",
    {
        "Requires": List["DocumentRequiresTypeDef"],
        "Attachments": List["AttachmentsSourceTypeDef"],
        "DisplayName": str,
        "VersionName": str,
        "DocumentType": DocumentTypeType,
        "DocumentFormat": DocumentFormatType,
        "TargetType": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDocumentRequestTypeDef(
    _RequiredCreateDocumentRequestTypeDef, _OptionalCreateDocumentRequestTypeDef
):
    pass


CreateDocumentResultResponseTypeDef = TypedDict(
    "CreateDocumentResultResponseTypeDef",
    {
        "DocumentDescription": "DocumentDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMaintenanceWindowRequestTypeDef = TypedDict(
    "_RequiredCreateMaintenanceWindowRequestTypeDef",
    {
        "Name": str,
        "Schedule": str,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
    },
)
_OptionalCreateMaintenanceWindowRequestTypeDef = TypedDict(
    "_OptionalCreateMaintenanceWindowRequestTypeDef",
    {
        "Description": str,
        "StartDate": str,
        "EndDate": str,
        "ScheduleTimezone": str,
        "ScheduleOffset": int,
        "ClientToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateMaintenanceWindowRequestTypeDef(
    _RequiredCreateMaintenanceWindowRequestTypeDef, _OptionalCreateMaintenanceWindowRequestTypeDef
):
    pass


CreateMaintenanceWindowResultResponseTypeDef = TypedDict(
    "CreateMaintenanceWindowResultResponseTypeDef",
    {
        "WindowId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateOpsItemRequestTypeDef = TypedDict(
    "_RequiredCreateOpsItemRequestTypeDef",
    {
        "Description": str,
        "Source": str,
        "Title": str,
    },
)
_OptionalCreateOpsItemRequestTypeDef = TypedDict(
    "_OptionalCreateOpsItemRequestTypeDef",
    {
        "OpsItemType": str,
        "OperationalData": Dict[str, "OpsItemDataValueTypeDef"],
        "Notifications": List["OpsItemNotificationTypeDef"],
        "Priority": int,
        "RelatedOpsItems": List["RelatedOpsItemTypeDef"],
        "Tags": List["TagTypeDef"],
        "Category": str,
        "Severity": str,
        "ActualStartTime": Union[datetime, str],
        "ActualEndTime": Union[datetime, str],
        "PlannedStartTime": Union[datetime, str],
        "PlannedEndTime": Union[datetime, str],
    },
    total=False,
)


class CreateOpsItemRequestTypeDef(
    _RequiredCreateOpsItemRequestTypeDef, _OptionalCreateOpsItemRequestTypeDef
):
    pass


CreateOpsItemResponseResponseTypeDef = TypedDict(
    "CreateOpsItemResponseResponseTypeDef",
    {
        "OpsItemId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateOpsMetadataRequestTypeDef = TypedDict(
    "_RequiredCreateOpsMetadataRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalCreateOpsMetadataRequestTypeDef = TypedDict(
    "_OptionalCreateOpsMetadataRequestTypeDef",
    {
        "Metadata": Dict[str, "MetadataValueTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateOpsMetadataRequestTypeDef(
    _RequiredCreateOpsMetadataRequestTypeDef, _OptionalCreateOpsMetadataRequestTypeDef
):
    pass


CreateOpsMetadataResultResponseTypeDef = TypedDict(
    "CreateOpsMetadataResultResponseTypeDef",
    {
        "OpsMetadataArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePatchBaselineRequestTypeDef = TypedDict(
    "_RequiredCreatePatchBaselineRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreatePatchBaselineRequestTypeDef = TypedDict(
    "_OptionalCreatePatchBaselineRequestTypeDef",
    {
        "OperatingSystem": OperatingSystemType,
        "GlobalFilters": "PatchFilterGroupTypeDef",
        "ApprovalRules": "PatchRuleGroupTypeDef",
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": PatchComplianceLevelType,
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": PatchActionType,
        "Description": str,
        "Sources": List["PatchSourceTypeDef"],
        "ClientToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreatePatchBaselineRequestTypeDef(
    _RequiredCreatePatchBaselineRequestTypeDef, _OptionalCreatePatchBaselineRequestTypeDef
):
    pass


CreatePatchBaselineResultResponseTypeDef = TypedDict(
    "CreatePatchBaselineResultResponseTypeDef",
    {
        "BaselineId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResourceDataSyncRequestTypeDef = TypedDict(
    "_RequiredCreateResourceDataSyncRequestTypeDef",
    {
        "SyncName": str,
    },
)
_OptionalCreateResourceDataSyncRequestTypeDef = TypedDict(
    "_OptionalCreateResourceDataSyncRequestTypeDef",
    {
        "S3Destination": "ResourceDataSyncS3DestinationTypeDef",
        "SyncType": str,
        "SyncSource": "ResourceDataSyncSourceTypeDef",
    },
    total=False,
)


class CreateResourceDataSyncRequestTypeDef(
    _RequiredCreateResourceDataSyncRequestTypeDef, _OptionalCreateResourceDataSyncRequestTypeDef
):
    pass


DeleteActivationRequestTypeDef = TypedDict(
    "DeleteActivationRequestTypeDef",
    {
        "ActivationId": str,
    },
)

DeleteAssociationRequestTypeDef = TypedDict(
    "DeleteAssociationRequestTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationId": str,
    },
    total=False,
)

_RequiredDeleteDocumentRequestTypeDef = TypedDict(
    "_RequiredDeleteDocumentRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDeleteDocumentRequestTypeDef = TypedDict(
    "_OptionalDeleteDocumentRequestTypeDef",
    {
        "DocumentVersion": str,
        "VersionName": str,
        "Force": bool,
    },
    total=False,
)


class DeleteDocumentRequestTypeDef(
    _RequiredDeleteDocumentRequestTypeDef, _OptionalDeleteDocumentRequestTypeDef
):
    pass


_RequiredDeleteInventoryRequestTypeDef = TypedDict(
    "_RequiredDeleteInventoryRequestTypeDef",
    {
        "TypeName": str,
    },
)
_OptionalDeleteInventoryRequestTypeDef = TypedDict(
    "_OptionalDeleteInventoryRequestTypeDef",
    {
        "SchemaDeleteOption": InventorySchemaDeleteOptionType,
        "DryRun": bool,
        "ClientToken": str,
    },
    total=False,
)


class DeleteInventoryRequestTypeDef(
    _RequiredDeleteInventoryRequestTypeDef, _OptionalDeleteInventoryRequestTypeDef
):
    pass


DeleteInventoryResultResponseTypeDef = TypedDict(
    "DeleteInventoryResultResponseTypeDef",
    {
        "DeletionId": str,
        "TypeName": str,
        "DeletionSummary": "InventoryDeletionSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMaintenanceWindowRequestTypeDef = TypedDict(
    "DeleteMaintenanceWindowRequestTypeDef",
    {
        "WindowId": str,
    },
)

DeleteMaintenanceWindowResultResponseTypeDef = TypedDict(
    "DeleteMaintenanceWindowResultResponseTypeDef",
    {
        "WindowId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteOpsMetadataRequestTypeDef = TypedDict(
    "DeleteOpsMetadataRequestTypeDef",
    {
        "OpsMetadataArn": str,
    },
)

DeleteParameterRequestTypeDef = TypedDict(
    "DeleteParameterRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteParametersRequestTypeDef = TypedDict(
    "DeleteParametersRequestTypeDef",
    {
        "Names": List[str],
    },
)

DeleteParametersResultResponseTypeDef = TypedDict(
    "DeleteParametersResultResponseTypeDef",
    {
        "DeletedParameters": List[str],
        "InvalidParameters": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePatchBaselineRequestTypeDef = TypedDict(
    "DeletePatchBaselineRequestTypeDef",
    {
        "BaselineId": str,
    },
)

DeletePatchBaselineResultResponseTypeDef = TypedDict(
    "DeletePatchBaselineResultResponseTypeDef",
    {
        "BaselineId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteResourceDataSyncRequestTypeDef = TypedDict(
    "_RequiredDeleteResourceDataSyncRequestTypeDef",
    {
        "SyncName": str,
    },
)
_OptionalDeleteResourceDataSyncRequestTypeDef = TypedDict(
    "_OptionalDeleteResourceDataSyncRequestTypeDef",
    {
        "SyncType": str,
    },
    total=False,
)


class DeleteResourceDataSyncRequestTypeDef(
    _RequiredDeleteResourceDataSyncRequestTypeDef, _OptionalDeleteResourceDataSyncRequestTypeDef
):
    pass


DeregisterManagedInstanceRequestTypeDef = TypedDict(
    "DeregisterManagedInstanceRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DeregisterPatchBaselineForPatchGroupRequestTypeDef = TypedDict(
    "DeregisterPatchBaselineForPatchGroupRequestTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
    },
)

DeregisterPatchBaselineForPatchGroupResultResponseTypeDef = TypedDict(
    "DeregisterPatchBaselineForPatchGroupResultResponseTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeregisterTargetFromMaintenanceWindowRequestTypeDef = TypedDict(
    "_RequiredDeregisterTargetFromMaintenanceWindowRequestTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
    },
)
_OptionalDeregisterTargetFromMaintenanceWindowRequestTypeDef = TypedDict(
    "_OptionalDeregisterTargetFromMaintenanceWindowRequestTypeDef",
    {
        "Safe": bool,
    },
    total=False,
)


class DeregisterTargetFromMaintenanceWindowRequestTypeDef(
    _RequiredDeregisterTargetFromMaintenanceWindowRequestTypeDef,
    _OptionalDeregisterTargetFromMaintenanceWindowRequestTypeDef,
):
    pass


DeregisterTargetFromMaintenanceWindowResultResponseTypeDef = TypedDict(
    "DeregisterTargetFromMaintenanceWindowResultResponseTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterTaskFromMaintenanceWindowRequestTypeDef = TypedDict(
    "DeregisterTaskFromMaintenanceWindowRequestTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
    },
)

DeregisterTaskFromMaintenanceWindowResultResponseTypeDef = TypedDict(
    "DeregisterTaskFromMaintenanceWindowResultResponseTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeActivationsFilterTypeDef = TypedDict(
    "DescribeActivationsFilterTypeDef",
    {
        "FilterKey": DescribeActivationsFilterKeysType,
        "FilterValues": List[str],
    },
    total=False,
)

DescribeActivationsRequestTypeDef = TypedDict(
    "DescribeActivationsRequestTypeDef",
    {
        "Filters": List["DescribeActivationsFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeActivationsResultResponseTypeDef = TypedDict(
    "DescribeActivationsResultResponseTypeDef",
    {
        "ActivationList": List["ActivationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAssociationExecutionTargetsRequestTypeDef = TypedDict(
    "_RequiredDescribeAssociationExecutionTargetsRequestTypeDef",
    {
        "AssociationId": str,
        "ExecutionId": str,
    },
)
_OptionalDescribeAssociationExecutionTargetsRequestTypeDef = TypedDict(
    "_OptionalDescribeAssociationExecutionTargetsRequestTypeDef",
    {
        "Filters": List["AssociationExecutionTargetsFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeAssociationExecutionTargetsRequestTypeDef(
    _RequiredDescribeAssociationExecutionTargetsRequestTypeDef,
    _OptionalDescribeAssociationExecutionTargetsRequestTypeDef,
):
    pass


DescribeAssociationExecutionTargetsResultResponseTypeDef = TypedDict(
    "DescribeAssociationExecutionTargetsResultResponseTypeDef",
    {
        "AssociationExecutionTargets": List["AssociationExecutionTargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAssociationExecutionsRequestTypeDef = TypedDict(
    "_RequiredDescribeAssociationExecutionsRequestTypeDef",
    {
        "AssociationId": str,
    },
)
_OptionalDescribeAssociationExecutionsRequestTypeDef = TypedDict(
    "_OptionalDescribeAssociationExecutionsRequestTypeDef",
    {
        "Filters": List["AssociationExecutionFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeAssociationExecutionsRequestTypeDef(
    _RequiredDescribeAssociationExecutionsRequestTypeDef,
    _OptionalDescribeAssociationExecutionsRequestTypeDef,
):
    pass


DescribeAssociationExecutionsResultResponseTypeDef = TypedDict(
    "DescribeAssociationExecutionsResultResponseTypeDef",
    {
        "AssociationExecutions": List["AssociationExecutionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssociationRequestTypeDef = TypedDict(
    "DescribeAssociationRequestTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationId": str,
        "AssociationVersion": str,
    },
    total=False,
)

DescribeAssociationResultResponseTypeDef = TypedDict(
    "DescribeAssociationResultResponseTypeDef",
    {
        "AssociationDescription": "AssociationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAutomationExecutionsRequestTypeDef = TypedDict(
    "DescribeAutomationExecutionsRequestTypeDef",
    {
        "Filters": List["AutomationExecutionFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeAutomationExecutionsResultResponseTypeDef = TypedDict(
    "DescribeAutomationExecutionsResultResponseTypeDef",
    {
        "AutomationExecutionMetadataList": List["AutomationExecutionMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAutomationStepExecutionsRequestTypeDef = TypedDict(
    "_RequiredDescribeAutomationStepExecutionsRequestTypeDef",
    {
        "AutomationExecutionId": str,
    },
)
_OptionalDescribeAutomationStepExecutionsRequestTypeDef = TypedDict(
    "_OptionalDescribeAutomationStepExecutionsRequestTypeDef",
    {
        "Filters": List["StepExecutionFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
        "ReverseOrder": bool,
    },
    total=False,
)


class DescribeAutomationStepExecutionsRequestTypeDef(
    _RequiredDescribeAutomationStepExecutionsRequestTypeDef,
    _OptionalDescribeAutomationStepExecutionsRequestTypeDef,
):
    pass


DescribeAutomationStepExecutionsResultResponseTypeDef = TypedDict(
    "DescribeAutomationStepExecutionsResultResponseTypeDef",
    {
        "StepExecutions": List["StepExecutionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAvailablePatchesRequestTypeDef = TypedDict(
    "DescribeAvailablePatchesRequestTypeDef",
    {
        "Filters": List["PatchOrchestratorFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeAvailablePatchesResultResponseTypeDef = TypedDict(
    "DescribeAvailablePatchesResultResponseTypeDef",
    {
        "Patches": List["PatchTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDocumentPermissionRequestTypeDef = TypedDict(
    "_RequiredDescribeDocumentPermissionRequestTypeDef",
    {
        "Name": str,
        "PermissionType": Literal["Share"],
    },
)
_OptionalDescribeDocumentPermissionRequestTypeDef = TypedDict(
    "_OptionalDescribeDocumentPermissionRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeDocumentPermissionRequestTypeDef(
    _RequiredDescribeDocumentPermissionRequestTypeDef,
    _OptionalDescribeDocumentPermissionRequestTypeDef,
):
    pass


DescribeDocumentPermissionResponseResponseTypeDef = TypedDict(
    "DescribeDocumentPermissionResponseResponseTypeDef",
    {
        "AccountIds": List[str],
        "AccountSharingInfoList": List["AccountSharingInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDocumentRequestTypeDef = TypedDict(
    "_RequiredDescribeDocumentRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDescribeDocumentRequestTypeDef = TypedDict(
    "_OptionalDescribeDocumentRequestTypeDef",
    {
        "DocumentVersion": str,
        "VersionName": str,
    },
    total=False,
)


class DescribeDocumentRequestTypeDef(
    _RequiredDescribeDocumentRequestTypeDef, _OptionalDescribeDocumentRequestTypeDef
):
    pass


DescribeDocumentResultResponseTypeDef = TypedDict(
    "DescribeDocumentResultResponseTypeDef",
    {
        "Document": "DocumentDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEffectiveInstanceAssociationsRequestTypeDef = TypedDict(
    "_RequiredDescribeEffectiveInstanceAssociationsRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalDescribeEffectiveInstanceAssociationsRequestTypeDef = TypedDict(
    "_OptionalDescribeEffectiveInstanceAssociationsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeEffectiveInstanceAssociationsRequestTypeDef(
    _RequiredDescribeEffectiveInstanceAssociationsRequestTypeDef,
    _OptionalDescribeEffectiveInstanceAssociationsRequestTypeDef,
):
    pass


DescribeEffectiveInstanceAssociationsResultResponseTypeDef = TypedDict(
    "DescribeEffectiveInstanceAssociationsResultResponseTypeDef",
    {
        "Associations": List["InstanceAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEffectivePatchesForPatchBaselineRequestTypeDef = TypedDict(
    "_RequiredDescribeEffectivePatchesForPatchBaselineRequestTypeDef",
    {
        "BaselineId": str,
    },
)
_OptionalDescribeEffectivePatchesForPatchBaselineRequestTypeDef = TypedDict(
    "_OptionalDescribeEffectivePatchesForPatchBaselineRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeEffectivePatchesForPatchBaselineRequestTypeDef(
    _RequiredDescribeEffectivePatchesForPatchBaselineRequestTypeDef,
    _OptionalDescribeEffectivePatchesForPatchBaselineRequestTypeDef,
):
    pass


DescribeEffectivePatchesForPatchBaselineResultResponseTypeDef = TypedDict(
    "DescribeEffectivePatchesForPatchBaselineResultResponseTypeDef",
    {
        "EffectivePatches": List["EffectivePatchTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeInstanceAssociationsStatusRequestTypeDef = TypedDict(
    "_RequiredDescribeInstanceAssociationsStatusRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalDescribeInstanceAssociationsStatusRequestTypeDef = TypedDict(
    "_OptionalDescribeInstanceAssociationsStatusRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeInstanceAssociationsStatusRequestTypeDef(
    _RequiredDescribeInstanceAssociationsStatusRequestTypeDef,
    _OptionalDescribeInstanceAssociationsStatusRequestTypeDef,
):
    pass


DescribeInstanceAssociationsStatusResultResponseTypeDef = TypedDict(
    "DescribeInstanceAssociationsStatusResultResponseTypeDef",
    {
        "InstanceAssociationStatusInfos": List["InstanceAssociationStatusInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceInformationRequestTypeDef = TypedDict(
    "DescribeInstanceInformationRequestTypeDef",
    {
        "InstanceInformationFilterList": List["InstanceInformationFilterTypeDef"],
        "Filters": List["InstanceInformationStringFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeInstanceInformationResultResponseTypeDef = TypedDict(
    "DescribeInstanceInformationResultResponseTypeDef",
    {
        "InstanceInformationList": List["InstanceInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeInstancePatchStatesForPatchGroupRequestTypeDef = TypedDict(
    "_RequiredDescribeInstancePatchStatesForPatchGroupRequestTypeDef",
    {
        "PatchGroup": str,
    },
)
_OptionalDescribeInstancePatchStatesForPatchGroupRequestTypeDef = TypedDict(
    "_OptionalDescribeInstancePatchStatesForPatchGroupRequestTypeDef",
    {
        "Filters": List["InstancePatchStateFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class DescribeInstancePatchStatesForPatchGroupRequestTypeDef(
    _RequiredDescribeInstancePatchStatesForPatchGroupRequestTypeDef,
    _OptionalDescribeInstancePatchStatesForPatchGroupRequestTypeDef,
):
    pass


DescribeInstancePatchStatesForPatchGroupResultResponseTypeDef = TypedDict(
    "DescribeInstancePatchStatesForPatchGroupResultResponseTypeDef",
    {
        "InstancePatchStates": List["InstancePatchStateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeInstancePatchStatesRequestTypeDef = TypedDict(
    "_RequiredDescribeInstancePatchStatesRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
)
_OptionalDescribeInstancePatchStatesRequestTypeDef = TypedDict(
    "_OptionalDescribeInstancePatchStatesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class DescribeInstancePatchStatesRequestTypeDef(
    _RequiredDescribeInstancePatchStatesRequestTypeDef,
    _OptionalDescribeInstancePatchStatesRequestTypeDef,
):
    pass


DescribeInstancePatchStatesResultResponseTypeDef = TypedDict(
    "DescribeInstancePatchStatesResultResponseTypeDef",
    {
        "InstancePatchStates": List["InstancePatchStateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeInstancePatchesRequestTypeDef = TypedDict(
    "_RequiredDescribeInstancePatchesRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalDescribeInstancePatchesRequestTypeDef = TypedDict(
    "_OptionalDescribeInstancePatchesRequestTypeDef",
    {
        "Filters": List["PatchOrchestratorFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class DescribeInstancePatchesRequestTypeDef(
    _RequiredDescribeInstancePatchesRequestTypeDef, _OptionalDescribeInstancePatchesRequestTypeDef
):
    pass


DescribeInstancePatchesResultResponseTypeDef = TypedDict(
    "DescribeInstancePatchesResultResponseTypeDef",
    {
        "Patches": List["PatchComplianceDataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInventoryDeletionsRequestTypeDef = TypedDict(
    "DescribeInventoryDeletionsRequestTypeDef",
    {
        "DeletionId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeInventoryDeletionsResultResponseTypeDef = TypedDict(
    "DescribeInventoryDeletionsResultResponseTypeDef",
    {
        "InventoryDeletions": List["InventoryDeletionStatusItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMaintenanceWindowExecutionTaskInvocationsRequestTypeDef = TypedDict(
    "_RequiredDescribeMaintenanceWindowExecutionTaskInvocationsRequestTypeDef",
    {
        "WindowExecutionId": str,
        "TaskId": str,
    },
)
_OptionalDescribeMaintenanceWindowExecutionTaskInvocationsRequestTypeDef = TypedDict(
    "_OptionalDescribeMaintenanceWindowExecutionTaskInvocationsRequestTypeDef",
    {
        "Filters": List["MaintenanceWindowFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeMaintenanceWindowExecutionTaskInvocationsRequestTypeDef(
    _RequiredDescribeMaintenanceWindowExecutionTaskInvocationsRequestTypeDef,
    _OptionalDescribeMaintenanceWindowExecutionTaskInvocationsRequestTypeDef,
):
    pass


DescribeMaintenanceWindowExecutionTaskInvocationsResultResponseTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTaskInvocationsResultResponseTypeDef",
    {
        "WindowExecutionTaskInvocationIdentities": List[
            "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMaintenanceWindowExecutionTasksRequestTypeDef = TypedDict(
    "_RequiredDescribeMaintenanceWindowExecutionTasksRequestTypeDef",
    {
        "WindowExecutionId": str,
    },
)
_OptionalDescribeMaintenanceWindowExecutionTasksRequestTypeDef = TypedDict(
    "_OptionalDescribeMaintenanceWindowExecutionTasksRequestTypeDef",
    {
        "Filters": List["MaintenanceWindowFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeMaintenanceWindowExecutionTasksRequestTypeDef(
    _RequiredDescribeMaintenanceWindowExecutionTasksRequestTypeDef,
    _OptionalDescribeMaintenanceWindowExecutionTasksRequestTypeDef,
):
    pass


DescribeMaintenanceWindowExecutionTasksResultResponseTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTasksResultResponseTypeDef",
    {
        "WindowExecutionTaskIdentities": List["MaintenanceWindowExecutionTaskIdentityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMaintenanceWindowExecutionsRequestTypeDef = TypedDict(
    "_RequiredDescribeMaintenanceWindowExecutionsRequestTypeDef",
    {
        "WindowId": str,
    },
)
_OptionalDescribeMaintenanceWindowExecutionsRequestTypeDef = TypedDict(
    "_OptionalDescribeMaintenanceWindowExecutionsRequestTypeDef",
    {
        "Filters": List["MaintenanceWindowFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeMaintenanceWindowExecutionsRequestTypeDef(
    _RequiredDescribeMaintenanceWindowExecutionsRequestTypeDef,
    _OptionalDescribeMaintenanceWindowExecutionsRequestTypeDef,
):
    pass


DescribeMaintenanceWindowExecutionsResultResponseTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionsResultResponseTypeDef",
    {
        "WindowExecutions": List["MaintenanceWindowExecutionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMaintenanceWindowScheduleRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowScheduleRequestTypeDef",
    {
        "WindowId": str,
        "Targets": List["TargetTypeDef"],
        "ResourceType": MaintenanceWindowResourceTypeType,
        "Filters": List["PatchOrchestratorFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeMaintenanceWindowScheduleResultResponseTypeDef = TypedDict(
    "DescribeMaintenanceWindowScheduleResultResponseTypeDef",
    {
        "ScheduledWindowExecutions": List["ScheduledWindowExecutionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMaintenanceWindowTargetsRequestTypeDef = TypedDict(
    "_RequiredDescribeMaintenanceWindowTargetsRequestTypeDef",
    {
        "WindowId": str,
    },
)
_OptionalDescribeMaintenanceWindowTargetsRequestTypeDef = TypedDict(
    "_OptionalDescribeMaintenanceWindowTargetsRequestTypeDef",
    {
        "Filters": List["MaintenanceWindowFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeMaintenanceWindowTargetsRequestTypeDef(
    _RequiredDescribeMaintenanceWindowTargetsRequestTypeDef,
    _OptionalDescribeMaintenanceWindowTargetsRequestTypeDef,
):
    pass


DescribeMaintenanceWindowTargetsResultResponseTypeDef = TypedDict(
    "DescribeMaintenanceWindowTargetsResultResponseTypeDef",
    {
        "Targets": List["MaintenanceWindowTargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMaintenanceWindowTasksRequestTypeDef = TypedDict(
    "_RequiredDescribeMaintenanceWindowTasksRequestTypeDef",
    {
        "WindowId": str,
    },
)
_OptionalDescribeMaintenanceWindowTasksRequestTypeDef = TypedDict(
    "_OptionalDescribeMaintenanceWindowTasksRequestTypeDef",
    {
        "Filters": List["MaintenanceWindowFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeMaintenanceWindowTasksRequestTypeDef(
    _RequiredDescribeMaintenanceWindowTasksRequestTypeDef,
    _OptionalDescribeMaintenanceWindowTasksRequestTypeDef,
):
    pass


DescribeMaintenanceWindowTasksResultResponseTypeDef = TypedDict(
    "DescribeMaintenanceWindowTasksResultResponseTypeDef",
    {
        "Tasks": List["MaintenanceWindowTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMaintenanceWindowsForTargetRequestTypeDef = TypedDict(
    "_RequiredDescribeMaintenanceWindowsForTargetRequestTypeDef",
    {
        "Targets": List["TargetTypeDef"],
        "ResourceType": MaintenanceWindowResourceTypeType,
    },
)
_OptionalDescribeMaintenanceWindowsForTargetRequestTypeDef = TypedDict(
    "_OptionalDescribeMaintenanceWindowsForTargetRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeMaintenanceWindowsForTargetRequestTypeDef(
    _RequiredDescribeMaintenanceWindowsForTargetRequestTypeDef,
    _OptionalDescribeMaintenanceWindowsForTargetRequestTypeDef,
):
    pass


DescribeMaintenanceWindowsForTargetResultResponseTypeDef = TypedDict(
    "DescribeMaintenanceWindowsForTargetResultResponseTypeDef",
    {
        "WindowIdentities": List["MaintenanceWindowIdentityForTargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMaintenanceWindowsRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowsRequestTypeDef",
    {
        "Filters": List["MaintenanceWindowFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeMaintenanceWindowsResultResponseTypeDef = TypedDict(
    "DescribeMaintenanceWindowsResultResponseTypeDef",
    {
        "WindowIdentities": List["MaintenanceWindowIdentityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOpsItemsRequestTypeDef = TypedDict(
    "DescribeOpsItemsRequestTypeDef",
    {
        "OpsItemFilters": List["OpsItemFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeOpsItemsResponseResponseTypeDef = TypedDict(
    "DescribeOpsItemsResponseResponseTypeDef",
    {
        "NextToken": str,
        "OpsItemSummaries": List["OpsItemSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeParametersRequestTypeDef = TypedDict(
    "DescribeParametersRequestTypeDef",
    {
        "Filters": List["ParametersFilterTypeDef"],
        "ParameterFilters": List["ParameterStringFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeParametersResultResponseTypeDef = TypedDict(
    "DescribeParametersResultResponseTypeDef",
    {
        "Parameters": List["ParameterMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePatchBaselinesRequestTypeDef = TypedDict(
    "DescribePatchBaselinesRequestTypeDef",
    {
        "Filters": List["PatchOrchestratorFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribePatchBaselinesResultResponseTypeDef = TypedDict(
    "DescribePatchBaselinesResultResponseTypeDef",
    {
        "BaselineIdentities": List["PatchBaselineIdentityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePatchGroupStateRequestTypeDef = TypedDict(
    "DescribePatchGroupStateRequestTypeDef",
    {
        "PatchGroup": str,
    },
)

DescribePatchGroupStateResultResponseTypeDef = TypedDict(
    "DescribePatchGroupStateResultResponseTypeDef",
    {
        "Instances": int,
        "InstancesWithInstalledPatches": int,
        "InstancesWithInstalledOtherPatches": int,
        "InstancesWithInstalledPendingRebootPatches": int,
        "InstancesWithInstalledRejectedPatches": int,
        "InstancesWithMissingPatches": int,
        "InstancesWithFailedPatches": int,
        "InstancesWithNotApplicablePatches": int,
        "InstancesWithUnreportedNotApplicablePatches": int,
        "InstancesWithCriticalNonCompliantPatches": int,
        "InstancesWithSecurityNonCompliantPatches": int,
        "InstancesWithOtherNonCompliantPatches": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePatchGroupsRequestTypeDef = TypedDict(
    "DescribePatchGroupsRequestTypeDef",
    {
        "MaxResults": int,
        "Filters": List["PatchOrchestratorFilterTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribePatchGroupsResultResponseTypeDef = TypedDict(
    "DescribePatchGroupsResultResponseTypeDef",
    {
        "Mappings": List["PatchGroupPatchBaselineMappingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribePatchPropertiesRequestTypeDef = TypedDict(
    "_RequiredDescribePatchPropertiesRequestTypeDef",
    {
        "OperatingSystem": OperatingSystemType,
        "Property": PatchPropertyType,
    },
)
_OptionalDescribePatchPropertiesRequestTypeDef = TypedDict(
    "_OptionalDescribePatchPropertiesRequestTypeDef",
    {
        "PatchSet": PatchSetType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribePatchPropertiesRequestTypeDef(
    _RequiredDescribePatchPropertiesRequestTypeDef, _OptionalDescribePatchPropertiesRequestTypeDef
):
    pass


DescribePatchPropertiesResultResponseTypeDef = TypedDict(
    "DescribePatchPropertiesResultResponseTypeDef",
    {
        "Properties": List[Dict[str, str]],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSessionsRequestTypeDef = TypedDict(
    "_RequiredDescribeSessionsRequestTypeDef",
    {
        "State": SessionStateType,
    },
)
_OptionalDescribeSessionsRequestTypeDef = TypedDict(
    "_OptionalDescribeSessionsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["SessionFilterTypeDef"],
    },
    total=False,
)


class DescribeSessionsRequestTypeDef(
    _RequiredDescribeSessionsRequestTypeDef, _OptionalDescribeSessionsRequestTypeDef
):
    pass


DescribeSessionsResponseResponseTypeDef = TypedDict(
    "DescribeSessionsResponseResponseTypeDef",
    {
        "Sessions": List["SessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateOpsItemRelatedItemRequestTypeDef = TypedDict(
    "DisassociateOpsItemRelatedItemRequestTypeDef",
    {
        "OpsItemId": str,
        "AssociationId": str,
    },
)

DocumentDefaultVersionDescriptionTypeDef = TypedDict(
    "DocumentDefaultVersionDescriptionTypeDef",
    {
        "Name": str,
        "DefaultVersion": str,
        "DefaultVersionName": str,
    },
    total=False,
)

DocumentDescriptionTypeDef = TypedDict(
    "DocumentDescriptionTypeDef",
    {
        "Sha1": str,
        "Hash": str,
        "HashType": DocumentHashTypeType,
        "Name": str,
        "DisplayName": str,
        "VersionName": str,
        "Owner": str,
        "CreatedDate": datetime,
        "Status": DocumentStatusType,
        "StatusInformation": str,
        "DocumentVersion": str,
        "Description": str,
        "Parameters": List["DocumentParameterTypeDef"],
        "PlatformTypes": List[PlatformTypeType],
        "DocumentType": DocumentTypeType,
        "SchemaVersion": str,
        "LatestVersion": str,
        "DefaultVersion": str,
        "DocumentFormat": DocumentFormatType,
        "TargetType": str,
        "Tags": List["TagTypeDef"],
        "AttachmentsInformation": List["AttachmentInformationTypeDef"],
        "Requires": List["DocumentRequiresTypeDef"],
        "Author": str,
        "ReviewInformation": List["ReviewInformationTypeDef"],
        "ApprovedVersion": str,
        "PendingReviewVersion": str,
        "ReviewStatus": ReviewStatusType,
    },
    total=False,
)

DocumentFilterTypeDef = TypedDict(
    "DocumentFilterTypeDef",
    {
        "key": DocumentFilterKeyType,
        "value": str,
    },
)

DocumentIdentifierTypeDef = TypedDict(
    "DocumentIdentifierTypeDef",
    {
        "Name": str,
        "CreatedDate": datetime,
        "DisplayName": str,
        "Owner": str,
        "VersionName": str,
        "PlatformTypes": List[PlatformTypeType],
        "DocumentVersion": str,
        "DocumentType": DocumentTypeType,
        "SchemaVersion": str,
        "DocumentFormat": DocumentFormatType,
        "TargetType": str,
        "Tags": List["TagTypeDef"],
        "Requires": List["DocumentRequiresTypeDef"],
        "ReviewStatus": ReviewStatusType,
        "Author": str,
    },
    total=False,
)

DocumentKeyValuesFilterTypeDef = TypedDict(
    "DocumentKeyValuesFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
    total=False,
)

DocumentMetadataResponseInfoTypeDef = TypedDict(
    "DocumentMetadataResponseInfoTypeDef",
    {
        "ReviewerResponse": List["DocumentReviewerResponseSourceTypeDef"],
    },
    total=False,
)

DocumentParameterTypeDef = TypedDict(
    "DocumentParameterTypeDef",
    {
        "Name": str,
        "Type": DocumentParameterTypeType,
        "Description": str,
        "DefaultValue": str,
    },
    total=False,
)

_RequiredDocumentRequiresTypeDef = TypedDict(
    "_RequiredDocumentRequiresTypeDef",
    {
        "Name": str,
    },
)
_OptionalDocumentRequiresTypeDef = TypedDict(
    "_OptionalDocumentRequiresTypeDef",
    {
        "Version": str,
    },
    total=False,
)


class DocumentRequiresTypeDef(_RequiredDocumentRequiresTypeDef, _OptionalDocumentRequiresTypeDef):
    pass


DocumentReviewCommentSourceTypeDef = TypedDict(
    "DocumentReviewCommentSourceTypeDef",
    {
        "Type": Literal["Comment"],
        "Content": str,
    },
    total=False,
)

DocumentReviewerResponseSourceTypeDef = TypedDict(
    "DocumentReviewerResponseSourceTypeDef",
    {
        "CreateTime": datetime,
        "UpdatedTime": datetime,
        "ReviewStatus": ReviewStatusType,
        "Comment": List["DocumentReviewCommentSourceTypeDef"],
        "Reviewer": str,
    },
    total=False,
)

_RequiredDocumentReviewsTypeDef = TypedDict(
    "_RequiredDocumentReviewsTypeDef",
    {
        "Action": DocumentReviewActionType,
    },
)
_OptionalDocumentReviewsTypeDef = TypedDict(
    "_OptionalDocumentReviewsTypeDef",
    {
        "Comment": List["DocumentReviewCommentSourceTypeDef"],
    },
    total=False,
)


class DocumentReviewsTypeDef(_RequiredDocumentReviewsTypeDef, _OptionalDocumentReviewsTypeDef):
    pass


DocumentVersionInfoTypeDef = TypedDict(
    "DocumentVersionInfoTypeDef",
    {
        "Name": str,
        "DisplayName": str,
        "DocumentVersion": str,
        "VersionName": str,
        "CreatedDate": datetime,
        "IsDefaultVersion": bool,
        "DocumentFormat": DocumentFormatType,
        "Status": DocumentStatusType,
        "StatusInformation": str,
        "ReviewStatus": ReviewStatusType,
    },
    total=False,
)

EffectivePatchTypeDef = TypedDict(
    "EffectivePatchTypeDef",
    {
        "Patch": "PatchTypeDef",
        "PatchStatus": "PatchStatusTypeDef",
    },
    total=False,
)

FailedCreateAssociationTypeDef = TypedDict(
    "FailedCreateAssociationTypeDef",
    {
        "Entry": "CreateAssociationBatchRequestEntryTypeDef",
        "Message": str,
        "Fault": FaultType,
    },
    total=False,
)

FailureDetailsTypeDef = TypedDict(
    "FailureDetailsTypeDef",
    {
        "FailureStage": str,
        "FailureType": str,
        "Details": Dict[str, List[str]],
    },
    total=False,
)

GetAutomationExecutionRequestTypeDef = TypedDict(
    "GetAutomationExecutionRequestTypeDef",
    {
        "AutomationExecutionId": str,
    },
)

GetAutomationExecutionResultResponseTypeDef = TypedDict(
    "GetAutomationExecutionResultResponseTypeDef",
    {
        "AutomationExecution": "AutomationExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCalendarStateRequestTypeDef = TypedDict(
    "_RequiredGetCalendarStateRequestTypeDef",
    {
        "CalendarNames": List[str],
    },
)
_OptionalGetCalendarStateRequestTypeDef = TypedDict(
    "_OptionalGetCalendarStateRequestTypeDef",
    {
        "AtTime": str,
    },
    total=False,
)


class GetCalendarStateRequestTypeDef(
    _RequiredGetCalendarStateRequestTypeDef, _OptionalGetCalendarStateRequestTypeDef
):
    pass


GetCalendarStateResponseResponseTypeDef = TypedDict(
    "GetCalendarStateResponseResponseTypeDef",
    {
        "State": CalendarStateType,
        "AtTime": str,
        "NextTransitionTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCommandInvocationRequestTypeDef = TypedDict(
    "_RequiredGetCommandInvocationRequestTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
    },
)
_OptionalGetCommandInvocationRequestTypeDef = TypedDict(
    "_OptionalGetCommandInvocationRequestTypeDef",
    {
        "PluginName": str,
    },
    total=False,
)


class GetCommandInvocationRequestTypeDef(
    _RequiredGetCommandInvocationRequestTypeDef, _OptionalGetCommandInvocationRequestTypeDef
):
    pass


GetCommandInvocationResultResponseTypeDef = TypedDict(
    "GetCommandInvocationResultResponseTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "Comment": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "PluginName": str,
        "ResponseCode": int,
        "ExecutionStartDateTime": str,
        "ExecutionElapsedTime": str,
        "ExecutionEndDateTime": str,
        "Status": CommandInvocationStatusType,
        "StatusDetails": str,
        "StandardOutputContent": str,
        "StandardOutputUrl": str,
        "StandardErrorContent": str,
        "StandardErrorUrl": str,
        "CloudWatchOutputConfig": "CloudWatchOutputConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectionStatusRequestTypeDef = TypedDict(
    "GetConnectionStatusRequestTypeDef",
    {
        "Target": str,
    },
)

GetConnectionStatusResponseResponseTypeDef = TypedDict(
    "GetConnectionStatusResponseResponseTypeDef",
    {
        "Target": str,
        "Status": ConnectionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDefaultPatchBaselineRequestTypeDef = TypedDict(
    "GetDefaultPatchBaselineRequestTypeDef",
    {
        "OperatingSystem": OperatingSystemType,
    },
    total=False,
)

GetDefaultPatchBaselineResultResponseTypeDef = TypedDict(
    "GetDefaultPatchBaselineResultResponseTypeDef",
    {
        "BaselineId": str,
        "OperatingSystem": OperatingSystemType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDeployablePatchSnapshotForInstanceRequestTypeDef = TypedDict(
    "_RequiredGetDeployablePatchSnapshotForInstanceRequestTypeDef",
    {
        "InstanceId": str,
        "SnapshotId": str,
    },
)
_OptionalGetDeployablePatchSnapshotForInstanceRequestTypeDef = TypedDict(
    "_OptionalGetDeployablePatchSnapshotForInstanceRequestTypeDef",
    {
        "BaselineOverride": "BaselineOverrideTypeDef",
    },
    total=False,
)


class GetDeployablePatchSnapshotForInstanceRequestTypeDef(
    _RequiredGetDeployablePatchSnapshotForInstanceRequestTypeDef,
    _OptionalGetDeployablePatchSnapshotForInstanceRequestTypeDef,
):
    pass


GetDeployablePatchSnapshotForInstanceResultResponseTypeDef = TypedDict(
    "GetDeployablePatchSnapshotForInstanceResultResponseTypeDef",
    {
        "InstanceId": str,
        "SnapshotId": str,
        "SnapshotDownloadUrl": str,
        "Product": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDocumentRequestTypeDef = TypedDict(
    "_RequiredGetDocumentRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetDocumentRequestTypeDef = TypedDict(
    "_OptionalGetDocumentRequestTypeDef",
    {
        "VersionName": str,
        "DocumentVersion": str,
        "DocumentFormat": DocumentFormatType,
    },
    total=False,
)


class GetDocumentRequestTypeDef(
    _RequiredGetDocumentRequestTypeDef, _OptionalGetDocumentRequestTypeDef
):
    pass


GetDocumentResultResponseTypeDef = TypedDict(
    "GetDocumentResultResponseTypeDef",
    {
        "Name": str,
        "CreatedDate": datetime,
        "DisplayName": str,
        "VersionName": str,
        "DocumentVersion": str,
        "Status": DocumentStatusType,
        "StatusInformation": str,
        "Content": str,
        "DocumentType": DocumentTypeType,
        "DocumentFormat": DocumentFormatType,
        "Requires": List["DocumentRequiresTypeDef"],
        "AttachmentsContent": List["AttachmentContentTypeDef"],
        "ReviewStatus": ReviewStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInventoryRequestTypeDef = TypedDict(
    "GetInventoryRequestTypeDef",
    {
        "Filters": List["InventoryFilterTypeDef"],
        "Aggregators": List["InventoryAggregatorTypeDef"],
        "ResultAttributes": List["ResultAttributeTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetInventoryResultResponseTypeDef = TypedDict(
    "GetInventoryResultResponseTypeDef",
    {
        "Entities": List["InventoryResultEntityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInventorySchemaRequestTypeDef = TypedDict(
    "GetInventorySchemaRequestTypeDef",
    {
        "TypeName": str,
        "NextToken": str,
        "MaxResults": int,
        "Aggregator": bool,
        "SubType": bool,
    },
    total=False,
)

GetInventorySchemaResultResponseTypeDef = TypedDict(
    "GetInventorySchemaResultResponseTypeDef",
    {
        "Schemas": List["InventoryItemSchemaTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMaintenanceWindowExecutionRequestTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionRequestTypeDef",
    {
        "WindowExecutionId": str,
    },
)

GetMaintenanceWindowExecutionResultResponseTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionResultResponseTypeDef",
    {
        "WindowExecutionId": str,
        "TaskIds": List[str],
        "Status": MaintenanceWindowExecutionStatusType,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMaintenanceWindowExecutionTaskInvocationRequestTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskInvocationRequestTypeDef",
    {
        "WindowExecutionId": str,
        "TaskId": str,
        "InvocationId": str,
    },
)

GetMaintenanceWindowExecutionTaskInvocationResultResponseTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskInvocationResultResponseTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "InvocationId": str,
        "ExecutionId": str,
        "TaskType": MaintenanceWindowTaskTypeType,
        "Parameters": str,
        "Status": MaintenanceWindowExecutionStatusType,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "OwnerInformation": str,
        "WindowTargetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMaintenanceWindowExecutionTaskRequestTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskRequestTypeDef",
    {
        "WindowExecutionId": str,
        "TaskId": str,
    },
)

GetMaintenanceWindowExecutionTaskResultResponseTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskResultResponseTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "TaskArn": str,
        "ServiceRole": str,
        "Type": MaintenanceWindowTaskTypeType,
        "TaskParameters": List[Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"]],
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Status": MaintenanceWindowExecutionStatusType,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMaintenanceWindowRequestTypeDef = TypedDict(
    "GetMaintenanceWindowRequestTypeDef",
    {
        "WindowId": str,
    },
)

GetMaintenanceWindowResultResponseTypeDef = TypedDict(
    "GetMaintenanceWindowResultResponseTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "StartDate": str,
        "EndDate": str,
        "Schedule": str,
        "ScheduleTimezone": str,
        "ScheduleOffset": int,
        "NextExecutionTime": str,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
        "Enabled": bool,
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMaintenanceWindowTaskRequestTypeDef = TypedDict(
    "GetMaintenanceWindowTaskRequestTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
    },
)

GetMaintenanceWindowTaskResultResponseTypeDef = TypedDict(
    "GetMaintenanceWindowTaskResultResponseTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "Targets": List["TargetTypeDef"],
        "TaskArn": str,
        "ServiceRoleArn": str,
        "TaskType": MaintenanceWindowTaskTypeType,
        "TaskParameters": Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"],
        "TaskInvocationParameters": "MaintenanceWindowTaskInvocationParametersTypeDef",
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": "LoggingInfoTypeDef",
        "Name": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOpsItemRequestTypeDef = TypedDict(
    "GetOpsItemRequestTypeDef",
    {
        "OpsItemId": str,
    },
)

GetOpsItemResponseResponseTypeDef = TypedDict(
    "GetOpsItemResponseResponseTypeDef",
    {
        "OpsItem": "OpsItemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetOpsMetadataRequestTypeDef = TypedDict(
    "_RequiredGetOpsMetadataRequestTypeDef",
    {
        "OpsMetadataArn": str,
    },
)
_OptionalGetOpsMetadataRequestTypeDef = TypedDict(
    "_OptionalGetOpsMetadataRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetOpsMetadataRequestTypeDef(
    _RequiredGetOpsMetadataRequestTypeDef, _OptionalGetOpsMetadataRequestTypeDef
):
    pass


GetOpsMetadataResultResponseTypeDef = TypedDict(
    "GetOpsMetadataResultResponseTypeDef",
    {
        "ResourceId": str,
        "Metadata": Dict[str, "MetadataValueTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOpsSummaryRequestTypeDef = TypedDict(
    "GetOpsSummaryRequestTypeDef",
    {
        "SyncName": str,
        "Filters": List["OpsFilterTypeDef"],
        "Aggregators": List["OpsAggregatorTypeDef"],
        "ResultAttributes": List["OpsResultAttributeTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetOpsSummaryResultResponseTypeDef = TypedDict(
    "GetOpsSummaryResultResponseTypeDef",
    {
        "Entities": List["OpsEntityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetParameterHistoryRequestTypeDef = TypedDict(
    "_RequiredGetParameterHistoryRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetParameterHistoryRequestTypeDef = TypedDict(
    "_OptionalGetParameterHistoryRequestTypeDef",
    {
        "WithDecryption": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetParameterHistoryRequestTypeDef(
    _RequiredGetParameterHistoryRequestTypeDef, _OptionalGetParameterHistoryRequestTypeDef
):
    pass


GetParameterHistoryResultResponseTypeDef = TypedDict(
    "GetParameterHistoryResultResponseTypeDef",
    {
        "Parameters": List["ParameterHistoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetParameterRequestTypeDef = TypedDict(
    "_RequiredGetParameterRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetParameterRequestTypeDef = TypedDict(
    "_OptionalGetParameterRequestTypeDef",
    {
        "WithDecryption": bool,
    },
    total=False,
)


class GetParameterRequestTypeDef(
    _RequiredGetParameterRequestTypeDef, _OptionalGetParameterRequestTypeDef
):
    pass


GetParameterResultResponseTypeDef = TypedDict(
    "GetParameterResultResponseTypeDef",
    {
        "Parameter": "ParameterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetParametersByPathRequestTypeDef = TypedDict(
    "_RequiredGetParametersByPathRequestTypeDef",
    {
        "Path": str,
    },
)
_OptionalGetParametersByPathRequestTypeDef = TypedDict(
    "_OptionalGetParametersByPathRequestTypeDef",
    {
        "Recursive": bool,
        "ParameterFilters": List["ParameterStringFilterTypeDef"],
        "WithDecryption": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetParametersByPathRequestTypeDef(
    _RequiredGetParametersByPathRequestTypeDef, _OptionalGetParametersByPathRequestTypeDef
):
    pass


GetParametersByPathResultResponseTypeDef = TypedDict(
    "GetParametersByPathResultResponseTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetParametersRequestTypeDef = TypedDict(
    "_RequiredGetParametersRequestTypeDef",
    {
        "Names": List[str],
    },
)
_OptionalGetParametersRequestTypeDef = TypedDict(
    "_OptionalGetParametersRequestTypeDef",
    {
        "WithDecryption": bool,
    },
    total=False,
)


class GetParametersRequestTypeDef(
    _RequiredGetParametersRequestTypeDef, _OptionalGetParametersRequestTypeDef
):
    pass


GetParametersResultResponseTypeDef = TypedDict(
    "GetParametersResultResponseTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "InvalidParameters": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPatchBaselineForPatchGroupRequestTypeDef = TypedDict(
    "_RequiredGetPatchBaselineForPatchGroupRequestTypeDef",
    {
        "PatchGroup": str,
    },
)
_OptionalGetPatchBaselineForPatchGroupRequestTypeDef = TypedDict(
    "_OptionalGetPatchBaselineForPatchGroupRequestTypeDef",
    {
        "OperatingSystem": OperatingSystemType,
    },
    total=False,
)


class GetPatchBaselineForPatchGroupRequestTypeDef(
    _RequiredGetPatchBaselineForPatchGroupRequestTypeDef,
    _OptionalGetPatchBaselineForPatchGroupRequestTypeDef,
):
    pass


GetPatchBaselineForPatchGroupResultResponseTypeDef = TypedDict(
    "GetPatchBaselineForPatchGroupResultResponseTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
        "OperatingSystem": OperatingSystemType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPatchBaselineRequestTypeDef = TypedDict(
    "GetPatchBaselineRequestTypeDef",
    {
        "BaselineId": str,
    },
)

GetPatchBaselineResultResponseTypeDef = TypedDict(
    "GetPatchBaselineResultResponseTypeDef",
    {
        "BaselineId": str,
        "Name": str,
        "OperatingSystem": OperatingSystemType,
        "GlobalFilters": "PatchFilterGroupTypeDef",
        "ApprovalRules": "PatchRuleGroupTypeDef",
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": PatchComplianceLevelType,
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": PatchActionType,
        "PatchGroups": List[str],
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "Description": str,
        "Sources": List["PatchSourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceSettingRequestTypeDef = TypedDict(
    "GetServiceSettingRequestTypeDef",
    {
        "SettingId": str,
    },
)

GetServiceSettingResultResponseTypeDef = TypedDict(
    "GetServiceSettingResultResponseTypeDef",
    {
        "ServiceSetting": "ServiceSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceAggregatedAssociationOverviewTypeDef = TypedDict(
    "InstanceAggregatedAssociationOverviewTypeDef",
    {
        "DetailedStatus": str,
        "InstanceAssociationStatusAggregatedCount": Dict[str, int],
    },
    total=False,
)

InstanceAssociationOutputLocationTypeDef = TypedDict(
    "InstanceAssociationOutputLocationTypeDef",
    {
        "S3Location": "S3OutputLocationTypeDef",
    },
    total=False,
)

InstanceAssociationOutputUrlTypeDef = TypedDict(
    "InstanceAssociationOutputUrlTypeDef",
    {
        "S3OutputUrl": "S3OutputUrlTypeDef",
    },
    total=False,
)

InstanceAssociationStatusInfoTypeDef = TypedDict(
    "InstanceAssociationStatusInfoTypeDef",
    {
        "AssociationId": str,
        "Name": str,
        "DocumentVersion": str,
        "AssociationVersion": str,
        "InstanceId": str,
        "ExecutionDate": datetime,
        "Status": str,
        "DetailedStatus": str,
        "ExecutionSummary": str,
        "ErrorCode": str,
        "OutputUrl": "InstanceAssociationOutputUrlTypeDef",
        "AssociationName": str,
    },
    total=False,
)

InstanceAssociationTypeDef = TypedDict(
    "InstanceAssociationTypeDef",
    {
        "AssociationId": str,
        "InstanceId": str,
        "Content": str,
        "AssociationVersion": str,
    },
    total=False,
)

InstanceInformationFilterTypeDef = TypedDict(
    "InstanceInformationFilterTypeDef",
    {
        "key": InstanceInformationFilterKeyType,
        "valueSet": List[str],
    },
)

InstanceInformationStringFilterTypeDef = TypedDict(
    "InstanceInformationStringFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
)

InstanceInformationTypeDef = TypedDict(
    "InstanceInformationTypeDef",
    {
        "InstanceId": str,
        "PingStatus": PingStatusType,
        "LastPingDateTime": datetime,
        "AgentVersion": str,
        "IsLatestVersion": bool,
        "PlatformType": PlatformTypeType,
        "PlatformName": str,
        "PlatformVersion": str,
        "ActivationId": str,
        "IamRole": str,
        "RegistrationDate": datetime,
        "ResourceType": ResourceTypeType,
        "Name": str,
        "IPAddress": str,
        "ComputerName": str,
        "AssociationStatus": str,
        "LastAssociationExecutionDate": datetime,
        "LastSuccessfulAssociationExecutionDate": datetime,
        "AssociationOverview": "InstanceAggregatedAssociationOverviewTypeDef",
    },
    total=False,
)

InstancePatchStateFilterTypeDef = TypedDict(
    "InstancePatchStateFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": InstancePatchStateOperatorTypeType,
    },
)

_RequiredInstancePatchStateTypeDef = TypedDict(
    "_RequiredInstancePatchStateTypeDef",
    {
        "InstanceId": str,
        "PatchGroup": str,
        "BaselineId": str,
        "OperationStartTime": datetime,
        "OperationEndTime": datetime,
        "Operation": PatchOperationTypeType,
    },
)
_OptionalInstancePatchStateTypeDef = TypedDict(
    "_OptionalInstancePatchStateTypeDef",
    {
        "SnapshotId": str,
        "InstallOverrideList": str,
        "OwnerInformation": str,
        "InstalledCount": int,
        "InstalledOtherCount": int,
        "InstalledPendingRebootCount": int,
        "InstalledRejectedCount": int,
        "MissingCount": int,
        "FailedCount": int,
        "UnreportedNotApplicableCount": int,
        "NotApplicableCount": int,
        "LastNoRebootInstallOperationTime": datetime,
        "RebootOption": RebootOptionType,
        "CriticalNonCompliantCount": int,
        "SecurityNonCompliantCount": int,
        "OtherNonCompliantCount": int,
    },
    total=False,
)


class InstancePatchStateTypeDef(
    _RequiredInstancePatchStateTypeDef, _OptionalInstancePatchStateTypeDef
):
    pass


InventoryAggregatorTypeDef = TypedDict(
    "InventoryAggregatorTypeDef",
    {
        "Expression": str,
        "Aggregators": List[Dict[str, Any]],
        "Groups": List["InventoryGroupTypeDef"],
    },
    total=False,
)

InventoryDeletionStatusItemTypeDef = TypedDict(
    "InventoryDeletionStatusItemTypeDef",
    {
        "DeletionId": str,
        "TypeName": str,
        "DeletionStartTime": datetime,
        "LastStatus": InventoryDeletionStatusType,
        "LastStatusMessage": str,
        "DeletionSummary": "InventoryDeletionSummaryTypeDef",
        "LastStatusUpdateTime": datetime,
    },
    total=False,
)

InventoryDeletionSummaryItemTypeDef = TypedDict(
    "InventoryDeletionSummaryItemTypeDef",
    {
        "Version": str,
        "Count": int,
        "RemainingCount": int,
    },
    total=False,
)

InventoryDeletionSummaryTypeDef = TypedDict(
    "InventoryDeletionSummaryTypeDef",
    {
        "TotalCount": int,
        "RemainingCount": int,
        "SummaryItems": List["InventoryDeletionSummaryItemTypeDef"],
    },
    total=False,
)

_RequiredInventoryFilterTypeDef = TypedDict(
    "_RequiredInventoryFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
)
_OptionalInventoryFilterTypeDef = TypedDict(
    "_OptionalInventoryFilterTypeDef",
    {
        "Type": InventoryQueryOperatorTypeType,
    },
    total=False,
)


class InventoryFilterTypeDef(_RequiredInventoryFilterTypeDef, _OptionalInventoryFilterTypeDef):
    pass


InventoryGroupTypeDef = TypedDict(
    "InventoryGroupTypeDef",
    {
        "Name": str,
        "Filters": List["InventoryFilterTypeDef"],
    },
)

InventoryItemAttributeTypeDef = TypedDict(
    "InventoryItemAttributeTypeDef",
    {
        "Name": str,
        "DataType": InventoryAttributeDataTypeType,
    },
)

_RequiredInventoryItemSchemaTypeDef = TypedDict(
    "_RequiredInventoryItemSchemaTypeDef",
    {
        "TypeName": str,
        "Attributes": List["InventoryItemAttributeTypeDef"],
    },
)
_OptionalInventoryItemSchemaTypeDef = TypedDict(
    "_OptionalInventoryItemSchemaTypeDef",
    {
        "Version": str,
        "DisplayName": str,
    },
    total=False,
)


class InventoryItemSchemaTypeDef(
    _RequiredInventoryItemSchemaTypeDef, _OptionalInventoryItemSchemaTypeDef
):
    pass


_RequiredInventoryItemTypeDef = TypedDict(
    "_RequiredInventoryItemTypeDef",
    {
        "TypeName": str,
        "SchemaVersion": str,
        "CaptureTime": str,
    },
)
_OptionalInventoryItemTypeDef = TypedDict(
    "_OptionalInventoryItemTypeDef",
    {
        "ContentHash": str,
        "Content": List[Dict[str, str]],
        "Context": Dict[str, str],
    },
    total=False,
)


class InventoryItemTypeDef(_RequiredInventoryItemTypeDef, _OptionalInventoryItemTypeDef):
    pass


InventoryResultEntityTypeDef = TypedDict(
    "InventoryResultEntityTypeDef",
    {
        "Id": str,
        "Data": Dict[str, "InventoryResultItemTypeDef"],
    },
    total=False,
)

_RequiredInventoryResultItemTypeDef = TypedDict(
    "_RequiredInventoryResultItemTypeDef",
    {
        "TypeName": str,
        "SchemaVersion": str,
        "Content": List[Dict[str, str]],
    },
)
_OptionalInventoryResultItemTypeDef = TypedDict(
    "_OptionalInventoryResultItemTypeDef",
    {
        "CaptureTime": str,
        "ContentHash": str,
    },
    total=False,
)


class InventoryResultItemTypeDef(
    _RequiredInventoryResultItemTypeDef, _OptionalInventoryResultItemTypeDef
):
    pass


_RequiredLabelParameterVersionRequestTypeDef = TypedDict(
    "_RequiredLabelParameterVersionRequestTypeDef",
    {
        "Name": str,
        "Labels": List[str],
    },
)
_OptionalLabelParameterVersionRequestTypeDef = TypedDict(
    "_OptionalLabelParameterVersionRequestTypeDef",
    {
        "ParameterVersion": int,
    },
    total=False,
)


class LabelParameterVersionRequestTypeDef(
    _RequiredLabelParameterVersionRequestTypeDef, _OptionalLabelParameterVersionRequestTypeDef
):
    pass


LabelParameterVersionResultResponseTypeDef = TypedDict(
    "LabelParameterVersionResultResponseTypeDef",
    {
        "InvalidLabels": List[str],
        "ParameterVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssociationVersionsRequestTypeDef = TypedDict(
    "_RequiredListAssociationVersionsRequestTypeDef",
    {
        "AssociationId": str,
    },
)
_OptionalListAssociationVersionsRequestTypeDef = TypedDict(
    "_OptionalListAssociationVersionsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListAssociationVersionsRequestTypeDef(
    _RequiredListAssociationVersionsRequestTypeDef, _OptionalListAssociationVersionsRequestTypeDef
):
    pass


ListAssociationVersionsResultResponseTypeDef = TypedDict(
    "ListAssociationVersionsResultResponseTypeDef",
    {
        "AssociationVersions": List["AssociationVersionInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssociationsRequestTypeDef = TypedDict(
    "ListAssociationsRequestTypeDef",
    {
        "AssociationFilterList": List["AssociationFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListAssociationsResultResponseTypeDef = TypedDict(
    "ListAssociationsResultResponseTypeDef",
    {
        "Associations": List["AssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCommandInvocationsRequestTypeDef = TypedDict(
    "ListCommandInvocationsRequestTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["CommandFilterTypeDef"],
        "Details": bool,
    },
    total=False,
)

ListCommandInvocationsResultResponseTypeDef = TypedDict(
    "ListCommandInvocationsResultResponseTypeDef",
    {
        "CommandInvocations": List["CommandInvocationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCommandsRequestTypeDef = TypedDict(
    "ListCommandsRequestTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["CommandFilterTypeDef"],
    },
    total=False,
)

ListCommandsResultResponseTypeDef = TypedDict(
    "ListCommandsResultResponseTypeDef",
    {
        "Commands": List["CommandTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListComplianceItemsRequestTypeDef = TypedDict(
    "ListComplianceItemsRequestTypeDef",
    {
        "Filters": List["ComplianceStringFilterTypeDef"],
        "ResourceIds": List[str],
        "ResourceTypes": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListComplianceItemsResultResponseTypeDef = TypedDict(
    "ListComplianceItemsResultResponseTypeDef",
    {
        "ComplianceItems": List["ComplianceItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListComplianceSummariesRequestTypeDef = TypedDict(
    "ListComplianceSummariesRequestTypeDef",
    {
        "Filters": List["ComplianceStringFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListComplianceSummariesResultResponseTypeDef = TypedDict(
    "ListComplianceSummariesResultResponseTypeDef",
    {
        "ComplianceSummaryItems": List["ComplianceSummaryItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDocumentMetadataHistoryRequestTypeDef = TypedDict(
    "_RequiredListDocumentMetadataHistoryRequestTypeDef",
    {
        "Name": str,
        "Metadata": Literal["DocumentReviews"],
    },
)
_OptionalListDocumentMetadataHistoryRequestTypeDef = TypedDict(
    "_OptionalListDocumentMetadataHistoryRequestTypeDef",
    {
        "DocumentVersion": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListDocumentMetadataHistoryRequestTypeDef(
    _RequiredListDocumentMetadataHistoryRequestTypeDef,
    _OptionalListDocumentMetadataHistoryRequestTypeDef,
):
    pass


ListDocumentMetadataHistoryResponseResponseTypeDef = TypedDict(
    "ListDocumentMetadataHistoryResponseResponseTypeDef",
    {
        "Name": str,
        "DocumentVersion": str,
        "Author": str,
        "Metadata": "DocumentMetadataResponseInfoTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDocumentVersionsRequestTypeDef = TypedDict(
    "_RequiredListDocumentVersionsRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalListDocumentVersionsRequestTypeDef = TypedDict(
    "_OptionalListDocumentVersionsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListDocumentVersionsRequestTypeDef(
    _RequiredListDocumentVersionsRequestTypeDef, _OptionalListDocumentVersionsRequestTypeDef
):
    pass


ListDocumentVersionsResultResponseTypeDef = TypedDict(
    "ListDocumentVersionsResultResponseTypeDef",
    {
        "DocumentVersions": List["DocumentVersionInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDocumentsRequestTypeDef = TypedDict(
    "ListDocumentsRequestTypeDef",
    {
        "DocumentFilterList": List["DocumentFilterTypeDef"],
        "Filters": List["DocumentKeyValuesFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListDocumentsResultResponseTypeDef = TypedDict(
    "ListDocumentsResultResponseTypeDef",
    {
        "DocumentIdentifiers": List["DocumentIdentifierTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInventoryEntriesRequestTypeDef = TypedDict(
    "_RequiredListInventoryEntriesRequestTypeDef",
    {
        "InstanceId": str,
        "TypeName": str,
    },
)
_OptionalListInventoryEntriesRequestTypeDef = TypedDict(
    "_OptionalListInventoryEntriesRequestTypeDef",
    {
        "Filters": List["InventoryFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListInventoryEntriesRequestTypeDef(
    _RequiredListInventoryEntriesRequestTypeDef, _OptionalListInventoryEntriesRequestTypeDef
):
    pass


ListInventoryEntriesResultResponseTypeDef = TypedDict(
    "ListInventoryEntriesResultResponseTypeDef",
    {
        "TypeName": str,
        "InstanceId": str,
        "SchemaVersion": str,
        "CaptureTime": str,
        "Entries": List[Dict[str, str]],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOpsItemEventsRequestTypeDef = TypedDict(
    "ListOpsItemEventsRequestTypeDef",
    {
        "Filters": List["OpsItemEventFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListOpsItemEventsResponseResponseTypeDef = TypedDict(
    "ListOpsItemEventsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Summaries": List["OpsItemEventSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOpsItemRelatedItemsRequestTypeDef = TypedDict(
    "ListOpsItemRelatedItemsRequestTypeDef",
    {
        "OpsItemId": str,
        "Filters": List["OpsItemRelatedItemsFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListOpsItemRelatedItemsResponseResponseTypeDef = TypedDict(
    "ListOpsItemRelatedItemsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Summaries": List["OpsItemRelatedItemSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOpsMetadataRequestTypeDef = TypedDict(
    "ListOpsMetadataRequestTypeDef",
    {
        "Filters": List["OpsMetadataFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListOpsMetadataResultResponseTypeDef = TypedDict(
    "ListOpsMetadataResultResponseTypeDef",
    {
        "OpsMetadataList": List["OpsMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceComplianceSummariesRequestTypeDef = TypedDict(
    "ListResourceComplianceSummariesRequestTypeDef",
    {
        "Filters": List["ComplianceStringFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListResourceComplianceSummariesResultResponseTypeDef = TypedDict(
    "ListResourceComplianceSummariesResultResponseTypeDef",
    {
        "ResourceComplianceSummaryItems": List["ResourceComplianceSummaryItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceDataSyncRequestTypeDef = TypedDict(
    "ListResourceDataSyncRequestTypeDef",
    {
        "SyncType": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListResourceDataSyncResultResponseTypeDef = TypedDict(
    "ListResourceDataSyncResultResponseTypeDef",
    {
        "ResourceDataSyncItems": List["ResourceDataSyncItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceType": ResourceTypeForTaggingType,
        "ResourceId": str,
    },
)

ListTagsForResourceResultResponseTypeDef = TypedDict(
    "ListTagsForResourceResultResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLoggingInfoTypeDef = TypedDict(
    "_RequiredLoggingInfoTypeDef",
    {
        "S3BucketName": str,
        "S3Region": str,
    },
)
_OptionalLoggingInfoTypeDef = TypedDict(
    "_OptionalLoggingInfoTypeDef",
    {
        "S3KeyPrefix": str,
    },
    total=False,
)


class LoggingInfoTypeDef(_RequiredLoggingInfoTypeDef, _OptionalLoggingInfoTypeDef):
    pass


MaintenanceWindowAutomationParametersTypeDef = TypedDict(
    "MaintenanceWindowAutomationParametersTypeDef",
    {
        "DocumentVersion": str,
        "Parameters": Dict[str, List[str]],
    },
    total=False,
)

MaintenanceWindowExecutionTaskIdentityTypeDef = TypedDict(
    "MaintenanceWindowExecutionTaskIdentityTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "Status": MaintenanceWindowExecutionStatusType,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "TaskArn": str,
        "TaskType": MaintenanceWindowTaskTypeType,
    },
    total=False,
)

MaintenanceWindowExecutionTaskInvocationIdentityTypeDef = TypedDict(
    "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "InvocationId": str,
        "ExecutionId": str,
        "TaskType": MaintenanceWindowTaskTypeType,
        "Parameters": str,
        "Status": MaintenanceWindowExecutionStatusType,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "OwnerInformation": str,
        "WindowTargetId": str,
    },
    total=False,
)

MaintenanceWindowExecutionTypeDef = TypedDict(
    "MaintenanceWindowExecutionTypeDef",
    {
        "WindowId": str,
        "WindowExecutionId": str,
        "Status": MaintenanceWindowExecutionStatusType,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

MaintenanceWindowFilterTypeDef = TypedDict(
    "MaintenanceWindowFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
    total=False,
)

MaintenanceWindowIdentityForTargetTypeDef = TypedDict(
    "MaintenanceWindowIdentityForTargetTypeDef",
    {
        "WindowId": str,
        "Name": str,
    },
    total=False,
)

MaintenanceWindowIdentityTypeDef = TypedDict(
    "MaintenanceWindowIdentityTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "Enabled": bool,
        "Duration": int,
        "Cutoff": int,
        "Schedule": str,
        "ScheduleTimezone": str,
        "ScheduleOffset": int,
        "EndDate": str,
        "StartDate": str,
        "NextExecutionTime": str,
    },
    total=False,
)

MaintenanceWindowLambdaParametersTypeDef = TypedDict(
    "MaintenanceWindowLambdaParametersTypeDef",
    {
        "ClientContext": str,
        "Qualifier": str,
        "Payload": bytes,
    },
    total=False,
)

MaintenanceWindowRunCommandParametersTypeDef = TypedDict(
    "MaintenanceWindowRunCommandParametersTypeDef",
    {
        "Comment": str,
        "CloudWatchOutputConfig": "CloudWatchOutputConfigTypeDef",
        "DocumentHash": str,
        "DocumentHashType": DocumentHashTypeType,
        "DocumentVersion": str,
        "NotificationConfig": "NotificationConfigTypeDef",
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "Parameters": Dict[str, List[str]],
        "ServiceRoleArn": str,
        "TimeoutSeconds": int,
    },
    total=False,
)

MaintenanceWindowStepFunctionsParametersTypeDef = TypedDict(
    "MaintenanceWindowStepFunctionsParametersTypeDef",
    {
        "Input": str,
        "Name": str,
    },
    total=False,
)

MaintenanceWindowTargetTypeDef = TypedDict(
    "MaintenanceWindowTargetTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "ResourceType": MaintenanceWindowResourceTypeType,
        "Targets": List["TargetTypeDef"],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

MaintenanceWindowTaskInvocationParametersTypeDef = TypedDict(
    "MaintenanceWindowTaskInvocationParametersTypeDef",
    {
        "RunCommand": "MaintenanceWindowRunCommandParametersTypeDef",
        "Automation": "MaintenanceWindowAutomationParametersTypeDef",
        "StepFunctions": "MaintenanceWindowStepFunctionsParametersTypeDef",
        "Lambda": "MaintenanceWindowLambdaParametersTypeDef",
    },
    total=False,
)

MaintenanceWindowTaskParameterValueExpressionTypeDef = TypedDict(
    "MaintenanceWindowTaskParameterValueExpressionTypeDef",
    {
        "Values": List[str],
    },
    total=False,
)

MaintenanceWindowTaskTypeDef = TypedDict(
    "MaintenanceWindowTaskTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "TaskArn": str,
        "Type": MaintenanceWindowTaskTypeType,
        "Targets": List["TargetTypeDef"],
        "TaskParameters": Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"],
        "Priority": int,
        "LoggingInfo": "LoggingInfoTypeDef",
        "ServiceRoleArn": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

MetadataValueTypeDef = TypedDict(
    "MetadataValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

_RequiredModifyDocumentPermissionRequestTypeDef = TypedDict(
    "_RequiredModifyDocumentPermissionRequestTypeDef",
    {
        "Name": str,
        "PermissionType": Literal["Share"],
    },
)
_OptionalModifyDocumentPermissionRequestTypeDef = TypedDict(
    "_OptionalModifyDocumentPermissionRequestTypeDef",
    {
        "AccountIdsToAdd": List[str],
        "AccountIdsToRemove": List[str],
        "SharedDocumentVersion": str,
    },
    total=False,
)


class ModifyDocumentPermissionRequestTypeDef(
    _RequiredModifyDocumentPermissionRequestTypeDef, _OptionalModifyDocumentPermissionRequestTypeDef
):
    pass


NonCompliantSummaryTypeDef = TypedDict(
    "NonCompliantSummaryTypeDef",
    {
        "NonCompliantCount": int,
        "SeveritySummary": "SeveritySummaryTypeDef",
    },
    total=False,
)

NotificationConfigTypeDef = TypedDict(
    "NotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[NotificationEventType],
        "NotificationType": NotificationTypeType,
    },
    total=False,
)

OpsAggregatorTypeDef = TypedDict(
    "OpsAggregatorTypeDef",
    {
        "AggregatorType": str,
        "TypeName": str,
        "AttributeName": str,
        "Values": Dict[str, str],
        "Filters": List["OpsFilterTypeDef"],
        "Aggregators": List[Dict[str, Any]],
    },
    total=False,
)

OpsEntityItemTypeDef = TypedDict(
    "OpsEntityItemTypeDef",
    {
        "CaptureTime": str,
        "Content": List[Dict[str, str]],
    },
    total=False,
)

OpsEntityTypeDef = TypedDict(
    "OpsEntityTypeDef",
    {
        "Id": str,
        "Data": Dict[str, "OpsEntityItemTypeDef"],
    },
    total=False,
)

_RequiredOpsFilterTypeDef = TypedDict(
    "_RequiredOpsFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
)
_OptionalOpsFilterTypeDef = TypedDict(
    "_OptionalOpsFilterTypeDef",
    {
        "Type": OpsFilterOperatorTypeType,
    },
    total=False,
)


class OpsFilterTypeDef(_RequiredOpsFilterTypeDef, _OptionalOpsFilterTypeDef):
    pass


OpsItemDataValueTypeDef = TypedDict(
    "OpsItemDataValueTypeDef",
    {
        "Value": str,
        "Type": OpsItemDataTypeType,
    },
    total=False,
)

OpsItemEventFilterTypeDef = TypedDict(
    "OpsItemEventFilterTypeDef",
    {
        "Key": Literal["OpsItemId"],
        "Values": List[str],
        "Operator": Literal["Equal"],
    },
)

OpsItemEventSummaryTypeDef = TypedDict(
    "OpsItemEventSummaryTypeDef",
    {
        "OpsItemId": str,
        "EventId": str,
        "Source": str,
        "DetailType": str,
        "Detail": str,
        "CreatedBy": "OpsItemIdentityTypeDef",
        "CreatedTime": datetime,
    },
    total=False,
)

OpsItemFilterTypeDef = TypedDict(
    "OpsItemFilterTypeDef",
    {
        "Key": OpsItemFilterKeyType,
        "Values": List[str],
        "Operator": OpsItemFilterOperatorType,
    },
)

OpsItemIdentityTypeDef = TypedDict(
    "OpsItemIdentityTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

OpsItemNotificationTypeDef = TypedDict(
    "OpsItemNotificationTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

OpsItemRelatedItemSummaryTypeDef = TypedDict(
    "OpsItemRelatedItemSummaryTypeDef",
    {
        "OpsItemId": str,
        "AssociationId": str,
        "ResourceType": str,
        "AssociationType": str,
        "ResourceUri": str,
        "CreatedBy": "OpsItemIdentityTypeDef",
        "CreatedTime": datetime,
        "LastModifiedBy": "OpsItemIdentityTypeDef",
        "LastModifiedTime": datetime,
    },
    total=False,
)

OpsItemRelatedItemsFilterTypeDef = TypedDict(
    "OpsItemRelatedItemsFilterTypeDef",
    {
        "Key": OpsItemRelatedItemsFilterKeyType,
        "Values": List[str],
        "Operator": Literal["Equal"],
    },
)

OpsItemSummaryTypeDef = TypedDict(
    "OpsItemSummaryTypeDef",
    {
        "CreatedBy": str,
        "CreatedTime": datetime,
        "LastModifiedBy": str,
        "LastModifiedTime": datetime,
        "Priority": int,
        "Source": str,
        "Status": OpsItemStatusType,
        "OpsItemId": str,
        "Title": str,
        "OperationalData": Dict[str, "OpsItemDataValueTypeDef"],
        "Category": str,
        "Severity": str,
        "OpsItemType": str,
        "ActualStartTime": datetime,
        "ActualEndTime": datetime,
        "PlannedStartTime": datetime,
        "PlannedEndTime": datetime,
    },
    total=False,
)

OpsItemTypeDef = TypedDict(
    "OpsItemTypeDef",
    {
        "CreatedBy": str,
        "OpsItemType": str,
        "CreatedTime": datetime,
        "Description": str,
        "LastModifiedBy": str,
        "LastModifiedTime": datetime,
        "Notifications": List["OpsItemNotificationTypeDef"],
        "Priority": int,
        "RelatedOpsItems": List["RelatedOpsItemTypeDef"],
        "Status": OpsItemStatusType,
        "OpsItemId": str,
        "Version": str,
        "Title": str,
        "Source": str,
        "OperationalData": Dict[str, "OpsItemDataValueTypeDef"],
        "Category": str,
        "Severity": str,
        "ActualStartTime": datetime,
        "ActualEndTime": datetime,
        "PlannedStartTime": datetime,
        "PlannedEndTime": datetime,
    },
    total=False,
)

OpsMetadataFilterTypeDef = TypedDict(
    "OpsMetadataFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
)

OpsMetadataTypeDef = TypedDict(
    "OpsMetadataTypeDef",
    {
        "ResourceId": str,
        "OpsMetadataArn": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "CreationDate": datetime,
    },
    total=False,
)

OpsResultAttributeTypeDef = TypedDict(
    "OpsResultAttributeTypeDef",
    {
        "TypeName": str,
    },
)

OutputSourceTypeDef = TypedDict(
    "OutputSourceTypeDef",
    {
        "OutputSourceId": str,
        "OutputSourceType": str,
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

ParameterHistoryTypeDef = TypedDict(
    "ParameterHistoryTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "Value": str,
        "AllowedPattern": str,
        "Version": int,
        "Labels": List[str],
        "Tier": ParameterTierType,
        "Policies": List["ParameterInlinePolicyTypeDef"],
        "DataType": str,
    },
    total=False,
)

ParameterInlinePolicyTypeDef = TypedDict(
    "ParameterInlinePolicyTypeDef",
    {
        "PolicyText": str,
        "PolicyType": str,
        "PolicyStatus": str,
    },
    total=False,
)

ParameterMetadataTypeDef = TypedDict(
    "ParameterMetadataTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "AllowedPattern": str,
        "Version": int,
        "Tier": ParameterTierType,
        "Policies": List["ParameterInlinePolicyTypeDef"],
        "DataType": str,
    },
    total=False,
)

_RequiredParameterStringFilterTypeDef = TypedDict(
    "_RequiredParameterStringFilterTypeDef",
    {
        "Key": str,
    },
)
_OptionalParameterStringFilterTypeDef = TypedDict(
    "_OptionalParameterStringFilterTypeDef",
    {
        "Option": str,
        "Values": List[str],
    },
    total=False,
)


class ParameterStringFilterTypeDef(
    _RequiredParameterStringFilterTypeDef, _OptionalParameterStringFilterTypeDef
):
    pass


ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
        "Value": str,
        "Version": int,
        "Selector": str,
        "SourceResult": str,
        "LastModifiedDate": datetime,
        "ARN": str,
        "DataType": str,
    },
    total=False,
)

ParametersFilterTypeDef = TypedDict(
    "ParametersFilterTypeDef",
    {
        "Key": ParametersFilterKeyType,
        "Values": List[str],
    },
)

PatchBaselineIdentityTypeDef = TypedDict(
    "PatchBaselineIdentityTypeDef",
    {
        "BaselineId": str,
        "BaselineName": str,
        "OperatingSystem": OperatingSystemType,
        "BaselineDescription": str,
        "DefaultBaseline": bool,
    },
    total=False,
)

_RequiredPatchComplianceDataTypeDef = TypedDict(
    "_RequiredPatchComplianceDataTypeDef",
    {
        "Title": str,
        "KBId": str,
        "Classification": str,
        "Severity": str,
        "State": PatchComplianceDataStateType,
        "InstalledTime": datetime,
    },
)
_OptionalPatchComplianceDataTypeDef = TypedDict(
    "_OptionalPatchComplianceDataTypeDef",
    {
        "CVEIds": str,
    },
    total=False,
)


class PatchComplianceDataTypeDef(
    _RequiredPatchComplianceDataTypeDef, _OptionalPatchComplianceDataTypeDef
):
    pass


PatchFilterGroupTypeDef = TypedDict(
    "PatchFilterGroupTypeDef",
    {
        "PatchFilters": List["PatchFilterTypeDef"],
    },
)

PatchFilterTypeDef = TypedDict(
    "PatchFilterTypeDef",
    {
        "Key": PatchFilterKeyType,
        "Values": List[str],
    },
)

PatchGroupPatchBaselineMappingTypeDef = TypedDict(
    "PatchGroupPatchBaselineMappingTypeDef",
    {
        "PatchGroup": str,
        "BaselineIdentity": "PatchBaselineIdentityTypeDef",
    },
    total=False,
)

PatchOrchestratorFilterTypeDef = TypedDict(
    "PatchOrchestratorFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
    total=False,
)

PatchRuleGroupTypeDef = TypedDict(
    "PatchRuleGroupTypeDef",
    {
        "PatchRules": List["PatchRuleTypeDef"],
    },
)

_RequiredPatchRuleTypeDef = TypedDict(
    "_RequiredPatchRuleTypeDef",
    {
        "PatchFilterGroup": "PatchFilterGroupTypeDef",
    },
)
_OptionalPatchRuleTypeDef = TypedDict(
    "_OptionalPatchRuleTypeDef",
    {
        "ComplianceLevel": PatchComplianceLevelType,
        "ApproveAfterDays": int,
        "ApproveUntilDate": str,
        "EnableNonSecurity": bool,
    },
    total=False,
)


class PatchRuleTypeDef(_RequiredPatchRuleTypeDef, _OptionalPatchRuleTypeDef):
    pass


PatchSourceTypeDef = TypedDict(
    "PatchSourceTypeDef",
    {
        "Name": str,
        "Products": List[str],
        "Configuration": str,
    },
)

PatchStatusTypeDef = TypedDict(
    "PatchStatusTypeDef",
    {
        "DeploymentStatus": PatchDeploymentStatusType,
        "ComplianceLevel": PatchComplianceLevelType,
        "ApprovalDate": datetime,
    },
    total=False,
)

PatchTypeDef = TypedDict(
    "PatchTypeDef",
    {
        "Id": str,
        "ReleaseDate": datetime,
        "Title": str,
        "Description": str,
        "ContentUrl": str,
        "Vendor": str,
        "ProductFamily": str,
        "Product": str,
        "Classification": str,
        "MsrcSeverity": str,
        "KbNumber": str,
        "MsrcNumber": str,
        "Language": str,
        "AdvisoryIds": List[str],
        "BugzillaIds": List[str],
        "CVEIds": List[str],
        "Name": str,
        "Epoch": int,
        "Version": str,
        "Release": str,
        "Arch": str,
        "Severity": str,
        "Repository": str,
    },
    total=False,
)

ProgressCountersTypeDef = TypedDict(
    "ProgressCountersTypeDef",
    {
        "TotalSteps": int,
        "SuccessSteps": int,
        "FailedSteps": int,
        "CancelledSteps": int,
        "TimedOutSteps": int,
    },
    total=False,
)

_RequiredPutComplianceItemsRequestTypeDef = TypedDict(
    "_RequiredPutComplianceItemsRequestTypeDef",
    {
        "ResourceId": str,
        "ResourceType": str,
        "ComplianceType": str,
        "ExecutionSummary": "ComplianceExecutionSummaryTypeDef",
        "Items": List["ComplianceItemEntryTypeDef"],
    },
)
_OptionalPutComplianceItemsRequestTypeDef = TypedDict(
    "_OptionalPutComplianceItemsRequestTypeDef",
    {
        "ItemContentHash": str,
        "UploadType": ComplianceUploadTypeType,
    },
    total=False,
)


class PutComplianceItemsRequestTypeDef(
    _RequiredPutComplianceItemsRequestTypeDef, _OptionalPutComplianceItemsRequestTypeDef
):
    pass


PutInventoryRequestTypeDef = TypedDict(
    "PutInventoryRequestTypeDef",
    {
        "InstanceId": str,
        "Items": List["InventoryItemTypeDef"],
    },
)

PutInventoryResultResponseTypeDef = TypedDict(
    "PutInventoryResultResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutParameterRequestTypeDef = TypedDict(
    "_RequiredPutParameterRequestTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
_OptionalPutParameterRequestTypeDef = TypedDict(
    "_OptionalPutParameterRequestTypeDef",
    {
        "Description": str,
        "Type": ParameterTypeType,
        "KeyId": str,
        "Overwrite": bool,
        "AllowedPattern": str,
        "Tags": List["TagTypeDef"],
        "Tier": ParameterTierType,
        "Policies": str,
        "DataType": str,
    },
    total=False,
)


class PutParameterRequestTypeDef(
    _RequiredPutParameterRequestTypeDef, _OptionalPutParameterRequestTypeDef
):
    pass


PutParameterResultResponseTypeDef = TypedDict(
    "PutParameterResultResponseTypeDef",
    {
        "Version": int,
        "Tier": ParameterTierType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterDefaultPatchBaselineRequestTypeDef = TypedDict(
    "RegisterDefaultPatchBaselineRequestTypeDef",
    {
        "BaselineId": str,
    },
)

RegisterDefaultPatchBaselineResultResponseTypeDef = TypedDict(
    "RegisterDefaultPatchBaselineResultResponseTypeDef",
    {
        "BaselineId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterPatchBaselineForPatchGroupRequestTypeDef = TypedDict(
    "RegisterPatchBaselineForPatchGroupRequestTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
    },
)

RegisterPatchBaselineForPatchGroupResultResponseTypeDef = TypedDict(
    "RegisterPatchBaselineForPatchGroupResultResponseTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterTargetWithMaintenanceWindowRequestTypeDef = TypedDict(
    "_RequiredRegisterTargetWithMaintenanceWindowRequestTypeDef",
    {
        "WindowId": str,
        "ResourceType": MaintenanceWindowResourceTypeType,
        "Targets": List["TargetTypeDef"],
    },
)
_OptionalRegisterTargetWithMaintenanceWindowRequestTypeDef = TypedDict(
    "_OptionalRegisterTargetWithMaintenanceWindowRequestTypeDef",
    {
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
        "ClientToken": str,
    },
    total=False,
)


class RegisterTargetWithMaintenanceWindowRequestTypeDef(
    _RequiredRegisterTargetWithMaintenanceWindowRequestTypeDef,
    _OptionalRegisterTargetWithMaintenanceWindowRequestTypeDef,
):
    pass


RegisterTargetWithMaintenanceWindowResultResponseTypeDef = TypedDict(
    "RegisterTargetWithMaintenanceWindowResultResponseTypeDef",
    {
        "WindowTargetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterTaskWithMaintenanceWindowRequestTypeDef = TypedDict(
    "_RequiredRegisterTaskWithMaintenanceWindowRequestTypeDef",
    {
        "WindowId": str,
        "TaskArn": str,
        "TaskType": MaintenanceWindowTaskTypeType,
    },
)
_OptionalRegisterTaskWithMaintenanceWindowRequestTypeDef = TypedDict(
    "_OptionalRegisterTaskWithMaintenanceWindowRequestTypeDef",
    {
        "Targets": List["TargetTypeDef"],
        "ServiceRoleArn": str,
        "TaskParameters": Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"],
        "TaskInvocationParameters": "MaintenanceWindowTaskInvocationParametersTypeDef",
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": "LoggingInfoTypeDef",
        "Name": str,
        "Description": str,
        "ClientToken": str,
    },
    total=False,
)


class RegisterTaskWithMaintenanceWindowRequestTypeDef(
    _RequiredRegisterTaskWithMaintenanceWindowRequestTypeDef,
    _OptionalRegisterTaskWithMaintenanceWindowRequestTypeDef,
):
    pass


RegisterTaskWithMaintenanceWindowResultResponseTypeDef = TypedDict(
    "RegisterTaskWithMaintenanceWindowResultResponseTypeDef",
    {
        "WindowTaskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RelatedOpsItemTypeDef = TypedDict(
    "RelatedOpsItemTypeDef",
    {
        "OpsItemId": str,
    },
)

RemoveTagsFromResourceRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceRequestTypeDef",
    {
        "ResourceType": ResourceTypeForTaggingType,
        "ResourceId": str,
        "TagKeys": List[str],
    },
)

ResetServiceSettingRequestTypeDef = TypedDict(
    "ResetServiceSettingRequestTypeDef",
    {
        "SettingId": str,
    },
)

ResetServiceSettingResultResponseTypeDef = TypedDict(
    "ResetServiceSettingResultResponseTypeDef",
    {
        "ServiceSetting": "ServiceSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolvedTargetsTypeDef = TypedDict(
    "ResolvedTargetsTypeDef",
    {
        "ParameterValues": List[str],
        "Truncated": bool,
    },
    total=False,
)

ResourceComplianceSummaryItemTypeDef = TypedDict(
    "ResourceComplianceSummaryItemTypeDef",
    {
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceId": str,
        "Status": ComplianceStatusType,
        "OverallSeverity": ComplianceSeverityType,
        "ExecutionSummary": "ComplianceExecutionSummaryTypeDef",
        "CompliantSummary": "CompliantSummaryTypeDef",
        "NonCompliantSummary": "NonCompliantSummaryTypeDef",
    },
    total=False,
)

_RequiredResourceDataSyncAwsOrganizationsSourceTypeDef = TypedDict(
    "_RequiredResourceDataSyncAwsOrganizationsSourceTypeDef",
    {
        "OrganizationSourceType": str,
    },
)
_OptionalResourceDataSyncAwsOrganizationsSourceTypeDef = TypedDict(
    "_OptionalResourceDataSyncAwsOrganizationsSourceTypeDef",
    {
        "OrganizationalUnits": List["ResourceDataSyncOrganizationalUnitTypeDef"],
    },
    total=False,
)


class ResourceDataSyncAwsOrganizationsSourceTypeDef(
    _RequiredResourceDataSyncAwsOrganizationsSourceTypeDef,
    _OptionalResourceDataSyncAwsOrganizationsSourceTypeDef,
):
    pass


ResourceDataSyncDestinationDataSharingTypeDef = TypedDict(
    "ResourceDataSyncDestinationDataSharingTypeDef",
    {
        "DestinationDataSharingType": str,
    },
    total=False,
)

ResourceDataSyncItemTypeDef = TypedDict(
    "ResourceDataSyncItemTypeDef",
    {
        "SyncName": str,
        "SyncType": str,
        "SyncSource": "ResourceDataSyncSourceWithStateTypeDef",
        "S3Destination": "ResourceDataSyncS3DestinationTypeDef",
        "LastSyncTime": datetime,
        "LastSuccessfulSyncTime": datetime,
        "SyncLastModifiedTime": datetime,
        "LastStatus": LastResourceDataSyncStatusType,
        "SyncCreatedTime": datetime,
        "LastSyncStatusMessage": str,
    },
    total=False,
)

ResourceDataSyncOrganizationalUnitTypeDef = TypedDict(
    "ResourceDataSyncOrganizationalUnitTypeDef",
    {
        "OrganizationalUnitId": str,
    },
    total=False,
)

_RequiredResourceDataSyncS3DestinationTypeDef = TypedDict(
    "_RequiredResourceDataSyncS3DestinationTypeDef",
    {
        "BucketName": str,
        "SyncFormat": Literal["JsonSerDe"],
        "Region": str,
    },
)
_OptionalResourceDataSyncS3DestinationTypeDef = TypedDict(
    "_OptionalResourceDataSyncS3DestinationTypeDef",
    {
        "Prefix": str,
        "AWSKMSKeyARN": str,
        "DestinationDataSharing": "ResourceDataSyncDestinationDataSharingTypeDef",
    },
    total=False,
)


class ResourceDataSyncS3DestinationTypeDef(
    _RequiredResourceDataSyncS3DestinationTypeDef, _OptionalResourceDataSyncS3DestinationTypeDef
):
    pass


_RequiredResourceDataSyncSourceTypeDef = TypedDict(
    "_RequiredResourceDataSyncSourceTypeDef",
    {
        "SourceType": str,
        "SourceRegions": List[str],
    },
)
_OptionalResourceDataSyncSourceTypeDef = TypedDict(
    "_OptionalResourceDataSyncSourceTypeDef",
    {
        "AwsOrganizationsSource": "ResourceDataSyncAwsOrganizationsSourceTypeDef",
        "IncludeFutureRegions": bool,
        "EnableAllOpsDataSources": bool,
    },
    total=False,
)


class ResourceDataSyncSourceTypeDef(
    _RequiredResourceDataSyncSourceTypeDef, _OptionalResourceDataSyncSourceTypeDef
):
    pass


ResourceDataSyncSourceWithStateTypeDef = TypedDict(
    "ResourceDataSyncSourceWithStateTypeDef",
    {
        "SourceType": str,
        "AwsOrganizationsSource": "ResourceDataSyncAwsOrganizationsSourceTypeDef",
        "SourceRegions": List[str],
        "IncludeFutureRegions": bool,
        "State": str,
        "EnableAllOpsDataSources": bool,
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

ResultAttributeTypeDef = TypedDict(
    "ResultAttributeTypeDef",
    {
        "TypeName": str,
    },
)

ResumeSessionRequestTypeDef = TypedDict(
    "ResumeSessionRequestTypeDef",
    {
        "SessionId": str,
    },
)

ResumeSessionResponseResponseTypeDef = TypedDict(
    "ResumeSessionResponseResponseTypeDef",
    {
        "SessionId": str,
        "TokenValue": str,
        "StreamUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReviewInformationTypeDef = TypedDict(
    "ReviewInformationTypeDef",
    {
        "ReviewedTime": datetime,
        "Status": ReviewStatusType,
        "Reviewer": str,
    },
    total=False,
)

_RequiredRunbookTypeDef = TypedDict(
    "_RequiredRunbookTypeDef",
    {
        "DocumentName": str,
    },
)
_OptionalRunbookTypeDef = TypedDict(
    "_OptionalRunbookTypeDef",
    {
        "DocumentVersion": str,
        "Parameters": Dict[str, List[str]],
        "TargetParameterName": str,
        "Targets": List["TargetTypeDef"],
        "MaxConcurrency": str,
        "MaxErrors": str,
        "TargetLocations": List["TargetLocationTypeDef"],
    },
    total=False,
)


class RunbookTypeDef(_RequiredRunbookTypeDef, _OptionalRunbookTypeDef):
    pass


S3OutputLocationTypeDef = TypedDict(
    "S3OutputLocationTypeDef",
    {
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
    },
    total=False,
)

S3OutputUrlTypeDef = TypedDict(
    "S3OutputUrlTypeDef",
    {
        "OutputUrl": str,
    },
    total=False,
)

ScheduledWindowExecutionTypeDef = TypedDict(
    "ScheduledWindowExecutionTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "ExecutionTime": str,
    },
    total=False,
)

_RequiredSendAutomationSignalRequestTypeDef = TypedDict(
    "_RequiredSendAutomationSignalRequestTypeDef",
    {
        "AutomationExecutionId": str,
        "SignalType": SignalTypeType,
    },
)
_OptionalSendAutomationSignalRequestTypeDef = TypedDict(
    "_OptionalSendAutomationSignalRequestTypeDef",
    {
        "Payload": Dict[str, List[str]],
    },
    total=False,
)


class SendAutomationSignalRequestTypeDef(
    _RequiredSendAutomationSignalRequestTypeDef, _OptionalSendAutomationSignalRequestTypeDef
):
    pass


_RequiredSendCommandRequestTypeDef = TypedDict(
    "_RequiredSendCommandRequestTypeDef",
    {
        "DocumentName": str,
    },
)
_OptionalSendCommandRequestTypeDef = TypedDict(
    "_OptionalSendCommandRequestTypeDef",
    {
        "InstanceIds": List[str],
        "Targets": List["TargetTypeDef"],
        "DocumentVersion": str,
        "DocumentHash": str,
        "DocumentHashType": DocumentHashTypeType,
        "TimeoutSeconds": int,
        "Comment": str,
        "Parameters": Dict[str, List[str]],
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "ServiceRoleArn": str,
        "NotificationConfig": "NotificationConfigTypeDef",
        "CloudWatchOutputConfig": "CloudWatchOutputConfigTypeDef",
    },
    total=False,
)


class SendCommandRequestTypeDef(
    _RequiredSendCommandRequestTypeDef, _OptionalSendCommandRequestTypeDef
):
    pass


SendCommandResultResponseTypeDef = TypedDict(
    "SendCommandResultResponseTypeDef",
    {
        "Command": "CommandTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceSettingTypeDef = TypedDict(
    "ServiceSettingTypeDef",
    {
        "SettingId": str,
        "SettingValue": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "ARN": str,
        "Status": str,
    },
    total=False,
)

SessionFilterTypeDef = TypedDict(
    "SessionFilterTypeDef",
    {
        "key": SessionFilterKeyType,
        "value": str,
    },
)

SessionManagerOutputUrlTypeDef = TypedDict(
    "SessionManagerOutputUrlTypeDef",
    {
        "S3OutputUrl": str,
        "CloudWatchOutputUrl": str,
    },
    total=False,
)

SessionTypeDef = TypedDict(
    "SessionTypeDef",
    {
        "SessionId": str,
        "Target": str,
        "Status": SessionStatusType,
        "StartDate": datetime,
        "EndDate": datetime,
        "DocumentName": str,
        "Owner": str,
        "Details": str,
        "OutputUrl": "SessionManagerOutputUrlTypeDef",
    },
    total=False,
)

SeveritySummaryTypeDef = TypedDict(
    "SeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)

StartAssociationsOnceRequestTypeDef = TypedDict(
    "StartAssociationsOnceRequestTypeDef",
    {
        "AssociationIds": List[str],
    },
)

_RequiredStartAutomationExecutionRequestTypeDef = TypedDict(
    "_RequiredStartAutomationExecutionRequestTypeDef",
    {
        "DocumentName": str,
    },
)
_OptionalStartAutomationExecutionRequestTypeDef = TypedDict(
    "_OptionalStartAutomationExecutionRequestTypeDef",
    {
        "DocumentVersion": str,
        "Parameters": Dict[str, List[str]],
        "ClientToken": str,
        "Mode": ExecutionModeType,
        "TargetParameterName": str,
        "Targets": List["TargetTypeDef"],
        "TargetMaps": List[Dict[str, List[str]]],
        "MaxConcurrency": str,
        "MaxErrors": str,
        "TargetLocations": List["TargetLocationTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class StartAutomationExecutionRequestTypeDef(
    _RequiredStartAutomationExecutionRequestTypeDef, _OptionalStartAutomationExecutionRequestTypeDef
):
    pass


StartAutomationExecutionResultResponseTypeDef = TypedDict(
    "StartAutomationExecutionResultResponseTypeDef",
    {
        "AutomationExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartChangeRequestExecutionRequestTypeDef = TypedDict(
    "_RequiredStartChangeRequestExecutionRequestTypeDef",
    {
        "DocumentName": str,
        "Runbooks": List["RunbookTypeDef"],
    },
)
_OptionalStartChangeRequestExecutionRequestTypeDef = TypedDict(
    "_OptionalStartChangeRequestExecutionRequestTypeDef",
    {
        "ScheduledTime": Union[datetime, str],
        "DocumentVersion": str,
        "Parameters": Dict[str, List[str]],
        "ChangeRequestName": str,
        "ClientToken": str,
        "Tags": List["TagTypeDef"],
        "ScheduledEndTime": Union[datetime, str],
        "ChangeDetails": str,
    },
    total=False,
)


class StartChangeRequestExecutionRequestTypeDef(
    _RequiredStartChangeRequestExecutionRequestTypeDef,
    _OptionalStartChangeRequestExecutionRequestTypeDef,
):
    pass


StartChangeRequestExecutionResultResponseTypeDef = TypedDict(
    "StartChangeRequestExecutionResultResponseTypeDef",
    {
        "AutomationExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartSessionRequestTypeDef = TypedDict(
    "_RequiredStartSessionRequestTypeDef",
    {
        "Target": str,
    },
)
_OptionalStartSessionRequestTypeDef = TypedDict(
    "_OptionalStartSessionRequestTypeDef",
    {
        "DocumentName": str,
        "Parameters": Dict[str, List[str]],
    },
    total=False,
)


class StartSessionRequestTypeDef(
    _RequiredStartSessionRequestTypeDef, _OptionalStartSessionRequestTypeDef
):
    pass


StartSessionResponseResponseTypeDef = TypedDict(
    "StartSessionResponseResponseTypeDef",
    {
        "SessionId": str,
        "TokenValue": str,
        "StreamUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StepExecutionFilterTypeDef = TypedDict(
    "StepExecutionFilterTypeDef",
    {
        "Key": StepExecutionFilterKeyType,
        "Values": List[str],
    },
)

StepExecutionTypeDef = TypedDict(
    "StepExecutionTypeDef",
    {
        "StepName": str,
        "Action": str,
        "TimeoutSeconds": int,
        "OnFailure": str,
        "MaxAttempts": int,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "StepStatus": AutomationExecutionStatusType,
        "ResponseCode": str,
        "Inputs": Dict[str, str],
        "Outputs": Dict[str, List[str]],
        "Response": str,
        "FailureMessage": str,
        "FailureDetails": "FailureDetailsTypeDef",
        "StepExecutionId": str,
        "OverriddenParameters": Dict[str, List[str]],
        "IsEnd": bool,
        "NextStep": str,
        "IsCritical": bool,
        "ValidNextSteps": List[str],
        "Targets": List["TargetTypeDef"],
        "TargetLocation": "TargetLocationTypeDef",
    },
    total=False,
)

_RequiredStopAutomationExecutionRequestTypeDef = TypedDict(
    "_RequiredStopAutomationExecutionRequestTypeDef",
    {
        "AutomationExecutionId": str,
    },
)
_OptionalStopAutomationExecutionRequestTypeDef = TypedDict(
    "_OptionalStopAutomationExecutionRequestTypeDef",
    {
        "Type": StopTypeType,
    },
    total=False,
)


class StopAutomationExecutionRequestTypeDef(
    _RequiredStopAutomationExecutionRequestTypeDef, _OptionalStopAutomationExecutionRequestTypeDef
):
    pass


TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TargetLocationTypeDef = TypedDict(
    "TargetLocationTypeDef",
    {
        "Accounts": List[str],
        "Regions": List[str],
        "TargetLocationMaxConcurrency": str,
        "TargetLocationMaxErrors": str,
        "ExecutionRoleName": str,
    },
    total=False,
)

TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
    total=False,
)

TerminateSessionRequestTypeDef = TypedDict(
    "TerminateSessionRequestTypeDef",
    {
        "SessionId": str,
    },
)

TerminateSessionResponseResponseTypeDef = TypedDict(
    "TerminateSessionResponseResponseTypeDef",
    {
        "SessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnlabelParameterVersionRequestTypeDef = TypedDict(
    "UnlabelParameterVersionRequestTypeDef",
    {
        "Name": str,
        "ParameterVersion": int,
        "Labels": List[str],
    },
)

UnlabelParameterVersionResultResponseTypeDef = TypedDict(
    "UnlabelParameterVersionResultResponseTypeDef",
    {
        "RemovedLabels": List[str],
        "InvalidLabels": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAssociationRequestTypeDef = TypedDict(
    "_RequiredUpdateAssociationRequestTypeDef",
    {
        "AssociationId": str,
    },
)
_OptionalUpdateAssociationRequestTypeDef = TypedDict(
    "_OptionalUpdateAssociationRequestTypeDef",
    {
        "Parameters": Dict[str, List[str]],
        "DocumentVersion": str,
        "ScheduleExpression": str,
        "OutputLocation": "InstanceAssociationOutputLocationTypeDef",
        "Name": str,
        "Targets": List["TargetTypeDef"],
        "AssociationName": str,
        "AssociationVersion": str,
        "AutomationTargetParameterName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": AssociationComplianceSeverityType,
        "SyncCompliance": AssociationSyncComplianceType,
        "ApplyOnlyAtCronInterval": bool,
        "CalendarNames": List[str],
        "TargetLocations": List["TargetLocationTypeDef"],
    },
    total=False,
)


class UpdateAssociationRequestTypeDef(
    _RequiredUpdateAssociationRequestTypeDef, _OptionalUpdateAssociationRequestTypeDef
):
    pass


UpdateAssociationResultResponseTypeDef = TypedDict(
    "UpdateAssociationResultResponseTypeDef",
    {
        "AssociationDescription": "AssociationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAssociationStatusRequestTypeDef = TypedDict(
    "UpdateAssociationStatusRequestTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationStatus": "AssociationStatusTypeDef",
    },
)

UpdateAssociationStatusResultResponseTypeDef = TypedDict(
    "UpdateAssociationStatusResultResponseTypeDef",
    {
        "AssociationDescription": "AssociationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDocumentDefaultVersionRequestTypeDef = TypedDict(
    "UpdateDocumentDefaultVersionRequestTypeDef",
    {
        "Name": str,
        "DocumentVersion": str,
    },
)

UpdateDocumentDefaultVersionResultResponseTypeDef = TypedDict(
    "UpdateDocumentDefaultVersionResultResponseTypeDef",
    {
        "Description": "DocumentDefaultVersionDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDocumentMetadataRequestTypeDef = TypedDict(
    "_RequiredUpdateDocumentMetadataRequestTypeDef",
    {
        "Name": str,
        "DocumentReviews": "DocumentReviewsTypeDef",
    },
)
_OptionalUpdateDocumentMetadataRequestTypeDef = TypedDict(
    "_OptionalUpdateDocumentMetadataRequestTypeDef",
    {
        "DocumentVersion": str,
    },
    total=False,
)


class UpdateDocumentMetadataRequestTypeDef(
    _RequiredUpdateDocumentMetadataRequestTypeDef, _OptionalUpdateDocumentMetadataRequestTypeDef
):
    pass


_RequiredUpdateDocumentRequestTypeDef = TypedDict(
    "_RequiredUpdateDocumentRequestTypeDef",
    {
        "Content": str,
        "Name": str,
    },
)
_OptionalUpdateDocumentRequestTypeDef = TypedDict(
    "_OptionalUpdateDocumentRequestTypeDef",
    {
        "Attachments": List["AttachmentsSourceTypeDef"],
        "DisplayName": str,
        "VersionName": str,
        "DocumentVersion": str,
        "DocumentFormat": DocumentFormatType,
        "TargetType": str,
    },
    total=False,
)


class UpdateDocumentRequestTypeDef(
    _RequiredUpdateDocumentRequestTypeDef, _OptionalUpdateDocumentRequestTypeDef
):
    pass


UpdateDocumentResultResponseTypeDef = TypedDict(
    "UpdateDocumentResultResponseTypeDef",
    {
        "DocumentDescription": "DocumentDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMaintenanceWindowRequestTypeDef = TypedDict(
    "_RequiredUpdateMaintenanceWindowRequestTypeDef",
    {
        "WindowId": str,
    },
)
_OptionalUpdateMaintenanceWindowRequestTypeDef = TypedDict(
    "_OptionalUpdateMaintenanceWindowRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "StartDate": str,
        "EndDate": str,
        "Schedule": str,
        "ScheduleTimezone": str,
        "ScheduleOffset": int,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
        "Enabled": bool,
        "Replace": bool,
    },
    total=False,
)


class UpdateMaintenanceWindowRequestTypeDef(
    _RequiredUpdateMaintenanceWindowRequestTypeDef, _OptionalUpdateMaintenanceWindowRequestTypeDef
):
    pass


UpdateMaintenanceWindowResultResponseTypeDef = TypedDict(
    "UpdateMaintenanceWindowResultResponseTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "StartDate": str,
        "EndDate": str,
        "Schedule": str,
        "ScheduleTimezone": str,
        "ScheduleOffset": int,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
        "Enabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMaintenanceWindowTargetRequestTypeDef = TypedDict(
    "_RequiredUpdateMaintenanceWindowTargetRequestTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
    },
)
_OptionalUpdateMaintenanceWindowTargetRequestTypeDef = TypedDict(
    "_OptionalUpdateMaintenanceWindowTargetRequestTypeDef",
    {
        "Targets": List["TargetTypeDef"],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
        "Replace": bool,
    },
    total=False,
)


class UpdateMaintenanceWindowTargetRequestTypeDef(
    _RequiredUpdateMaintenanceWindowTargetRequestTypeDef,
    _OptionalUpdateMaintenanceWindowTargetRequestTypeDef,
):
    pass


UpdateMaintenanceWindowTargetResultResponseTypeDef = TypedDict(
    "UpdateMaintenanceWindowTargetResultResponseTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "Targets": List["TargetTypeDef"],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMaintenanceWindowTaskRequestTypeDef = TypedDict(
    "_RequiredUpdateMaintenanceWindowTaskRequestTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
    },
)
_OptionalUpdateMaintenanceWindowTaskRequestTypeDef = TypedDict(
    "_OptionalUpdateMaintenanceWindowTaskRequestTypeDef",
    {
        "Targets": List["TargetTypeDef"],
        "TaskArn": str,
        "ServiceRoleArn": str,
        "TaskParameters": Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"],
        "TaskInvocationParameters": "MaintenanceWindowTaskInvocationParametersTypeDef",
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": "LoggingInfoTypeDef",
        "Name": str,
        "Description": str,
        "Replace": bool,
    },
    total=False,
)


class UpdateMaintenanceWindowTaskRequestTypeDef(
    _RequiredUpdateMaintenanceWindowTaskRequestTypeDef,
    _OptionalUpdateMaintenanceWindowTaskRequestTypeDef,
):
    pass


UpdateMaintenanceWindowTaskResultResponseTypeDef = TypedDict(
    "UpdateMaintenanceWindowTaskResultResponseTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "Targets": List["TargetTypeDef"],
        "TaskArn": str,
        "ServiceRoleArn": str,
        "TaskParameters": Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"],
        "TaskInvocationParameters": "MaintenanceWindowTaskInvocationParametersTypeDef",
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": "LoggingInfoTypeDef",
        "Name": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateManagedInstanceRoleRequestTypeDef = TypedDict(
    "UpdateManagedInstanceRoleRequestTypeDef",
    {
        "InstanceId": str,
        "IamRole": str,
    },
)

_RequiredUpdateOpsItemRequestTypeDef = TypedDict(
    "_RequiredUpdateOpsItemRequestTypeDef",
    {
        "OpsItemId": str,
    },
)
_OptionalUpdateOpsItemRequestTypeDef = TypedDict(
    "_OptionalUpdateOpsItemRequestTypeDef",
    {
        "Description": str,
        "OperationalData": Dict[str, "OpsItemDataValueTypeDef"],
        "OperationalDataToDelete": List[str],
        "Notifications": List["OpsItemNotificationTypeDef"],
        "Priority": int,
        "RelatedOpsItems": List["RelatedOpsItemTypeDef"],
        "Status": OpsItemStatusType,
        "Title": str,
        "Category": str,
        "Severity": str,
        "ActualStartTime": Union[datetime, str],
        "ActualEndTime": Union[datetime, str],
        "PlannedStartTime": Union[datetime, str],
        "PlannedEndTime": Union[datetime, str],
    },
    total=False,
)


class UpdateOpsItemRequestTypeDef(
    _RequiredUpdateOpsItemRequestTypeDef, _OptionalUpdateOpsItemRequestTypeDef
):
    pass


_RequiredUpdateOpsMetadataRequestTypeDef = TypedDict(
    "_RequiredUpdateOpsMetadataRequestTypeDef",
    {
        "OpsMetadataArn": str,
    },
)
_OptionalUpdateOpsMetadataRequestTypeDef = TypedDict(
    "_OptionalUpdateOpsMetadataRequestTypeDef",
    {
        "MetadataToUpdate": Dict[str, "MetadataValueTypeDef"],
        "KeysToDelete": List[str],
    },
    total=False,
)


class UpdateOpsMetadataRequestTypeDef(
    _RequiredUpdateOpsMetadataRequestTypeDef, _OptionalUpdateOpsMetadataRequestTypeDef
):
    pass


UpdateOpsMetadataResultResponseTypeDef = TypedDict(
    "UpdateOpsMetadataResultResponseTypeDef",
    {
        "OpsMetadataArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePatchBaselineRequestTypeDef = TypedDict(
    "_RequiredUpdatePatchBaselineRequestTypeDef",
    {
        "BaselineId": str,
    },
)
_OptionalUpdatePatchBaselineRequestTypeDef = TypedDict(
    "_OptionalUpdatePatchBaselineRequestTypeDef",
    {
        "Name": str,
        "GlobalFilters": "PatchFilterGroupTypeDef",
        "ApprovalRules": "PatchRuleGroupTypeDef",
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": PatchComplianceLevelType,
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": PatchActionType,
        "Description": str,
        "Sources": List["PatchSourceTypeDef"],
        "Replace": bool,
    },
    total=False,
)


class UpdatePatchBaselineRequestTypeDef(
    _RequiredUpdatePatchBaselineRequestTypeDef, _OptionalUpdatePatchBaselineRequestTypeDef
):
    pass


UpdatePatchBaselineResultResponseTypeDef = TypedDict(
    "UpdatePatchBaselineResultResponseTypeDef",
    {
        "BaselineId": str,
        "Name": str,
        "OperatingSystem": OperatingSystemType,
        "GlobalFilters": "PatchFilterGroupTypeDef",
        "ApprovalRules": "PatchRuleGroupTypeDef",
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": PatchComplianceLevelType,
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": PatchActionType,
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "Description": str,
        "Sources": List["PatchSourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateResourceDataSyncRequestTypeDef = TypedDict(
    "UpdateResourceDataSyncRequestTypeDef",
    {
        "SyncName": str,
        "SyncType": str,
        "SyncSource": "ResourceDataSyncSourceTypeDef",
    },
)

UpdateServiceSettingRequestTypeDef = TypedDict(
    "UpdateServiceSettingRequestTypeDef",
    {
        "SettingId": str,
        "SettingValue": str,
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
