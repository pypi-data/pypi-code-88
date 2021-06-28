"""
Type annotations for emr service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/type_defs.html)

Usage::

    ```python
    from mypy_boto3_emr.type_defs import AddInstanceFleetInputTypeDef

    data: AddInstanceFleetInputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ActionOnFailureType,
    AdjustmentTypeType,
    AuthModeType,
    AutoScalingPolicyStateChangeReasonCodeType,
    AutoScalingPolicyStateType,
    CancelStepsRequestStatusType,
    ClusterStateChangeReasonCodeType,
    ClusterStateType,
    ComparisonOperatorType,
    ComputeLimitsUnitTypeType,
    IdentityTypeType,
    InstanceCollectionTypeType,
    InstanceFleetStateChangeReasonCodeType,
    InstanceFleetStateType,
    InstanceFleetTypeType,
    InstanceGroupStateChangeReasonCodeType,
    InstanceGroupStateType,
    InstanceGroupTypeType,
    InstanceRoleTypeType,
    InstanceStateChangeReasonCodeType,
    InstanceStateType,
    JobFlowExecutionStateType,
    MarketTypeType,
    NotebookExecutionStatusType,
    OnDemandCapacityReservationPreferenceType,
    PlacementGroupStrategyType,
    RepoUpgradeOnBootType,
    ScaleDownBehaviorType,
    SpotProvisioningTimeoutActionType,
    StatisticType,
    StepCancellationOptionType,
    StepExecutionStateType,
    StepStateType,
    UnitType,
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
    "AddInstanceFleetInputTypeDef",
    "AddInstanceFleetOutputResponseTypeDef",
    "AddInstanceGroupsInputTypeDef",
    "AddInstanceGroupsOutputResponseTypeDef",
    "AddJobFlowStepsInputTypeDef",
    "AddJobFlowStepsOutputResponseTypeDef",
    "AddTagsInputTypeDef",
    "ApplicationTypeDef",
    "AutoScalingPolicyDescriptionTypeDef",
    "AutoScalingPolicyStateChangeReasonTypeDef",
    "AutoScalingPolicyStatusTypeDef",
    "AutoScalingPolicyTypeDef",
    "BlockPublicAccessConfigurationMetadataTypeDef",
    "BlockPublicAccessConfigurationTypeDef",
    "BootstrapActionConfigTypeDef",
    "BootstrapActionDetailTypeDef",
    "CancelStepsInfoTypeDef",
    "CancelStepsInputTypeDef",
    "CancelStepsOutputResponseTypeDef",
    "CloudWatchAlarmDefinitionTypeDef",
    "ClusterStateChangeReasonTypeDef",
    "ClusterStatusTypeDef",
    "ClusterSummaryTypeDef",
    "ClusterTimelineTypeDef",
    "ClusterTypeDef",
    "CommandTypeDef",
    "ComputeLimitsTypeDef",
    "ConfigurationTypeDef",
    "CreateSecurityConfigurationInputTypeDef",
    "CreateSecurityConfigurationOutputResponseTypeDef",
    "CreateStudioInputTypeDef",
    "CreateStudioOutputResponseTypeDef",
    "CreateStudioSessionMappingInputTypeDef",
    "DeleteSecurityConfigurationInputTypeDef",
    "DeleteStudioInputTypeDef",
    "DeleteStudioSessionMappingInputTypeDef",
    "DescribeClusterInputTypeDef",
    "DescribeClusterOutputResponseTypeDef",
    "DescribeJobFlowsInputTypeDef",
    "DescribeJobFlowsOutputResponseTypeDef",
    "DescribeNotebookExecutionInputTypeDef",
    "DescribeNotebookExecutionOutputResponseTypeDef",
    "DescribeSecurityConfigurationInputTypeDef",
    "DescribeSecurityConfigurationOutputResponseTypeDef",
    "DescribeStepInputTypeDef",
    "DescribeStepOutputResponseTypeDef",
    "DescribeStudioInputTypeDef",
    "DescribeStudioOutputResponseTypeDef",
    "EbsBlockDeviceConfigTypeDef",
    "EbsBlockDeviceTypeDef",
    "EbsConfigurationTypeDef",
    "EbsVolumeTypeDef",
    "Ec2InstanceAttributesTypeDef",
    "ExecutionEngineConfigTypeDef",
    "FailureDetailsTypeDef",
    "GetBlockPublicAccessConfigurationOutputResponseTypeDef",
    "GetManagedScalingPolicyInputTypeDef",
    "GetManagedScalingPolicyOutputResponseTypeDef",
    "GetStudioSessionMappingInputTypeDef",
    "GetStudioSessionMappingOutputResponseTypeDef",
    "HadoopJarStepConfigTypeDef",
    "HadoopStepConfigTypeDef",
    "InstanceFleetConfigTypeDef",
    "InstanceFleetModifyConfigTypeDef",
    "InstanceFleetProvisioningSpecificationsTypeDef",
    "InstanceFleetStateChangeReasonTypeDef",
    "InstanceFleetStatusTypeDef",
    "InstanceFleetTimelineTypeDef",
    "InstanceFleetTypeDef",
    "InstanceGroupConfigTypeDef",
    "InstanceGroupDetailTypeDef",
    "InstanceGroupModifyConfigTypeDef",
    "InstanceGroupStateChangeReasonTypeDef",
    "InstanceGroupStatusTypeDef",
    "InstanceGroupTimelineTypeDef",
    "InstanceGroupTypeDef",
    "InstanceResizePolicyTypeDef",
    "InstanceStateChangeReasonTypeDef",
    "InstanceStatusTypeDef",
    "InstanceTimelineTypeDef",
    "InstanceTypeConfigTypeDef",
    "InstanceTypeDef",
    "InstanceTypeSpecificationTypeDef",
    "JobFlowDetailTypeDef",
    "JobFlowExecutionStatusDetailTypeDef",
    "JobFlowInstancesConfigTypeDef",
    "JobFlowInstancesDetailTypeDef",
    "KerberosAttributesTypeDef",
    "KeyValueTypeDef",
    "ListBootstrapActionsInputTypeDef",
    "ListBootstrapActionsOutputResponseTypeDef",
    "ListClustersInputTypeDef",
    "ListClustersOutputResponseTypeDef",
    "ListInstanceFleetsInputTypeDef",
    "ListInstanceFleetsOutputResponseTypeDef",
    "ListInstanceGroupsInputTypeDef",
    "ListInstanceGroupsOutputResponseTypeDef",
    "ListInstancesInputTypeDef",
    "ListInstancesOutputResponseTypeDef",
    "ListNotebookExecutionsInputTypeDef",
    "ListNotebookExecutionsOutputResponseTypeDef",
    "ListSecurityConfigurationsInputTypeDef",
    "ListSecurityConfigurationsOutputResponseTypeDef",
    "ListStepsInputTypeDef",
    "ListStepsOutputResponseTypeDef",
    "ListStudioSessionMappingsInputTypeDef",
    "ListStudioSessionMappingsOutputResponseTypeDef",
    "ListStudiosInputTypeDef",
    "ListStudiosOutputResponseTypeDef",
    "ManagedScalingPolicyTypeDef",
    "MetricDimensionTypeDef",
    "ModifyClusterInputTypeDef",
    "ModifyClusterOutputResponseTypeDef",
    "ModifyInstanceFleetInputTypeDef",
    "ModifyInstanceGroupsInputTypeDef",
    "NotebookExecutionSummaryTypeDef",
    "NotebookExecutionTypeDef",
    "OnDemandCapacityReservationOptionsTypeDef",
    "OnDemandProvisioningSpecificationTypeDef",
    "PaginatorConfigTypeDef",
    "PlacementGroupConfigTypeDef",
    "PlacementTypeTypeDef",
    "PortRangeTypeDef",
    "PutAutoScalingPolicyInputTypeDef",
    "PutAutoScalingPolicyOutputResponseTypeDef",
    "PutBlockPublicAccessConfigurationInputTypeDef",
    "PutManagedScalingPolicyInputTypeDef",
    "RemoveAutoScalingPolicyInputTypeDef",
    "RemoveManagedScalingPolicyInputTypeDef",
    "RemoveTagsInputTypeDef",
    "ResponseMetadataTypeDef",
    "RunJobFlowInputTypeDef",
    "RunJobFlowOutputResponseTypeDef",
    "ScalingActionTypeDef",
    "ScalingConstraintsTypeDef",
    "ScalingRuleTypeDef",
    "ScalingTriggerTypeDef",
    "ScriptBootstrapActionConfigTypeDef",
    "SecurityConfigurationSummaryTypeDef",
    "SessionMappingDetailTypeDef",
    "SessionMappingSummaryTypeDef",
    "SetTerminationProtectionInputTypeDef",
    "SetVisibleToAllUsersInputTypeDef",
    "ShrinkPolicyTypeDef",
    "SimpleScalingPolicyConfigurationTypeDef",
    "SpotProvisioningSpecificationTypeDef",
    "StartNotebookExecutionInputTypeDef",
    "StartNotebookExecutionOutputResponseTypeDef",
    "StepConfigTypeDef",
    "StepDetailTypeDef",
    "StepExecutionStatusDetailTypeDef",
    "StepStateChangeReasonTypeDef",
    "StepStatusTypeDef",
    "StepSummaryTypeDef",
    "StepTimelineTypeDef",
    "StepTypeDef",
    "StopNotebookExecutionInputTypeDef",
    "StudioSummaryTypeDef",
    "StudioTypeDef",
    "SupportedProductConfigTypeDef",
    "TagTypeDef",
    "TerminateJobFlowsInputTypeDef",
    "UpdateStudioInputTypeDef",
    "UpdateStudioSessionMappingInputTypeDef",
    "VolumeSpecificationTypeDef",
    "WaiterConfigTypeDef",
)

AddInstanceFleetInputTypeDef = TypedDict(
    "AddInstanceFleetInputTypeDef",
    {
        "ClusterId": str,
        "InstanceFleet": "InstanceFleetConfigTypeDef",
    },
)

AddInstanceFleetOutputResponseTypeDef = TypedDict(
    "AddInstanceFleetOutputResponseTypeDef",
    {
        "ClusterId": str,
        "InstanceFleetId": str,
        "ClusterArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddInstanceGroupsInputTypeDef = TypedDict(
    "AddInstanceGroupsInputTypeDef",
    {
        "InstanceGroups": List["InstanceGroupConfigTypeDef"],
        "JobFlowId": str,
    },
)

AddInstanceGroupsOutputResponseTypeDef = TypedDict(
    "AddInstanceGroupsOutputResponseTypeDef",
    {
        "JobFlowId": str,
        "InstanceGroupIds": List[str],
        "ClusterArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddJobFlowStepsInputTypeDef = TypedDict(
    "AddJobFlowStepsInputTypeDef",
    {
        "JobFlowId": str,
        "Steps": List["StepConfigTypeDef"],
    },
)

AddJobFlowStepsOutputResponseTypeDef = TypedDict(
    "AddJobFlowStepsOutputResponseTypeDef",
    {
        "StepIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsInputTypeDef = TypedDict(
    "AddTagsInputTypeDef",
    {
        "ResourceId": str,
        "Tags": List["TagTypeDef"],
    },
)

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "Name": str,
        "Version": str,
        "Args": List[str],
        "AdditionalInfo": Dict[str, str],
    },
    total=False,
)

AutoScalingPolicyDescriptionTypeDef = TypedDict(
    "AutoScalingPolicyDescriptionTypeDef",
    {
        "Status": "AutoScalingPolicyStatusTypeDef",
        "Constraints": "ScalingConstraintsTypeDef",
        "Rules": List["ScalingRuleTypeDef"],
    },
    total=False,
)

AutoScalingPolicyStateChangeReasonTypeDef = TypedDict(
    "AutoScalingPolicyStateChangeReasonTypeDef",
    {
        "Code": AutoScalingPolicyStateChangeReasonCodeType,
        "Message": str,
    },
    total=False,
)

AutoScalingPolicyStatusTypeDef = TypedDict(
    "AutoScalingPolicyStatusTypeDef",
    {
        "State": AutoScalingPolicyStateType,
        "StateChangeReason": "AutoScalingPolicyStateChangeReasonTypeDef",
    },
    total=False,
)

AutoScalingPolicyTypeDef = TypedDict(
    "AutoScalingPolicyTypeDef",
    {
        "Constraints": "ScalingConstraintsTypeDef",
        "Rules": List["ScalingRuleTypeDef"],
    },
)

BlockPublicAccessConfigurationMetadataTypeDef = TypedDict(
    "BlockPublicAccessConfigurationMetadataTypeDef",
    {
        "CreationDateTime": datetime,
        "CreatedByArn": str,
    },
)

_RequiredBlockPublicAccessConfigurationTypeDef = TypedDict(
    "_RequiredBlockPublicAccessConfigurationTypeDef",
    {
        "BlockPublicSecurityGroupRules": bool,
    },
)
_OptionalBlockPublicAccessConfigurationTypeDef = TypedDict(
    "_OptionalBlockPublicAccessConfigurationTypeDef",
    {
        "PermittedPublicSecurityGroupRuleRanges": List["PortRangeTypeDef"],
    },
    total=False,
)


class BlockPublicAccessConfigurationTypeDef(
    _RequiredBlockPublicAccessConfigurationTypeDef, _OptionalBlockPublicAccessConfigurationTypeDef
):
    pass


BootstrapActionConfigTypeDef = TypedDict(
    "BootstrapActionConfigTypeDef",
    {
        "Name": str,
        "ScriptBootstrapAction": "ScriptBootstrapActionConfigTypeDef",
    },
)

BootstrapActionDetailTypeDef = TypedDict(
    "BootstrapActionDetailTypeDef",
    {
        "BootstrapActionConfig": "BootstrapActionConfigTypeDef",
    },
    total=False,
)

CancelStepsInfoTypeDef = TypedDict(
    "CancelStepsInfoTypeDef",
    {
        "StepId": str,
        "Status": CancelStepsRequestStatusType,
        "Reason": str,
    },
    total=False,
)

_RequiredCancelStepsInputTypeDef = TypedDict(
    "_RequiredCancelStepsInputTypeDef",
    {
        "ClusterId": str,
        "StepIds": List[str],
    },
)
_OptionalCancelStepsInputTypeDef = TypedDict(
    "_OptionalCancelStepsInputTypeDef",
    {
        "StepCancellationOption": StepCancellationOptionType,
    },
    total=False,
)


class CancelStepsInputTypeDef(_RequiredCancelStepsInputTypeDef, _OptionalCancelStepsInputTypeDef):
    pass


CancelStepsOutputResponseTypeDef = TypedDict(
    "CancelStepsOutputResponseTypeDef",
    {
        "CancelStepsInfoList": List["CancelStepsInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_RequiredCloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": ComparisonOperatorType,
        "MetricName": str,
        "Period": int,
        "Threshold": float,
    },
)
_OptionalCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_OptionalCloudWatchAlarmDefinitionTypeDef",
    {
        "EvaluationPeriods": int,
        "Namespace": str,
        "Statistic": StatisticType,
        "Unit": UnitType,
        "Dimensions": List["MetricDimensionTypeDef"],
    },
    total=False,
)


class CloudWatchAlarmDefinitionTypeDef(
    _RequiredCloudWatchAlarmDefinitionTypeDef, _OptionalCloudWatchAlarmDefinitionTypeDef
):
    pass


ClusterStateChangeReasonTypeDef = TypedDict(
    "ClusterStateChangeReasonTypeDef",
    {
        "Code": ClusterStateChangeReasonCodeType,
        "Message": str,
    },
    total=False,
)

ClusterStatusTypeDef = TypedDict(
    "ClusterStatusTypeDef",
    {
        "State": ClusterStateType,
        "StateChangeReason": "ClusterStateChangeReasonTypeDef",
        "Timeline": "ClusterTimelineTypeDef",
    },
    total=False,
)

ClusterSummaryTypeDef = TypedDict(
    "ClusterSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": "ClusterStatusTypeDef",
        "NormalizedInstanceHours": int,
        "ClusterArn": str,
        "OutpostArn": str,
    },
    total=False,
)

ClusterTimelineTypeDef = TypedDict(
    "ClusterTimelineTypeDef",
    {
        "CreationDateTime": datetime,
        "ReadyDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": "ClusterStatusTypeDef",
        "Ec2InstanceAttributes": "Ec2InstanceAttributesTypeDef",
        "InstanceCollectionType": InstanceCollectionTypeType,
        "LogUri": str,
        "LogEncryptionKmsKeyId": str,
        "RequestedAmiVersion": str,
        "RunningAmiVersion": str,
        "ReleaseLabel": str,
        "AutoTerminate": bool,
        "TerminationProtected": bool,
        "VisibleToAllUsers": bool,
        "Applications": List["ApplicationTypeDef"],
        "Tags": List["TagTypeDef"],
        "ServiceRole": str,
        "NormalizedInstanceHours": int,
        "MasterPublicDnsName": str,
        "Configurations": List["ConfigurationTypeDef"],
        "SecurityConfiguration": str,
        "AutoScalingRole": str,
        "ScaleDownBehavior": ScaleDownBehaviorType,
        "CustomAmiId": str,
        "EbsRootVolumeSize": int,
        "RepoUpgradeOnBoot": RepoUpgradeOnBootType,
        "KerberosAttributes": "KerberosAttributesTypeDef",
        "ClusterArn": str,
        "OutpostArn": str,
        "StepConcurrencyLevel": int,
        "PlacementGroups": List["PlacementGroupConfigTypeDef"],
    },
    total=False,
)

CommandTypeDef = TypedDict(
    "CommandTypeDef",
    {
        "Name": str,
        "ScriptPath": str,
        "Args": List[str],
    },
    total=False,
)

_RequiredComputeLimitsTypeDef = TypedDict(
    "_RequiredComputeLimitsTypeDef",
    {
        "UnitType": ComputeLimitsUnitTypeType,
        "MinimumCapacityUnits": int,
        "MaximumCapacityUnits": int,
    },
)
_OptionalComputeLimitsTypeDef = TypedDict(
    "_OptionalComputeLimitsTypeDef",
    {
        "MaximumOnDemandCapacityUnits": int,
        "MaximumCoreCapacityUnits": int,
    },
    total=False,
)


class ComputeLimitsTypeDef(_RequiredComputeLimitsTypeDef, _OptionalComputeLimitsTypeDef):
    pass


ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Classification": str,
        "Configurations": List[Dict[str, Any]],
        "Properties": Dict[str, str],
    },
    total=False,
)

CreateSecurityConfigurationInputTypeDef = TypedDict(
    "CreateSecurityConfigurationInputTypeDef",
    {
        "Name": str,
        "SecurityConfiguration": str,
    },
)

CreateSecurityConfigurationOutputResponseTypeDef = TypedDict(
    "CreateSecurityConfigurationOutputResponseTypeDef",
    {
        "Name": str,
        "CreationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStudioInputTypeDef = TypedDict(
    "_RequiredCreateStudioInputTypeDef",
    {
        "Name": str,
        "AuthMode": AuthModeType,
        "VpcId": str,
        "SubnetIds": List[str],
        "ServiceRole": str,
        "UserRole": str,
        "WorkspaceSecurityGroupId": str,
        "EngineSecurityGroupId": str,
        "DefaultS3Location": str,
    },
)
_OptionalCreateStudioInputTypeDef = TypedDict(
    "_OptionalCreateStudioInputTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateStudioInputTypeDef(
    _RequiredCreateStudioInputTypeDef, _OptionalCreateStudioInputTypeDef
):
    pass


CreateStudioOutputResponseTypeDef = TypedDict(
    "CreateStudioOutputResponseTypeDef",
    {
        "StudioId": str,
        "Url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStudioSessionMappingInputTypeDef = TypedDict(
    "_RequiredCreateStudioSessionMappingInputTypeDef",
    {
        "StudioId": str,
        "IdentityType": IdentityTypeType,
        "SessionPolicyArn": str,
    },
)
_OptionalCreateStudioSessionMappingInputTypeDef = TypedDict(
    "_OptionalCreateStudioSessionMappingInputTypeDef",
    {
        "IdentityId": str,
        "IdentityName": str,
    },
    total=False,
)


class CreateStudioSessionMappingInputTypeDef(
    _RequiredCreateStudioSessionMappingInputTypeDef, _OptionalCreateStudioSessionMappingInputTypeDef
):
    pass


DeleteSecurityConfigurationInputTypeDef = TypedDict(
    "DeleteSecurityConfigurationInputTypeDef",
    {
        "Name": str,
    },
)

DeleteStudioInputTypeDef = TypedDict(
    "DeleteStudioInputTypeDef",
    {
        "StudioId": str,
    },
)

_RequiredDeleteStudioSessionMappingInputTypeDef = TypedDict(
    "_RequiredDeleteStudioSessionMappingInputTypeDef",
    {
        "StudioId": str,
        "IdentityType": IdentityTypeType,
    },
)
_OptionalDeleteStudioSessionMappingInputTypeDef = TypedDict(
    "_OptionalDeleteStudioSessionMappingInputTypeDef",
    {
        "IdentityId": str,
        "IdentityName": str,
    },
    total=False,
)


class DeleteStudioSessionMappingInputTypeDef(
    _RequiredDeleteStudioSessionMappingInputTypeDef, _OptionalDeleteStudioSessionMappingInputTypeDef
):
    pass


DescribeClusterInputTypeDef = TypedDict(
    "DescribeClusterInputTypeDef",
    {
        "ClusterId": str,
    },
)

DescribeClusterOutputResponseTypeDef = TypedDict(
    "DescribeClusterOutputResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobFlowsInputTypeDef = TypedDict(
    "DescribeJobFlowsInputTypeDef",
    {
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "JobFlowIds": List[str],
        "JobFlowStates": List[JobFlowExecutionStateType],
    },
    total=False,
)

DescribeJobFlowsOutputResponseTypeDef = TypedDict(
    "DescribeJobFlowsOutputResponseTypeDef",
    {
        "JobFlows": List["JobFlowDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNotebookExecutionInputTypeDef = TypedDict(
    "DescribeNotebookExecutionInputTypeDef",
    {
        "NotebookExecutionId": str,
    },
)

DescribeNotebookExecutionOutputResponseTypeDef = TypedDict(
    "DescribeNotebookExecutionOutputResponseTypeDef",
    {
        "NotebookExecution": "NotebookExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityConfigurationInputTypeDef = TypedDict(
    "DescribeSecurityConfigurationInputTypeDef",
    {
        "Name": str,
    },
)

DescribeSecurityConfigurationOutputResponseTypeDef = TypedDict(
    "DescribeSecurityConfigurationOutputResponseTypeDef",
    {
        "Name": str,
        "SecurityConfiguration": str,
        "CreationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStepInputTypeDef = TypedDict(
    "DescribeStepInputTypeDef",
    {
        "ClusterId": str,
        "StepId": str,
    },
)

DescribeStepOutputResponseTypeDef = TypedDict(
    "DescribeStepOutputResponseTypeDef",
    {
        "Step": "StepTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStudioInputTypeDef = TypedDict(
    "DescribeStudioInputTypeDef",
    {
        "StudioId": str,
    },
)

DescribeStudioOutputResponseTypeDef = TypedDict(
    "DescribeStudioOutputResponseTypeDef",
    {
        "Studio": "StudioTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEbsBlockDeviceConfigTypeDef = TypedDict(
    "_RequiredEbsBlockDeviceConfigTypeDef",
    {
        "VolumeSpecification": "VolumeSpecificationTypeDef",
    },
)
_OptionalEbsBlockDeviceConfigTypeDef = TypedDict(
    "_OptionalEbsBlockDeviceConfigTypeDef",
    {
        "VolumesPerInstance": int,
    },
    total=False,
)


class EbsBlockDeviceConfigTypeDef(
    _RequiredEbsBlockDeviceConfigTypeDef, _OptionalEbsBlockDeviceConfigTypeDef
):
    pass


EbsBlockDeviceTypeDef = TypedDict(
    "EbsBlockDeviceTypeDef",
    {
        "VolumeSpecification": "VolumeSpecificationTypeDef",
        "Device": str,
    },
    total=False,
)

EbsConfigurationTypeDef = TypedDict(
    "EbsConfigurationTypeDef",
    {
        "EbsBlockDeviceConfigs": List["EbsBlockDeviceConfigTypeDef"],
        "EbsOptimized": bool,
    },
    total=False,
)

EbsVolumeTypeDef = TypedDict(
    "EbsVolumeTypeDef",
    {
        "Device": str,
        "VolumeId": str,
    },
    total=False,
)

Ec2InstanceAttributesTypeDef = TypedDict(
    "Ec2InstanceAttributesTypeDef",
    {
        "Ec2KeyName": str,
        "Ec2SubnetId": str,
        "RequestedEc2SubnetIds": List[str],
        "Ec2AvailabilityZone": str,
        "RequestedEc2AvailabilityZones": List[str],
        "IamInstanceProfile": str,
        "EmrManagedMasterSecurityGroup": str,
        "EmrManagedSlaveSecurityGroup": str,
        "ServiceAccessSecurityGroup": str,
        "AdditionalMasterSecurityGroups": List[str],
        "AdditionalSlaveSecurityGroups": List[str],
    },
    total=False,
)

_RequiredExecutionEngineConfigTypeDef = TypedDict(
    "_RequiredExecutionEngineConfigTypeDef",
    {
        "Id": str,
    },
)
_OptionalExecutionEngineConfigTypeDef = TypedDict(
    "_OptionalExecutionEngineConfigTypeDef",
    {
        "Type": Literal["EMR"],
        "MasterInstanceSecurityGroupId": str,
    },
    total=False,
)


class ExecutionEngineConfigTypeDef(
    _RequiredExecutionEngineConfigTypeDef, _OptionalExecutionEngineConfigTypeDef
):
    pass


FailureDetailsTypeDef = TypedDict(
    "FailureDetailsTypeDef",
    {
        "Reason": str,
        "Message": str,
        "LogFile": str,
    },
    total=False,
)

GetBlockPublicAccessConfigurationOutputResponseTypeDef = TypedDict(
    "GetBlockPublicAccessConfigurationOutputResponseTypeDef",
    {
        "BlockPublicAccessConfiguration": "BlockPublicAccessConfigurationTypeDef",
        "BlockPublicAccessConfigurationMetadata": "BlockPublicAccessConfigurationMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetManagedScalingPolicyInputTypeDef = TypedDict(
    "GetManagedScalingPolicyInputTypeDef",
    {
        "ClusterId": str,
    },
)

GetManagedScalingPolicyOutputResponseTypeDef = TypedDict(
    "GetManagedScalingPolicyOutputResponseTypeDef",
    {
        "ManagedScalingPolicy": "ManagedScalingPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetStudioSessionMappingInputTypeDef = TypedDict(
    "_RequiredGetStudioSessionMappingInputTypeDef",
    {
        "StudioId": str,
        "IdentityType": IdentityTypeType,
    },
)
_OptionalGetStudioSessionMappingInputTypeDef = TypedDict(
    "_OptionalGetStudioSessionMappingInputTypeDef",
    {
        "IdentityId": str,
        "IdentityName": str,
    },
    total=False,
)


class GetStudioSessionMappingInputTypeDef(
    _RequiredGetStudioSessionMappingInputTypeDef, _OptionalGetStudioSessionMappingInputTypeDef
):
    pass


GetStudioSessionMappingOutputResponseTypeDef = TypedDict(
    "GetStudioSessionMappingOutputResponseTypeDef",
    {
        "SessionMapping": "SessionMappingDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredHadoopJarStepConfigTypeDef = TypedDict(
    "_RequiredHadoopJarStepConfigTypeDef",
    {
        "Jar": str,
    },
)
_OptionalHadoopJarStepConfigTypeDef = TypedDict(
    "_OptionalHadoopJarStepConfigTypeDef",
    {
        "Properties": List["KeyValueTypeDef"],
        "MainClass": str,
        "Args": List[str],
    },
    total=False,
)


class HadoopJarStepConfigTypeDef(
    _RequiredHadoopJarStepConfigTypeDef, _OptionalHadoopJarStepConfigTypeDef
):
    pass


HadoopStepConfigTypeDef = TypedDict(
    "HadoopStepConfigTypeDef",
    {
        "Jar": str,
        "Properties": Dict[str, str],
        "MainClass": str,
        "Args": List[str],
    },
    total=False,
)

_RequiredInstanceFleetConfigTypeDef = TypedDict(
    "_RequiredInstanceFleetConfigTypeDef",
    {
        "InstanceFleetType": InstanceFleetTypeType,
    },
)
_OptionalInstanceFleetConfigTypeDef = TypedDict(
    "_OptionalInstanceFleetConfigTypeDef",
    {
        "Name": str,
        "TargetOnDemandCapacity": int,
        "TargetSpotCapacity": int,
        "InstanceTypeConfigs": List["InstanceTypeConfigTypeDef"],
        "LaunchSpecifications": "InstanceFleetProvisioningSpecificationsTypeDef",
    },
    total=False,
)


class InstanceFleetConfigTypeDef(
    _RequiredInstanceFleetConfigTypeDef, _OptionalInstanceFleetConfigTypeDef
):
    pass


_RequiredInstanceFleetModifyConfigTypeDef = TypedDict(
    "_RequiredInstanceFleetModifyConfigTypeDef",
    {
        "InstanceFleetId": str,
    },
)
_OptionalInstanceFleetModifyConfigTypeDef = TypedDict(
    "_OptionalInstanceFleetModifyConfigTypeDef",
    {
        "TargetOnDemandCapacity": int,
        "TargetSpotCapacity": int,
    },
    total=False,
)


class InstanceFleetModifyConfigTypeDef(
    _RequiredInstanceFleetModifyConfigTypeDef, _OptionalInstanceFleetModifyConfigTypeDef
):
    pass


InstanceFleetProvisioningSpecificationsTypeDef = TypedDict(
    "InstanceFleetProvisioningSpecificationsTypeDef",
    {
        "SpotSpecification": "SpotProvisioningSpecificationTypeDef",
        "OnDemandSpecification": "OnDemandProvisioningSpecificationTypeDef",
    },
    total=False,
)

InstanceFleetStateChangeReasonTypeDef = TypedDict(
    "InstanceFleetStateChangeReasonTypeDef",
    {
        "Code": InstanceFleetStateChangeReasonCodeType,
        "Message": str,
    },
    total=False,
)

InstanceFleetStatusTypeDef = TypedDict(
    "InstanceFleetStatusTypeDef",
    {
        "State": InstanceFleetStateType,
        "StateChangeReason": "InstanceFleetStateChangeReasonTypeDef",
        "Timeline": "InstanceFleetTimelineTypeDef",
    },
    total=False,
)

InstanceFleetTimelineTypeDef = TypedDict(
    "InstanceFleetTimelineTypeDef",
    {
        "CreationDateTime": datetime,
        "ReadyDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)

InstanceFleetTypeDef = TypedDict(
    "InstanceFleetTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": "InstanceFleetStatusTypeDef",
        "InstanceFleetType": InstanceFleetTypeType,
        "TargetOnDemandCapacity": int,
        "TargetSpotCapacity": int,
        "ProvisionedOnDemandCapacity": int,
        "ProvisionedSpotCapacity": int,
        "InstanceTypeSpecifications": List["InstanceTypeSpecificationTypeDef"],
        "LaunchSpecifications": "InstanceFleetProvisioningSpecificationsTypeDef",
    },
    total=False,
)

_RequiredInstanceGroupConfigTypeDef = TypedDict(
    "_RequiredInstanceGroupConfigTypeDef",
    {
        "InstanceRole": InstanceRoleTypeType,
        "InstanceType": str,
        "InstanceCount": int,
    },
)
_OptionalInstanceGroupConfigTypeDef = TypedDict(
    "_OptionalInstanceGroupConfigTypeDef",
    {
        "Name": str,
        "Market": MarketTypeType,
        "BidPrice": str,
        "Configurations": List["ConfigurationTypeDef"],
        "EbsConfiguration": "EbsConfigurationTypeDef",
        "AutoScalingPolicy": "AutoScalingPolicyTypeDef",
    },
    total=False,
)


class InstanceGroupConfigTypeDef(
    _RequiredInstanceGroupConfigTypeDef, _OptionalInstanceGroupConfigTypeDef
):
    pass


_RequiredInstanceGroupDetailTypeDef = TypedDict(
    "_RequiredInstanceGroupDetailTypeDef",
    {
        "Market": MarketTypeType,
        "InstanceRole": InstanceRoleTypeType,
        "InstanceType": str,
        "InstanceRequestCount": int,
        "InstanceRunningCount": int,
        "State": InstanceGroupStateType,
        "CreationDateTime": datetime,
    },
)
_OptionalInstanceGroupDetailTypeDef = TypedDict(
    "_OptionalInstanceGroupDetailTypeDef",
    {
        "InstanceGroupId": str,
        "Name": str,
        "BidPrice": str,
        "LastStateChangeReason": str,
        "StartDateTime": datetime,
        "ReadyDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)


class InstanceGroupDetailTypeDef(
    _RequiredInstanceGroupDetailTypeDef, _OptionalInstanceGroupDetailTypeDef
):
    pass


_RequiredInstanceGroupModifyConfigTypeDef = TypedDict(
    "_RequiredInstanceGroupModifyConfigTypeDef",
    {
        "InstanceGroupId": str,
    },
)
_OptionalInstanceGroupModifyConfigTypeDef = TypedDict(
    "_OptionalInstanceGroupModifyConfigTypeDef",
    {
        "InstanceCount": int,
        "EC2InstanceIdsToTerminate": List[str],
        "ShrinkPolicy": "ShrinkPolicyTypeDef",
        "Configurations": List["ConfigurationTypeDef"],
    },
    total=False,
)


class InstanceGroupModifyConfigTypeDef(
    _RequiredInstanceGroupModifyConfigTypeDef, _OptionalInstanceGroupModifyConfigTypeDef
):
    pass


InstanceGroupStateChangeReasonTypeDef = TypedDict(
    "InstanceGroupStateChangeReasonTypeDef",
    {
        "Code": InstanceGroupStateChangeReasonCodeType,
        "Message": str,
    },
    total=False,
)

InstanceGroupStatusTypeDef = TypedDict(
    "InstanceGroupStatusTypeDef",
    {
        "State": InstanceGroupStateType,
        "StateChangeReason": "InstanceGroupStateChangeReasonTypeDef",
        "Timeline": "InstanceGroupTimelineTypeDef",
    },
    total=False,
)

InstanceGroupTimelineTypeDef = TypedDict(
    "InstanceGroupTimelineTypeDef",
    {
        "CreationDateTime": datetime,
        "ReadyDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)

InstanceGroupTypeDef = TypedDict(
    "InstanceGroupTypeDef",
    {
        "Id": str,
        "Name": str,
        "Market": MarketTypeType,
        "InstanceGroupType": InstanceGroupTypeType,
        "BidPrice": str,
        "InstanceType": str,
        "RequestedInstanceCount": int,
        "RunningInstanceCount": int,
        "Status": "InstanceGroupStatusTypeDef",
        "Configurations": List["ConfigurationTypeDef"],
        "ConfigurationsVersion": int,
        "LastSuccessfullyAppliedConfigurations": List["ConfigurationTypeDef"],
        "LastSuccessfullyAppliedConfigurationsVersion": int,
        "EbsBlockDevices": List["EbsBlockDeviceTypeDef"],
        "EbsOptimized": bool,
        "ShrinkPolicy": "ShrinkPolicyTypeDef",
        "AutoScalingPolicy": "AutoScalingPolicyDescriptionTypeDef",
    },
    total=False,
)

InstanceResizePolicyTypeDef = TypedDict(
    "InstanceResizePolicyTypeDef",
    {
        "InstancesToTerminate": List[str],
        "InstancesToProtect": List[str],
        "InstanceTerminationTimeout": int,
    },
    total=False,
)

InstanceStateChangeReasonTypeDef = TypedDict(
    "InstanceStateChangeReasonTypeDef",
    {
        "Code": InstanceStateChangeReasonCodeType,
        "Message": str,
    },
    total=False,
)

InstanceStatusTypeDef = TypedDict(
    "InstanceStatusTypeDef",
    {
        "State": InstanceStateType,
        "StateChangeReason": "InstanceStateChangeReasonTypeDef",
        "Timeline": "InstanceTimelineTypeDef",
    },
    total=False,
)

InstanceTimelineTypeDef = TypedDict(
    "InstanceTimelineTypeDef",
    {
        "CreationDateTime": datetime,
        "ReadyDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)

_RequiredInstanceTypeConfigTypeDef = TypedDict(
    "_RequiredInstanceTypeConfigTypeDef",
    {
        "InstanceType": str,
    },
)
_OptionalInstanceTypeConfigTypeDef = TypedDict(
    "_OptionalInstanceTypeConfigTypeDef",
    {
        "WeightedCapacity": int,
        "BidPrice": str,
        "BidPriceAsPercentageOfOnDemandPrice": float,
        "EbsConfiguration": "EbsConfigurationTypeDef",
        "Configurations": List["ConfigurationTypeDef"],
    },
    total=False,
)


class InstanceTypeConfigTypeDef(
    _RequiredInstanceTypeConfigTypeDef, _OptionalInstanceTypeConfigTypeDef
):
    pass


InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "Id": str,
        "Ec2InstanceId": str,
        "PublicDnsName": str,
        "PublicIpAddress": str,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "Status": "InstanceStatusTypeDef",
        "InstanceGroupId": str,
        "InstanceFleetId": str,
        "Market": MarketTypeType,
        "InstanceType": str,
        "EbsVolumes": List["EbsVolumeTypeDef"],
    },
    total=False,
)

InstanceTypeSpecificationTypeDef = TypedDict(
    "InstanceTypeSpecificationTypeDef",
    {
        "InstanceType": str,
        "WeightedCapacity": int,
        "BidPrice": str,
        "BidPriceAsPercentageOfOnDemandPrice": float,
        "Configurations": List["ConfigurationTypeDef"],
        "EbsBlockDevices": List["EbsBlockDeviceTypeDef"],
        "EbsOptimized": bool,
    },
    total=False,
)

_RequiredJobFlowDetailTypeDef = TypedDict(
    "_RequiredJobFlowDetailTypeDef",
    {
        "JobFlowId": str,
        "Name": str,
        "ExecutionStatusDetail": "JobFlowExecutionStatusDetailTypeDef",
        "Instances": "JobFlowInstancesDetailTypeDef",
    },
)
_OptionalJobFlowDetailTypeDef = TypedDict(
    "_OptionalJobFlowDetailTypeDef",
    {
        "LogUri": str,
        "LogEncryptionKmsKeyId": str,
        "AmiVersion": str,
        "Steps": List["StepDetailTypeDef"],
        "BootstrapActions": List["BootstrapActionDetailTypeDef"],
        "SupportedProducts": List[str],
        "VisibleToAllUsers": bool,
        "JobFlowRole": str,
        "ServiceRole": str,
        "AutoScalingRole": str,
        "ScaleDownBehavior": ScaleDownBehaviorType,
    },
    total=False,
)


class JobFlowDetailTypeDef(_RequiredJobFlowDetailTypeDef, _OptionalJobFlowDetailTypeDef):
    pass


_RequiredJobFlowExecutionStatusDetailTypeDef = TypedDict(
    "_RequiredJobFlowExecutionStatusDetailTypeDef",
    {
        "State": JobFlowExecutionStateType,
        "CreationDateTime": datetime,
    },
)
_OptionalJobFlowExecutionStatusDetailTypeDef = TypedDict(
    "_OptionalJobFlowExecutionStatusDetailTypeDef",
    {
        "StartDateTime": datetime,
        "ReadyDateTime": datetime,
        "EndDateTime": datetime,
        "LastStateChangeReason": str,
    },
    total=False,
)


class JobFlowExecutionStatusDetailTypeDef(
    _RequiredJobFlowExecutionStatusDetailTypeDef, _OptionalJobFlowExecutionStatusDetailTypeDef
):
    pass


JobFlowInstancesConfigTypeDef = TypedDict(
    "JobFlowInstancesConfigTypeDef",
    {
        "MasterInstanceType": str,
        "SlaveInstanceType": str,
        "InstanceCount": int,
        "InstanceGroups": List["InstanceGroupConfigTypeDef"],
        "InstanceFleets": List["InstanceFleetConfigTypeDef"],
        "Ec2KeyName": str,
        "Placement": "PlacementTypeTypeDef",
        "KeepJobFlowAliveWhenNoSteps": bool,
        "TerminationProtected": bool,
        "HadoopVersion": str,
        "Ec2SubnetId": str,
        "Ec2SubnetIds": List[str],
        "EmrManagedMasterSecurityGroup": str,
        "EmrManagedSlaveSecurityGroup": str,
        "ServiceAccessSecurityGroup": str,
        "AdditionalMasterSecurityGroups": List[str],
        "AdditionalSlaveSecurityGroups": List[str],
    },
    total=False,
)

_RequiredJobFlowInstancesDetailTypeDef = TypedDict(
    "_RequiredJobFlowInstancesDetailTypeDef",
    {
        "MasterInstanceType": str,
        "SlaveInstanceType": str,
        "InstanceCount": int,
    },
)
_OptionalJobFlowInstancesDetailTypeDef = TypedDict(
    "_OptionalJobFlowInstancesDetailTypeDef",
    {
        "MasterPublicDnsName": str,
        "MasterInstanceId": str,
        "InstanceGroups": List["InstanceGroupDetailTypeDef"],
        "NormalizedInstanceHours": int,
        "Ec2KeyName": str,
        "Ec2SubnetId": str,
        "Placement": "PlacementTypeTypeDef",
        "KeepJobFlowAliveWhenNoSteps": bool,
        "TerminationProtected": bool,
        "HadoopVersion": str,
    },
    total=False,
)


class JobFlowInstancesDetailTypeDef(
    _RequiredJobFlowInstancesDetailTypeDef, _OptionalJobFlowInstancesDetailTypeDef
):
    pass


_RequiredKerberosAttributesTypeDef = TypedDict(
    "_RequiredKerberosAttributesTypeDef",
    {
        "Realm": str,
        "KdcAdminPassword": str,
    },
)
_OptionalKerberosAttributesTypeDef = TypedDict(
    "_OptionalKerberosAttributesTypeDef",
    {
        "CrossRealmTrustPrincipalPassword": str,
        "ADDomainJoinUser": str,
        "ADDomainJoinPassword": str,
    },
    total=False,
)


class KerberosAttributesTypeDef(
    _RequiredKerberosAttributesTypeDef, _OptionalKerberosAttributesTypeDef
):
    pass


KeyValueTypeDef = TypedDict(
    "KeyValueTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredListBootstrapActionsInputTypeDef = TypedDict(
    "_RequiredListBootstrapActionsInputTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalListBootstrapActionsInputTypeDef = TypedDict(
    "_OptionalListBootstrapActionsInputTypeDef",
    {
        "Marker": str,
    },
    total=False,
)


class ListBootstrapActionsInputTypeDef(
    _RequiredListBootstrapActionsInputTypeDef, _OptionalListBootstrapActionsInputTypeDef
):
    pass


ListBootstrapActionsOutputResponseTypeDef = TypedDict(
    "ListBootstrapActionsOutputResponseTypeDef",
    {
        "BootstrapActions": List["CommandTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClustersInputTypeDef = TypedDict(
    "ListClustersInputTypeDef",
    {
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "ClusterStates": List[ClusterStateType],
        "Marker": str,
    },
    total=False,
)

ListClustersOutputResponseTypeDef = TypedDict(
    "ListClustersOutputResponseTypeDef",
    {
        "Clusters": List["ClusterSummaryTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstanceFleetsInputTypeDef = TypedDict(
    "_RequiredListInstanceFleetsInputTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalListInstanceFleetsInputTypeDef = TypedDict(
    "_OptionalListInstanceFleetsInputTypeDef",
    {
        "Marker": str,
    },
    total=False,
)


class ListInstanceFleetsInputTypeDef(
    _RequiredListInstanceFleetsInputTypeDef, _OptionalListInstanceFleetsInputTypeDef
):
    pass


ListInstanceFleetsOutputResponseTypeDef = TypedDict(
    "ListInstanceFleetsOutputResponseTypeDef",
    {
        "InstanceFleets": List["InstanceFleetTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstanceGroupsInputTypeDef = TypedDict(
    "_RequiredListInstanceGroupsInputTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalListInstanceGroupsInputTypeDef = TypedDict(
    "_OptionalListInstanceGroupsInputTypeDef",
    {
        "Marker": str,
    },
    total=False,
)


class ListInstanceGroupsInputTypeDef(
    _RequiredListInstanceGroupsInputTypeDef, _OptionalListInstanceGroupsInputTypeDef
):
    pass


ListInstanceGroupsOutputResponseTypeDef = TypedDict(
    "ListInstanceGroupsOutputResponseTypeDef",
    {
        "InstanceGroups": List["InstanceGroupTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstancesInputTypeDef = TypedDict(
    "_RequiredListInstancesInputTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalListInstancesInputTypeDef = TypedDict(
    "_OptionalListInstancesInputTypeDef",
    {
        "InstanceGroupId": str,
        "InstanceGroupTypes": List[InstanceGroupTypeType],
        "InstanceFleetId": str,
        "InstanceFleetType": InstanceFleetTypeType,
        "InstanceStates": List[InstanceStateType],
        "Marker": str,
    },
    total=False,
)


class ListInstancesInputTypeDef(
    _RequiredListInstancesInputTypeDef, _OptionalListInstancesInputTypeDef
):
    pass


ListInstancesOutputResponseTypeDef = TypedDict(
    "ListInstancesOutputResponseTypeDef",
    {
        "Instances": List["InstanceTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNotebookExecutionsInputTypeDef = TypedDict(
    "ListNotebookExecutionsInputTypeDef",
    {
        "EditorId": str,
        "Status": NotebookExecutionStatusType,
        "From": Union[datetime, str],
        "To": Union[datetime, str],
        "Marker": str,
    },
    total=False,
)

ListNotebookExecutionsOutputResponseTypeDef = TypedDict(
    "ListNotebookExecutionsOutputResponseTypeDef",
    {
        "NotebookExecutions": List["NotebookExecutionSummaryTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSecurityConfigurationsInputTypeDef = TypedDict(
    "ListSecurityConfigurationsInputTypeDef",
    {
        "Marker": str,
    },
    total=False,
)

ListSecurityConfigurationsOutputResponseTypeDef = TypedDict(
    "ListSecurityConfigurationsOutputResponseTypeDef",
    {
        "SecurityConfigurations": List["SecurityConfigurationSummaryTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStepsInputTypeDef = TypedDict(
    "_RequiredListStepsInputTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalListStepsInputTypeDef = TypedDict(
    "_OptionalListStepsInputTypeDef",
    {
        "StepStates": List[StepStateType],
        "StepIds": List[str],
        "Marker": str,
    },
    total=False,
)


class ListStepsInputTypeDef(_RequiredListStepsInputTypeDef, _OptionalListStepsInputTypeDef):
    pass


ListStepsOutputResponseTypeDef = TypedDict(
    "ListStepsOutputResponseTypeDef",
    {
        "Steps": List["StepSummaryTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStudioSessionMappingsInputTypeDef = TypedDict(
    "ListStudioSessionMappingsInputTypeDef",
    {
        "StudioId": str,
        "IdentityType": IdentityTypeType,
        "Marker": str,
    },
    total=False,
)

ListStudioSessionMappingsOutputResponseTypeDef = TypedDict(
    "ListStudioSessionMappingsOutputResponseTypeDef",
    {
        "SessionMappings": List["SessionMappingSummaryTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStudiosInputTypeDef = TypedDict(
    "ListStudiosInputTypeDef",
    {
        "Marker": str,
    },
    total=False,
)

ListStudiosOutputResponseTypeDef = TypedDict(
    "ListStudiosOutputResponseTypeDef",
    {
        "Studios": List["StudioSummaryTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ManagedScalingPolicyTypeDef = TypedDict(
    "ManagedScalingPolicyTypeDef",
    {
        "ComputeLimits": "ComputeLimitsTypeDef",
    },
    total=False,
)

MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredModifyClusterInputTypeDef = TypedDict(
    "_RequiredModifyClusterInputTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalModifyClusterInputTypeDef = TypedDict(
    "_OptionalModifyClusterInputTypeDef",
    {
        "StepConcurrencyLevel": int,
    },
    total=False,
)


class ModifyClusterInputTypeDef(
    _RequiredModifyClusterInputTypeDef, _OptionalModifyClusterInputTypeDef
):
    pass


ModifyClusterOutputResponseTypeDef = TypedDict(
    "ModifyClusterOutputResponseTypeDef",
    {
        "StepConcurrencyLevel": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyInstanceFleetInputTypeDef = TypedDict(
    "ModifyInstanceFleetInputTypeDef",
    {
        "ClusterId": str,
        "InstanceFleet": "InstanceFleetModifyConfigTypeDef",
    },
)

ModifyInstanceGroupsInputTypeDef = TypedDict(
    "ModifyInstanceGroupsInputTypeDef",
    {
        "ClusterId": str,
        "InstanceGroups": List["InstanceGroupModifyConfigTypeDef"],
    },
    total=False,
)

NotebookExecutionSummaryTypeDef = TypedDict(
    "NotebookExecutionSummaryTypeDef",
    {
        "NotebookExecutionId": str,
        "EditorId": str,
        "NotebookExecutionName": str,
        "Status": NotebookExecutionStatusType,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

NotebookExecutionTypeDef = TypedDict(
    "NotebookExecutionTypeDef",
    {
        "NotebookExecutionId": str,
        "EditorId": str,
        "ExecutionEngine": "ExecutionEngineConfigTypeDef",
        "NotebookExecutionName": str,
        "NotebookParams": str,
        "Status": NotebookExecutionStatusType,
        "StartTime": datetime,
        "EndTime": datetime,
        "Arn": str,
        "OutputNotebookURI": str,
        "LastStateChangeReason": str,
        "NotebookInstanceSecurityGroupId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

OnDemandCapacityReservationOptionsTypeDef = TypedDict(
    "OnDemandCapacityReservationOptionsTypeDef",
    {
        "UsageStrategy": Literal["use-capacity-reservations-first"],
        "CapacityReservationPreference": OnDemandCapacityReservationPreferenceType,
        "CapacityReservationResourceGroupArn": str,
    },
    total=False,
)

_RequiredOnDemandProvisioningSpecificationTypeDef = TypedDict(
    "_RequiredOnDemandProvisioningSpecificationTypeDef",
    {
        "AllocationStrategy": Literal["lowest-price"],
    },
)
_OptionalOnDemandProvisioningSpecificationTypeDef = TypedDict(
    "_OptionalOnDemandProvisioningSpecificationTypeDef",
    {
        "CapacityReservationOptions": "OnDemandCapacityReservationOptionsTypeDef",
    },
    total=False,
)


class OnDemandProvisioningSpecificationTypeDef(
    _RequiredOnDemandProvisioningSpecificationTypeDef,
    _OptionalOnDemandProvisioningSpecificationTypeDef,
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredPlacementGroupConfigTypeDef = TypedDict(
    "_RequiredPlacementGroupConfigTypeDef",
    {
        "InstanceRole": InstanceRoleTypeType,
    },
)
_OptionalPlacementGroupConfigTypeDef = TypedDict(
    "_OptionalPlacementGroupConfigTypeDef",
    {
        "PlacementStrategy": PlacementGroupStrategyType,
    },
    total=False,
)


class PlacementGroupConfigTypeDef(
    _RequiredPlacementGroupConfigTypeDef, _OptionalPlacementGroupConfigTypeDef
):
    pass


PlacementTypeTypeDef = TypedDict(
    "PlacementTypeTypeDef",
    {
        "AvailabilityZone": str,
        "AvailabilityZones": List[str],
    },
    total=False,
)

_RequiredPortRangeTypeDef = TypedDict(
    "_RequiredPortRangeTypeDef",
    {
        "MinRange": int,
    },
)
_OptionalPortRangeTypeDef = TypedDict(
    "_OptionalPortRangeTypeDef",
    {
        "MaxRange": int,
    },
    total=False,
)


class PortRangeTypeDef(_RequiredPortRangeTypeDef, _OptionalPortRangeTypeDef):
    pass


PutAutoScalingPolicyInputTypeDef = TypedDict(
    "PutAutoScalingPolicyInputTypeDef",
    {
        "ClusterId": str,
        "InstanceGroupId": str,
        "AutoScalingPolicy": "AutoScalingPolicyTypeDef",
    },
)

PutAutoScalingPolicyOutputResponseTypeDef = TypedDict(
    "PutAutoScalingPolicyOutputResponseTypeDef",
    {
        "ClusterId": str,
        "InstanceGroupId": str,
        "AutoScalingPolicy": "AutoScalingPolicyDescriptionTypeDef",
        "ClusterArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutBlockPublicAccessConfigurationInputTypeDef = TypedDict(
    "PutBlockPublicAccessConfigurationInputTypeDef",
    {
        "BlockPublicAccessConfiguration": "BlockPublicAccessConfigurationTypeDef",
    },
)

PutManagedScalingPolicyInputTypeDef = TypedDict(
    "PutManagedScalingPolicyInputTypeDef",
    {
        "ClusterId": str,
        "ManagedScalingPolicy": "ManagedScalingPolicyTypeDef",
    },
)

RemoveAutoScalingPolicyInputTypeDef = TypedDict(
    "RemoveAutoScalingPolicyInputTypeDef",
    {
        "ClusterId": str,
        "InstanceGroupId": str,
    },
)

RemoveManagedScalingPolicyInputTypeDef = TypedDict(
    "RemoveManagedScalingPolicyInputTypeDef",
    {
        "ClusterId": str,
    },
)

RemoveTagsInputTypeDef = TypedDict(
    "RemoveTagsInputTypeDef",
    {
        "ResourceId": str,
        "TagKeys": List[str],
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

_RequiredRunJobFlowInputTypeDef = TypedDict(
    "_RequiredRunJobFlowInputTypeDef",
    {
        "Name": str,
        "Instances": "JobFlowInstancesConfigTypeDef",
    },
)
_OptionalRunJobFlowInputTypeDef = TypedDict(
    "_OptionalRunJobFlowInputTypeDef",
    {
        "LogUri": str,
        "LogEncryptionKmsKeyId": str,
        "AdditionalInfo": str,
        "AmiVersion": str,
        "ReleaseLabel": str,
        "Steps": List["StepConfigTypeDef"],
        "BootstrapActions": List["BootstrapActionConfigTypeDef"],
        "SupportedProducts": List[str],
        "NewSupportedProducts": List["SupportedProductConfigTypeDef"],
        "Applications": List["ApplicationTypeDef"],
        "Configurations": List["ConfigurationTypeDef"],
        "VisibleToAllUsers": bool,
        "JobFlowRole": str,
        "ServiceRole": str,
        "Tags": List["TagTypeDef"],
        "SecurityConfiguration": str,
        "AutoScalingRole": str,
        "ScaleDownBehavior": ScaleDownBehaviorType,
        "CustomAmiId": str,
        "EbsRootVolumeSize": int,
        "RepoUpgradeOnBoot": RepoUpgradeOnBootType,
        "KerberosAttributes": "KerberosAttributesTypeDef",
        "StepConcurrencyLevel": int,
        "ManagedScalingPolicy": "ManagedScalingPolicyTypeDef",
        "PlacementGroupConfigs": List["PlacementGroupConfigTypeDef"],
    },
    total=False,
)


class RunJobFlowInputTypeDef(_RequiredRunJobFlowInputTypeDef, _OptionalRunJobFlowInputTypeDef):
    pass


RunJobFlowOutputResponseTypeDef = TypedDict(
    "RunJobFlowOutputResponseTypeDef",
    {
        "JobFlowId": str,
        "ClusterArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredScalingActionTypeDef = TypedDict(
    "_RequiredScalingActionTypeDef",
    {
        "SimpleScalingPolicyConfiguration": "SimpleScalingPolicyConfigurationTypeDef",
    },
)
_OptionalScalingActionTypeDef = TypedDict(
    "_OptionalScalingActionTypeDef",
    {
        "Market": MarketTypeType,
    },
    total=False,
)


class ScalingActionTypeDef(_RequiredScalingActionTypeDef, _OptionalScalingActionTypeDef):
    pass


ScalingConstraintsTypeDef = TypedDict(
    "ScalingConstraintsTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
    },
)

_RequiredScalingRuleTypeDef = TypedDict(
    "_RequiredScalingRuleTypeDef",
    {
        "Name": str,
        "Action": "ScalingActionTypeDef",
        "Trigger": "ScalingTriggerTypeDef",
    },
)
_OptionalScalingRuleTypeDef = TypedDict(
    "_OptionalScalingRuleTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class ScalingRuleTypeDef(_RequiredScalingRuleTypeDef, _OptionalScalingRuleTypeDef):
    pass


ScalingTriggerTypeDef = TypedDict(
    "ScalingTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": "CloudWatchAlarmDefinitionTypeDef",
    },
)

_RequiredScriptBootstrapActionConfigTypeDef = TypedDict(
    "_RequiredScriptBootstrapActionConfigTypeDef",
    {
        "Path": str,
    },
)
_OptionalScriptBootstrapActionConfigTypeDef = TypedDict(
    "_OptionalScriptBootstrapActionConfigTypeDef",
    {
        "Args": List[str],
    },
    total=False,
)


class ScriptBootstrapActionConfigTypeDef(
    _RequiredScriptBootstrapActionConfigTypeDef, _OptionalScriptBootstrapActionConfigTypeDef
):
    pass


SecurityConfigurationSummaryTypeDef = TypedDict(
    "SecurityConfigurationSummaryTypeDef",
    {
        "Name": str,
        "CreationDateTime": datetime,
    },
    total=False,
)

SessionMappingDetailTypeDef = TypedDict(
    "SessionMappingDetailTypeDef",
    {
        "StudioId": str,
        "IdentityId": str,
        "IdentityName": str,
        "IdentityType": IdentityTypeType,
        "SessionPolicyArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

SessionMappingSummaryTypeDef = TypedDict(
    "SessionMappingSummaryTypeDef",
    {
        "StudioId": str,
        "IdentityId": str,
        "IdentityName": str,
        "IdentityType": IdentityTypeType,
        "SessionPolicyArn": str,
        "CreationTime": datetime,
    },
    total=False,
)

SetTerminationProtectionInputTypeDef = TypedDict(
    "SetTerminationProtectionInputTypeDef",
    {
        "JobFlowIds": List[str],
        "TerminationProtected": bool,
    },
)

SetVisibleToAllUsersInputTypeDef = TypedDict(
    "SetVisibleToAllUsersInputTypeDef",
    {
        "JobFlowIds": List[str],
        "VisibleToAllUsers": bool,
    },
)

ShrinkPolicyTypeDef = TypedDict(
    "ShrinkPolicyTypeDef",
    {
        "DecommissionTimeout": int,
        "InstanceResizePolicy": "InstanceResizePolicyTypeDef",
    },
    total=False,
)

_RequiredSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_RequiredSimpleScalingPolicyConfigurationTypeDef",
    {
        "ScalingAdjustment": int,
    },
)
_OptionalSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_OptionalSimpleScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": AdjustmentTypeType,
        "CoolDown": int,
    },
    total=False,
)


class SimpleScalingPolicyConfigurationTypeDef(
    _RequiredSimpleScalingPolicyConfigurationTypeDef,
    _OptionalSimpleScalingPolicyConfigurationTypeDef,
):
    pass


_RequiredSpotProvisioningSpecificationTypeDef = TypedDict(
    "_RequiredSpotProvisioningSpecificationTypeDef",
    {
        "TimeoutDurationMinutes": int,
        "TimeoutAction": SpotProvisioningTimeoutActionType,
    },
)
_OptionalSpotProvisioningSpecificationTypeDef = TypedDict(
    "_OptionalSpotProvisioningSpecificationTypeDef",
    {
        "BlockDurationMinutes": int,
        "AllocationStrategy": Literal["capacity-optimized"],
    },
    total=False,
)


class SpotProvisioningSpecificationTypeDef(
    _RequiredSpotProvisioningSpecificationTypeDef, _OptionalSpotProvisioningSpecificationTypeDef
):
    pass


_RequiredStartNotebookExecutionInputTypeDef = TypedDict(
    "_RequiredStartNotebookExecutionInputTypeDef",
    {
        "EditorId": str,
        "RelativePath": str,
        "ExecutionEngine": "ExecutionEngineConfigTypeDef",
        "ServiceRole": str,
    },
)
_OptionalStartNotebookExecutionInputTypeDef = TypedDict(
    "_OptionalStartNotebookExecutionInputTypeDef",
    {
        "NotebookExecutionName": str,
        "NotebookParams": str,
        "NotebookInstanceSecurityGroupId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class StartNotebookExecutionInputTypeDef(
    _RequiredStartNotebookExecutionInputTypeDef, _OptionalStartNotebookExecutionInputTypeDef
):
    pass


StartNotebookExecutionOutputResponseTypeDef = TypedDict(
    "StartNotebookExecutionOutputResponseTypeDef",
    {
        "NotebookExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStepConfigTypeDef = TypedDict(
    "_RequiredStepConfigTypeDef",
    {
        "Name": str,
        "HadoopJarStep": "HadoopJarStepConfigTypeDef",
    },
)
_OptionalStepConfigTypeDef = TypedDict(
    "_OptionalStepConfigTypeDef",
    {
        "ActionOnFailure": ActionOnFailureType,
    },
    total=False,
)


class StepConfigTypeDef(_RequiredStepConfigTypeDef, _OptionalStepConfigTypeDef):
    pass


StepDetailTypeDef = TypedDict(
    "StepDetailTypeDef",
    {
        "StepConfig": "StepConfigTypeDef",
        "ExecutionStatusDetail": "StepExecutionStatusDetailTypeDef",
    },
)

_RequiredStepExecutionStatusDetailTypeDef = TypedDict(
    "_RequiredStepExecutionStatusDetailTypeDef",
    {
        "State": StepExecutionStateType,
        "CreationDateTime": datetime,
    },
)
_OptionalStepExecutionStatusDetailTypeDef = TypedDict(
    "_OptionalStepExecutionStatusDetailTypeDef",
    {
        "StartDateTime": datetime,
        "EndDateTime": datetime,
        "LastStateChangeReason": str,
    },
    total=False,
)


class StepExecutionStatusDetailTypeDef(
    _RequiredStepExecutionStatusDetailTypeDef, _OptionalStepExecutionStatusDetailTypeDef
):
    pass


StepStateChangeReasonTypeDef = TypedDict(
    "StepStateChangeReasonTypeDef",
    {
        "Code": Literal["NONE"],
        "Message": str,
    },
    total=False,
)

StepStatusTypeDef = TypedDict(
    "StepStatusTypeDef",
    {
        "State": StepStateType,
        "StateChangeReason": "StepStateChangeReasonTypeDef",
        "FailureDetails": "FailureDetailsTypeDef",
        "Timeline": "StepTimelineTypeDef",
    },
    total=False,
)

StepSummaryTypeDef = TypedDict(
    "StepSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Config": "HadoopStepConfigTypeDef",
        "ActionOnFailure": ActionOnFailureType,
        "Status": "StepStatusTypeDef",
    },
    total=False,
)

StepTimelineTypeDef = TypedDict(
    "StepTimelineTypeDef",
    {
        "CreationDateTime": datetime,
        "StartDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)

StepTypeDef = TypedDict(
    "StepTypeDef",
    {
        "Id": str,
        "Name": str,
        "Config": "HadoopStepConfigTypeDef",
        "ActionOnFailure": ActionOnFailureType,
        "Status": "StepStatusTypeDef",
    },
    total=False,
)

StopNotebookExecutionInputTypeDef = TypedDict(
    "StopNotebookExecutionInputTypeDef",
    {
        "NotebookExecutionId": str,
    },
)

StudioSummaryTypeDef = TypedDict(
    "StudioSummaryTypeDef",
    {
        "StudioId": str,
        "Name": str,
        "VpcId": str,
        "Description": str,
        "Url": str,
        "CreationTime": datetime,
    },
    total=False,
)

StudioTypeDef = TypedDict(
    "StudioTypeDef",
    {
        "StudioId": str,
        "StudioArn": str,
        "Name": str,
        "Description": str,
        "AuthMode": AuthModeType,
        "VpcId": str,
        "SubnetIds": List[str],
        "ServiceRole": str,
        "UserRole": str,
        "WorkspaceSecurityGroupId": str,
        "EngineSecurityGroupId": str,
        "Url": str,
        "CreationTime": datetime,
        "DefaultS3Location": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

SupportedProductConfigTypeDef = TypedDict(
    "SupportedProductConfigTypeDef",
    {
        "Name": str,
        "Args": List[str],
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TerminateJobFlowsInputTypeDef = TypedDict(
    "TerminateJobFlowsInputTypeDef",
    {
        "JobFlowIds": List[str],
    },
)

_RequiredUpdateStudioInputTypeDef = TypedDict(
    "_RequiredUpdateStudioInputTypeDef",
    {
        "StudioId": str,
    },
)
_OptionalUpdateStudioInputTypeDef = TypedDict(
    "_OptionalUpdateStudioInputTypeDef",
    {
        "Name": str,
        "Description": str,
        "SubnetIds": List[str],
        "DefaultS3Location": str,
    },
    total=False,
)


class UpdateStudioInputTypeDef(
    _RequiredUpdateStudioInputTypeDef, _OptionalUpdateStudioInputTypeDef
):
    pass


_RequiredUpdateStudioSessionMappingInputTypeDef = TypedDict(
    "_RequiredUpdateStudioSessionMappingInputTypeDef",
    {
        "StudioId": str,
        "IdentityType": IdentityTypeType,
        "SessionPolicyArn": str,
    },
)
_OptionalUpdateStudioSessionMappingInputTypeDef = TypedDict(
    "_OptionalUpdateStudioSessionMappingInputTypeDef",
    {
        "IdentityId": str,
        "IdentityName": str,
    },
    total=False,
)


class UpdateStudioSessionMappingInputTypeDef(
    _RequiredUpdateStudioSessionMappingInputTypeDef, _OptionalUpdateStudioSessionMappingInputTypeDef
):
    pass


_RequiredVolumeSpecificationTypeDef = TypedDict(
    "_RequiredVolumeSpecificationTypeDef",
    {
        "VolumeType": str,
        "SizeInGB": int,
    },
)
_OptionalVolumeSpecificationTypeDef = TypedDict(
    "_OptionalVolumeSpecificationTypeDef",
    {
        "Iops": int,
    },
    total=False,
)


class VolumeSpecificationTypeDef(
    _RequiredVolumeSpecificationTypeDef, _OptionalVolumeSpecificationTypeDef
):
    pass


WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
