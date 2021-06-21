import logging

from tqdm import tqdm

class TqdmHandler(logging.StreamHandler):

    def emit(self, record):
        try:
            tqdm.write(self.format(record), end=self.terminator)
        except RecursionError:
            raise
        except Exception:
            self.handleError(record)
