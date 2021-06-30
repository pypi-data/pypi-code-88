import json
import logging
import typing
import uuid
from dataclasses import dataclass, field


@dataclass
class RedisQueItem:
    """
    Representation of single queue item.

    :param data: queue item data, as dict that can be json-dumped
    :param key: identifier of item that is unique. Random is generated if not provided. Used to avoid
    adding duplicate entries to the queue.
    """

    data: dict
    key: str = field(default_factory=lambda: uuid.uuid4().hex)


class RedisObjectQueueBase:
    """Base class for redis queue, provides uniform way of handling data. Actual queries are delegated to subclasses
    that use synchronous and asynchronous redis clients and respectively provide synchronous and asynchronous APIs to
    manage the queue."""

    # Expiry time in seconds, if None queue won't expire (and then you are responsible to clean it up with `prune()`)
    EXPIRY_TIME = 60

    def __init__(self, name: str, redis_url: typing.Optional[str] = None):
        # Name, used to identify the queue. Queues with same name are the same queue
        self._name = name

        # Redis URL, like "redis://localhost:6379/1
        self.redis_url = redis_url or self._get_redis_url()

    def _get_redis_url(self) -> str:
        """Override this so that redis_url doesn't have to be passed over to every instance"""
        raise RuntimeError(
            "Subclass {class_name} and override `_get_redis_url` or provide redis_url when creating the instance.".format(
                class_name=self.__class__.__name__,
            ),
        )

    @classmethod
    def dump_data(cls, data: typing.Dict) -> bytes:
        """Serialize data to be put into redis. Uses json by default. You can override this method to use something
        else, like pickle.

        Be sure to override load_data as well if you override this."""
        return json.dumps(data).encode("utf-8")

    @classmethod
    def load_data(cls, data: bytes) -> typing.Dict:
        """Un-serialize data coming from redis back to dict. Uses json by default. You can override this method to
        use something else, like pickle.

        Be sure to override dump_data as well if you override this."""
        return json.loads(data.decode("utf-8"))

    def _get_scores_key(self) -> str:
        """Redis key for sorted set with the queue ordering scores"""
        return f"{self._name}:scores"

    def _get_values_key(self) -> str:
        """Redis key for hash with queue item values"""
        return f"{self._name}:values"

    # Most of the following methods are used by sync or async versions of the classes, so for better understanding
    # of how they are supposed to work refer to respective subclasses.

    def _convert_expiry_time(self, raw_expiry_time: int) -> typing.Optional[int]:
        """
        Redis returns two special values for expiry time, here we convert them to be more comprehensive.

        :returns: None if neve expires, 0 if expired, int number of seconds to expire otherwise
        """
        # -1 - never expires
        if raw_expiry_time == -1:
            return None

        # -2 - does not exist, so practically expired (or not yet created)
        if raw_expiry_time == -2:
            return 0 if self.EXPIRY_TIME is not None else None

        return raw_expiry_time

    def _prepare_add_item(self, data: typing.Union[RedisQueItem, dict]) -> RedisQueItem:
        """Prepares item for being added to the queue - wrapping it into RedisQueItem if necessary"""
        if not isinstance(data, RedisQueItem):
            item = RedisQueItem(data)
        else:
            item = data

        logging.debug("Adding data to que %s: %r", self._name, item.data)

        return item

    def _process_get_result(self, result: typing.List[RedisQueItem]):
        """Used to convert results of get_results function for get_result function"""
        if result:
            return result[0]

        return None

    def _prepare_remove_item(self, item: RedisQueItem) -> RedisQueItem:
        """Validates arguments for remove_item"""
        if not isinstance(item, RedisQueItem):
            raise TypeError(f"Expected RedisQueItem, found {type(item)}.")

        return item

    def _prepare_remove(self, data: typing.List[RedisQueItem]) -> typing.List[str]:
        """Validates arguments for remove and creates the list of keys that can be sent to redis for removal
        Removes the queue items, returns number of items removed."""
        if not isinstance(data, list):
            raise TypeError(f"Expected data to be a list, found {type(data)}.")

        keys_to_remove = []

        for item in data:
            if not isinstance(item, RedisQueItem):
                raise TypeError(f"Expected only RedisQueItem as data items, found {type(item)}.")

            keys_to_remove.append(item.key)

        return keys_to_remove

    def _process_remove_result(self, scores_deleted: int, values_deleted: int):
        """Checks the result of removal for consistency (and warns of possible race conditions)"""
        if scores_deleted != values_deleted:
            logging.warning(
                "Deleted %d scores, but %d values, possible race condition.",
                scores_deleted,
                values_deleted,
            )

        return scores_deleted

    def _process_get_items_result(self, pairs: typing.List[typing.Tuple[bytes, bytes]]) -> typing.List[RedisQueItem]:
        """Converts strings returned from redis to RedisQueItem instances"""
        if not pairs:
            return []

        result = []
        for key, value in pairs:
            # It is possible that due to read/delete race, the value is already gone - then, skip it
            if value:
                key_string = key.decode("utf-8")
                result.append(RedisQueItem(self.load_data(value), key=key_string))

        return result
