import asyncio
import json
import logging
from typing import Optional

import certifi
from aiokafka import AIOKafkaConsumer
from aiokafka.helpers import create_ssl_context

from komolibs.core.utils.async_utils import safe_ensure_future
from komolibs.logger.logger import KomoLogger
from komolibs.messaging.base import MessageBase


class KomoReceiver(MessageBase):
    kr_logger: Optional[KomoLogger] = None
    _shared_instance: "KomoReceiver" = None


    @classmethod
    def get_instance(cls, config_file_path) -> "KomoReceiver":
        if cls._shared_instance is None:
            cls._shared_instance = KomoReceiver(config_file_path=config_file_path)
        return cls._shared_instance

    @classmethod
    def logger(cls) -> KomoLogger:
        if cls.kr_logger is None:
            cls.kr_logger = logging.getLogger(__name__)
        return cls.kr_logger

    def __init__(self,
                 config_file_path: str,
                 topic: Optional[str] = "test1"):
        super().__init__(config_file=config_file_path)
        self._consumer: Optional[AIOKafkaConsumer] = None
        self._ev_loop: asyncio.events.AbstractEventLoop = asyncio.get_event_loop()
        self._message_stream: asyncio.Queue = asyncio.Queue()
        self._start_consumer_task: Optional[asyncio.Task] = None
        self._message_receiver_loop_task: Optional[asyncio.Task] = None
        self._topic = topic

    def ready(self):
        return self._start_consumer_task.done()

    async def wait_til_consumer_start_task_is_done(self):
        while True:
            if self._start_consumer_task.done():
                self.logger().info(f"Successfully started the kafka message consumer.")
                return
            self.logger().info(f"Waiting for the kafka message consumer to start.")
            await asyncio.sleep(1)

    async def start(self):
        """
        Start message reception loop
        """
        self._consumer = AIOKafkaConsumer(
            self._topic,
            loop=self._ev_loop,
            bootstrap_servers=self._bootstrap_servers,
            security_protocol='SASL_SSL',
            ssl_context=create_ssl_context(cafile=certifi.where()),
            sasl_mechanism='PLAIN',
            sasl_plain_username=self._sasl_username,
            sasl_plain_password=self._sasl_password,
            # auto_offset_reset='earliest'
        )

        self._start_consumer_task = safe_ensure_future(self.start_consumer())
        await self.wait_til_consumer_start_task_is_done()
        self._message_receiver_loop_task = safe_ensure_future(self.listen_for_kafka_messages(self._message_stream))

    async def start_consumer(self):
        await self._consumer.start()

    async def stop(self):
        await self._consumer.stop()
        if self._start_consumer_task is not None:
            self._start_consumer_task.cancel()
            self._start_consumer_task = None

        self.logger().info(f"Stopping")
        if self._message_receiver_loop_task is not None:
            self._message_receiver_loop_task.cancel()
            self._message_receiver_loop_task = None

    @property
    def message_stream(self) -> asyncio.Queue:
        return self._message_stream

    async def listen_for_kafka_messages(self, output: asyncio.Queue):
        """
        A consumer for kafka messages.
        :param output: an async queue where the incoming messages are stored
        """
        try:
            async for message in self._consumer:
                output.put_nowait({"topic": message.topic,
                                   "key": message.key.decode('utf-8'),
                                   "value": json.loads(message.value.decode('utf-8')),
                                   "timestamp": message.timestamp})
                self.logger().info(json.loads(message.value.decode('utf-8')))
        except asyncio.CancelledError:
            raise
        except Exception:
            raise
        finally:
            await self._consumer.stop()
