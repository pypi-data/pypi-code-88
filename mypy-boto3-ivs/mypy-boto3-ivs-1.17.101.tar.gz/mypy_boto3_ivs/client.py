"""
Type annotations for ivs service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ivs import IVSClient

    client: IVSClient = boto3.client("ivs")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import ChannelLatencyModeType, ChannelTypeType
from .paginator import (
    ListChannelsPaginator,
    ListPlaybackKeyPairsPaginator,
    ListRecordingConfigurationsPaginator,
    ListStreamKeysPaginator,
    ListStreamsPaginator,
)
from .type_defs import (
    BatchGetChannelResponseTypeDef,
    BatchGetStreamKeyResponseTypeDef,
    CreateChannelResponseTypeDef,
    CreateRecordingConfigurationResponseTypeDef,
    CreateStreamKeyResponseTypeDef,
    DestinationConfigurationTypeDef,
    GetChannelResponseTypeDef,
    GetPlaybackKeyPairResponseTypeDef,
    GetRecordingConfigurationResponseTypeDef,
    GetStreamKeyResponseTypeDef,
    GetStreamResponseTypeDef,
    ImportPlaybackKeyPairResponseTypeDef,
    ListChannelsResponseTypeDef,
    ListPlaybackKeyPairsResponseTypeDef,
    ListRecordingConfigurationsResponseTypeDef,
    ListStreamKeysResponseTypeDef,
    ListStreamsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    UpdateChannelResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IVSClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ChannelNotBroadcasting: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    PendingVerification: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    StreamUnavailable: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class IVSClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_get_channel(self, *, arns: List[str]) -> BatchGetChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.batch_get_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#batch_get_channel)
        """

    def batch_get_stream_key(self, *, arns: List[str]) -> BatchGetStreamKeyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.batch_get_stream_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#batch_get_stream_key)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#can_paginate)
        """

    def create_channel(
        self,
        *,
        name: str = None,
        latencyMode: ChannelLatencyModeType = None,
        type: ChannelTypeType = None,
        authorized: bool = None,
        recordingConfigurationArn: str = None,
        tags: Dict[str, str] = None
    ) -> CreateChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.create_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#create_channel)
        """

    def create_recording_configuration(
        self,
        *,
        destinationConfiguration: "DestinationConfigurationTypeDef",
        name: str = None,
        tags: Dict[str, str] = None
    ) -> CreateRecordingConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.create_recording_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#create_recording_configuration)
        """

    def create_stream_key(
        self, *, channelArn: str, tags: Dict[str, str] = None
    ) -> CreateStreamKeyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.create_stream_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#create_stream_key)
        """

    def delete_channel(self, *, arn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.delete_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#delete_channel)
        """

    def delete_playback_key_pair(self, *, arn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.delete_playback_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#delete_playback_key_pair)
        """

    def delete_recording_configuration(self, *, arn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.delete_recording_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#delete_recording_configuration)
        """

    def delete_stream_key(self, *, arn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.delete_stream_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#delete_stream_key)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#generate_presigned_url)
        """

    def get_channel(self, *, arn: str) -> GetChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.get_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#get_channel)
        """

    def get_playback_key_pair(self, *, arn: str) -> GetPlaybackKeyPairResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.get_playback_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#get_playback_key_pair)
        """

    def get_recording_configuration(self, *, arn: str) -> GetRecordingConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.get_recording_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#get_recording_configuration)
        """

    def get_stream(self, *, channelArn: str) -> GetStreamResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.get_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#get_stream)
        """

    def get_stream_key(self, *, arn: str) -> GetStreamKeyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.get_stream_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#get_stream_key)
        """

    def import_playback_key_pair(
        self, *, publicKeyMaterial: str, name: str = None, tags: Dict[str, str] = None
    ) -> ImportPlaybackKeyPairResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.import_playback_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#import_playback_key_pair)
        """

    def list_channels(
        self,
        *,
        filterByName: str = None,
        filterByRecordingConfigurationArn: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListChannelsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.list_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#list_channels)
        """

    def list_playback_key_pairs(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListPlaybackKeyPairsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.list_playback_key_pairs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#list_playback_key_pairs)
        """

    def list_recording_configurations(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListRecordingConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.list_recording_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#list_recording_configurations)
        """

    def list_stream_keys(
        self, *, channelArn: str, nextToken: str = None, maxResults: int = None
    ) -> ListStreamKeysResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.list_stream_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#list_stream_keys)
        """

    def list_streams(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListStreamsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.list_streams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#list_streams)
        """

    def list_tags_for_resource(
        self, *, resourceArn: str, nextToken: str = None, maxResults: int = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#list_tags_for_resource)
        """

    def put_metadata(self, *, channelArn: str, metadata: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.put_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#put_metadata)
        """

    def stop_stream(self, *, channelArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.stop_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#stop_stream)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#untag_resource)
        """

    def update_channel(
        self,
        *,
        arn: str,
        name: str = None,
        latencyMode: ChannelLatencyModeType = None,
        type: ChannelTypeType = None,
        authorized: bool = None,
        recordingConfigurationArn: str = None
    ) -> UpdateChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Client.update_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/client.html#update_channel)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_channels"]) -> ListChannelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Paginator.ListChannels)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/paginators.html#listchannelspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_playback_key_pairs"]
    ) -> ListPlaybackKeyPairsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Paginator.ListPlaybackKeyPairs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/paginators.html#listplaybackkeypairspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_recording_configurations"]
    ) -> ListRecordingConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Paginator.ListRecordingConfigurations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/paginators.html#listrecordingconfigurationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_stream_keys"]) -> ListStreamKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Paginator.ListStreamKeys)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/paginators.html#liststreamkeyspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_streams"]) -> ListStreamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ivs.html#IVS.Paginator.ListStreams)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/paginators.html#liststreamspaginator)
        """
