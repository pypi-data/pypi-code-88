"""
Type annotations for sagemaker-featurestore-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sagemaker_featurestore_runtime.type_defs import BatchGetRecordErrorTypeDef

    data: BatchGetRecordErrorTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchGetRecordErrorTypeDef",
    "BatchGetRecordIdentifierTypeDef",
    "BatchGetRecordRequestTypeDef",
    "BatchGetRecordResponseResponseTypeDef",
    "BatchGetRecordResultDetailTypeDef",
    "DeleteRecordRequestTypeDef",
    "FeatureValueTypeDef",
    "GetRecordRequestTypeDef",
    "GetRecordResponseResponseTypeDef",
    "PutRecordRequestTypeDef",
    "ResponseMetadataTypeDef",
)

BatchGetRecordErrorTypeDef = TypedDict(
    "BatchGetRecordErrorTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
)

_RequiredBatchGetRecordIdentifierTypeDef = TypedDict(
    "_RequiredBatchGetRecordIdentifierTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifiersValueAsString": List[str],
    },
)
_OptionalBatchGetRecordIdentifierTypeDef = TypedDict(
    "_OptionalBatchGetRecordIdentifierTypeDef",
    {
        "FeatureNames": List[str],
    },
    total=False,
)


class BatchGetRecordIdentifierTypeDef(
    _RequiredBatchGetRecordIdentifierTypeDef, _OptionalBatchGetRecordIdentifierTypeDef
):
    pass


BatchGetRecordRequestTypeDef = TypedDict(
    "BatchGetRecordRequestTypeDef",
    {
        "Identifiers": List["BatchGetRecordIdentifierTypeDef"],
    },
)

BatchGetRecordResponseResponseTypeDef = TypedDict(
    "BatchGetRecordResponseResponseTypeDef",
    {
        "Records": List["BatchGetRecordResultDetailTypeDef"],
        "Errors": List["BatchGetRecordErrorTypeDef"],
        "UnprocessedIdentifiers": List["BatchGetRecordIdentifierTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetRecordResultDetailTypeDef = TypedDict(
    "BatchGetRecordResultDetailTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
        "Record": List["FeatureValueTypeDef"],
    },
)

DeleteRecordRequestTypeDef = TypedDict(
    "DeleteRecordRequestTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
        "EventTime": str,
    },
)

FeatureValueTypeDef = TypedDict(
    "FeatureValueTypeDef",
    {
        "FeatureName": str,
        "ValueAsString": str,
    },
)

_RequiredGetRecordRequestTypeDef = TypedDict(
    "_RequiredGetRecordRequestTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
    },
)
_OptionalGetRecordRequestTypeDef = TypedDict(
    "_OptionalGetRecordRequestTypeDef",
    {
        "FeatureNames": List[str],
    },
    total=False,
)


class GetRecordRequestTypeDef(_RequiredGetRecordRequestTypeDef, _OptionalGetRecordRequestTypeDef):
    pass


GetRecordResponseResponseTypeDef = TypedDict(
    "GetRecordResponseResponseTypeDef",
    {
        "Record": List["FeatureValueTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRecordRequestTypeDef = TypedDict(
    "PutRecordRequestTypeDef",
    {
        "FeatureGroupName": str,
        "Record": List["FeatureValueTypeDef"],
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
