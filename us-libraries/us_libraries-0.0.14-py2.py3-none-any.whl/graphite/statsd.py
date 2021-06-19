from __future__ import with_statement

from us_libraries.graphite.graphite_client import GraphiteClient

__all__ = ['StatsClient']


class StatsClient(object):
    """A client for statsd."""
    def __init__(self, prefix: str = None) -> None:
        """Create a new client."""
        self._prefix = prefix
        self._graphite = GraphiteClient(prefix=prefix)

    def timing(self, stat: str, delta: int) -> None:
        """Send new timing information. `delta` is in milliseconds."""
        self._send_stat(stat, delta)

    def incr(self, stat: str, count: int = 1) -> None:
        """Increment a stat by `count`."""
        self._send_stat(stat, count)

    def decr(self, stat: str, count: int = 1) -> None:
        """Decrement a stat by `count`."""
        self.incr(stat, -count)

    def set(self, stat: str, value: int) -> None:
        """Set a set value."""
        self._send_stat(stat, value)

    def _send_stat(self, stat: str, value: int) -> None:
        self._graphite.send(stat, value)
