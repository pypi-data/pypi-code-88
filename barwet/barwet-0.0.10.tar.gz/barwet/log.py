import logging
from logging import StreamHandler
from logging import FileHandler
from logging import Formatter
from datetime import datetime


def get_logger(name, to_console=True, to_file=True, **kwargs):
    """
    `level`: str, default: `logging.INFO`
        
    If `to_console` is `True`:
        - `console_fmt`: str, default: `'%(asctime)s %(name)s.%(levelname)s # %(message)s'`
        - `console_datefmt`: str, default: `'%Y-%m-%d %H:%M:%S'`

    If `to_file` is `True`:
        - `output_dir`: str, default: `'./'`
        - `timestamp`: str, deafult: `'%Y%m%d%H%M%S'`, for log file name
        - `file_fmt`: str, default: `console_fmt` or `'%(asctime)s %(name)s.%(levelname)s # %(message)s'`
        - `file_datefmt`: str, default: `console_datefmt` or `'%Y-%m-%d %H:%M:%S'`
    """

    _level = kwargs.get('level', logging.INFO)  # 日志级别

    logger = logging.getLogger(name)
    logger.setLevel(_level)

    if to_console:
        stream_handler = StreamHandler()
        _console_fmt = kwargs.get(
            'console_fmt', '%(asctime)s %(name)s.%(levelname)s # %(message)s')
        _console_datefmt = kwargs.get('console_datefmt', r'%Y-%m-%d %H:%M:%S')
        formatter = Formatter(fmt=_console_fmt, datefmt=_console_datefmt)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    if to_file:
        _output_dir = kwargs.get('output_dir', './')
        _timestamp = kwargs.get('timestamp', r'%Y%m%d%H%M%S')
        if _timestamp is None:
            logfile = f'{_output_dir}/{name}.log'
        else:
            time_str = datetime.now().strftime(_timestamp)
            logfile = f'{_output_dir}/{name}.{time_str}.log'
        file_handler = FileHandler(logfile, 'w')
        _file_fmt = kwargs.get('file_fmt')
        if _file_fmt is None:
            _file_fmt = kwargs.get('console_fmt')
        if _file_fmt is None:
            _file_fmt = r'%Y-%m-%d %H:%M:%S'
        _file_datefmt = kwargs.get('file_datefmt')
        if _file_datefmt is None:
            _file_datefmt = kwargs.get('console_datefmt')
        if _file_datefmt is None:
            _file_datefmt = '%(asctime)s %(name)s.%(levelname)s # %(message)s'
        formatter = Formatter(fmt=_file_fmt, datefmt=_file_datefmt)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
