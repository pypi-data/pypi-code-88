"""
Type annotations for dynamodb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_dynamodb.type_defs import ArchivalSummaryTypeDef

    data: ArchivalSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, Set, Union

from boto3.dynamodb.conditions import ConditionBase

from .literals import (
    AttributeActionType,
    BackupStatusType,
    BackupTypeFilterType,
    BackupTypeType,
    BatchStatementErrorCodeEnumType,
    BillingModeType,
    ComparisonOperatorType,
    ConditionalOperatorType,
    ContinuousBackupsStatusType,
    ContributorInsightsActionType,
    ContributorInsightsStatusType,
    DestinationStatusType,
    ExportFormatType,
    ExportStatusType,
    GlobalTableStatusType,
    IndexStatusType,
    KeyTypeType,
    PointInTimeRecoveryStatusType,
    ProjectionTypeType,
    ReplicaStatusType,
    ReturnConsumedCapacityType,
    ReturnItemCollectionMetricsType,
    ReturnValuesOnConditionCheckFailureType,
    ReturnValueType,
    S3SseAlgorithmType,
    ScalarAttributeTypeType,
    SelectType,
    SSEStatusType,
    SSETypeType,
    StreamViewTypeType,
    TableStatusType,
    TimeToLiveStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ArchivalSummaryTypeDef",
    "AttributeDefinitionTypeDef",
    "AttributeValueUpdateTypeDef",
    "AutoScalingPolicyDescriptionTypeDef",
    "AutoScalingPolicyUpdateTypeDef",
    "AutoScalingSettingsDescriptionTypeDef",
    "AutoScalingSettingsUpdateTypeDef",
    "AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    "AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    "BackupDescriptionTypeDef",
    "BackupDetailsTypeDef",
    "BackupSummaryTypeDef",
    "BatchExecuteStatementInputTypeDef",
    "BatchExecuteStatementOutputResponseTypeDef",
    "BatchGetItemInputServiceResourceTypeDef",
    "BatchGetItemInputTypeDef",
    "BatchGetItemOutputResponseTypeDef",
    "BatchStatementErrorTypeDef",
    "BatchStatementRequestTypeDef",
    "BatchStatementResponseTypeDef",
    "BatchWriteItemInputServiceResourceTypeDef",
    "BatchWriteItemInputTypeDef",
    "BatchWriteItemOutputResponseTypeDef",
    "BillingModeSummaryTypeDef",
    "CapacityTypeDef",
    "ConditionCheckTypeDef",
    "ConditionTypeDef",
    "ConsumedCapacityTypeDef",
    "ContinuousBackupsDescriptionTypeDef",
    "ContributorInsightsSummaryTypeDef",
    "CreateBackupInputTypeDef",
    "CreateBackupOutputResponseTypeDef",
    "CreateGlobalSecondaryIndexActionTypeDef",
    "CreateGlobalTableInputTypeDef",
    "CreateGlobalTableOutputResponseTypeDef",
    "CreateReplicaActionTypeDef",
    "CreateReplicationGroupMemberActionTypeDef",
    "CreateTableInputServiceResourceTypeDef",
    "CreateTableInputTypeDef",
    "CreateTableOutputResponseTypeDef",
    "DeleteBackupInputTypeDef",
    "DeleteBackupOutputResponseTypeDef",
    "DeleteGlobalSecondaryIndexActionTypeDef",
    "DeleteItemInputTableTypeDef",
    "DeleteItemInputTypeDef",
    "DeleteItemOutputResponseTypeDef",
    "DeleteReplicaActionTypeDef",
    "DeleteReplicationGroupMemberActionTypeDef",
    "DeleteRequestTypeDef",
    "DeleteTableInputTypeDef",
    "DeleteTableOutputResponseTypeDef",
    "DeleteTypeDef",
    "DescribeBackupInputTypeDef",
    "DescribeBackupOutputResponseTypeDef",
    "DescribeContinuousBackupsInputTypeDef",
    "DescribeContinuousBackupsOutputResponseTypeDef",
    "DescribeContributorInsightsInputTypeDef",
    "DescribeContributorInsightsOutputResponseTypeDef",
    "DescribeEndpointsResponseResponseTypeDef",
    "DescribeExportInputTypeDef",
    "DescribeExportOutputResponseTypeDef",
    "DescribeGlobalTableInputTypeDef",
    "DescribeGlobalTableOutputResponseTypeDef",
    "DescribeGlobalTableSettingsInputTypeDef",
    "DescribeGlobalTableSettingsOutputResponseTypeDef",
    "DescribeKinesisStreamingDestinationInputTypeDef",
    "DescribeKinesisStreamingDestinationOutputResponseTypeDef",
    "DescribeLimitsOutputResponseTypeDef",
    "DescribeTableInputTypeDef",
    "DescribeTableOutputResponseTypeDef",
    "DescribeTableReplicaAutoScalingInputTypeDef",
    "DescribeTableReplicaAutoScalingOutputResponseTypeDef",
    "DescribeTimeToLiveInputTypeDef",
    "DescribeTimeToLiveOutputResponseTypeDef",
    "EndpointTypeDef",
    "ExecuteStatementInputTypeDef",
    "ExecuteStatementOutputResponseTypeDef",
    "ExecuteTransactionInputTypeDef",
    "ExecuteTransactionOutputResponseTypeDef",
    "ExpectedAttributeValueTypeDef",
    "ExportDescriptionTypeDef",
    "ExportSummaryTypeDef",
    "ExportTableToPointInTimeInputTypeDef",
    "ExportTableToPointInTimeOutputResponseTypeDef",
    "FailureExceptionTypeDef",
    "GetItemInputTableTypeDef",
    "GetItemInputTypeDef",
    "GetItemOutputResponseTypeDef",
    "GetTypeDef",
    "GlobalSecondaryIndexAutoScalingUpdateTypeDef",
    "GlobalSecondaryIndexDescriptionTypeDef",
    "GlobalSecondaryIndexInfoTypeDef",
    "GlobalSecondaryIndexTypeDef",
    "GlobalSecondaryIndexUpdateTypeDef",
    "GlobalTableDescriptionTypeDef",
    "GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    "GlobalTableTypeDef",
    "ItemCollectionMetricsTypeDef",
    "ItemResponseTypeDef",
    "KeySchemaElementTypeDef",
    "KeysAndAttributesTypeDef",
    "KinesisDataStreamDestinationTypeDef",
    "KinesisStreamingDestinationInputTypeDef",
    "KinesisStreamingDestinationOutputResponseTypeDef",
    "ListBackupsInputTypeDef",
    "ListBackupsOutputResponseTypeDef",
    "ListContributorInsightsInputTypeDef",
    "ListContributorInsightsOutputResponseTypeDef",
    "ListExportsInputTypeDef",
    "ListExportsOutputResponseTypeDef",
    "ListGlobalTablesInputTypeDef",
    "ListGlobalTablesOutputResponseTypeDef",
    "ListTablesInputTypeDef",
    "ListTablesOutputResponseTypeDef",
    "ListTagsOfResourceInputTypeDef",
    "ListTagsOfResourceOutputResponseTypeDef",
    "LocalSecondaryIndexDescriptionTypeDef",
    "LocalSecondaryIndexInfoTypeDef",
    "LocalSecondaryIndexTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterizedStatementTypeDef",
    "PointInTimeRecoveryDescriptionTypeDef",
    "PointInTimeRecoverySpecificationTypeDef",
    "ProjectionTypeDef",
    "ProvisionedThroughputDescriptionTypeDef",
    "ProvisionedThroughputOverrideTypeDef",
    "ProvisionedThroughputTypeDef",
    "PutItemInputTableTypeDef",
    "PutItemInputTypeDef",
    "PutItemOutputResponseTypeDef",
    "PutRequestTypeDef",
    "PutTypeDef",
    "QueryInputTableTypeDef",
    "QueryInputTypeDef",
    "QueryOutputResponseTypeDef",
    "ReplicaAutoScalingDescriptionTypeDef",
    "ReplicaAutoScalingUpdateTypeDef",
    "ReplicaDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef",
    "ReplicaGlobalSecondaryIndexDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    "ReplicaGlobalSecondaryIndexTypeDef",
    "ReplicaSettingsDescriptionTypeDef",
    "ReplicaSettingsUpdateTypeDef",
    "ReplicaTypeDef",
    "ReplicaUpdateTypeDef",
    "ReplicationGroupUpdateTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreSummaryTypeDef",
    "RestoreTableFromBackupInputTypeDef",
    "RestoreTableFromBackupOutputResponseTypeDef",
    "RestoreTableToPointInTimeInputTypeDef",
    "RestoreTableToPointInTimeOutputResponseTypeDef",
    "SSEDescriptionTypeDef",
    "SSESpecificationTypeDef",
    "ScanInputTableTypeDef",
    "ScanInputTypeDef",
    "ScanOutputResponseTypeDef",
    "ServiceResourceTableRequestTypeDef",
    "SourceTableDetailsTypeDef",
    "SourceTableFeatureDetailsTypeDef",
    "StreamSpecificationTypeDef",
    "TableAutoScalingDescriptionTypeDef",
    "TableBatchWriterRequestTypeDef",
    "TableDescriptionTypeDef",
    "TagResourceInputTypeDef",
    "TagTypeDef",
    "TimeToLiveDescriptionTypeDef",
    "TimeToLiveSpecificationTypeDef",
    "TransactGetItemTypeDef",
    "TransactGetItemsInputTypeDef",
    "TransactGetItemsOutputResponseTypeDef",
    "TransactWriteItemTypeDef",
    "TransactWriteItemsInputTypeDef",
    "TransactWriteItemsOutputResponseTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateContinuousBackupsInputTypeDef",
    "UpdateContinuousBackupsOutputResponseTypeDef",
    "UpdateContributorInsightsInputTypeDef",
    "UpdateContributorInsightsOutputResponseTypeDef",
    "UpdateGlobalSecondaryIndexActionTypeDef",
    "UpdateGlobalTableInputTypeDef",
    "UpdateGlobalTableOutputResponseTypeDef",
    "UpdateGlobalTableSettingsInputTypeDef",
    "UpdateGlobalTableSettingsOutputResponseTypeDef",
    "UpdateItemInputTableTypeDef",
    "UpdateItemInputTypeDef",
    "UpdateItemOutputResponseTypeDef",
    "UpdateReplicationGroupMemberActionTypeDef",
    "UpdateTableInputTableTypeDef",
    "UpdateTableInputTypeDef",
    "UpdateTableOutputResponseTypeDef",
    "UpdateTableReplicaAutoScalingInputTypeDef",
    "UpdateTableReplicaAutoScalingOutputResponseTypeDef",
    "UpdateTimeToLiveInputTypeDef",
    "UpdateTimeToLiveOutputResponseTypeDef",
    "UpdateTypeDef",
    "WaiterConfigTypeDef",
    "WriteRequestTypeDef",
)

ArchivalSummaryTypeDef = TypedDict(
    "ArchivalSummaryTypeDef",
    {
        "ArchivalDateTime": datetime,
        "ArchivalReason": str,
        "ArchivalBackupArn": str,
    },
    total=False,
)

AttributeDefinitionTypeDef = TypedDict(
    "AttributeDefinitionTypeDef",
    {
        "AttributeName": str,
        "AttributeType": ScalarAttributeTypeType,
    },
)

AttributeValueUpdateTypeDef = TypedDict(
    "AttributeValueUpdateTypeDef",
    {
        "Value": Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
        "Action": AttributeActionType,
    },
    total=False,
)

AutoScalingPolicyDescriptionTypeDef = TypedDict(
    "AutoScalingPolicyDescriptionTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": "AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    },
    total=False,
)

_RequiredAutoScalingPolicyUpdateTypeDef = TypedDict(
    "_RequiredAutoScalingPolicyUpdateTypeDef",
    {
        "TargetTrackingScalingPolicyConfiguration": "AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    },
)
_OptionalAutoScalingPolicyUpdateTypeDef = TypedDict(
    "_OptionalAutoScalingPolicyUpdateTypeDef",
    {
        "PolicyName": str,
    },
    total=False,
)


class AutoScalingPolicyUpdateTypeDef(
    _RequiredAutoScalingPolicyUpdateTypeDef, _OptionalAutoScalingPolicyUpdateTypeDef
):
    pass


AutoScalingSettingsDescriptionTypeDef = TypedDict(
    "AutoScalingSettingsDescriptionTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List["AutoScalingPolicyDescriptionTypeDef"],
    },
    total=False,
)

AutoScalingSettingsUpdateTypeDef = TypedDict(
    "AutoScalingSettingsUpdateTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicyUpdate": "AutoScalingPolicyUpdateTypeDef",
    },
    total=False,
)

_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef = TypedDict(
    "_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    {
        "TargetValue": float,
    },
)
_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef = TypedDict(
    "_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    {
        "DisableScaleIn": bool,
        "ScaleInCooldown": int,
        "ScaleOutCooldown": int,
    },
    total=False,
)


class AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef(
    _RequiredAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef,
    _OptionalAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef,
):
    pass


_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef = TypedDict(
    "_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    {
        "TargetValue": float,
    },
)
_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef = TypedDict(
    "_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    {
        "DisableScaleIn": bool,
        "ScaleInCooldown": int,
        "ScaleOutCooldown": int,
    },
    total=False,
)


class AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef(
    _RequiredAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef,
    _OptionalAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef,
):
    pass


BackupDescriptionTypeDef = TypedDict(
    "BackupDescriptionTypeDef",
    {
        "BackupDetails": "BackupDetailsTypeDef",
        "SourceTableDetails": "SourceTableDetailsTypeDef",
        "SourceTableFeatureDetails": "SourceTableFeatureDetailsTypeDef",
    },
    total=False,
)

_RequiredBackupDetailsTypeDef = TypedDict(
    "_RequiredBackupDetailsTypeDef",
    {
        "BackupArn": str,
        "BackupName": str,
        "BackupStatus": BackupStatusType,
        "BackupType": BackupTypeType,
        "BackupCreationDateTime": datetime,
    },
)
_OptionalBackupDetailsTypeDef = TypedDict(
    "_OptionalBackupDetailsTypeDef",
    {
        "BackupSizeBytes": int,
        "BackupExpiryDateTime": datetime,
    },
    total=False,
)


class BackupDetailsTypeDef(_RequiredBackupDetailsTypeDef, _OptionalBackupDetailsTypeDef):
    pass


BackupSummaryTypeDef = TypedDict(
    "BackupSummaryTypeDef",
    {
        "TableName": str,
        "TableId": str,
        "TableArn": str,
        "BackupArn": str,
        "BackupName": str,
        "BackupCreationDateTime": datetime,
        "BackupExpiryDateTime": datetime,
        "BackupStatus": BackupStatusType,
        "BackupType": BackupTypeType,
        "BackupSizeBytes": int,
    },
    total=False,
)

BatchExecuteStatementInputTypeDef = TypedDict(
    "BatchExecuteStatementInputTypeDef",
    {
        "Statements": List["BatchStatementRequestTypeDef"],
    },
)

BatchExecuteStatementOutputResponseTypeDef = TypedDict(
    "BatchExecuteStatementOutputResponseTypeDef",
    {
        "Responses": List["BatchStatementResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchGetItemInputServiceResourceTypeDef = TypedDict(
    "_RequiredBatchGetItemInputServiceResourceTypeDef",
    {
        "RequestItems": Dict[str, "KeysAndAttributesTypeDef"],
    },
)
_OptionalBatchGetItemInputServiceResourceTypeDef = TypedDict(
    "_OptionalBatchGetItemInputServiceResourceTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
    },
    total=False,
)


class BatchGetItemInputServiceResourceTypeDef(
    _RequiredBatchGetItemInputServiceResourceTypeDef,
    _OptionalBatchGetItemInputServiceResourceTypeDef,
):
    pass


_RequiredBatchGetItemInputTypeDef = TypedDict(
    "_RequiredBatchGetItemInputTypeDef",
    {
        "RequestItems": Dict[str, "KeysAndAttributesTypeDef"],
    },
)
_OptionalBatchGetItemInputTypeDef = TypedDict(
    "_OptionalBatchGetItemInputTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
    },
    total=False,
)


class BatchGetItemInputTypeDef(
    _RequiredBatchGetItemInputTypeDef, _OptionalBatchGetItemInputTypeDef
):
    pass


BatchGetItemOutputResponseTypeDef = TypedDict(
    "BatchGetItemOutputResponseTypeDef",
    {
        "Responses": Dict[
            str,
            List[
                Dict[
                    str,
                    Union[
                        bytes,
                        bytearray,
                        str,
                        int,
                        Decimal,
                        bool,
                        Set[int],
                        Set[Decimal],
                        Set[str],
                        Set[bytes],
                        Set[bytearray],
                        List[Any],
                        Dict[str, Any],
                        None,
                    ],
                ]
            ],
        ],
        "UnprocessedKeys": Dict[str, "KeysAndAttributesTypeDef"],
        "ConsumedCapacity": List["ConsumedCapacityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchStatementErrorTypeDef = TypedDict(
    "BatchStatementErrorTypeDef",
    {
        "Code": BatchStatementErrorCodeEnumType,
        "Message": str,
    },
    total=False,
)

_RequiredBatchStatementRequestTypeDef = TypedDict(
    "_RequiredBatchStatementRequestTypeDef",
    {
        "Statement": str,
    },
)
_OptionalBatchStatementRequestTypeDef = TypedDict(
    "_OptionalBatchStatementRequestTypeDef",
    {
        "Parameters": List[
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ]
        ],
        "ConsistentRead": bool,
    },
    total=False,
)


class BatchStatementRequestTypeDef(
    _RequiredBatchStatementRequestTypeDef, _OptionalBatchStatementRequestTypeDef
):
    pass


BatchStatementResponseTypeDef = TypedDict(
    "BatchStatementResponseTypeDef",
    {
        "Error": "BatchStatementErrorTypeDef",
        "TableName": str,
        "Item": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)

_RequiredBatchWriteItemInputServiceResourceTypeDef = TypedDict(
    "_RequiredBatchWriteItemInputServiceResourceTypeDef",
    {
        "RequestItems": Dict[str, List["WriteRequestTypeDef"]],
    },
)
_OptionalBatchWriteItemInputServiceResourceTypeDef = TypedDict(
    "_OptionalBatchWriteItemInputServiceResourceTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
    },
    total=False,
)


class BatchWriteItemInputServiceResourceTypeDef(
    _RequiredBatchWriteItemInputServiceResourceTypeDef,
    _OptionalBatchWriteItemInputServiceResourceTypeDef,
):
    pass


_RequiredBatchWriteItemInputTypeDef = TypedDict(
    "_RequiredBatchWriteItemInputTypeDef",
    {
        "RequestItems": Dict[str, List["WriteRequestTypeDef"]],
    },
)
_OptionalBatchWriteItemInputTypeDef = TypedDict(
    "_OptionalBatchWriteItemInputTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
    },
    total=False,
)


class BatchWriteItemInputTypeDef(
    _RequiredBatchWriteItemInputTypeDef, _OptionalBatchWriteItemInputTypeDef
):
    pass


BatchWriteItemOutputResponseTypeDef = TypedDict(
    "BatchWriteItemOutputResponseTypeDef",
    {
        "UnprocessedItems": Dict[str, List["WriteRequestTypeDef"]],
        "ItemCollectionMetrics": Dict[str, List["ItemCollectionMetricsTypeDef"]],
        "ConsumedCapacity": List["ConsumedCapacityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BillingModeSummaryTypeDef = TypedDict(
    "BillingModeSummaryTypeDef",
    {
        "BillingMode": BillingModeType,
        "LastUpdateToPayPerRequestDateTime": datetime,
    },
    total=False,
)

CapacityTypeDef = TypedDict(
    "CapacityTypeDef",
    {
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "CapacityUnits": float,
    },
    total=False,
)

_RequiredConditionCheckTypeDef = TypedDict(
    "_RequiredConditionCheckTypeDef",
    {
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "TableName": str,
        "ConditionExpression": str,
    },
)
_OptionalConditionCheckTypeDef = TypedDict(
    "_OptionalConditionCheckTypeDef",
    {
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)


class ConditionCheckTypeDef(_RequiredConditionCheckTypeDef, _OptionalConditionCheckTypeDef):
    pass


_RequiredConditionTypeDef = TypedDict(
    "_RequiredConditionTypeDef",
    {
        "ComparisonOperator": ComparisonOperatorType,
    },
)
_OptionalConditionTypeDef = TypedDict(
    "_OptionalConditionTypeDef",
    {
        "AttributeValueList": List[
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ]
        ],
    },
    total=False,
)


class ConditionTypeDef(_RequiredConditionTypeDef, _OptionalConditionTypeDef):
    pass


ConsumedCapacityTypeDef = TypedDict(
    "ConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": "CapacityTypeDef",
        "LocalSecondaryIndexes": Dict[str, "CapacityTypeDef"],
        "GlobalSecondaryIndexes": Dict[str, "CapacityTypeDef"],
    },
    total=False,
)

_RequiredContinuousBackupsDescriptionTypeDef = TypedDict(
    "_RequiredContinuousBackupsDescriptionTypeDef",
    {
        "ContinuousBackupsStatus": ContinuousBackupsStatusType,
    },
)
_OptionalContinuousBackupsDescriptionTypeDef = TypedDict(
    "_OptionalContinuousBackupsDescriptionTypeDef",
    {
        "PointInTimeRecoveryDescription": "PointInTimeRecoveryDescriptionTypeDef",
    },
    total=False,
)


class ContinuousBackupsDescriptionTypeDef(
    _RequiredContinuousBackupsDescriptionTypeDef, _OptionalContinuousBackupsDescriptionTypeDef
):
    pass


ContributorInsightsSummaryTypeDef = TypedDict(
    "ContributorInsightsSummaryTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsStatus": ContributorInsightsStatusType,
    },
    total=False,
)

CreateBackupInputTypeDef = TypedDict(
    "CreateBackupInputTypeDef",
    {
        "TableName": str,
        "BackupName": str,
    },
)

CreateBackupOutputResponseTypeDef = TypedDict(
    "CreateBackupOutputResponseTypeDef",
    {
        "BackupDetails": "BackupDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGlobalSecondaryIndexActionTypeDef = TypedDict(
    "_RequiredCreateGlobalSecondaryIndexActionTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
    },
)
_OptionalCreateGlobalSecondaryIndexActionTypeDef = TypedDict(
    "_OptionalCreateGlobalSecondaryIndexActionTypeDef",
    {
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
    },
    total=False,
)


class CreateGlobalSecondaryIndexActionTypeDef(
    _RequiredCreateGlobalSecondaryIndexActionTypeDef,
    _OptionalCreateGlobalSecondaryIndexActionTypeDef,
):
    pass


CreateGlobalTableInputTypeDef = TypedDict(
    "CreateGlobalTableInputTypeDef",
    {
        "GlobalTableName": str,
        "ReplicationGroup": List["ReplicaTypeDef"],
    },
)

CreateGlobalTableOutputResponseTypeDef = TypedDict(
    "CreateGlobalTableOutputResponseTypeDef",
    {
        "GlobalTableDescription": "GlobalTableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateReplicaActionTypeDef = TypedDict(
    "CreateReplicaActionTypeDef",
    {
        "RegionName": str,
    },
)

_RequiredCreateReplicationGroupMemberActionTypeDef = TypedDict(
    "_RequiredCreateReplicationGroupMemberActionTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalCreateReplicationGroupMemberActionTypeDef = TypedDict(
    "_OptionalCreateReplicationGroupMemberActionTypeDef",
    {
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": "ProvisionedThroughputOverrideTypeDef",
        "GlobalSecondaryIndexes": List["ReplicaGlobalSecondaryIndexTypeDef"],
    },
    total=False,
)


class CreateReplicationGroupMemberActionTypeDef(
    _RequiredCreateReplicationGroupMemberActionTypeDef,
    _OptionalCreateReplicationGroupMemberActionTypeDef,
):
    pass


_RequiredCreateTableInputServiceResourceTypeDef = TypedDict(
    "_RequiredCreateTableInputServiceResourceTypeDef",
    {
        "AttributeDefinitions": List["AttributeDefinitionTypeDef"],
        "TableName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
    },
)
_OptionalCreateTableInputServiceResourceTypeDef = TypedDict(
    "_OptionalCreateTableInputServiceResourceTypeDef",
    {
        "LocalSecondaryIndexes": List["LocalSecondaryIndexTypeDef"],
        "GlobalSecondaryIndexes": List["GlobalSecondaryIndexTypeDef"],
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
        "StreamSpecification": "StreamSpecificationTypeDef",
        "SSESpecification": "SSESpecificationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateTableInputServiceResourceTypeDef(
    _RequiredCreateTableInputServiceResourceTypeDef, _OptionalCreateTableInputServiceResourceTypeDef
):
    pass


_RequiredCreateTableInputTypeDef = TypedDict(
    "_RequiredCreateTableInputTypeDef",
    {
        "AttributeDefinitions": List["AttributeDefinitionTypeDef"],
        "TableName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
    },
)
_OptionalCreateTableInputTypeDef = TypedDict(
    "_OptionalCreateTableInputTypeDef",
    {
        "LocalSecondaryIndexes": List["LocalSecondaryIndexTypeDef"],
        "GlobalSecondaryIndexes": List["GlobalSecondaryIndexTypeDef"],
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
        "StreamSpecification": "StreamSpecificationTypeDef",
        "SSESpecification": "SSESpecificationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateTableInputTypeDef(_RequiredCreateTableInputTypeDef, _OptionalCreateTableInputTypeDef):
    pass


CreateTableOutputResponseTypeDef = TypedDict(
    "CreateTableOutputResponseTypeDef",
    {
        "TableDescription": "TableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackupInputTypeDef = TypedDict(
    "DeleteBackupInputTypeDef",
    {
        "BackupArn": str,
    },
)

DeleteBackupOutputResponseTypeDef = TypedDict(
    "DeleteBackupOutputResponseTypeDef",
    {
        "BackupDescription": "BackupDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGlobalSecondaryIndexActionTypeDef = TypedDict(
    "DeleteGlobalSecondaryIndexActionTypeDef",
    {
        "IndexName": str,
    },
)

_RequiredDeleteItemInputTableTypeDef = TypedDict(
    "_RequiredDeleteItemInputTableTypeDef",
    {
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)
_OptionalDeleteItemInputTableTypeDef = TypedDict(
    "_OptionalDeleteItemInputTableTypeDef",
    {
        "Expected": Dict[str, "ExpectedAttributeValueTypeDef"],
        "ConditionalOperator": ConditionalOperatorType,
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)


class DeleteItemInputTableTypeDef(
    _RequiredDeleteItemInputTableTypeDef, _OptionalDeleteItemInputTableTypeDef
):
    pass


_RequiredDeleteItemInputTypeDef = TypedDict(
    "_RequiredDeleteItemInputTypeDef",
    {
        "TableName": str,
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)
_OptionalDeleteItemInputTypeDef = TypedDict(
    "_OptionalDeleteItemInputTypeDef",
    {
        "Expected": Dict[str, "ExpectedAttributeValueTypeDef"],
        "ConditionalOperator": ConditionalOperatorType,
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)


class DeleteItemInputTypeDef(_RequiredDeleteItemInputTypeDef, _OptionalDeleteItemInputTypeDef):
    pass


DeleteItemOutputResponseTypeDef = TypedDict(
    "DeleteItemOutputResponseTypeDef",
    {
        "Attributes": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ItemCollectionMetrics": "ItemCollectionMetricsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReplicaActionTypeDef = TypedDict(
    "DeleteReplicaActionTypeDef",
    {
        "RegionName": str,
    },
)

DeleteReplicationGroupMemberActionTypeDef = TypedDict(
    "DeleteReplicationGroupMemberActionTypeDef",
    {
        "RegionName": str,
    },
)

DeleteRequestTypeDef = TypedDict(
    "DeleteRequestTypeDef",
    {
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)

DeleteTableInputTypeDef = TypedDict(
    "DeleteTableInputTypeDef",
    {
        "TableName": str,
    },
)

DeleteTableOutputResponseTypeDef = TypedDict(
    "DeleteTableOutputResponseTypeDef",
    {
        "TableDescription": "TableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTypeDef = TypedDict(
    "_RequiredDeleteTypeDef",
    {
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "TableName": str,
    },
)
_OptionalDeleteTypeDef = TypedDict(
    "_OptionalDeleteTypeDef",
    {
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)


class DeleteTypeDef(_RequiredDeleteTypeDef, _OptionalDeleteTypeDef):
    pass


DescribeBackupInputTypeDef = TypedDict(
    "DescribeBackupInputTypeDef",
    {
        "BackupArn": str,
    },
)

DescribeBackupOutputResponseTypeDef = TypedDict(
    "DescribeBackupOutputResponseTypeDef",
    {
        "BackupDescription": "BackupDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContinuousBackupsInputTypeDef = TypedDict(
    "DescribeContinuousBackupsInputTypeDef",
    {
        "TableName": str,
    },
)

DescribeContinuousBackupsOutputResponseTypeDef = TypedDict(
    "DescribeContinuousBackupsOutputResponseTypeDef",
    {
        "ContinuousBackupsDescription": "ContinuousBackupsDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeContributorInsightsInputTypeDef = TypedDict(
    "_RequiredDescribeContributorInsightsInputTypeDef",
    {
        "TableName": str,
    },
)
_OptionalDescribeContributorInsightsInputTypeDef = TypedDict(
    "_OptionalDescribeContributorInsightsInputTypeDef",
    {
        "IndexName": str,
    },
    total=False,
)


class DescribeContributorInsightsInputTypeDef(
    _RequiredDescribeContributorInsightsInputTypeDef,
    _OptionalDescribeContributorInsightsInputTypeDef,
):
    pass


DescribeContributorInsightsOutputResponseTypeDef = TypedDict(
    "DescribeContributorInsightsOutputResponseTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsRuleList": List[str],
        "ContributorInsightsStatus": ContributorInsightsStatusType,
        "LastUpdateDateTime": datetime,
        "FailureException": "FailureExceptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointsResponseResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseResponseTypeDef",
    {
        "Endpoints": List["EndpointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportInputTypeDef = TypedDict(
    "DescribeExportInputTypeDef",
    {
        "ExportArn": str,
    },
)

DescribeExportOutputResponseTypeDef = TypedDict(
    "DescribeExportOutputResponseTypeDef",
    {
        "ExportDescription": "ExportDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGlobalTableInputTypeDef = TypedDict(
    "DescribeGlobalTableInputTypeDef",
    {
        "GlobalTableName": str,
    },
)

DescribeGlobalTableOutputResponseTypeDef = TypedDict(
    "DescribeGlobalTableOutputResponseTypeDef",
    {
        "GlobalTableDescription": "GlobalTableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGlobalTableSettingsInputTypeDef = TypedDict(
    "DescribeGlobalTableSettingsInputTypeDef",
    {
        "GlobalTableName": str,
    },
)

DescribeGlobalTableSettingsOutputResponseTypeDef = TypedDict(
    "DescribeGlobalTableSettingsOutputResponseTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaSettings": List["ReplicaSettingsDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeKinesisStreamingDestinationInputTypeDef = TypedDict(
    "DescribeKinesisStreamingDestinationInputTypeDef",
    {
        "TableName": str,
    },
)

DescribeKinesisStreamingDestinationOutputResponseTypeDef = TypedDict(
    "DescribeKinesisStreamingDestinationOutputResponseTypeDef",
    {
        "TableName": str,
        "KinesisDataStreamDestinations": List["KinesisDataStreamDestinationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLimitsOutputResponseTypeDef = TypedDict(
    "DescribeLimitsOutputResponseTypeDef",
    {
        "AccountMaxReadCapacityUnits": int,
        "AccountMaxWriteCapacityUnits": int,
        "TableMaxReadCapacityUnits": int,
        "TableMaxWriteCapacityUnits": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTableInputTypeDef = TypedDict(
    "DescribeTableInputTypeDef",
    {
        "TableName": str,
    },
)

DescribeTableOutputResponseTypeDef = TypedDict(
    "DescribeTableOutputResponseTypeDef",
    {
        "Table": "TableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTableReplicaAutoScalingInputTypeDef = TypedDict(
    "DescribeTableReplicaAutoScalingInputTypeDef",
    {
        "TableName": str,
    },
)

DescribeTableReplicaAutoScalingOutputResponseTypeDef = TypedDict(
    "DescribeTableReplicaAutoScalingOutputResponseTypeDef",
    {
        "TableAutoScalingDescription": "TableAutoScalingDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTimeToLiveInputTypeDef = TypedDict(
    "DescribeTimeToLiveInputTypeDef",
    {
        "TableName": str,
    },
)

DescribeTimeToLiveOutputResponseTypeDef = TypedDict(
    "DescribeTimeToLiveOutputResponseTypeDef",
    {
        "TimeToLiveDescription": "TimeToLiveDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "CachePeriodInMinutes": int,
    },
)

_RequiredExecuteStatementInputTypeDef = TypedDict(
    "_RequiredExecuteStatementInputTypeDef",
    {
        "Statement": str,
    },
)
_OptionalExecuteStatementInputTypeDef = TypedDict(
    "_OptionalExecuteStatementInputTypeDef",
    {
        "Parameters": List[
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ]
        ],
        "ConsistentRead": bool,
        "NextToken": str,
    },
    total=False,
)


class ExecuteStatementInputTypeDef(
    _RequiredExecuteStatementInputTypeDef, _OptionalExecuteStatementInputTypeDef
):
    pass


ExecuteStatementOutputResponseTypeDef = TypedDict(
    "ExecuteStatementOutputResponseTypeDef",
    {
        "Items": List[
            Dict[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    List[Any],
                    Dict[str, Any],
                    None,
                ],
            ]
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExecuteTransactionInputTypeDef = TypedDict(
    "_RequiredExecuteTransactionInputTypeDef",
    {
        "TransactStatements": List["ParameterizedStatementTypeDef"],
    },
)
_OptionalExecuteTransactionInputTypeDef = TypedDict(
    "_OptionalExecuteTransactionInputTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)


class ExecuteTransactionInputTypeDef(
    _RequiredExecuteTransactionInputTypeDef, _OptionalExecuteTransactionInputTypeDef
):
    pass


ExecuteTransactionOutputResponseTypeDef = TypedDict(
    "ExecuteTransactionOutputResponseTypeDef",
    {
        "Responses": List["ItemResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExpectedAttributeValueTypeDef = TypedDict(
    "ExpectedAttributeValueTypeDef",
    {
        "Value": Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
        "Exists": bool,
        "ComparisonOperator": ComparisonOperatorType,
        "AttributeValueList": List[
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ]
        ],
    },
    total=False,
)

ExportDescriptionTypeDef = TypedDict(
    "ExportDescriptionTypeDef",
    {
        "ExportArn": str,
        "ExportStatus": ExportStatusType,
        "StartTime": datetime,
        "EndTime": datetime,
        "ExportManifest": str,
        "TableArn": str,
        "TableId": str,
        "ExportTime": datetime,
        "ClientToken": str,
        "S3Bucket": str,
        "S3BucketOwner": str,
        "S3Prefix": str,
        "S3SseAlgorithm": S3SseAlgorithmType,
        "S3SseKmsKeyId": str,
        "FailureCode": str,
        "FailureMessage": str,
        "ExportFormat": ExportFormatType,
        "BilledSizeBytes": int,
        "ItemCount": int,
    },
    total=False,
)

ExportSummaryTypeDef = TypedDict(
    "ExportSummaryTypeDef",
    {
        "ExportArn": str,
        "ExportStatus": ExportStatusType,
    },
    total=False,
)

_RequiredExportTableToPointInTimeInputTypeDef = TypedDict(
    "_RequiredExportTableToPointInTimeInputTypeDef",
    {
        "TableArn": str,
        "S3Bucket": str,
    },
)
_OptionalExportTableToPointInTimeInputTypeDef = TypedDict(
    "_OptionalExportTableToPointInTimeInputTypeDef",
    {
        "ExportTime": Union[datetime, str],
        "ClientToken": str,
        "S3BucketOwner": str,
        "S3Prefix": str,
        "S3SseAlgorithm": S3SseAlgorithmType,
        "S3SseKmsKeyId": str,
        "ExportFormat": ExportFormatType,
    },
    total=False,
)


class ExportTableToPointInTimeInputTypeDef(
    _RequiredExportTableToPointInTimeInputTypeDef, _OptionalExportTableToPointInTimeInputTypeDef
):
    pass


ExportTableToPointInTimeOutputResponseTypeDef = TypedDict(
    "ExportTableToPointInTimeOutputResponseTypeDef",
    {
        "ExportDescription": "ExportDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailureExceptionTypeDef = TypedDict(
    "FailureExceptionTypeDef",
    {
        "ExceptionName": str,
        "ExceptionDescription": str,
    },
    total=False,
)

_RequiredGetItemInputTableTypeDef = TypedDict(
    "_RequiredGetItemInputTableTypeDef",
    {
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)
_OptionalGetItemInputTableTypeDef = TypedDict(
    "_OptionalGetItemInputTableTypeDef",
    {
        "AttributesToGet": List[str],
        "ConsistentRead": bool,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
    },
    total=False,
)


class GetItemInputTableTypeDef(
    _RequiredGetItemInputTableTypeDef, _OptionalGetItemInputTableTypeDef
):
    pass


_RequiredGetItemInputTypeDef = TypedDict(
    "_RequiredGetItemInputTypeDef",
    {
        "TableName": str,
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)
_OptionalGetItemInputTypeDef = TypedDict(
    "_OptionalGetItemInputTypeDef",
    {
        "AttributesToGet": List[str],
        "ConsistentRead": bool,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
    },
    total=False,
)


class GetItemInputTypeDef(_RequiredGetItemInputTypeDef, _OptionalGetItemInputTypeDef):
    pass


GetItemOutputResponseTypeDef = TypedDict(
    "GetItemOutputResponseTypeDef",
    {
        "Item": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTypeDef = TypedDict(
    "_RequiredGetTypeDef",
    {
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "TableName": str,
    },
)
_OptionalGetTypeDef = TypedDict(
    "_OptionalGetTypeDef",
    {
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
    },
    total=False,
)


class GetTypeDef(_RequiredGetTypeDef, _OptionalGetTypeDef):
    pass


GlobalSecondaryIndexAutoScalingUpdateTypeDef = TypedDict(
    "GlobalSecondaryIndexAutoScalingUpdateTypeDef",
    {
        "IndexName": str,
        "ProvisionedWriteCapacityAutoScalingUpdate": "AutoScalingSettingsUpdateTypeDef",
    },
    total=False,
)

GlobalSecondaryIndexDescriptionTypeDef = TypedDict(
    "GlobalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
        "IndexStatus": IndexStatusType,
        "Backfilling": bool,
        "ProvisionedThroughput": "ProvisionedThroughputDescriptionTypeDef",
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

GlobalSecondaryIndexInfoTypeDef = TypedDict(
    "GlobalSecondaryIndexInfoTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
    },
    total=False,
)

_RequiredGlobalSecondaryIndexTypeDef = TypedDict(
    "_RequiredGlobalSecondaryIndexTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
    },
)
_OptionalGlobalSecondaryIndexTypeDef = TypedDict(
    "_OptionalGlobalSecondaryIndexTypeDef",
    {
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
    },
    total=False,
)


class GlobalSecondaryIndexTypeDef(
    _RequiredGlobalSecondaryIndexTypeDef, _OptionalGlobalSecondaryIndexTypeDef
):
    pass


GlobalSecondaryIndexUpdateTypeDef = TypedDict(
    "GlobalSecondaryIndexUpdateTypeDef",
    {
        "Update": "UpdateGlobalSecondaryIndexActionTypeDef",
        "Create": "CreateGlobalSecondaryIndexActionTypeDef",
        "Delete": "DeleteGlobalSecondaryIndexActionTypeDef",
    },
    total=False,
)

GlobalTableDescriptionTypeDef = TypedDict(
    "GlobalTableDescriptionTypeDef",
    {
        "ReplicationGroup": List["ReplicaDescriptionTypeDef"],
        "GlobalTableArn": str,
        "CreationDateTime": datetime,
        "GlobalTableStatus": GlobalTableStatusType,
        "GlobalTableName": str,
    },
    total=False,
)

_RequiredGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_RequiredGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "IndexName": str,
    },
)
_OptionalGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_OptionalGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "ProvisionedWriteCapacityUnits": int,
        "ProvisionedWriteCapacityAutoScalingSettingsUpdate": "AutoScalingSettingsUpdateTypeDef",
    },
    total=False,
)


class GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef(
    _RequiredGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef,
    _OptionalGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef,
):
    pass


GlobalTableTypeDef = TypedDict(
    "GlobalTableTypeDef",
    {
        "GlobalTableName": str,
        "ReplicationGroup": List["ReplicaTypeDef"],
    },
    total=False,
)

ItemCollectionMetricsTypeDef = TypedDict(
    "ItemCollectionMetricsTypeDef",
    {
        "ItemCollectionKey": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "SizeEstimateRangeGB": List[float],
    },
    total=False,
)

ItemResponseTypeDef = TypedDict(
    "ItemResponseTypeDef",
    {
        "Item": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)

KeySchemaElementTypeDef = TypedDict(
    "KeySchemaElementTypeDef",
    {
        "AttributeName": str,
        "KeyType": KeyTypeType,
    },
)

_RequiredKeysAndAttributesTypeDef = TypedDict(
    "_RequiredKeysAndAttributesTypeDef",
    {
        "Keys": List[
            Dict[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    List[Any],
                    Dict[str, Any],
                    None,
                ],
            ]
        ],
    },
)
_OptionalKeysAndAttributesTypeDef = TypedDict(
    "_OptionalKeysAndAttributesTypeDef",
    {
        "AttributesToGet": List[str],
        "ConsistentRead": bool,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
    },
    total=False,
)


class KeysAndAttributesTypeDef(
    _RequiredKeysAndAttributesTypeDef, _OptionalKeysAndAttributesTypeDef
):
    pass


KinesisDataStreamDestinationTypeDef = TypedDict(
    "KinesisDataStreamDestinationTypeDef",
    {
        "StreamArn": str,
        "DestinationStatus": DestinationStatusType,
        "DestinationStatusDescription": str,
    },
    total=False,
)

KinesisStreamingDestinationInputTypeDef = TypedDict(
    "KinesisStreamingDestinationInputTypeDef",
    {
        "TableName": str,
        "StreamArn": str,
    },
)

KinesisStreamingDestinationOutputResponseTypeDef = TypedDict(
    "KinesisStreamingDestinationOutputResponseTypeDef",
    {
        "TableName": str,
        "StreamArn": str,
        "DestinationStatus": DestinationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackupsInputTypeDef = TypedDict(
    "ListBackupsInputTypeDef",
    {
        "TableName": str,
        "Limit": int,
        "TimeRangeLowerBound": Union[datetime, str],
        "TimeRangeUpperBound": Union[datetime, str],
        "ExclusiveStartBackupArn": str,
        "BackupType": BackupTypeFilterType,
    },
    total=False,
)

ListBackupsOutputResponseTypeDef = TypedDict(
    "ListBackupsOutputResponseTypeDef",
    {
        "BackupSummaries": List["BackupSummaryTypeDef"],
        "LastEvaluatedBackupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContributorInsightsInputTypeDef = TypedDict(
    "ListContributorInsightsInputTypeDef",
    {
        "TableName": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListContributorInsightsOutputResponseTypeDef = TypedDict(
    "ListContributorInsightsOutputResponseTypeDef",
    {
        "ContributorInsightsSummaries": List["ContributorInsightsSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExportsInputTypeDef = TypedDict(
    "ListExportsInputTypeDef",
    {
        "TableArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListExportsOutputResponseTypeDef = TypedDict(
    "ListExportsOutputResponseTypeDef",
    {
        "ExportSummaries": List["ExportSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGlobalTablesInputTypeDef = TypedDict(
    "ListGlobalTablesInputTypeDef",
    {
        "ExclusiveStartGlobalTableName": str,
        "Limit": int,
        "RegionName": str,
    },
    total=False,
)

ListGlobalTablesOutputResponseTypeDef = TypedDict(
    "ListGlobalTablesOutputResponseTypeDef",
    {
        "GlobalTables": List["GlobalTableTypeDef"],
        "LastEvaluatedGlobalTableName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTablesInputTypeDef = TypedDict(
    "ListTablesInputTypeDef",
    {
        "ExclusiveStartTableName": str,
        "Limit": int,
    },
    total=False,
)

ListTablesOutputResponseTypeDef = TypedDict(
    "ListTablesOutputResponseTypeDef",
    {
        "TableNames": List[str],
        "LastEvaluatedTableName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsOfResourceInputTypeDef = TypedDict(
    "_RequiredListTagsOfResourceInputTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsOfResourceInputTypeDef = TypedDict(
    "_OptionalListTagsOfResourceInputTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListTagsOfResourceInputTypeDef(
    _RequiredListTagsOfResourceInputTypeDef, _OptionalListTagsOfResourceInputTypeDef
):
    pass


ListTagsOfResourceOutputResponseTypeDef = TypedDict(
    "ListTagsOfResourceOutputResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocalSecondaryIndexDescriptionTypeDef = TypedDict(
    "LocalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

LocalSecondaryIndexInfoTypeDef = TypedDict(
    "LocalSecondaryIndexInfoTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
    },
    total=False,
)

LocalSecondaryIndexTypeDef = TypedDict(
    "LocalSecondaryIndexTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
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

_RequiredParameterizedStatementTypeDef = TypedDict(
    "_RequiredParameterizedStatementTypeDef",
    {
        "Statement": str,
    },
)
_OptionalParameterizedStatementTypeDef = TypedDict(
    "_OptionalParameterizedStatementTypeDef",
    {
        "Parameters": List[
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ]
        ],
    },
    total=False,
)


class ParameterizedStatementTypeDef(
    _RequiredParameterizedStatementTypeDef, _OptionalParameterizedStatementTypeDef
):
    pass


PointInTimeRecoveryDescriptionTypeDef = TypedDict(
    "PointInTimeRecoveryDescriptionTypeDef",
    {
        "PointInTimeRecoveryStatus": PointInTimeRecoveryStatusType,
        "EarliestRestorableDateTime": datetime,
        "LatestRestorableDateTime": datetime,
    },
    total=False,
)

PointInTimeRecoverySpecificationTypeDef = TypedDict(
    "PointInTimeRecoverySpecificationTypeDef",
    {
        "PointInTimeRecoveryEnabled": bool,
    },
)

ProjectionTypeDef = TypedDict(
    "ProjectionTypeDef",
    {
        "ProjectionType": ProjectionTypeType,
        "NonKeyAttributes": List[str],
    },
    total=False,
)

ProvisionedThroughputDescriptionTypeDef = TypedDict(
    "ProvisionedThroughputDescriptionTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

ProvisionedThroughputOverrideTypeDef = TypedDict(
    "ProvisionedThroughputOverrideTypeDef",
    {
        "ReadCapacityUnits": int,
    },
    total=False,
)

ProvisionedThroughputTypeDef = TypedDict(
    "ProvisionedThroughputTypeDef",
    {
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
)

_RequiredPutItemInputTableTypeDef = TypedDict(
    "_RequiredPutItemInputTableTypeDef",
    {
        "Item": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)
_OptionalPutItemInputTableTypeDef = TypedDict(
    "_OptionalPutItemInputTableTypeDef",
    {
        "Expected": Dict[str, "ExpectedAttributeValueTypeDef"],
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ConditionalOperator": ConditionalOperatorType,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)


class PutItemInputTableTypeDef(
    _RequiredPutItemInputTableTypeDef, _OptionalPutItemInputTableTypeDef
):
    pass


_RequiredPutItemInputTypeDef = TypedDict(
    "_RequiredPutItemInputTypeDef",
    {
        "TableName": str,
        "Item": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)
_OptionalPutItemInputTypeDef = TypedDict(
    "_OptionalPutItemInputTypeDef",
    {
        "Expected": Dict[str, "ExpectedAttributeValueTypeDef"],
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ConditionalOperator": ConditionalOperatorType,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)


class PutItemInputTypeDef(_RequiredPutItemInputTypeDef, _OptionalPutItemInputTypeDef):
    pass


PutItemOutputResponseTypeDef = TypedDict(
    "PutItemOutputResponseTypeDef",
    {
        "Attributes": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ItemCollectionMetrics": "ItemCollectionMetricsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRequestTypeDef = TypedDict(
    "PutRequestTypeDef",
    {
        "Item": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)

_RequiredPutTypeDef = TypedDict(
    "_RequiredPutTypeDef",
    {
        "Item": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "TableName": str,
    },
)
_OptionalPutTypeDef = TypedDict(
    "_OptionalPutTypeDef",
    {
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)


class PutTypeDef(_RequiredPutTypeDef, _OptionalPutTypeDef):
    pass


QueryInputTableTypeDef = TypedDict(
    "QueryInputTableTypeDef",
    {
        "IndexName": str,
        "Select": SelectType,
        "AttributesToGet": List[str],
        "Limit": int,
        "ConsistentRead": bool,
        "KeyConditions": Dict[str, "ConditionTypeDef"],
        "QueryFilter": Dict[str, "ConditionTypeDef"],
        "ConditionalOperator": ConditionalOperatorType,
        "ScanIndexForward": bool,
        "ExclusiveStartKey": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ProjectionExpression": str,
        "FilterExpression": Union[str, ConditionBase],
        "KeyConditionExpression": Union[str, ConditionBase],
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)

_RequiredQueryInputTypeDef = TypedDict(
    "_RequiredQueryInputTypeDef",
    {
        "TableName": str,
    },
)
_OptionalQueryInputTypeDef = TypedDict(
    "_OptionalQueryInputTypeDef",
    {
        "IndexName": str,
        "Select": SelectType,
        "AttributesToGet": List[str],
        "Limit": int,
        "ConsistentRead": bool,
        "KeyConditions": Dict[str, "ConditionTypeDef"],
        "QueryFilter": Dict[str, "ConditionTypeDef"],
        "ConditionalOperator": ConditionalOperatorType,
        "ScanIndexForward": bool,
        "ExclusiveStartKey": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ProjectionExpression": str,
        "FilterExpression": str,
        "KeyConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)


class QueryInputTypeDef(_RequiredQueryInputTypeDef, _OptionalQueryInputTypeDef):
    pass


QueryOutputResponseTypeDef = TypedDict(
    "QueryOutputResponseTypeDef",
    {
        "Items": List[
            Dict[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    List[Any],
                    Dict[str, Any],
                    None,
                ],
            ]
        ],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplicaAutoScalingDescriptionTypeDef = TypedDict(
    "ReplicaAutoScalingDescriptionTypeDef",
    {
        "RegionName": str,
        "GlobalSecondaryIndexes": List["ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef"],
        "ReplicaProvisionedReadCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
        "ReplicaProvisionedWriteCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
        "ReplicaStatus": ReplicaStatusType,
    },
    total=False,
)

_RequiredReplicaAutoScalingUpdateTypeDef = TypedDict(
    "_RequiredReplicaAutoScalingUpdateTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalReplicaAutoScalingUpdateTypeDef = TypedDict(
    "_OptionalReplicaAutoScalingUpdateTypeDef",
    {
        "ReplicaGlobalSecondaryIndexUpdates": List[
            "ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef"
        ],
        "ReplicaProvisionedReadCapacityAutoScalingUpdate": "AutoScalingSettingsUpdateTypeDef",
    },
    total=False,
)


class ReplicaAutoScalingUpdateTypeDef(
    _RequiredReplicaAutoScalingUpdateTypeDef, _OptionalReplicaAutoScalingUpdateTypeDef
):
    pass


ReplicaDescriptionTypeDef = TypedDict(
    "ReplicaDescriptionTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": ReplicaStatusType,
        "ReplicaStatusDescription": str,
        "ReplicaStatusPercentProgress": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": "ProvisionedThroughputOverrideTypeDef",
        "GlobalSecondaryIndexes": List["ReplicaGlobalSecondaryIndexDescriptionTypeDef"],
        "ReplicaInaccessibleDateTime": datetime,
    },
    total=False,
)

ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef",
    {
        "IndexName": str,
        "IndexStatus": IndexStatusType,
        "ProvisionedReadCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
        "ProvisionedWriteCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
    },
    total=False,
)

ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef",
    {
        "IndexName": str,
        "ProvisionedReadCapacityAutoScalingUpdate": "AutoScalingSettingsUpdateTypeDef",
    },
    total=False,
)

ReplicaGlobalSecondaryIndexDescriptionTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": "ProvisionedThroughputOverrideTypeDef",
    },
    total=False,
)

_RequiredReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef = TypedDict(
    "_RequiredReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef",
    {
        "IndexName": str,
    },
)
_OptionalReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef = TypedDict(
    "_OptionalReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef",
    {
        "IndexStatus": IndexStatusType,
        "ProvisionedReadCapacityUnits": int,
        "ProvisionedReadCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
        "ProvisionedWriteCapacityUnits": int,
        "ProvisionedWriteCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
    },
    total=False,
)


class ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef(
    _RequiredReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef,
    _OptionalReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef,
):
    pass


_RequiredReplicaGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_RequiredReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "IndexName": str,
    },
)
_OptionalReplicaGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_OptionalReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "ProvisionedReadCapacityUnits": int,
        "ProvisionedReadCapacityAutoScalingSettingsUpdate": "AutoScalingSettingsUpdateTypeDef",
    },
    total=False,
)


class ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef(
    _RequiredReplicaGlobalSecondaryIndexSettingsUpdateTypeDef,
    _OptionalReplicaGlobalSecondaryIndexSettingsUpdateTypeDef,
):
    pass


_RequiredReplicaGlobalSecondaryIndexTypeDef = TypedDict(
    "_RequiredReplicaGlobalSecondaryIndexTypeDef",
    {
        "IndexName": str,
    },
)
_OptionalReplicaGlobalSecondaryIndexTypeDef = TypedDict(
    "_OptionalReplicaGlobalSecondaryIndexTypeDef",
    {
        "ProvisionedThroughputOverride": "ProvisionedThroughputOverrideTypeDef",
    },
    total=False,
)


class ReplicaGlobalSecondaryIndexTypeDef(
    _RequiredReplicaGlobalSecondaryIndexTypeDef, _OptionalReplicaGlobalSecondaryIndexTypeDef
):
    pass


_RequiredReplicaSettingsDescriptionTypeDef = TypedDict(
    "_RequiredReplicaSettingsDescriptionTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalReplicaSettingsDescriptionTypeDef = TypedDict(
    "_OptionalReplicaSettingsDescriptionTypeDef",
    {
        "ReplicaStatus": ReplicaStatusType,
        "ReplicaBillingModeSummary": "BillingModeSummaryTypeDef",
        "ReplicaProvisionedReadCapacityUnits": int,
        "ReplicaProvisionedReadCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
        "ReplicaProvisionedWriteCapacityUnits": int,
        "ReplicaProvisionedWriteCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
        "ReplicaGlobalSecondaryIndexSettings": List[
            "ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef"
        ],
    },
    total=False,
)


class ReplicaSettingsDescriptionTypeDef(
    _RequiredReplicaSettingsDescriptionTypeDef, _OptionalReplicaSettingsDescriptionTypeDef
):
    pass


_RequiredReplicaSettingsUpdateTypeDef = TypedDict(
    "_RequiredReplicaSettingsUpdateTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalReplicaSettingsUpdateTypeDef = TypedDict(
    "_OptionalReplicaSettingsUpdateTypeDef",
    {
        "ReplicaProvisionedReadCapacityUnits": int,
        "ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate": "AutoScalingSettingsUpdateTypeDef",
        "ReplicaGlobalSecondaryIndexSettingsUpdate": List[
            "ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef"
        ],
    },
    total=False,
)


class ReplicaSettingsUpdateTypeDef(
    _RequiredReplicaSettingsUpdateTypeDef, _OptionalReplicaSettingsUpdateTypeDef
):
    pass


ReplicaTypeDef = TypedDict(
    "ReplicaTypeDef",
    {
        "RegionName": str,
    },
    total=False,
)

ReplicaUpdateTypeDef = TypedDict(
    "ReplicaUpdateTypeDef",
    {
        "Create": "CreateReplicaActionTypeDef",
        "Delete": "DeleteReplicaActionTypeDef",
    },
    total=False,
)

ReplicationGroupUpdateTypeDef = TypedDict(
    "ReplicationGroupUpdateTypeDef",
    {
        "Create": "CreateReplicationGroupMemberActionTypeDef",
        "Update": "UpdateReplicationGroupMemberActionTypeDef",
        "Delete": "DeleteReplicationGroupMemberActionTypeDef",
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

_RequiredRestoreSummaryTypeDef = TypedDict(
    "_RequiredRestoreSummaryTypeDef",
    {
        "RestoreDateTime": datetime,
        "RestoreInProgress": bool,
    },
)
_OptionalRestoreSummaryTypeDef = TypedDict(
    "_OptionalRestoreSummaryTypeDef",
    {
        "SourceBackupArn": str,
        "SourceTableArn": str,
    },
    total=False,
)


class RestoreSummaryTypeDef(_RequiredRestoreSummaryTypeDef, _OptionalRestoreSummaryTypeDef):
    pass


_RequiredRestoreTableFromBackupInputTypeDef = TypedDict(
    "_RequiredRestoreTableFromBackupInputTypeDef",
    {
        "TargetTableName": str,
        "BackupArn": str,
    },
)
_OptionalRestoreTableFromBackupInputTypeDef = TypedDict(
    "_OptionalRestoreTableFromBackupInputTypeDef",
    {
        "BillingModeOverride": BillingModeType,
        "GlobalSecondaryIndexOverride": List["GlobalSecondaryIndexTypeDef"],
        "LocalSecondaryIndexOverride": List["LocalSecondaryIndexTypeDef"],
        "ProvisionedThroughputOverride": "ProvisionedThroughputTypeDef",
        "SSESpecificationOverride": "SSESpecificationTypeDef",
    },
    total=False,
)


class RestoreTableFromBackupInputTypeDef(
    _RequiredRestoreTableFromBackupInputTypeDef, _OptionalRestoreTableFromBackupInputTypeDef
):
    pass


RestoreTableFromBackupOutputResponseTypeDef = TypedDict(
    "RestoreTableFromBackupOutputResponseTypeDef",
    {
        "TableDescription": "TableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRestoreTableToPointInTimeInputTypeDef = TypedDict(
    "_RequiredRestoreTableToPointInTimeInputTypeDef",
    {
        "TargetTableName": str,
    },
)
_OptionalRestoreTableToPointInTimeInputTypeDef = TypedDict(
    "_OptionalRestoreTableToPointInTimeInputTypeDef",
    {
        "SourceTableArn": str,
        "SourceTableName": str,
        "UseLatestRestorableTime": bool,
        "RestoreDateTime": Union[datetime, str],
        "BillingModeOverride": BillingModeType,
        "GlobalSecondaryIndexOverride": List["GlobalSecondaryIndexTypeDef"],
        "LocalSecondaryIndexOverride": List["LocalSecondaryIndexTypeDef"],
        "ProvisionedThroughputOverride": "ProvisionedThroughputTypeDef",
        "SSESpecificationOverride": "SSESpecificationTypeDef",
    },
    total=False,
)


class RestoreTableToPointInTimeInputTypeDef(
    _RequiredRestoreTableToPointInTimeInputTypeDef, _OptionalRestoreTableToPointInTimeInputTypeDef
):
    pass


RestoreTableToPointInTimeOutputResponseTypeDef = TypedDict(
    "RestoreTableToPointInTimeOutputResponseTypeDef",
    {
        "TableDescription": "TableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SSEDescriptionTypeDef = TypedDict(
    "SSEDescriptionTypeDef",
    {
        "Status": SSEStatusType,
        "SSEType": SSETypeType,
        "KMSMasterKeyArn": str,
        "InaccessibleEncryptionDateTime": datetime,
    },
    total=False,
)

SSESpecificationTypeDef = TypedDict(
    "SSESpecificationTypeDef",
    {
        "Enabled": bool,
        "SSEType": SSETypeType,
        "KMSMasterKeyId": str,
    },
    total=False,
)

ScanInputTableTypeDef = TypedDict(
    "ScanInputTableTypeDef",
    {
        "IndexName": str,
        "AttributesToGet": List[str],
        "Limit": int,
        "Select": SelectType,
        "ScanFilter": Dict[str, "ConditionTypeDef"],
        "ConditionalOperator": ConditionalOperatorType,
        "ExclusiveStartKey": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "TotalSegments": int,
        "Segment": int,
        "ProjectionExpression": str,
        "FilterExpression": Union[str, ConditionBase],
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ConsistentRead": bool,
    },
    total=False,
)

_RequiredScanInputTypeDef = TypedDict(
    "_RequiredScanInputTypeDef",
    {
        "TableName": str,
    },
)
_OptionalScanInputTypeDef = TypedDict(
    "_OptionalScanInputTypeDef",
    {
        "IndexName": str,
        "AttributesToGet": List[str],
        "Limit": int,
        "Select": SelectType,
        "ScanFilter": Dict[str, "ConditionTypeDef"],
        "ConditionalOperator": ConditionalOperatorType,
        "ExclusiveStartKey": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "TotalSegments": int,
        "Segment": int,
        "ProjectionExpression": str,
        "FilterExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ConsistentRead": bool,
    },
    total=False,
)


class ScanInputTypeDef(_RequiredScanInputTypeDef, _OptionalScanInputTypeDef):
    pass


ScanOutputResponseTypeDef = TypedDict(
    "ScanOutputResponseTypeDef",
    {
        "Items": List[
            Dict[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    List[Any],
                    Dict[str, Any],
                    None,
                ],
            ]
        ],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceResourceTableRequestTypeDef = TypedDict(
    "ServiceResourceTableRequestTypeDef",
    {
        "name": str,
    },
)

_RequiredSourceTableDetailsTypeDef = TypedDict(
    "_RequiredSourceTableDetailsTypeDef",
    {
        "TableName": str,
        "TableId": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "TableCreationDateTime": datetime,
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
    },
)
_OptionalSourceTableDetailsTypeDef = TypedDict(
    "_OptionalSourceTableDetailsTypeDef",
    {
        "TableArn": str,
        "TableSizeBytes": int,
        "ItemCount": int,
        "BillingMode": BillingModeType,
    },
    total=False,
)


class SourceTableDetailsTypeDef(
    _RequiredSourceTableDetailsTypeDef, _OptionalSourceTableDetailsTypeDef
):
    pass


SourceTableFeatureDetailsTypeDef = TypedDict(
    "SourceTableFeatureDetailsTypeDef",
    {
        "LocalSecondaryIndexes": List["LocalSecondaryIndexInfoTypeDef"],
        "GlobalSecondaryIndexes": List["GlobalSecondaryIndexInfoTypeDef"],
        "StreamDescription": "StreamSpecificationTypeDef",
        "TimeToLiveDescription": "TimeToLiveDescriptionTypeDef",
        "SSEDescription": "SSEDescriptionTypeDef",
    },
    total=False,
)

_RequiredStreamSpecificationTypeDef = TypedDict(
    "_RequiredStreamSpecificationTypeDef",
    {
        "StreamEnabled": bool,
    },
)
_OptionalStreamSpecificationTypeDef = TypedDict(
    "_OptionalStreamSpecificationTypeDef",
    {
        "StreamViewType": StreamViewTypeType,
    },
    total=False,
)


class StreamSpecificationTypeDef(
    _RequiredStreamSpecificationTypeDef, _OptionalStreamSpecificationTypeDef
):
    pass


TableAutoScalingDescriptionTypeDef = TypedDict(
    "TableAutoScalingDescriptionTypeDef",
    {
        "TableName": str,
        "TableStatus": TableStatusType,
        "Replicas": List["ReplicaAutoScalingDescriptionTypeDef"],
    },
    total=False,
)

TableBatchWriterRequestTypeDef = TypedDict(
    "TableBatchWriterRequestTypeDef",
    {
        "overwrite_by_pkeys": List[str],
    },
    total=False,
)

TableDescriptionTypeDef = TypedDict(
    "TableDescriptionTypeDef",
    {
        "AttributeDefinitions": List["AttributeDefinitionTypeDef"],
        "TableName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "TableStatus": TableStatusType,
        "CreationDateTime": datetime,
        "ProvisionedThroughput": "ProvisionedThroughputDescriptionTypeDef",
        "TableSizeBytes": int,
        "ItemCount": int,
        "TableArn": str,
        "TableId": str,
        "BillingModeSummary": "BillingModeSummaryTypeDef",
        "LocalSecondaryIndexes": List["LocalSecondaryIndexDescriptionTypeDef"],
        "GlobalSecondaryIndexes": List["GlobalSecondaryIndexDescriptionTypeDef"],
        "StreamSpecification": "StreamSpecificationTypeDef",
        "LatestStreamLabel": str,
        "LatestStreamArn": str,
        "GlobalTableVersion": str,
        "Replicas": List["ReplicaDescriptionTypeDef"],
        "RestoreSummary": "RestoreSummaryTypeDef",
        "SSEDescription": "SSEDescriptionTypeDef",
        "ArchivalSummary": "ArchivalSummaryTypeDef",
    },
    total=False,
)

TagResourceInputTypeDef = TypedDict(
    "TagResourceInputTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TimeToLiveDescriptionTypeDef = TypedDict(
    "TimeToLiveDescriptionTypeDef",
    {
        "TimeToLiveStatus": TimeToLiveStatusType,
        "AttributeName": str,
    },
    total=False,
)

TimeToLiveSpecificationTypeDef = TypedDict(
    "TimeToLiveSpecificationTypeDef",
    {
        "Enabled": bool,
        "AttributeName": str,
    },
)

TransactGetItemTypeDef = TypedDict(
    "TransactGetItemTypeDef",
    {
        "Get": "GetTypeDef",
    },
)

_RequiredTransactGetItemsInputTypeDef = TypedDict(
    "_RequiredTransactGetItemsInputTypeDef",
    {
        "TransactItems": List["TransactGetItemTypeDef"],
    },
)
_OptionalTransactGetItemsInputTypeDef = TypedDict(
    "_OptionalTransactGetItemsInputTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
    },
    total=False,
)


class TransactGetItemsInputTypeDef(
    _RequiredTransactGetItemsInputTypeDef, _OptionalTransactGetItemsInputTypeDef
):
    pass


TransactGetItemsOutputResponseTypeDef = TypedDict(
    "TransactGetItemsOutputResponseTypeDef",
    {
        "ConsumedCapacity": List["ConsumedCapacityTypeDef"],
        "Responses": List["ItemResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TransactWriteItemTypeDef = TypedDict(
    "TransactWriteItemTypeDef",
    {
        "ConditionCheck": "ConditionCheckTypeDef",
        "Put": "PutTypeDef",
        "Delete": "DeleteTypeDef",
        "Update": "UpdateTypeDef",
    },
    total=False,
)

_RequiredTransactWriteItemsInputTypeDef = TypedDict(
    "_RequiredTransactWriteItemsInputTypeDef",
    {
        "TransactItems": List["TransactWriteItemTypeDef"],
    },
)
_OptionalTransactWriteItemsInputTypeDef = TypedDict(
    "_OptionalTransactWriteItemsInputTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ClientRequestToken": str,
    },
    total=False,
)


class TransactWriteItemsInputTypeDef(
    _RequiredTransactWriteItemsInputTypeDef, _OptionalTransactWriteItemsInputTypeDef
):
    pass


TransactWriteItemsOutputResponseTypeDef = TypedDict(
    "TransactWriteItemsOutputResponseTypeDef",
    {
        "ConsumedCapacity": List["ConsumedCapacityTypeDef"],
        "ItemCollectionMetrics": Dict[str, List["ItemCollectionMetricsTypeDef"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceInputTypeDef = TypedDict(
    "UntagResourceInputTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateContinuousBackupsInputTypeDef = TypedDict(
    "UpdateContinuousBackupsInputTypeDef",
    {
        "TableName": str,
        "PointInTimeRecoverySpecification": "PointInTimeRecoverySpecificationTypeDef",
    },
)

UpdateContinuousBackupsOutputResponseTypeDef = TypedDict(
    "UpdateContinuousBackupsOutputResponseTypeDef",
    {
        "ContinuousBackupsDescription": "ContinuousBackupsDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateContributorInsightsInputTypeDef = TypedDict(
    "_RequiredUpdateContributorInsightsInputTypeDef",
    {
        "TableName": str,
        "ContributorInsightsAction": ContributorInsightsActionType,
    },
)
_OptionalUpdateContributorInsightsInputTypeDef = TypedDict(
    "_OptionalUpdateContributorInsightsInputTypeDef",
    {
        "IndexName": str,
    },
    total=False,
)


class UpdateContributorInsightsInputTypeDef(
    _RequiredUpdateContributorInsightsInputTypeDef, _OptionalUpdateContributorInsightsInputTypeDef
):
    pass


UpdateContributorInsightsOutputResponseTypeDef = TypedDict(
    "UpdateContributorInsightsOutputResponseTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsStatus": ContributorInsightsStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGlobalSecondaryIndexActionTypeDef = TypedDict(
    "UpdateGlobalSecondaryIndexActionTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
    },
)

UpdateGlobalTableInputTypeDef = TypedDict(
    "UpdateGlobalTableInputTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaUpdates": List["ReplicaUpdateTypeDef"],
    },
)

UpdateGlobalTableOutputResponseTypeDef = TypedDict(
    "UpdateGlobalTableOutputResponseTypeDef",
    {
        "GlobalTableDescription": "GlobalTableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGlobalTableSettingsInputTypeDef = TypedDict(
    "_RequiredUpdateGlobalTableSettingsInputTypeDef",
    {
        "GlobalTableName": str,
    },
)
_OptionalUpdateGlobalTableSettingsInputTypeDef = TypedDict(
    "_OptionalUpdateGlobalTableSettingsInputTypeDef",
    {
        "GlobalTableBillingMode": BillingModeType,
        "GlobalTableProvisionedWriteCapacityUnits": int,
        "GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate": "AutoScalingSettingsUpdateTypeDef",
        "GlobalTableGlobalSecondaryIndexSettingsUpdate": List[
            "GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef"
        ],
        "ReplicaSettingsUpdate": List["ReplicaSettingsUpdateTypeDef"],
    },
    total=False,
)


class UpdateGlobalTableSettingsInputTypeDef(
    _RequiredUpdateGlobalTableSettingsInputTypeDef, _OptionalUpdateGlobalTableSettingsInputTypeDef
):
    pass


UpdateGlobalTableSettingsOutputResponseTypeDef = TypedDict(
    "UpdateGlobalTableSettingsOutputResponseTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaSettings": List["ReplicaSettingsDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateItemInputTableTypeDef = TypedDict(
    "_RequiredUpdateItemInputTableTypeDef",
    {
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)
_OptionalUpdateItemInputTableTypeDef = TypedDict(
    "_OptionalUpdateItemInputTableTypeDef",
    {
        "AttributeUpdates": Dict[str, "AttributeValueUpdateTypeDef"],
        "Expected": Dict[str, "ExpectedAttributeValueTypeDef"],
        "ConditionalOperator": ConditionalOperatorType,
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "UpdateExpression": str,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)


class UpdateItemInputTableTypeDef(
    _RequiredUpdateItemInputTableTypeDef, _OptionalUpdateItemInputTableTypeDef
):
    pass


_RequiredUpdateItemInputTypeDef = TypedDict(
    "_RequiredUpdateItemInputTypeDef",
    {
        "TableName": str,
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)
_OptionalUpdateItemInputTypeDef = TypedDict(
    "_OptionalUpdateItemInputTypeDef",
    {
        "AttributeUpdates": Dict[str, "AttributeValueUpdateTypeDef"],
        "Expected": Dict[str, "ExpectedAttributeValueTypeDef"],
        "ConditionalOperator": ConditionalOperatorType,
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "UpdateExpression": str,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)


class UpdateItemInputTypeDef(_RequiredUpdateItemInputTypeDef, _OptionalUpdateItemInputTypeDef):
    pass


UpdateItemOutputResponseTypeDef = TypedDict(
    "UpdateItemOutputResponseTypeDef",
    {
        "Attributes": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ItemCollectionMetrics": "ItemCollectionMetricsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateReplicationGroupMemberActionTypeDef = TypedDict(
    "_RequiredUpdateReplicationGroupMemberActionTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalUpdateReplicationGroupMemberActionTypeDef = TypedDict(
    "_OptionalUpdateReplicationGroupMemberActionTypeDef",
    {
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": "ProvisionedThroughputOverrideTypeDef",
        "GlobalSecondaryIndexes": List["ReplicaGlobalSecondaryIndexTypeDef"],
    },
    total=False,
)


class UpdateReplicationGroupMemberActionTypeDef(
    _RequiredUpdateReplicationGroupMemberActionTypeDef,
    _OptionalUpdateReplicationGroupMemberActionTypeDef,
):
    pass


UpdateTableInputTableTypeDef = TypedDict(
    "UpdateTableInputTableTypeDef",
    {
        "AttributeDefinitions": List["AttributeDefinitionTypeDef"],
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
        "GlobalSecondaryIndexUpdates": List["GlobalSecondaryIndexUpdateTypeDef"],
        "StreamSpecification": "StreamSpecificationTypeDef",
        "SSESpecification": "SSESpecificationTypeDef",
        "ReplicaUpdates": List["ReplicationGroupUpdateTypeDef"],
    },
    total=False,
)

_RequiredUpdateTableInputTypeDef = TypedDict(
    "_RequiredUpdateTableInputTypeDef",
    {
        "TableName": str,
    },
)
_OptionalUpdateTableInputTypeDef = TypedDict(
    "_OptionalUpdateTableInputTypeDef",
    {
        "AttributeDefinitions": List["AttributeDefinitionTypeDef"],
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
        "GlobalSecondaryIndexUpdates": List["GlobalSecondaryIndexUpdateTypeDef"],
        "StreamSpecification": "StreamSpecificationTypeDef",
        "SSESpecification": "SSESpecificationTypeDef",
        "ReplicaUpdates": List["ReplicationGroupUpdateTypeDef"],
    },
    total=False,
)


class UpdateTableInputTypeDef(_RequiredUpdateTableInputTypeDef, _OptionalUpdateTableInputTypeDef):
    pass


UpdateTableOutputResponseTypeDef = TypedDict(
    "UpdateTableOutputResponseTypeDef",
    {
        "TableDescription": "TableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTableReplicaAutoScalingInputTypeDef = TypedDict(
    "_RequiredUpdateTableReplicaAutoScalingInputTypeDef",
    {
        "TableName": str,
    },
)
_OptionalUpdateTableReplicaAutoScalingInputTypeDef = TypedDict(
    "_OptionalUpdateTableReplicaAutoScalingInputTypeDef",
    {
        "GlobalSecondaryIndexUpdates": List["GlobalSecondaryIndexAutoScalingUpdateTypeDef"],
        "ProvisionedWriteCapacityAutoScalingUpdate": "AutoScalingSettingsUpdateTypeDef",
        "ReplicaUpdates": List["ReplicaAutoScalingUpdateTypeDef"],
    },
    total=False,
)


class UpdateTableReplicaAutoScalingInputTypeDef(
    _RequiredUpdateTableReplicaAutoScalingInputTypeDef,
    _OptionalUpdateTableReplicaAutoScalingInputTypeDef,
):
    pass


UpdateTableReplicaAutoScalingOutputResponseTypeDef = TypedDict(
    "UpdateTableReplicaAutoScalingOutputResponseTypeDef",
    {
        "TableAutoScalingDescription": "TableAutoScalingDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTimeToLiveInputTypeDef = TypedDict(
    "UpdateTimeToLiveInputTypeDef",
    {
        "TableName": str,
        "TimeToLiveSpecification": "TimeToLiveSpecificationTypeDef",
    },
)

UpdateTimeToLiveOutputResponseTypeDef = TypedDict(
    "UpdateTimeToLiveOutputResponseTypeDef",
    {
        "TimeToLiveSpecification": "TimeToLiveSpecificationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTypeDef = TypedDict(
    "_RequiredUpdateTypeDef",
    {
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "UpdateExpression": str,
        "TableName": str,
    },
)
_OptionalUpdateTypeDef = TypedDict(
    "_OptionalUpdateTypeDef",
    {
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)


class UpdateTypeDef(_RequiredUpdateTypeDef, _OptionalUpdateTypeDef):
    pass


WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

WriteRequestTypeDef = TypedDict(
    "WriteRequestTypeDef",
    {
        "PutRequest": "PutRequestTypeDef",
        "DeleteRequest": "DeleteRequestTypeDef",
    },
    total=False,
)
