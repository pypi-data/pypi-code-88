import typing as _T

import zmq
from rlogging.handlers import BaseHandler
from rlogging.printers import PrintersPool
from rlogging.records import Record


class DaemonProcessHandler(BaseHandler):
    """ Хендлер, работающий в отдельном потоке.

    При инициализации хендлера, создается демон.
    При создании лога, он в отправляется в хендлер (в фиг знает какой процесс) и программа продолжит выполнение.

    Чтобы убить демона, нужно обратиться к Экзорцисту.

    Для использования функционала демона, нужна библиотека `zmq`.

    """

    zmqSocketBindString: str

    context: _T.Optional[zmq.Context]
    socket: _T.Optional[zmq.Socket]

    def __init__(self, zmqSocketBindString: str = 'tcp://127.0.0.1:4400'):
        self.context = None
        self.socket = None

        self.zmqSocketBindString = zmqSocketBindString
        self.printersPool = PrintersPool([])

    def start(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUSH)
        self.socket.connect(self.zmqSocketBindString)

        self._started = True

    def stop(self):
        self.socket.disconnect(self.zmqSocketBindString)

        self._started = False

    def send(self, record: Record):
        self.socket.send_pyobj(record)
