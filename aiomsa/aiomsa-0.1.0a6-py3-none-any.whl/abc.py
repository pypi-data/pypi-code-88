#!/usr/bin/env python3
# Copyright 2004-present Facebook. All Rights Reserved.

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import IntEnum
from types import TracebackType
from typing import Any, AsyncIterator, Dict, List, Optional, Tuple, Type


class RICActionType(IntEnum):
    """An :class:`~.enum.IntEnum` defining possible RIC actions.

    Attributes:
        REPORT
        INSERT
        POLICY
    """

    REPORT = 0
    INSERT = 1
    POLICY = 2


class RICControlAckRequest(IntEnum):
    """An :class:`~.enum.IntEnum` defining circumstances in which the E2 node
    can/should reply to a RIC control acknowledge message.

    Attributes:
        ACK
        NO_ACK
        NACK
    """

    ACK = 0
    NO_ACK = 1
    NACK = 2


class RICSubsequentActionType(IntEnum):
    """An :class:`~.enum.IntEnum` defining the valid actions that can be taken after
    completing a particular :class:`~.RICAction`.

    Attributes:
        CONTINUE
        WAIT
    """

    CONTINUE = 0
    WAIT = 1


class RICTimeToWait(IntEnum):
    """An :class:`~.enum.IntEnum` defining the time to wait after completing a
    particular :class:`~.RICAction`.

    Attributes:
        ZERO
        W1MS
        W2MS
        W5MS
        W10MS
        W20MS
        W30MS
        W40MS
        W50MS
        W100MS
        W200MS
        W500MS
        W1S
        W2S
        W5S
        W10S
        W20S
        W60S
    """

    ZERO = 0
    W1MS = 1
    W2MS = 2
    W5MS = 3
    W10MS = 4
    W20MS = 5
    W30MS = 6
    W40MS = 7
    W50MS = 8
    W100MS = 9
    W200MS = 10
    W500MS = 11
    W1S = 12
    W2S = 13
    W5S = 14
    W10S = 15
    W20S = 16
    W60S = 17


@dataclass
class RICSubsequentAction:
    """The subsequent action to take once the action is complete.

    Args:
        type: The subsequent action type.
        time_to_wait: Time to wait before performing the subsequent action.
    """

    type: RICSubsequentActionType
    time_to_wait: RICTimeToWait


@dataclass
class RICAction:
    """An action to be taken in a :meth:`~.E2Client.subscribe` request.

    Args:
        id: The RIC action ID.
        type: The action type to be executed.
        subsequent_action: The subsequent action to take once the action is complete.
        definition: Parameters used when executing a report, insert, or policy service.
    """

    id: int
    type: RICActionType
    subsequent_action: Optional[RICSubsequentAction] = None
    definition: Optional[bytes] = None

    def __post_init__(self) -> None:
        if self.type == RICActionType.INSERT and self.subsequent_action is None:
            raise ValueError(
                "subsequent_action must be present when RICActionType is set to 'INSERT'"
            )


@dataclass
class RanFunction:
    """The function corresponding to a specific E2 service model.

    Args:
        id: The RAN function ID.
        oid: The RAN function object ID.
        definition: Data corresponding to a specific E2 service model.
        revision: The RAN function revision.
    """

    id: str
    oid: str
    definition: Dict[str, Any]
    revision: Optional[int] = None


@dataclass
class E2Node:
    """A logical node terminating E2 interface.

    Args:
        id: The E2 node ID.
        ran_functions: The list of RAN functions supported by this E2 node.
    """

    id: str
    ran_functions: List[RanFunction]


class Subscription(ABC):
    @property
    @abstractmethod
    def id(self) -> str:
        """Return an identifier for the subscription."""
        pass

    @abstractmethod
    def __aiter__(self) -> "Subscription":
        """Initialize any resources, if needed."""
        pass

    @abstractmethod
    async def __anext__(self) -> Tuple[bytes, bytes]:
        """Return the next indication in the subscription.

        Returns:
            The next indication header and message, if available.

        Raises:
            StopAsyncIteration: The subscription has been exhausted.
        """
        pass


class E2Client(ABC):
    @abstractmethod
    async def control(
        self,
        e2_node_id: str,
        service_model_name: str,
        service_model_version: str,
        header: bytes,
        message: bytes,
        control_ack_request: RICControlAckRequest,
    ) -> Optional[bytes]:
        """Send a control message to the RIC to initiate or resume some functionality.

        Args:
            e2_node_id: The target E2 node ID.
            service_model_name: The service model name.
            service_model_version: The service model version.
            header: The RIC control header.
            message: The RIC control message.
            control_ack_request: Instruct whether/how the E2 node should reply.

        Returns:
            The control outcome, if specifically requested via ``control_ack_request``,
            else ``None``.

        Raises:
            E2ClientError: The control outcome is failure or missing.
        """
        pass

    @abstractmethod
    async def subscribe(
        self,
        e2_node_id: str,
        service_model_name: str,
        service_model_version: str,
        subscription_id: str,
        trigger: bytes,
        actions: List[RICAction],
    ) -> Subscription:
        """Establish an E2 subscription.

        Args:
            e2_node_id: The target E2 node ID.
            service_model_name: The service model name.
            service_model_version: The service model version.
            subscription_id: The ID to use for the subscription.
            trigger: The event trigger.
            actions: A sequence of RIC service actions.

        Returns:
            The created subscription.
        """
        pass

    @abstractmethod
    async def unsubscribe(
        self,
        e2_node_id: str,
        service_model_name: str,
        service_model_vesrion: str,
        subscription_id: str,
    ) -> None:
        """Delete an E2 subscription.

        Args:
            e2_node_id: The target E2 node ID.
            service_model_name: The service model name.
            service_model_version: The service model version.
            subscription_id: The ID of the subscription to delete.
        """
        pass

    @abstractmethod
    async def __aenter__(self) -> "E2Client":
        """Create any underlying resources required for the client to run."""
        pass

    @abstractmethod
    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        """Cleanly stop all underlying resources used by the client."""
        pass


class SDLClient(ABC):
    @abstractmethod
    async def get_cell_ids(self, e2_node_id: str) -> List[str]:
        """Get the cell IDs corresponding to the given E2 node ID.

        Args:
            e2_node_id: The target E2 node ID.
        """
        pass

    @abstractmethod
    def watch_e2_connections(self) -> AsyncIterator[E2Node]:
        """Stream for newly available E2 node connections."""
        pass

    @abstractmethod
    async def __aenter__(self) -> "SDLClient":
        """Create any underlying resources required for the client to run."""
        pass

    @abstractmethod
    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        """Cleanly stop all underlying resources used by the client."""
        pass
