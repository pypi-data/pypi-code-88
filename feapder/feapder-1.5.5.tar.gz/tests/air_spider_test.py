# -*- coding: utf-8 -*-
"""
Created on 2021-06-16 14:19:54
---------
@summary:
---------
@author: liubo
"""

import feapder


class AirSpiderTest(feapder.AirSpider):
    __custom_setting__ = dict(
        # SPIDER
        SPIDER_THREAD_COUNT=1,  # 爬虫并发数
        SPIDER_SLEEP_TIME=10,  # 下载时间间隔（解析完一个response后休眠时间）
    )

    def start_requests(self):
        yield feapder.Request("https://www.baidu.com#1")
        yield feapder.Request("https://www.baidu.com#2")

    def parse(self, request, response):
        print(response)


if __name__ == "__main__":
    AirSpiderTest().start()
