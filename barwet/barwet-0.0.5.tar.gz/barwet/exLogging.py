import os, logging, datetime

class Logger(object):
    def __init__(self, name, output_dir=None, use_timestamp=True):
        self.name = name
        if output_dir:
            self.output_dir = output_dir
            self.logger = Logger.get_logger(name, output_dir, use_timestamp=use_timestamp)

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
    def get_logger(name, output_dir=None, suffix='log', use_timestamp=True):
        output_dir = output_dir if output_dir else '.'
        if use_timestamp:
            timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            logfile = os.path.join(output_dir, '%s.%s.%s' % (name, timestamp, suffix))
        else:
            logfile = f'{output_dir}/{name}.{suffix}'
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler(logfile, 'w')
        formatter = logging.Formatter(fmt='%(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
