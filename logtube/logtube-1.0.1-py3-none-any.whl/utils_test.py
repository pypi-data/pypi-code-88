import datetime
import logging

from .utils import TopicAware, format_event_timestamp

log = logging.getLogger()


def test_topic_aware():
    ta = TopicAware(["*", "-a", "-b"])
    assert not ta.is_enabled("a")
    assert not ta.is_enabled("b")
    assert ta.is_enabled("c")

    ta = TopicAware(["*"])
    assert ta.is_enabled("a")
    assert ta.is_enabled("b")
    assert ta.is_enabled("c")

    ta = TopicAware([])
    assert not ta.is_enabled("a")
    assert not ta.is_enabled("b")
    assert not ta.is_enabled("c")

    ta = TopicAware(["a", "b"])
    assert ta.is_enabled("a")
    assert ta.is_enabled("b")
    assert not ta.is_enabled("c")


def test_format_event_timestamp():
    log.debug(format_event_timestamp(datetime.datetime.now()))
