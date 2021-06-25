"""
Type annotations for mediapackage service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_mediapackage import MediaPackageClient

    client: MediaPackageClient = boto3.client("mediapackage")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import OriginationType
from .paginator import ListChannelsPaginator, ListHarvestJobsPaginator, ListOriginEndpointsPaginator
from .type_defs import (
    AuthorizationTypeDef,
    CmafPackageCreateOrUpdateParametersTypeDef,
    ConfigureLogsResponseTypeDef,
    CreateChannelResponseTypeDef,
    CreateHarvestJobResponseTypeDef,
    CreateOriginEndpointResponseTypeDef,
    DashPackageTypeDef,
    DescribeChannelResponseTypeDef,
    DescribeHarvestJobResponseTypeDef,
    DescribeOriginEndpointResponseTypeDef,
    EgressAccessLogsTypeDef,
    HlsPackageTypeDef,
    IngressAccessLogsTypeDef,
    ListChannelsResponseTypeDef,
    ListHarvestJobsResponseTypeDef,
    ListOriginEndpointsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MssPackageTypeDef,
    RotateChannelCredentialsResponseTypeDef,
    RotateIngestEndpointCredentialsResponseTypeDef,
    S3DestinationTypeDef,
    UpdateChannelResponseTypeDef,
    UpdateOriginEndpointResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MediaPackageClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnprocessableEntityException: Type[BotocoreClientError]


class MediaPackageClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#can_paginate)
        """

    def configure_logs(
        self,
        *,
        Id: str,
        EgressAccessLogs: "EgressAccessLogsTypeDef" = None,
        IngressAccessLogs: "IngressAccessLogsTypeDef" = None
    ) -> ConfigureLogsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.configure_logs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#configure_logs)
        """

    def create_channel(
        self, *, Id: str, Description: str = None, Tags: Dict[str, str] = None
    ) -> CreateChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.create_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#create_channel)
        """

    def create_harvest_job(
        self,
        *,
        EndTime: str,
        Id: str,
        OriginEndpointId: str,
        S3Destination: "S3DestinationTypeDef",
        StartTime: str
    ) -> CreateHarvestJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.create_harvest_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#create_harvest_job)
        """

    def create_origin_endpoint(
        self,
        *,
        ChannelId: str,
        Id: str,
        Authorization: "AuthorizationTypeDef" = None,
        CmafPackage: CmafPackageCreateOrUpdateParametersTypeDef = None,
        DashPackage: "DashPackageTypeDef" = None,
        Description: str = None,
        HlsPackage: "HlsPackageTypeDef" = None,
        ManifestName: str = None,
        MssPackage: "MssPackageTypeDef" = None,
        Origination: OriginationType = None,
        StartoverWindowSeconds: int = None,
        Tags: Dict[str, str] = None,
        TimeDelaySeconds: int = None,
        Whitelist: List[str] = None
    ) -> CreateOriginEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.create_origin_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#create_origin_endpoint)
        """

    def delete_channel(self, *, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.delete_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#delete_channel)
        """

    def delete_origin_endpoint(self, *, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.delete_origin_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#delete_origin_endpoint)
        """

    def describe_channel(self, *, Id: str) -> DescribeChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.describe_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#describe_channel)
        """

    def describe_harvest_job(self, *, Id: str) -> DescribeHarvestJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.describe_harvest_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#describe_harvest_job)
        """

    def describe_origin_endpoint(self, *, Id: str) -> DescribeOriginEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.describe_origin_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#describe_origin_endpoint)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#generate_presigned_url)
        """

    def list_channels(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListChannelsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.list_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#list_channels)
        """

    def list_harvest_jobs(
        self,
        *,
        IncludeChannelId: str = None,
        IncludeStatus: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListHarvestJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.list_harvest_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#list_harvest_jobs)
        """

    def list_origin_endpoints(
        self, *, ChannelId: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListOriginEndpointsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.list_origin_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#list_origin_endpoints)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#list_tags_for_resource)
        """

    def rotate_channel_credentials(self, *, Id: str) -> RotateChannelCredentialsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.rotate_channel_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#rotate_channel_credentials)
        """

    def rotate_ingest_endpoint_credentials(
        self, *, Id: str, IngestEndpointId: str
    ) -> RotateIngestEndpointCredentialsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.rotate_ingest_endpoint_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#rotate_ingest_endpoint_credentials)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#untag_resource)
        """

    def update_channel(self, *, Id: str, Description: str = None) -> UpdateChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.update_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#update_channel)
        """

    def update_origin_endpoint(
        self,
        *,
        Id: str,
        Authorization: "AuthorizationTypeDef" = None,
        CmafPackage: CmafPackageCreateOrUpdateParametersTypeDef = None,
        DashPackage: "DashPackageTypeDef" = None,
        Description: str = None,
        HlsPackage: "HlsPackageTypeDef" = None,
        ManifestName: str = None,
        MssPackage: "MssPackageTypeDef" = None,
        Origination: OriginationType = None,
        StartoverWindowSeconds: int = None,
        TimeDelaySeconds: int = None,
        Whitelist: List[str] = None
    ) -> UpdateOriginEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Client.update_origin_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/client.html#update_origin_endpoint)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_channels"]) -> ListChannelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Paginator.ListChannels)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/paginators.html#listchannelspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_harvest_jobs"]
    ) -> ListHarvestJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Paginator.ListHarvestJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/paginators.html#listharvestjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_origin_endpoints"]
    ) -> ListOriginEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mediapackage.html#MediaPackage.Paginator.ListOriginEndpoints)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/paginators.html#listoriginendpointspaginator)
        """
