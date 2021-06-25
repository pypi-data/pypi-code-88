"""
Type annotations for kinesisvideo service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesisvideo.type_defs import ChannelInfoTypeDef

    data: ChannelInfoTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import ChannelProtocolType, ChannelRoleType, StatusType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ChannelInfoTypeDef",
    "ChannelNameConditionTypeDef",
    "CreateSignalingChannelOutputTypeDef",
    "CreateStreamOutputTypeDef",
    "DescribeSignalingChannelOutputTypeDef",
    "DescribeStreamOutputTypeDef",
    "GetDataEndpointOutputTypeDef",
    "GetSignalingChannelEndpointOutputTypeDef",
    "ListSignalingChannelsOutputTypeDef",
    "ListStreamsOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTagsForStreamOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceEndpointListItemTypeDef",
    "ResponseMetadataTypeDef",
    "SingleMasterChannelEndpointConfigurationTypeDef",
    "SingleMasterConfigurationTypeDef",
    "StreamInfoTypeDef",
    "StreamNameConditionTypeDef",
    "TagTypeDef",
)

ChannelInfoTypeDef = TypedDict(
    "ChannelInfoTypeDef",
    {
        "ChannelName": str,
        "ChannelARN": str,
        "ChannelType": Literal["SINGLE_MASTER"],
        "ChannelStatus": StatusType,
        "CreationTime": datetime,
        "SingleMasterConfiguration": "SingleMasterConfigurationTypeDef",
        "Version": str,
    },
    total=False,
)

ChannelNameConditionTypeDef = TypedDict(
    "ChannelNameConditionTypeDef",
    {
        "ComparisonOperator": Literal["BEGINS_WITH"],
        "ComparisonValue": str,
    },
    total=False,
)

CreateSignalingChannelOutputTypeDef = TypedDict(
    "CreateSignalingChannelOutputTypeDef",
    {
        "ChannelARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStreamOutputTypeDef = TypedDict(
    "CreateStreamOutputTypeDef",
    {
        "StreamARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSignalingChannelOutputTypeDef = TypedDict(
    "DescribeSignalingChannelOutputTypeDef",
    {
        "ChannelInfo": "ChannelInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStreamOutputTypeDef = TypedDict(
    "DescribeStreamOutputTypeDef",
    {
        "StreamInfo": "StreamInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataEndpointOutputTypeDef = TypedDict(
    "GetDataEndpointOutputTypeDef",
    {
        "DataEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSignalingChannelEndpointOutputTypeDef = TypedDict(
    "GetSignalingChannelEndpointOutputTypeDef",
    {
        "ResourceEndpointList": List["ResourceEndpointListItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSignalingChannelsOutputTypeDef = TypedDict(
    "ListSignalingChannelsOutputTypeDef",
    {
        "ChannelInfoList": List["ChannelInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamsOutputTypeDef = TypedDict(
    "ListStreamsOutputTypeDef",
    {
        "StreamInfoList": List["StreamInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "NextToken": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForStreamOutputTypeDef = TypedDict(
    "ListTagsForStreamOutputTypeDef",
    {
        "NextToken": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

ResourceEndpointListItemTypeDef = TypedDict(
    "ResourceEndpointListItemTypeDef",
    {
        "Protocol": ChannelProtocolType,
        "ResourceEndpoint": str,
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

SingleMasterChannelEndpointConfigurationTypeDef = TypedDict(
    "SingleMasterChannelEndpointConfigurationTypeDef",
    {
        "Protocols": List[ChannelProtocolType],
        "Role": ChannelRoleType,
    },
    total=False,
)

SingleMasterConfigurationTypeDef = TypedDict(
    "SingleMasterConfigurationTypeDef",
    {
        "MessageTtlSeconds": int,
    },
    total=False,
)

StreamInfoTypeDef = TypedDict(
    "StreamInfoTypeDef",
    {
        "DeviceName": str,
        "StreamName": str,
        "StreamARN": str,
        "MediaType": str,
        "KmsKeyId": str,
        "Version": str,
        "Status": StatusType,
        "CreationTime": datetime,
        "DataRetentionInHours": int,
    },
    total=False,
)

StreamNameConditionTypeDef = TypedDict(
    "StreamNameConditionTypeDef",
    {
        "ComparisonOperator": Literal["BEGINS_WITH"],
        "ComparisonValue": str,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
