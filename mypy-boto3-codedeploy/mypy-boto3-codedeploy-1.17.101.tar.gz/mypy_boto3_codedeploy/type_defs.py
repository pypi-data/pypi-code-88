"""
Type annotations for codedeploy service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codedeploy.type_defs import AlarmConfigurationTypeDef

    data: AlarmConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AutoRollbackEventType,
    BundleTypeType,
    ComputePlatformType,
    DeploymentCreatorType,
    DeploymentOptionType,
    DeploymentReadyActionType,
    DeploymentStatusType,
    DeploymentTargetTypeType,
    DeploymentTypeType,
    EC2TagFilterTypeType,
    ErrorCodeType,
    FileExistsBehaviorType,
    GreenFleetProvisioningActionType,
    InstanceActionType,
    InstanceStatusType,
    InstanceTypeType,
    LifecycleErrorCodeType,
    LifecycleEventStatusType,
    MinimumHealthyHostsTypeType,
    OutdatedInstancesStrategyType,
    RevisionLocationTypeType,
    StopStatusType,
    TagFilterTypeType,
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
    "AlarmConfigurationTypeDef",
    "AlarmTypeDef",
    "AppSpecContentTypeDef",
    "ApplicationInfoTypeDef",
    "AutoRollbackConfigurationTypeDef",
    "AutoScalingGroupTypeDef",
    "BatchGetApplicationRevisionsOutputTypeDef",
    "BatchGetApplicationsOutputTypeDef",
    "BatchGetDeploymentGroupsOutputTypeDef",
    "BatchGetDeploymentInstancesOutputTypeDef",
    "BatchGetDeploymentTargetsOutputTypeDef",
    "BatchGetDeploymentsOutputTypeDef",
    "BatchGetOnPremisesInstancesOutputTypeDef",
    "BlueGreenDeploymentConfigurationTypeDef",
    "BlueInstanceTerminationOptionTypeDef",
    "CloudFormationTargetTypeDef",
    "CreateApplicationOutputTypeDef",
    "CreateDeploymentConfigOutputTypeDef",
    "CreateDeploymentGroupOutputTypeDef",
    "CreateDeploymentOutputTypeDef",
    "DeleteDeploymentGroupOutputTypeDef",
    "DeleteGitHubAccountTokenOutputTypeDef",
    "DeploymentConfigInfoTypeDef",
    "DeploymentGroupInfoTypeDef",
    "DeploymentInfoTypeDef",
    "DeploymentOverviewTypeDef",
    "DeploymentReadyOptionTypeDef",
    "DeploymentStyleTypeDef",
    "DeploymentTargetTypeDef",
    "DiagnosticsTypeDef",
    "EC2TagFilterTypeDef",
    "EC2TagSetTypeDef",
    "ECSServiceTypeDef",
    "ECSTargetTypeDef",
    "ECSTaskSetTypeDef",
    "ELBInfoTypeDef",
    "ErrorInformationTypeDef",
    "GenericRevisionInfoTypeDef",
    "GetApplicationOutputTypeDef",
    "GetApplicationRevisionOutputTypeDef",
    "GetDeploymentConfigOutputTypeDef",
    "GetDeploymentGroupOutputTypeDef",
    "GetDeploymentInstanceOutputTypeDef",
    "GetDeploymentOutputTypeDef",
    "GetDeploymentTargetOutputTypeDef",
    "GetOnPremisesInstanceOutputTypeDef",
    "GitHubLocationTypeDef",
    "GreenFleetProvisioningOptionTypeDef",
    "InstanceInfoTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTargetTypeDef",
    "LambdaFunctionInfoTypeDef",
    "LambdaTargetTypeDef",
    "LastDeploymentInfoTypeDef",
    "LifecycleEventTypeDef",
    "ListApplicationRevisionsOutputTypeDef",
    "ListApplicationsOutputTypeDef",
    "ListDeploymentConfigsOutputTypeDef",
    "ListDeploymentGroupsOutputTypeDef",
    "ListDeploymentInstancesOutputTypeDef",
    "ListDeploymentTargetsOutputTypeDef",
    "ListDeploymentsOutputTypeDef",
    "ListGitHubAccountTokenNamesOutputTypeDef",
    "ListOnPremisesInstancesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LoadBalancerInfoTypeDef",
    "MinimumHealthyHostsTypeDef",
    "OnPremisesTagSetTypeDef",
    "PaginatorConfigTypeDef",
    "PutLifecycleEventHookExecutionStatusOutputTypeDef",
    "RawStringTypeDef",
    "RelatedDeploymentsTypeDef",
    "ResponseMetadataTypeDef",
    "RevisionInfoTypeDef",
    "RevisionLocationTypeDef",
    "RollbackInfoTypeDef",
    "S3LocationTypeDef",
    "StopDeploymentOutputTypeDef",
    "TagFilterTypeDef",
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
    "UpdateDeploymentGroupOutputTypeDef",
    "WaiterConfigTypeDef",
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

BatchGetApplicationRevisionsOutputTypeDef = TypedDict(
    "BatchGetApplicationRevisionsOutputTypeDef",
    {
        "applicationName": str,
        "errorMessage": str,
        "revisions": List["RevisionInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetApplicationsOutputTypeDef = TypedDict(
    "BatchGetApplicationsOutputTypeDef",
    {
        "applicationsInfo": List["ApplicationInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDeploymentGroupsOutputTypeDef = TypedDict(
    "BatchGetDeploymentGroupsOutputTypeDef",
    {
        "deploymentGroupsInfo": List["DeploymentGroupInfoTypeDef"],
        "errorMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDeploymentInstancesOutputTypeDef = TypedDict(
    "BatchGetDeploymentInstancesOutputTypeDef",
    {
        "instancesSummary": List["InstanceSummaryTypeDef"],
        "errorMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDeploymentTargetsOutputTypeDef = TypedDict(
    "BatchGetDeploymentTargetsOutputTypeDef",
    {
        "deploymentTargets": List["DeploymentTargetTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDeploymentsOutputTypeDef = TypedDict(
    "BatchGetDeploymentsOutputTypeDef",
    {
        "deploymentsInfo": List["DeploymentInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetOnPremisesInstancesOutputTypeDef = TypedDict(
    "BatchGetOnPremisesInstancesOutputTypeDef",
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

CreateApplicationOutputTypeDef = TypedDict(
    "CreateApplicationOutputTypeDef",
    {
        "applicationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDeploymentConfigOutputTypeDef = TypedDict(
    "CreateDeploymentConfigOutputTypeDef",
    {
        "deploymentConfigId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDeploymentGroupOutputTypeDef = TypedDict(
    "CreateDeploymentGroupOutputTypeDef",
    {
        "deploymentGroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDeploymentOutputTypeDef = TypedDict(
    "CreateDeploymentOutputTypeDef",
    {
        "deploymentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDeploymentGroupOutputTypeDef = TypedDict(
    "DeleteDeploymentGroupOutputTypeDef",
    {
        "hooksNotCleanedUp": List["AutoScalingGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGitHubAccountTokenOutputTypeDef = TypedDict(
    "DeleteGitHubAccountTokenOutputTypeDef",
    {
        "tokenName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

GetApplicationOutputTypeDef = TypedDict(
    "GetApplicationOutputTypeDef",
    {
        "application": "ApplicationInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationRevisionOutputTypeDef = TypedDict(
    "GetApplicationRevisionOutputTypeDef",
    {
        "applicationName": str,
        "revision": "RevisionLocationTypeDef",
        "revisionInfo": "GenericRevisionInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentConfigOutputTypeDef = TypedDict(
    "GetDeploymentConfigOutputTypeDef",
    {
        "deploymentConfigInfo": "DeploymentConfigInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentGroupOutputTypeDef = TypedDict(
    "GetDeploymentGroupOutputTypeDef",
    {
        "deploymentGroupInfo": "DeploymentGroupInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentInstanceOutputTypeDef = TypedDict(
    "GetDeploymentInstanceOutputTypeDef",
    {
        "instanceSummary": "InstanceSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentOutputTypeDef = TypedDict(
    "GetDeploymentOutputTypeDef",
    {
        "deploymentInfo": "DeploymentInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentTargetOutputTypeDef = TypedDict(
    "GetDeploymentTargetOutputTypeDef",
    {
        "deploymentTarget": "DeploymentTargetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOnPremisesInstanceOutputTypeDef = TypedDict(
    "GetOnPremisesInstanceOutputTypeDef",
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

ListApplicationRevisionsOutputTypeDef = TypedDict(
    "ListApplicationRevisionsOutputTypeDef",
    {
        "revisions": List["RevisionLocationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationsOutputTypeDef = TypedDict(
    "ListApplicationsOutputTypeDef",
    {
        "applications": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentConfigsOutputTypeDef = TypedDict(
    "ListDeploymentConfigsOutputTypeDef",
    {
        "deploymentConfigsList": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentGroupsOutputTypeDef = TypedDict(
    "ListDeploymentGroupsOutputTypeDef",
    {
        "applicationName": str,
        "deploymentGroups": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentInstancesOutputTypeDef = TypedDict(
    "ListDeploymentInstancesOutputTypeDef",
    {
        "instancesList": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentTargetsOutputTypeDef = TypedDict(
    "ListDeploymentTargetsOutputTypeDef",
    {
        "targetIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentsOutputTypeDef = TypedDict(
    "ListDeploymentsOutputTypeDef",
    {
        "deployments": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGitHubAccountTokenNamesOutputTypeDef = TypedDict(
    "ListGitHubAccountTokenNamesOutputTypeDef",
    {
        "tokenNameList": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOnPremisesInstancesOutputTypeDef = TypedDict(
    "ListOnPremisesInstancesOutputTypeDef",
    {
        "instanceNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
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

PutLifecycleEventHookExecutionStatusOutputTypeDef = TypedDict(
    "PutLifecycleEventHookExecutionStatusOutputTypeDef",
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

RelatedDeploymentsTypeDef = TypedDict(
    "RelatedDeploymentsTypeDef",
    {
        "autoUpdateOutdatedInstancesRootDeploymentId": str,
        "autoUpdateOutdatedInstancesDeploymentIds": List[str],
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

StopDeploymentOutputTypeDef = TypedDict(
    "StopDeploymentOutputTypeDef",
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
        "start": datetime,
        "end": datetime,
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

UpdateDeploymentGroupOutputTypeDef = TypedDict(
    "UpdateDeploymentGroupOutputTypeDef",
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
