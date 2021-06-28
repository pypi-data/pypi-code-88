"""
Type annotations for cloudhsm service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudhsm import CloudHSMClient

    client: CloudHSMClient = boto3.client("cloudhsm")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import ClientVersionType
from .paginator import ListHapgsPaginator, ListHsmsPaginator, ListLunaClientsPaginator
from .type_defs import (
    AddTagsToResourceResponseResponseTypeDef,
    CreateHapgResponseResponseTypeDef,
    CreateHsmResponseResponseTypeDef,
    CreateLunaClientResponseResponseTypeDef,
    DeleteHapgResponseResponseTypeDef,
    DeleteHsmResponseResponseTypeDef,
    DeleteLunaClientResponseResponseTypeDef,
    DescribeHapgResponseResponseTypeDef,
    DescribeHsmResponseResponseTypeDef,
    DescribeLunaClientResponseResponseTypeDef,
    GetConfigResponseResponseTypeDef,
    ListAvailableZonesResponseResponseTypeDef,
    ListHapgsResponseResponseTypeDef,
    ListHsmsResponseResponseTypeDef,
    ListLunaClientsResponseResponseTypeDef,
    ListTagsForResourceResponseResponseTypeDef,
    ModifyHapgResponseResponseTypeDef,
    ModifyHsmResponseResponseTypeDef,
    ModifyLunaClientResponseResponseTypeDef,
    RemoveTagsFromResourceResponseResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CloudHSMClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    CloudHsmInternalException: Type[BotocoreClientError]
    CloudHsmServiceException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]


class CloudHSMClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_tags_to_resource(
        self, *, ResourceArn: str, TagList: List["TagTypeDef"]
    ) -> AddTagsToResourceResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.add_tags_to_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#add_tags_to_resource)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#can_paginate)
        """

    def create_hapg(self, *, Label: str) -> CreateHapgResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.create_hapg)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#create_hapg)
        """

    def create_hsm(
        self,
        *,
        SubnetId: str,
        SshKey: str,
        IamRoleArn: str,
        SubscriptionType: Literal["PRODUCTION"],
        EniIp: str = None,
        ExternalId: str = None,
        ClientToken: str = None,
        SyslogIp: str = None
    ) -> CreateHsmResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.create_hsm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#create_hsm)
        """

    def create_luna_client(
        self, *, Certificate: str, Label: str = None
    ) -> CreateLunaClientResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.create_luna_client)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#create_luna_client)
        """

    def delete_hapg(self, *, HapgArn: str) -> DeleteHapgResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.delete_hapg)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#delete_hapg)
        """

    def delete_hsm(self, *, HsmArn: str) -> DeleteHsmResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.delete_hsm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#delete_hsm)
        """

    def delete_luna_client(self, *, ClientArn: str) -> DeleteLunaClientResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.delete_luna_client)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#delete_luna_client)
        """

    def describe_hapg(self, *, HapgArn: str) -> DescribeHapgResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.describe_hapg)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#describe_hapg)
        """

    def describe_hsm(
        self, *, HsmArn: str = None, HsmSerialNumber: str = None
    ) -> DescribeHsmResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.describe_hsm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#describe_hsm)
        """

    def describe_luna_client(
        self, *, ClientArn: str = None, CertificateFingerprint: str = None
    ) -> DescribeLunaClientResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.describe_luna_client)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#describe_luna_client)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#generate_presigned_url)
        """

    def get_config(
        self, *, ClientArn: str, ClientVersion: ClientVersionType, HapgList: List[str]
    ) -> GetConfigResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.get_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#get_config)
        """

    def list_available_zones(self) -> ListAvailableZonesResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.list_available_zones)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#list_available_zones)
        """

    def list_hapgs(self, *, NextToken: str = None) -> ListHapgsResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.list_hapgs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#list_hapgs)
        """

    def list_hsms(self, *, NextToken: str = None) -> ListHsmsResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.list_hsms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#list_hsms)
        """

    def list_luna_clients(self, *, NextToken: str = None) -> ListLunaClientsResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.list_luna_clients)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#list_luna_clients)
        """

    def list_tags_for_resource(
        self, *, ResourceArn: str
    ) -> ListTagsForResourceResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#list_tags_for_resource)
        """

    def modify_hapg(
        self, *, HapgArn: str, Label: str = None, PartitionSerialList: List[str] = None
    ) -> ModifyHapgResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.modify_hapg)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#modify_hapg)
        """

    def modify_hsm(
        self,
        *,
        HsmArn: str,
        SubnetId: str = None,
        EniIp: str = None,
        IamRoleArn: str = None,
        ExternalId: str = None,
        SyslogIp: str = None
    ) -> ModifyHsmResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.modify_hsm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#modify_hsm)
        """

    def modify_luna_client(
        self, *, ClientArn: str, Certificate: str
    ) -> ModifyLunaClientResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.modify_luna_client)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#modify_luna_client)
        """

    def remove_tags_from_resource(
        self, *, ResourceArn: str, TagKeyList: List[str]
    ) -> RemoveTagsFromResourceResponseResponseTypeDef:
        """
        This is documentation for **AWS CloudHSM Classic**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Client.remove_tags_from_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/client.html#remove_tags_from_resource)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_hapgs"]) -> ListHapgsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHapgs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/paginators.html#listhapgspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_hsms"]) -> ListHsmsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHsms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/paginators.html#listhsmspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_luna_clients"]
    ) -> ListLunaClientsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Paginator.ListLunaClients)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/paginators.html#listlunaclientspaginator)
        """
