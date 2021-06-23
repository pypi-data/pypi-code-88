from __future__ import annotations

from typing import Dict, Optional, Any, List

from .core import CoreProvider
from .event import Event
from .job_commiter import JobCommitter


class Logger(object):
    """
    Logger 用于制造日志条目，并允许预先为日志增加关键字，额外键值等
    """

    keywords: Optional[List[str]]
    extra: Optional[Dict[str, Any]]
    crid: Optional[str]
    cp: CoreProvider

    def __init__(self, cp: CoreProvider):
        self.keywords = None
        self.extra = None
        self.crid = None
        self.cp = cp

    def event(self, topic: str) -> Event:
        """
        创建一个日志条目，使用方必须手动调用 commit 以提交该条日志

        :param topic:
        :return:
        """
        e = self.cp.get_core().create_event()
        e.topic = topic
        if self.crid is not None:
            e.crid = self.crid
        if self.keywords is not None:
            e = e.k(*self.keywords)
        if self.extra is not None:
            for (k, v) in self.extra.items():
                e = e.x(k, v)
        return e

    def add_keyword(self, *keywords: str) -> Logger:
        """
        添加额外关键字，之后该 Logger 产生的日志都会附带该关键字

        :param keywords:
        :return:
        """
        if self.keywords is None:
            self.keywords = []
        self.keywords.append(*keywords)
        return self

    def add_extra(self, key: str, val: Any) -> Logger:
        """
        添加额外键值对，之后该 Logger 产生的日志都会附带该键值对

        :param key:
        :param val:
        :return:
        """
        if self.extra is None:
            self.extra = {}
        self.extra[key] = val
        return self

    def topic(self, topic: str) -> Event:
        """
        event 方法的别名

        :param topic:
        :return:
        """
        return self.event(topic)

    def job(self) -> JobCommitter:
        """
        创建一条任务日志，提供一些糖方法

        :return:
        """
        return JobCommitter(self)

    def log(self, topic: str, keyword: str, message: str) -> None:
        """
        产生一条纯文本日志，并立即提交

        :param topic: 主题
        :param keyword: 关键字
        :param message: 纯文本内容
        :return: Non
        """
        self.event(topic).add_keyword(keyword).msg(message)

    def debug(self, keyword: str, message: str):
        """
        产生纯文本 debug 日志，并立即提交

        :param keyword:
        :param message:
        :return:
        """
        self.log("debug", keyword, message)

    def info(self, keyword: str, message: str):
        """
        产生纯文本 info 日志，并立即提交

        :param keyword:
        :param message:
        :return:
        """
        self.log("info", keyword, message)

    def warn(self, keyword: str, message: str):
        """
        产生纯文本 warn 日志，并立即提交

        :param keyword:
        :param message:
        :return:
        """
        self.log("warn", keyword, message)

    def error(self, keyword: str, message: str):
        """
        产生纯文本 error 日志，并立即提交

        :param keyword:
        :param message:
        :return:
        """
        self.log("error", keyword, message)

    def fatal(self, keyword: str, message: str):
        """
        产生纯文本 fatal 日志，并立即提交

        :param keyword:
        :param message:
        :return:
        """
        self.log("fatal", keyword, message)
