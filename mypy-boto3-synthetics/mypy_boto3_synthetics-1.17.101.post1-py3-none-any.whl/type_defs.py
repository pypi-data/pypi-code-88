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

from botocore.response import StreamingBody

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
    "CreateCanaryRequestTypeDef",
    "CreateCanaryResponseResponseTypeDef",
    "DeleteCanaryRequestTypeDef",
    "DescribeCanariesLastRunRequestTypeDef",
    "DescribeCanariesLastRunResponseResponseTypeDef",
    "DescribeCanariesRequestTypeDef",
    "DescribeCanariesResponseResponseTypeDef",
    "DescribeRuntimeVersionsRequestTypeDef",
    "DescribeRuntimeVersionsResponseResponseTypeDef",
    "GetCanaryRequestTypeDef",
    "GetCanaryResponseResponseTypeDef",
    "GetCanaryRunsRequestTypeDef",
    "GetCanaryRunsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RuntimeVersionTypeDef",
    "StartCanaryRequestTypeDef",
    "StopCanaryRequestTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateCanaryRequestTypeDef",
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
        "ZipFile": Union[bytes, IO[bytes], StreamingBody],
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
    },
    total=False,
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
    },
    total=False,
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
    },
    total=False,
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

_RequiredCreateCanaryRequestTypeDef = TypedDict(
    "_RequiredCreateCanaryRequestTypeDef",
    {
        "Name": str,
        "Code": "CanaryCodeInputTypeDef",
        "ArtifactS3Location": str,
        "ExecutionRoleArn": str,
        "Schedule": "CanaryScheduleInputTypeDef",
        "RuntimeVersion": str,
    },
)
_OptionalCreateCanaryRequestTypeDef = TypedDict(
    "_OptionalCreateCanaryRequestTypeDef",
    {
        "RunConfig": "CanaryRunConfigInputTypeDef",
        "SuccessRetentionPeriodInDays": int,
        "FailureRetentionPeriodInDays": int,
        "VpcConfig": "VpcConfigInputTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateCanaryRequestTypeDef(
    _RequiredCreateCanaryRequestTypeDef, _OptionalCreateCanaryRequestTypeDef
):
    pass


CreateCanaryResponseResponseTypeDef = TypedDict(
    "CreateCanaryResponseResponseTypeDef",
    {
        "Canary": "CanaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCanaryRequestTypeDef = TypedDict(
    "DeleteCanaryRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeCanariesLastRunRequestTypeDef = TypedDict(
    "DescribeCanariesLastRunRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeCanariesLastRunResponseResponseTypeDef = TypedDict(
    "DescribeCanariesLastRunResponseResponseTypeDef",
    {
        "CanariesLastRun": List["CanaryLastRunTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCanariesRequestTypeDef = TypedDict(
    "DescribeCanariesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeCanariesResponseResponseTypeDef = TypedDict(
    "DescribeCanariesResponseResponseTypeDef",
    {
        "Canaries": List["CanaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRuntimeVersionsRequestTypeDef = TypedDict(
    "DescribeRuntimeVersionsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeRuntimeVersionsResponseResponseTypeDef = TypedDict(
    "DescribeRuntimeVersionsResponseResponseTypeDef",
    {
        "RuntimeVersions": List["RuntimeVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCanaryRequestTypeDef = TypedDict(
    "GetCanaryRequestTypeDef",
    {
        "Name": str,
    },
)

GetCanaryResponseResponseTypeDef = TypedDict(
    "GetCanaryResponseResponseTypeDef",
    {
        "Canary": "CanaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCanaryRunsRequestTypeDef = TypedDict(
    "_RequiredGetCanaryRunsRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetCanaryRunsRequestTypeDef = TypedDict(
    "_OptionalGetCanaryRunsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetCanaryRunsRequestTypeDef(
    _RequiredGetCanaryRunsRequestTypeDef, _OptionalGetCanaryRunsRequestTypeDef
):
    pass


GetCanaryRunsResponseResponseTypeDef = TypedDict(
    "GetCanaryRunsResponseResponseTypeDef",
    {
        "CanaryRuns": List["CanaryRunTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

StartCanaryRequestTypeDef = TypedDict(
    "StartCanaryRequestTypeDef",
    {
        "Name": str,
    },
)

StopCanaryRequestTypeDef = TypedDict(
    "StopCanaryRequestTypeDef",
    {
        "Name": str,
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateCanaryRequestTypeDef = TypedDict(
    "_RequiredUpdateCanaryRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateCanaryRequestTypeDef = TypedDict(
    "_OptionalUpdateCanaryRequestTypeDef",
    {
        "Code": "CanaryCodeInputTypeDef",
        "ExecutionRoleArn": str,
        "RuntimeVersion": str,
        "Schedule": "CanaryScheduleInputTypeDef",
        "RunConfig": "CanaryRunConfigInputTypeDef",
        "SuccessRetentionPeriodInDays": int,
        "FailureRetentionPeriodInDays": int,
        "VpcConfig": "VpcConfigInputTypeDef",
    },
    total=False,
)


class UpdateCanaryRequestTypeDef(
    _RequiredUpdateCanaryRequestTypeDef, _OptionalUpdateCanaryRequestTypeDef
):
    pass


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
    },
    total=False,
)
