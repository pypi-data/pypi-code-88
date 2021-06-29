# -*- coding:utf-8 -*-
"""
@desc: 爬虫类中定义类属性 cookies，类型为str或dict,启动时自动解析
"""
class CookiesDownloaderMiddleware(object):

    def __init__(self, cookies):
        self.cookies = cookies

    @classmethod
    def from_crawler(cls, crawler):
        cookies = getattr(crawler.spider, "cookies", None)
        if isinstance(cookies, str):
            cookies = cls.get_cookie_from_str(cookies)
        elif isinstance(cookies, dict):
            cookies = cookies
        else:
            cookies = None
        return cls(cookies)


    def process_request(self, request, spider):
        """
        针对暗网爬虫的专用暗网代理，如果是Selenium发出的请求则忽略
        :param request:
        :param spider:
        :return:
        """
        if self.cookies:
            request.cookies = self.cookies
        return None

    @staticmethod
    def get_cookie_from_str(cookie_str: str):
        """
        translate cookies_str to dict
        """
        return {cookie.split("=", maxsplit=1)[0]: cookie.split("=", maxsplit=1)[1] for cookie in cookie_str.split("; ")}