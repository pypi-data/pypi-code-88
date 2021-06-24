import os, logging, datetime


class Logger(object):
    def __init__(self, name, output_dir=None, use_timestamp=True):
        self.name = name
        if output_dir:
            self.output_dir = output_dir
            self.logger = Logger.get_logger(name,
                                            output_dir,
                                            use_timestamp=use_timestamp)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

    def write(self, string):
        self.logger.info(string)
        return string

    def set_dir(self, output_dir):
        self.output_dir = output_dir
        self.logger = Logger.get_logger(self.name, output_dir)

    @staticmethod
    def get_logger(name, output_dir=None, **kwargs):
        """
        不指定`output_dir`时日志输出到标准输出。
        args:
            `name: str`
            `output_dir: str | None`, if None, not output to file
        kwargs:
            If `output_dir` is not None:
                `file_suffix: str`, suffix of log file
                `use_timestamp: bool`, if add a timestamp to log filename
                `timestamp_fmt: str`, added timestamp format
        """

        logfile = None
        if output_dir is not None:
            file_suffix = kwargs.get('file_suffix', 'log')
            use_timestamp = kwargs.get('use_timestamp', True)
            if use_timestamp:
                timestamp_fmt = kwargs.get('timestamp_fmt', r'%Y%m%d%H%M%S')
                timestamp = datetime.datetime.now().strftime(timestamp_fmt)
                logfile = os.path.join(
                    output_dir, '%s.%s.%s' % (name, timestamp, file_suffix))
            else:
                logfile = f'{output_dir}/{name}.{file_suffix}'

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        if logfile is not None:
            file_handler = logging.FileHandler(logfile, 'w')
            formatter = logging.Formatter(fmt='%(message)s')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        return logger
