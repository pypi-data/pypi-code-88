from .event import Event
from .output import ConsoleOutput


def test_console_output():
    o = ConsoleOutput({
        "topics": ["*", "-debug"],
    })
    e = Event()
    e.project = "logtube-py-test"
    e.env = "test"
    e.crid = "xxx"
    e.topic = "info"
    e.add_keyword("a")
    e.add_keyword("b")
    e.add_extra("hello", "world")
    e.add_extra("hello", "world2")
    o.append_event(e)
