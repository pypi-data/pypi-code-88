import time
import typing

import redis

from tg_redis_queue.base_redis_que import RedisObjectQueueBase, RedisQueItem


class RedisObjectQueue(RedisObjectQueueBase):
    """
    Redis que that stores JSON-serializable dictionaries

    Usage:

    >>> add = RedisObjectQueue(name='example_que')
    >>> add.add({'key': 1})
    >>> add.add({'key': 2})
    >>> add.add({'key': 3})
    >>> add.add({'key': 4})
    >>> add.add({'key': 5})

    >>> worker = RedisObjectQueue(name='example_que')
    >>> items = worker.get_items(end=3)
    >>> print(items)
    >>> [{'key': 1}, {'key': 2}, {'key': 3}]
    >>>
    >>> # Then: process the items
    >>>
    >>> # Finally remove the items from the que
    >>> print(worker.remove(items))
    >>> 3
    """

    # Implementation details:
    #
    # Uses redis sorted sets to store queue item order. Sorted sets are sets sorted by "score" which is provided
    # when item is added to set. Current time is used for score when adding item, so that items that are added
    # earlier come first in the queue.
    #
    # Uses redis hashes to store queue item values. Hashes are maps between the string fields and the string
    # values.
    #
    # Scores set is single source of truth about presence or absence of item in the queue (in case of race conditions)
    #
    # To reliably determine if queue is empty, use `get_total_size` and compare it to 0. `get()` and `pop()` may return
    # None for non-empty queue, due to race conditions between different workers

    def __init__(self, name: str, redis_url: typing.Optional[str] = None):
        super().__init__(name, redis_url)
        self.redis = self.connect_redis(self.redis_url)

    @classmethod
    def connect_redis(cls, redis_url: str):
        """Used to crate redis client instance on initialization"""
        return redis.StrictRedis.from_url(redis_url)

    def _update_expiry_time(self) -> None:
        """Updates expiry time in redis, invoked after operations that add to the queue."""
        if self.EXPIRY_TIME:
            self.redis.expire(self._get_values_key(), self.EXPIRY_TIME)
            self.redis.expire(self._get_scores_key(), self.EXPIRY_TIME)

    def get_expiry_time(self) -> typing.Optional[int]:
        """Reports how long until queue expires, in seconds. None if never expires, 0 if already expired."""
        expiry_time = self.redis.ttl(self._get_values_key())
        return self._convert_expiry_time(expiry_time)

    def add(self, data: typing.Union[RedisQueItem, dict]) -> None:
        """Add single item to the end of the queue"""
        item = self._prepare_add_item(data)

        # Adding to values first, so that in case of add/remove race every key has value
        # (keys are taken from scores set)

        # HSET sets a single key to value in the hash
        self.redis.hset(self._get_values_key(), key=item.key, value=self.dump_data(item.data))

        # ZADD adds key-score pairs to sorted set (we only need to add one).
        # `nx=True` makes redis only add new items, without updating the score for existing ones
        # (so that if something is queued two times, the earliest place in the queue is kept by it)
        self.redis.zadd(self._get_scores_key(), {item.key: time.time()}, nx=True)
        self._update_expiry_time()

    def move_to_end(self, item: RedisQueItem) -> None:
        """Move an item to end of the queue, if it is still in the queue"""
        # `xx=True` makes redis only update existing items, so if item was already deleted it won't be moved
        self.redis.zadd(self._get_scores_key(), {item.key: time.time()}, xx=True)
        self._update_expiry_time()

    def get(self) -> typing.Optional[RedisQueItem]:
        """Get single item from the beginning of the queue"""
        result = self.get_items(start=0, end=0)
        return self._process_get_result(result)

    def pop(self) -> typing.Optional[RedisQueItem]:
        """Get single item from the beginning of the queue, removing it from the queue"""
        item = self.get()
        if not item:
            return None

        self.remove_item(item)
        return item

    def get_items(self, start: int = 0, end: int = 100) -> typing.List[RedisQueItem]:
        """Get multiple items from the queue.

        NB: number of items returned can be less than end-start even if the queue is full, if there is a race condition
        between reading the queue and deleting items from the queue
        """
        keys = self.redis.zrange(self._get_scores_key(), start, end)
        if not keys:
            return self._process_get_items_result([])

        results = []
        for key in keys:
            value = self.redis.hget(self._get_values_key(), key)
            results.append((key, value))

        return self._process_get_items_result(results)

    def remove_item(self, item: RedisQueItem) -> bool:
        """Removes a queue item, returns true if item was found and deleted, false otherwise"""
        return bool(self.remove([self._prepare_remove_item(item)]))

    def prune(self) -> None:
        """Empties queue by removing all queue data from redis"""
        self.redis.delete(
            self._get_values_key(),
            self._get_scores_key(),
        )

    def get_total_size(self) -> int:
        """Returns total size of the queue"""
        return self.redis.zcard(self._get_scores_key())

    def remove(self, data: typing.List[RedisQueItem]) -> int:
        """Removes multiple items from the queue"""
        keys_to_remove = self._prepare_remove(data)
        scores_deleted: int = self.redis.zrem(self._get_scores_key(), *keys_to_remove)
        values_deleted: int = self.redis.hdel(self._get_values_key(), *keys_to_remove)
        return self._process_remove_result(scores_deleted, values_deleted)

    def cleanup_connection(self) -> None:
        # Not required for redis package since it uses connection pool, but provided to make API similar to
        # asynchronous version
        pass
