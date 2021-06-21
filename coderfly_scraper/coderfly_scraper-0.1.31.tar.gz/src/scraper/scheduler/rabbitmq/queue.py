# -*- coding:utf-8 -*-
"""
@desc: 
"""
import logging
import uuid
import pika
from pika.adapters.blocking_connection import BlockingChannel

from scrapy.utils.reqser import request_to_dict

from . import picklecompat

logger = logging.getLogger(__name__)
pika_logger = logging.getLogger('pika').setLevel(logging.ERROR)


class RabbitMQ:
    connection = None
    channel_pool = {}

    def __init__(self, connection_url, queue_name, spider=None, exchange="", durable=True):
        self.connection_url = connection_url
        self.queue_name = queue_name
        self.spider = spider
        self.exchange = exchange
        self.durable = durable
        self.serializer = picklecompat
        self.connect()

    def __len__(self):
        """Return the length of the queue"""
        declared = self.connection.channel().queue_declare(self.queue_name, passive=True)
        return declared.method.message_count

    def _encode_request(self, request):
        """Encode a request object"""
        obj = request_to_dict(request, self.spider)
        return self.serializer.dumps(obj)

    def push(self, queue_name, request):
        channel = self.connection.channel()
        channel.queue_declare(queue=queue_name, durable=self.durable)
        channel.basic_publish(self.exchange, queue_name,
                              body=self._encode_request(request),
                              properties=pika.BasicProperties(
                                  delivery_mode=2  # 消息持久化
                              ))
        channel.close()

    def pop(self, auto_ack=False):
        """从队列中获取一条消息"""
        channel: BlockingChannel = self.connection.channel()
        channel.queue_declare(self.queue_name, passive=True, durable=self.durable)
        cid = uuid.uuid4().__str__()
        self.channel_pool[cid] = channel
        method, properrties, body = channel.basic_get(queue=self.queue_name, auto_ack=auto_ack)
        logger.debug('获取一条消息...')
        return body, cid

    def ack(self, channel_id: int):
        """消息确认"""
        channel: BlockingChannel = self.channel_pool.pop(channel_id, None)
        if channel:
            if not channel.is_closed:
                channel.basic_ack(1)
                channel.close()
                logger.debug('ack success.')
            else:
                logger.debug('ack faild, channel have cloesd.')
        else:
            logger.debug('ack faild, channel does not exists.')

    def nack(self, channel_id: int):
        channel: BlockingChannel = self.channel_pool.pop(channel_id, None)
        if channel:
            if not channel.is_closed:
                channel.basic_nack(1, requeue=True)
                channel.close()
                logger.debug('nack success.')
            else:
                logger.debug('nack faild, channel have cloesd.')
        else:
            logger.debug('nack faild, channel does not exists.')

    def connect(self):
        """connect to rabbitmq server and declare queue"""
        connection = pika.BlockingConnection(pika.URLParameters(self.connection_url))
        channel = connection.channel()
        channel.queue_declare(queue=self.queue_name, durable=self.durable)
        if self.spider.settings.get('RABBITMQ_CONFIRM_DELIVERY', True):
            channel.confirm_delivery()
        self.connection = connection

    def close(self):
        self.channel_pool.clear()
        logger.info('channel pool has clear...')
        if not self.connection.is_closed:
            self.connection.close()
        logger.info('connection has closed....')
