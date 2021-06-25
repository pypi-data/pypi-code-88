"""
Type annotations for iot-jobs-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iot_jobs_data.type_defs import DescribeJobExecutionResponseTypeDef

    data: DescribeJobExecutionResponseTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from .literals import JobExecutionStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DescribeJobExecutionResponseTypeDef",
    "GetPendingJobExecutionsResponseTypeDef",
    "JobExecutionStateTypeDef",
    "JobExecutionSummaryTypeDef",
    "JobExecutionTypeDef",
    "StartNextPendingJobExecutionResponseTypeDef",
    "UpdateJobExecutionResponseTypeDef",
)

DescribeJobExecutionResponseTypeDef = TypedDict(
    "DescribeJobExecutionResponseTypeDef",
    {
        "execution": "JobExecutionTypeDef",
    },
    total=False,
)

GetPendingJobExecutionsResponseTypeDef = TypedDict(
    "GetPendingJobExecutionsResponseTypeDef",
    {
        "inProgressJobs": List["JobExecutionSummaryTypeDef"],
        "queuedJobs": List["JobExecutionSummaryTypeDef"],
    },
    total=False,
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

StartNextPendingJobExecutionResponseTypeDef = TypedDict(
    "StartNextPendingJobExecutionResponseTypeDef",
    {
        "execution": "JobExecutionTypeDef",
    },
    total=False,
)

UpdateJobExecutionResponseTypeDef = TypedDict(
    "UpdateJobExecutionResponseTypeDef",
    {
        "executionState": "JobExecutionStateTypeDef",
        "jobDocument": str,
    },
    total=False,
)
