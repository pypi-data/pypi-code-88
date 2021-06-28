"""
Type annotations for compute-optimizer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_compute_optimizer.type_defs import AutoScalingGroupConfigurationTypeDef

    data: AutoScalingGroupConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    EBSFindingType,
    EBSMetricNameType,
    ExportableAutoScalingGroupFieldType,
    ExportableInstanceFieldType,
    ExportableLambdaFunctionFieldType,
    ExportableVolumeFieldType,
    FilterNameType,
    FindingReasonCodeType,
    FindingType,
    InstanceRecommendationFindingReasonCodeType,
    JobFilterNameType,
    JobStatusType,
    LambdaFunctionMemoryMetricStatisticType,
    LambdaFunctionMetricNameType,
    LambdaFunctionMetricStatisticType,
    LambdaFunctionRecommendationFilterNameType,
    LambdaFunctionRecommendationFindingReasonCodeType,
    LambdaFunctionRecommendationFindingType,
    MetricNameType,
    MetricStatisticType,
    PlatformDifferenceType,
    RecommendationSourceTypeType,
    ResourceTypeType,
    StatusType,
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
    "AutoScalingGroupConfigurationTypeDef",
    "AutoScalingGroupRecommendationOptionTypeDef",
    "AutoScalingGroupRecommendationTypeDef",
    "DescribeRecommendationExportJobsRequestTypeDef",
    "DescribeRecommendationExportJobsResponseResponseTypeDef",
    "EBSFilterTypeDef",
    "EBSUtilizationMetricTypeDef",
    "ExportAutoScalingGroupRecommendationsRequestTypeDef",
    "ExportAutoScalingGroupRecommendationsResponseResponseTypeDef",
    "ExportDestinationTypeDef",
    "ExportEBSVolumeRecommendationsRequestTypeDef",
    "ExportEBSVolumeRecommendationsResponseResponseTypeDef",
    "ExportEC2InstanceRecommendationsRequestTypeDef",
    "ExportEC2InstanceRecommendationsResponseResponseTypeDef",
    "ExportLambdaFunctionRecommendationsRequestTypeDef",
    "ExportLambdaFunctionRecommendationsResponseResponseTypeDef",
    "FilterTypeDef",
    "GetAutoScalingGroupRecommendationsRequestTypeDef",
    "GetAutoScalingGroupRecommendationsResponseResponseTypeDef",
    "GetEBSVolumeRecommendationsRequestTypeDef",
    "GetEBSVolumeRecommendationsResponseResponseTypeDef",
    "GetEC2InstanceRecommendationsRequestTypeDef",
    "GetEC2InstanceRecommendationsResponseResponseTypeDef",
    "GetEC2RecommendationProjectedMetricsRequestTypeDef",
    "GetEC2RecommendationProjectedMetricsResponseResponseTypeDef",
    "GetEnrollmentStatusResponseResponseTypeDef",
    "GetLambdaFunctionRecommendationsRequestTypeDef",
    "GetLambdaFunctionRecommendationsResponseResponseTypeDef",
    "GetRecommendationErrorTypeDef",
    "GetRecommendationSummariesRequestTypeDef",
    "GetRecommendationSummariesResponseResponseTypeDef",
    "InstanceRecommendationOptionTypeDef",
    "InstanceRecommendationTypeDef",
    "JobFilterTypeDef",
    "LambdaFunctionMemoryProjectedMetricTypeDef",
    "LambdaFunctionMemoryRecommendationOptionTypeDef",
    "LambdaFunctionRecommendationFilterTypeDef",
    "LambdaFunctionRecommendationTypeDef",
    "LambdaFunctionUtilizationMetricTypeDef",
    "ProjectedMetricTypeDef",
    "ReasonCodeSummaryTypeDef",
    "RecommendationExportJobTypeDef",
    "RecommendationSourceTypeDef",
    "RecommendationSummaryTypeDef",
    "RecommendedOptionProjectedMetricTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationConfigTypeDef",
    "S3DestinationTypeDef",
    "SummaryTypeDef",
    "UpdateEnrollmentStatusRequestTypeDef",
    "UpdateEnrollmentStatusResponseResponseTypeDef",
    "UtilizationMetricTypeDef",
    "VolumeConfigurationTypeDef",
    "VolumeRecommendationOptionTypeDef",
    "VolumeRecommendationTypeDef",
)

AutoScalingGroupConfigurationTypeDef = TypedDict(
    "AutoScalingGroupConfigurationTypeDef",
    {
        "desiredCapacity": int,
        "minSize": int,
        "maxSize": int,
        "instanceType": str,
    },
    total=False,
)

AutoScalingGroupRecommendationOptionTypeDef = TypedDict(
    "AutoScalingGroupRecommendationOptionTypeDef",
    {
        "configuration": "AutoScalingGroupConfigurationTypeDef",
        "projectedUtilizationMetrics": List["UtilizationMetricTypeDef"],
        "performanceRisk": float,
        "rank": int,
    },
    total=False,
)

AutoScalingGroupRecommendationTypeDef = TypedDict(
    "AutoScalingGroupRecommendationTypeDef",
    {
        "accountId": str,
        "autoScalingGroupArn": str,
        "autoScalingGroupName": str,
        "finding": FindingType,
        "utilizationMetrics": List["UtilizationMetricTypeDef"],
        "lookBackPeriodInDays": float,
        "currentConfiguration": "AutoScalingGroupConfigurationTypeDef",
        "recommendationOptions": List["AutoScalingGroupRecommendationOptionTypeDef"],
        "lastRefreshTimestamp": datetime,
    },
    total=False,
)

DescribeRecommendationExportJobsRequestTypeDef = TypedDict(
    "DescribeRecommendationExportJobsRequestTypeDef",
    {
        "jobIds": List[str],
        "filters": List["JobFilterTypeDef"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

DescribeRecommendationExportJobsResponseResponseTypeDef = TypedDict(
    "DescribeRecommendationExportJobsResponseResponseTypeDef",
    {
        "recommendationExportJobs": List["RecommendationExportJobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EBSFilterTypeDef = TypedDict(
    "EBSFilterTypeDef",
    {
        "name": Literal["Finding"],
        "values": List[str],
    },
    total=False,
)

EBSUtilizationMetricTypeDef = TypedDict(
    "EBSUtilizationMetricTypeDef",
    {
        "name": EBSMetricNameType,
        "statistic": MetricStatisticType,
        "value": float,
    },
    total=False,
)

_RequiredExportAutoScalingGroupRecommendationsRequestTypeDef = TypedDict(
    "_RequiredExportAutoScalingGroupRecommendationsRequestTypeDef",
    {
        "s3DestinationConfig": "S3DestinationConfigTypeDef",
    },
)
_OptionalExportAutoScalingGroupRecommendationsRequestTypeDef = TypedDict(
    "_OptionalExportAutoScalingGroupRecommendationsRequestTypeDef",
    {
        "accountIds": List[str],
        "filters": List["FilterTypeDef"],
        "fieldsToExport": List[ExportableAutoScalingGroupFieldType],
        "fileFormat": Literal["Csv"],
        "includeMemberAccounts": bool,
    },
    total=False,
)


class ExportAutoScalingGroupRecommendationsRequestTypeDef(
    _RequiredExportAutoScalingGroupRecommendationsRequestTypeDef,
    _OptionalExportAutoScalingGroupRecommendationsRequestTypeDef,
):
    pass


ExportAutoScalingGroupRecommendationsResponseResponseTypeDef = TypedDict(
    "ExportAutoScalingGroupRecommendationsResponseResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": "S3DestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportDestinationTypeDef = TypedDict(
    "ExportDestinationTypeDef",
    {
        "s3": "S3DestinationTypeDef",
    },
    total=False,
)

_RequiredExportEBSVolumeRecommendationsRequestTypeDef = TypedDict(
    "_RequiredExportEBSVolumeRecommendationsRequestTypeDef",
    {
        "s3DestinationConfig": "S3DestinationConfigTypeDef",
    },
)
_OptionalExportEBSVolumeRecommendationsRequestTypeDef = TypedDict(
    "_OptionalExportEBSVolumeRecommendationsRequestTypeDef",
    {
        "accountIds": List[str],
        "filters": List["EBSFilterTypeDef"],
        "fieldsToExport": List[ExportableVolumeFieldType],
        "fileFormat": Literal["Csv"],
        "includeMemberAccounts": bool,
    },
    total=False,
)


class ExportEBSVolumeRecommendationsRequestTypeDef(
    _RequiredExportEBSVolumeRecommendationsRequestTypeDef,
    _OptionalExportEBSVolumeRecommendationsRequestTypeDef,
):
    pass


ExportEBSVolumeRecommendationsResponseResponseTypeDef = TypedDict(
    "ExportEBSVolumeRecommendationsResponseResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": "S3DestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportEC2InstanceRecommendationsRequestTypeDef = TypedDict(
    "_RequiredExportEC2InstanceRecommendationsRequestTypeDef",
    {
        "s3DestinationConfig": "S3DestinationConfigTypeDef",
    },
)
_OptionalExportEC2InstanceRecommendationsRequestTypeDef = TypedDict(
    "_OptionalExportEC2InstanceRecommendationsRequestTypeDef",
    {
        "accountIds": List[str],
        "filters": List["FilterTypeDef"],
        "fieldsToExport": List[ExportableInstanceFieldType],
        "fileFormat": Literal["Csv"],
        "includeMemberAccounts": bool,
    },
    total=False,
)


class ExportEC2InstanceRecommendationsRequestTypeDef(
    _RequiredExportEC2InstanceRecommendationsRequestTypeDef,
    _OptionalExportEC2InstanceRecommendationsRequestTypeDef,
):
    pass


ExportEC2InstanceRecommendationsResponseResponseTypeDef = TypedDict(
    "ExportEC2InstanceRecommendationsResponseResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": "S3DestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportLambdaFunctionRecommendationsRequestTypeDef = TypedDict(
    "_RequiredExportLambdaFunctionRecommendationsRequestTypeDef",
    {
        "s3DestinationConfig": "S3DestinationConfigTypeDef",
    },
)
_OptionalExportLambdaFunctionRecommendationsRequestTypeDef = TypedDict(
    "_OptionalExportLambdaFunctionRecommendationsRequestTypeDef",
    {
        "accountIds": List[str],
        "filters": List["LambdaFunctionRecommendationFilterTypeDef"],
        "fieldsToExport": List[ExportableLambdaFunctionFieldType],
        "fileFormat": Literal["Csv"],
        "includeMemberAccounts": bool,
    },
    total=False,
)


class ExportLambdaFunctionRecommendationsRequestTypeDef(
    _RequiredExportLambdaFunctionRecommendationsRequestTypeDef,
    _OptionalExportLambdaFunctionRecommendationsRequestTypeDef,
):
    pass


ExportLambdaFunctionRecommendationsResponseResponseTypeDef = TypedDict(
    "ExportLambdaFunctionRecommendationsResponseResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": "S3DestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": FilterNameType,
        "values": List[str],
    },
    total=False,
)

GetAutoScalingGroupRecommendationsRequestTypeDef = TypedDict(
    "GetAutoScalingGroupRecommendationsRequestTypeDef",
    {
        "accountIds": List[str],
        "autoScalingGroupArns": List[str],
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
    },
    total=False,
)

GetAutoScalingGroupRecommendationsResponseResponseTypeDef = TypedDict(
    "GetAutoScalingGroupRecommendationsResponseResponseTypeDef",
    {
        "nextToken": str,
        "autoScalingGroupRecommendations": List["AutoScalingGroupRecommendationTypeDef"],
        "errors": List["GetRecommendationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEBSVolumeRecommendationsRequestTypeDef = TypedDict(
    "GetEBSVolumeRecommendationsRequestTypeDef",
    {
        "volumeArns": List[str],
        "nextToken": str,
        "maxResults": int,
        "filters": List["EBSFilterTypeDef"],
        "accountIds": List[str],
    },
    total=False,
)

GetEBSVolumeRecommendationsResponseResponseTypeDef = TypedDict(
    "GetEBSVolumeRecommendationsResponseResponseTypeDef",
    {
        "nextToken": str,
        "volumeRecommendations": List["VolumeRecommendationTypeDef"],
        "errors": List["GetRecommendationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEC2InstanceRecommendationsRequestTypeDef = TypedDict(
    "GetEC2InstanceRecommendationsRequestTypeDef",
    {
        "instanceArns": List[str],
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
        "accountIds": List[str],
    },
    total=False,
)

GetEC2InstanceRecommendationsResponseResponseTypeDef = TypedDict(
    "GetEC2InstanceRecommendationsResponseResponseTypeDef",
    {
        "nextToken": str,
        "instanceRecommendations": List["InstanceRecommendationTypeDef"],
        "errors": List["GetRecommendationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEC2RecommendationProjectedMetricsRequestTypeDef = TypedDict(
    "GetEC2RecommendationProjectedMetricsRequestTypeDef",
    {
        "instanceArn": str,
        "stat": MetricStatisticType,
        "period": int,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)

GetEC2RecommendationProjectedMetricsResponseResponseTypeDef = TypedDict(
    "GetEC2RecommendationProjectedMetricsResponseResponseTypeDef",
    {
        "recommendedOptionProjectedMetrics": List["RecommendedOptionProjectedMetricTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnrollmentStatusResponseResponseTypeDef = TypedDict(
    "GetEnrollmentStatusResponseResponseTypeDef",
    {
        "status": StatusType,
        "statusReason": str,
        "memberAccountsEnrolled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLambdaFunctionRecommendationsRequestTypeDef = TypedDict(
    "GetLambdaFunctionRecommendationsRequestTypeDef",
    {
        "functionArns": List[str],
        "accountIds": List[str],
        "filters": List["LambdaFunctionRecommendationFilterTypeDef"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetLambdaFunctionRecommendationsResponseResponseTypeDef = TypedDict(
    "GetLambdaFunctionRecommendationsResponseResponseTypeDef",
    {
        "nextToken": str,
        "lambdaFunctionRecommendations": List["LambdaFunctionRecommendationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommendationErrorTypeDef = TypedDict(
    "GetRecommendationErrorTypeDef",
    {
        "identifier": str,
        "code": str,
        "message": str,
    },
    total=False,
)

GetRecommendationSummariesRequestTypeDef = TypedDict(
    "GetRecommendationSummariesRequestTypeDef",
    {
        "accountIds": List[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetRecommendationSummariesResponseResponseTypeDef = TypedDict(
    "GetRecommendationSummariesResponseResponseTypeDef",
    {
        "nextToken": str,
        "recommendationSummaries": List["RecommendationSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceRecommendationOptionTypeDef = TypedDict(
    "InstanceRecommendationOptionTypeDef",
    {
        "instanceType": str,
        "projectedUtilizationMetrics": List["UtilizationMetricTypeDef"],
        "platformDifferences": List[PlatformDifferenceType],
        "performanceRisk": float,
        "rank": int,
    },
    total=False,
)

InstanceRecommendationTypeDef = TypedDict(
    "InstanceRecommendationTypeDef",
    {
        "instanceArn": str,
        "accountId": str,
        "instanceName": str,
        "currentInstanceType": str,
        "finding": FindingType,
        "findingReasonCodes": List[InstanceRecommendationFindingReasonCodeType],
        "utilizationMetrics": List["UtilizationMetricTypeDef"],
        "lookBackPeriodInDays": float,
        "recommendationOptions": List["InstanceRecommendationOptionTypeDef"],
        "recommendationSources": List["RecommendationSourceTypeDef"],
        "lastRefreshTimestamp": datetime,
    },
    total=False,
)

JobFilterTypeDef = TypedDict(
    "JobFilterTypeDef",
    {
        "name": JobFilterNameType,
        "values": List[str],
    },
    total=False,
)

LambdaFunctionMemoryProjectedMetricTypeDef = TypedDict(
    "LambdaFunctionMemoryProjectedMetricTypeDef",
    {
        "name": Literal["Duration"],
        "statistic": LambdaFunctionMemoryMetricStatisticType,
        "value": float,
    },
    total=False,
)

LambdaFunctionMemoryRecommendationOptionTypeDef = TypedDict(
    "LambdaFunctionMemoryRecommendationOptionTypeDef",
    {
        "rank": int,
        "memorySize": int,
        "projectedUtilizationMetrics": List["LambdaFunctionMemoryProjectedMetricTypeDef"],
    },
    total=False,
)

LambdaFunctionRecommendationFilterTypeDef = TypedDict(
    "LambdaFunctionRecommendationFilterTypeDef",
    {
        "name": LambdaFunctionRecommendationFilterNameType,
        "values": List[str],
    },
    total=False,
)

LambdaFunctionRecommendationTypeDef = TypedDict(
    "LambdaFunctionRecommendationTypeDef",
    {
        "functionArn": str,
        "functionVersion": str,
        "accountId": str,
        "currentMemorySize": int,
        "numberOfInvocations": int,
        "utilizationMetrics": List["LambdaFunctionUtilizationMetricTypeDef"],
        "lookbackPeriodInDays": float,
        "lastRefreshTimestamp": datetime,
        "finding": LambdaFunctionRecommendationFindingType,
        "findingReasonCodes": List[LambdaFunctionRecommendationFindingReasonCodeType],
        "memorySizeRecommendationOptions": List["LambdaFunctionMemoryRecommendationOptionTypeDef"],
    },
    total=False,
)

LambdaFunctionUtilizationMetricTypeDef = TypedDict(
    "LambdaFunctionUtilizationMetricTypeDef",
    {
        "name": LambdaFunctionMetricNameType,
        "statistic": LambdaFunctionMetricStatisticType,
        "value": float,
    },
    total=False,
)

ProjectedMetricTypeDef = TypedDict(
    "ProjectedMetricTypeDef",
    {
        "name": MetricNameType,
        "timestamps": List[datetime],
        "values": List[float],
    },
    total=False,
)

ReasonCodeSummaryTypeDef = TypedDict(
    "ReasonCodeSummaryTypeDef",
    {
        "name": FindingReasonCodeType,
        "value": float,
    },
    total=False,
)

RecommendationExportJobTypeDef = TypedDict(
    "RecommendationExportJobTypeDef",
    {
        "jobId": str,
        "destination": "ExportDestinationTypeDef",
        "resourceType": ResourceTypeType,
        "status": JobStatusType,
        "creationTimestamp": datetime,
        "lastUpdatedTimestamp": datetime,
        "failureReason": str,
    },
    total=False,
)

RecommendationSourceTypeDef = TypedDict(
    "RecommendationSourceTypeDef",
    {
        "recommendationSourceArn": str,
        "recommendationSourceType": RecommendationSourceTypeType,
    },
    total=False,
)

RecommendationSummaryTypeDef = TypedDict(
    "RecommendationSummaryTypeDef",
    {
        "summaries": List["SummaryTypeDef"],
        "recommendationResourceType": RecommendationSourceTypeType,
        "accountId": str,
    },
    total=False,
)

RecommendedOptionProjectedMetricTypeDef = TypedDict(
    "RecommendedOptionProjectedMetricTypeDef",
    {
        "recommendedInstanceType": str,
        "rank": int,
        "projectedMetrics": List["ProjectedMetricTypeDef"],
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

S3DestinationConfigTypeDef = TypedDict(
    "S3DestinationConfigTypeDef",
    {
        "bucket": str,
        "keyPrefix": str,
    },
    total=False,
)

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "bucket": str,
        "key": str,
        "metadataKey": str,
    },
    total=False,
)

SummaryTypeDef = TypedDict(
    "SummaryTypeDef",
    {
        "name": FindingType,
        "value": float,
        "reasonCodeSummaries": List["ReasonCodeSummaryTypeDef"],
    },
    total=False,
)

_RequiredUpdateEnrollmentStatusRequestTypeDef = TypedDict(
    "_RequiredUpdateEnrollmentStatusRequestTypeDef",
    {
        "status": StatusType,
    },
)
_OptionalUpdateEnrollmentStatusRequestTypeDef = TypedDict(
    "_OptionalUpdateEnrollmentStatusRequestTypeDef",
    {
        "includeMemberAccounts": bool,
    },
    total=False,
)


class UpdateEnrollmentStatusRequestTypeDef(
    _RequiredUpdateEnrollmentStatusRequestTypeDef, _OptionalUpdateEnrollmentStatusRequestTypeDef
):
    pass


UpdateEnrollmentStatusResponseResponseTypeDef = TypedDict(
    "UpdateEnrollmentStatusResponseResponseTypeDef",
    {
        "status": StatusType,
        "statusReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UtilizationMetricTypeDef = TypedDict(
    "UtilizationMetricTypeDef",
    {
        "name": MetricNameType,
        "statistic": MetricStatisticType,
        "value": float,
    },
    total=False,
)

VolumeConfigurationTypeDef = TypedDict(
    "VolumeConfigurationTypeDef",
    {
        "volumeType": str,
        "volumeSize": int,
        "volumeBaselineIOPS": int,
        "volumeBurstIOPS": int,
        "volumeBaselineThroughput": int,
        "volumeBurstThroughput": int,
    },
    total=False,
)

VolumeRecommendationOptionTypeDef = TypedDict(
    "VolumeRecommendationOptionTypeDef",
    {
        "configuration": "VolumeConfigurationTypeDef",
        "performanceRisk": float,
        "rank": int,
    },
    total=False,
)

VolumeRecommendationTypeDef = TypedDict(
    "VolumeRecommendationTypeDef",
    {
        "volumeArn": str,
        "accountId": str,
        "currentConfiguration": "VolumeConfigurationTypeDef",
        "finding": EBSFindingType,
        "utilizationMetrics": List["EBSUtilizationMetricTypeDef"],
        "lookBackPeriodInDays": float,
        "volumeRecommendationOptions": List["VolumeRecommendationOptionTypeDef"],
        "lastRefreshTimestamp": datetime,
    },
    total=False,
)
