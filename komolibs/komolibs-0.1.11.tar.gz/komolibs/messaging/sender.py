import asyncio
import json
import logging
from typing import Optional, NamedTuple, Any, Dict

import certifi
from aiokafka import AIOKafkaProducer
from aiokafka.helpers import create_ssl_context

from komolibs.core.utils.async_utils import safe_ensure_future
from komolibs.logger.logger import KomoLogger
from komolibs.messaging.base import MessageBase


class MessagePackTuple(NamedTuple):
    topic: str
    key: str
    value: Dict[str, Any]

    def __repr__(self):
        return f"MessagePackTuple('topic': {self.topic}, 'key': {self.key}, 'value': {self.value})"

    @property
    def topic(self):
        return self.topic

    @property
    def key(self):
        return self.key

    @property
    def keyb(self):
        return json.dumps(self.key).encode('utf-8')

    @property
    def value(self):
        return self.value

    @property
    def valueb(self):
        return str.encode(json.dumps(self.value))  # json.dumps(self.value).encode('utf-8')


class KomoSender(MessageBase):
    ks_logger: Optional[KomoLogger] = None
    _shared_instance: "KomoSender" = None

    @classmethod
    def get_instance(cls, config_file_path) -> "KomoSender":
        if cls._shared_instance is None:
            cls._shared_instance = KomoSender(config_file_path=config_file_path)
        return cls._shared_instance

    @classmethod
    def logger(cls) -> KomoLogger:
        if cls.ks_logger is None:
            cls.ks_logger = logging.getLogger(__name__)
        return cls.ks_logger

    def __init__(self,
                 config_file_path: str,
                 topic: Optional[str] = "test1"):
        super().__init__(config_file=config_file_path)
        self._topic = topic
        self._producer: Optional[AIOKafkaProducer] = None
        self._delivered_records = 0
        self._ev_loop: asyncio.events.AbstractEventLoop = asyncio.get_event_loop()
        self._start_producer_task: Optional[asyncio.Task] = None
        self._message_sender_loop_task: Optional[asyncio.Task] = None
        self._message_queue: asyncio.Queue = asyncio.Queue()

    @property
    def ready(self):
        return self._start_producer_task.done()

    async def wait_til_producer_start_task_is_done(self):
        while True:
            if self._start_producer_task.done():
                self.logger().info(f"Successfully started the kafka message producer.")
                return
            self.logger().info(f"Waiting for the kafka message producer to start.")
            await asyncio.sleep(1)

    async def start(self):
        """
        Start message sender loop
        """
        self._producer = AIOKafkaProducer(
            loop=self._ev_loop,
            bootstrap_servers=self._bootstrap_servers,
            security_protocol='SASL_SSL',
            ssl_context=create_ssl_context(cafile=certifi.where()),
            sasl_mechanism='PLAIN',
            sasl_plain_username=self._sasl_username,
            sasl_plain_password=self._sasl_password,
            # auto_offset_reset='earliest'
        )

        self._start_producer_task = safe_ensure_future(self.start_producer())
        await self.wait_til_producer_start_task_is_done()
        self._message_sender_loop_task = safe_ensure_future(self.message_sender_loop())

    async def start_producer(self):
        await self._producer.start()

    async def stop(self):
        await self._producer.stop()
        if self._start_producer_task is not None:
            self._start_producer_task.cancel()
            self._start_producer_task = None
        if self._message_sender_loop_task is not None:
            self._message_sender_loop_task.cancel()
            self._message_sender_loop_task = None

    @property
    def message_queue(self) -> asyncio.Queue:
        return self._message_queue

    # Optional per-message on_delivery handler (triggered by poll() or flush())
    # when a message has been successfully delivered or
    # permanently failed delivery (after retries).
    def acked(self, err, msg):
        """
        Delivery report handler called on successful or failed delivery of message.
        """
        if err is not None:
            self.logger().error("Failed to deliver message: {}".format(err))
        else:
            self._delivered_records += 1
            self.logger().info("Produced record to topic {} partition [{}] @ offset {}"
                               .format(msg.topic(), msg.partition(), msg.offset()))

    async def message_sender_loop(self):
        while True:
            try:
                print(f"Message loop started.")
                pack: MessagePackTuple = await self._message_queue.get()

                print(f"Sending message to server.")
                await self._producer.send(topic=pack.topic, key=pack.keyb,
                                          value=pack.valueb, partition=0)
                print(f"Message sent")
            except asyncio.CancelledError:
                raise
            except Exception:
                raise
            finally:
                safe_ensure_future(self.stop())
