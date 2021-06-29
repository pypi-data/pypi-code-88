# Load libraries ---------------------------------------------

from roomsage_utils.logging_initializer import get_logger
import inspect

# ------------------------------------------------------------


class B(object):

    def a(self):
        log = get_logger(__name__, self, inspect.currentframe())
    
        log.error("Error")
     
    def b(self):
        log = get_logger(__name__, self, inspect.currentframe())
        log.info("Info 1")
        self.a()
        log.info("Info 2")
