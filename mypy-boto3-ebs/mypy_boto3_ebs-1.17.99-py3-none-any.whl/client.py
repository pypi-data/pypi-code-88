"""
Type annotations for ebs service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ebs/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ebs import EBSClient

    client: EBSClient = boto3.client("ebs")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union

from botocore.client import ClientMeta
from botocore.response import StreamingBody

from .type_defs import (
    CompleteSnapshotResponseTypeDef,
    GetSnapshotBlockResponseTypeDef,
    ListChangedBlocksResponseTypeDef,
    ListSnapshotBlocksResponseTypeDef,
    PutSnapshotBlockResponseTypeDef,
    StartSnapshotResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("EBSClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentLimitExceededException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    RequestThrottledException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class EBSClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ebs.html#EBS.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ebs/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ebs.html#EBS.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ebs/client.html#can_paginate)
        """

    def complete_snapshot(
        self,
        *,
        SnapshotId: str,
        ChangedBlocksCount: int,
        Checksum: str = None,
        ChecksumAlgorithm: Literal["SHA256"] = None,
        ChecksumAggregationMethod: Literal["LINEAR"] = None
    ) -> CompleteSnapshotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ebs.html#EBS.Client.complete_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ebs/client.html#complete_snapshot)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ebs.html#EBS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ebs/client.html#generate_presigned_url)
        """

    def get_snapshot_block(
        self, *, SnapshotId: str, BlockIndex: int, BlockToken: str
    ) -> GetSnapshotBlockResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ebs.html#EBS.Client.get_snapshot_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ebs/client.html#get_snapshot_block)
        """

    def list_changed_blocks(
        self,
        *,
        SecondSnapshotId: str,
        FirstSnapshotId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        StartingBlockIndex: int = None
    ) -> ListChangedBlocksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ebs.html#EBS.Client.list_changed_blocks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ebs/client.html#list_changed_blocks)
        """

    def list_snapshot_blocks(
        self,
        *,
        SnapshotId: str,
        NextToken: str = None,
        MaxResults: int = None,
        StartingBlockIndex: int = None
    ) -> ListSnapshotBlocksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ebs.html#EBS.Client.list_snapshot_blocks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ebs/client.html#list_snapshot_blocks)
        """

    def put_snapshot_block(
        self,
        *,
        SnapshotId: str,
        BlockIndex: int,
        BlockData: Union[bytes, IO[bytes], StreamingBody],
        DataLength: int,
        Checksum: str,
        ChecksumAlgorithm: Literal["SHA256"],
        Progress: int = None
    ) -> PutSnapshotBlockResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ebs.html#EBS.Client.put_snapshot_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ebs/client.html#put_snapshot_block)
        """

    def start_snapshot(
        self,
        *,
        VolumeSize: int,
        ParentSnapshotId: str = None,
        Tags: List["TagTypeDef"] = None,
        Description: str = None,
        ClientToken: str = None,
        Encrypted: bool = None,
        KmsKeyArn: str = None,
        Timeout: int = None
    ) -> StartSnapshotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ebs.html#EBS.Client.start_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ebs/client.html#start_snapshot)
        """
