from __future__ import annotations
from typing import (
    NamedTuple,
    Optional,
    Type,
    Union,
)
from nptyping import NDArray

from metta.types.topic_pb2 import DataLocation, TopicMessage
from metta.types.trace_pb2 import Trace

from google.protobuf import message

ProtobufMessage = Type[message.Message]
MessageData = Union[ProtobufMessage, NDArray]


class TopicNotRegistered(Exception):
    pass


class TopicAlreadyRegistered(Exception):
    pass


class Topic(NamedTuple):
    """
    Attributes
    ----------
    name : str
        Topic name.
    data_location : DataLocation
        Where data is stored for this topic.
    env : str
        Environemnt name.
    type : ProtobufMessage
        Proto message type.
    """

    name: str
    source: str
    # env: str TODO: create separate partitions for each env
    data_location: DataLocation
    type: ProtobufMessage

    @property
    def type_name(self):
        return self.type.DESCRIPTOR.full_name

    def __repr__(self) -> str:
        return f"Topic(name={self.name}, source={self.source} type={self.type_name})"


class Message(NamedTuple):
    topic: Topic
    msg: TopicMessage
    data: MessageData


class NewMessage(NamedTuple):
    source: str
    timestamp: int
    data: MessageData
    trace: Optional[Trace]
