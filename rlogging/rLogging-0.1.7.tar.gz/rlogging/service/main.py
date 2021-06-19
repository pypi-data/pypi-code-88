
import logging
import pathlib as pa
import sys
import typing as _T

from rlogging import handlers, printers
from rlogging.records import Record

logFile = pa.Path(__file__).parent.parent / 'logs/daemon-core.log'
print(logFile)

if not logFile.parent.is_dir():
    logFile.parent.mkdir(parents=True)

logFormatStr = '[%(asctime)s %(process)s %(levelname)s] %(message)s'
logging.basicConfig(filename=logFile, level=logging.DEBUG, format=logFormatStr)
pylogger = logging.getLogger(__name__)
