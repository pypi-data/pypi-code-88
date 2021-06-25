"""
Type annotations for timestream-write service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_timestream_write import TimestreamWriteClient

    client: TimestreamWriteClient = boto3.client("timestream-write")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .type_defs import (
    CreateDatabaseResponseTypeDef,
    CreateTableResponseTypeDef,
    DescribeDatabaseResponseTypeDef,
    DescribeEndpointsResponseTypeDef,
    DescribeTableResponseTypeDef,
    ListDatabasesResponseTypeDef,
    ListTablesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    RecordTypeDef,
    RetentionPropertiesTypeDef,
    TagTypeDef,
    UpdateDatabaseResponseTypeDef,
    UpdateTableResponseTypeDef,
)

__all__ = ("TimestreamWriteClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidEndpointException: Type[BotocoreClientError]
    RejectedRecordsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class TimestreamWriteClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/timestream-write.html#TimestreamWrite.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/timestream-write.html#TimestreamWrite.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client.html#can_paginate)
        """

    def create_database(
        self, *, DatabaseName: str, KmsKeyId: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateDatabaseResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/timestream-write.html#TimestreamWrite.Client.create_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client.html#create_database)
        """

    def create_table(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        RetentionProperties: "RetentionPropertiesTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateTableResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/timestream-write.html#TimestreamWrite.Client.create_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client.html#create_table)
        """

    def delete_database(self, *, DatabaseName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/timestream-write.html#TimestreamWrite.Client.delete_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client.html#delete_database)
        """

    def delete_table(self, *, DatabaseName: str, TableName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/timestream-write.html#TimestreamWrite.Client.delete_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client.html#delete_table)
        """

    def describe_database(self, *, DatabaseName: str) -> DescribeDatabaseResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/timestream-write.html#TimestreamWrite.Client.describe_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client.html#describe_database)
        """

    def describe_endpoints(self) -> DescribeEndpointsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/timestream-write.html#TimestreamWrite.Client.describe_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client.html#describe_endpoints)
        """

    def describe_table(self, *, DatabaseName: str, TableName: str) -> DescribeTableResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/timestream-write.html#TimestreamWrite.Client.describe_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client.html#describe_table)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/timestream-write.html#TimestreamWrite.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client.html#generate_presigned_url)
        """

    def list_databases(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListDatabasesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/timestream-write.html#TimestreamWrite.Client.list_databases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client.html#list_databases)
        """

    def list_tables(
        self, *, DatabaseName: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListTablesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/timestream-write.html#TimestreamWrite.Client.list_tables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client.html#list_tables)
        """

    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/timestream-write.html#TimestreamWrite.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client.html#list_tags_for_resource)
        """

    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/timestream-write.html#TimestreamWrite.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/timestream-write.html#TimestreamWrite.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client.html#untag_resource)
        """

    def update_database(self, *, DatabaseName: str, KmsKeyId: str) -> UpdateDatabaseResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/timestream-write.html#TimestreamWrite.Client.update_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client.html#update_database)
        """

    def update_table(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        RetentionProperties: "RetentionPropertiesTypeDef"
    ) -> UpdateTableResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/timestream-write.html#TimestreamWrite.Client.update_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client.html#update_table)
        """

    def write_records(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        Records: List[RecordTypeDef],
        CommonAttributes: RecordTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/timestream-write.html#TimestreamWrite.Client.write_records)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/client.html#write_records)
        """
