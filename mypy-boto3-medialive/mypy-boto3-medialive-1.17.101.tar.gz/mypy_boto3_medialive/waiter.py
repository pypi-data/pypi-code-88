"""
Type annotations for medialive service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_medialive import MediaLiveClient
    from mypy_boto3_medialive.waiter import (
        ChannelCreatedWaiter,
        ChannelDeletedWaiter,
        ChannelRunningWaiter,
        ChannelStoppedWaiter,
        InputAttachedWaiter,
        InputDeletedWaiter,
        InputDetachedWaiter,
        MultiplexCreatedWaiter,
        MultiplexDeletedWaiter,
        MultiplexRunningWaiter,
        MultiplexStoppedWaiter,
    )

    client: MediaLiveClient = boto3.client("medialive")

    channel_created_waiter: ChannelCreatedWaiter = client.get_waiter("channel_created")
    channel_deleted_waiter: ChannelDeletedWaiter = client.get_waiter("channel_deleted")
    channel_running_waiter: ChannelRunningWaiter = client.get_waiter("channel_running")
    channel_stopped_waiter: ChannelStoppedWaiter = client.get_waiter("channel_stopped")
    input_attached_waiter: InputAttachedWaiter = client.get_waiter("input_attached")
    input_deleted_waiter: InputDeletedWaiter = client.get_waiter("input_deleted")
    input_detached_waiter: InputDetachedWaiter = client.get_waiter("input_detached")
    multiplex_created_waiter: MultiplexCreatedWaiter = client.get_waiter("multiplex_created")
    multiplex_deleted_waiter: MultiplexDeletedWaiter = client.get_waiter("multiplex_deleted")
    multiplex_running_waiter: MultiplexRunningWaiter = client.get_waiter("multiplex_running")
    multiplex_stopped_waiter: MultiplexStoppedWaiter = client.get_waiter("multiplex_stopped")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = (
    "ChannelCreatedWaiter",
    "ChannelDeletedWaiter",
    "ChannelRunningWaiter",
    "ChannelStoppedWaiter",
    "InputAttachedWaiter",
    "InputDeletedWaiter",
    "InputDetachedWaiter",
    "MultiplexCreatedWaiter",
    "MultiplexDeletedWaiter",
    "MultiplexRunningWaiter",
    "MultiplexStoppedWaiter",
)


class ChannelCreatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.channel_created)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channelcreatedwaiter)
    """

    def wait(self, *, ChannelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.ChannelCreatedWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channelcreated)
        """


class ChannelDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.channel_deleted)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channeldeletedwaiter)
    """

    def wait(self, *, ChannelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.ChannelDeletedWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channeldeleted)
        """


class ChannelRunningWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.channel_running)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channelrunningwaiter)
    """

    def wait(self, *, ChannelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.ChannelRunningWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channelrunning)
        """


class ChannelStoppedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.channel_stopped)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channelstoppedwaiter)
    """

    def wait(self, *, ChannelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.ChannelStoppedWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channelstopped)
        """


class InputAttachedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.input_attached)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#inputattachedwaiter)
    """

    def wait(self, *, InputId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.InputAttachedWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#inputattached)
        """


class InputDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.input_deleted)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#inputdeletedwaiter)
    """

    def wait(self, *, InputId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.InputDeletedWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#inputdeleted)
        """


class InputDetachedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.input_detached)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#inputdetachedwaiter)
    """

    def wait(self, *, InputId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.InputDetachedWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#inputdetached)
        """


class MultiplexCreatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.multiplex_created)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexcreatedwaiter)
    """

    def wait(self, *, MultiplexId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.MultiplexCreatedWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexcreated)
        """


class MultiplexDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.multiplex_deleted)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexdeletedwaiter)
    """

    def wait(self, *, MultiplexId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.MultiplexDeletedWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexdeleted)
        """


class MultiplexRunningWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.multiplex_running)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexrunningwaiter)
    """

    def wait(self, *, MultiplexId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.MultiplexRunningWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexrunning)
        """


class MultiplexStoppedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.multiplex_stopped)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexstoppedwaiter)
    """

    def wait(self, *, MultiplexId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/medialive.html#MediaLive.Waiter.MultiplexStoppedWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexstopped)
        """
