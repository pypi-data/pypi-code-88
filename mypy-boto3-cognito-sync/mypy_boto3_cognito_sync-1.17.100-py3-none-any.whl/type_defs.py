"""
Type annotations for cognito-sync service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cognito_sync.type_defs import BulkPublishResponseTypeDef

    data: BulkPublishResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from .literals import BulkPublishStatusType, OperationType, StreamingStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BulkPublishResponseTypeDef",
    "CognitoStreamsTypeDef",
    "DatasetTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeIdentityPoolUsageResponseTypeDef",
    "DescribeIdentityUsageResponseTypeDef",
    "GetBulkPublishDetailsResponseTypeDef",
    "GetCognitoEventsResponseTypeDef",
    "GetIdentityPoolConfigurationResponseTypeDef",
    "IdentityPoolUsageTypeDef",
    "IdentityUsageTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListIdentityPoolUsageResponseTypeDef",
    "ListRecordsResponseTypeDef",
    "PushSyncTypeDef",
    "RecordPatchTypeDef",
    "RecordTypeDef",
    "RegisterDeviceResponseTypeDef",
    "SetIdentityPoolConfigurationResponseTypeDef",
    "UpdateRecordsResponseTypeDef",
)

BulkPublishResponseTypeDef = TypedDict(
    "BulkPublishResponseTypeDef",
    {
        "IdentityPoolId": str,
    },
    total=False,
)

CognitoStreamsTypeDef = TypedDict(
    "CognitoStreamsTypeDef",
    {
        "StreamName": str,
        "RoleArn": str,
        "StreamingStatus": StreamingStatusType,
    },
    total=False,
)

DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "IdentityId": str,
        "DatasetName": str,
        "CreationDate": datetime,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "DataStorage": int,
        "NumRecords": int,
    },
    total=False,
)

DeleteDatasetResponseTypeDef = TypedDict(
    "DeleteDatasetResponseTypeDef",
    {
        "Dataset": "DatasetTypeDef",
    },
    total=False,
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "Dataset": "DatasetTypeDef",
    },
    total=False,
)

DescribeIdentityPoolUsageResponseTypeDef = TypedDict(
    "DescribeIdentityPoolUsageResponseTypeDef",
    {
        "IdentityPoolUsage": "IdentityPoolUsageTypeDef",
    },
    total=False,
)

DescribeIdentityUsageResponseTypeDef = TypedDict(
    "DescribeIdentityUsageResponseTypeDef",
    {
        "IdentityUsage": "IdentityUsageTypeDef",
    },
    total=False,
)

GetBulkPublishDetailsResponseTypeDef = TypedDict(
    "GetBulkPublishDetailsResponseTypeDef",
    {
        "IdentityPoolId": str,
        "BulkPublishStartTime": datetime,
        "BulkPublishCompleteTime": datetime,
        "BulkPublishStatus": BulkPublishStatusType,
        "FailureMessage": str,
    },
    total=False,
)

GetCognitoEventsResponseTypeDef = TypedDict(
    "GetCognitoEventsResponseTypeDef",
    {
        "Events": Dict[str, str],
    },
    total=False,
)

GetIdentityPoolConfigurationResponseTypeDef = TypedDict(
    "GetIdentityPoolConfigurationResponseTypeDef",
    {
        "IdentityPoolId": str,
        "PushSync": "PushSyncTypeDef",
        "CognitoStreams": "CognitoStreamsTypeDef",
    },
    total=False,
)

IdentityPoolUsageTypeDef = TypedDict(
    "IdentityPoolUsageTypeDef",
    {
        "IdentityPoolId": str,
        "SyncSessionsCount": int,
        "DataStorage": int,
        "LastModifiedDate": datetime,
    },
    total=False,
)

IdentityUsageTypeDef = TypedDict(
    "IdentityUsageTypeDef",
    {
        "IdentityId": str,
        "IdentityPoolId": str,
        "LastModifiedDate": datetime,
        "DatasetCount": int,
        "DataStorage": int,
    },
    total=False,
)

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "Datasets": List["DatasetTypeDef"],
        "Count": int,
        "NextToken": str,
    },
    total=False,
)

ListIdentityPoolUsageResponseTypeDef = TypedDict(
    "ListIdentityPoolUsageResponseTypeDef",
    {
        "IdentityPoolUsages": List["IdentityPoolUsageTypeDef"],
        "MaxResults": int,
        "Count": int,
        "NextToken": str,
    },
    total=False,
)

ListRecordsResponseTypeDef = TypedDict(
    "ListRecordsResponseTypeDef",
    {
        "Records": List["RecordTypeDef"],
        "NextToken": str,
        "Count": int,
        "DatasetSyncCount": int,
        "LastModifiedBy": str,
        "MergedDatasetNames": List[str],
        "DatasetExists": bool,
        "DatasetDeletedAfterRequestedSyncCount": bool,
        "SyncSessionToken": str,
    },
    total=False,
)

PushSyncTypeDef = TypedDict(
    "PushSyncTypeDef",
    {
        "ApplicationArns": List[str],
        "RoleArn": str,
    },
    total=False,
)

_RequiredRecordPatchTypeDef = TypedDict(
    "_RequiredRecordPatchTypeDef",
    {
        "Op": OperationType,
        "Key": str,
        "SyncCount": int,
    },
)
_OptionalRecordPatchTypeDef = TypedDict(
    "_OptionalRecordPatchTypeDef",
    {
        "Value": str,
        "DeviceLastModifiedDate": datetime,
    },
    total=False,
)


class RecordPatchTypeDef(_RequiredRecordPatchTypeDef, _OptionalRecordPatchTypeDef):
    pass


RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "Key": str,
        "Value": str,
        "SyncCount": int,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "DeviceLastModifiedDate": datetime,
    },
    total=False,
)

RegisterDeviceResponseTypeDef = TypedDict(
    "RegisterDeviceResponseTypeDef",
    {
        "DeviceId": str,
    },
    total=False,
)

SetIdentityPoolConfigurationResponseTypeDef = TypedDict(
    "SetIdentityPoolConfigurationResponseTypeDef",
    {
        "IdentityPoolId": str,
        "PushSync": "PushSyncTypeDef",
        "CognitoStreams": "CognitoStreamsTypeDef",
    },
    total=False,
)

UpdateRecordsResponseTypeDef = TypedDict(
    "UpdateRecordsResponseTypeDef",
    {
        "Records": List["RecordTypeDef"],
    },
    total=False,
)
