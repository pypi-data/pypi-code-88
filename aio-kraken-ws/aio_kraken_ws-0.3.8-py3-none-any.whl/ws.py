""" Manage datasets streams via websockets. """
import asyncio
from collections import defaultdict
from contextlib import suppress
import json
import logging
import websockets


logger = logging.getLogger(__name__)


class Ws:
    """ Connection interface. """

    def __init__(self, url, callback):
        """
        :param str url: websocket server endpoint.
        :param coroutine callback: coroutine triggered on new message.
        """
        self.url = url
        self.callback = callback
        self.datasets = set()
        self._ready_to_read_event = asyncio.Event()  # set when ws is ready to handle messages
        self._read_is_over = asyncio.Event()
        self._ws = None
        self._read_task = None
        self._end_of_read_task = None

    @property
    def connected(self):
        return self._ready_to_read_event.is_set() and not self._read_is_over.is_set()

    async def close(self):
        """ Stop the connection. """
        logger.debug("close connection")
        if self._end_of_read_task:
            self._end_of_read_task.cancel()
            with suppress(asyncio.CancelledError):
                await self._end_of_read_task
        self._end_of_read_task = None
        await self.close_read()

    async def close_read(self):
        if self._ws:
            if self._read_task:
                self._read_task.cancel()
                with suppress(asyncio.CancelledError, websockets.exceptions.ConnectionClosedError):
                    await self._read_task
            if self._ws:
                await self._ws.close()
            self._ws = None
            self._read_task = None
            self._ready_to_read_event = asyncio.Event()
            self._read_is_over = asyncio.Event()

    async def subscribe(self, datasets):
        """ Perform subscribe command.

        :param list((str,int)) datasets: list of (pair name, interval), interval is a time
            period in minutes
        """
        datasets = set(datasets)
        if len(self.datasets.union(datasets)) > 20:
            raise ValueError("Max 20 datasets per connection")
        diff = datasets.difference(self.datasets)
        self.datasets = self.datasets.union(datasets)
        await self._subscribe(diff)

    async def resubscribe(self):
        await self._subscribe(self.datasets)

    async def _subscribe(self, datasets):
        """
        :param set((str,int)) datasets: list of (pair name, interval)
        """
        intervals = self._group_pairs_by_interval(datasets)
        for interval, pairs in intervals.items():
            await self._send({
                "event": "subscribe",
                "pair": pairs,
                "subscription": {
                    "name": "ohlc",
                    "interval": interval
                }
            })

    async def unsubscribe(self, datasets, locally=False):
        """ Perform unsubscribe command.

        :param list((str,int)) datasets: list of (pair name, interval), interval is a time
            period in minutes
        :param bool locally: avoid to send an unsubscribe request to kraken
        """
        inter = self.datasets.intersection(set(datasets))
        if not inter:
            return

        if not locally:
            intervals = self._group_pairs_by_interval(inter)
            for interval, pairs in intervals.items():
                await self._send({
                    "event": "unsubscribe",
                    "pair": pairs,
                    "subscription": {
                        "name": "ohlc",
                        "interval": interval
                    }
                })
        self.datasets = self.datasets.difference(inter)

    async def reset(self):
        """ Close the connection, reconnect & subscribe again. """
        logger.debug("reset ws connection")
        await self.close_read()
        await self.resubscribe()

    async def reset_if_ping_fails(self):
        await self._send({"event": "ping"})

    async def _connect(self):
        """ Acquire websocket connection. """
        logger.debug(f"connecting to {self.url}...")

        while not self._ready_to_read_event.is_set():
            try:
                await self.close_read()
                self._ws = await asyncio.wait_for(websockets.connect(self.url), timeout=5)

                self._read_task = asyncio.create_task(self._read(self._ready_to_read_event))
                await self._ready_to_read_event.wait()

                if self._end_of_read_task is None:
                    self._end_of_read_task = asyncio.create_task(self._end_of_read())
            except websockets.exceptions.InvalidStatusCode as exc:
                if exc.status_code == 429:
                    logger.error("Too many requests. Sleep 60 sec")
                    await asyncio.sleep(60)
            except Exception:
                logger.exception(f"Fail to connect to {self.url}... Retry in a second.")
            await asyncio.sleep(1)

    async def _send(self, data):
        """ Send a command to the server.

        :param dict data:
        """
        logger.debug(f"→ {data}")
        if self._ws is None:
            await self._connect()
        try:
            await self._ws.send(json.dumps(data))
        except websockets.ConnectionClosedError:
            logger.exception(f"Reset ws connection. Fail to send {data} over ws.")
            await self.reset()

    async def _read(self, ready_event):
        """ Background task that handle incoming data from the ws.

        :raises: websockets.exceptions.ConnectionClosed when subscription is over

        ::

            [823,
              ['1568266025.580083',
               '1568266080.000000',
               '0.00009900',
               '0.00009900',
               '0.00009900',
               '0.00009900',
               '0.00009900',
               '568.44750717',
               1],
              'ohlc-1',
              'XTZ/XBT']
        """
        logger.debug("ready to receive data from Kraken.")
        ready_event.set()
        async for message in self._ws:
            logger.debug(f"← {message}")
            try:
                await self.callback(message, ws=self)
            except asyncio.CancelledError:
                raise
            except Exception:
                logger.exception(f"fail to process {message}")
        self._read_is_over.set()

    async def _end_of_read(self):
        """ Task handling ws deconnection. """
        while True:
            await self._read_is_over.wait()
            self._read_is_over.clear()
            try:
                await self.reset()
            except asyncio.CancelledError:
                raise
            except websockets.exceptions.ConnectionClosedOK:
                self._read_is_over.set()
            except websockets.exceptions.InvalidStatusCode as exc:
                if exc.status_code == 429:
                    logger.exception("Too many requests. Sleep 60 sec")
                    await asyncio.sleep(60)
                else:
                    logger.exception("fail to reconnect")
                self._read_is_over.set()
            except Exception:
                logger.exception("fail to reconnect")
                self._read_is_over.set()
            finally:
                await asyncio.sleep(1)

    @staticmethod
    def _group_pairs_by_interval(datasets):
        """ Helper to format a dataset. """
        intervals = defaultdict(list)
        for pair, interval in datasets:
            intervals[interval].append(pair)
        return intervals
