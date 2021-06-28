"""
Type annotations for iot-jobs-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iot_jobs_data.type_defs import DescribeJobExecutionRequestTypeDef

    data: DescribeJobExecutionRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import JobExecutionStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DescribeJobExecutionRequestTypeDef",
    "DescribeJobExecutionResponseResponseTypeDef",
    "GetPendingJobExecutionsRequestTypeDef",
    "GetPendingJobExecutionsResponseResponseTypeDef",
    "JobExecutionStateTypeDef",
    "JobExecutionSummaryTypeDef",
    "JobExecutionTypeDef",
    "ResponseMetadataTypeDef",
    "StartNextPendingJobExecutionRequestTypeDef",
    "StartNextPendingJobExecutionResponseResponseTypeDef",
    "UpdateJobExecutionRequestTypeDef",
    "UpdateJobExecutionResponseResponseTypeDef",
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
        "includeJobDocument": bool,
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

GetPendingJobExecutionsRequestTypeDef = TypedDict(
    "GetPendingJobExecutionsRequestTypeDef",
    {
        "thingName": str,
    },
)

GetPendingJobExecutionsResponseResponseTypeDef = TypedDict(
    "GetPendingJobExecutionsResponseResponseTypeDef",
    {
        "inProgressJobs": List["JobExecutionSummaryTypeDef"],
        "queuedJobs": List["JobExecutionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

JobExecutionStateTypeDef = TypedDict(
    "JobExecutionStateTypeDef",
    {
        "status": JobExecutionStatusType,
        "statusDetails": Dict[str, str],
        "versionNumber": int,
    },
    total=False,
)

JobExecutionSummaryTypeDef = TypedDict(
    "JobExecutionSummaryTypeDef",
    {
        "jobId": str,
        "queuedAt": int,
        "startedAt": int,
        "lastUpdatedAt": int,
        "versionNumber": int,
        "executionNumber": int,
    },
    total=False,
)

JobExecutionTypeDef = TypedDict(
    "JobExecutionTypeDef",
    {
        "jobId": str,
        "thingName": str,
        "status": JobExecutionStatusType,
        "statusDetails": Dict[str, str],
        "queuedAt": int,
        "startedAt": int,
        "lastUpdatedAt": int,
        "approximateSecondsBeforeTimedOut": int,
        "versionNumber": int,
        "executionNumber": int,
        "jobDocument": str,
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

_RequiredStartNextPendingJobExecutionRequestTypeDef = TypedDict(
    "_RequiredStartNextPendingJobExecutionRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalStartNextPendingJobExecutionRequestTypeDef = TypedDict(
    "_OptionalStartNextPendingJobExecutionRequestTypeDef",
    {
        "statusDetails": Dict[str, str],
        "stepTimeoutInMinutes": int,
    },
    total=False,
)


class StartNextPendingJobExecutionRequestTypeDef(
    _RequiredStartNextPendingJobExecutionRequestTypeDef,
    _OptionalStartNextPendingJobExecutionRequestTypeDef,
):
    pass


StartNextPendingJobExecutionResponseResponseTypeDef = TypedDict(
    "StartNextPendingJobExecutionResponseResponseTypeDef",
    {
        "execution": "JobExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateJobExecutionRequestTypeDef = TypedDict(
    "_RequiredUpdateJobExecutionRequestTypeDef",
    {
        "jobId": str,
        "thingName": str,
        "status": JobExecutionStatusType,
    },
)
_OptionalUpdateJobExecutionRequestTypeDef = TypedDict(
    "_OptionalUpdateJobExecutionRequestTypeDef",
    {
        "statusDetails": Dict[str, str],
        "stepTimeoutInMinutes": int,
        "expectedVersion": int,
        "includeJobExecutionState": bool,
        "includeJobDocument": bool,
        "executionNumber": int,
    },
    total=False,
)


class UpdateJobExecutionRequestTypeDef(
    _RequiredUpdateJobExecutionRequestTypeDef, _OptionalUpdateJobExecutionRequestTypeDef
):
    pass


UpdateJobExecutionResponseResponseTypeDef = TypedDict(
    "UpdateJobExecutionResponseResponseTypeDef",
    {
        "executionState": "JobExecutionStateTypeDef",
        "jobDocument": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
