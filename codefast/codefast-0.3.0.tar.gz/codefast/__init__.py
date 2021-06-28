import builtins
import sys

import codefast.reader
import codefast.utils as utils
from codefast.logger import Logger

builtins._str = utils._str
builtins.io = utils.FileIO
builtins.say = io.say
builtins.reader = codefast.reader
builtins.jsn = utils.JsonIO

# Export methods and variables
json = utils.JsonIO
text = utils.FileIO
file = utils.FileIO
csv = utils.CSVIO
net = utils.Network
os = utils._os()

format = utils.FormatPrint
logger = Logger()
info = logger.info
error = logger.error
warning = logger.warning
say = io.say

shell = utils.shell

sys.modules[__name__] = utils.wrap_mod(sys.modules[__name__],
                                       deprecated=['text'])
