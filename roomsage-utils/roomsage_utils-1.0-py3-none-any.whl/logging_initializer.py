# Load libraries ---------------------------------------------

import logging
import logging.config
import os
import time

# ------------------------------------------------------------


def get_logger(module, obj, frame):
    logging.config.fileConfig(os.environ.get('logging_ini_path'))
    logging.Formatter.converter = time.gmtime

    # Get logger
    # For __file__ use os.path.basename(module)[:-3]
    logger = logging.getLogger("{}{}{}".format(
        module,
        ".{}".format(obj.__class__.__name__) if obj is not None else "",
        ".{}".format(frame.f_code.co_name) if frame is not None else ""))

    return logger
