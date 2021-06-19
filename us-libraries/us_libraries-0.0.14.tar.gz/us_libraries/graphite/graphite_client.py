import logging
from typing import Dict, Optional

import graphyte

logger = logging.getLogger(__name__)


class GraphiteClient:

    def __init__(self, url: str = 'graphite', interval: int = 60, prefix: Optional[str] = None) -> None:
        graphyte.init(url, prefix=prefix, interval=interval)

    @staticmethod
    def send(stats: str, value: float, tags: Optional[Dict] = {}) -> None:
        try:
            graphyte.send(stats, value=value, tags=tags)
        except Exception as e:
            logger.error('an error occurred when sending to graphite')
            logger.exception(e)
