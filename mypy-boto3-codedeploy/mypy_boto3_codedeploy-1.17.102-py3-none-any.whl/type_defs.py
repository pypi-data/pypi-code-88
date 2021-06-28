"""
Type annotations for codedeploy service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codedeploy.type_defs import AddTagsToOnPremisesInstancesInputTypeDef

    data: AddTagsToOnPremisesInstancesInputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ApplicationRevisionSortByType,
    AutoRollbackEventType,
    BundleTypeType,
    ComputePlatformType,
    DeploymentCreatorType,
    DeploymentOptionType,
    DeploymentReadyActionType,
    DeploymentStatusType,
    DeploymentTargetTypeType,
    DeploymentTypeType,
    DeploymentWaitTypeType,
    EC2TagFilterTypeType,
    ErrorCodeType,
    FileExistsBehaviorType,
    GreenFleetProvisioningActionType,
    InstanceActionType,
    InstanceStatusType,
    InstanceTypeType,
    LifecycleErrorCodeType,
    LifecycleEventStatusType,
    ListStateFilterActionType,
    MinimumHealthyHostsTypeType,
    OutdatedInstancesStrategyType,
    RegistrationStatusType,
    RevisionLocationTypeType,
    SortOrderType,
    StopStatusType,
    TagFilterTypeType,
    TargetFilterNameType,
    TargetLabelType,
    TargetStatusType,
    TrafficRoutingTypeType,
    TriggerEventTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddTagsToOnPremisesInstancesInputTypeDef",
    "AlarmConfigurationTypeDef",
    "AlarmTypeDef",
    "AppSpecContentTypeDef",
    "ApplicationInfoTypeDef",
    "AutoRollbackConfigurationTypeDef",
    "AutoScalingGroupTypeDef",
    "BatchGetApplicationRevisionsInputTypeDef",
    "BatchGetApplicationRevisionsOutputResponseTypeDef",
    "BatchGetApplicationsInputTypeDef",
    "BatchGetApplicationsOutputResponseTypeDef",
    "BatchGetDeploymentGroupsInputTypeDef",
    "BatchGetDeploymentGroupsOutputResponseTypeDef",
    "BatchGetDeploymentInstancesInputTypeDef",
    "BatchGetDeploymentInstancesOutputResponseTypeDef",
    "BatchGetDeploymentTargetsInputTypeDef",
    "BatchGetDeploymentTargetsOutputResponseTypeDef",
    "BatchGetDeploymentsInputTypeDef",
    "BatchGetDeploymentsOutputResponseTypeDef",
    "BatchGetOnPremisesInstancesInputTypeDef",
    "BatchGetOnPremisesInstancesOutputResponseTypeDef",
    "BlueGreenDeploymentConfigurationTypeDef",
    "BlueInstanceTerminationOptionTypeDef",
    "CloudFormationTargetTypeDef",
    "ContinueDeploymentInputTypeDef",
    "CreateApplicationInputTypeDef",
    "CreateApplicationOutputResponseTypeDef",
    "CreateDeploymentConfigInputTypeDef",
    "CreateDeploymentConfigOutputResponseTypeDef",
    "CreateDeploymentGroupInputTypeDef",
    "CreateDeploymentGroupOutputResponseTypeDef",
    "CreateDeploymentInputTypeDef",
    "CreateDeploymentOutputResponseTypeDef",
    "DeleteApplicationInputTypeDef",
    "DeleteDeploymentConfigInputTypeDef",
    "DeleteDeploymentGroupInputTypeDef",
    "DeleteDeploymentGroupOutputResponseTypeDef",
    "DeleteGitHubAccountTokenInputTypeDef",
    "DeleteGitHubAccountTokenOutputResponseTypeDef",
    "DeleteResourcesByExternalIdInputTypeDef",
    "DeploymentConfigInfoTypeDef",
    "DeploymentGroupInfoTypeDef",
    "DeploymentInfoTypeDef",
    "DeploymentOverviewTypeDef",
    "DeploymentReadyOptionTypeDef",
    "DeploymentStyleTypeDef",
    "DeploymentTargetTypeDef",
    "DeregisterOnPremisesInstanceInputTypeDef",
    "DiagnosticsTypeDef",
    "EC2TagFilterTypeDef",
    "EC2TagSetTypeDef",
    "ECSServiceTypeDef",
    "ECSTargetTypeDef",
    "ECSTaskSetTypeDef",
    "ELBInfoTypeDef",
    "ErrorInformationTypeDef",
    "GenericRevisionInfoTypeDef",
    "GetApplicationInputTypeDef",
    "GetApplicationOutputResponseTypeDef",
    "GetApplicationRevisionInputTypeDef",
    "GetApplicationRevisionOutputResponseTypeDef",
    "GetDeploymentConfigInputTypeDef",
    "GetDeploymentConfigOutputResponseTypeDef",
    "GetDeploymentGroupInputTypeDef",
    "GetDeploymentGroupOutputResponseTypeDef",
    "GetDeploymentInputTypeDef",
    "GetDeploymentInstanceInputTypeDef",
    "GetDeploymentInstanceOutputResponseTypeDef",
    "GetDeploymentOutputResponseTypeDef",
    "GetDeploymentTargetInputTypeDef",
    "GetDeploymentTargetOutputResponseTypeDef",
    "GetOnPremisesInstanceInputTypeDef",
    "GetOnPremisesInstanceOutputResponseTypeDef",
    "GitHubLocationTypeDef",
    "GreenFleetProvisioningOptionTypeDef",
    "InstanceInfoTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTargetTypeDef",
    "LambdaFunctionInfoTypeDef",
    "LambdaTargetTypeDef",
    "LastDeploymentInfoTypeDef",
    "LifecycleEventTypeDef",
    "ListApplicationRevisionsInputTypeDef",
    "ListApplicationRevisionsOutputResponseTypeDef",
    "ListApplicationsInputTypeDef",
    "ListApplicationsOutputResponseTypeDef",
    "ListDeploymentConfigsInputTypeDef",
    "ListDeploymentConfigsOutputResponseTypeDef",
    "ListDeploymentGroupsInputTypeDef",
    "ListDeploymentGroupsOutputResponseTypeDef",
    "ListDeploymentInstancesInputTypeDef",
    "ListDeploymentInstancesOutputResponseTypeDef",
    "ListDeploymentTargetsInputTypeDef",
    "ListDeploymentTargetsOutputResponseTypeDef",
    "ListDeploymentsInputTypeDef",
    "ListDeploymentsOutputResponseTypeDef",
    "ListGitHubAccountTokenNamesInputTypeDef",
    "ListGitHubAccountTokenNamesOutputResponseTypeDef",
    "ListOnPremisesInstancesInputTypeDef",
    "ListOnPremisesInstancesOutputResponseTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputResponseTypeDef",
    "LoadBalancerInfoTypeDef",
    "MinimumHealthyHostsTypeDef",
    "OnPremisesTagSetTypeDef",
    "PaginatorConfigTypeDef",
    "PutLifecycleEventHookExecutionStatusInputTypeDef",
    "PutLifecycleEventHookExecutionStatusOutputResponseTypeDef",
    "RawStringTypeDef",
    "RegisterApplicationRevisionInputTypeDef",
    "RegisterOnPremisesInstanceInputTypeDef",
    "RelatedDeploymentsTypeDef",
    "RemoveTagsFromOnPremisesInstancesInputTypeDef",
    "ResponseMetadataTypeDef",
    "RevisionInfoTypeDef",
    "RevisionLocationTypeDef",
    "RollbackInfoTypeDef",
    "S3LocationTypeDef",
    "SkipWaitTimeForInstanceTerminationInputTypeDef",
    "StopDeploymentInputTypeDef",
    "StopDeploymentOutputResponseTypeDef",
    "TagFilterTypeDef",
    "TagResourceInputTypeDef",
    "TagTypeDef",
    "TargetGroupInfoTypeDef",
    "TargetGroupPairInfoTypeDef",
    "TargetInstancesTypeDef",
    "TimeBasedCanaryTypeDef",
    "TimeBasedLinearTypeDef",
    "TimeRangeTypeDef",
    "TrafficRouteTypeDef",
    "TrafficRoutingConfigTypeDef",
    "TriggerConfigTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateApplicationInputTypeDef",
    "UpdateDeploymentGroupInputTypeDef",
    "UpdateDeploymentGroupOutputResponseTypeDef",
    "WaiterConfigTypeDef",
)

AddTagsToOnPremisesInstancesInputTypeDef = TypedDict(
    "AddTagsToOnPremisesInstancesInputTypeDef",
    {
        "tags": List["TagTypeDef"],
        "instanceNames": List[str],
    },
)

AlarmConfigurationTypeDef = TypedDict(
    "AlarmConfigurationTypeDef",
    {
        "enabled": bool,
        "ignorePollAlarmFailure": bool,
        "alarms": List["AlarmTypeDef"],
    },
    total=False,
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "name": str,
    },
    total=False,
)

AppSpecContentTypeDef = TypedDict(
    "AppSpecContentTypeDef",
    {
        "content": str,
        "sha256": str,
    },
    total=False,
)

ApplicationInfoTypeDef = TypedDict(
    "ApplicationInfoTypeDef",
    {
        "applicationId": str,
        "applicationName": str,
        "createTime": datetime,
        "linkedToGitHub": bool,
        "gitHubAccountName": str,
        "computePlatform": ComputePlatformType,
    },
    total=False,
)

AutoRollbackConfigurationTypeDef = TypedDict(
    "AutoRollbackConfigurationTypeDef",
    {
        "enabled": bool,
        "events": List[AutoRollbackEventType],
    },
    total=False,
)

AutoScalingGroupTypeDef = TypedDict(
    "AutoScalingGroupTypeDef",
    {
        "name": str,
        "hook": str,
    },
    total=False,
)

BatchGetApplicationRevisionsInputTypeDef = TypedDict(
    "BatchGetApplicationRevisionsInputTypeDef",
    {
        "applicationName": str,
        "revisions": List["RevisionLocationTypeDef"],
    },
)

BatchGetApplicationRevisionsOutputResponseTypeDef = TypedDict(
    "BatchGetApplicationRevisionsOutputResponseTypeDef",
    {
        "applicationName": str,
        "errorMessage": str,
        "revisions": List["RevisionInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetApplicationsInputTypeDef = TypedDict(
    "BatchGetApplicationsInputTypeDef",
    {
        "applicationNames": List[str],
    },
)

BatchGetApplicationsOutputResponseTypeDef = TypedDict(
    "BatchGetApplicationsOutputResponseTypeDef",
    {
        "applicationsInfo": List["ApplicationInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDeploymentGroupsInputTypeDef = TypedDict(
    "BatchGetDeploymentGroupsInputTypeDef",
    {
        "applicationName": str,
        "deploymentGroupNames": List[str],
    },
)

BatchGetDeploymentGroupsOutputResponseTypeDef = TypedDict(
    "BatchGetDeploymentGroupsOutputResponseTypeDef",
    {
        "deploymentGroupsInfo": List["DeploymentGroupInfoTypeDef"],
        "errorMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDeploymentInstancesInputTypeDef = TypedDict(
    "BatchGetDeploymentInstancesInputTypeDef",
    {
        "deploymentId": str,
        "instanceIds": List[str],
    },
)

BatchGetDeploymentInstancesOutputResponseTypeDef = TypedDict(
    "BatchGetDeploymentInstancesOutputResponseTypeDef",
    {
        "instancesSummary": List["InstanceSummaryTypeDef"],
        "errorMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDeploymentTargetsInputTypeDef = TypedDict(
    "BatchGetDeploymentTargetsInputTypeDef",
    {
        "deploymentId": str,
        "targetIds": List[str],
    },
    total=False,
)

BatchGetDeploymentTargetsOutputResponseTypeDef = TypedDict(
    "BatchGetDeploymentTargetsOutputResponseTypeDef",
    {
        "deploymentTargets": List["DeploymentTargetTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDeploymentsInputTypeDef = TypedDict(
    "BatchGetDeploymentsInputTypeDef",
    {
        "deploymentIds": List[str],
    },
)

BatchGetDeploymentsOutputResponseTypeDef = TypedDict(
    "BatchGetDeploymentsOutputResponseTypeDef",
    {
        "deploymentsInfo": List["DeploymentInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetOnPremisesInstancesInputTypeDef = TypedDict(
    "BatchGetOnPremisesInstancesInputTypeDef",
    {
        "instanceNames": List[str],
    },
)

BatchGetOnPremisesInstancesOutputResponseTypeDef = TypedDict(
    "BatchGetOnPremisesInstancesOutputResponseTypeDef",
    {
        "instanceInfos": List["InstanceInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BlueGreenDeploymentConfigurationTypeDef = TypedDict(
    "BlueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": "BlueInstanceTerminationOptionTypeDef",
        "deploymentReadyOption": "DeploymentReadyOptionTypeDef",
        "greenFleetProvisioningOption": "GreenFleetProvisioningOptionTypeDef",
    },
    total=False,
)

BlueInstanceTerminationOptionTypeDef = TypedDict(
    "BlueInstanceTerminationOptionTypeDef",
    {
        "action": InstanceActionType,
        "terminationWaitTimeInMinutes": int,
    },
    total=False,
)

CloudFormationTargetTypeDef = TypedDict(
    "CloudFormationTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List["LifecycleEventTypeDef"],
        "status": TargetStatusType,
        "resourceType": str,
        "targetVersionWeight": float,
    },
    total=False,
)

ContinueDeploymentInputTypeDef = TypedDict(
    "ContinueDeploymentInputTypeDef",
    {
        "deploymentId": str,
        "deploymentWaitType": DeploymentWaitTypeType,
    },
    total=False,
)

_RequiredCreateApplicationInputTypeDef = TypedDict(
    "_RequiredCreateApplicationInputTypeDef",
    {
        "applicationName": str,
    },
)
_OptionalCreateApplicationInputTypeDef = TypedDict(
    "_OptionalCreateApplicationInputTypeDef",
    {
        "computePlatform": ComputePlatformType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateApplicationInputTypeDef(
    _RequiredCreateApplicationInputTypeDef, _OptionalCreateApplicationInputTypeDef
):
    pass


CreateApplicationOutputResponseTypeDef = TypedDict(
    "CreateApplicationOutputResponseTypeDef",
    {
        "applicationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeploymentConfigInputTypeDef = TypedDict(
    "_RequiredCreateDeploymentConfigInputTypeDef",
    {
        "deploymentConfigName": str,
    },
)
_OptionalCreateDeploymentConfigInputTypeDef = TypedDict(
    "_OptionalCreateDeploymentConfigInputTypeDef",
    {
        "minimumHealthyHosts": "MinimumHealthyHostsTypeDef",
        "trafficRoutingConfig": "TrafficRoutingConfigTypeDef",
        "computePlatform": ComputePlatformType,
    },
    total=False,
)


class CreateDeploymentConfigInputTypeDef(
    _RequiredCreateDeploymentConfigInputTypeDef, _OptionalCreateDeploymentConfigInputTypeDef
):
    pass


CreateDeploymentConfigOutputResponseTypeDef = TypedDict(
    "CreateDeploymentConfigOutputResponseTypeDef",
    {
        "deploymentConfigId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeploymentGroupInputTypeDef = TypedDict(
    "_RequiredCreateDeploymentGroupInputTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
        "serviceRoleArn": str,
    },
)
_OptionalCreateDeploymentGroupInputTypeDef = TypedDict(
    "_OptionalCreateDeploymentGroupInputTypeDef",
    {
        "deploymentConfigName": str,
        "ec2TagFilters": List["EC2TagFilterTypeDef"],
        "onPremisesInstanceTagFilters": List["TagFilterTypeDef"],
        "autoScalingGroups": List[str],
        "triggerConfigurations": List["TriggerConfigTypeDef"],
        "alarmConfiguration": "AlarmConfigurationTypeDef",
        "autoRollbackConfiguration": "AutoRollbackConfigurationTypeDef",
        "outdatedInstancesStrategy": OutdatedInstancesStrategyType,
        "deploymentStyle": "DeploymentStyleTypeDef",
        "blueGreenDeploymentConfiguration": "BlueGreenDeploymentConfigurationTypeDef",
        "loadBalancerInfo": "LoadBalancerInfoTypeDef",
        "ec2TagSet": "EC2TagSetTypeDef",
        "ecsServices": List["ECSServiceTypeDef"],
        "onPremisesTagSet": "OnPremisesTagSetTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDeploymentGroupInputTypeDef(
    _RequiredCreateDeploymentGroupInputTypeDef, _OptionalCreateDeploymentGroupInputTypeDef
):
    pass


CreateDeploymentGroupOutputResponseTypeDef = TypedDict(
    "CreateDeploymentGroupOutputResponseTypeDef",
    {
        "deploymentGroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeploymentInputTypeDef = TypedDict(
    "_RequiredCreateDeploymentInputTypeDef",
    {
        "applicationName": str,
    },
)
_OptionalCreateDeploymentInputTypeDef = TypedDict(
    "_OptionalCreateDeploymentInputTypeDef",
    {
        "deploymentGroupName": str,
        "revision": "RevisionLocationTypeDef",
        "deploymentConfigName": str,
        "description": str,
        "ignoreApplicationStopFailures": bool,
        "targetInstances": "TargetInstancesTypeDef",
        "autoRollbackConfiguration": "AutoRollbackConfigurationTypeDef",
        "updateOutdatedInstancesOnly": bool,
        "fileExistsBehavior": FileExistsBehaviorType,
    },
    total=False,
)


class CreateDeploymentInputTypeDef(
    _RequiredCreateDeploymentInputTypeDef, _OptionalCreateDeploymentInputTypeDef
):
    pass


CreateDeploymentOutputResponseTypeDef = TypedDict(
    "CreateDeploymentOutputResponseTypeDef",
    {
        "deploymentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationInputTypeDef = TypedDict(
    "DeleteApplicationInputTypeDef",
    {
        "applicationName": str,
    },
)

DeleteDeploymentConfigInputTypeDef = TypedDict(
    "DeleteDeploymentConfigInputTypeDef",
    {
        "deploymentConfigName": str,
    },
)

DeleteDeploymentGroupInputTypeDef = TypedDict(
    "DeleteDeploymentGroupInputTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
    },
)

DeleteDeploymentGroupOutputResponseTypeDef = TypedDict(
    "DeleteDeploymentGroupOutputResponseTypeDef",
    {
        "hooksNotCleanedUp": List["AutoScalingGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGitHubAccountTokenInputTypeDef = TypedDict(
    "DeleteGitHubAccountTokenInputTypeDef",
    {
        "tokenName": str,
    },
    total=False,
)

DeleteGitHubAccountTokenOutputResponseTypeDef = TypedDict(
    "DeleteGitHubAccountTokenOutputResponseTypeDef",
    {
        "tokenName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcesByExternalIdInputTypeDef = TypedDict(
    "DeleteResourcesByExternalIdInputTypeDef",
    {
        "externalId": str,
    },
    total=False,
)

DeploymentConfigInfoTypeDef = TypedDict(
    "DeploymentConfigInfoTypeDef",
    {
        "deploymentConfigId": str,
        "deploymentConfigName": str,
        "minimumHealthyHosts": "MinimumHealthyHostsTypeDef",
        "createTime": datetime,
        "computePlatform": ComputePlatformType,
        "trafficRoutingConfig": "TrafficRoutingConfigTypeDef",
    },
    total=False,
)

DeploymentGroupInfoTypeDef = TypedDict(
    "DeploymentGroupInfoTypeDef",
    {
        "applicationName": str,
        "deploymentGroupId": str,
        "deploymentGroupName": str,
        "deploymentConfigName": str,
        "ec2TagFilters": List["EC2TagFilterTypeDef"],
        "onPremisesInstanceTagFilters": List["TagFilterTypeDef"],
        "autoScalingGroups": List["AutoScalingGroupTypeDef"],
        "serviceRoleArn": str,
        "targetRevision": "RevisionLocationTypeDef",
        "triggerConfigurations": List["TriggerConfigTypeDef"],
        "alarmConfiguration": "AlarmConfigurationTypeDef",
        "autoRollbackConfiguration": "AutoRollbackConfigurationTypeDef",
        "deploymentStyle": "DeploymentStyleTypeDef",
        "outdatedInstancesStrategy": OutdatedInstancesStrategyType,
        "blueGreenDeploymentConfiguration": "BlueGreenDeploymentConfigurationTypeDef",
        "loadBalancerInfo": "LoadBalancerInfoTypeDef",
        "lastSuccessfulDeployment": "LastDeploymentInfoTypeDef",
        "lastAttemptedDeployment": "LastDeploymentInfoTypeDef",
        "ec2TagSet": "EC2TagSetTypeDef",
        "onPremisesTagSet": "OnPremisesTagSetTypeDef",
        "computePlatform": ComputePlatformType,
        "ecsServices": List["ECSServiceTypeDef"],
    },
    total=False,
)

DeploymentInfoTypeDef = TypedDict(
    "DeploymentInfoTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
        "deploymentConfigName": str,
        "deploymentId": str,
        "previousRevision": "RevisionLocationTypeDef",
        "revision": "RevisionLocationTypeDef",
        "status": DeploymentStatusType,
        "errorInformation": "ErrorInformationTypeDef",
        "createTime": datetime,
        "startTime": datetime,
        "completeTime": datetime,
        "deploymentOverview": "DeploymentOverviewTypeDef",
        "description": str,
        "creator": DeploymentCreatorType,
        "ignoreApplicationStopFailures": bool,
        "autoRollbackConfiguration": "AutoRollbackConfigurationTypeDef",
        "updateOutdatedInstancesOnly": bool,
        "rollbackInfo": "RollbackInfoTypeDef",
        "deploymentStyle": "DeploymentStyleTypeDef",
        "targetInstances": "TargetInstancesTypeDef",
        "instanceTerminationWaitTimeStarted": bool,
        "blueGreenDeploymentConfiguration": "BlueGreenDeploymentConfigurationTypeDef",
        "loadBalancerInfo": "LoadBalancerInfoTypeDef",
        "additionalDeploymentStatusInfo": str,
        "fileExistsBehavior": FileExistsBehaviorType,
        "deploymentStatusMessages": List[str],
        "computePlatform": ComputePlatformType,
        "externalId": str,
        "relatedDeployments": "RelatedDeploymentsTypeDef",
    },
    total=False,
)

DeploymentOverviewTypeDef = TypedDict(
    "DeploymentOverviewTypeDef",
    {
        "Pending": int,
        "InProgress": int,
        "Succeeded": int,
        "Failed": int,
        "Skipped": int,
        "Ready": int,
    },
    total=False,
)

DeploymentReadyOptionTypeDef = TypedDict(
    "DeploymentReadyOptionTypeDef",
    {
        "actionOnTimeout": DeploymentReadyActionType,
        "waitTimeInMinutes": int,
    },
    total=False,
)

DeploymentStyleTypeDef = TypedDict(
    "DeploymentStyleTypeDef",
    {
        "deploymentType": DeploymentTypeType,
        "deploymentOption": DeploymentOptionType,
    },
    total=False,
)

DeploymentTargetTypeDef = TypedDict(
    "DeploymentTargetTypeDef",
    {
        "deploymentTargetType": DeploymentTargetTypeType,
        "instanceTarget": "InstanceTargetTypeDef",
        "lambdaTarget": "LambdaTargetTypeDef",
        "ecsTarget": "ECSTargetTypeDef",
        "cloudFormationTarget": "CloudFormationTargetTypeDef",
    },
    total=False,
)

DeregisterOnPremisesInstanceInputTypeDef = TypedDict(
    "DeregisterOnPremisesInstanceInputTypeDef",
    {
        "instanceName": str,
    },
)

DiagnosticsTypeDef = TypedDict(
    "DiagnosticsTypeDef",
    {
        "errorCode": LifecycleErrorCodeType,
        "scriptName": str,
        "message": str,
        "logTail": str,
    },
    total=False,
)

EC2TagFilterTypeDef = TypedDict(
    "EC2TagFilterTypeDef",
    {
        "Key": str,
        "Value": str,
        "Type": EC2TagFilterTypeType,
    },
    total=False,
)

EC2TagSetTypeDef = TypedDict(
    "EC2TagSetTypeDef",
    {
        "ec2TagSetList": List[List["EC2TagFilterTypeDef"]],
    },
    total=False,
)

ECSServiceTypeDef = TypedDict(
    "ECSServiceTypeDef",
    {
        "serviceName": str,
        "clusterName": str,
    },
    total=False,
)

ECSTargetTypeDef = TypedDict(
    "ECSTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List["LifecycleEventTypeDef"],
        "status": TargetStatusType,
        "taskSetsInfo": List["ECSTaskSetTypeDef"],
    },
    total=False,
)

ECSTaskSetTypeDef = TypedDict(
    "ECSTaskSetTypeDef",
    {
        "identifer": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "status": str,
        "trafficWeight": float,
        "targetGroup": "TargetGroupInfoTypeDef",
        "taskSetLabel": TargetLabelType,
    },
    total=False,
)

ELBInfoTypeDef = TypedDict(
    "ELBInfoTypeDef",
    {
        "name": str,
    },
    total=False,
)

ErrorInformationTypeDef = TypedDict(
    "ErrorInformationTypeDef",
    {
        "code": ErrorCodeType,
        "message": str,
    },
    total=False,
)

GenericRevisionInfoTypeDef = TypedDict(
    "GenericRevisionInfoTypeDef",
    {
        "description": str,
        "deploymentGroups": List[str],
        "firstUsedTime": datetime,
        "lastUsedTime": datetime,
        "registerTime": datetime,
    },
    total=False,
)

GetApplicationInputTypeDef = TypedDict(
    "GetApplicationInputTypeDef",
    {
        "applicationName": str,
    },
)

GetApplicationOutputResponseTypeDef = TypedDict(
    "GetApplicationOutputResponseTypeDef",
    {
        "application": "ApplicationInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationRevisionInputTypeDef = TypedDict(
    "GetApplicationRevisionInputTypeDef",
    {
        "applicationName": str,
        "revision": "RevisionLocationTypeDef",
    },
)

GetApplicationRevisionOutputResponseTypeDef = TypedDict(
    "GetApplicationRevisionOutputResponseTypeDef",
    {
        "applicationName": str,
        "revision": "RevisionLocationTypeDef",
        "revisionInfo": "GenericRevisionInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentConfigInputTypeDef = TypedDict(
    "GetDeploymentConfigInputTypeDef",
    {
        "deploymentConfigName": str,
    },
)

GetDeploymentConfigOutputResponseTypeDef = TypedDict(
    "GetDeploymentConfigOutputResponseTypeDef",
    {
        "deploymentConfigInfo": "DeploymentConfigInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentGroupInputTypeDef = TypedDict(
    "GetDeploymentGroupInputTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
    },
)

GetDeploymentGroupOutputResponseTypeDef = TypedDict(
    "GetDeploymentGroupOutputResponseTypeDef",
    {
        "deploymentGroupInfo": "DeploymentGroupInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentInputTypeDef = TypedDict(
    "GetDeploymentInputTypeDef",
    {
        "deploymentId": str,
    },
)

GetDeploymentInstanceInputTypeDef = TypedDict(
    "GetDeploymentInstanceInputTypeDef",
    {
        "deploymentId": str,
        "instanceId": str,
    },
)

GetDeploymentInstanceOutputResponseTypeDef = TypedDict(
    "GetDeploymentInstanceOutputResponseTypeDef",
    {
        "instanceSummary": "InstanceSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentOutputResponseTypeDef = TypedDict(
    "GetDeploymentOutputResponseTypeDef",
    {
        "deploymentInfo": "DeploymentInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentTargetInputTypeDef = TypedDict(
    "GetDeploymentTargetInputTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
    },
    total=False,
)

GetDeploymentTargetOutputResponseTypeDef = TypedDict(
    "GetDeploymentTargetOutputResponseTypeDef",
    {
        "deploymentTarget": "DeploymentTargetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOnPremisesInstanceInputTypeDef = TypedDict(
    "GetOnPremisesInstanceInputTypeDef",
    {
        "instanceName": str,
    },
)

GetOnPremisesInstanceOutputResponseTypeDef = TypedDict(
    "GetOnPremisesInstanceOutputResponseTypeDef",
    {
        "instanceInfo": "InstanceInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GitHubLocationTypeDef = TypedDict(
    "GitHubLocationTypeDef",
    {
        "repository": str,
        "commitId": str,
    },
    total=False,
)

GreenFleetProvisioningOptionTypeDef = TypedDict(
    "GreenFleetProvisioningOptionTypeDef",
    {
        "action": GreenFleetProvisioningActionType,
    },
    total=False,
)

InstanceInfoTypeDef = TypedDict(
    "InstanceInfoTypeDef",
    {
        "instanceName": str,
        "iamSessionArn": str,
        "iamUserArn": str,
        "instanceArn": str,
        "registerTime": datetime,
        "deregisterTime": datetime,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef",
    {
        "deploymentId": str,
        "instanceId": str,
        "status": InstanceStatusType,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List["LifecycleEventTypeDef"],
        "instanceType": InstanceTypeType,
    },
    total=False,
)

InstanceTargetTypeDef = TypedDict(
    "InstanceTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "status": TargetStatusType,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List["LifecycleEventTypeDef"],
        "instanceLabel": TargetLabelType,
    },
    total=False,
)

LambdaFunctionInfoTypeDef = TypedDict(
    "LambdaFunctionInfoTypeDef",
    {
        "functionName": str,
        "functionAlias": str,
        "currentVersion": str,
        "targetVersion": str,
        "targetVersionWeight": float,
    },
    total=False,
)

LambdaTargetTypeDef = TypedDict(
    "LambdaTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "status": TargetStatusType,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List["LifecycleEventTypeDef"],
        "lambdaFunctionInfo": "LambdaFunctionInfoTypeDef",
    },
    total=False,
)

LastDeploymentInfoTypeDef = TypedDict(
    "LastDeploymentInfoTypeDef",
    {
        "deploymentId": str,
        "status": DeploymentStatusType,
        "endTime": datetime,
        "createTime": datetime,
    },
    total=False,
)

LifecycleEventTypeDef = TypedDict(
    "LifecycleEventTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": "DiagnosticsTypeDef",
        "startTime": datetime,
        "endTime": datetime,
        "status": LifecycleEventStatusType,
    },
    total=False,
)

_RequiredListApplicationRevisionsInputTypeDef = TypedDict(
    "_RequiredListApplicationRevisionsInputTypeDef",
    {
        "applicationName": str,
    },
)
_OptionalListApplicationRevisionsInputTypeDef = TypedDict(
    "_OptionalListApplicationRevisionsInputTypeDef",
    {
        "sortBy": ApplicationRevisionSortByType,
        "sortOrder": SortOrderType,
        "s3Bucket": str,
        "s3KeyPrefix": str,
        "deployed": ListStateFilterActionType,
        "nextToken": str,
    },
    total=False,
)


class ListApplicationRevisionsInputTypeDef(
    _RequiredListApplicationRevisionsInputTypeDef, _OptionalListApplicationRevisionsInputTypeDef
):
    pass


ListApplicationRevisionsOutputResponseTypeDef = TypedDict(
    "ListApplicationRevisionsOutputResponseTypeDef",
    {
        "revisions": List["RevisionLocationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationsInputTypeDef = TypedDict(
    "ListApplicationsInputTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ListApplicationsOutputResponseTypeDef = TypedDict(
    "ListApplicationsOutputResponseTypeDef",
    {
        "applications": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentConfigsInputTypeDef = TypedDict(
    "ListDeploymentConfigsInputTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ListDeploymentConfigsOutputResponseTypeDef = TypedDict(
    "ListDeploymentConfigsOutputResponseTypeDef",
    {
        "deploymentConfigsList": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDeploymentGroupsInputTypeDef = TypedDict(
    "_RequiredListDeploymentGroupsInputTypeDef",
    {
        "applicationName": str,
    },
)
_OptionalListDeploymentGroupsInputTypeDef = TypedDict(
    "_OptionalListDeploymentGroupsInputTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListDeploymentGroupsInputTypeDef(
    _RequiredListDeploymentGroupsInputTypeDef, _OptionalListDeploymentGroupsInputTypeDef
):
    pass


ListDeploymentGroupsOutputResponseTypeDef = TypedDict(
    "ListDeploymentGroupsOutputResponseTypeDef",
    {
        "applicationName": str,
        "deploymentGroups": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDeploymentInstancesInputTypeDef = TypedDict(
    "_RequiredListDeploymentInstancesInputTypeDef",
    {
        "deploymentId": str,
    },
)
_OptionalListDeploymentInstancesInputTypeDef = TypedDict(
    "_OptionalListDeploymentInstancesInputTypeDef",
    {
        "nextToken": str,
        "instanceStatusFilter": List[InstanceStatusType],
        "instanceTypeFilter": List[InstanceTypeType],
    },
    total=False,
)


class ListDeploymentInstancesInputTypeDef(
    _RequiredListDeploymentInstancesInputTypeDef, _OptionalListDeploymentInstancesInputTypeDef
):
    pass


ListDeploymentInstancesOutputResponseTypeDef = TypedDict(
    "ListDeploymentInstancesOutputResponseTypeDef",
    {
        "instancesList": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentTargetsInputTypeDef = TypedDict(
    "ListDeploymentTargetsInputTypeDef",
    {
        "deploymentId": str,
        "nextToken": str,
        "targetFilters": Dict[TargetFilterNameType, List[str]],
    },
    total=False,
)

ListDeploymentTargetsOutputResponseTypeDef = TypedDict(
    "ListDeploymentTargetsOutputResponseTypeDef",
    {
        "targetIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentsInputTypeDef = TypedDict(
    "ListDeploymentsInputTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
        "externalId": str,
        "includeOnlyStatuses": List[DeploymentStatusType],
        "createTimeRange": "TimeRangeTypeDef",
        "nextToken": str,
    },
    total=False,
)

ListDeploymentsOutputResponseTypeDef = TypedDict(
    "ListDeploymentsOutputResponseTypeDef",
    {
        "deployments": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGitHubAccountTokenNamesInputTypeDef = TypedDict(
    "ListGitHubAccountTokenNamesInputTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ListGitHubAccountTokenNamesOutputResponseTypeDef = TypedDict(
    "ListGitHubAccountTokenNamesOutputResponseTypeDef",
    {
        "tokenNameList": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOnPremisesInstancesInputTypeDef = TypedDict(
    "ListOnPremisesInstancesInputTypeDef",
    {
        "registrationStatus": RegistrationStatusType,
        "tagFilters": List["TagFilterTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListOnPremisesInstancesOutputResponseTypeDef = TypedDict(
    "ListOnPremisesInstancesOutputResponseTypeDef",
    {
        "instanceNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceInputTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceInputTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListTagsForResourceInputTypeDef(
    _RequiredListTagsForResourceInputTypeDef, _OptionalListTagsForResourceInputTypeDef
):
    pass


ListTagsForResourceOutputResponseTypeDef = TypedDict(
    "ListTagsForResourceOutputResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoadBalancerInfoTypeDef = TypedDict(
    "LoadBalancerInfoTypeDef",
    {
        "elbInfoList": List["ELBInfoTypeDef"],
        "targetGroupInfoList": List["TargetGroupInfoTypeDef"],
        "targetGroupPairInfoList": List["TargetGroupPairInfoTypeDef"],
    },
    total=False,
)

MinimumHealthyHostsTypeDef = TypedDict(
    "MinimumHealthyHostsTypeDef",
    {
        "type": MinimumHealthyHostsTypeType,
        "value": int,
    },
    total=False,
)

OnPremisesTagSetTypeDef = TypedDict(
    "OnPremisesTagSetTypeDef",
    {
        "onPremisesTagSetList": List[List["TagFilterTypeDef"]],
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

PutLifecycleEventHookExecutionStatusInputTypeDef = TypedDict(
    "PutLifecycleEventHookExecutionStatusInputTypeDef",
    {
        "deploymentId": str,
        "lifecycleEventHookExecutionId": str,
        "status": LifecycleEventStatusType,
    },
    total=False,
)

PutLifecycleEventHookExecutionStatusOutputResponseTypeDef = TypedDict(
    "PutLifecycleEventHookExecutionStatusOutputResponseTypeDef",
    {
        "lifecycleEventHookExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RawStringTypeDef = TypedDict(
    "RawStringTypeDef",
    {
        "content": str,
        "sha256": str,
    },
    total=False,
)

_RequiredRegisterApplicationRevisionInputTypeDef = TypedDict(
    "_RequiredRegisterApplicationRevisionInputTypeDef",
    {
        "applicationName": str,
        "revision": "RevisionLocationTypeDef",
    },
)
_OptionalRegisterApplicationRevisionInputTypeDef = TypedDict(
    "_OptionalRegisterApplicationRevisionInputTypeDef",
    {
        "description": str,
    },
    total=False,
)


class RegisterApplicationRevisionInputTypeDef(
    _RequiredRegisterApplicationRevisionInputTypeDef,
    _OptionalRegisterApplicationRevisionInputTypeDef,
):
    pass


_RequiredRegisterOnPremisesInstanceInputTypeDef = TypedDict(
    "_RequiredRegisterOnPremisesInstanceInputTypeDef",
    {
        "instanceName": str,
    },
)
_OptionalRegisterOnPremisesInstanceInputTypeDef = TypedDict(
    "_OptionalRegisterOnPremisesInstanceInputTypeDef",
    {
        "iamSessionArn": str,
        "iamUserArn": str,
    },
    total=False,
)


class RegisterOnPremisesInstanceInputTypeDef(
    _RequiredRegisterOnPremisesInstanceInputTypeDef, _OptionalRegisterOnPremisesInstanceInputTypeDef
):
    pass


RelatedDeploymentsTypeDef = TypedDict(
    "RelatedDeploymentsTypeDef",
    {
        "autoUpdateOutdatedInstancesRootDeploymentId": str,
        "autoUpdateOutdatedInstancesDeploymentIds": List[str],
    },
    total=False,
)

RemoveTagsFromOnPremisesInstancesInputTypeDef = TypedDict(
    "RemoveTagsFromOnPremisesInstancesInputTypeDef",
    {
        "tags": List["TagTypeDef"],
        "instanceNames": List[str],
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

RevisionInfoTypeDef = TypedDict(
    "RevisionInfoTypeDef",
    {
        "revisionLocation": "RevisionLocationTypeDef",
        "genericRevisionInfo": "GenericRevisionInfoTypeDef",
    },
    total=False,
)

RevisionLocationTypeDef = TypedDict(
    "RevisionLocationTypeDef",
    {
        "revisionType": RevisionLocationTypeType,
        "s3Location": "S3LocationTypeDef",
        "gitHubLocation": "GitHubLocationTypeDef",
        "string": "RawStringTypeDef",
        "appSpecContent": "AppSpecContentTypeDef",
    },
    total=False,
)

RollbackInfoTypeDef = TypedDict(
    "RollbackInfoTypeDef",
    {
        "rollbackDeploymentId": str,
        "rollbackTriggeringDeploymentId": str,
        "rollbackMessage": str,
    },
    total=False,
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": BundleTypeType,
        "version": str,
        "eTag": str,
    },
    total=False,
)

SkipWaitTimeForInstanceTerminationInputTypeDef = TypedDict(
    "SkipWaitTimeForInstanceTerminationInputTypeDef",
    {
        "deploymentId": str,
    },
    total=False,
)

_RequiredStopDeploymentInputTypeDef = TypedDict(
    "_RequiredStopDeploymentInputTypeDef",
    {
        "deploymentId": str,
    },
)
_OptionalStopDeploymentInputTypeDef = TypedDict(
    "_OptionalStopDeploymentInputTypeDef",
    {
        "autoRollbackEnabled": bool,
    },
    total=False,
)


class StopDeploymentInputTypeDef(
    _RequiredStopDeploymentInputTypeDef, _OptionalStopDeploymentInputTypeDef
):
    pass


StopDeploymentOutputResponseTypeDef = TypedDict(
    "StopDeploymentOutputResponseTypeDef",
    {
        "status": StopStatusType,
        "statusMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "Key": str,
        "Value": str,
        "Type": TagFilterTypeType,
    },
    total=False,
)

TagResourceInputTypeDef = TypedDict(
    "TagResourceInputTypeDef",
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

TargetGroupInfoTypeDef = TypedDict(
    "TargetGroupInfoTypeDef",
    {
        "name": str,
    },
    total=False,
)

TargetGroupPairInfoTypeDef = TypedDict(
    "TargetGroupPairInfoTypeDef",
    {
        "targetGroups": List["TargetGroupInfoTypeDef"],
        "prodTrafficRoute": "TrafficRouteTypeDef",
        "testTrafficRoute": "TrafficRouteTypeDef",
    },
    total=False,
)

TargetInstancesTypeDef = TypedDict(
    "TargetInstancesTypeDef",
    {
        "tagFilters": List["EC2TagFilterTypeDef"],
        "autoScalingGroups": List[str],
        "ec2TagSet": "EC2TagSetTypeDef",
    },
    total=False,
)

TimeBasedCanaryTypeDef = TypedDict(
    "TimeBasedCanaryTypeDef",
    {
        "canaryPercentage": int,
        "canaryInterval": int,
    },
    total=False,
)

TimeBasedLinearTypeDef = TypedDict(
    "TimeBasedLinearTypeDef",
    {
        "linearPercentage": int,
        "linearInterval": int,
    },
    total=False,
)

TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "start": Union[datetime, str],
        "end": Union[datetime, str],
    },
    total=False,
)

TrafficRouteTypeDef = TypedDict(
    "TrafficRouteTypeDef",
    {
        "listenerArns": List[str],
    },
    total=False,
)

TrafficRoutingConfigTypeDef = TypedDict(
    "TrafficRoutingConfigTypeDef",
    {
        "type": TrafficRoutingTypeType,
        "timeBasedCanary": "TimeBasedCanaryTypeDef",
        "timeBasedLinear": "TimeBasedLinearTypeDef",
    },
    total=False,
)

TriggerConfigTypeDef = TypedDict(
    "TriggerConfigTypeDef",
    {
        "triggerName": str,
        "triggerTargetArn": str,
        "triggerEvents": List[TriggerEventTypeType],
    },
    total=False,
)

UntagResourceInputTypeDef = TypedDict(
    "UntagResourceInputTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateApplicationInputTypeDef = TypedDict(
    "UpdateApplicationInputTypeDef",
    {
        "applicationName": str,
        "newApplicationName": str,
    },
    total=False,
)

_RequiredUpdateDeploymentGroupInputTypeDef = TypedDict(
    "_RequiredUpdateDeploymentGroupInputTypeDef",
    {
        "applicationName": str,
        "currentDeploymentGroupName": str,
    },
)
_OptionalUpdateDeploymentGroupInputTypeDef = TypedDict(
    "_OptionalUpdateDeploymentGroupInputTypeDef",
    {
        "newDeploymentGroupName": str,
        "deploymentConfigName": str,
        "ec2TagFilters": List["EC2TagFilterTypeDef"],
        "onPremisesInstanceTagFilters": List["TagFilterTypeDef"],
        "autoScalingGroups": List[str],
        "serviceRoleArn": str,
        "triggerConfigurations": List["TriggerConfigTypeDef"],
        "alarmConfiguration": "AlarmConfigurationTypeDef",
        "autoRollbackConfiguration": "AutoRollbackConfigurationTypeDef",
        "outdatedInstancesStrategy": OutdatedInstancesStrategyType,
        "deploymentStyle": "DeploymentStyleTypeDef",
        "blueGreenDeploymentConfiguration": "BlueGreenDeploymentConfigurationTypeDef",
        "loadBalancerInfo": "LoadBalancerInfoTypeDef",
        "ec2TagSet": "EC2TagSetTypeDef",
        "ecsServices": List["ECSServiceTypeDef"],
        "onPremisesTagSet": "OnPremisesTagSetTypeDef",
    },
    total=False,
)


class UpdateDeploymentGroupInputTypeDef(
    _RequiredUpdateDeploymentGroupInputTypeDef, _OptionalUpdateDeploymentGroupInputTypeDef
):
    pass


UpdateDeploymentGroupOutputResponseTypeDef = TypedDict(
    "UpdateDeploymentGroupOutputResponseTypeDef",
    {
        "hooksNotCleanedUp": List["AutoScalingGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
