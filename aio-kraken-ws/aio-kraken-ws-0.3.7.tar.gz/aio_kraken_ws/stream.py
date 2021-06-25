""" Manage datasets streams via websockets. """
import asyncio
from collections import namedtuple
from contextlib import suppress
import copy
import json
import logging
import time

from aio_kraken_ws.ws import Ws

logger = logging.getLogger(__name__)


class Stream:
    """ Manage a socket and datasets. """

    def __init__(self, url, callback, reset_period):
        """
        :param str url: websocket server endpoint.
        :param coroutine callback: coroutine triggered on new candle.
        :param int reset_period: time in seconds. The ws connection is reset periodically.
        """
        self.url = url
        self.callback = callback
        self.reset_period = reset_period
        self._datasets_to_add = set()
        self._datasets_to_remove = set()
        self._all_ws = set()
        self._ws = {}  # dataset → ws
        self._builders = {}  # dataset → Builder
        self._worker_task = None
        self._datasets_unsubscribed_tmp = {}
        self._started_event = asyncio.Event()

    @classmethod
    async def create(cls, url, callback, reset_period):
        """ Start to subscribe using ws.

        :param str url: websocket server endpoint.
        :param coroutine callback: coroutine triggered on new candle.
        :param int reset_period: time in seconds. The ws connection is reset periodically.
        :returns: Stream instance.
        """
        stream = cls(url, callback, reset_period)
        await stream.start()
        return stream

    def start(self):
        """ Unlock the worker start. """
        self._started_event.set()

    @property
    def datasets(self):
        """ All datasets currently streamed. """
        return set(self._builders.keys()
                   ).union(self._datasets_to_add
                           ).difference(self._datasets_to_remove)

    @property
    def is_connected(self) -> bool:
        return any(ws.connected for ws in set(self._ws.values()))

    def subscribe(self, datasets):
        """ Make a new subscription.

        :param list((str,int)) datasets: list of (pair name, interval), interval is a time
            period in minutes
        """
        for dataset in datasets:
            self._datasets_to_add.add(dataset)
        # create the worker - locked until start() called
        if self._worker_task is None:
            self._worker_task = asyncio.create_task(self.worker())

    def unsubscribe(self, datasets):
        """ Unsubscribe to datasets.

        :param list((str,int)) datasets: list of (pair name, interval), interval is a time
            period in minutes
        """
        for dataset in datasets:
            self._datasets_to_remove.add(dataset)

    async def close(self):
        """ Stop all subscriptions. """
        logger.debug("close stream")
        if self._worker_task:
            self._worker_task.cancel()
            with suppress(asyncio.CancelledError, asyncio.TimeoutError):
                await asyncio.wait_for(self._worker_task, timeout=2)
        await asyncio.gather(*[ws.close() for ws in self._all_ws])

    async def _message_callback(self, message, ws):
        """ Process incoming messages from the kraken.

        :param str message: data from kraken ws.
        :param Ws ws: websocket that receive the message.
        """
        msg = json.loads(message)
        if isinstance(msg, dict):
            if msg.get("status") == "error":
                # message is an error message...
                logger.error(msg)
                await self._manage_errors(msg)
            if msg.get("event") == "systemStatus":
                # Status sent on connection or system status changes.
                if msg.get("status") == "online":
                    logger.info(msg)
                else:
                    logger.warning(msg)
            return
        try:
            _, data, interval_type, pair = msg
            _, interval = interval_type.split('-')
            interval = int(interval)
        except ValueError:
            logger.debug(f"message ignored: {message}")
        else:
            # message is ohlc data...
            builder = self._get_ohlc_builder(pair, interval)
            builder.new_data(data)

    async def _manage_errors(self, data):
        """ We received an error from the Kraken API. This method handle these errors.

        :param dict data: the kraken payload
        """
        err = data.get("errorMessage", "")
        if (err.startswith("Currency pair not supported") or
                err == "Subscription ohlc interval not supported"):
            # unsubscribe to the dataset
            current_tmp = int(time.time())
            current_tmp -= current_tmp % 60
            pair = data["pair"]
            interval = data["subscription"]["interval"]
            tmp = self._datasets_unsubscribed_tmp.get((pair, interval))
            if tmp == current_tmp:  # avoid error loop: unsubscribe → error
                return
            self._datasets_unsubscribed_tmp[(pair, interval)] = current_tmp
            logger.warning(f"Unsubscribe to ({pair},{interval})")
            await self._unsubscribe([(pair, interval)], locally=True)

    async def _manage_subscriptions(self):
        """ Reset subscriptions to kraken server if necessary to get less than
        20 subscriptions commands (limit from Kraken Server).
        """
        await self._unsubscribe(self._datasets_to_remove)
        self._datasets_to_remove = set()
        if self._datasets_to_add:
            current_datasets = self._builders.keys()
            to_add = self._datasets_to_add.difference(current_datasets)
            await self._subscribe(to_add)
            self._datasets_to_add = self._datasets_to_add.difference(to_add)

    async def _unsubscribe(self, datasets, locally=False):
        """
        :param set datasets:
        :param bool locally: avoid to send an unsubscribe request to kraken
        """
        wss = set()
        for dataset in datasets:
            if dataset in self._ws:
                wss.add(self._ws[dataset])
                del self._ws[dataset]
            self._del_ohlc_builder(dataset)

        async def unsub(ws, datasets, locally):
            try:
                await ws.unsubscribe(datasets, locally)
            except Exception:
                logger.exception(f"Unsubscribe error {datasets}")

        await asyncio.gather(*[unsub(ws, datasets, locally) for ws in wss])

    async def _subscribe(self, datasets):
        """
        :param set datasets:
        """
        datasets = list(datasets)

        async def sub(ws, datasets, num):
            head, datasets = datasets[:num], datasets[num:]
            for dataset in head:
                self._get_ohlc_builder(*dataset)
                self._ws[dataset] = ws
            await ws.subscribe(head)
            return datasets

        # re-use connections
        for ws in self._all_ws:
            if len(datasets) == 0:
                break
            remaining_sub = 20 - len(ws.datasets)
            if remaining_sub >= 1:
                datasets = await sub(ws, datasets, remaining_sub)
        # open new connections
        while datasets:
            ws = Ws(self.url, self._message_callback)
            self._all_ws.add(ws)
            datasets = await sub(ws, datasets, 20)

    async def worker(self):
        """ Periodically run and trigger callback with closed candles builded. """
        if not self._started_event.is_set():
            await self._started_event.wait()
        while True:
            try:
                await self._worker_job()
            except asyncio.CancelledError:
                raise
            except Exception:
                logger.exception("Error doing the job")
                await asyncio.sleep(1)

    async def _worker_job(self):
        """ Actual job. """
        last_subscriptions_update = int(time.time())
        timestamp = int(time.time())
        await self._manage_subscriptions()
        now = int(time.time())
        if now - timestamp < 60:
            await self._sleep_until_next_interval()
        now = int(time.time())
        timestamp = now - (now % 60)

        await asyncio.gather(*[
            self._trigger_callback(timestamp, dataset, builder)
            for dataset, builder in self._builders.items()
            if self.is_new_candle(dataset, timestamp)
        ])

        exc_time = int(time.time()) - now
        if exc_time >= 60:
            logger.warning("Callback took more than a minute to process.")

        for ws in [ws for ws in self._all_ws if len(ws.datasets) == 0]:
            await ws.close()
        self._all_ws = set(filter(lambda ws: len(ws.datasets) > 0, self._all_ws))

        if timestamp - last_subscriptions_update >= self.reset_period:
            # Reset subscriptions.
            last_subscriptions_update = timestamp
            # Reset connection.
            timeout = 30
            try:
                await asyncio.wait_for(
                    asyncio.gather(*[ws.reset() for ws in self._all_ws]),
                    timeout=timeout
                )
            except TimeoutError:
                logger.warning(f"Fail to reset all ws connections within {timeout}s")
        # reset ws if ping request fail
        await asyncio.wait_for(
            asyncio.gather(*[ws.reset_if_ping_fails() for ws in self._all_ws]),
            timeout=30
        )

    async def _trigger_callback(self, timestamp, dataset, builder):
        pair, interval = dataset
        ohlc = builder.get_ohlc(timestamp - interval * 60)
        if ohlc is None:
            return
        logger.info(f"new candle ({pair}, {interval}, *{ohlc})")
        try:
            await self.callback(pair, interval, *ohlc)
        except Exception:
            logger.exception("error with callback processing "
                             f"({pair}, {interval}, *{ohlc})")

    def _get_ohlc_builder(self, pair, interval):
        """
        :param str pair:
        :param int interval:
        :rtype: OhlcBuilder
        """
        try:
            return self._builders[(pair, interval)]
        except KeyError:
            pass

        builder = OhlcBuilder(interval)
        self._builders[(pair, interval)] = builder
        return builder

    def _del_ohlc_builder(self, dataset):
        """
        :param (str, int) dataset: (name, interval)
        """
        try:
            del self._builders[dataset]
        except KeyError:
            pass

    @staticmethod
    def is_new_candle(dataset, timestamp):
        _, interval = dataset
        return timestamp % (interval * 60) == 0

    @staticmethod
    async def _sleep_until_next_interval():
        """ Sleep until next UT interval.
        Precision is 10ms max after the exact date according to the system.
        """
        now = int(time.time() * 100)
        to_sleep = (6000 - (now % 6000)) / 100
        await asyncio.sleep(to_sleep)


Candle = namedtuple("Candle", "t, o, h, l, c, v")


class OhlcBuilder:
    """ Build closed candle for a market from Kraken data. """

    def __init__(self, interval):
        """
        :param int interval: in minute
        """
        self.interval_sec = interval * 60
        self.candle = None  # current candle
        self._next_candle_tmp = self.next_timestamp()
        self.last_candle = None  # latest closed candles

    def next_timestamp(self):
        """ Start time of the next candle. """
        now = int(time.time())
        return now - (now % self.interval_sec) + self.interval_sec

    def new_data(self, data):
        """ Build current candle with data received from the websocket.

        :param data: part of message of the kraken msg that contain market data.
        """
        try:
            tmp, end_tmp, o, h, l, c, _, v, _ = data
        except ValueError:
            logger.debug(f"data ignored: {data}")
            return

        tmp = float(tmp)
        end_tmp = int(float(end_tmp))

        timestamp = end_tmp - self.interval_sec
        candle = Candle(timestamp, float(o), float(h), float(l), float(c), float(v))

        if candle.t >= self._next_candle_tmp:
            self._next_candle_tmp = self.next_timestamp()
            self.last_candle = copy.deepcopy(self.candle or candle)
            self.candle = candle

        self.candle = candle
        logger.debug(f"current candle (ut:{self.interval_sec}):{self.candle}")

    def get_ohlc(self, timestamp):
        """ Get closed candle that start at the given timestamp.

        :param int timestamp:
        :returns: dump of the candle or None
        """
        # we do not have data yet
        if self.candle is None:
            return None

        # the latest close candle match the timestamp
        if self.last_candle is not None and timestamp == self.last_candle.t:
            return self._dump_to_ohlc(self.last_candle)

        # last data receiv is the most up to date.
        if timestamp - self.candle.t <= self.interval_sec:
            return self._dump_to_ohlc(self.candle)

        # no activity
        if timestamp - self.candle.t > self.interval_sec:
            close = self.candle.c
            return [timestamp, close, close, close, close, 0]

        return None

    @staticmethod
    def _dump_to_ohlc(candle):
        return [candle.t, candle.o, candle.h, candle.l, candle.c, candle.v]
