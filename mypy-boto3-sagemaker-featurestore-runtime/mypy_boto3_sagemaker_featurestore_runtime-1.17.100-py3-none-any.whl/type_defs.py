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
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchGetRecordErrorTypeDef",
    "BatchGetRecordIdentifierTypeDef",
    "BatchGetRecordResponseTypeDef",
    "BatchGetRecordResultDetailTypeDef",
    "FeatureValueTypeDef",
    "GetRecordResponseTypeDef",
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


BatchGetRecordResponseTypeDef = TypedDict(
    "BatchGetRecordResponseTypeDef",
    {
        "Records": List["BatchGetRecordResultDetailTypeDef"],
        "Errors": List["BatchGetRecordErrorTypeDef"],
        "UnprocessedIdentifiers": List["BatchGetRecordIdentifierTypeDef"],
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

FeatureValueTypeDef = TypedDict(
    "FeatureValueTypeDef",
    {
        "FeatureName": str,
        "ValueAsString": str,
    },
)

GetRecordResponseTypeDef = TypedDict(
    "GetRecordResponseTypeDef",
    {
        "Record": List["FeatureValueTypeDef"],
    },
    total=False,
)
