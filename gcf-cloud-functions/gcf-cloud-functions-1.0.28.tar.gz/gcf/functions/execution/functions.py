import time
import logging
import traceback

from gcf.functions.execution.exceptions import RetryException
from gcf.functions.execution.time import Timer
from gcf.functions.execution.config import ExecutionStatus
from gcf.functions.execution.events.handler import EventHandler
from gcf.functions.execution.worker import AbstractWorker


class Function(object):
    def __init__(self, db, event_path, worker_class: AbstractWorker.__class__):

        self.db = db
        self.event_path = event_path
        self.worker_class = worker_class
        self.worker = None

        self.event_ref = db.document(event_path)

        self.logger = self._init_logger()

    def _init_logger(self):
        logger = logging.getLogger(f"[{self.event_ref.id}] [{self.__class__.__name__}]")
        logger.setLevel(logging.DEBUG)

        stdout = logging.StreamHandler()
        logger.addHandler(stdout)

        stdout.setFormatter(logging.Formatter('%(asctime)s %(name)s %(message)s'))
        return logger

    def try_run(self, timeout_seconds):
        start = time.time()

        # Handle Event
        # Can raise ExecutionNotAllowedException or RetryException
        event_handler = EventHandler(event_ref=self.event_ref)
        event = event_handler.handle()

        # Init the timer
        timer = Timer(event_id=self.event_ref.id)

        # Create the worker
        self.worker = self.worker_class(timer=timer, event=event)

        self.worker.start()

        # Wait TIMEOUT_MILLIS seconds and timeout 30 seconds early
        self.worker.join(timeout_seconds - 30)

        # Timeout here - from now on we have 30 seconds to finish threads
        timer.timeout()

        if self.worker.is_alive():
            self.logger.debug('# SIGTIMEOUT Sent')

        # Wait for thread to finish
        self.worker.join()

        self.logger.debug(f"# Function exited with <{self.worker.status}>")

        end = time.time()
        duration = end - start
        self.logger.debug(f'# Durations in seconds: {int(duration)}, (start={start}, end={end})')

        # Raise exceptions here so GCP will retry our function
        if self.worker.status in [ExecutionStatus.WAITING_RETRY, ExecutionStatus.WAITING_SLEEP]:
            raise RetryException

    def run(self, timeout_seconds):
        self.logger.debug("# START")

        try:
            self.try_run(timeout_seconds)
        except RetryException:
            # Exit with exception so GCP will retry the function
            raise
        except Exception:
            # Exit normally, no retry here
            traceback.print_exc()
        finally:
            self.logger.debug("# END")
