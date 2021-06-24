
import logging
import sys
import typing as _T

import zmq
from rlogging.printers import PrintersPool

pylogger = logging.getLogger(__name__)


class BaseDaemon(object):
    """ Базовый класс демона """

    daemonName: str = None

    printersPool: PrintersPool

    def __init__(self):
        pass

        # daemonName = self.daemonName or self.__class__.__name__
        # pIdFile = pa.Path('/tmp/rlogging/pids/{0}.pid'.format(
        #     daemonName
        # ))

        # if not pIdFile.parent.is_dir():
        #     pIdFile.parent.mkdir(parents=True)

        # super().__init__(pidfile=pIdFile)

    def setup(self):
        """ Настройка демона.

        Тут задаются принтеры, которые будут сохранять логи.

        Raises:
            AttributeError: Демон не переопределил метод настройки

        """

        if self:
            raise AttributeError('Демон "{0}" не переопределил метод настройки'.format(
                self.__class__.__name__
            ))

    def run(self):
        """ Запуск демона.

        Raises:
            AttributeError: Демон не переопределил метод запуска

        """

        if self:
            raise AttributeError('Демон "{0}" не переопределил метод запуска'.format(
                self.__class__.__name__
            ))

    def stop(self):
        pass

    def start_printers(self):
        """ Запуск всех принтеров """

        for printer in self.printersPool.printers:
            printer.start()

    def stop_printers(self):
        """ Остановка всех принтеров """

        for printer in self.printersPool.printers:
            printer.stop()

    @classmethod
    def start(cls):
        """ Запуск """

        daemon = cls()

        daemon.setup()
        daemon.start_printers()

        try:
            daemon.run()

        except Exception as ex:
            print()
            print('ERROR: ', ex)
            print()

        daemon.stop()

    @classmethod
    def __cli(cls):
        """ Обработка параметров командной строки

        Raises:
            SyntaxError: Введены не валидные данные

        """

        daemon = cls()

        argv = sys.argv[1:]

        if argv[0] != 'daemon':
            return

        if len(argv) == 1:
            print('Доступные команды: [start, stop, restart]')
            exit(1)

        if argv[1] == 'start':
            daemon.start()

        elif argv[1] == 'stop':
            daemon.stop()

        elif argv[1] == 'restart':
            daemon.restart()

        else:
            raise SyntaxError('Не валидные команды')


class ZMQDaemon(BaseDaemon):
    """ Демон создающий и обрабатывающий ZMQ очередь """

    zmqSocketBindString = 'tcp://127.0.0.1:4400'

    context: _T.Optional[zmq.Context]
    socket: _T.Optional[zmq.Socket]

    def __init__(self):
        super().__init__()
        self.context = None
        self.socket = None

    def processing(self):
        """ Получение новых логов из очереди и передача их в принтер """

        while True:
            pylogger.info('while True')

            record = self.socket.recv_pyobj()

            if record is None:
                break

            pylogger.info(str(record.__dict__))

            self.printersPool.print(record)
            pylogger.info(str(1))

    def connect(self):
        pylogger.info('connect {0}'.format(
            self.zmqSocketBindString
        ))

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PULL)
        self.socket.bind(self.zmqSocketBindString)

    def disconnect(self):
        pylogger.info('disconnect {0}'.format(
            self.zmqSocketBindString
        ))

        self.socket.unbind(self.zmqSocketBindString)
        self.context.destroy()

    def run(self):
        pylogger.info('run')

        self.connect()
        self.processing()

    def stop(self):
        self.stop_printers()
        self.disconnect()
