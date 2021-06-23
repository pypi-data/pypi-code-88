from __future__ import annotations

import datetime
import json
from typing import Any, Optional, Dict

from .output import Output
from .utils import format_event_timestamp

NONAME = "noname"


class Event(object):
    timestamp: str
    project: str
    env: str
    topic: str
    crid: str
    keyword: Optional[str]
    message: Optional[str]
    extra: Optional[Dict[str, Any]]
    output: Optional[Output]

    """
    单个日志条目
    """

    def __init__(self):
        self.timestamp = format_event_timestamp(datetime.datetime.now())
        self.project = NONAME
        self.env = NONAME
        self.topic = NONAME
        self.crid = "-"
        self.keyword = None
        self.message = None
        self.extra = None
        self.output = None

    def format_extra(self) -> str:
        out = {
            "c": self.crid,
        }
        if self.keyword is not None:
            out["k"] = self.keyword
        if self.extra is not None:
            out["x"] = self.extra
        return str(json.dumps(out))

    def submit(self):
        """
        提交日志条目，让日志条目生效

        :return: None
        """
        if self.output is not None:
            self.output.append_event(self)

    def commit(self) -> None:
        """
        submit 别名

        :return: None
        """
        self.submit()

    def add_keyword(self, keyword: str) -> Event:
        """
        添加关键字，会以逗号分隔的形式添加到 keyword 字段上

        :param keyword: 关键字
        :return: 自己
        """
        if str is None:
            return self
        if self.keyword is None:
            self.keyword = keyword
        else:
            self.keyword = self.keyword + "," + keyword
        return self

    def add_extra(self, key: str, val: Any) -> Event:
        """
        添加额外键值对，需与日志系统维护人协商

        :param key: 键
        :param val: 值
        :return: 自己
        """
        if self.extra is None:
            self.extra = {}
        self.extra[key] = val
        return self

    def k(self, *keywords: str) -> Event:
        """
        添加多个 Keyword

        :param keywords: 关键字
        :return: 自己
        """
        for keyword in keywords:
            self.add_keyword(keyword)
        return self

    def x(self, key: str, val: Any) -> Event:
        """
        add_extra 的别名

        :param key: 键
        :param val: 值
        :return: 自己
        """
        return self.add_extra(key, val)

    def msg(self, message: str) -> None:
        """
        设置文本日志内容，并立刻提交日志

        :param message: 文本内容
        :return: None
        """
        self.message = message
        self.submit()
