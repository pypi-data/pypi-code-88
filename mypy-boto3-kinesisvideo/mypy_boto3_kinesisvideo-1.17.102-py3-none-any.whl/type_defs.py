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

from .literals import (
    APINameType,
    ChannelProtocolType,
    ChannelRoleType,
    StatusType,
    UpdateDataRetentionOperationType,
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
    "ChannelInfoTypeDef",
    "ChannelNameConditionTypeDef",
    "CreateSignalingChannelInputTypeDef",
    "CreateSignalingChannelOutputResponseTypeDef",
    "CreateStreamInputTypeDef",
    "CreateStreamOutputResponseTypeDef",
    "DeleteSignalingChannelInputTypeDef",
    "DeleteStreamInputTypeDef",
    "DescribeSignalingChannelInputTypeDef",
    "DescribeSignalingChannelOutputResponseTypeDef",
    "DescribeStreamInputTypeDef",
    "DescribeStreamOutputResponseTypeDef",
    "GetDataEndpointInputTypeDef",
    "GetDataEndpointOutputResponseTypeDef",
    "GetSignalingChannelEndpointInputTypeDef",
    "GetSignalingChannelEndpointOutputResponseTypeDef",
    "ListSignalingChannelsInputTypeDef",
    "ListSignalingChannelsOutputResponseTypeDef",
    "ListStreamsInputTypeDef",
    "ListStreamsOutputResponseTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputResponseTypeDef",
    "ListTagsForStreamInputTypeDef",
    "ListTagsForStreamOutputResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceEndpointListItemTypeDef",
    "ResponseMetadataTypeDef",
    "SingleMasterChannelEndpointConfigurationTypeDef",
    "SingleMasterConfigurationTypeDef",
    "StreamInfoTypeDef",
    "StreamNameConditionTypeDef",
    "TagResourceInputTypeDef",
    "TagStreamInputTypeDef",
    "TagTypeDef",
    "UntagResourceInputTypeDef",
    "UntagStreamInputTypeDef",
    "UpdateDataRetentionInputTypeDef",
    "UpdateSignalingChannelInputTypeDef",
    "UpdateStreamInputTypeDef",
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

_RequiredCreateSignalingChannelInputTypeDef = TypedDict(
    "_RequiredCreateSignalingChannelInputTypeDef",
    {
        "ChannelName": str,
    },
)
_OptionalCreateSignalingChannelInputTypeDef = TypedDict(
    "_OptionalCreateSignalingChannelInputTypeDef",
    {
        "ChannelType": Literal["SINGLE_MASTER"],
        "SingleMasterConfiguration": "SingleMasterConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateSignalingChannelInputTypeDef(
    _RequiredCreateSignalingChannelInputTypeDef, _OptionalCreateSignalingChannelInputTypeDef
):
    pass


CreateSignalingChannelOutputResponseTypeDef = TypedDict(
    "CreateSignalingChannelOutputResponseTypeDef",
    {
        "ChannelARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStreamInputTypeDef = TypedDict(
    "_RequiredCreateStreamInputTypeDef",
    {
        "StreamName": str,
    },
)
_OptionalCreateStreamInputTypeDef = TypedDict(
    "_OptionalCreateStreamInputTypeDef",
    {
        "DeviceName": str,
        "MediaType": str,
        "KmsKeyId": str,
        "DataRetentionInHours": int,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateStreamInputTypeDef(
    _RequiredCreateStreamInputTypeDef, _OptionalCreateStreamInputTypeDef
):
    pass


CreateStreamOutputResponseTypeDef = TypedDict(
    "CreateStreamOutputResponseTypeDef",
    {
        "StreamARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteSignalingChannelInputTypeDef = TypedDict(
    "_RequiredDeleteSignalingChannelInputTypeDef",
    {
        "ChannelARN": str,
    },
)
_OptionalDeleteSignalingChannelInputTypeDef = TypedDict(
    "_OptionalDeleteSignalingChannelInputTypeDef",
    {
        "CurrentVersion": str,
    },
    total=False,
)


class DeleteSignalingChannelInputTypeDef(
    _RequiredDeleteSignalingChannelInputTypeDef, _OptionalDeleteSignalingChannelInputTypeDef
):
    pass


_RequiredDeleteStreamInputTypeDef = TypedDict(
    "_RequiredDeleteStreamInputTypeDef",
    {
        "StreamARN": str,
    },
)
_OptionalDeleteStreamInputTypeDef = TypedDict(
    "_OptionalDeleteStreamInputTypeDef",
    {
        "CurrentVersion": str,
    },
    total=False,
)


class DeleteStreamInputTypeDef(
    _RequiredDeleteStreamInputTypeDef, _OptionalDeleteStreamInputTypeDef
):
    pass


DescribeSignalingChannelInputTypeDef = TypedDict(
    "DescribeSignalingChannelInputTypeDef",
    {
        "ChannelName": str,
        "ChannelARN": str,
    },
    total=False,
)

DescribeSignalingChannelOutputResponseTypeDef = TypedDict(
    "DescribeSignalingChannelOutputResponseTypeDef",
    {
        "ChannelInfo": "ChannelInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStreamInputTypeDef = TypedDict(
    "DescribeStreamInputTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

DescribeStreamOutputResponseTypeDef = TypedDict(
    "DescribeStreamOutputResponseTypeDef",
    {
        "StreamInfo": "StreamInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDataEndpointInputTypeDef = TypedDict(
    "_RequiredGetDataEndpointInputTypeDef",
    {
        "APIName": APINameType,
    },
)
_OptionalGetDataEndpointInputTypeDef = TypedDict(
    "_OptionalGetDataEndpointInputTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)


class GetDataEndpointInputTypeDef(
    _RequiredGetDataEndpointInputTypeDef, _OptionalGetDataEndpointInputTypeDef
):
    pass


GetDataEndpointOutputResponseTypeDef = TypedDict(
    "GetDataEndpointOutputResponseTypeDef",
    {
        "DataEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSignalingChannelEndpointInputTypeDef = TypedDict(
    "_RequiredGetSignalingChannelEndpointInputTypeDef",
    {
        "ChannelARN": str,
    },
)
_OptionalGetSignalingChannelEndpointInputTypeDef = TypedDict(
    "_OptionalGetSignalingChannelEndpointInputTypeDef",
    {
        "SingleMasterChannelEndpointConfiguration": "SingleMasterChannelEndpointConfigurationTypeDef",
    },
    total=False,
)


class GetSignalingChannelEndpointInputTypeDef(
    _RequiredGetSignalingChannelEndpointInputTypeDef,
    _OptionalGetSignalingChannelEndpointInputTypeDef,
):
    pass


GetSignalingChannelEndpointOutputResponseTypeDef = TypedDict(
    "GetSignalingChannelEndpointOutputResponseTypeDef",
    {
        "ResourceEndpointList": List["ResourceEndpointListItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSignalingChannelsInputTypeDef = TypedDict(
    "ListSignalingChannelsInputTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ChannelNameCondition": "ChannelNameConditionTypeDef",
    },
    total=False,
)

ListSignalingChannelsOutputResponseTypeDef = TypedDict(
    "ListSignalingChannelsOutputResponseTypeDef",
    {
        "ChannelInfoList": List["ChannelInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamsInputTypeDef = TypedDict(
    "ListStreamsInputTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "StreamNameCondition": "StreamNameConditionTypeDef",
    },
    total=False,
)

ListStreamsOutputResponseTypeDef = TypedDict(
    "ListStreamsOutputResponseTypeDef",
    {
        "StreamInfoList": List["StreamInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceInputTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalListTagsForResourceInputTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListTagsForResourceInputTypeDef(
    _RequiredListTagsForResourceInputTypeDef, _OptionalListTagsForResourceInputTypeDef
):
    pass


ListTagsForResourceOutputResponseTypeDef = TypedDict(
    "ListTagsForResourceOutputResponseTypeDef",
    {
        "NextToken": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForStreamInputTypeDef = TypedDict(
    "ListTagsForStreamInputTypeDef",
    {
        "NextToken": str,
        "StreamARN": str,
        "StreamName": str,
    },
    total=False,
)

ListTagsForStreamOutputResponseTypeDef = TypedDict(
    "ListTagsForStreamOutputResponseTypeDef",
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

TagResourceInputTypeDef = TypedDict(
    "TagResourceInputTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

_RequiredTagStreamInputTypeDef = TypedDict(
    "_RequiredTagStreamInputTypeDef",
    {
        "Tags": Dict[str, str],
    },
)
_OptionalTagStreamInputTypeDef = TypedDict(
    "_OptionalTagStreamInputTypeDef",
    {
        "StreamARN": str,
        "StreamName": str,
    },
    total=False,
)


class TagStreamInputTypeDef(_RequiredTagStreamInputTypeDef, _OptionalTagStreamInputTypeDef):
    pass


TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceInputTypeDef = TypedDict(
    "UntagResourceInputTypeDef",
    {
        "ResourceARN": str,
        "TagKeyList": List[str],
    },
)

_RequiredUntagStreamInputTypeDef = TypedDict(
    "_RequiredUntagStreamInputTypeDef",
    {
        "TagKeyList": List[str],
    },
)
_OptionalUntagStreamInputTypeDef = TypedDict(
    "_OptionalUntagStreamInputTypeDef",
    {
        "StreamARN": str,
        "StreamName": str,
    },
    total=False,
)


class UntagStreamInputTypeDef(_RequiredUntagStreamInputTypeDef, _OptionalUntagStreamInputTypeDef):
    pass


_RequiredUpdateDataRetentionInputTypeDef = TypedDict(
    "_RequiredUpdateDataRetentionInputTypeDef",
    {
        "CurrentVersion": str,
        "Operation": UpdateDataRetentionOperationType,
        "DataRetentionChangeInHours": int,
    },
)
_OptionalUpdateDataRetentionInputTypeDef = TypedDict(
    "_OptionalUpdateDataRetentionInputTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)


class UpdateDataRetentionInputTypeDef(
    _RequiredUpdateDataRetentionInputTypeDef, _OptionalUpdateDataRetentionInputTypeDef
):
    pass


_RequiredUpdateSignalingChannelInputTypeDef = TypedDict(
    "_RequiredUpdateSignalingChannelInputTypeDef",
    {
        "ChannelARN": str,
        "CurrentVersion": str,
    },
)
_OptionalUpdateSignalingChannelInputTypeDef = TypedDict(
    "_OptionalUpdateSignalingChannelInputTypeDef",
    {
        "SingleMasterConfiguration": "SingleMasterConfigurationTypeDef",
    },
    total=False,
)


class UpdateSignalingChannelInputTypeDef(
    _RequiredUpdateSignalingChannelInputTypeDef, _OptionalUpdateSignalingChannelInputTypeDef
):
    pass


_RequiredUpdateStreamInputTypeDef = TypedDict(
    "_RequiredUpdateStreamInputTypeDef",
    {
        "CurrentVersion": str,
    },
)
_OptionalUpdateStreamInputTypeDef = TypedDict(
    "_OptionalUpdateStreamInputTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "DeviceName": str,
        "MediaType": str,
    },
    total=False,
)


class UpdateStreamInputTypeDef(
    _RequiredUpdateStreamInputTypeDef, _OptionalUpdateStreamInputTypeDef
):
    pass
