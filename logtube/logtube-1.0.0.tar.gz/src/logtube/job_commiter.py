from __future__ import annotations

import time
from typing import Optional, List, Dict, Any

from .event import Event


class JobCommitter(object):
    logger: "Logger"
    job_name: Optional[str]
    job_id: Optional[str]
    keywords: Optional[List[str]]
    extra: Optional[Dict[str, Any]]
    started_at: int

    def __init__(self, logger: "Logger"):
        self.logger = logger
        self.job_name = None
        self.job_id = None
        self.keywords = None
        self.extra = None
        self.started_at = 0

    def set_job_name(self, job_name: Optional[str]) -> JobCommitter:
        self.job_name = job_name
        return self

    def set_job_id(self, job_id: Optional[str]) -> JobCommitter:
        self.job_id = job_id
        return self

    def add_keyword(self, keyword: str) -> JobCommitter:
        if self.keywords is None:
            self.keywords = []
        self.keywords.append(keyword)
        return self

    def add_extra(self, key: str, val: Any) -> JobCommitter:
        if self.extra is None:
            self.extra = {}
        self.extra[key] = val
        return self

    def decorate_event(self, e: Event):
        if self.job_id is not None:
            e.x("job_id", self.job_id)
        if self.job_name is not None:
            e.x("job_name", self.job_name)
        if self.keywords is not None:
            e = e.k(*self.keywords)
        if self.extra is not None:
            for (k, v) in self.extra.items():
                e = e.x(k, v)

    def mark_start(self) -> JobCommitter:
        self.started_at = int(time.time() * 1000)
        e: Event = self.logger.event("job")
        self.decorate_event(e)
        e.x("started_at", self.started_at)
        e.x("result", "started")
        e.submit()
        return self

    def mark_end(self, success: bool, message: str) -> JobCommitter:
        ended_at = int(time.time() * 1000)
        e: Event = self.logger.event("job")
        self.decorate_event(e)
        e.x("started_at", self.started_at)
        e.x("ended_at", ended_at)
        e.x("duration", ended_at - self.started_at)
        if success:
            e.x("result", "ok")
        else:
            e.x("result", "failed")
        e.message = message
        e.submit()
        return self
