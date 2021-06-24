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
from typing import List

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
    "DescribeScalableTargetsResponseTypeDef",
    "DescribeScalingActivitiesResponseTypeDef",
    "DescribeScalingPoliciesResponseTypeDef",
    "DescribeScheduledActionsResponseTypeDef",
    "MetricDimensionTypeDef",
    "PaginatorConfigTypeDef",
    "PredefinedMetricSpecificationTypeDef",
    "PutScalingPolicyResponseTypeDef",
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


DescribeScalableTargetsResponseTypeDef = TypedDict(
    "DescribeScalableTargetsResponseTypeDef",
    {
        "ScalableTargets": List["ScalableTargetTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeScalingActivitiesResponseTypeDef = TypedDict(
    "DescribeScalingActivitiesResponseTypeDef",
    {
        "ScalingActivities": List["ScalingActivityTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeScalingPoliciesResponseTypeDef = TypedDict(
    "DescribeScalingPoliciesResponseTypeDef",
    {
        "ScalingPolicies": List["ScalingPolicyTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeScheduledActionsResponseTypeDef = TypedDict(
    "DescribeScheduledActionsResponseTypeDef",
    {
        "ScheduledActions": List["ScheduledActionTypeDef"],
        "NextToken": str,
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


_RequiredPutScalingPolicyResponseTypeDef = TypedDict(
    "_RequiredPutScalingPolicyResponseTypeDef",
    {
        "PolicyARN": str,
    },
)
_OptionalPutScalingPolicyResponseTypeDef = TypedDict(
    "_OptionalPutScalingPolicyResponseTypeDef",
    {
        "Alarms": List["AlarmTypeDef"],
    },
    total=False,
)


class PutScalingPolicyResponseTypeDef(
    _RequiredPutScalingPolicyResponseTypeDef, _OptionalPutScalingPolicyResponseTypeDef
):
    pass


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
