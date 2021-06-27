from contextlib import contextmanager
from datetime import datetime
from json import loads as from_json
from json.decoder import JSONDecodeError
from pathlib import Path
from random import sample
from ssl import SSLError
from threading import current_thread
from typing import Optional, Callable, Any, Dict, Union
from uuid import uuid4 as uuid, UUID

from arrow import Arrow, get as to_arrow, now
from funcy import first
from pika import BlockingConnection
from pika.channel import Channel
from pika.exceptions import AMQPError, AMQPConnectionError
from pydantic import BaseModel  # pylint: disable=E0611
from typeguard import typechecked

from robotnikmq.config import RobotnikConfig, conn_params_of, config_of
from robotnikmq.error import UnableToConnect
from robotnikmq.utils import to_json

AMQPErrorCallback = Optional[Callable[[AMQPError], None]]
ConnErrorCallback = Optional[Callable[[AMQPConnectionError], None]]


@contextmanager
def thread_name(name: Union[str, UUID]):
    thread = current_thread()
    original = thread.name
    thread.name = str(name)
    yield
    thread.name = original


@typechecked
def jsonable(content: Any) -> bool:
    try:
        to_json(content)
        return True
    except (TypeError, OverflowError):
        return False


@typechecked
def valid_json(string: str) -> bool:
    try:
        from_json(string)
        return True
    except JSONDecodeError:
        return False


class Message:
    @typechecked
    def __init__(self, contents: Union[BaseModel, Dict[str, Any]],
                 routing_key: Optional[str] = None,
                 timestamp: Union[int, float, datetime, None] = None,
                 msg_id: Union[str, UUID, None] = None):
        self.msg_id = msg_id or uuid()
        if not jsonable(contents):
            raise ValueError("Contents of message have to be JSON-serializeable")
        self.contents = contents.dict() if isinstance(contents, BaseModel) else contents
        self.routing_key: str = routing_key or ''
        self.timestamp: Arrow = to_arrow(timestamp) if timestamp is not None else now()

    @typechecked
    def to_dict(self) -> Dict[str, Any]:
        return {'routing_key': self.routing_key,
                'contents': self.contents,
                'msg_id': str(self.msg_id),
                'timestamp': self.timestamp.int_timestamp}

    @typechecked
    def to_json(self) -> str:
        return to_json(self.to_dict())

    @staticmethod
    @typechecked
    def of(body: str) -> 'Message':
        msg = from_json(body)
        return Message(msg['contents'], msg['routing_key'], msg['timestamp'], msg['msg_id'])


class Robotnik:
    CONFIG_LOCATIONS = [Path.cwd() / 'robotnikmq.yaml',
                        Path.home() / '.config' / 'robotnikmq' / 'robotnikmq.yaml',
                        Path('/etc/robotnikmq/robotnikmq.yaml')]

    @typechecked
    def __init__(self, config: Optional[RobotnikConfig] = None,
                 on_conn_error: ConnErrorCallback = None):
        self.config = config or config_of(first(location for location in self.CONFIG_LOCATIONS if location.exists()))
        self._connection = None
        self._channel = None
        self._on_conn_error = on_conn_error

    @typechecked
    def _make_connection(self,
                         on_conn_error: ConnErrorCallback = None) -> BlockingConnection:
        errors: Dict[str, str] = {}
        for tier in self.config.tiers:
            for config in sample(tier, len(tier)):
                try:
                    return BlockingConnection(conn_params_of(config))
                except (AMQPConnectionError, SSLError) as exc:
                    errors[f'{config.user}@{config.host}:{config.port}'] = str(exc)
                    if on_conn_error is not None:
                        on_conn_error(exc)
                    elif self._on_conn_error is not None:
                        self._on_conn_error(exc)
        raise UnableToConnect(f'Cannot connect to any of the configured servers: {errors}')

    @typechecked
    def _clear_channel(self, _: Channel, __: Exception) -> None:
        self._channel = None

    @typechecked
    def make_connection(self, on_conn_error: ConnErrorCallback = None) -> BlockingConnection:
        return self._make_connection(on_conn_error=on_conn_error)

    @property
    def connection(self) -> BlockingConnection:
        if self._connection is None or not self._connection.is_open:
            self._connection = self.make_connection()
        return self._connection

    @property
    def channel(self) -> Channel:
        if self._channel is None or not self._channel.is_open:
            self._channel = self.connection.channel()
            self._channel.basic_qos(prefetch_count=1)
        return self._channel

    @typechecked
    def stop(self) -> None:
        if self._channel is not None and self._channel.is_open:
            self._channel.close()
