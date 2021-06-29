import time
import signal
import logging
from scrapy import signals
from scrapy.exceptions import DontCloseSpider

from scrapy.http import Request
from . import connection, defaults
from .queue import RabbitMQ

logger = logging.getLogger(__name__)


class RabbitMQScheduler(object):
    """ A RabbitMQ Scheduler for Scrapy. """
    mq_client = None
    stats = None
    crawler = None
    is_closing = False
    parse_faild_times = 0
    queue_name = None
    current_requests_count = 0
    start_idle_time = None

    def __init__(self, connection_url, max_idle_time, spider_parse_failed_times, current_requests,http_requeue_status, *args, **kwargs):
        self.connection_url = connection_url
        self.max_idle_time = max_idle_time
        self.spider_parse_failed_times = spider_parse_failed_times
        self.current_requests = current_requests
        self.http_requeue_status = http_requeue_status

    def __len__(self):
        return len(self.mq_client)

    @classmethod
    def from_settings(cls, settings):
        rabbitmq_url = settings.get('RABBITMQ_CONNECTION_PARAMETERS') or defaults.RABBITMQ_CONNECTION_PARAMETERS
        max_idle_time = settings.get('SCHEDULER_MAX_IDLE_TIME') or defaults.SCHEDULER_MAX_IDLE_TIME
        spider_parse_failed_times = settings.get(
            'SPIDER_PARSE_FAILD_MAX_TIMES') or defaults.SPIDER_PARSE_FAILD_MAX_TIMES
        current_requests = settings.get('CONCURRENT_REQUESTS', 16)
        http_requeue_status = settings.get('HTTP_REQUEUE_STATUS', defaults.HTTP_REQUEUE_STATUS)
        return cls(rabbitmq_url, max_idle_time, spider_parse_failed_times, current_requests,http_requeue_status)

    @classmethod
    def from_crawler(cls, crawler):
        scheduler = cls.from_settings(crawler.settings)
        scheduler.crawler = crawler
        scheduler.stats = crawler.stats
        crawler.signals.connect(scheduler.closing, signal.SIGTERM)  # 接收到停止信号，不再从队列获取数据
        crawler.signals.connect(scheduler.close, signals.spider_closed)  # 关闭爬虫时关闭连接
        crawler.signals.connect(scheduler.spider_idle, signals.spider_idle)  # 最大等待时间
        crawler.signals.connect(scheduler.ack_message, signals.item_scraped)  # 保存item后发送消息确认
        crawler.signals.connect(scheduler.ack_on_item_error,
                                signals.item_error)  # item未能成功经过所有pipeline时，ack并将request发送到错误队列
        crawler.signals.connect(scheduler.ack_on_spider_error, signals.spider_error)  # 解析程序出错时，ack并将request发送到错误队列
        crawler.signals.connect(scheduler._request_left_downloader,
                                signals.request_left_downloader)  # 限制从rabbitmq取出数据的量


        return scheduler

    def spider_idle(self) -> None:
        """"""
        working = self.schedule_next_requests()

        if working:
            self.start_idle_time = None
            raise DontCloseSpider
        else:
            if not self.start_idle_time:
                self.start_idle_time = time.time()

            if time.time() - self.start_idle_time <= self.max_idle_time:
                raise DontCloseSpider

    def schedule_next_requests(self) -> bool:
        """将从RabbitMQ中获取的任务通过 `scrapy.engine` 放入调度器的队列中.
        Returns:
            bool: 当前爬虫是否又有任务处理.
        """
        working = False
        req = self.next_request()
        if req:
            self.crawler.engine.crawl(req, spider=self)
            working = True

        return working

    def open(self, spider):
        self.spider = spider
        self.queue_name = spider.name
        self.error_queue_name = '{}_error'.format(spider.name)
        durable = spider.settings.get("RABBITMQ_DURABLE", True)
        self.mq_client = RabbitMQ(connection_url=self.connection_url, exchange=spider.exchange,
                                  queue_name=self.queue_name, spider=spider, durable=durable)
        if len(self.mq_client):
            spider.log("Resuming crawl (%d requests scheduled)" % len(self.mq_client))

    def enqueue_request(self, request):
        """ Enqueues request to main queues back
        """
        if self.mq_client is not None:
            if self.stats:
                self.stats.inc_value('scheduler/enqueued/rabbitmq',
                                     spider=self.spider)
            self.mq_client.push(self.queue_name, request)
        return True

    def next_request(self):
        """ Creates and returns a request to fire
        """
        self.current_requests_count += 1
        auto_ack = True if self.spider.settings.get('RABBITMQ_CONFIRM_DELIVERY', True) is False else False
        body, channel_id = self.mq_client.pop(auto_ack=auto_ack)
        if not body:
            return
        if self.stats:
            self.stats.inc_value('scheduler/dequeued/rabbitmq',
                                 spider=self.spider)
        if hasattr(self.spider, "_make_request"):
            request = self.spider._make_request(body)
        else:
            request = Request(url=body.decode('utf-8'))
        if self.spider.settings.get('RABBITMQ_CONFIRM_DELIVERY', True):
            request.meta['channel_id'] = channel_id

        logger.debug('Running request {}'.format(request.url))
        return request

    def _request_left_downloader(self, request, spider):
        self.current_requests_count -= 1

    def ack_channel(self, channel_id):
        self.mq_client.ack(channel_id=channel_id)
        logger.debug('消息确认成功，channel_id :%s' % channel_id)

    def nack_channel(self, channel_id):
        self.mq_client.nack(channel_id=channel_id)
        logger.debug('消息确认成功，channel_id :%s' % channel_id)

    def ack_message(self, item, spider, response):
        channel_id = response.meta.get("channel_id")
        self.mq_client.ack(channel_id=channel_id)
        logger.debug('消息确认成功，item from:%s' % response.url)

    def ack_on_item_error(self, item, spider, response):
        self.mq_client.push(self.error_queue_name, response.request)
        channel_id = response.meta.get("channel_id")
        self.mq_client.nack(channel_id=channel_id)
        logger.info('item_error，item from:%s, request has been published error queue.' % response.url)

    def ack_on_spider_error(self, failure, response, spider):
        logger.info(
            'spider parse function failure, request url:%s,request has been published error queue.' % response.url)
        logger.exception(failure)
        self.mq_client.push(self.error_queue_name, response.request)
        channel_id = response.meta.get("channel_id")
        self.mq_client.ack(channel_id=channel_id)
        self.parse_faild_times += 1
        if self.parse_faild_times >= self.spider_parse_failed_times:
            spider.crawler.engine.close_spider(spider=spider, reason="解析程序异常次数达到上限.")


    def has_pending_requests(self):
        return not self.closing

    def closing(self, signal, frame):
        self.is_closing = True

    def close(self, reason):
        if self.mq_client:
            try:
                self.mq_client.close()
                logger.info('关闭rabbitmq连接.')
            except:
                pass
