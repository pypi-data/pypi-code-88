import logging
import os
import threading
from typing import Any

from us_libraries.graphite import statsd
from us_libraries.graphite.constants import STATSDNAME


class StatsClientHelper(object):
    _lock = threading.Lock()
    _instance = None
    _gauge_warning_done = False

    def __new__(cls, *args: Any) -> Any:
        """ Singleton """
        with cls._lock:
            if not cls._instance:
                cls._instance = super(
                    StatsClientHelper, cls).__new__(cls, *args)
                cls._instance.logger = logging.getLogger(__name__)
                cls._instance.__client = None
        return cls._instance

    def __getattr__(self, key: Any) -> Any:
        if self.__client:
            return getattr(self.__client, key)
        else:
            self.logger.warning('attempted to access attribute when stats client '
                                'has not been defined yet')

    def is_configured(self) -> bool:
        """
        Returns True if `configure()` has already been called.
        :rtype: bool
        """
        return self.__client is not None

    def configure(self, prefix: str) -> None:
        with self.__class__._lock:
            os.environ[STATSDNAME] = prefix
            self.__client = statsd.StatsClient(prefix)
