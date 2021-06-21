"""
Type annotations for synthetics service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/type_defs.html)

Usage::

    ```python
    from mypy_boto3_synthetics.type_defs import CanaryCodeInputTypeDef

    data: CanaryCodeInputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from .literals import CanaryRunStateReasonCodeType, CanaryRunStateType, CanaryStateType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CanaryCodeInputTypeDef",
    "CanaryCodeOutputTypeDef",
    "CanaryLastRunTypeDef",
    "CanaryRunConfigInputTypeDef",
    "CanaryRunConfigOutputTypeDef",
    "CanaryRunStatusTypeDef",
    "CanaryRunTimelineTypeDef",
    "CanaryRunTypeDef",
    "CanaryScheduleInputTypeDef",
    "CanaryScheduleOutputTypeDef",
    "CanaryStatusTypeDef",
    "CanaryTimelineTypeDef",
    "CanaryTypeDef",
    "CreateCanaryResponseTypeDef",
    "DescribeCanariesLastRunResponseTypeDef",
    "DescribeCanariesResponseTypeDef",
    "DescribeRuntimeVersionsResponseTypeDef",
    "GetCanaryResponseTypeDef",
    "GetCanaryRunsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RuntimeVersionTypeDef",
    "VpcConfigInputTypeDef",
    "VpcConfigOutputTypeDef",
)

_RequiredCanaryCodeInputTypeDef = TypedDict(
    "_RequiredCanaryCodeInputTypeDef",
    {
        "Handler": str,
    },
)
_OptionalCanaryCodeInputTypeDef = TypedDict(
    "_OptionalCanaryCodeInputTypeDef",
    {
        "S3Bucket": str,
        "S3Key": str,
        "S3Version": str,
        "ZipFile": Union[bytes, IO[bytes]],
    },
    total=False,
)


class CanaryCodeInputTypeDef(_RequiredCanaryCodeInputTypeDef, _OptionalCanaryCodeInputTypeDef):
    pass


CanaryCodeOutputTypeDef = TypedDict(
    "CanaryCodeOutputTypeDef",
    {
        "SourceLocationArn": str,
        "Handler": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CanaryLastRunTypeDef = TypedDict(
    "CanaryLastRunTypeDef",
    {
        "CanaryName": str,
        "LastRun": "CanaryRunTypeDef",
    },
    total=False,
)

CanaryRunConfigInputTypeDef = TypedDict(
    "CanaryRunConfigInputTypeDef",
    {
        "TimeoutInSeconds": int,
        "MemoryInMB": int,
        "ActiveTracing": bool,
        "EnvironmentVariables": Dict[str, str],
    },
    total=False,
)

CanaryRunConfigOutputTypeDef = TypedDict(
    "CanaryRunConfigOutputTypeDef",
    {
        "TimeoutInSeconds": int,
        "MemoryInMB": int,
        "ActiveTracing": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CanaryRunStatusTypeDef = TypedDict(
    "CanaryRunStatusTypeDef",
    {
        "State": CanaryRunStateType,
        "StateReason": str,
        "StateReasonCode": CanaryRunStateReasonCodeType,
    },
    total=False,
)

CanaryRunTimelineTypeDef = TypedDict(
    "CanaryRunTimelineTypeDef",
    {
        "Started": datetime,
        "Completed": datetime,
    },
    total=False,
)

CanaryRunTypeDef = TypedDict(
    "CanaryRunTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": "CanaryRunStatusTypeDef",
        "Timeline": "CanaryRunTimelineTypeDef",
        "ArtifactS3Location": str,
    },
    total=False,
)

_RequiredCanaryScheduleInputTypeDef = TypedDict(
    "_RequiredCanaryScheduleInputTypeDef",
    {
        "Expression": str,
    },
)
_OptionalCanaryScheduleInputTypeDef = TypedDict(
    "_OptionalCanaryScheduleInputTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)


class CanaryScheduleInputTypeDef(
    _RequiredCanaryScheduleInputTypeDef, _OptionalCanaryScheduleInputTypeDef
):
    pass


CanaryScheduleOutputTypeDef = TypedDict(
    "CanaryScheduleOutputTypeDef",
    {
        "Expression": str,
        "DurationInSeconds": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CanaryStatusTypeDef = TypedDict(
    "CanaryStatusTypeDef",
    {
        "State": CanaryStateType,
        "StateReason": str,
        "StateReasonCode": Literal["INVALID_PERMISSIONS"],
    },
    total=False,
)

CanaryTimelineTypeDef = TypedDict(
    "CanaryTimelineTypeDef",
    {
        "Created": datetime,
        "LastModified": datetime,
        "LastStarted": datetime,
        "LastStopped": datetime,
    },
    total=False,
)

CanaryTypeDef = TypedDict(
    "CanaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Code": "CanaryCodeOutputTypeDef",
        "ExecutionRoleArn": str,
        "Schedule": "CanaryScheduleOutputTypeDef",
        "RunConfig": "CanaryRunConfigOutputTypeDef",
        "SuccessRetentionPeriodInDays": int,
        "FailureRetentionPeriodInDays": int,
        "Status": "CanaryStatusTypeDef",
        "Timeline": "CanaryTimelineTypeDef",
        "ArtifactS3Location": str,
        "EngineArn": str,
        "RuntimeVersion": str,
        "VpcConfig": "VpcConfigOutputTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

CreateCanaryResponseTypeDef = TypedDict(
    "CreateCanaryResponseTypeDef",
    {
        "Canary": "CanaryTypeDef",
    },
    total=False,
)

DescribeCanariesLastRunResponseTypeDef = TypedDict(
    "DescribeCanariesLastRunResponseTypeDef",
    {
        "CanariesLastRun": List["CanaryLastRunTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeCanariesResponseTypeDef = TypedDict(
    "DescribeCanariesResponseTypeDef",
    {
        "Canaries": List["CanaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeRuntimeVersionsResponseTypeDef = TypedDict(
    "DescribeRuntimeVersionsResponseTypeDef",
    {
        "RuntimeVersions": List["RuntimeVersionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

GetCanaryResponseTypeDef = TypedDict(
    "GetCanaryResponseTypeDef",
    {
        "Canary": "CanaryTypeDef",
    },
    total=False,
)

GetCanaryRunsResponseTypeDef = TypedDict(
    "GetCanaryRunsResponseTypeDef",
    {
        "CanaryRuns": List["CanaryRunTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
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

RuntimeVersionTypeDef = TypedDict(
    "RuntimeVersionTypeDef",
    {
        "VersionName": str,
        "Description": str,
        "ReleaseDate": datetime,
        "DeprecationDate": datetime,
    },
    total=False,
)

VpcConfigInputTypeDef = TypedDict(
    "VpcConfigInputTypeDef",
    {
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)

VpcConfigOutputTypeDef = TypedDict(
    "VpcConfigOutputTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
