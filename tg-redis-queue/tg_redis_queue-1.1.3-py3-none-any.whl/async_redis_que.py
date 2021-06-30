import asyncio
import time
import typing

import aioredis

from tg_redis_queue.base_redis_que import RedisObjectQueueBase, RedisQueItem


class AsyncRedisObjectQueue(RedisObjectQueueBase):
    """
    Asynchronous redis queue that stores JSON-serializable dictionaries

    """

    def __init__(self, name: str, redis_url: typing.Optional[str] = None, _delay_redis_configuration: bool = False):
        super().__init__(name, redis_url)
        self.redis: typing.Optional[aioredis.Redis] = None
        if not _delay_redis_configuration:
            raise RuntimeError(
                "Use await {class_name}.create() instead of using the constructor.".format(
                    class_name=self.__class__.__name__,
                )
            )

    @classmethod
    async def create(cls, name: str, redis_url: typing.Optional[str] = None):
        """Asynchronously creates instance of the class, connecting to redis with aioredis"""
        instance = cls(name, redis_url, _delay_redis_configuration=True)
        instance.redis = await cls.connect_redis_async(instance.redis_url)
        return instance

    @classmethod
    async def connect_redis_async(cls, redis_url: str) -> aioredis.Redis:
        """Used to crate redis client instance on initialization"""
        return await aioredis.create_redis_pool(redis_url)

    async def _update_expiry_time(self) -> None:
        """Updates expiry time in redis, invoked after operations that add to the queue."""
        if self.EXPIRY_TIME:
            await asyncio.gather(
                self.redis.expire(self._get_values_key(), self.EXPIRY_TIME),
                self.redis.expire(self._get_scores_key(), self.EXPIRY_TIME),
            )

    async def get_expiry_time(self) -> typing.Optional[int]:
        """Reports how long until queue expires, in seconds. None if never expires, 0 if already expired."""
        expiry_time = await self.redis.ttl(self._get_values_key())
        return self._convert_expiry_time(expiry_time)

    async def add(self, data: typing.Union[RedisQueItem, dict]) -> None:
        """Add single item to the end of the queue"""
        item = self._prepare_add_item(data)

        # Adding to values first, so that in case of add/remove race every key has value
        # (keys are taken from scores set)

        # HSET sets a single key to value in the hash
        await self.redis.hset(key=self._get_values_key(), field=item.key, value=self.dump_data(item.data))

        # ZADD adds key-score pairs to sorted set (we only need to add one).
        #  exist=aioredis.Redis.ZSET_IF_NOT_EXIST sets `nx=True` and makes redis only add new items,
        #  without updating the score for existing ones (so that if something is queued two times, the earliest place
        #  in the queue is kept by it)
        await self.redis.zadd(
            key=self._get_scores_key(), score=time.time(), member=item.key, exist=aioredis.Redis.ZSET_IF_NOT_EXIST
        )
        await self._update_expiry_time()

    async def move_to_end(self, item: RedisQueItem) -> None:
        """Move an item to end of the queue, if it is still in the queue"""
        # exist=aioredis.Redis.ZSET_IF_EXIST sets `xx=True` and makes redis only update existing items,
        # so if item was already deleted it won't be moved
        await self.redis.zadd(
            key=self._get_scores_key(), score=time.time(), member=item.key, exist=aioredis.Redis.ZSET_IF_EXIST
        )
        await self._update_expiry_time()

    async def get(self) -> typing.Optional[RedisQueItem]:
        """Get single item from the beginning of the queue"""
        result = await self.get_items(start=0, end=0)
        return self._process_get_result(result)

    async def pop(self) -> typing.Optional[RedisQueItem]:
        """Get single item from the beginning of the queue, removing it from the queue"""
        item = await self.get()
        if not item:
            return None

        await self.remove_item(item)
        return item

    async def get_items(self, start: int = 0, end: int = 100) -> typing.List[RedisQueItem]:
        """Get multiple items from the queue.

        NB: number of items returned can be less than end-start even if the queue is full, if there is a race condition
        between reading the queue and deleting items from the queue
        """
        keys = await self.redis.zrange(self._get_scores_key(), start, end)
        if not keys:
            return self._process_get_items_result([])

        results = []
        for key in keys:
            value = await self.redis.hget(self._get_values_key(), key)
            results.append((key, value))

        return self._process_get_items_result(results)

    async def remove_item(self, item: RedisQueItem) -> bool:
        """Removes a queue item, returns true if item was found and deleted, false otherwise"""
        return bool(await self.remove([self._prepare_remove_item(item)]))

    async def prune(self) -> None:
        """Empties queue by removing all queue data from redis"""
        await self.redis.delete(
            self._get_values_key(),
            self._get_scores_key(),
        )

    async def get_total_size(self) -> int:
        """Returns total size of the queue"""
        return await self.redis.zcard(self._get_scores_key())

    async def remove(self, data: typing.List[RedisQueItem]) -> int:
        """Removes multiple items from the queue"""
        keys_to_remove = self._prepare_remove(data)
        scores_deleted: int = await self.redis.zrem(self._get_scores_key(), *keys_to_remove)
        values_deleted: int = await self.redis.hdel(self._get_values_key(), *keys_to_remove)
        return self._process_remove_result(scores_deleted, values_deleted)

    async def cleanup_connection(self) -> None:
        """Disconnects redis and waits for all relevant tasks to be complete"""
        self.redis.close()
        await self.redis.wait_closed()
