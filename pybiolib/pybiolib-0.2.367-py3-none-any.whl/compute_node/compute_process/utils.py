from queue import Queue

from biolib.biolib_binary_format import SystemException
from biolib.biolib_logging import logger


class ComputeProcessException(Exception):
    def __init__(self, original_error: Exception, biolib_error_code, messages_to_send_queue: Queue):
        super().__init__()

        system_exception_package = SystemException().serialize(biolib_error_code)
        messages_to_send_queue.put(system_exception_package)

        logger.error(original_error)
