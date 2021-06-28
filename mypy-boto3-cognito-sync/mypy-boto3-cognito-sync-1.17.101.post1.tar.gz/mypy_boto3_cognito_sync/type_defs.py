"""
Type annotations for cognito-sync service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cognito_sync.type_defs import BulkPublishRequestTypeDef

    data: BulkPublishRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import BulkPublishStatusType, OperationType, PlatformType, StreamingStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BulkPublishRequestTypeDef",
    "BulkPublishResponseResponseTypeDef",
    "CognitoStreamsTypeDef",
    "DatasetTypeDef",
    "DeleteDatasetRequestTypeDef",
    "DeleteDatasetResponseResponseTypeDef",
    "DescribeDatasetRequestTypeDef",
    "DescribeDatasetResponseResponseTypeDef",
    "DescribeIdentityPoolUsageRequestTypeDef",
    "DescribeIdentityPoolUsageResponseResponseTypeDef",
    "DescribeIdentityUsageRequestTypeDef",
    "DescribeIdentityUsageResponseResponseTypeDef",
    "GetBulkPublishDetailsRequestTypeDef",
    "GetBulkPublishDetailsResponseResponseTypeDef",
    "GetCognitoEventsRequestTypeDef",
    "GetCognitoEventsResponseResponseTypeDef",
    "GetIdentityPoolConfigurationRequestTypeDef",
    "GetIdentityPoolConfigurationResponseResponseTypeDef",
    "IdentityPoolUsageTypeDef",
    "IdentityUsageTypeDef",
    "ListDatasetsRequestTypeDef",
    "ListDatasetsResponseResponseTypeDef",
    "ListIdentityPoolUsageRequestTypeDef",
    "ListIdentityPoolUsageResponseResponseTypeDef",
    "ListRecordsRequestTypeDef",
    "ListRecordsResponseResponseTypeDef",
    "PushSyncTypeDef",
    "RecordPatchTypeDef",
    "RecordTypeDef",
    "RegisterDeviceRequestTypeDef",
    "RegisterDeviceResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SetCognitoEventsRequestTypeDef",
    "SetIdentityPoolConfigurationRequestTypeDef",
    "SetIdentityPoolConfigurationResponseResponseTypeDef",
    "SubscribeToDatasetRequestTypeDef",
    "UnsubscribeFromDatasetRequestTypeDef",
    "UpdateRecordsRequestTypeDef",
    "UpdateRecordsResponseResponseTypeDef",
)

BulkPublishRequestTypeDef = TypedDict(
    "BulkPublishRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

BulkPublishResponseResponseTypeDef = TypedDict(
    "BulkPublishResponseResponseTypeDef",
    {
        "IdentityPoolId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

DeleteDatasetRequestTypeDef = TypedDict(
    "DeleteDatasetRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
    },
)

DeleteDatasetResponseResponseTypeDef = TypedDict(
    "DeleteDatasetResponseResponseTypeDef",
    {
        "Dataset": "DatasetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestTypeDef = TypedDict(
    "DescribeDatasetRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
    },
)

DescribeDatasetResponseResponseTypeDef = TypedDict(
    "DescribeDatasetResponseResponseTypeDef",
    {
        "Dataset": "DatasetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIdentityPoolUsageRequestTypeDef = TypedDict(
    "DescribeIdentityPoolUsageRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

DescribeIdentityPoolUsageResponseResponseTypeDef = TypedDict(
    "DescribeIdentityPoolUsageResponseResponseTypeDef",
    {
        "IdentityPoolUsage": "IdentityPoolUsageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIdentityUsageRequestTypeDef = TypedDict(
    "DescribeIdentityUsageRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
    },
)

DescribeIdentityUsageResponseResponseTypeDef = TypedDict(
    "DescribeIdentityUsageResponseResponseTypeDef",
    {
        "IdentityUsage": "IdentityUsageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBulkPublishDetailsRequestTypeDef = TypedDict(
    "GetBulkPublishDetailsRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

GetBulkPublishDetailsResponseResponseTypeDef = TypedDict(
    "GetBulkPublishDetailsResponseResponseTypeDef",
    {
        "IdentityPoolId": str,
        "BulkPublishStartTime": datetime,
        "BulkPublishCompleteTime": datetime,
        "BulkPublishStatus": BulkPublishStatusType,
        "FailureMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCognitoEventsRequestTypeDef = TypedDict(
    "GetCognitoEventsRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

GetCognitoEventsResponseResponseTypeDef = TypedDict(
    "GetCognitoEventsResponseResponseTypeDef",
    {
        "Events": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityPoolConfigurationRequestTypeDef = TypedDict(
    "GetIdentityPoolConfigurationRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

GetIdentityPoolConfigurationResponseResponseTypeDef = TypedDict(
    "GetIdentityPoolConfigurationResponseResponseTypeDef",
    {
        "IdentityPoolId": str,
        "PushSync": "PushSyncTypeDef",
        "CognitoStreams": "CognitoStreamsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredListDatasetsRequestTypeDef = TypedDict(
    "_RequiredListDatasetsRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
    },
)
_OptionalListDatasetsRequestTypeDef = TypedDict(
    "_OptionalListDatasetsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListDatasetsRequestTypeDef(
    _RequiredListDatasetsRequestTypeDef, _OptionalListDatasetsRequestTypeDef
):
    pass


ListDatasetsResponseResponseTypeDef = TypedDict(
    "ListDatasetsResponseResponseTypeDef",
    {
        "Datasets": List["DatasetTypeDef"],
        "Count": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdentityPoolUsageRequestTypeDef = TypedDict(
    "ListIdentityPoolUsageRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListIdentityPoolUsageResponseResponseTypeDef = TypedDict(
    "ListIdentityPoolUsageResponseResponseTypeDef",
    {
        "IdentityPoolUsages": List["IdentityPoolUsageTypeDef"],
        "MaxResults": int,
        "Count": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRecordsRequestTypeDef = TypedDict(
    "_RequiredListRecordsRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
    },
)
_OptionalListRecordsRequestTypeDef = TypedDict(
    "_OptionalListRecordsRequestTypeDef",
    {
        "LastSyncCount": int,
        "NextToken": str,
        "MaxResults": int,
        "SyncSessionToken": str,
    },
    total=False,
)


class ListRecordsRequestTypeDef(
    _RequiredListRecordsRequestTypeDef, _OptionalListRecordsRequestTypeDef
):
    pass


ListRecordsResponseResponseTypeDef = TypedDict(
    "ListRecordsResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "DeviceLastModifiedDate": Union[datetime, str],
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

RegisterDeviceRequestTypeDef = TypedDict(
    "RegisterDeviceRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "Platform": PlatformType,
        "Token": str,
    },
)

RegisterDeviceResponseResponseTypeDef = TypedDict(
    "RegisterDeviceResponseResponseTypeDef",
    {
        "DeviceId": str,
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

SetCognitoEventsRequestTypeDef = TypedDict(
    "SetCognitoEventsRequestTypeDef",
    {
        "IdentityPoolId": str,
        "Events": Dict[str, str],
    },
)

_RequiredSetIdentityPoolConfigurationRequestTypeDef = TypedDict(
    "_RequiredSetIdentityPoolConfigurationRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)
_OptionalSetIdentityPoolConfigurationRequestTypeDef = TypedDict(
    "_OptionalSetIdentityPoolConfigurationRequestTypeDef",
    {
        "PushSync": "PushSyncTypeDef",
        "CognitoStreams": "CognitoStreamsTypeDef",
    },
    total=False,
)


class SetIdentityPoolConfigurationRequestTypeDef(
    _RequiredSetIdentityPoolConfigurationRequestTypeDef,
    _OptionalSetIdentityPoolConfigurationRequestTypeDef,
):
    pass


SetIdentityPoolConfigurationResponseResponseTypeDef = TypedDict(
    "SetIdentityPoolConfigurationResponseResponseTypeDef",
    {
        "IdentityPoolId": str,
        "PushSync": "PushSyncTypeDef",
        "CognitoStreams": "CognitoStreamsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubscribeToDatasetRequestTypeDef = TypedDict(
    "SubscribeToDatasetRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
        "DeviceId": str,
    },
)

UnsubscribeFromDatasetRequestTypeDef = TypedDict(
    "UnsubscribeFromDatasetRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
        "DeviceId": str,
    },
)

_RequiredUpdateRecordsRequestTypeDef = TypedDict(
    "_RequiredUpdateRecordsRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
        "SyncSessionToken": str,
    },
)
_OptionalUpdateRecordsRequestTypeDef = TypedDict(
    "_OptionalUpdateRecordsRequestTypeDef",
    {
        "DeviceId": str,
        "RecordPatches": List["RecordPatchTypeDef"],
        "ClientContext": str,
    },
    total=False,
)


class UpdateRecordsRequestTypeDef(
    _RequiredUpdateRecordsRequestTypeDef, _OptionalUpdateRecordsRequestTypeDef
):
    pass


UpdateRecordsResponseResponseTypeDef = TypedDict(
    "UpdateRecordsResponseResponseTypeDef",
    {
        "Records": List["RecordTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
