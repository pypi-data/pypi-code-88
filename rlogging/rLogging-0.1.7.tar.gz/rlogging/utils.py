""" Вспомогательные функции

"""

import multiprocessing as _M
import pathlib as pa
import time
import typing as _T


class SubProcessMixing(object):
    """ Миксин для инициализации доп процесса внутри класса """

    _started: bool

    _queue: _T.Optional[_M.Queue]
    _process: _T.Optional[_M.Process]

    def __init__(self) -> None:
        self._started = False

        self._queue = None
        self._process = None

    def start(self):
        if self._started:
            self.stop()

        self._queue = _M.Queue(-1)
        self._process = _M.Process(target=self.on_process)
        self._process.start()

        self._started = True

    def stop(self):
        self._queue.put(None)
        while not self._queue.empty():
            time.sleep(0.1)

        self._process.join()
        self._process.terminate()

        self._queue.close()
        self._queue.join_thread()

        self._started = False
