"""
Type annotations for dynamodb service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_dynamodb import DynamoDBClient

    client: DynamoDBClient = boto3.client("dynamodb")
    ```
"""
import sys
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, Set, Type, Union, overload

from botocore.client import ClientMeta

from .literals import (
    BackupTypeFilterType,
    BillingModeType,
    ConditionalOperatorType,
    ContributorInsightsActionType,
    ExportFormatType,
    ReturnConsumedCapacityType,
    ReturnItemCollectionMetricsType,
    ReturnValueType,
    S3SseAlgorithmType,
    SelectType,
)
from .paginator import (
    ListBackupsPaginator,
    ListTablesPaginator,
    ListTagsOfResourcePaginator,
    QueryPaginator,
    ScanPaginator,
)
from .type_defs import (
    AttributeDefinitionTypeDef,
    AttributeValueUpdateTypeDef,
    AutoScalingSettingsUpdateTypeDef,
    BatchExecuteStatementOutputTypeDef,
    BatchGetItemOutputTypeDef,
    BatchStatementRequestTypeDef,
    BatchWriteItemOutputTypeDef,
    ConditionTypeDef,
    CreateBackupOutputTypeDef,
    CreateGlobalTableOutputTypeDef,
    CreateTableOutputTypeDef,
    DeleteBackupOutputTypeDef,
    DeleteItemOutputTypeDef,
    DeleteTableOutputTypeDef,
    DescribeBackupOutputTypeDef,
    DescribeContinuousBackupsOutputTypeDef,
    DescribeContributorInsightsOutputTypeDef,
    DescribeEndpointsResponseTypeDef,
    DescribeExportOutputTypeDef,
    DescribeGlobalTableOutputTypeDef,
    DescribeGlobalTableSettingsOutputTypeDef,
    DescribeKinesisStreamingDestinationOutputTypeDef,
    DescribeLimitsOutputTypeDef,
    DescribeTableOutputTypeDef,
    DescribeTableReplicaAutoScalingOutputTypeDef,
    DescribeTimeToLiveOutputTypeDef,
    ExecuteStatementOutputTypeDef,
    ExecuteTransactionOutputTypeDef,
    ExpectedAttributeValueTypeDef,
    ExportTableToPointInTimeOutputTypeDef,
    GetItemOutputTypeDef,
    GlobalSecondaryIndexAutoScalingUpdateTypeDef,
    GlobalSecondaryIndexTypeDef,
    GlobalSecondaryIndexUpdateTypeDef,
    GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef,
    KeysAndAttributesTypeDef,
    KeySchemaElementTypeDef,
    KinesisStreamingDestinationOutputTypeDef,
    ListBackupsOutputTypeDef,
    ListContributorInsightsOutputTypeDef,
    ListExportsOutputTypeDef,
    ListGlobalTablesOutputTypeDef,
    ListTablesOutputTypeDef,
    ListTagsOfResourceOutputTypeDef,
    LocalSecondaryIndexTypeDef,
    ParameterizedStatementTypeDef,
    PointInTimeRecoverySpecificationTypeDef,
    ProvisionedThroughputTypeDef,
    PutItemOutputTypeDef,
    QueryOutputTypeDef,
    ReplicaAutoScalingUpdateTypeDef,
    ReplicaSettingsUpdateTypeDef,
    ReplicationGroupUpdateTypeDef,
    ReplicaTypeDef,
    ReplicaUpdateTypeDef,
    RestoreTableFromBackupOutputTypeDef,
    RestoreTableToPointInTimeOutputTypeDef,
    ScanOutputTypeDef,
    SSESpecificationTypeDef,
    StreamSpecificationTypeDef,
    TagTypeDef,
    TimeToLiveSpecificationTypeDef,
    TransactGetItemsOutputTypeDef,
    TransactGetItemTypeDef,
    TransactWriteItemsOutputTypeDef,
    TransactWriteItemTypeDef,
    UpdateContinuousBackupsOutputTypeDef,
    UpdateContributorInsightsOutputTypeDef,
    UpdateGlobalTableOutputTypeDef,
    UpdateGlobalTableSettingsOutputTypeDef,
    UpdateItemOutputTypeDef,
    UpdateTableOutputTypeDef,
    UpdateTableReplicaAutoScalingOutputTypeDef,
    UpdateTimeToLiveOutputTypeDef,
    WriteRequestTypeDef,
)
from .waiter import TableExistsWaiter, TableNotExistsWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DynamoDBClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BackupInUseException: Type[BotocoreClientError]
    BackupNotFoundException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConditionalCheckFailedException: Type[BotocoreClientError]
    ContinuousBackupsUnavailableException: Type[BotocoreClientError]
    DuplicateItemException: Type[BotocoreClientError]
    ExportConflictException: Type[BotocoreClientError]
    ExportNotFoundException: Type[BotocoreClientError]
    GlobalTableAlreadyExistsException: Type[BotocoreClientError]
    GlobalTableNotFoundException: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    IndexNotFoundException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidExportTimeException: Type[BotocoreClientError]
    InvalidRestoreTimeException: Type[BotocoreClientError]
    ItemCollectionSizeLimitExceededException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    PointInTimeRecoveryUnavailableException: Type[BotocoreClientError]
    ProvisionedThroughputExceededException: Type[BotocoreClientError]
    ReplicaAlreadyExistsException: Type[BotocoreClientError]
    ReplicaNotFoundException: Type[BotocoreClientError]
    RequestLimitExceeded: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TableAlreadyExistsException: Type[BotocoreClientError]
    TableInUseException: Type[BotocoreClientError]
    TableNotFoundException: Type[BotocoreClientError]
    TransactionCanceledException: Type[BotocoreClientError]
    TransactionConflictException: Type[BotocoreClientError]
    TransactionInProgressException: Type[BotocoreClientError]


class DynamoDBClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_execute_statement(
        self, *, Statements: List[BatchStatementRequestTypeDef]
    ) -> BatchExecuteStatementOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.batch_execute_statement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#batch_execute_statement)
        """

    def batch_get_item(
        self,
        *,
        RequestItems: Dict[str, "KeysAndAttributesTypeDef"],
        ReturnConsumedCapacity: ReturnConsumedCapacityType = None
    ) -> BatchGetItemOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.batch_get_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#batch_get_item)
        """

    def batch_write_item(
        self,
        *,
        RequestItems: Dict[str, List["WriteRequestTypeDef"]],
        ReturnConsumedCapacity: ReturnConsumedCapacityType = None,
        ReturnItemCollectionMetrics: ReturnItemCollectionMetricsType = None
    ) -> BatchWriteItemOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.batch_write_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#batch_write_item)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#can_paginate)
        """

    def create_backup(self, *, TableName: str, BackupName: str) -> CreateBackupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.create_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#create_backup)
        """

    def create_global_table(
        self, *, GlobalTableName: str, ReplicationGroup: List["ReplicaTypeDef"]
    ) -> CreateGlobalTableOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.create_global_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#create_global_table)
        """

    def create_table(
        self,
        *,
        AttributeDefinitions: List["AttributeDefinitionTypeDef"],
        TableName: str,
        KeySchema: List["KeySchemaElementTypeDef"],
        LocalSecondaryIndexes: List[LocalSecondaryIndexTypeDef] = None,
        GlobalSecondaryIndexes: List[GlobalSecondaryIndexTypeDef] = None,
        BillingMode: BillingModeType = None,
        ProvisionedThroughput: "ProvisionedThroughputTypeDef" = None,
        StreamSpecification: "StreamSpecificationTypeDef" = None,
        SSESpecification: SSESpecificationTypeDef = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateTableOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.create_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#create_table)
        """

    def delete_backup(self, *, BackupArn: str) -> DeleteBackupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.delete_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#delete_backup)
        """

    def delete_item(
        self,
        *,
        TableName: str,
        Key: Dict[
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
        Expected: Dict[str, ExpectedAttributeValueTypeDef] = None,
        ConditionalOperator: ConditionalOperatorType = None,
        ReturnValues: ReturnValueType = None,
        ReturnConsumedCapacity: ReturnConsumedCapacityType = None,
        ReturnItemCollectionMetrics: ReturnItemCollectionMetricsType = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[
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
        ] = None
    ) -> DeleteItemOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.delete_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#delete_item)
        """

    def delete_table(self, *, TableName: str) -> DeleteTableOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.delete_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#delete_table)
        """

    def describe_backup(self, *, BackupArn: str) -> DescribeBackupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.describe_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#describe_backup)
        """

    def describe_continuous_backups(
        self, *, TableName: str
    ) -> DescribeContinuousBackupsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.describe_continuous_backups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#describe_continuous_backups)
        """

    def describe_contributor_insights(
        self, *, TableName: str, IndexName: str = None
    ) -> DescribeContributorInsightsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.describe_contributor_insights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#describe_contributor_insights)
        """

    def describe_endpoints(self) -> DescribeEndpointsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.describe_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#describe_endpoints)
        """

    def describe_export(self, *, ExportArn: str) -> DescribeExportOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.describe_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#describe_export)
        """

    def describe_global_table(self, *, GlobalTableName: str) -> DescribeGlobalTableOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.describe_global_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#describe_global_table)
        """

    def describe_global_table_settings(
        self, *, GlobalTableName: str
    ) -> DescribeGlobalTableSettingsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.describe_global_table_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#describe_global_table_settings)
        """

    def describe_kinesis_streaming_destination(
        self, *, TableName: str
    ) -> DescribeKinesisStreamingDestinationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.describe_kinesis_streaming_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#describe_kinesis_streaming_destination)
        """

    def describe_limits(self) -> DescribeLimitsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.describe_limits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#describe_limits)
        """

    def describe_table(self, *, TableName: str) -> DescribeTableOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.describe_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#describe_table)
        """

    def describe_table_replica_auto_scaling(
        self, *, TableName: str
    ) -> DescribeTableReplicaAutoScalingOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.describe_table_replica_auto_scaling)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#describe_table_replica_auto_scaling)
        """

    def describe_time_to_live(self, *, TableName: str) -> DescribeTimeToLiveOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.describe_time_to_live)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#describe_time_to_live)
        """

    def disable_kinesis_streaming_destination(
        self, *, TableName: str, StreamArn: str
    ) -> KinesisStreamingDestinationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.disable_kinesis_streaming_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#disable_kinesis_streaming_destination)
        """

    def enable_kinesis_streaming_destination(
        self, *, TableName: str, StreamArn: str
    ) -> KinesisStreamingDestinationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.enable_kinesis_streaming_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#enable_kinesis_streaming_destination)
        """

    def execute_statement(
        self,
        *,
        Statement: str,
        Parameters: List[
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
        ] = None,
        ConsistentRead: bool = None,
        NextToken: str = None
    ) -> ExecuteStatementOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.execute_statement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#execute_statement)
        """

    def execute_transaction(
        self,
        *,
        TransactStatements: List[ParameterizedStatementTypeDef],
        ClientRequestToken: str = None
    ) -> ExecuteTransactionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.execute_transaction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#execute_transaction)
        """

    def export_table_to_point_in_time(
        self,
        *,
        TableArn: str,
        S3Bucket: str,
        ExportTime: datetime = None,
        ClientToken: str = None,
        S3BucketOwner: str = None,
        S3Prefix: str = None,
        S3SseAlgorithm: S3SseAlgorithmType = None,
        S3SseKmsKeyId: str = None,
        ExportFormat: ExportFormatType = None
    ) -> ExportTableToPointInTimeOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.export_table_to_point_in_time)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#export_table_to_point_in_time)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#generate_presigned_url)
        """

    def get_item(
        self,
        *,
        TableName: str,
        Key: Dict[
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
        AttributesToGet: List[str] = None,
        ConsistentRead: bool = None,
        ReturnConsumedCapacity: ReturnConsumedCapacityType = None,
        ProjectionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None
    ) -> GetItemOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.get_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#get_item)
        """

    def list_backups(
        self,
        *,
        TableName: str = None,
        Limit: int = None,
        TimeRangeLowerBound: datetime = None,
        TimeRangeUpperBound: datetime = None,
        ExclusiveStartBackupArn: str = None,
        BackupType: BackupTypeFilterType = None
    ) -> ListBackupsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.list_backups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#list_backups)
        """

    def list_contributor_insights(
        self, *, TableName: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListContributorInsightsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.list_contributor_insights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#list_contributor_insights)
        """

    def list_exports(
        self, *, TableArn: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListExportsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.list_exports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#list_exports)
        """

    def list_global_tables(
        self,
        *,
        ExclusiveStartGlobalTableName: str = None,
        Limit: int = None,
        RegionName: str = None
    ) -> ListGlobalTablesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.list_global_tables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#list_global_tables)
        """

    def list_tables(
        self, *, ExclusiveStartTableName: str = None, Limit: int = None
    ) -> ListTablesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.list_tables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#list_tables)
        """

    def list_tags_of_resource(
        self, *, ResourceArn: str, NextToken: str = None
    ) -> ListTagsOfResourceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.list_tags_of_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#list_tags_of_resource)
        """

    def put_item(
        self,
        *,
        TableName: str,
        Item: Dict[
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
        Expected: Dict[str, ExpectedAttributeValueTypeDef] = None,
        ReturnValues: ReturnValueType = None,
        ReturnConsumedCapacity: ReturnConsumedCapacityType = None,
        ReturnItemCollectionMetrics: ReturnItemCollectionMetricsType = None,
        ConditionalOperator: ConditionalOperatorType = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[
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
        ] = None
    ) -> PutItemOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.put_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#put_item)
        """

    def query(
        self,
        *,
        TableName: str,
        IndexName: str = None,
        Select: SelectType = None,
        AttributesToGet: List[str] = None,
        Limit: int = None,
        ConsistentRead: bool = None,
        KeyConditions: Dict[str, ConditionTypeDef] = None,
        QueryFilter: Dict[str, ConditionTypeDef] = None,
        ConditionalOperator: ConditionalOperatorType = None,
        ScanIndexForward: bool = None,
        ExclusiveStartKey: Dict[
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
        ] = None,
        ReturnConsumedCapacity: ReturnConsumedCapacityType = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        KeyConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[
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
        ] = None
    ) -> QueryOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#query)
        """

    def restore_table_from_backup(
        self,
        *,
        TargetTableName: str,
        BackupArn: str,
        BillingModeOverride: BillingModeType = None,
        GlobalSecondaryIndexOverride: List[GlobalSecondaryIndexTypeDef] = None,
        LocalSecondaryIndexOverride: List[LocalSecondaryIndexTypeDef] = None,
        ProvisionedThroughputOverride: "ProvisionedThroughputTypeDef" = None,
        SSESpecificationOverride: SSESpecificationTypeDef = None
    ) -> RestoreTableFromBackupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.restore_table_from_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#restore_table_from_backup)
        """

    def restore_table_to_point_in_time(
        self,
        *,
        TargetTableName: str,
        SourceTableArn: str = None,
        SourceTableName: str = None,
        UseLatestRestorableTime: bool = None,
        RestoreDateTime: datetime = None,
        BillingModeOverride: BillingModeType = None,
        GlobalSecondaryIndexOverride: List[GlobalSecondaryIndexTypeDef] = None,
        LocalSecondaryIndexOverride: List[LocalSecondaryIndexTypeDef] = None,
        ProvisionedThroughputOverride: "ProvisionedThroughputTypeDef" = None,
        SSESpecificationOverride: SSESpecificationTypeDef = None
    ) -> RestoreTableToPointInTimeOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.restore_table_to_point_in_time)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#restore_table_to_point_in_time)
        """

    def scan(
        self,
        *,
        TableName: str,
        IndexName: str = None,
        AttributesToGet: List[str] = None,
        Limit: int = None,
        Select: SelectType = None,
        ScanFilter: Dict[str, ConditionTypeDef] = None,
        ConditionalOperator: ConditionalOperatorType = None,
        ExclusiveStartKey: Dict[
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
        ] = None,
        ReturnConsumedCapacity: ReturnConsumedCapacityType = None,
        TotalSegments: int = None,
        Segment: int = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[
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
        ] = None,
        ConsistentRead: bool = None
    ) -> ScanOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.scan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#scan)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#tag_resource)
        """

    def transact_get_items(
        self,
        *,
        TransactItems: List[TransactGetItemTypeDef],
        ReturnConsumedCapacity: ReturnConsumedCapacityType = None
    ) -> TransactGetItemsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.transact_get_items)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#transact_get_items)
        """

    def transact_write_items(
        self,
        *,
        TransactItems: List[TransactWriteItemTypeDef],
        ReturnConsumedCapacity: ReturnConsumedCapacityType = None,
        ReturnItemCollectionMetrics: ReturnItemCollectionMetricsType = None,
        ClientRequestToken: str = None
    ) -> TransactWriteItemsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.transact_write_items)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#transact_write_items)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#untag_resource)
        """

    def update_continuous_backups(
        self,
        *,
        TableName: str,
        PointInTimeRecoverySpecification: PointInTimeRecoverySpecificationTypeDef
    ) -> UpdateContinuousBackupsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.update_continuous_backups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#update_continuous_backups)
        """

    def update_contributor_insights(
        self,
        *,
        TableName: str,
        ContributorInsightsAction: ContributorInsightsActionType,
        IndexName: str = None
    ) -> UpdateContributorInsightsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.update_contributor_insights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#update_contributor_insights)
        """

    def update_global_table(
        self, *, GlobalTableName: str, ReplicaUpdates: List[ReplicaUpdateTypeDef]
    ) -> UpdateGlobalTableOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.update_global_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#update_global_table)
        """

    def update_global_table_settings(
        self,
        *,
        GlobalTableName: str,
        GlobalTableBillingMode: BillingModeType = None,
        GlobalTableProvisionedWriteCapacityUnits: int = None,
        GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate: "AutoScalingSettingsUpdateTypeDef" = None,
        GlobalTableGlobalSecondaryIndexSettingsUpdate: List[
            GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef
        ] = None,
        ReplicaSettingsUpdate: List[ReplicaSettingsUpdateTypeDef] = None
    ) -> UpdateGlobalTableSettingsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.update_global_table_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#update_global_table_settings)
        """

    def update_item(
        self,
        *,
        TableName: str,
        Key: Dict[
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
        AttributeUpdates: Dict[str, AttributeValueUpdateTypeDef] = None,
        Expected: Dict[str, ExpectedAttributeValueTypeDef] = None,
        ConditionalOperator: ConditionalOperatorType = None,
        ReturnValues: ReturnValueType = None,
        ReturnConsumedCapacity: ReturnConsumedCapacityType = None,
        ReturnItemCollectionMetrics: ReturnItemCollectionMetricsType = None,
        UpdateExpression: str = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[
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
        ] = None
    ) -> UpdateItemOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.update_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#update_item)
        """

    def update_table(
        self,
        *,
        TableName: str,
        AttributeDefinitions: List["AttributeDefinitionTypeDef"] = None,
        BillingMode: BillingModeType = None,
        ProvisionedThroughput: "ProvisionedThroughputTypeDef" = None,
        GlobalSecondaryIndexUpdates: List[GlobalSecondaryIndexUpdateTypeDef] = None,
        StreamSpecification: "StreamSpecificationTypeDef" = None,
        SSESpecification: SSESpecificationTypeDef = None,
        ReplicaUpdates: List[ReplicationGroupUpdateTypeDef] = None
    ) -> UpdateTableOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.update_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#update_table)
        """

    def update_table_replica_auto_scaling(
        self,
        *,
        TableName: str,
        GlobalSecondaryIndexUpdates: List[GlobalSecondaryIndexAutoScalingUpdateTypeDef] = None,
        ProvisionedWriteCapacityAutoScalingUpdate: "AutoScalingSettingsUpdateTypeDef" = None,
        ReplicaUpdates: List[ReplicaAutoScalingUpdateTypeDef] = None
    ) -> UpdateTableReplicaAutoScalingOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.update_table_replica_auto_scaling)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#update_table_replica_auto_scaling)
        """

    def update_time_to_live(
        self, *, TableName: str, TimeToLiveSpecification: "TimeToLiveSpecificationTypeDef"
    ) -> UpdateTimeToLiveOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Client.update_time_to_live)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/client.html#update_time_to_live)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_backups"]) -> ListBackupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Paginator.ListBackups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/paginators.html#listbackupspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tables"]) -> ListTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Paginator.ListTables)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/paginators.html#listtablespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_of_resource"]
    ) -> ListTagsOfResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Paginator.ListTagsOfResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/paginators.html#listtagsofresourcepaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["query"]) -> QueryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Paginator.Query)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/paginators.html#querypaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["scan"]) -> ScanPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Paginator.Scan)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/paginators.html#scanpaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["table_exists"]) -> TableExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Waiter.table_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/waiters.html#tableexistswaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["table_not_exists"]) -> TableNotExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dynamodb.html#DynamoDB.Waiter.table_not_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/waiters.html#tablenotexistswaiter)
        """
