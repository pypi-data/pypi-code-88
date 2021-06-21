# -*- coding:utf-8 -*-
"""
@desc: 
"""
from scrapy import Spider, Request
from scrapy.utils.reqser import request_from_dict

from . import picklecompat

class RabbitMQSpider(Spider):
    def _make_request(self, body, *args, **kwargs):
        try:
            request = request_from_dict(picklecompat.loads(body), self)
        except Exception as e:
            body = body.decode()
            request = Request(body, callback=self.parse, dont_filter=True)
        return request