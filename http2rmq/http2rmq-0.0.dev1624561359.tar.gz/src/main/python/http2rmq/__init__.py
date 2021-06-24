import logging
from dataclasses import asdict
from enum import Enum
from logging import Logger
from typing import Any

import aio_pika
import bson
from aiorx import Observer, Subscription
from aiorx.observables import ObservableAdapter
from aiorx.observers import ObserverAdapter
from aiorx.operators import Map
from aiorx.subjects import Subject, Observable
from http2async.api import Http2Async, Http2AsyncMessage
from http2async.http import HttpServerConnection, HttpIncoming, HttpOutgoing

__logger__: Logger = logging.getLogger(__name__)


class Header(Enum):
    APPLICATION = 'application'
    CONTENT_ENCODING = 'content_encoding'
    CONTENT_TYPE = 'content_type'


class Encoding(Enum):
    BSON = 'application/bson'


class RabbitMQAdapter:
    def __init__(self, loop):
        self.loop = loop
        self.connection = None
        self.channel = None

    async def connect(self, uri='amqp://guest:guest@127.0.0.1/'):
        self.connection = await aio_pika.connect_robust(
            uri, loop=self.loop
        )
        self.channel = await self.connection.channel()


def parse_message(message: aio_pika.IncomingMessage) -> Http2AsyncMessage:
    application = message.headers[Header.APPLICATION.value]
    if application != Http2Async.APPLICATION.value:
        return None
    message_type = message.headers[Http2Async.APPLICATION.value]
    message_data = bson.loads(message.body)
    http2async_message = Http2Async(message_type).clazz.parse(message_data)
    return http2async_message


class ServerSideAdapterConnection(Observer[HttpIncoming], Observable[HttpOutgoing]):
    subject: Subject[HttpOutgoing]
    logger: Logger = __logger__

    @classmethod
    async def create(cls, channel, exchange) -> 'self':
        queue = await channel.declare_queue(
            '', auto_delete=True, exclusive=True,
        )
        instance = cls(queue, exchange)
        await instance.start()
        return instance

    def __init__(self, queue, exchange):
        self.consumer_tag = None
        self.queue = queue
        self.exchange = exchange
        self.subject = Subject()

    async def start(self):
        self.consumer_tag = await self.queue.consume(self.on_message)

    async def close(self):
        await self.queue.cancel(self.consumer_tag)
        await self.queue.delete()

    async def on_next(self, event: HttpIncoming):
        path = getattr(event, 'path', None) or ''
        message = aio_pika.Message(
            reply_to=self.queue,
            content_type=Encoding.BSON.value,
            headers={
                Header.APPLICATION.value: Http2Async.APPLICATION.value,
                Http2Async.APPLICATION.value: event.type,
            },
            body=bson.dumps(asdict(event)),
        )
        await self.exchange.publish(
            routing_key=path,
            message=message,
        )

    async def on_complete(self):
        self.logger.info("Connection complete, closing it...")
        await self.close()

    async def on_error(self, error):
        self.logger.warning("Connection error, closing it...", exc_info=error)
        await self.close()

    async def on_message(self, message: aio_pika.IncomingMessage):
        async with message.process():
            http2async_message = parse_message(message)
            if not http2async_message or not isinstance(http2async_message, (HttpOutgoing,)):
                return
            await self.subject.on_next(http2async_message)
            if not http2async_message.is_final():
                return
            self.logger.info("Final messaged sent, closing it...")
            await self.close()
            await self.subject.on_complete()

    async def subscribe(self, *args, **kwargs) -> Subscription:
        return await self.subject.subscribe(*args, **kwargs)


class ServerSideAdapter(RabbitMQAdapter, Observer[HttpServerConnection]):
    logger: Logger = __logger__

    async def on_next(self, event: HttpServerConnection):
        connection = await ServerSideAdapterConnection.create(
            self.channel, self.exchange,
        )
        self.logger.info("New connection received, opening it...")
        await event.subscribe(connection)
        await connection.subscribe(event)

    def __init__(self, loop, exchange='http'):
        super().__init__(loop=loop)
        self.exchange = None
        self.exchange_name = exchange

    async def connect(self, *args, **kwargs):
        await super().connect(*args, **kwargs)
        self.exchange = await self.channel.declare_exchange(
            self.exchange_name,
            type=aio_pika.ExchangeType.TOPIC,
        )


class ServiceSideAdapter(RabbitMQAdapter):

    def __init__(self, loop, exchange='http'):
        super().__init__(loop=loop)
        self.exchange = exchange
        self.exchange_name = exchange

    def map_message(self, message: aio_pika.IncomingMessage):
        reply_to = message.reply_to

        http2async_message = parse_message(message)

        async def on_next(data):
            response = aio_pika.Message(
                content_type=Encoding.BSON.value,
                headers={
                    Header.APPLICATION.value: Http2Async.APPLICATION.value,
                    Http2Async.APPLICATION.value: data.type,
                },
                body=bson.dumps(asdict(data)) if data else b'',
            )
            await self.channel.default_exchange.publish(
                response, routing_key=reply_to
            )

        return http2async_message, ObserverAdapter.create_from(on_next=on_next)

    def register(self, routing_key='*', queue='', exclusive=False, auto_delete=True) -> Observable[Any]:
        queue_name = queue

        async def _subscribe(observer):
            queue: aio_pika.Queue = await self.channel.declare_queue(
                queue_name,
                exclusive=exclusive,
                auto_delete=auto_delete,
            )
            await queue.bind(self.exchange, routing_key=routing_key)
            consumer_tag = await queue.consume(observer.on_next)

            async def unsubscribe():
                return queue.cancel(consumer_tag)

            return lambda: self.loop.create_task(unsubscribe())

        def subscribe(observer):
            self.loop.create_task(_subscribe(observer))

        return Map(self.map_message)(ObservableAdapter(subscribe))
