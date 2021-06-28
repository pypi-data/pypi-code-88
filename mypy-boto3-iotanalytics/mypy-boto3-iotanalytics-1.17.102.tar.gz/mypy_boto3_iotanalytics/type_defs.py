"""
Type annotations for iotanalytics service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotanalytics.type_defs import AddAttributesActivityTypeDef

    data: AddAttributesActivityTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ChannelStatusType,
    ComputeTypeType,
    DatasetActionTypeType,
    DatasetContentStateType,
    DatasetStatusType,
    DatastoreStatusType,
    FileFormatTypeType,
    ReprocessingStatusType,
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
    "AddAttributesActivityTypeDef",
    "BatchPutMessageErrorEntryTypeDef",
    "BatchPutMessageRequestTypeDef",
    "BatchPutMessageResponseResponseTypeDef",
    "CancelPipelineReprocessingRequestTypeDef",
    "ChannelActivityTypeDef",
    "ChannelMessagesTypeDef",
    "ChannelStatisticsTypeDef",
    "ChannelStorageSummaryTypeDef",
    "ChannelStorageTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "ColumnTypeDef",
    "ContainerDatasetActionTypeDef",
    "CreateChannelRequestTypeDef",
    "CreateChannelResponseResponseTypeDef",
    "CreateDatasetContentRequestTypeDef",
    "CreateDatasetContentResponseResponseTypeDef",
    "CreateDatasetRequestTypeDef",
    "CreateDatasetResponseResponseTypeDef",
    "CreateDatastoreRequestTypeDef",
    "CreateDatastoreResponseResponseTypeDef",
    "CreatePipelineRequestTypeDef",
    "CreatePipelineResponseResponseTypeDef",
    "CustomerManagedChannelS3StorageSummaryTypeDef",
    "CustomerManagedChannelS3StorageTypeDef",
    "CustomerManagedDatastoreS3StorageSummaryTypeDef",
    "CustomerManagedDatastoreS3StorageTypeDef",
    "DatasetActionSummaryTypeDef",
    "DatasetActionTypeDef",
    "DatasetContentDeliveryDestinationTypeDef",
    "DatasetContentDeliveryRuleTypeDef",
    "DatasetContentStatusTypeDef",
    "DatasetContentSummaryTypeDef",
    "DatasetContentVersionValueTypeDef",
    "DatasetEntryTypeDef",
    "DatasetSummaryTypeDef",
    "DatasetTriggerTypeDef",
    "DatasetTypeDef",
    "DatastoreActivityTypeDef",
    "DatastorePartitionTypeDef",
    "DatastorePartitionsTypeDef",
    "DatastoreStatisticsTypeDef",
    "DatastoreStorageSummaryTypeDef",
    "DatastoreStorageTypeDef",
    "DatastoreSummaryTypeDef",
    "DatastoreTypeDef",
    "DeleteChannelRequestTypeDef",
    "DeleteDatasetContentRequestTypeDef",
    "DeleteDatasetRequestTypeDef",
    "DeleteDatastoreRequestTypeDef",
    "DeletePipelineRequestTypeDef",
    "DeltaTimeSessionWindowConfigurationTypeDef",
    "DeltaTimeTypeDef",
    "DescribeChannelRequestTypeDef",
    "DescribeChannelResponseResponseTypeDef",
    "DescribeDatasetRequestTypeDef",
    "DescribeDatasetResponseResponseTypeDef",
    "DescribeDatastoreRequestTypeDef",
    "DescribeDatastoreResponseResponseTypeDef",
    "DescribeLoggingOptionsResponseResponseTypeDef",
    "DescribePipelineRequestTypeDef",
    "DescribePipelineResponseResponseTypeDef",
    "DeviceRegistryEnrichActivityTypeDef",
    "DeviceShadowEnrichActivityTypeDef",
    "EstimatedResourceSizeTypeDef",
    "FileFormatConfigurationTypeDef",
    "FilterActivityTypeDef",
    "GetDatasetContentRequestTypeDef",
    "GetDatasetContentResponseResponseTypeDef",
    "GlueConfigurationTypeDef",
    "IotEventsDestinationConfigurationTypeDef",
    "LambdaActivityTypeDef",
    "LateDataRuleConfigurationTypeDef",
    "LateDataRuleTypeDef",
    "ListChannelsRequestTypeDef",
    "ListChannelsResponseResponseTypeDef",
    "ListDatasetContentsRequestTypeDef",
    "ListDatasetContentsResponseResponseTypeDef",
    "ListDatasetsRequestTypeDef",
    "ListDatasetsResponseResponseTypeDef",
    "ListDatastoresRequestTypeDef",
    "ListDatastoresResponseResponseTypeDef",
    "ListPipelinesRequestTypeDef",
    "ListPipelinesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "LoggingOptionsTypeDef",
    "MathActivityTypeDef",
    "MessageTypeDef",
    "OutputFileUriValueTypeDef",
    "PaginatorConfigTypeDef",
    "ParquetConfigurationTypeDef",
    "PartitionTypeDef",
    "PipelineActivityTypeDef",
    "PipelineSummaryTypeDef",
    "PipelineTypeDef",
    "PutLoggingOptionsRequestTypeDef",
    "QueryFilterTypeDef",
    "RemoveAttributesActivityTypeDef",
    "ReprocessingSummaryTypeDef",
    "ResourceConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionPeriodTypeDef",
    "RunPipelineActivityRequestTypeDef",
    "RunPipelineActivityResponseResponseTypeDef",
    "S3DestinationConfigurationTypeDef",
    "SampleChannelDataRequestTypeDef",
    "SampleChannelDataResponseResponseTypeDef",
    "ScheduleTypeDef",
    "SchemaDefinitionTypeDef",
    "SelectAttributesActivityTypeDef",
    "SqlQueryDatasetActionTypeDef",
    "StartPipelineReprocessingRequestTypeDef",
    "StartPipelineReprocessingResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimestampPartitionTypeDef",
    "TriggeringDatasetTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateChannelRequestTypeDef",
    "UpdateDatasetRequestTypeDef",
    "UpdateDatastoreRequestTypeDef",
    "UpdatePipelineRequestTypeDef",
    "VariableTypeDef",
    "VersioningConfigurationTypeDef",
)

_RequiredAddAttributesActivityTypeDef = TypedDict(
    "_RequiredAddAttributesActivityTypeDef",
    {
        "name": str,
        "attributes": Dict[str, str],
    },
)
_OptionalAddAttributesActivityTypeDef = TypedDict(
    "_OptionalAddAttributesActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)


class AddAttributesActivityTypeDef(
    _RequiredAddAttributesActivityTypeDef, _OptionalAddAttributesActivityTypeDef
):
    pass


BatchPutMessageErrorEntryTypeDef = TypedDict(
    "BatchPutMessageErrorEntryTypeDef",
    {
        "messageId": str,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

BatchPutMessageRequestTypeDef = TypedDict(
    "BatchPutMessageRequestTypeDef",
    {
        "channelName": str,
        "messages": List["MessageTypeDef"],
    },
)

BatchPutMessageResponseResponseTypeDef = TypedDict(
    "BatchPutMessageResponseResponseTypeDef",
    {
        "batchPutMessageErrorEntries": List["BatchPutMessageErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelPipelineReprocessingRequestTypeDef = TypedDict(
    "CancelPipelineReprocessingRequestTypeDef",
    {
        "pipelineName": str,
        "reprocessingId": str,
    },
)

_RequiredChannelActivityTypeDef = TypedDict(
    "_RequiredChannelActivityTypeDef",
    {
        "name": str,
        "channelName": str,
    },
)
_OptionalChannelActivityTypeDef = TypedDict(
    "_OptionalChannelActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)


class ChannelActivityTypeDef(_RequiredChannelActivityTypeDef, _OptionalChannelActivityTypeDef):
    pass


ChannelMessagesTypeDef = TypedDict(
    "ChannelMessagesTypeDef",
    {
        "s3Paths": List[str],
    },
    total=False,
)

ChannelStatisticsTypeDef = TypedDict(
    "ChannelStatisticsTypeDef",
    {
        "size": "EstimatedResourceSizeTypeDef",
    },
    total=False,
)

ChannelStorageSummaryTypeDef = TypedDict(
    "ChannelStorageSummaryTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": "CustomerManagedChannelS3StorageSummaryTypeDef",
    },
    total=False,
)

ChannelStorageTypeDef = TypedDict(
    "ChannelStorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": "CustomerManagedChannelS3StorageTypeDef",
    },
    total=False,
)

ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "channelName": str,
        "channelStorage": "ChannelStorageSummaryTypeDef",
        "status": ChannelStatusType,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "lastMessageArrivalTime": datetime,
    },
    total=False,
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "name": str,
        "storage": "ChannelStorageTypeDef",
        "arn": str,
        "status": ChannelStatusType,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "lastMessageArrivalTime": datetime,
    },
    total=False,
)

ColumnTypeDef = TypedDict(
    "ColumnTypeDef",
    {
        "name": str,
        "type": str,
    },
)

_RequiredContainerDatasetActionTypeDef = TypedDict(
    "_RequiredContainerDatasetActionTypeDef",
    {
        "image": str,
        "executionRoleArn": str,
        "resourceConfiguration": "ResourceConfigurationTypeDef",
    },
)
_OptionalContainerDatasetActionTypeDef = TypedDict(
    "_OptionalContainerDatasetActionTypeDef",
    {
        "variables": List["VariableTypeDef"],
    },
    total=False,
)


class ContainerDatasetActionTypeDef(
    _RequiredContainerDatasetActionTypeDef, _OptionalContainerDatasetActionTypeDef
):
    pass


_RequiredCreateChannelRequestTypeDef = TypedDict(
    "_RequiredCreateChannelRequestTypeDef",
    {
        "channelName": str,
    },
)
_OptionalCreateChannelRequestTypeDef = TypedDict(
    "_OptionalCreateChannelRequestTypeDef",
    {
        "channelStorage": "ChannelStorageTypeDef",
        "retentionPeriod": "RetentionPeriodTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateChannelRequestTypeDef(
    _RequiredCreateChannelRequestTypeDef, _OptionalCreateChannelRequestTypeDef
):
    pass


CreateChannelResponseResponseTypeDef = TypedDict(
    "CreateChannelResponseResponseTypeDef",
    {
        "channelName": str,
        "channelArn": str,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatasetContentRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetContentRequestTypeDef",
    {
        "datasetName": str,
    },
)
_OptionalCreateDatasetContentRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetContentRequestTypeDef",
    {
        "versionId": str,
    },
    total=False,
)


class CreateDatasetContentRequestTypeDef(
    _RequiredCreateDatasetContentRequestTypeDef, _OptionalCreateDatasetContentRequestTypeDef
):
    pass


CreateDatasetContentResponseResponseTypeDef = TypedDict(
    "CreateDatasetContentResponseResponseTypeDef",
    {
        "versionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatasetRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetRequestTypeDef",
    {
        "datasetName": str,
        "actions": List["DatasetActionTypeDef"],
    },
)
_OptionalCreateDatasetRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetRequestTypeDef",
    {
        "triggers": List["DatasetTriggerTypeDef"],
        "contentDeliveryRules": List["DatasetContentDeliveryRuleTypeDef"],
        "retentionPeriod": "RetentionPeriodTypeDef",
        "versioningConfiguration": "VersioningConfigurationTypeDef",
        "tags": List["TagTypeDef"],
        "lateDataRules": List["LateDataRuleTypeDef"],
    },
    total=False,
)


class CreateDatasetRequestTypeDef(
    _RequiredCreateDatasetRequestTypeDef, _OptionalCreateDatasetRequestTypeDef
):
    pass


CreateDatasetResponseResponseTypeDef = TypedDict(
    "CreateDatasetResponseResponseTypeDef",
    {
        "datasetName": str,
        "datasetArn": str,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatastoreRequestTypeDef = TypedDict(
    "_RequiredCreateDatastoreRequestTypeDef",
    {
        "datastoreName": str,
    },
)
_OptionalCreateDatastoreRequestTypeDef = TypedDict(
    "_OptionalCreateDatastoreRequestTypeDef",
    {
        "datastoreStorage": "DatastoreStorageTypeDef",
        "retentionPeriod": "RetentionPeriodTypeDef",
        "tags": List["TagTypeDef"],
        "fileFormatConfiguration": "FileFormatConfigurationTypeDef",
        "datastorePartitions": "DatastorePartitionsTypeDef",
    },
    total=False,
)


class CreateDatastoreRequestTypeDef(
    _RequiredCreateDatastoreRequestTypeDef, _OptionalCreateDatastoreRequestTypeDef
):
    pass


CreateDatastoreResponseResponseTypeDef = TypedDict(
    "CreateDatastoreResponseResponseTypeDef",
    {
        "datastoreName": str,
        "datastoreArn": str,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePipelineRequestTypeDef = TypedDict(
    "_RequiredCreatePipelineRequestTypeDef",
    {
        "pipelineName": str,
        "pipelineActivities": List["PipelineActivityTypeDef"],
    },
)
_OptionalCreatePipelineRequestTypeDef = TypedDict(
    "_OptionalCreatePipelineRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreatePipelineRequestTypeDef(
    _RequiredCreatePipelineRequestTypeDef, _OptionalCreatePipelineRequestTypeDef
):
    pass


CreatePipelineResponseResponseTypeDef = TypedDict(
    "CreatePipelineResponseResponseTypeDef",
    {
        "pipelineName": str,
        "pipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomerManagedChannelS3StorageSummaryTypeDef = TypedDict(
    "CustomerManagedChannelS3StorageSummaryTypeDef",
    {
        "bucket": str,
        "keyPrefix": str,
        "roleArn": str,
    },
    total=False,
)

_RequiredCustomerManagedChannelS3StorageTypeDef = TypedDict(
    "_RequiredCustomerManagedChannelS3StorageTypeDef",
    {
        "bucket": str,
        "roleArn": str,
    },
)
_OptionalCustomerManagedChannelS3StorageTypeDef = TypedDict(
    "_OptionalCustomerManagedChannelS3StorageTypeDef",
    {
        "keyPrefix": str,
    },
    total=False,
)


class CustomerManagedChannelS3StorageTypeDef(
    _RequiredCustomerManagedChannelS3StorageTypeDef, _OptionalCustomerManagedChannelS3StorageTypeDef
):
    pass


CustomerManagedDatastoreS3StorageSummaryTypeDef = TypedDict(
    "CustomerManagedDatastoreS3StorageSummaryTypeDef",
    {
        "bucket": str,
        "keyPrefix": str,
        "roleArn": str,
    },
    total=False,
)

_RequiredCustomerManagedDatastoreS3StorageTypeDef = TypedDict(
    "_RequiredCustomerManagedDatastoreS3StorageTypeDef",
    {
        "bucket": str,
        "roleArn": str,
    },
)
_OptionalCustomerManagedDatastoreS3StorageTypeDef = TypedDict(
    "_OptionalCustomerManagedDatastoreS3StorageTypeDef",
    {
        "keyPrefix": str,
    },
    total=False,
)


class CustomerManagedDatastoreS3StorageTypeDef(
    _RequiredCustomerManagedDatastoreS3StorageTypeDef,
    _OptionalCustomerManagedDatastoreS3StorageTypeDef,
):
    pass


DatasetActionSummaryTypeDef = TypedDict(
    "DatasetActionSummaryTypeDef",
    {
        "actionName": str,
        "actionType": DatasetActionTypeType,
    },
    total=False,
)

DatasetActionTypeDef = TypedDict(
    "DatasetActionTypeDef",
    {
        "actionName": str,
        "queryAction": "SqlQueryDatasetActionTypeDef",
        "containerAction": "ContainerDatasetActionTypeDef",
    },
    total=False,
)

DatasetContentDeliveryDestinationTypeDef = TypedDict(
    "DatasetContentDeliveryDestinationTypeDef",
    {
        "iotEventsDestinationConfiguration": "IotEventsDestinationConfigurationTypeDef",
        "s3DestinationConfiguration": "S3DestinationConfigurationTypeDef",
    },
    total=False,
)

_RequiredDatasetContentDeliveryRuleTypeDef = TypedDict(
    "_RequiredDatasetContentDeliveryRuleTypeDef",
    {
        "destination": "DatasetContentDeliveryDestinationTypeDef",
    },
)
_OptionalDatasetContentDeliveryRuleTypeDef = TypedDict(
    "_OptionalDatasetContentDeliveryRuleTypeDef",
    {
        "entryName": str,
    },
    total=False,
)


class DatasetContentDeliveryRuleTypeDef(
    _RequiredDatasetContentDeliveryRuleTypeDef, _OptionalDatasetContentDeliveryRuleTypeDef
):
    pass


DatasetContentStatusTypeDef = TypedDict(
    "DatasetContentStatusTypeDef",
    {
        "state": DatasetContentStateType,
        "reason": str,
    },
    total=False,
)

DatasetContentSummaryTypeDef = TypedDict(
    "DatasetContentSummaryTypeDef",
    {
        "version": str,
        "status": "DatasetContentStatusTypeDef",
        "creationTime": datetime,
        "scheduleTime": datetime,
        "completionTime": datetime,
    },
    total=False,
)

DatasetContentVersionValueTypeDef = TypedDict(
    "DatasetContentVersionValueTypeDef",
    {
        "datasetName": str,
    },
)

DatasetEntryTypeDef = TypedDict(
    "DatasetEntryTypeDef",
    {
        "entryName": str,
        "dataURI": str,
    },
    total=False,
)

DatasetSummaryTypeDef = TypedDict(
    "DatasetSummaryTypeDef",
    {
        "datasetName": str,
        "status": DatasetStatusType,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "triggers": List["DatasetTriggerTypeDef"],
        "actions": List["DatasetActionSummaryTypeDef"],
    },
    total=False,
)

DatasetTriggerTypeDef = TypedDict(
    "DatasetTriggerTypeDef",
    {
        "schedule": "ScheduleTypeDef",
        "dataset": "TriggeringDatasetTypeDef",
    },
    total=False,
)

DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "name": str,
        "arn": str,
        "actions": List["DatasetActionTypeDef"],
        "triggers": List["DatasetTriggerTypeDef"],
        "contentDeliveryRules": List["DatasetContentDeliveryRuleTypeDef"],
        "status": DatasetStatusType,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "versioningConfiguration": "VersioningConfigurationTypeDef",
        "lateDataRules": List["LateDataRuleTypeDef"],
    },
    total=False,
)

DatastoreActivityTypeDef = TypedDict(
    "DatastoreActivityTypeDef",
    {
        "name": str,
        "datastoreName": str,
    },
)

DatastorePartitionTypeDef = TypedDict(
    "DatastorePartitionTypeDef",
    {
        "attributePartition": "PartitionTypeDef",
        "timestampPartition": "TimestampPartitionTypeDef",
    },
    total=False,
)

DatastorePartitionsTypeDef = TypedDict(
    "DatastorePartitionsTypeDef",
    {
        "partitions": List["DatastorePartitionTypeDef"],
    },
    total=False,
)

DatastoreStatisticsTypeDef = TypedDict(
    "DatastoreStatisticsTypeDef",
    {
        "size": "EstimatedResourceSizeTypeDef",
    },
    total=False,
)

DatastoreStorageSummaryTypeDef = TypedDict(
    "DatastoreStorageSummaryTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": "CustomerManagedDatastoreS3StorageSummaryTypeDef",
    },
    total=False,
)

DatastoreStorageTypeDef = TypedDict(
    "DatastoreStorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": "CustomerManagedDatastoreS3StorageTypeDef",
    },
    total=False,
)

DatastoreSummaryTypeDef = TypedDict(
    "DatastoreSummaryTypeDef",
    {
        "datastoreName": str,
        "datastoreStorage": "DatastoreStorageSummaryTypeDef",
        "status": DatastoreStatusType,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "lastMessageArrivalTime": datetime,
        "fileFormatType": FileFormatTypeType,
        "datastorePartitions": "DatastorePartitionsTypeDef",
    },
    total=False,
)

DatastoreTypeDef = TypedDict(
    "DatastoreTypeDef",
    {
        "name": str,
        "storage": "DatastoreStorageTypeDef",
        "arn": str,
        "status": DatastoreStatusType,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "lastMessageArrivalTime": datetime,
        "fileFormatConfiguration": "FileFormatConfigurationTypeDef",
        "datastorePartitions": "DatastorePartitionsTypeDef",
    },
    total=False,
)

DeleteChannelRequestTypeDef = TypedDict(
    "DeleteChannelRequestTypeDef",
    {
        "channelName": str,
    },
)

_RequiredDeleteDatasetContentRequestTypeDef = TypedDict(
    "_RequiredDeleteDatasetContentRequestTypeDef",
    {
        "datasetName": str,
    },
)
_OptionalDeleteDatasetContentRequestTypeDef = TypedDict(
    "_OptionalDeleteDatasetContentRequestTypeDef",
    {
        "versionId": str,
    },
    total=False,
)


class DeleteDatasetContentRequestTypeDef(
    _RequiredDeleteDatasetContentRequestTypeDef, _OptionalDeleteDatasetContentRequestTypeDef
):
    pass


DeleteDatasetRequestTypeDef = TypedDict(
    "DeleteDatasetRequestTypeDef",
    {
        "datasetName": str,
    },
)

DeleteDatastoreRequestTypeDef = TypedDict(
    "DeleteDatastoreRequestTypeDef",
    {
        "datastoreName": str,
    },
)

DeletePipelineRequestTypeDef = TypedDict(
    "DeletePipelineRequestTypeDef",
    {
        "pipelineName": str,
    },
)

DeltaTimeSessionWindowConfigurationTypeDef = TypedDict(
    "DeltaTimeSessionWindowConfigurationTypeDef",
    {
        "timeoutInMinutes": int,
    },
)

DeltaTimeTypeDef = TypedDict(
    "DeltaTimeTypeDef",
    {
        "offsetSeconds": int,
        "timeExpression": str,
    },
)

_RequiredDescribeChannelRequestTypeDef = TypedDict(
    "_RequiredDescribeChannelRequestTypeDef",
    {
        "channelName": str,
    },
)
_OptionalDescribeChannelRequestTypeDef = TypedDict(
    "_OptionalDescribeChannelRequestTypeDef",
    {
        "includeStatistics": bool,
    },
    total=False,
)


class DescribeChannelRequestTypeDef(
    _RequiredDescribeChannelRequestTypeDef, _OptionalDescribeChannelRequestTypeDef
):
    pass


DescribeChannelResponseResponseTypeDef = TypedDict(
    "DescribeChannelResponseResponseTypeDef",
    {
        "channel": "ChannelTypeDef",
        "statistics": "ChannelStatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestTypeDef = TypedDict(
    "DescribeDatasetRequestTypeDef",
    {
        "datasetName": str,
    },
)

DescribeDatasetResponseResponseTypeDef = TypedDict(
    "DescribeDatasetResponseResponseTypeDef",
    {
        "dataset": "DatasetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDatastoreRequestTypeDef = TypedDict(
    "_RequiredDescribeDatastoreRequestTypeDef",
    {
        "datastoreName": str,
    },
)
_OptionalDescribeDatastoreRequestTypeDef = TypedDict(
    "_OptionalDescribeDatastoreRequestTypeDef",
    {
        "includeStatistics": bool,
    },
    total=False,
)


class DescribeDatastoreRequestTypeDef(
    _RequiredDescribeDatastoreRequestTypeDef, _OptionalDescribeDatastoreRequestTypeDef
):
    pass


DescribeDatastoreResponseResponseTypeDef = TypedDict(
    "DescribeDatastoreResponseResponseTypeDef",
    {
        "datastore": "DatastoreTypeDef",
        "statistics": "DatastoreStatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoggingOptionsResponseResponseTypeDef = TypedDict(
    "DescribeLoggingOptionsResponseResponseTypeDef",
    {
        "loggingOptions": "LoggingOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePipelineRequestTypeDef = TypedDict(
    "DescribePipelineRequestTypeDef",
    {
        "pipelineName": str,
    },
)

DescribePipelineResponseResponseTypeDef = TypedDict(
    "DescribePipelineResponseResponseTypeDef",
    {
        "pipeline": "PipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeviceRegistryEnrichActivityTypeDef = TypedDict(
    "_RequiredDeviceRegistryEnrichActivityTypeDef",
    {
        "name": str,
        "attribute": str,
        "thingName": str,
        "roleArn": str,
    },
)
_OptionalDeviceRegistryEnrichActivityTypeDef = TypedDict(
    "_OptionalDeviceRegistryEnrichActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)


class DeviceRegistryEnrichActivityTypeDef(
    _RequiredDeviceRegistryEnrichActivityTypeDef, _OptionalDeviceRegistryEnrichActivityTypeDef
):
    pass


_RequiredDeviceShadowEnrichActivityTypeDef = TypedDict(
    "_RequiredDeviceShadowEnrichActivityTypeDef",
    {
        "name": str,
        "attribute": str,
        "thingName": str,
        "roleArn": str,
    },
)
_OptionalDeviceShadowEnrichActivityTypeDef = TypedDict(
    "_OptionalDeviceShadowEnrichActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)


class DeviceShadowEnrichActivityTypeDef(
    _RequiredDeviceShadowEnrichActivityTypeDef, _OptionalDeviceShadowEnrichActivityTypeDef
):
    pass


EstimatedResourceSizeTypeDef = TypedDict(
    "EstimatedResourceSizeTypeDef",
    {
        "estimatedSizeInBytes": float,
        "estimatedOn": datetime,
    },
    total=False,
)

FileFormatConfigurationTypeDef = TypedDict(
    "FileFormatConfigurationTypeDef",
    {
        "jsonConfiguration": Dict[str, Any],
        "parquetConfiguration": "ParquetConfigurationTypeDef",
    },
    total=False,
)

_RequiredFilterActivityTypeDef = TypedDict(
    "_RequiredFilterActivityTypeDef",
    {
        "name": str,
        "filter": str,
    },
)
_OptionalFilterActivityTypeDef = TypedDict(
    "_OptionalFilterActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)


class FilterActivityTypeDef(_RequiredFilterActivityTypeDef, _OptionalFilterActivityTypeDef):
    pass


_RequiredGetDatasetContentRequestTypeDef = TypedDict(
    "_RequiredGetDatasetContentRequestTypeDef",
    {
        "datasetName": str,
    },
)
_OptionalGetDatasetContentRequestTypeDef = TypedDict(
    "_OptionalGetDatasetContentRequestTypeDef",
    {
        "versionId": str,
    },
    total=False,
)


class GetDatasetContentRequestTypeDef(
    _RequiredGetDatasetContentRequestTypeDef, _OptionalGetDatasetContentRequestTypeDef
):
    pass


GetDatasetContentResponseResponseTypeDef = TypedDict(
    "GetDatasetContentResponseResponseTypeDef",
    {
        "entries": List["DatasetEntryTypeDef"],
        "timestamp": datetime,
        "status": "DatasetContentStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GlueConfigurationTypeDef = TypedDict(
    "GlueConfigurationTypeDef",
    {
        "tableName": str,
        "databaseName": str,
    },
)

IotEventsDestinationConfigurationTypeDef = TypedDict(
    "IotEventsDestinationConfigurationTypeDef",
    {
        "inputName": str,
        "roleArn": str,
    },
)

_RequiredLambdaActivityTypeDef = TypedDict(
    "_RequiredLambdaActivityTypeDef",
    {
        "name": str,
        "lambdaName": str,
        "batchSize": int,
    },
)
_OptionalLambdaActivityTypeDef = TypedDict(
    "_OptionalLambdaActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)


class LambdaActivityTypeDef(_RequiredLambdaActivityTypeDef, _OptionalLambdaActivityTypeDef):
    pass


LateDataRuleConfigurationTypeDef = TypedDict(
    "LateDataRuleConfigurationTypeDef",
    {
        "deltaTimeSessionWindowConfiguration": "DeltaTimeSessionWindowConfigurationTypeDef",
    },
    total=False,
)

_RequiredLateDataRuleTypeDef = TypedDict(
    "_RequiredLateDataRuleTypeDef",
    {
        "ruleConfiguration": "LateDataRuleConfigurationTypeDef",
    },
)
_OptionalLateDataRuleTypeDef = TypedDict(
    "_OptionalLateDataRuleTypeDef",
    {
        "ruleName": str,
    },
    total=False,
)


class LateDataRuleTypeDef(_RequiredLateDataRuleTypeDef, _OptionalLateDataRuleTypeDef):
    pass


ListChannelsRequestTypeDef = TypedDict(
    "ListChannelsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListChannelsResponseResponseTypeDef = TypedDict(
    "ListChannelsResponseResponseTypeDef",
    {
        "channelSummaries": List["ChannelSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDatasetContentsRequestTypeDef = TypedDict(
    "_RequiredListDatasetContentsRequestTypeDef",
    {
        "datasetName": str,
    },
)
_OptionalListDatasetContentsRequestTypeDef = TypedDict(
    "_OptionalListDatasetContentsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "scheduledOnOrAfter": Union[datetime, str],
        "scheduledBefore": Union[datetime, str],
    },
    total=False,
)


class ListDatasetContentsRequestTypeDef(
    _RequiredListDatasetContentsRequestTypeDef, _OptionalListDatasetContentsRequestTypeDef
):
    pass


ListDatasetContentsResponseResponseTypeDef = TypedDict(
    "ListDatasetContentsResponseResponseTypeDef",
    {
        "datasetContentSummaries": List["DatasetContentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetsRequestTypeDef = TypedDict(
    "ListDatasetsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDatasetsResponseResponseTypeDef = TypedDict(
    "ListDatasetsResponseResponseTypeDef",
    {
        "datasetSummaries": List["DatasetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatastoresRequestTypeDef = TypedDict(
    "ListDatastoresRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDatastoresResponseResponseTypeDef = TypedDict(
    "ListDatastoresResponseResponseTypeDef",
    {
        "datastoreSummaries": List["DatastoreSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPipelinesRequestTypeDef = TypedDict(
    "ListPipelinesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListPipelinesResponseResponseTypeDef = TypedDict(
    "ListPipelinesResponseResponseTypeDef",
    {
        "pipelineSummaries": List["PipelineSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingOptionsTypeDef = TypedDict(
    "LoggingOptionsTypeDef",
    {
        "roleArn": str,
        "level": Literal["ERROR"],
        "enabled": bool,
    },
)

_RequiredMathActivityTypeDef = TypedDict(
    "_RequiredMathActivityTypeDef",
    {
        "name": str,
        "attribute": str,
        "math": str,
    },
)
_OptionalMathActivityTypeDef = TypedDict(
    "_OptionalMathActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)


class MathActivityTypeDef(_RequiredMathActivityTypeDef, _OptionalMathActivityTypeDef):
    pass


MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "messageId": str,
        "payload": Union[bytes, IO[bytes], StreamingBody],
    },
)

OutputFileUriValueTypeDef = TypedDict(
    "OutputFileUriValueTypeDef",
    {
        "fileName": str,
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

ParquetConfigurationTypeDef = TypedDict(
    "ParquetConfigurationTypeDef",
    {
        "schemaDefinition": "SchemaDefinitionTypeDef",
    },
    total=False,
)

PartitionTypeDef = TypedDict(
    "PartitionTypeDef",
    {
        "attributeName": str,
    },
)

PipelineActivityTypeDef = TypedDict(
    "PipelineActivityTypeDef",
    {
        "channel": "ChannelActivityTypeDef",
        "lambda": "LambdaActivityTypeDef",
        "datastore": "DatastoreActivityTypeDef",
        "addAttributes": "AddAttributesActivityTypeDef",
        "removeAttributes": "RemoveAttributesActivityTypeDef",
        "selectAttributes": "SelectAttributesActivityTypeDef",
        "filter": "FilterActivityTypeDef",
        "math": "MathActivityTypeDef",
        "deviceRegistryEnrich": "DeviceRegistryEnrichActivityTypeDef",
        "deviceShadowEnrich": "DeviceShadowEnrichActivityTypeDef",
    },
    total=False,
)

PipelineSummaryTypeDef = TypedDict(
    "PipelineSummaryTypeDef",
    {
        "pipelineName": str,
        "reprocessingSummaries": List["ReprocessingSummaryTypeDef"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

PipelineTypeDef = TypedDict(
    "PipelineTypeDef",
    {
        "name": str,
        "arn": str,
        "activities": List["PipelineActivityTypeDef"],
        "reprocessingSummaries": List["ReprocessingSummaryTypeDef"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

PutLoggingOptionsRequestTypeDef = TypedDict(
    "PutLoggingOptionsRequestTypeDef",
    {
        "loggingOptions": "LoggingOptionsTypeDef",
    },
)

QueryFilterTypeDef = TypedDict(
    "QueryFilterTypeDef",
    {
        "deltaTime": "DeltaTimeTypeDef",
    },
    total=False,
)

_RequiredRemoveAttributesActivityTypeDef = TypedDict(
    "_RequiredRemoveAttributesActivityTypeDef",
    {
        "name": str,
        "attributes": List[str],
    },
)
_OptionalRemoveAttributesActivityTypeDef = TypedDict(
    "_OptionalRemoveAttributesActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)


class RemoveAttributesActivityTypeDef(
    _RequiredRemoveAttributesActivityTypeDef, _OptionalRemoveAttributesActivityTypeDef
):
    pass


ReprocessingSummaryTypeDef = TypedDict(
    "ReprocessingSummaryTypeDef",
    {
        "id": str,
        "status": ReprocessingStatusType,
        "creationTime": datetime,
    },
    total=False,
)

ResourceConfigurationTypeDef = TypedDict(
    "ResourceConfigurationTypeDef",
    {
        "computeType": ComputeTypeType,
        "volumeSizeInGB": int,
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

RetentionPeriodTypeDef = TypedDict(
    "RetentionPeriodTypeDef",
    {
        "unlimited": bool,
        "numberOfDays": int,
    },
    total=False,
)

RunPipelineActivityRequestTypeDef = TypedDict(
    "RunPipelineActivityRequestTypeDef",
    {
        "pipelineActivity": "PipelineActivityTypeDef",
        "payloads": List[Union[bytes, IO[bytes], StreamingBody]],
    },
)

RunPipelineActivityResponseResponseTypeDef = TypedDict(
    "RunPipelineActivityResponseResponseTypeDef",
    {
        "payloads": List[bytes],
        "logResult": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredS3DestinationConfigurationTypeDef = TypedDict(
    "_RequiredS3DestinationConfigurationTypeDef",
    {
        "bucket": str,
        "key": str,
        "roleArn": str,
    },
)
_OptionalS3DestinationConfigurationTypeDef = TypedDict(
    "_OptionalS3DestinationConfigurationTypeDef",
    {
        "glueConfiguration": "GlueConfigurationTypeDef",
    },
    total=False,
)


class S3DestinationConfigurationTypeDef(
    _RequiredS3DestinationConfigurationTypeDef, _OptionalS3DestinationConfigurationTypeDef
):
    pass


_RequiredSampleChannelDataRequestTypeDef = TypedDict(
    "_RequiredSampleChannelDataRequestTypeDef",
    {
        "channelName": str,
    },
)
_OptionalSampleChannelDataRequestTypeDef = TypedDict(
    "_OptionalSampleChannelDataRequestTypeDef",
    {
        "maxMessages": int,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
    total=False,
)


class SampleChannelDataRequestTypeDef(
    _RequiredSampleChannelDataRequestTypeDef, _OptionalSampleChannelDataRequestTypeDef
):
    pass


SampleChannelDataResponseResponseTypeDef = TypedDict(
    "SampleChannelDataResponseResponseTypeDef",
    {
        "payloads": List[bytes],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "expression": str,
    },
    total=False,
)

SchemaDefinitionTypeDef = TypedDict(
    "SchemaDefinitionTypeDef",
    {
        "columns": List["ColumnTypeDef"],
    },
    total=False,
)

_RequiredSelectAttributesActivityTypeDef = TypedDict(
    "_RequiredSelectAttributesActivityTypeDef",
    {
        "name": str,
        "attributes": List[str],
    },
)
_OptionalSelectAttributesActivityTypeDef = TypedDict(
    "_OptionalSelectAttributesActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)


class SelectAttributesActivityTypeDef(
    _RequiredSelectAttributesActivityTypeDef, _OptionalSelectAttributesActivityTypeDef
):
    pass


_RequiredSqlQueryDatasetActionTypeDef = TypedDict(
    "_RequiredSqlQueryDatasetActionTypeDef",
    {
        "sqlQuery": str,
    },
)
_OptionalSqlQueryDatasetActionTypeDef = TypedDict(
    "_OptionalSqlQueryDatasetActionTypeDef",
    {
        "filters": List["QueryFilterTypeDef"],
    },
    total=False,
)


class SqlQueryDatasetActionTypeDef(
    _RequiredSqlQueryDatasetActionTypeDef, _OptionalSqlQueryDatasetActionTypeDef
):
    pass


_RequiredStartPipelineReprocessingRequestTypeDef = TypedDict(
    "_RequiredStartPipelineReprocessingRequestTypeDef",
    {
        "pipelineName": str,
    },
)
_OptionalStartPipelineReprocessingRequestTypeDef = TypedDict(
    "_OptionalStartPipelineReprocessingRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "channelMessages": "ChannelMessagesTypeDef",
    },
    total=False,
)


class StartPipelineReprocessingRequestTypeDef(
    _RequiredStartPipelineReprocessingRequestTypeDef,
    _OptionalStartPipelineReprocessingRequestTypeDef,
):
    pass


StartPipelineReprocessingResponseResponseTypeDef = TypedDict(
    "StartPipelineReprocessingResponseResponseTypeDef",
    {
        "reprocessingId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

_RequiredTimestampPartitionTypeDef = TypedDict(
    "_RequiredTimestampPartitionTypeDef",
    {
        "attributeName": str,
    },
)
_OptionalTimestampPartitionTypeDef = TypedDict(
    "_OptionalTimestampPartitionTypeDef",
    {
        "timestampFormat": str,
    },
    total=False,
)


class TimestampPartitionTypeDef(
    _RequiredTimestampPartitionTypeDef, _OptionalTimestampPartitionTypeDef
):
    pass


TriggeringDatasetTypeDef = TypedDict(
    "TriggeringDatasetTypeDef",
    {
        "name": str,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateChannelRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelRequestTypeDef",
    {
        "channelName": str,
    },
)
_OptionalUpdateChannelRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelRequestTypeDef",
    {
        "channelStorage": "ChannelStorageTypeDef",
        "retentionPeriod": "RetentionPeriodTypeDef",
    },
    total=False,
)


class UpdateChannelRequestTypeDef(
    _RequiredUpdateChannelRequestTypeDef, _OptionalUpdateChannelRequestTypeDef
):
    pass


_RequiredUpdateDatasetRequestTypeDef = TypedDict(
    "_RequiredUpdateDatasetRequestTypeDef",
    {
        "datasetName": str,
        "actions": List["DatasetActionTypeDef"],
    },
)
_OptionalUpdateDatasetRequestTypeDef = TypedDict(
    "_OptionalUpdateDatasetRequestTypeDef",
    {
        "triggers": List["DatasetTriggerTypeDef"],
        "contentDeliveryRules": List["DatasetContentDeliveryRuleTypeDef"],
        "retentionPeriod": "RetentionPeriodTypeDef",
        "versioningConfiguration": "VersioningConfigurationTypeDef",
        "lateDataRules": List["LateDataRuleTypeDef"],
    },
    total=False,
)


class UpdateDatasetRequestTypeDef(
    _RequiredUpdateDatasetRequestTypeDef, _OptionalUpdateDatasetRequestTypeDef
):
    pass


_RequiredUpdateDatastoreRequestTypeDef = TypedDict(
    "_RequiredUpdateDatastoreRequestTypeDef",
    {
        "datastoreName": str,
    },
)
_OptionalUpdateDatastoreRequestTypeDef = TypedDict(
    "_OptionalUpdateDatastoreRequestTypeDef",
    {
        "retentionPeriod": "RetentionPeriodTypeDef",
        "datastoreStorage": "DatastoreStorageTypeDef",
        "fileFormatConfiguration": "FileFormatConfigurationTypeDef",
    },
    total=False,
)


class UpdateDatastoreRequestTypeDef(
    _RequiredUpdateDatastoreRequestTypeDef, _OptionalUpdateDatastoreRequestTypeDef
):
    pass


UpdatePipelineRequestTypeDef = TypedDict(
    "UpdatePipelineRequestTypeDef",
    {
        "pipelineName": str,
        "pipelineActivities": List["PipelineActivityTypeDef"],
    },
)

_RequiredVariableTypeDef = TypedDict(
    "_RequiredVariableTypeDef",
    {
        "name": str,
    },
)
_OptionalVariableTypeDef = TypedDict(
    "_OptionalVariableTypeDef",
    {
        "stringValue": str,
        "doubleValue": float,
        "datasetContentVersionValue": "DatasetContentVersionValueTypeDef",
        "outputFileUriValue": "OutputFileUriValueTypeDef",
    },
    total=False,
)


class VariableTypeDef(_RequiredVariableTypeDef, _OptionalVariableTypeDef):
    pass


VersioningConfigurationTypeDef = TypedDict(
    "VersioningConfigurationTypeDef",
    {
        "unlimited": bool,
        "maxVersions": int,
    },
    total=False,
)
