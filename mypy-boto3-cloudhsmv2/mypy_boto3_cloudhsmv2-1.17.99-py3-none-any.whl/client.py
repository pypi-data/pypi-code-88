"""
Type annotations for cloudhsmv2 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudhsmv2 import CloudHSMV2Client

    client: CloudHSMV2Client = boto3.client("cloudhsmv2")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .paginator import DescribeBackupsPaginator, DescribeClustersPaginator, ListTagsPaginator
from .type_defs import (
    BackupRetentionPolicyTypeDef,
    CopyBackupToRegionResponseTypeDef,
    CreateClusterResponseTypeDef,
    CreateHsmResponseTypeDef,
    DeleteBackupResponseTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteHsmResponseTypeDef,
    DescribeBackupsResponseTypeDef,
    DescribeClustersResponseTypeDef,
    InitializeClusterResponseTypeDef,
    ListTagsResponseTypeDef,
    ModifyBackupAttributesResponseTypeDef,
    ModifyClusterResponseTypeDef,
    RestoreBackupResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CloudHSMV2Client",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    CloudHsmAccessDeniedException: Type[BotocoreClientError]
    CloudHsmInternalFailureException: Type[BotocoreClientError]
    CloudHsmInvalidRequestException: Type[BotocoreClientError]
    CloudHsmResourceNotFoundException: Type[BotocoreClientError]
    CloudHsmServiceException: Type[BotocoreClientError]
    CloudHsmTagException: Type[BotocoreClientError]


class CloudHSMV2Client:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client.html#can_paginate)
        """

    def copy_backup_to_region(
        self, *, DestinationRegion: str, BackupId: str, TagList: List["TagTypeDef"] = None
    ) -> CopyBackupToRegionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Client.copy_backup_to_region)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client.html#copy_backup_to_region)
        """

    def create_cluster(
        self,
        *,
        HsmType: str,
        SubnetIds: List[str],
        BackupRetentionPolicy: "BackupRetentionPolicyTypeDef" = None,
        SourceBackupId: str = None,
        TagList: List["TagTypeDef"] = None
    ) -> CreateClusterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Client.create_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client.html#create_cluster)
        """

    def create_hsm(
        self, *, ClusterId: str, AvailabilityZone: str, IpAddress: str = None
    ) -> CreateHsmResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Client.create_hsm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client.html#create_hsm)
        """

    def delete_backup(self, *, BackupId: str) -> DeleteBackupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Client.delete_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client.html#delete_backup)
        """

    def delete_cluster(self, *, ClusterId: str) -> DeleteClusterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Client.delete_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client.html#delete_cluster)
        """

    def delete_hsm(
        self, *, ClusterId: str, HsmId: str = None, EniId: str = None, EniIp: str = None
    ) -> DeleteHsmResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Client.delete_hsm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client.html#delete_hsm)
        """

    def describe_backups(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: Dict[str, List[str]] = None,
        SortAscending: bool = None
    ) -> DescribeBackupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Client.describe_backups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client.html#describe_backups)
        """

    def describe_clusters(
        self, *, Filters: Dict[str, List[str]] = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeClustersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Client.describe_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client.html#describe_clusters)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client.html#generate_presigned_url)
        """

    def initialize_cluster(
        self, *, ClusterId: str, SignedCert: str, TrustAnchor: str
    ) -> InitializeClusterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Client.initialize_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client.html#initialize_cluster)
        """

    def list_tags(
        self, *, ResourceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Client.list_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client.html#list_tags)
        """

    def modify_backup_attributes(
        self, *, BackupId: str, NeverExpires: bool
    ) -> ModifyBackupAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Client.modify_backup_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client.html#modify_backup_attributes)
        """

    def modify_cluster(
        self, *, BackupRetentionPolicy: "BackupRetentionPolicyTypeDef", ClusterId: str
    ) -> ModifyClusterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Client.modify_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client.html#modify_cluster)
        """

    def restore_backup(self, *, BackupId: str) -> RestoreBackupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Client.restore_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client.html#restore_backup)
        """

    def tag_resource(self, *, ResourceId: str, TagList: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceId: str, TagKeyList: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client.html#untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_backups"]
    ) -> DescribeBackupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.DescribeBackups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/paginators.html#describebackupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_clusters"]
    ) -> DescribeClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.DescribeClusters)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/paginators.html#describeclusterspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tags"]) -> ListTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.ListTags)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/paginators.html#listtagspaginator)
        """
