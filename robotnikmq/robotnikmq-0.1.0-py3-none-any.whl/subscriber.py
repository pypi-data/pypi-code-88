from typing import Optional, Callable

from typeguard import typechecked

from robotnikmq.config import RobotnikConfig
from robotnikmq.core import Robotnik, ConnErrorCallback, Message

OnMessageCallback = Callable[[Message], None]


class Subscriber(Robotnik):
    @typechecked
    def __init__(self, exchange: str,
                 binding_key: Optional[str] = None,
                 config: Optional[RobotnikConfig] = None,
                 on_conn_error: ConnErrorCallback = None):
        super().__init__(config=config, on_conn_error=on_conn_error)
        self.exchange = exchange
        self.channel.exchange_declare(exchange=self.exchange,
                                      exchange_type='topic',
                                      auto_delete=True)
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.queue = result.method.queue
        self.channel.queue_bind(exchange=exchange,
                                queue=self.queue,
                                routing_key=(binding_key or '#'))

    @typechecked
    def register_listener(self, callback: OnMessageCallback) -> None:
        @typechecked
        def meta_callback(_, method, ___, body: bytes):
            callback(Message.of(body.decode()))
            self.channel.basic_ack(delivery_tag=method.delivery_tag)
        self.channel.basic_consume(queue=self.queue,
                                   on_message_callback=meta_callback,
                                   auto_ack=False)

    @typechecked
    def run(self) -> None:
        self.channel.start_consuming()
