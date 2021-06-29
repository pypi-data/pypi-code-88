#!/usr/bin/env python3

import asyncio
import logging

from .component import Component, LocalEvents
from .message import Message

_l = logging.getLogger(__name__)


class Pipe(Component, LocalEvents):
    """Message transit mechanism."""

    def __aiter__(self):
        return self._receiver()

    def __str__(self):
        return f'<{self.__class__.__name__} {self.id}>'

    async def send(self, message, **kwargs):
        raise NotImplementedError(f'{self}.send()')

    async def sender(self, messages):
        raise NotImplementedError(f'{self}.sender()')

        yield

    def drop(self, message):
        if isinstance(message, Message):
            try:
                # self.debug(f'--- dropping {message}')
                message.drop(self)
            except Exception:
                __import__('pudb').set_trace()
                raise

    async def receive(self, **kwargs):
        raise NotImplementedError(f'{self}.receive()')

    async def _receiver(self):
        self.status = 'running'
        try:
            async for message in self.receiver():
                if not self.running:
                    break

                yield message

        except Exception:
            self.status = 'aborted'
            raise

        else:
            self.status = 'finished'
        finally:
            self.status = 'exited'

    async def receiver(self):
        raise NotImplementedError(f'{self}.receiver()')


class Sentinel:
    """Used to signal the end of transmission of a queue."""

    def __init__(self, type_):
        self.type = type_

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'__{self.type}__'

    def __bytes__(self):
        return self.__str__().encode()

    def __eq__(self, other):
        if isinstance(other, bytes):
            return self.__bytes__() == other

        elif isinstance(other, str):
            return self.__str__() == other

        else:
            return self is other


EOT = Sentinel('EOT')


class PipeRef:
    """Holds a node channel reference that can later on be resolved to the actual pipe object."""

    def __init__(self, node, msgbox, channel):
        self.node = node
        self.msgbox = msgbox
        self.channel = channel

    def __str__(self):
        return f'<{type(self).__name__} {self.node.key}.{self.msgbox}:{self.channel}>'

    def __repr__(self):
        return str(self)

    def resolve(self):
        return self.node[self.msgbox][self.channel].instance


class Manifold(Pipe):
    def configure(self, buffersize=1, **channels):
        self.buffersize = buffersize
        self.channels = channels
        self.children = list(channels.values())
        self.ready = asyncio.Event()
        return channels

    def __str__(self):
        return '<%s [%s]>' % (self.__class__.__name__,
                              ', '.join('%s:%s' % (n, p.id)
                                        for n, p in self.channels.items()))
        # ', '.join('%s:%s' % (n, p.get('id', f'--{p}'))

    _dependent_statuses = set()

    def start(self):
        return asyncio.gather(super().start(), *(c.start() for c in self.children))

    async def Xrun(self):
        await super().run()
        self.status = 'running'
        # self.debug('- starting pipes')
        # __import__('pudb').set_trace()
        for pipe in self.channels.values():
            if not pipe.running:
                self.debug(f'*** pipe not running {pipe} {pipe.start}')
                # await pipe.start()
            else:
                self.debug(f'*** pipe already running {pipe}')
        # self.debug('- watching pipes')
        # running = True
        # while running:
        #     await asyncio.sleep(0.1)
        #     running = False
        #     for pipe in self.channels.values():
        #         running = running or pipe.running
        #         if running:
        #             break
        # self.debug('- pipes stopped')
        self.ready.set()


class NullPipe(Pipe):
    async def send(self, message, **kwargs):
        self.drop(message)

    async def receive(self, wait=True):
        return self.running and await asyncio.sleep(1 / self.settings.get('rate', 10 ** 0))

    async def receiver(self):
        while await self.receive() or self.running:
            yield


# class FeederPipe(Pipe):
class DataPipe(Pipe):
    """Outputs preloaded messages, in order."""

    def configure(self, messages=None):
        self.messages = [Message(**m) for m in reversed(messages or [])]
        return dict(messages=len(self.messages))

    async def receive(self, wait=True):
        try:
            return self.messages.pop()

        except IndexError:
            self.status = 'finished'
            return EOT

    async def receiver(self):
        while self.running:
            try:
                yield await self.receive()

            except IndexError:
                break


class QueuePipe(Pipe):
    def configure(self, queue=None, maxsize=1):
        self._queue = queue or asyncio.Queue(maxsize=maxsize)

    async def send(self, *args, **kwargs):
        return await self._queue.put(*args, **kwargs)

    async def receive(self, wait=True):
        if not self.running:
            # self.debug('*** not receiving since not running')
            return EOT

        if wait:
            # self.debug('*** reading from queue (waiting)')
            message = await self._queue.get()
            # self.debug(f'*** read from queue: {message}')
        else:
            # self.debug('*** reading from queue (no wait)')
            message = self._queue.get_nowait()
        if message == EOT:
            self.status = 'finished'
        self._queue.task_done()
        return message

    async def receiver(self):
        while self.running:
            yield await self.receive()
