"""
Type annotations for autoscaling service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/type_defs.html)

Usage::

    ```python
    from mypy_boto3_autoscaling.type_defs import ActivitiesTypeResponseTypeDef

    data: ActivitiesTypeResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    InstanceMetadataEndpointStateType,
    InstanceMetadataHttpTokensStateType,
    InstanceRefreshStatusType,
    LifecycleStateType,
    MetricStatisticType,
    MetricTypeType,
    PredefinedLoadMetricTypeType,
    PredefinedMetricPairTypeType,
    PredefinedScalingMetricTypeType,
    PredictiveScalingMaxCapacityBreachBehaviorType,
    PredictiveScalingModeType,
    ScalingActivityStatusCodeType,
    WarmPoolStateType,
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
    "ActivitiesTypeResponseTypeDef",
    "ActivityTypeDef",
    "ActivityTypeResponseTypeDef",
    "AdjustmentTypeTypeDef",
    "AlarmTypeDef",
    "AttachInstancesQueryTypeDef",
    "AttachLoadBalancerTargetGroupsTypeTypeDef",
    "AttachLoadBalancersTypeTypeDef",
    "AutoScalingGroupNamesTypeTypeDef",
    "AutoScalingGroupTypeDef",
    "AutoScalingGroupsTypeResponseTypeDef",
    "AutoScalingInstanceDetailsTypeDef",
    "AutoScalingInstancesTypeResponseTypeDef",
    "BatchDeleteScheduledActionAnswerResponseTypeDef",
    "BatchDeleteScheduledActionTypeTypeDef",
    "BatchPutScheduledUpdateGroupActionAnswerResponseTypeDef",
    "BatchPutScheduledUpdateGroupActionTypeTypeDef",
    "BlockDeviceMappingTypeDef",
    "CancelInstanceRefreshAnswerResponseTypeDef",
    "CancelInstanceRefreshTypeTypeDef",
    "CapacityForecastTypeDef",
    "CompleteLifecycleActionTypeTypeDef",
    "CreateAutoScalingGroupTypeTypeDef",
    "CreateLaunchConfigurationTypeTypeDef",
    "CreateOrUpdateTagsTypeTypeDef",
    "CustomizedMetricSpecificationTypeDef",
    "DeleteAutoScalingGroupTypeTypeDef",
    "DeleteLifecycleHookTypeTypeDef",
    "DeleteNotificationConfigurationTypeTypeDef",
    "DeletePolicyTypeTypeDef",
    "DeleteScheduledActionTypeTypeDef",
    "DeleteTagsTypeTypeDef",
    "DeleteWarmPoolTypeTypeDef",
    "DescribeAccountLimitsAnswerResponseTypeDef",
    "DescribeAdjustmentTypesAnswerResponseTypeDef",
    "DescribeAutoScalingInstancesTypeTypeDef",
    "DescribeAutoScalingNotificationTypesAnswerResponseTypeDef",
    "DescribeInstanceRefreshesAnswerResponseTypeDef",
    "DescribeInstanceRefreshesTypeTypeDef",
    "DescribeLifecycleHookTypesAnswerResponseTypeDef",
    "DescribeLifecycleHooksAnswerResponseTypeDef",
    "DescribeLifecycleHooksTypeTypeDef",
    "DescribeLoadBalancerTargetGroupsRequestTypeDef",
    "DescribeLoadBalancerTargetGroupsResponseResponseTypeDef",
    "DescribeLoadBalancersRequestTypeDef",
    "DescribeLoadBalancersResponseResponseTypeDef",
    "DescribeMetricCollectionTypesAnswerResponseTypeDef",
    "DescribeNotificationConfigurationsAnswerResponseTypeDef",
    "DescribeNotificationConfigurationsTypeTypeDef",
    "DescribePoliciesTypeTypeDef",
    "DescribeScalingActivitiesTypeTypeDef",
    "DescribeScheduledActionsTypeTypeDef",
    "DescribeTagsTypeTypeDef",
    "DescribeTerminationPolicyTypesAnswerResponseTypeDef",
    "DescribeWarmPoolAnswerResponseTypeDef",
    "DescribeWarmPoolTypeTypeDef",
    "DetachInstancesAnswerResponseTypeDef",
    "DetachInstancesQueryTypeDef",
    "DetachLoadBalancerTargetGroupsTypeTypeDef",
    "DetachLoadBalancersTypeTypeDef",
    "DisableMetricsCollectionQueryTypeDef",
    "EbsTypeDef",
    "EnableMetricsCollectionQueryTypeDef",
    "EnabledMetricTypeDef",
    "EnterStandbyAnswerResponseTypeDef",
    "EnterStandbyQueryTypeDef",
    "ExecutePolicyTypeTypeDef",
    "ExitStandbyAnswerResponseTypeDef",
    "ExitStandbyQueryTypeDef",
    "FailedScheduledUpdateGroupActionRequestTypeDef",
    "FilterTypeDef",
    "GetPredictiveScalingForecastAnswerResponseTypeDef",
    "GetPredictiveScalingForecastTypeTypeDef",
    "InstanceMetadataOptionsTypeDef",
    "InstanceMonitoringTypeDef",
    "InstanceRefreshLivePoolProgressTypeDef",
    "InstanceRefreshProgressDetailsTypeDef",
    "InstanceRefreshTypeDef",
    "InstanceRefreshWarmPoolProgressTypeDef",
    "InstanceTypeDef",
    "InstancesDistributionTypeDef",
    "LaunchConfigurationNameTypeTypeDef",
    "LaunchConfigurationNamesTypeTypeDef",
    "LaunchConfigurationTypeDef",
    "LaunchConfigurationsTypeResponseTypeDef",
    "LaunchTemplateOverridesTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "LaunchTemplateTypeDef",
    "LifecycleHookSpecificationTypeDef",
    "LifecycleHookTypeDef",
    "LoadBalancerStateTypeDef",
    "LoadBalancerTargetGroupStateTypeDef",
    "LoadForecastTypeDef",
    "MetricCollectionTypeTypeDef",
    "MetricDimensionTypeDef",
    "MetricGranularityTypeTypeDef",
    "MixedInstancesPolicyTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PoliciesTypeResponseTypeDef",
    "PolicyARNTypeResponseTypeDef",
    "PredefinedMetricSpecificationTypeDef",
    "PredictiveScalingConfigurationTypeDef",
    "PredictiveScalingMetricSpecificationTypeDef",
    "PredictiveScalingPredefinedLoadMetricTypeDef",
    "PredictiveScalingPredefinedMetricPairTypeDef",
    "PredictiveScalingPredefinedScalingMetricTypeDef",
    "ProcessTypeTypeDef",
    "ProcessesTypeResponseTypeDef",
    "PutLifecycleHookTypeTypeDef",
    "PutNotificationConfigurationTypeTypeDef",
    "PutScalingPolicyTypeTypeDef",
    "PutScheduledUpdateGroupActionTypeTypeDef",
    "PutWarmPoolTypeTypeDef",
    "RecordLifecycleActionHeartbeatTypeTypeDef",
    "RefreshPreferencesTypeDef",
    "ResponseMetadataTypeDef",
    "ScalingPolicyTypeDef",
    "ScalingProcessQueryTypeDef",
    "ScheduledActionsTypeResponseTypeDef",
    "ScheduledUpdateGroupActionRequestTypeDef",
    "ScheduledUpdateGroupActionTypeDef",
    "SetDesiredCapacityTypeTypeDef",
    "SetInstanceHealthQueryTypeDef",
    "SetInstanceProtectionQueryTypeDef",
    "StartInstanceRefreshAnswerResponseTypeDef",
    "StartInstanceRefreshTypeTypeDef",
    "StepAdjustmentTypeDef",
    "SuspendedProcessTypeDef",
    "TagDescriptionTypeDef",
    "TagTypeDef",
    "TagsTypeResponseTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "TerminateInstanceInAutoScalingGroupTypeTypeDef",
    "UpdateAutoScalingGroupTypeTypeDef",
    "WarmPoolConfigurationTypeDef",
)

ActivitiesTypeResponseTypeDef = TypedDict(
    "ActivitiesTypeResponseTypeDef",
    {
        "Activities": List["ActivityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredActivityTypeDef = TypedDict(
    "_RequiredActivityTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Cause": str,
        "StartTime": datetime,
        "StatusCode": ScalingActivityStatusCodeType,
    },
)
_OptionalActivityTypeDef = TypedDict(
    "_OptionalActivityTypeDef",
    {
        "Description": str,
        "EndTime": datetime,
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
        "AutoScalingGroupState": str,
        "AutoScalingGroupARN": str,
    },
    total=False,
)


class ActivityTypeDef(_RequiredActivityTypeDef, _OptionalActivityTypeDef):
    pass


ActivityTypeResponseTypeDef = TypedDict(
    "ActivityTypeResponseTypeDef",
    {
        "Activity": "ActivityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdjustmentTypeTypeDef = TypedDict(
    "AdjustmentTypeTypeDef",
    {
        "AdjustmentType": str,
    },
    total=False,
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "AlarmName": str,
        "AlarmARN": str,
    },
    total=False,
)

_RequiredAttachInstancesQueryTypeDef = TypedDict(
    "_RequiredAttachInstancesQueryTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalAttachInstancesQueryTypeDef = TypedDict(
    "_OptionalAttachInstancesQueryTypeDef",
    {
        "InstanceIds": List[str],
    },
    total=False,
)


class AttachInstancesQueryTypeDef(
    _RequiredAttachInstancesQueryTypeDef, _OptionalAttachInstancesQueryTypeDef
):
    pass


AttachLoadBalancerTargetGroupsTypeTypeDef = TypedDict(
    "AttachLoadBalancerTargetGroupsTypeTypeDef",
    {
        "AutoScalingGroupName": str,
        "TargetGroupARNs": List[str],
    },
)

AttachLoadBalancersTypeTypeDef = TypedDict(
    "AttachLoadBalancersTypeTypeDef",
    {
        "AutoScalingGroupName": str,
        "LoadBalancerNames": List[str],
    },
)

AutoScalingGroupNamesTypeTypeDef = TypedDict(
    "AutoScalingGroupNamesTypeTypeDef",
    {
        "AutoScalingGroupNames": List[str],
        "NextToken": str,
        "MaxRecords": int,
    },
    total=False,
)

_RequiredAutoScalingGroupTypeDef = TypedDict(
    "_RequiredAutoScalingGroupTypeDef",
    {
        "AutoScalingGroupName": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
        "DefaultCooldown": int,
        "AvailabilityZones": List[str],
        "HealthCheckType": str,
        "CreatedTime": datetime,
    },
)
_OptionalAutoScalingGroupTypeDef = TypedDict(
    "_OptionalAutoScalingGroupTypeDef",
    {
        "AutoScalingGroupARN": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": "LaunchTemplateSpecificationTypeDef",
        "MixedInstancesPolicy": "MixedInstancesPolicyTypeDef",
        "PredictedCapacity": int,
        "LoadBalancerNames": List[str],
        "TargetGroupARNs": List[str],
        "HealthCheckGracePeriod": int,
        "Instances": List["InstanceTypeDef"],
        "SuspendedProcesses": List["SuspendedProcessTypeDef"],
        "PlacementGroup": str,
        "VPCZoneIdentifier": str,
        "EnabledMetrics": List["EnabledMetricTypeDef"],
        "Status": str,
        "Tags": List["TagDescriptionTypeDef"],
        "TerminationPolicies": List[str],
        "NewInstancesProtectedFromScaleIn": bool,
        "ServiceLinkedRoleARN": str,
        "MaxInstanceLifetime": int,
        "CapacityRebalance": bool,
        "WarmPoolConfiguration": "WarmPoolConfigurationTypeDef",
        "WarmPoolSize": int,
    },
    total=False,
)


class AutoScalingGroupTypeDef(_RequiredAutoScalingGroupTypeDef, _OptionalAutoScalingGroupTypeDef):
    pass


AutoScalingGroupsTypeResponseTypeDef = TypedDict(
    "AutoScalingGroupsTypeResponseTypeDef",
    {
        "AutoScalingGroups": List["AutoScalingGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAutoScalingInstanceDetailsTypeDef = TypedDict(
    "_RequiredAutoScalingInstanceDetailsTypeDef",
    {
        "InstanceId": str,
        "AutoScalingGroupName": str,
        "AvailabilityZone": str,
        "LifecycleState": str,
        "HealthStatus": str,
        "ProtectedFromScaleIn": bool,
    },
)
_OptionalAutoScalingInstanceDetailsTypeDef = TypedDict(
    "_OptionalAutoScalingInstanceDetailsTypeDef",
    {
        "InstanceType": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": "LaunchTemplateSpecificationTypeDef",
        "WeightedCapacity": str,
    },
    total=False,
)


class AutoScalingInstanceDetailsTypeDef(
    _RequiredAutoScalingInstanceDetailsTypeDef, _OptionalAutoScalingInstanceDetailsTypeDef
):
    pass


AutoScalingInstancesTypeResponseTypeDef = TypedDict(
    "AutoScalingInstancesTypeResponseTypeDef",
    {
        "AutoScalingInstances": List["AutoScalingInstanceDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteScheduledActionAnswerResponseTypeDef = TypedDict(
    "BatchDeleteScheduledActionAnswerResponseTypeDef",
    {
        "FailedScheduledActions": List["FailedScheduledUpdateGroupActionRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteScheduledActionTypeTypeDef = TypedDict(
    "BatchDeleteScheduledActionTypeTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionNames": List[str],
    },
)

BatchPutScheduledUpdateGroupActionAnswerResponseTypeDef = TypedDict(
    "BatchPutScheduledUpdateGroupActionAnswerResponseTypeDef",
    {
        "FailedScheduledUpdateGroupActions": List["FailedScheduledUpdateGroupActionRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPutScheduledUpdateGroupActionTypeTypeDef = TypedDict(
    "BatchPutScheduledUpdateGroupActionTypeTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledUpdateGroupActions": List["ScheduledUpdateGroupActionRequestTypeDef"],
    },
)

_RequiredBlockDeviceMappingTypeDef = TypedDict(
    "_RequiredBlockDeviceMappingTypeDef",
    {
        "DeviceName": str,
    },
)
_OptionalBlockDeviceMappingTypeDef = TypedDict(
    "_OptionalBlockDeviceMappingTypeDef",
    {
        "VirtualName": str,
        "Ebs": "EbsTypeDef",
        "NoDevice": bool,
    },
    total=False,
)


class BlockDeviceMappingTypeDef(
    _RequiredBlockDeviceMappingTypeDef, _OptionalBlockDeviceMappingTypeDef
):
    pass


CancelInstanceRefreshAnswerResponseTypeDef = TypedDict(
    "CancelInstanceRefreshAnswerResponseTypeDef",
    {
        "InstanceRefreshId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelInstanceRefreshTypeTypeDef = TypedDict(
    "CancelInstanceRefreshTypeTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)

CapacityForecastTypeDef = TypedDict(
    "CapacityForecastTypeDef",
    {
        "Timestamps": List[datetime],
        "Values": List[float],
    },
)

_RequiredCompleteLifecycleActionTypeTypeDef = TypedDict(
    "_RequiredCompleteLifecycleActionTypeTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
        "LifecycleActionResult": str,
    },
)
_OptionalCompleteLifecycleActionTypeTypeDef = TypedDict(
    "_OptionalCompleteLifecycleActionTypeTypeDef",
    {
        "LifecycleActionToken": str,
        "InstanceId": str,
    },
    total=False,
)


class CompleteLifecycleActionTypeTypeDef(
    _RequiredCompleteLifecycleActionTypeTypeDef, _OptionalCompleteLifecycleActionTypeTypeDef
):
    pass


_RequiredCreateAutoScalingGroupTypeTypeDef = TypedDict(
    "_RequiredCreateAutoScalingGroupTypeTypeDef",
    {
        "AutoScalingGroupName": str,
        "MinSize": int,
        "MaxSize": int,
    },
)
_OptionalCreateAutoScalingGroupTypeTypeDef = TypedDict(
    "_OptionalCreateAutoScalingGroupTypeTypeDef",
    {
        "LaunchConfigurationName": str,
        "LaunchTemplate": "LaunchTemplateSpecificationTypeDef",
        "MixedInstancesPolicy": "MixedInstancesPolicyTypeDef",
        "InstanceId": str,
        "DesiredCapacity": int,
        "DefaultCooldown": int,
        "AvailabilityZones": List[str],
        "LoadBalancerNames": List[str],
        "TargetGroupARNs": List[str],
        "HealthCheckType": str,
        "HealthCheckGracePeriod": int,
        "PlacementGroup": str,
        "VPCZoneIdentifier": str,
        "TerminationPolicies": List[str],
        "NewInstancesProtectedFromScaleIn": bool,
        "CapacityRebalance": bool,
        "LifecycleHookSpecificationList": List["LifecycleHookSpecificationTypeDef"],
        "Tags": List["TagTypeDef"],
        "ServiceLinkedRoleARN": str,
        "MaxInstanceLifetime": int,
    },
    total=False,
)


class CreateAutoScalingGroupTypeTypeDef(
    _RequiredCreateAutoScalingGroupTypeTypeDef, _OptionalCreateAutoScalingGroupTypeTypeDef
):
    pass


_RequiredCreateLaunchConfigurationTypeTypeDef = TypedDict(
    "_RequiredCreateLaunchConfigurationTypeTypeDef",
    {
        "LaunchConfigurationName": str,
    },
)
_OptionalCreateLaunchConfigurationTypeTypeDef = TypedDict(
    "_OptionalCreateLaunchConfigurationTypeTypeDef",
    {
        "ImageId": str,
        "KeyName": str,
        "SecurityGroups": List[str],
        "ClassicLinkVPCId": str,
        "ClassicLinkVPCSecurityGroups": List[str],
        "UserData": str,
        "InstanceId": str,
        "InstanceType": str,
        "KernelId": str,
        "RamdiskId": str,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "InstanceMonitoring": "InstanceMonitoringTypeDef",
        "SpotPrice": str,
        "IamInstanceProfile": str,
        "EbsOptimized": bool,
        "AssociatePublicIpAddress": bool,
        "PlacementTenancy": str,
        "MetadataOptions": "InstanceMetadataOptionsTypeDef",
    },
    total=False,
)


class CreateLaunchConfigurationTypeTypeDef(
    _RequiredCreateLaunchConfigurationTypeTypeDef, _OptionalCreateLaunchConfigurationTypeTypeDef
):
    pass


CreateOrUpdateTagsTypeTypeDef = TypedDict(
    "CreateOrUpdateTagsTypeTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
)

_RequiredCustomizedMetricSpecificationTypeDef = TypedDict(
    "_RequiredCustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": MetricStatisticType,
    },
)
_OptionalCustomizedMetricSpecificationTypeDef = TypedDict(
    "_OptionalCustomizedMetricSpecificationTypeDef",
    {
        "Dimensions": List["MetricDimensionTypeDef"],
        "Unit": str,
    },
    total=False,
)


class CustomizedMetricSpecificationTypeDef(
    _RequiredCustomizedMetricSpecificationTypeDef, _OptionalCustomizedMetricSpecificationTypeDef
):
    pass


_RequiredDeleteAutoScalingGroupTypeTypeDef = TypedDict(
    "_RequiredDeleteAutoScalingGroupTypeTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalDeleteAutoScalingGroupTypeTypeDef = TypedDict(
    "_OptionalDeleteAutoScalingGroupTypeTypeDef",
    {
        "ForceDelete": bool,
    },
    total=False,
)


class DeleteAutoScalingGroupTypeTypeDef(
    _RequiredDeleteAutoScalingGroupTypeTypeDef, _OptionalDeleteAutoScalingGroupTypeTypeDef
):
    pass


DeleteLifecycleHookTypeTypeDef = TypedDict(
    "DeleteLifecycleHookTypeTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
    },
)

DeleteNotificationConfigurationTypeTypeDef = TypedDict(
    "DeleteNotificationConfigurationTypeTypeDef",
    {
        "AutoScalingGroupName": str,
        "TopicARN": str,
    },
)

_RequiredDeletePolicyTypeTypeDef = TypedDict(
    "_RequiredDeletePolicyTypeTypeDef",
    {
        "PolicyName": str,
    },
)
_OptionalDeletePolicyTypeTypeDef = TypedDict(
    "_OptionalDeletePolicyTypeTypeDef",
    {
        "AutoScalingGroupName": str,
    },
    total=False,
)


class DeletePolicyTypeTypeDef(_RequiredDeletePolicyTypeTypeDef, _OptionalDeletePolicyTypeTypeDef):
    pass


DeleteScheduledActionTypeTypeDef = TypedDict(
    "DeleteScheduledActionTypeTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionName": str,
    },
)

DeleteTagsTypeTypeDef = TypedDict(
    "DeleteTagsTypeTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
)

_RequiredDeleteWarmPoolTypeTypeDef = TypedDict(
    "_RequiredDeleteWarmPoolTypeTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalDeleteWarmPoolTypeTypeDef = TypedDict(
    "_OptionalDeleteWarmPoolTypeTypeDef",
    {
        "ForceDelete": bool,
    },
    total=False,
)


class DeleteWarmPoolTypeTypeDef(
    _RequiredDeleteWarmPoolTypeTypeDef, _OptionalDeleteWarmPoolTypeTypeDef
):
    pass


DescribeAccountLimitsAnswerResponseTypeDef = TypedDict(
    "DescribeAccountLimitsAnswerResponseTypeDef",
    {
        "MaxNumberOfAutoScalingGroups": int,
        "MaxNumberOfLaunchConfigurations": int,
        "NumberOfAutoScalingGroups": int,
        "NumberOfLaunchConfigurations": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAdjustmentTypesAnswerResponseTypeDef = TypedDict(
    "DescribeAdjustmentTypesAnswerResponseTypeDef",
    {
        "AdjustmentTypes": List["AdjustmentTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAutoScalingInstancesTypeTypeDef = TypedDict(
    "DescribeAutoScalingInstancesTypeTypeDef",
    {
        "InstanceIds": List[str],
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeAutoScalingNotificationTypesAnswerResponseTypeDef = TypedDict(
    "DescribeAutoScalingNotificationTypesAnswerResponseTypeDef",
    {
        "AutoScalingNotificationTypes": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceRefreshesAnswerResponseTypeDef = TypedDict(
    "DescribeInstanceRefreshesAnswerResponseTypeDef",
    {
        "InstanceRefreshes": List["InstanceRefreshTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeInstanceRefreshesTypeTypeDef = TypedDict(
    "_RequiredDescribeInstanceRefreshesTypeTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalDescribeInstanceRefreshesTypeTypeDef = TypedDict(
    "_OptionalDescribeInstanceRefreshesTypeTypeDef",
    {
        "InstanceRefreshIds": List[str],
        "NextToken": str,
        "MaxRecords": int,
    },
    total=False,
)


class DescribeInstanceRefreshesTypeTypeDef(
    _RequiredDescribeInstanceRefreshesTypeTypeDef, _OptionalDescribeInstanceRefreshesTypeTypeDef
):
    pass


DescribeLifecycleHookTypesAnswerResponseTypeDef = TypedDict(
    "DescribeLifecycleHookTypesAnswerResponseTypeDef",
    {
        "LifecycleHookTypes": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLifecycleHooksAnswerResponseTypeDef = TypedDict(
    "DescribeLifecycleHooksAnswerResponseTypeDef",
    {
        "LifecycleHooks": List["LifecycleHookTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeLifecycleHooksTypeTypeDef = TypedDict(
    "_RequiredDescribeLifecycleHooksTypeTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalDescribeLifecycleHooksTypeTypeDef = TypedDict(
    "_OptionalDescribeLifecycleHooksTypeTypeDef",
    {
        "LifecycleHookNames": List[str],
    },
    total=False,
)


class DescribeLifecycleHooksTypeTypeDef(
    _RequiredDescribeLifecycleHooksTypeTypeDef, _OptionalDescribeLifecycleHooksTypeTypeDef
):
    pass


_RequiredDescribeLoadBalancerTargetGroupsRequestTypeDef = TypedDict(
    "_RequiredDescribeLoadBalancerTargetGroupsRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalDescribeLoadBalancerTargetGroupsRequestTypeDef = TypedDict(
    "_OptionalDescribeLoadBalancerTargetGroupsRequestTypeDef",
    {
        "NextToken": str,
        "MaxRecords": int,
    },
    total=False,
)


class DescribeLoadBalancerTargetGroupsRequestTypeDef(
    _RequiredDescribeLoadBalancerTargetGroupsRequestTypeDef,
    _OptionalDescribeLoadBalancerTargetGroupsRequestTypeDef,
):
    pass


DescribeLoadBalancerTargetGroupsResponseResponseTypeDef = TypedDict(
    "DescribeLoadBalancerTargetGroupsResponseResponseTypeDef",
    {
        "LoadBalancerTargetGroups": List["LoadBalancerTargetGroupStateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeLoadBalancersRequestTypeDef = TypedDict(
    "_RequiredDescribeLoadBalancersRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalDescribeLoadBalancersRequestTypeDef = TypedDict(
    "_OptionalDescribeLoadBalancersRequestTypeDef",
    {
        "NextToken": str,
        "MaxRecords": int,
    },
    total=False,
)


class DescribeLoadBalancersRequestTypeDef(
    _RequiredDescribeLoadBalancersRequestTypeDef, _OptionalDescribeLoadBalancersRequestTypeDef
):
    pass


DescribeLoadBalancersResponseResponseTypeDef = TypedDict(
    "DescribeLoadBalancersResponseResponseTypeDef",
    {
        "LoadBalancers": List["LoadBalancerStateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMetricCollectionTypesAnswerResponseTypeDef = TypedDict(
    "DescribeMetricCollectionTypesAnswerResponseTypeDef",
    {
        "Metrics": List["MetricCollectionTypeTypeDef"],
        "Granularities": List["MetricGranularityTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNotificationConfigurationsAnswerResponseTypeDef = TypedDict(
    "DescribeNotificationConfigurationsAnswerResponseTypeDef",
    {
        "NotificationConfigurations": List["NotificationConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNotificationConfigurationsTypeTypeDef = TypedDict(
    "DescribeNotificationConfigurationsTypeTypeDef",
    {
        "AutoScalingGroupNames": List[str],
        "NextToken": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribePoliciesTypeTypeDef = TypedDict(
    "DescribePoliciesTypeTypeDef",
    {
        "AutoScalingGroupName": str,
        "PolicyNames": List[str],
        "PolicyTypes": List[str],
        "NextToken": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribeScalingActivitiesTypeTypeDef = TypedDict(
    "DescribeScalingActivitiesTypeTypeDef",
    {
        "ActivityIds": List[str],
        "AutoScalingGroupName": str,
        "IncludeDeletedGroups": bool,
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeScheduledActionsTypeTypeDef = TypedDict(
    "DescribeScheduledActionsTypeTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionNames": List[str],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "NextToken": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribeTagsTypeTypeDef = TypedDict(
    "DescribeTagsTypeTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribeTerminationPolicyTypesAnswerResponseTypeDef = TypedDict(
    "DescribeTerminationPolicyTypesAnswerResponseTypeDef",
    {
        "TerminationPolicyTypes": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWarmPoolAnswerResponseTypeDef = TypedDict(
    "DescribeWarmPoolAnswerResponseTypeDef",
    {
        "WarmPoolConfiguration": "WarmPoolConfigurationTypeDef",
        "Instances": List["InstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeWarmPoolTypeTypeDef = TypedDict(
    "_RequiredDescribeWarmPoolTypeTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalDescribeWarmPoolTypeTypeDef = TypedDict(
    "_OptionalDescribeWarmPoolTypeTypeDef",
    {
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeWarmPoolTypeTypeDef(
    _RequiredDescribeWarmPoolTypeTypeDef, _OptionalDescribeWarmPoolTypeTypeDef
):
    pass


DetachInstancesAnswerResponseTypeDef = TypedDict(
    "DetachInstancesAnswerResponseTypeDef",
    {
        "Activities": List["ActivityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetachInstancesQueryTypeDef = TypedDict(
    "_RequiredDetachInstancesQueryTypeDef",
    {
        "AutoScalingGroupName": str,
        "ShouldDecrementDesiredCapacity": bool,
    },
)
_OptionalDetachInstancesQueryTypeDef = TypedDict(
    "_OptionalDetachInstancesQueryTypeDef",
    {
        "InstanceIds": List[str],
    },
    total=False,
)


class DetachInstancesQueryTypeDef(
    _RequiredDetachInstancesQueryTypeDef, _OptionalDetachInstancesQueryTypeDef
):
    pass


DetachLoadBalancerTargetGroupsTypeTypeDef = TypedDict(
    "DetachLoadBalancerTargetGroupsTypeTypeDef",
    {
        "AutoScalingGroupName": str,
        "TargetGroupARNs": List[str],
    },
)

DetachLoadBalancersTypeTypeDef = TypedDict(
    "DetachLoadBalancersTypeTypeDef",
    {
        "AutoScalingGroupName": str,
        "LoadBalancerNames": List[str],
    },
)

_RequiredDisableMetricsCollectionQueryTypeDef = TypedDict(
    "_RequiredDisableMetricsCollectionQueryTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalDisableMetricsCollectionQueryTypeDef = TypedDict(
    "_OptionalDisableMetricsCollectionQueryTypeDef",
    {
        "Metrics": List[str],
    },
    total=False,
)


class DisableMetricsCollectionQueryTypeDef(
    _RequiredDisableMetricsCollectionQueryTypeDef, _OptionalDisableMetricsCollectionQueryTypeDef
):
    pass


EbsTypeDef = TypedDict(
    "EbsTypeDef",
    {
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": str,
        "DeleteOnTermination": bool,
        "Iops": int,
        "Encrypted": bool,
        "Throughput": int,
    },
    total=False,
)

_RequiredEnableMetricsCollectionQueryTypeDef = TypedDict(
    "_RequiredEnableMetricsCollectionQueryTypeDef",
    {
        "AutoScalingGroupName": str,
        "Granularity": str,
    },
)
_OptionalEnableMetricsCollectionQueryTypeDef = TypedDict(
    "_OptionalEnableMetricsCollectionQueryTypeDef",
    {
        "Metrics": List[str],
    },
    total=False,
)


class EnableMetricsCollectionQueryTypeDef(
    _RequiredEnableMetricsCollectionQueryTypeDef, _OptionalEnableMetricsCollectionQueryTypeDef
):
    pass


EnabledMetricTypeDef = TypedDict(
    "EnabledMetricTypeDef",
    {
        "Metric": str,
        "Granularity": str,
    },
    total=False,
)

EnterStandbyAnswerResponseTypeDef = TypedDict(
    "EnterStandbyAnswerResponseTypeDef",
    {
        "Activities": List["ActivityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnterStandbyQueryTypeDef = TypedDict(
    "_RequiredEnterStandbyQueryTypeDef",
    {
        "AutoScalingGroupName": str,
        "ShouldDecrementDesiredCapacity": bool,
    },
)
_OptionalEnterStandbyQueryTypeDef = TypedDict(
    "_OptionalEnterStandbyQueryTypeDef",
    {
        "InstanceIds": List[str],
    },
    total=False,
)


class EnterStandbyQueryTypeDef(
    _RequiredEnterStandbyQueryTypeDef, _OptionalEnterStandbyQueryTypeDef
):
    pass


_RequiredExecutePolicyTypeTypeDef = TypedDict(
    "_RequiredExecutePolicyTypeTypeDef",
    {
        "PolicyName": str,
    },
)
_OptionalExecutePolicyTypeTypeDef = TypedDict(
    "_OptionalExecutePolicyTypeTypeDef",
    {
        "AutoScalingGroupName": str,
        "HonorCooldown": bool,
        "MetricValue": float,
        "BreachThreshold": float,
    },
    total=False,
)


class ExecutePolicyTypeTypeDef(
    _RequiredExecutePolicyTypeTypeDef, _OptionalExecutePolicyTypeTypeDef
):
    pass


ExitStandbyAnswerResponseTypeDef = TypedDict(
    "ExitStandbyAnswerResponseTypeDef",
    {
        "Activities": List["ActivityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExitStandbyQueryTypeDef = TypedDict(
    "_RequiredExitStandbyQueryTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalExitStandbyQueryTypeDef = TypedDict(
    "_OptionalExitStandbyQueryTypeDef",
    {
        "InstanceIds": List[str],
    },
    total=False,
)


class ExitStandbyQueryTypeDef(_RequiredExitStandbyQueryTypeDef, _OptionalExitStandbyQueryTypeDef):
    pass


_RequiredFailedScheduledUpdateGroupActionRequestTypeDef = TypedDict(
    "_RequiredFailedScheduledUpdateGroupActionRequestTypeDef",
    {
        "ScheduledActionName": str,
    },
)
_OptionalFailedScheduledUpdateGroupActionRequestTypeDef = TypedDict(
    "_OptionalFailedScheduledUpdateGroupActionRequestTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)


class FailedScheduledUpdateGroupActionRequestTypeDef(
    _RequiredFailedScheduledUpdateGroupActionRequestTypeDef,
    _OptionalFailedScheduledUpdateGroupActionRequestTypeDef,
):
    pass


FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
    total=False,
)

GetPredictiveScalingForecastAnswerResponseTypeDef = TypedDict(
    "GetPredictiveScalingForecastAnswerResponseTypeDef",
    {
        "LoadForecast": List["LoadForecastTypeDef"],
        "CapacityForecast": "CapacityForecastTypeDef",
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPredictiveScalingForecastTypeTypeDef = TypedDict(
    "GetPredictiveScalingForecastTypeTypeDef",
    {
        "AutoScalingGroupName": str,
        "PolicyName": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)

InstanceMetadataOptionsTypeDef = TypedDict(
    "InstanceMetadataOptionsTypeDef",
    {
        "HttpTokens": InstanceMetadataHttpTokensStateType,
        "HttpPutResponseHopLimit": int,
        "HttpEndpoint": InstanceMetadataEndpointStateType,
    },
    total=False,
)

InstanceMonitoringTypeDef = TypedDict(
    "InstanceMonitoringTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

InstanceRefreshLivePoolProgressTypeDef = TypedDict(
    "InstanceRefreshLivePoolProgressTypeDef",
    {
        "PercentageComplete": int,
        "InstancesToUpdate": int,
    },
    total=False,
)

InstanceRefreshProgressDetailsTypeDef = TypedDict(
    "InstanceRefreshProgressDetailsTypeDef",
    {
        "LivePoolProgress": "InstanceRefreshLivePoolProgressTypeDef",
        "WarmPoolProgress": "InstanceRefreshWarmPoolProgressTypeDef",
    },
    total=False,
)

InstanceRefreshTypeDef = TypedDict(
    "InstanceRefreshTypeDef",
    {
        "InstanceRefreshId": str,
        "AutoScalingGroupName": str,
        "Status": InstanceRefreshStatusType,
        "StatusReason": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "PercentageComplete": int,
        "InstancesToUpdate": int,
        "ProgressDetails": "InstanceRefreshProgressDetailsTypeDef",
    },
    total=False,
)

InstanceRefreshWarmPoolProgressTypeDef = TypedDict(
    "InstanceRefreshWarmPoolProgressTypeDef",
    {
        "PercentageComplete": int,
        "InstancesToUpdate": int,
    },
    total=False,
)

_RequiredInstanceTypeDef = TypedDict(
    "_RequiredInstanceTypeDef",
    {
        "InstanceId": str,
        "AvailabilityZone": str,
        "LifecycleState": LifecycleStateType,
        "HealthStatus": str,
        "ProtectedFromScaleIn": bool,
    },
)
_OptionalInstanceTypeDef = TypedDict(
    "_OptionalInstanceTypeDef",
    {
        "InstanceType": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": "LaunchTemplateSpecificationTypeDef",
        "WeightedCapacity": str,
    },
    total=False,
)


class InstanceTypeDef(_RequiredInstanceTypeDef, _OptionalInstanceTypeDef):
    pass


InstancesDistributionTypeDef = TypedDict(
    "InstancesDistributionTypeDef",
    {
        "OnDemandAllocationStrategy": str,
        "OnDemandBaseCapacity": int,
        "OnDemandPercentageAboveBaseCapacity": int,
        "SpotAllocationStrategy": str,
        "SpotInstancePools": int,
        "SpotMaxPrice": str,
    },
    total=False,
)

LaunchConfigurationNameTypeTypeDef = TypedDict(
    "LaunchConfigurationNameTypeTypeDef",
    {
        "LaunchConfigurationName": str,
    },
)

LaunchConfigurationNamesTypeTypeDef = TypedDict(
    "LaunchConfigurationNamesTypeTypeDef",
    {
        "LaunchConfigurationNames": List[str],
        "NextToken": str,
        "MaxRecords": int,
    },
    total=False,
)

_RequiredLaunchConfigurationTypeDef = TypedDict(
    "_RequiredLaunchConfigurationTypeDef",
    {
        "LaunchConfigurationName": str,
        "ImageId": str,
        "InstanceType": str,
        "CreatedTime": datetime,
    },
)
_OptionalLaunchConfigurationTypeDef = TypedDict(
    "_OptionalLaunchConfigurationTypeDef",
    {
        "LaunchConfigurationARN": str,
        "KeyName": str,
        "SecurityGroups": List[str],
        "ClassicLinkVPCId": str,
        "ClassicLinkVPCSecurityGroups": List[str],
        "UserData": str,
        "KernelId": str,
        "RamdiskId": str,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "InstanceMonitoring": "InstanceMonitoringTypeDef",
        "SpotPrice": str,
        "IamInstanceProfile": str,
        "EbsOptimized": bool,
        "AssociatePublicIpAddress": bool,
        "PlacementTenancy": str,
        "MetadataOptions": "InstanceMetadataOptionsTypeDef",
    },
    total=False,
)


class LaunchConfigurationTypeDef(
    _RequiredLaunchConfigurationTypeDef, _OptionalLaunchConfigurationTypeDef
):
    pass


LaunchConfigurationsTypeResponseTypeDef = TypedDict(
    "LaunchConfigurationsTypeResponseTypeDef",
    {
        "LaunchConfigurations": List["LaunchConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LaunchTemplateOverridesTypeDef = TypedDict(
    "LaunchTemplateOverridesTypeDef",
    {
        "InstanceType": str,
        "WeightedCapacity": str,
        "LaunchTemplateSpecification": "LaunchTemplateSpecificationTypeDef",
    },
    total=False,
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "Version": str,
    },
    total=False,
)

LaunchTemplateTypeDef = TypedDict(
    "LaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": "LaunchTemplateSpecificationTypeDef",
        "Overrides": List["LaunchTemplateOverridesTypeDef"],
    },
    total=False,
)

_RequiredLifecycleHookSpecificationTypeDef = TypedDict(
    "_RequiredLifecycleHookSpecificationTypeDef",
    {
        "LifecycleHookName": str,
        "LifecycleTransition": str,
    },
)
_OptionalLifecycleHookSpecificationTypeDef = TypedDict(
    "_OptionalLifecycleHookSpecificationTypeDef",
    {
        "NotificationMetadata": str,
        "HeartbeatTimeout": int,
        "DefaultResult": str,
        "NotificationTargetARN": str,
        "RoleARN": str,
    },
    total=False,
)


class LifecycleHookSpecificationTypeDef(
    _RequiredLifecycleHookSpecificationTypeDef, _OptionalLifecycleHookSpecificationTypeDef
):
    pass


LifecycleHookTypeDef = TypedDict(
    "LifecycleHookTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
        "LifecycleTransition": str,
        "NotificationTargetARN": str,
        "RoleARN": str,
        "NotificationMetadata": str,
        "HeartbeatTimeout": int,
        "GlobalTimeout": int,
        "DefaultResult": str,
    },
    total=False,
)

LoadBalancerStateTypeDef = TypedDict(
    "LoadBalancerStateTypeDef",
    {
        "LoadBalancerName": str,
        "State": str,
    },
    total=False,
)

LoadBalancerTargetGroupStateTypeDef = TypedDict(
    "LoadBalancerTargetGroupStateTypeDef",
    {
        "LoadBalancerTargetGroupARN": str,
        "State": str,
    },
    total=False,
)

LoadForecastTypeDef = TypedDict(
    "LoadForecastTypeDef",
    {
        "Timestamps": List[datetime],
        "Values": List[float],
        "MetricSpecification": "PredictiveScalingMetricSpecificationTypeDef",
    },
)

MetricCollectionTypeTypeDef = TypedDict(
    "MetricCollectionTypeTypeDef",
    {
        "Metric": str,
    },
    total=False,
)

MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

MetricGranularityTypeTypeDef = TypedDict(
    "MetricGranularityTypeTypeDef",
    {
        "Granularity": str,
    },
    total=False,
)

MixedInstancesPolicyTypeDef = TypedDict(
    "MixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": "LaunchTemplateTypeDef",
        "InstancesDistribution": "InstancesDistributionTypeDef",
    },
    total=False,
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "AutoScalingGroupName": str,
        "TopicARN": str,
        "NotificationType": str,
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

PoliciesTypeResponseTypeDef = TypedDict(
    "PoliciesTypeResponseTypeDef",
    {
        "ScalingPolicies": List["ScalingPolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PolicyARNTypeResponseTypeDef = TypedDict(
    "PolicyARNTypeResponseTypeDef",
    {
        "PolicyARN": str,
        "Alarms": List["AlarmTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPredefinedMetricSpecificationTypeDef = TypedDict(
    "_RequiredPredefinedMetricSpecificationTypeDef",
    {
        "PredefinedMetricType": MetricTypeType,
    },
)
_OptionalPredefinedMetricSpecificationTypeDef = TypedDict(
    "_OptionalPredefinedMetricSpecificationTypeDef",
    {
        "ResourceLabel": str,
    },
    total=False,
)


class PredefinedMetricSpecificationTypeDef(
    _RequiredPredefinedMetricSpecificationTypeDef, _OptionalPredefinedMetricSpecificationTypeDef
):
    pass


_RequiredPredictiveScalingConfigurationTypeDef = TypedDict(
    "_RequiredPredictiveScalingConfigurationTypeDef",
    {
        "MetricSpecifications": List["PredictiveScalingMetricSpecificationTypeDef"],
    },
)
_OptionalPredictiveScalingConfigurationTypeDef = TypedDict(
    "_OptionalPredictiveScalingConfigurationTypeDef",
    {
        "Mode": PredictiveScalingModeType,
        "SchedulingBufferTime": int,
        "MaxCapacityBreachBehavior": PredictiveScalingMaxCapacityBreachBehaviorType,
        "MaxCapacityBuffer": int,
    },
    total=False,
)


class PredictiveScalingConfigurationTypeDef(
    _RequiredPredictiveScalingConfigurationTypeDef, _OptionalPredictiveScalingConfigurationTypeDef
):
    pass


_RequiredPredictiveScalingMetricSpecificationTypeDef = TypedDict(
    "_RequiredPredictiveScalingMetricSpecificationTypeDef",
    {
        "TargetValue": float,
    },
)
_OptionalPredictiveScalingMetricSpecificationTypeDef = TypedDict(
    "_OptionalPredictiveScalingMetricSpecificationTypeDef",
    {
        "PredefinedMetricPairSpecification": "PredictiveScalingPredefinedMetricPairTypeDef",
        "PredefinedScalingMetricSpecification": "PredictiveScalingPredefinedScalingMetricTypeDef",
        "PredefinedLoadMetricSpecification": "PredictiveScalingPredefinedLoadMetricTypeDef",
    },
    total=False,
)


class PredictiveScalingMetricSpecificationTypeDef(
    _RequiredPredictiveScalingMetricSpecificationTypeDef,
    _OptionalPredictiveScalingMetricSpecificationTypeDef,
):
    pass


_RequiredPredictiveScalingPredefinedLoadMetricTypeDef = TypedDict(
    "_RequiredPredictiveScalingPredefinedLoadMetricTypeDef",
    {
        "PredefinedMetricType": PredefinedLoadMetricTypeType,
    },
)
_OptionalPredictiveScalingPredefinedLoadMetricTypeDef = TypedDict(
    "_OptionalPredictiveScalingPredefinedLoadMetricTypeDef",
    {
        "ResourceLabel": str,
    },
    total=False,
)


class PredictiveScalingPredefinedLoadMetricTypeDef(
    _RequiredPredictiveScalingPredefinedLoadMetricTypeDef,
    _OptionalPredictiveScalingPredefinedLoadMetricTypeDef,
):
    pass


_RequiredPredictiveScalingPredefinedMetricPairTypeDef = TypedDict(
    "_RequiredPredictiveScalingPredefinedMetricPairTypeDef",
    {
        "PredefinedMetricType": PredefinedMetricPairTypeType,
    },
)
_OptionalPredictiveScalingPredefinedMetricPairTypeDef = TypedDict(
    "_OptionalPredictiveScalingPredefinedMetricPairTypeDef",
    {
        "ResourceLabel": str,
    },
    total=False,
)


class PredictiveScalingPredefinedMetricPairTypeDef(
    _RequiredPredictiveScalingPredefinedMetricPairTypeDef,
    _OptionalPredictiveScalingPredefinedMetricPairTypeDef,
):
    pass


_RequiredPredictiveScalingPredefinedScalingMetricTypeDef = TypedDict(
    "_RequiredPredictiveScalingPredefinedScalingMetricTypeDef",
    {
        "PredefinedMetricType": PredefinedScalingMetricTypeType,
    },
)
_OptionalPredictiveScalingPredefinedScalingMetricTypeDef = TypedDict(
    "_OptionalPredictiveScalingPredefinedScalingMetricTypeDef",
    {
        "ResourceLabel": str,
    },
    total=False,
)


class PredictiveScalingPredefinedScalingMetricTypeDef(
    _RequiredPredictiveScalingPredefinedScalingMetricTypeDef,
    _OptionalPredictiveScalingPredefinedScalingMetricTypeDef,
):
    pass


ProcessTypeTypeDef = TypedDict(
    "ProcessTypeTypeDef",
    {
        "ProcessName": str,
    },
)

ProcessesTypeResponseTypeDef = TypedDict(
    "ProcessesTypeResponseTypeDef",
    {
        "Processes": List["ProcessTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutLifecycleHookTypeTypeDef = TypedDict(
    "_RequiredPutLifecycleHookTypeTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
    },
)
_OptionalPutLifecycleHookTypeTypeDef = TypedDict(
    "_OptionalPutLifecycleHookTypeTypeDef",
    {
        "LifecycleTransition": str,
        "RoleARN": str,
        "NotificationTargetARN": str,
        "NotificationMetadata": str,
        "HeartbeatTimeout": int,
        "DefaultResult": str,
    },
    total=False,
)


class PutLifecycleHookTypeTypeDef(
    _RequiredPutLifecycleHookTypeTypeDef, _OptionalPutLifecycleHookTypeTypeDef
):
    pass


PutNotificationConfigurationTypeTypeDef = TypedDict(
    "PutNotificationConfigurationTypeTypeDef",
    {
        "AutoScalingGroupName": str,
        "TopicARN": str,
        "NotificationTypes": List[str],
    },
)

_RequiredPutScalingPolicyTypeTypeDef = TypedDict(
    "_RequiredPutScalingPolicyTypeTypeDef",
    {
        "AutoScalingGroupName": str,
        "PolicyName": str,
    },
)
_OptionalPutScalingPolicyTypeTypeDef = TypedDict(
    "_OptionalPutScalingPolicyTypeTypeDef",
    {
        "PolicyType": str,
        "AdjustmentType": str,
        "MinAdjustmentStep": int,
        "MinAdjustmentMagnitude": int,
        "ScalingAdjustment": int,
        "Cooldown": int,
        "MetricAggregationType": str,
        "StepAdjustments": List["StepAdjustmentTypeDef"],
        "EstimatedInstanceWarmup": int,
        "TargetTrackingConfiguration": "TargetTrackingConfigurationTypeDef",
        "Enabled": bool,
        "PredictiveScalingConfiguration": "PredictiveScalingConfigurationTypeDef",
    },
    total=False,
)


class PutScalingPolicyTypeTypeDef(
    _RequiredPutScalingPolicyTypeTypeDef, _OptionalPutScalingPolicyTypeTypeDef
):
    pass


_RequiredPutScheduledUpdateGroupActionTypeTypeDef = TypedDict(
    "_RequiredPutScheduledUpdateGroupActionTypeTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionName": str,
    },
)
_OptionalPutScheduledUpdateGroupActionTypeTypeDef = TypedDict(
    "_OptionalPutScheduledUpdateGroupActionTypeTypeDef",
    {
        "Time": Union[datetime, str],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Recurrence": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
        "TimeZone": str,
    },
    total=False,
)


class PutScheduledUpdateGroupActionTypeTypeDef(
    _RequiredPutScheduledUpdateGroupActionTypeTypeDef,
    _OptionalPutScheduledUpdateGroupActionTypeTypeDef,
):
    pass


_RequiredPutWarmPoolTypeTypeDef = TypedDict(
    "_RequiredPutWarmPoolTypeTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalPutWarmPoolTypeTypeDef = TypedDict(
    "_OptionalPutWarmPoolTypeTypeDef",
    {
        "MaxGroupPreparedCapacity": int,
        "MinSize": int,
        "PoolState": WarmPoolStateType,
    },
    total=False,
)


class PutWarmPoolTypeTypeDef(_RequiredPutWarmPoolTypeTypeDef, _OptionalPutWarmPoolTypeTypeDef):
    pass


_RequiredRecordLifecycleActionHeartbeatTypeTypeDef = TypedDict(
    "_RequiredRecordLifecycleActionHeartbeatTypeTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
    },
)
_OptionalRecordLifecycleActionHeartbeatTypeTypeDef = TypedDict(
    "_OptionalRecordLifecycleActionHeartbeatTypeTypeDef",
    {
        "LifecycleActionToken": str,
        "InstanceId": str,
    },
    total=False,
)


class RecordLifecycleActionHeartbeatTypeTypeDef(
    _RequiredRecordLifecycleActionHeartbeatTypeTypeDef,
    _OptionalRecordLifecycleActionHeartbeatTypeTypeDef,
):
    pass


RefreshPreferencesTypeDef = TypedDict(
    "RefreshPreferencesTypeDef",
    {
        "MinHealthyPercentage": int,
        "InstanceWarmup": int,
        "CheckpointPercentages": List[int],
        "CheckpointDelay": int,
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

ScalingPolicyTypeDef = TypedDict(
    "ScalingPolicyTypeDef",
    {
        "AutoScalingGroupName": str,
        "PolicyName": str,
        "PolicyARN": str,
        "PolicyType": str,
        "AdjustmentType": str,
        "MinAdjustmentStep": int,
        "MinAdjustmentMagnitude": int,
        "ScalingAdjustment": int,
        "Cooldown": int,
        "StepAdjustments": List["StepAdjustmentTypeDef"],
        "MetricAggregationType": str,
        "EstimatedInstanceWarmup": int,
        "Alarms": List["AlarmTypeDef"],
        "TargetTrackingConfiguration": "TargetTrackingConfigurationTypeDef",
        "Enabled": bool,
        "PredictiveScalingConfiguration": "PredictiveScalingConfigurationTypeDef",
    },
    total=False,
)

_RequiredScalingProcessQueryTypeDef = TypedDict(
    "_RequiredScalingProcessQueryTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalScalingProcessQueryTypeDef = TypedDict(
    "_OptionalScalingProcessQueryTypeDef",
    {
        "ScalingProcesses": List[str],
    },
    total=False,
)


class ScalingProcessQueryTypeDef(
    _RequiredScalingProcessQueryTypeDef, _OptionalScalingProcessQueryTypeDef
):
    pass


ScheduledActionsTypeResponseTypeDef = TypedDict(
    "ScheduledActionsTypeResponseTypeDef",
    {
        "ScheduledUpdateGroupActions": List["ScheduledUpdateGroupActionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredScheduledUpdateGroupActionRequestTypeDef = TypedDict(
    "_RequiredScheduledUpdateGroupActionRequestTypeDef",
    {
        "ScheduledActionName": str,
    },
)
_OptionalScheduledUpdateGroupActionRequestTypeDef = TypedDict(
    "_OptionalScheduledUpdateGroupActionRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Recurrence": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
        "TimeZone": str,
    },
    total=False,
)


class ScheduledUpdateGroupActionRequestTypeDef(
    _RequiredScheduledUpdateGroupActionRequestTypeDef,
    _OptionalScheduledUpdateGroupActionRequestTypeDef,
):
    pass


ScheduledUpdateGroupActionTypeDef = TypedDict(
    "ScheduledUpdateGroupActionTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionName": str,
        "ScheduledActionARN": str,
        "Time": datetime,
        "StartTime": datetime,
        "EndTime": datetime,
        "Recurrence": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
        "TimeZone": str,
    },
    total=False,
)

_RequiredSetDesiredCapacityTypeTypeDef = TypedDict(
    "_RequiredSetDesiredCapacityTypeTypeDef",
    {
        "AutoScalingGroupName": str,
        "DesiredCapacity": int,
    },
)
_OptionalSetDesiredCapacityTypeTypeDef = TypedDict(
    "_OptionalSetDesiredCapacityTypeTypeDef",
    {
        "HonorCooldown": bool,
    },
    total=False,
)


class SetDesiredCapacityTypeTypeDef(
    _RequiredSetDesiredCapacityTypeTypeDef, _OptionalSetDesiredCapacityTypeTypeDef
):
    pass


_RequiredSetInstanceHealthQueryTypeDef = TypedDict(
    "_RequiredSetInstanceHealthQueryTypeDef",
    {
        "InstanceId": str,
        "HealthStatus": str,
    },
)
_OptionalSetInstanceHealthQueryTypeDef = TypedDict(
    "_OptionalSetInstanceHealthQueryTypeDef",
    {
        "ShouldRespectGracePeriod": bool,
    },
    total=False,
)


class SetInstanceHealthQueryTypeDef(
    _RequiredSetInstanceHealthQueryTypeDef, _OptionalSetInstanceHealthQueryTypeDef
):
    pass


SetInstanceProtectionQueryTypeDef = TypedDict(
    "SetInstanceProtectionQueryTypeDef",
    {
        "InstanceIds": List[str],
        "AutoScalingGroupName": str,
        "ProtectedFromScaleIn": bool,
    },
)

StartInstanceRefreshAnswerResponseTypeDef = TypedDict(
    "StartInstanceRefreshAnswerResponseTypeDef",
    {
        "InstanceRefreshId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartInstanceRefreshTypeTypeDef = TypedDict(
    "_RequiredStartInstanceRefreshTypeTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalStartInstanceRefreshTypeTypeDef = TypedDict(
    "_OptionalStartInstanceRefreshTypeTypeDef",
    {
        "Strategy": Literal["Rolling"],
        "Preferences": "RefreshPreferencesTypeDef",
    },
    total=False,
)


class StartInstanceRefreshTypeTypeDef(
    _RequiredStartInstanceRefreshTypeTypeDef, _OptionalStartInstanceRefreshTypeTypeDef
):
    pass


_RequiredStepAdjustmentTypeDef = TypedDict(
    "_RequiredStepAdjustmentTypeDef",
    {
        "ScalingAdjustment": int,
    },
)
_OptionalStepAdjustmentTypeDef = TypedDict(
    "_OptionalStepAdjustmentTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
    },
    total=False,
)


class StepAdjustmentTypeDef(_RequiredStepAdjustmentTypeDef, _OptionalStepAdjustmentTypeDef):
    pass


SuspendedProcessTypeDef = TypedDict(
    "SuspendedProcessTypeDef",
    {
        "ProcessName": str,
        "SuspensionReason": str,
    },
    total=False,
)

TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {
        "ResourceId": str,
        "ResourceType": str,
        "Key": str,
        "Value": str,
        "PropagateAtLaunch": bool,
    },
    total=False,
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
        "ResourceId": str,
        "ResourceType": str,
        "Value": str,
        "PropagateAtLaunch": bool,
    },
    total=False,
)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


TagsTypeResponseTypeDef = TypedDict(
    "TagsTypeResponseTypeDef",
    {
        "Tags": List["TagDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTargetTrackingConfigurationTypeDef = TypedDict(
    "_RequiredTargetTrackingConfigurationTypeDef",
    {
        "TargetValue": float,
    },
)
_OptionalTargetTrackingConfigurationTypeDef = TypedDict(
    "_OptionalTargetTrackingConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": "PredefinedMetricSpecificationTypeDef",
        "CustomizedMetricSpecification": "CustomizedMetricSpecificationTypeDef",
        "DisableScaleIn": bool,
    },
    total=False,
)


class TargetTrackingConfigurationTypeDef(
    _RequiredTargetTrackingConfigurationTypeDef, _OptionalTargetTrackingConfigurationTypeDef
):
    pass


TerminateInstanceInAutoScalingGroupTypeTypeDef = TypedDict(
    "TerminateInstanceInAutoScalingGroupTypeTypeDef",
    {
        "InstanceId": str,
        "ShouldDecrementDesiredCapacity": bool,
    },
)

_RequiredUpdateAutoScalingGroupTypeTypeDef = TypedDict(
    "_RequiredUpdateAutoScalingGroupTypeTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
_OptionalUpdateAutoScalingGroupTypeTypeDef = TypedDict(
    "_OptionalUpdateAutoScalingGroupTypeTypeDef",
    {
        "LaunchConfigurationName": str,
        "LaunchTemplate": "LaunchTemplateSpecificationTypeDef",
        "MixedInstancesPolicy": "MixedInstancesPolicyTypeDef",
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
        "DefaultCooldown": int,
        "AvailabilityZones": List[str],
        "HealthCheckType": str,
        "HealthCheckGracePeriod": int,
        "PlacementGroup": str,
        "VPCZoneIdentifier": str,
        "TerminationPolicies": List[str],
        "NewInstancesProtectedFromScaleIn": bool,
        "ServiceLinkedRoleARN": str,
        "MaxInstanceLifetime": int,
        "CapacityRebalance": bool,
    },
    total=False,
)


class UpdateAutoScalingGroupTypeTypeDef(
    _RequiredUpdateAutoScalingGroupTypeTypeDef, _OptionalUpdateAutoScalingGroupTypeTypeDef
):
    pass


WarmPoolConfigurationTypeDef = TypedDict(
    "WarmPoolConfigurationTypeDef",
    {
        "MaxGroupPreparedCapacity": int,
        "MinSize": int,
        "PoolState": WarmPoolStateType,
        "Status": Literal["PendingDelete"],
    },
    total=False,
)
