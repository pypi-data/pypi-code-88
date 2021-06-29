import os
import sys

from loguru import logger


class base_logger:
    __instance = None

    def __init__(self, log_name: str = 'default', file_path: str = './', mode: str = 'DEBUG',
                 cmd_output: bool = False, backup_count: int = 3):
        import socket
        self.logger = logger
        logger.remove()
        if cmd_output:
            handler_id = self.logger.add(sys.stderr, level=mode)
        else:
            handler_id = self.logger.add(sys.stderr, level="ERROR")

        host_name = socket.gethostname()
        try:
            ip = socket.gethostbyname(host_name)
        except Exception as e:
            ip = "未知获取ip错误"
        log_file = os.path.join(file_path, log_name)
        formatter = """<green>{time:YYYY-MM-DD HH:mm:ss}</green> @zkr@ {file} @zkr@ {name} @zkr@ {level} @zkr@ {module} @zkr@ {function} @zkr@ {line} @zkr@ process-id: {process} @zkr@ """ + ip + """ @zkr@ """ + host_name + """ @zkr@ {message}"""
        self.logger.add("{}.log".format(log_file), format=formatter, level=mode,
                        enqueue=True, retention="5 days", encoding="utf-8",
                        rotation="50MB")

    def __new__(cls, log_name: str = 'default', file_path: str = './', mode: str = 'DEBUG',
                cmd_output: bool = False, backup_count: int = 3, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(base_logger, cls).__new__(cls)
        return cls.__instance

    def info(self, msg):
        return self.logger.info(msg)

    def debug(self, msg):
        return self.logger.debug(msg)

    def warning(self, msg):
        return self.logger.warning(msg)

    def error(self, msg):
        return self.logger.error(msg)
