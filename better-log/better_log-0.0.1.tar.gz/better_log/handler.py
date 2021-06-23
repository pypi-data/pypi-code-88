import sys
import time
import logging
import os
import traceback

os_name = os.name


def very_nb_print(*args, sep=' ', end='\n', file=None):
    """
    超流弊的print补丁
    :param x:
    :return:
    """
    # 获取被调用函数在被调用时所处代码行数
    line = sys._getframe().f_back.f_lineno
    # 获取被调用函数所在模块文件名
    file_name = sys._getframe(1).f_code.co_filename
    # sys.stdout.write(f'"{__file__}:{sys._getframe().f_lineno}"    {x}\n')
    args = (str(arg) for arg in args)  # REMIND 防止是数字不能被join
    sys.stdout.write(f'"{file_name}:{line}"  {time.strftime("%H:%M:%S")}  \033[0;94m{"".join(args)}\033[0m\n')  # 36  93 96 94


class ColorHandler(logging.Handler):
    """
    A handler class which writes logging records, appropriately formatted,
    to a stream. Note that this class does not close the stream, as
    sys.stdout or sys.stderr may be used.
    """

    terminator = '\n'
    bule = 96 if os_name == 'nt' else 36
    yellow = 93 if os_name == 'nt' else 33

    def __init__(self, stream=None, is_pycharm_2019=False):
        """
        Initialize the handler.

        If stream is not specified, sys.stderr is used.
        """
        logging.Handler.__init__(self)
        if stream is None:
            stream = sys.stdout  # stderr无彩。
        self.stream = stream
        self._is_pycharm_2019 = is_pycharm_2019
        self._display_method = 0

    def flush(self):
        """
        Flushes the stream.
        """
        self.acquire()
        try:
            if self.stream and hasattr(self.stream, "flush"):
                self.stream.flush()
        finally:
            self.release()

    def emit(self, record):
        """
        Emit a record.

        If a formatter is specified, it is used to format the record.
        The record is then written to the stream with a trailing newline.  If
        exception information is present, it is formatted using
        traceback.print_exception and appended to the stream.  If the stream
        has an 'encoding' attribute, it is used to determine how to do the
        output to the stream.
        """
        # noinspection PyBroadException
        try:
            msg = self.format(record)
            stream = self.stream
            if record.levelno == 10:
                # msg_color = ('\033[0;32m%s\033[0m' % msg)  # 绿色
                msg_color = ('\033[%s;%sm%s\033[0m' % (self._display_method, 34 if self._is_pycharm_2019 else 32, msg))  # 绿色
            elif record.levelno == 20:
                msg_color = ('\033[%s;%sm%s\033[0m' % (self._display_method, self.bule, msg))  # 青蓝色 36    96
            elif record.levelno == 30:
                msg_color = ('\033[%s;%sm%s\033[0m' % (self._display_method, self.yellow, msg))
            elif record.levelno == 40:
                msg_color = ('\033[%s;35m%s\033[0m' % (self._display_method, msg))  # 紫红色
            elif record.levelno == 50:
                msg_color = ('\033[%s;31m%s\033[0m' % (self._display_method, msg))  # 血红色
            else:
                msg_color = msg
            # print(msg_color,'***************')
            stream.write(msg_color)
            stream.write(self.terminator)
            self.flush()
        except Exception:
            self.handleError(record)

    def emit2(self, record):
        """
        Emit a record.

        If a formatter is specified, it is used to format the record.
        The record is then written to the stream with a trailing newline.  If
        exception information is present, it is formatted using
        traceback.print_exception and appended to the stream.  If the stream
        has an 'encoding' attribute, it is used to determine how to do the
        output to the stream.
        """
        # noinspection PyBroadException
        try:
            # very_nb_print(record)
            msg = self.format(record)
            stream = self.stream
            msg1, msg2 = self.__spilt_msg(record.levelno, msg)
            if record.levelno == 10:
                # msg_color = ('\033[0;32m%s\033[0m' % msg)  # 绿色
                msg_color = f'\033[0;32m{msg1}\033[0m \033[7;32m{msg2}\033[0m'  # 绿色
            elif record.levelno == 20:
                # msg_color = ('\033[%s;%sm%s\033[0m' % (self._display_method, self.bule, msg))  # 青蓝色 36    96
                msg_color = f'\033[0;{self.bule}m{msg1}\033[0m \033[7;{self.bule}m{msg2}\033[0m'
            elif record.levelno == 30:
                # msg_color = ('\033[%s;%sm%s\033[0m' % (self._display_method, self.yellow, msg))
                msg_color = f'\033[0;{self.yellow}m{msg1}\033[0m \033[7;{self.yellow}m{msg2}\033[0m'
            elif record.levelno == 40:
                # msg_color = ('\033[%s;35m%s\033[0m' % (self._display_method, msg))  # 紫红色
                msg_color = f'\033[0;35m{msg1}\033[0m \033[7;35m{msg2}\033[0m'
            elif record.levelno == 50:
                # msg_color = ('\033[%s;31m%s\033[0m' % (self._display_method, msg))  # 血红色
                msg_color = f'\033[0;31m{msg1}\033[0m \033[7;31m{msg2}\033[0m'
            else:
                msg_color = msg
            # print(msg_color,'***************')
            stream.write(msg_color)
            stream.write(self.terminator)
            self.flush()
        except Exception as e:
            very_nb_print(e)
            very_nb_print(traceback.format_exc())
            # self.handleError(record)

    @staticmethod
    def __spilt_msg(log_level, msg: str):
        split_text = '- 级别 -'
        if log_level == 10:
            split_text = '- DEBUG -'
        elif log_level == 20:
            split_text = '- INFO -'
        elif log_level == 30:
            split_text = '- WARNING -'
        elif log_level == 40:
            split_text = '- ERROR -'
        elif log_level == 50:
            split_text = '- CRITICAL -'
        msg_split = msg.split(split_text, maxsplit=1)
        return msg_split[0] + split_text, msg_split[-1]

    def __repr__(self):
        level = logging.getLevelName(self.level)
        name = getattr(self.stream, 'name', '')
        if name:
            name += ' '
        return '<%s %s(%s)>' % (self.__class__.__name__, name, level)
