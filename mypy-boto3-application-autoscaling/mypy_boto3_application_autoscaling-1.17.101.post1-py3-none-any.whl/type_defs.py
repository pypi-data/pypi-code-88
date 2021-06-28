"""
Type annotations for application-autoscaling service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/type_defs.html)

Usage::

    ```python
    from mypy_boto3_application_autoscaling.type_defs import AlarmTypeDef

    data: AlarmTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AdjustmentTypeType,
    MetricAggregationTypeType,
    MetricStatisticType,
    MetricTypeType,
    PolicyTypeType,
    ScalableDimensionType,
    ScalingActivityStatusCodeType,
    ServiceNamespaceType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AlarmTypeDef",
    "CustomizedMetricSpecificationTypeDef",
    "DeleteScalingPolicyRequestTypeDef",
    "DeleteScheduledActionRequestTypeDef",
    "DeregisterScalableTargetRequestTypeDef",
    "DescribeScalableTargetsRequestTypeDef",
    "DescribeScalableTargetsResponseResponseTypeDef",
    "DescribeScalingActivitiesRequestTypeDef",
    "DescribeScalingActivitiesResponseResponseTypeDef",
    "DescribeScalingPoliciesRequestTypeDef",
    "DescribeScalingPoliciesResponseResponseTypeDef",
    "DescribeScheduledActionsRequestTypeDef",
    "DescribeScheduledActionsResponseResponseTypeDef",
    "MetricDimensionTypeDef",
    "PaginatorConfigTypeDef",
    "PredefinedMetricSpecificationTypeDef",
    "PutScalingPolicyRequestTypeDef",
    "PutScalingPolicyResponseResponseTypeDef",
    "PutScheduledActionRequestTypeDef",
    "RegisterScalableTargetRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ScalableTargetActionTypeDef",
    "ScalableTargetTypeDef",
    "ScalingActivityTypeDef",
    "ScalingPolicyTypeDef",
    "ScheduledActionTypeDef",
    "StepAdjustmentTypeDef",
    "StepScalingPolicyConfigurationTypeDef",
    "SuspendedStateTypeDef",
    "TargetTrackingScalingPolicyConfigurationTypeDef",
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "AlarmName": str,
        "AlarmARN": str,
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


DeleteScalingPolicyRequestTypeDef = TypedDict(
    "DeleteScalingPolicyRequestTypeDef",
    {
        "PolicyName": str,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
    },
)

DeleteScheduledActionRequestTypeDef = TypedDict(
    "DeleteScheduledActionRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ScheduledActionName": str,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
    },
)

DeregisterScalableTargetRequestTypeDef = TypedDict(
    "DeregisterScalableTargetRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
    },
)

_RequiredDescribeScalableTargetsRequestTypeDef = TypedDict(
    "_RequiredDescribeScalableTargetsRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
    },
)
_OptionalDescribeScalableTargetsRequestTypeDef = TypedDict(
    "_OptionalDescribeScalableTargetsRequestTypeDef",
    {
        "ResourceIds": List[str],
        "ScalableDimension": ScalableDimensionType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeScalableTargetsRequestTypeDef(
    _RequiredDescribeScalableTargetsRequestTypeDef, _OptionalDescribeScalableTargetsRequestTypeDef
):
    pass


DescribeScalableTargetsResponseResponseTypeDef = TypedDict(
    "DescribeScalableTargetsResponseResponseTypeDef",
    {
        "ScalableTargets": List["ScalableTargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeScalingActivitiesRequestTypeDef = TypedDict(
    "_RequiredDescribeScalingActivitiesRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
    },
)
_OptionalDescribeScalingActivitiesRequestTypeDef = TypedDict(
    "_OptionalDescribeScalingActivitiesRequestTypeDef",
    {
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeScalingActivitiesRequestTypeDef(
    _RequiredDescribeScalingActivitiesRequestTypeDef,
    _OptionalDescribeScalingActivitiesRequestTypeDef,
):
    pass


DescribeScalingActivitiesResponseResponseTypeDef = TypedDict(
    "DescribeScalingActivitiesResponseResponseTypeDef",
    {
        "ScalingActivities": List["ScalingActivityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeScalingPoliciesRequestTypeDef = TypedDict(
    "_RequiredDescribeScalingPoliciesRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
    },
)
_OptionalDescribeScalingPoliciesRequestTypeDef = TypedDict(
    "_OptionalDescribeScalingPoliciesRequestTypeDef",
    {
        "PolicyNames": List[str],
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeScalingPoliciesRequestTypeDef(
    _RequiredDescribeScalingPoliciesRequestTypeDef, _OptionalDescribeScalingPoliciesRequestTypeDef
):
    pass


DescribeScalingPoliciesResponseResponseTypeDef = TypedDict(
    "DescribeScalingPoliciesResponseResponseTypeDef",
    {
        "ScalingPolicies": List["ScalingPolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeScheduledActionsRequestTypeDef = TypedDict(
    "_RequiredDescribeScheduledActionsRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
    },
)
_OptionalDescribeScheduledActionsRequestTypeDef = TypedDict(
    "_OptionalDescribeScheduledActionsRequestTypeDef",
    {
        "ScheduledActionNames": List[str],
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeScheduledActionsRequestTypeDef(
    _RequiredDescribeScheduledActionsRequestTypeDef, _OptionalDescribeScheduledActionsRequestTypeDef
):
    pass


DescribeScheduledActionsResponseResponseTypeDef = TypedDict(
    "DescribeScheduledActionsResponseResponseTypeDef",
    {
        "ScheduledActions": List["ScheduledActionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
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


_RequiredPutScalingPolicyRequestTypeDef = TypedDict(
    "_RequiredPutScalingPolicyRequestTypeDef",
    {
        "PolicyName": str,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
    },
)
_OptionalPutScalingPolicyRequestTypeDef = TypedDict(
    "_OptionalPutScalingPolicyRequestTypeDef",
    {
        "PolicyType": PolicyTypeType,
        "StepScalingPolicyConfiguration": "StepScalingPolicyConfigurationTypeDef",
        "TargetTrackingScalingPolicyConfiguration": "TargetTrackingScalingPolicyConfigurationTypeDef",
    },
    total=False,
)


class PutScalingPolicyRequestTypeDef(
    _RequiredPutScalingPolicyRequestTypeDef, _OptionalPutScalingPolicyRequestTypeDef
):
    pass


PutScalingPolicyResponseResponseTypeDef = TypedDict(
    "PutScalingPolicyResponseResponseTypeDef",
    {
        "PolicyARN": str,
        "Alarms": List["AlarmTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutScheduledActionRequestTypeDef = TypedDict(
    "_RequiredPutScheduledActionRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ScheduledActionName": str,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
    },
)
_OptionalPutScheduledActionRequestTypeDef = TypedDict(
    "_OptionalPutScheduledActionRequestTypeDef",
    {
        "Schedule": str,
        "Timezone": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "ScalableTargetAction": "ScalableTargetActionTypeDef",
    },
    total=False,
)


class PutScheduledActionRequestTypeDef(
    _RequiredPutScheduledActionRequestTypeDef, _OptionalPutScheduledActionRequestTypeDef
):
    pass


_RequiredRegisterScalableTargetRequestTypeDef = TypedDict(
    "_RequiredRegisterScalableTargetRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
    },
)
_OptionalRegisterScalableTargetRequestTypeDef = TypedDict(
    "_OptionalRegisterScalableTargetRequestTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "RoleARN": str,
        "SuspendedState": "SuspendedStateTypeDef",
    },
    total=False,
)


class RegisterScalableTargetRequestTypeDef(
    _RequiredRegisterScalableTargetRequestTypeDef, _OptionalRegisterScalableTargetRequestTypeDef
):
    pass


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

ScalableTargetActionTypeDef = TypedDict(
    "ScalableTargetActionTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
    },
    total=False,
)

_RequiredScalableTargetTypeDef = TypedDict(
    "_RequiredScalableTargetTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "MinCapacity": int,
        "MaxCapacity": int,
        "RoleARN": str,
        "CreationTime": datetime,
    },
)
_OptionalScalableTargetTypeDef = TypedDict(
    "_OptionalScalableTargetTypeDef",
    {
        "SuspendedState": "SuspendedStateTypeDef",
    },
    total=False,
)


class ScalableTargetTypeDef(_RequiredScalableTargetTypeDef, _OptionalScalableTargetTypeDef):
    pass


_RequiredScalingActivityTypeDef = TypedDict(
    "_RequiredScalingActivityTypeDef",
    {
        "ActivityId": str,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "StatusCode": ScalingActivityStatusCodeType,
    },
)
_OptionalScalingActivityTypeDef = TypedDict(
    "_OptionalScalingActivityTypeDef",
    {
        "EndTime": datetime,
        "StatusMessage": str,
        "Details": str,
    },
    total=False,
)


class ScalingActivityTypeDef(_RequiredScalingActivityTypeDef, _OptionalScalingActivityTypeDef):
    pass


_RequiredScalingPolicyTypeDef = TypedDict(
    "_RequiredScalingPolicyTypeDef",
    {
        "PolicyARN": str,
        "PolicyName": str,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "PolicyType": PolicyTypeType,
        "CreationTime": datetime,
    },
)
_OptionalScalingPolicyTypeDef = TypedDict(
    "_OptionalScalingPolicyTypeDef",
    {
        "StepScalingPolicyConfiguration": "StepScalingPolicyConfigurationTypeDef",
        "TargetTrackingScalingPolicyConfiguration": "TargetTrackingScalingPolicyConfigurationTypeDef",
        "Alarms": List["AlarmTypeDef"],
    },
    total=False,
)


class ScalingPolicyTypeDef(_RequiredScalingPolicyTypeDef, _OptionalScalingPolicyTypeDef):
    pass


_RequiredScheduledActionTypeDef = TypedDict(
    "_RequiredScheduledActionTypeDef",
    {
        "ScheduledActionName": str,
        "ScheduledActionARN": str,
        "ServiceNamespace": ServiceNamespaceType,
        "Schedule": str,
        "ResourceId": str,
        "CreationTime": datetime,
    },
)
_OptionalScheduledActionTypeDef = TypedDict(
    "_OptionalScheduledActionTypeDef",
    {
        "Timezone": str,
        "ScalableDimension": ScalableDimensionType,
        "StartTime": datetime,
        "EndTime": datetime,
        "ScalableTargetAction": "ScalableTargetActionTypeDef",
    },
    total=False,
)


class ScheduledActionTypeDef(_RequiredScheduledActionTypeDef, _OptionalScheduledActionTypeDef):
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


StepScalingPolicyConfigurationTypeDef = TypedDict(
    "StepScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": AdjustmentTypeType,
        "StepAdjustments": List["StepAdjustmentTypeDef"],
        "MinAdjustmentMagnitude": int,
        "Cooldown": int,
        "MetricAggregationType": MetricAggregationTypeType,
    },
    total=False,
)

SuspendedStateTypeDef = TypedDict(
    "SuspendedStateTypeDef",
    {
        "DynamicScalingInSuspended": bool,
        "DynamicScalingOutSuspended": bool,
        "ScheduledScalingSuspended": bool,
    },
    total=False,
)

_RequiredTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "_RequiredTargetTrackingScalingPolicyConfigurationTypeDef",
    {
        "TargetValue": float,
    },
)
_OptionalTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "_OptionalTargetTrackingScalingPolicyConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": "PredefinedMetricSpecificationTypeDef",
        "CustomizedMetricSpecification": "CustomizedMetricSpecificationTypeDef",
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "DisableScaleIn": bool,
    },
    total=False,
)


class TargetTrackingScalingPolicyConfigurationTypeDef(
    _RequiredTargetTrackingScalingPolicyConfigurationTypeDef,
    _OptionalTargetTrackingScalingPolicyConfigurationTypeDef,
):
    pass
