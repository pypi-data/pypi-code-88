"""
Type annotations for kinesis service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesis.type_defs import AddTagsToStreamInputTypeDef

    data: AddTagsToStreamInputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ConsumerStatusType,
    EncryptionTypeType,
    MetricsNameType,
    ShardFilterTypeType,
    ShardIteratorTypeType,
    StreamStatusType,
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
    "AddTagsToStreamInputTypeDef",
    "ChildShardTypeDef",
    "ConsumerDescriptionTypeDef",
    "ConsumerTypeDef",
    "CreateStreamInputTypeDef",
    "DecreaseStreamRetentionPeriodInputTypeDef",
    "DeleteStreamInputTypeDef",
    "DeregisterStreamConsumerInputTypeDef",
    "DescribeLimitsOutputResponseTypeDef",
    "DescribeStreamConsumerInputTypeDef",
    "DescribeStreamConsumerOutputResponseTypeDef",
    "DescribeStreamInputTypeDef",
    "DescribeStreamOutputResponseTypeDef",
    "DescribeStreamSummaryInputTypeDef",
    "DescribeStreamSummaryOutputResponseTypeDef",
    "DisableEnhancedMonitoringInputTypeDef",
    "EnableEnhancedMonitoringInputTypeDef",
    "EnhancedMetricsTypeDef",
    "EnhancedMonitoringOutputResponseTypeDef",
    "GetRecordsInputTypeDef",
    "GetRecordsOutputResponseTypeDef",
    "GetShardIteratorInputTypeDef",
    "GetShardIteratorOutputResponseTypeDef",
    "HashKeyRangeTypeDef",
    "IncreaseStreamRetentionPeriodInputTypeDef",
    "InternalFailureExceptionTypeDef",
    "KMSAccessDeniedExceptionTypeDef",
    "KMSDisabledExceptionTypeDef",
    "KMSInvalidStateExceptionTypeDef",
    "KMSNotFoundExceptionTypeDef",
    "KMSOptInRequiredTypeDef",
    "KMSThrottlingExceptionTypeDef",
    "ListShardsInputTypeDef",
    "ListShardsOutputResponseTypeDef",
    "ListStreamConsumersInputTypeDef",
    "ListStreamConsumersOutputResponseTypeDef",
    "ListStreamsInputTypeDef",
    "ListStreamsOutputResponseTypeDef",
    "ListTagsForStreamInputTypeDef",
    "ListTagsForStreamOutputResponseTypeDef",
    "MergeShardsInputTypeDef",
    "PaginatorConfigTypeDef",
    "PutRecordInputTypeDef",
    "PutRecordOutputResponseTypeDef",
    "PutRecordsInputTypeDef",
    "PutRecordsOutputResponseTypeDef",
    "PutRecordsRequestEntryTypeDef",
    "PutRecordsResultEntryTypeDef",
    "RecordTypeDef",
    "RegisterStreamConsumerInputTypeDef",
    "RegisterStreamConsumerOutputResponseTypeDef",
    "RemoveTagsFromStreamInputTypeDef",
    "ResourceInUseExceptionTypeDef",
    "ResourceNotFoundExceptionTypeDef",
    "ResponseMetadataTypeDef",
    "SequenceNumberRangeTypeDef",
    "ShardFilterTypeDef",
    "ShardTypeDef",
    "SplitShardInputTypeDef",
    "StartStreamEncryptionInputTypeDef",
    "StartingPositionTypeDef",
    "StopStreamEncryptionInputTypeDef",
    "StreamDescriptionSummaryTypeDef",
    "StreamDescriptionTypeDef",
    "SubscribeToShardEventStreamTypeDef",
    "SubscribeToShardEventTypeDef",
    "SubscribeToShardInputTypeDef",
    "SubscribeToShardOutputResponseTypeDef",
    "TagTypeDef",
    "UpdateShardCountInputTypeDef",
    "UpdateShardCountOutputResponseTypeDef",
    "WaiterConfigTypeDef",
)

AddTagsToStreamInputTypeDef = TypedDict(
    "AddTagsToStreamInputTypeDef",
    {
        "StreamName": str,
        "Tags": Dict[str, str],
    },
)

ChildShardTypeDef = TypedDict(
    "ChildShardTypeDef",
    {
        "ShardId": str,
        "ParentShards": List[str],
        "HashKeyRange": "HashKeyRangeTypeDef",
    },
)

ConsumerDescriptionTypeDef = TypedDict(
    "ConsumerDescriptionTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": ConsumerStatusType,
        "ConsumerCreationTimestamp": datetime,
        "StreamARN": str,
    },
)

ConsumerTypeDef = TypedDict(
    "ConsumerTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": ConsumerStatusType,
        "ConsumerCreationTimestamp": datetime,
    },
)

CreateStreamInputTypeDef = TypedDict(
    "CreateStreamInputTypeDef",
    {
        "StreamName": str,
        "ShardCount": int,
    },
)

DecreaseStreamRetentionPeriodInputTypeDef = TypedDict(
    "DecreaseStreamRetentionPeriodInputTypeDef",
    {
        "StreamName": str,
        "RetentionPeriodHours": int,
    },
)

_RequiredDeleteStreamInputTypeDef = TypedDict(
    "_RequiredDeleteStreamInputTypeDef",
    {
        "StreamName": str,
    },
)
_OptionalDeleteStreamInputTypeDef = TypedDict(
    "_OptionalDeleteStreamInputTypeDef",
    {
        "EnforceConsumerDeletion": bool,
    },
    total=False,
)


class DeleteStreamInputTypeDef(
    _RequiredDeleteStreamInputTypeDef, _OptionalDeleteStreamInputTypeDef
):
    pass


DeregisterStreamConsumerInputTypeDef = TypedDict(
    "DeregisterStreamConsumerInputTypeDef",
    {
        "StreamARN": str,
        "ConsumerName": str,
        "ConsumerARN": str,
    },
    total=False,
)

DescribeLimitsOutputResponseTypeDef = TypedDict(
    "DescribeLimitsOutputResponseTypeDef",
    {
        "ShardLimit": int,
        "OpenShardCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStreamConsumerInputTypeDef = TypedDict(
    "DescribeStreamConsumerInputTypeDef",
    {
        "StreamARN": str,
        "ConsumerName": str,
        "ConsumerARN": str,
    },
    total=False,
)

DescribeStreamConsumerOutputResponseTypeDef = TypedDict(
    "DescribeStreamConsumerOutputResponseTypeDef",
    {
        "ConsumerDescription": "ConsumerDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeStreamInputTypeDef = TypedDict(
    "_RequiredDescribeStreamInputTypeDef",
    {
        "StreamName": str,
    },
)
_OptionalDescribeStreamInputTypeDef = TypedDict(
    "_OptionalDescribeStreamInputTypeDef",
    {
        "Limit": int,
        "ExclusiveStartShardId": str,
    },
    total=False,
)


class DescribeStreamInputTypeDef(
    _RequiredDescribeStreamInputTypeDef, _OptionalDescribeStreamInputTypeDef
):
    pass


DescribeStreamOutputResponseTypeDef = TypedDict(
    "DescribeStreamOutputResponseTypeDef",
    {
        "StreamDescription": "StreamDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStreamSummaryInputTypeDef = TypedDict(
    "DescribeStreamSummaryInputTypeDef",
    {
        "StreamName": str,
    },
)

DescribeStreamSummaryOutputResponseTypeDef = TypedDict(
    "DescribeStreamSummaryOutputResponseTypeDef",
    {
        "StreamDescriptionSummary": "StreamDescriptionSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableEnhancedMonitoringInputTypeDef = TypedDict(
    "DisableEnhancedMonitoringInputTypeDef",
    {
        "StreamName": str,
        "ShardLevelMetrics": List[MetricsNameType],
    },
)

EnableEnhancedMonitoringInputTypeDef = TypedDict(
    "EnableEnhancedMonitoringInputTypeDef",
    {
        "StreamName": str,
        "ShardLevelMetrics": List[MetricsNameType],
    },
)

EnhancedMetricsTypeDef = TypedDict(
    "EnhancedMetricsTypeDef",
    {
        "ShardLevelMetrics": List[MetricsNameType],
    },
    total=False,
)

EnhancedMonitoringOutputResponseTypeDef = TypedDict(
    "EnhancedMonitoringOutputResponseTypeDef",
    {
        "StreamName": str,
        "CurrentShardLevelMetrics": List[MetricsNameType],
        "DesiredShardLevelMetrics": List[MetricsNameType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRecordsInputTypeDef = TypedDict(
    "_RequiredGetRecordsInputTypeDef",
    {
        "ShardIterator": str,
    },
)
_OptionalGetRecordsInputTypeDef = TypedDict(
    "_OptionalGetRecordsInputTypeDef",
    {
        "Limit": int,
    },
    total=False,
)


class GetRecordsInputTypeDef(_RequiredGetRecordsInputTypeDef, _OptionalGetRecordsInputTypeDef):
    pass


GetRecordsOutputResponseTypeDef = TypedDict(
    "GetRecordsOutputResponseTypeDef",
    {
        "Records": List["RecordTypeDef"],
        "NextShardIterator": str,
        "MillisBehindLatest": int,
        "ChildShards": List["ChildShardTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetShardIteratorInputTypeDef = TypedDict(
    "_RequiredGetShardIteratorInputTypeDef",
    {
        "StreamName": str,
        "ShardId": str,
        "ShardIteratorType": ShardIteratorTypeType,
    },
)
_OptionalGetShardIteratorInputTypeDef = TypedDict(
    "_OptionalGetShardIteratorInputTypeDef",
    {
        "StartingSequenceNumber": str,
        "Timestamp": Union[datetime, str],
    },
    total=False,
)


class GetShardIteratorInputTypeDef(
    _RequiredGetShardIteratorInputTypeDef, _OptionalGetShardIteratorInputTypeDef
):
    pass


GetShardIteratorOutputResponseTypeDef = TypedDict(
    "GetShardIteratorOutputResponseTypeDef",
    {
        "ShardIterator": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HashKeyRangeTypeDef = TypedDict(
    "HashKeyRangeTypeDef",
    {
        "StartingHashKey": str,
        "EndingHashKey": str,
    },
)

IncreaseStreamRetentionPeriodInputTypeDef = TypedDict(
    "IncreaseStreamRetentionPeriodInputTypeDef",
    {
        "StreamName": str,
        "RetentionPeriodHours": int,
    },
)

InternalFailureExceptionTypeDef = TypedDict(
    "InternalFailureExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

KMSAccessDeniedExceptionTypeDef = TypedDict(
    "KMSAccessDeniedExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

KMSDisabledExceptionTypeDef = TypedDict(
    "KMSDisabledExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

KMSInvalidStateExceptionTypeDef = TypedDict(
    "KMSInvalidStateExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

KMSNotFoundExceptionTypeDef = TypedDict(
    "KMSNotFoundExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

KMSOptInRequiredTypeDef = TypedDict(
    "KMSOptInRequiredTypeDef",
    {
        "message": str,
    },
    total=False,
)

KMSThrottlingExceptionTypeDef = TypedDict(
    "KMSThrottlingExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

ListShardsInputTypeDef = TypedDict(
    "ListShardsInputTypeDef",
    {
        "StreamName": str,
        "NextToken": str,
        "ExclusiveStartShardId": str,
        "MaxResults": int,
        "StreamCreationTimestamp": Union[datetime, str],
        "ShardFilter": "ShardFilterTypeDef",
    },
    total=False,
)

ListShardsOutputResponseTypeDef = TypedDict(
    "ListShardsOutputResponseTypeDef",
    {
        "Shards": List["ShardTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStreamConsumersInputTypeDef = TypedDict(
    "_RequiredListStreamConsumersInputTypeDef",
    {
        "StreamARN": str,
    },
)
_OptionalListStreamConsumersInputTypeDef = TypedDict(
    "_OptionalListStreamConsumersInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "StreamCreationTimestamp": Union[datetime, str],
    },
    total=False,
)


class ListStreamConsumersInputTypeDef(
    _RequiredListStreamConsumersInputTypeDef, _OptionalListStreamConsumersInputTypeDef
):
    pass


ListStreamConsumersOutputResponseTypeDef = TypedDict(
    "ListStreamConsumersOutputResponseTypeDef",
    {
        "Consumers": List["ConsumerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamsInputTypeDef = TypedDict(
    "ListStreamsInputTypeDef",
    {
        "Limit": int,
        "ExclusiveStartStreamName": str,
    },
    total=False,
)

ListStreamsOutputResponseTypeDef = TypedDict(
    "ListStreamsOutputResponseTypeDef",
    {
        "StreamNames": List[str],
        "HasMoreStreams": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForStreamInputTypeDef = TypedDict(
    "_RequiredListTagsForStreamInputTypeDef",
    {
        "StreamName": str,
    },
)
_OptionalListTagsForStreamInputTypeDef = TypedDict(
    "_OptionalListTagsForStreamInputTypeDef",
    {
        "ExclusiveStartTagKey": str,
        "Limit": int,
    },
    total=False,
)


class ListTagsForStreamInputTypeDef(
    _RequiredListTagsForStreamInputTypeDef, _OptionalListTagsForStreamInputTypeDef
):
    pass


ListTagsForStreamOutputResponseTypeDef = TypedDict(
    "ListTagsForStreamOutputResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "HasMoreTags": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MergeShardsInputTypeDef = TypedDict(
    "MergeShardsInputTypeDef",
    {
        "StreamName": str,
        "ShardToMerge": str,
        "AdjacentShardToMerge": str,
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

_RequiredPutRecordInputTypeDef = TypedDict(
    "_RequiredPutRecordInputTypeDef",
    {
        "StreamName": str,
        "Data": Union[bytes, IO[bytes], StreamingBody],
        "PartitionKey": str,
    },
)
_OptionalPutRecordInputTypeDef = TypedDict(
    "_OptionalPutRecordInputTypeDef",
    {
        "ExplicitHashKey": str,
        "SequenceNumberForOrdering": str,
    },
    total=False,
)


class PutRecordInputTypeDef(_RequiredPutRecordInputTypeDef, _OptionalPutRecordInputTypeDef):
    pass


PutRecordOutputResponseTypeDef = TypedDict(
    "PutRecordOutputResponseTypeDef",
    {
        "ShardId": str,
        "SequenceNumber": str,
        "EncryptionType": EncryptionTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRecordsInputTypeDef = TypedDict(
    "PutRecordsInputTypeDef",
    {
        "Records": List["PutRecordsRequestEntryTypeDef"],
        "StreamName": str,
    },
)

PutRecordsOutputResponseTypeDef = TypedDict(
    "PutRecordsOutputResponseTypeDef",
    {
        "FailedRecordCount": int,
        "Records": List["PutRecordsResultEntryTypeDef"],
        "EncryptionType": EncryptionTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutRecordsRequestEntryTypeDef = TypedDict(
    "_RequiredPutRecordsRequestEntryTypeDef",
    {
        "Data": Union[bytes, IO[bytes], StreamingBody],
        "PartitionKey": str,
    },
)
_OptionalPutRecordsRequestEntryTypeDef = TypedDict(
    "_OptionalPutRecordsRequestEntryTypeDef",
    {
        "ExplicitHashKey": str,
    },
    total=False,
)


class PutRecordsRequestEntryTypeDef(
    _RequiredPutRecordsRequestEntryTypeDef, _OptionalPutRecordsRequestEntryTypeDef
):
    pass


PutRecordsResultEntryTypeDef = TypedDict(
    "PutRecordsResultEntryTypeDef",
    {
        "SequenceNumber": str,
        "ShardId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredRecordTypeDef = TypedDict(
    "_RequiredRecordTypeDef",
    {
        "SequenceNumber": str,
        "Data": bytes,
        "PartitionKey": str,
    },
)
_OptionalRecordTypeDef = TypedDict(
    "_OptionalRecordTypeDef",
    {
        "ApproximateArrivalTimestamp": datetime,
        "EncryptionType": EncryptionTypeType,
    },
    total=False,
)


class RecordTypeDef(_RequiredRecordTypeDef, _OptionalRecordTypeDef):
    pass


RegisterStreamConsumerInputTypeDef = TypedDict(
    "RegisterStreamConsumerInputTypeDef",
    {
        "StreamARN": str,
        "ConsumerName": str,
    },
)

RegisterStreamConsumerOutputResponseTypeDef = TypedDict(
    "RegisterStreamConsumerOutputResponseTypeDef",
    {
        "Consumer": "ConsumerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsFromStreamInputTypeDef = TypedDict(
    "RemoveTagsFromStreamInputTypeDef",
    {
        "StreamName": str,
        "TagKeys": List[str],
    },
)

ResourceInUseExceptionTypeDef = TypedDict(
    "ResourceInUseExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

ResourceNotFoundExceptionTypeDef = TypedDict(
    "ResourceNotFoundExceptionTypeDef",
    {
        "message": str,
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

_RequiredSequenceNumberRangeTypeDef = TypedDict(
    "_RequiredSequenceNumberRangeTypeDef",
    {
        "StartingSequenceNumber": str,
    },
)
_OptionalSequenceNumberRangeTypeDef = TypedDict(
    "_OptionalSequenceNumberRangeTypeDef",
    {
        "EndingSequenceNumber": str,
    },
    total=False,
)


class SequenceNumberRangeTypeDef(
    _RequiredSequenceNumberRangeTypeDef, _OptionalSequenceNumberRangeTypeDef
):
    pass


_RequiredShardFilterTypeDef = TypedDict(
    "_RequiredShardFilterTypeDef",
    {
        "Type": ShardFilterTypeType,
    },
)
_OptionalShardFilterTypeDef = TypedDict(
    "_OptionalShardFilterTypeDef",
    {
        "ShardId": str,
        "Timestamp": Union[datetime, str],
    },
    total=False,
)


class ShardFilterTypeDef(_RequiredShardFilterTypeDef, _OptionalShardFilterTypeDef):
    pass


_RequiredShardTypeDef = TypedDict(
    "_RequiredShardTypeDef",
    {
        "ShardId": str,
        "HashKeyRange": "HashKeyRangeTypeDef",
        "SequenceNumberRange": "SequenceNumberRangeTypeDef",
    },
)
_OptionalShardTypeDef = TypedDict(
    "_OptionalShardTypeDef",
    {
        "ParentShardId": str,
        "AdjacentParentShardId": str,
    },
    total=False,
)


class ShardTypeDef(_RequiredShardTypeDef, _OptionalShardTypeDef):
    pass


SplitShardInputTypeDef = TypedDict(
    "SplitShardInputTypeDef",
    {
        "StreamName": str,
        "ShardToSplit": str,
        "NewStartingHashKey": str,
    },
)

StartStreamEncryptionInputTypeDef = TypedDict(
    "StartStreamEncryptionInputTypeDef",
    {
        "StreamName": str,
        "EncryptionType": EncryptionTypeType,
        "KeyId": str,
    },
)

_RequiredStartingPositionTypeDef = TypedDict(
    "_RequiredStartingPositionTypeDef",
    {
        "Type": ShardIteratorTypeType,
    },
)
_OptionalStartingPositionTypeDef = TypedDict(
    "_OptionalStartingPositionTypeDef",
    {
        "SequenceNumber": str,
        "Timestamp": Union[datetime, str],
    },
    total=False,
)


class StartingPositionTypeDef(_RequiredStartingPositionTypeDef, _OptionalStartingPositionTypeDef):
    pass


StopStreamEncryptionInputTypeDef = TypedDict(
    "StopStreamEncryptionInputTypeDef",
    {
        "StreamName": str,
        "EncryptionType": EncryptionTypeType,
        "KeyId": str,
    },
)

_RequiredStreamDescriptionSummaryTypeDef = TypedDict(
    "_RequiredStreamDescriptionSummaryTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": StreamStatusType,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List["EnhancedMetricsTypeDef"],
        "OpenShardCount": int,
    },
)
_OptionalStreamDescriptionSummaryTypeDef = TypedDict(
    "_OptionalStreamDescriptionSummaryTypeDef",
    {
        "EncryptionType": EncryptionTypeType,
        "KeyId": str,
        "ConsumerCount": int,
    },
    total=False,
)


class StreamDescriptionSummaryTypeDef(
    _RequiredStreamDescriptionSummaryTypeDef, _OptionalStreamDescriptionSummaryTypeDef
):
    pass


_RequiredStreamDescriptionTypeDef = TypedDict(
    "_RequiredStreamDescriptionTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": StreamStatusType,
        "Shards": List["ShardTypeDef"],
        "HasMoreShards": bool,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List["EnhancedMetricsTypeDef"],
    },
)
_OptionalStreamDescriptionTypeDef = TypedDict(
    "_OptionalStreamDescriptionTypeDef",
    {
        "EncryptionType": EncryptionTypeType,
        "KeyId": str,
    },
    total=False,
)


class StreamDescriptionTypeDef(
    _RequiredStreamDescriptionTypeDef, _OptionalStreamDescriptionTypeDef
):
    pass


_RequiredSubscribeToShardEventStreamTypeDef = TypedDict(
    "_RequiredSubscribeToShardEventStreamTypeDef",
    {
        "SubscribeToShardEvent": "SubscribeToShardEventTypeDef",
    },
)
_OptionalSubscribeToShardEventStreamTypeDef = TypedDict(
    "_OptionalSubscribeToShardEventStreamTypeDef",
    {
        "ResourceNotFoundException": "ResourceNotFoundExceptionTypeDef",
        "ResourceInUseException": "ResourceInUseExceptionTypeDef",
        "KMSDisabledException": "KMSDisabledExceptionTypeDef",
        "KMSInvalidStateException": "KMSInvalidStateExceptionTypeDef",
        "KMSAccessDeniedException": "KMSAccessDeniedExceptionTypeDef",
        "KMSNotFoundException": "KMSNotFoundExceptionTypeDef",
        "KMSOptInRequired": "KMSOptInRequiredTypeDef",
        "KMSThrottlingException": "KMSThrottlingExceptionTypeDef",
        "InternalFailureException": "InternalFailureExceptionTypeDef",
    },
    total=False,
)


class SubscribeToShardEventStreamTypeDef(
    _RequiredSubscribeToShardEventStreamTypeDef, _OptionalSubscribeToShardEventStreamTypeDef
):
    pass


_RequiredSubscribeToShardEventTypeDef = TypedDict(
    "_RequiredSubscribeToShardEventTypeDef",
    {
        "Records": List["RecordTypeDef"],
        "ContinuationSequenceNumber": str,
        "MillisBehindLatest": int,
    },
)
_OptionalSubscribeToShardEventTypeDef = TypedDict(
    "_OptionalSubscribeToShardEventTypeDef",
    {
        "ChildShards": List["ChildShardTypeDef"],
    },
    total=False,
)


class SubscribeToShardEventTypeDef(
    _RequiredSubscribeToShardEventTypeDef, _OptionalSubscribeToShardEventTypeDef
):
    pass


SubscribeToShardInputTypeDef = TypedDict(
    "SubscribeToShardInputTypeDef",
    {
        "ConsumerARN": str,
        "ShardId": str,
        "StartingPosition": "StartingPositionTypeDef",
    },
)

SubscribeToShardOutputResponseTypeDef = TypedDict(
    "SubscribeToShardOutputResponseTypeDef",
    {
        "EventStream": "SubscribeToShardEventStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "Value": str,
    },
    total=False,
)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


UpdateShardCountInputTypeDef = TypedDict(
    "UpdateShardCountInputTypeDef",
    {
        "StreamName": str,
        "TargetShardCount": int,
        "ScalingType": Literal["UNIFORM_SCALING"],
    },
)

UpdateShardCountOutputResponseTypeDef = TypedDict(
    "UpdateShardCountOutputResponseTypeDef",
    {
        "StreamName": str,
        "CurrentShardCount": int,
        "TargetShardCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
