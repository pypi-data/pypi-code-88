import logging
import os
import sys
from dataclasses import dataclass
from typing import Any

# noinspection PyPackageRequirements
from chromaformatter import ChromaFormatter
from dataclasses_json import dataclass_json

from snacks.rabbit import RabbitClient

log = logging.getLogger('snacks')
log.setLevel(logging.INFO)
formatter = ChromaFormatter(
    '$GREEN%(asctime)-s $LEVEL- '
    '$MAGENTA%(filename)-14s:'
    '%(lineno)-3d'
    '$LEVEL: %(message)s'
)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
log.addHandler(stream_handler)
log.setLevel(logging.DEBUG)

# Initial setup of configuration and Rabbit class.
rabbit = RabbitClient(
    host='localhost',
    port=5672,
    default_exchange='snacks',
    virtual_host='/',
    username=os.environ.get('AMQP_USERNAME') or 'guest',
    password=os.environ.get('AMQP_PASSWORD') or 'guest'
)
# Setup queues to use.
str_queue = 'snack_str'
bytes_queue = 'snack_bytes'
event_queue = 'snack_event'
rpc_queue = 'snack_rpc'
str_key = 'str_key'
bytes_key = 'bytes_key'
event_key = 'event_key'
rpc_key = 'rpc_key'
rabbit.exchange_declare(exchange_type='topic', durable=True)
for key, queue in {
    str_key: str_queue,
    bytes_key: bytes_queue,
    event_key: event_queue,
    rpc_key: rpc_queue
}.items():
    rabbit.queue_declare(queue=queue, durable=True)
    rabbit.queue_bind(queue=queue, routing_key=key)


@dataclass_json
@dataclass
class User:
    id: int
    first: str
    last: str


@dataclass_json
@dataclass
class Event:
    type: str
    body: Any


@rabbit.consumer([str_queue, bytes_queue])
def str_listen(string: str) -> None:
    log.info('Received message: %s', string)


@rabbit.consumer([event_queue])
def event_listen(event: Event) -> None:
    log.info('Received message: %s', event)


@rabbit.consumer([rpc_queue])
def event_rpc(event: Event) -> Event:
    log.info('RPC REQUEST %s', event)
    return Event('parse', User(2, 'Respondy', 'McResponseFace'))


if __name__ == '__main__':
    rabbit.publish('Eat this string.', str_key)
    rabbit.publish(b'Nom these bytes.', bytes_key)
    rabbit.publish(19, str_key)
    rabbit.publish(Event('parse', User(1, 'Snacky', 'McSnackface')), event_key)
    response = rabbit.publish_and_receive(
        Event('parse', User(1, 'Snacky', 'McSnackface')),
        rpc_key
    )
    log.info('RPC RESPONSE: %s', response)
