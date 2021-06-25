import os
import pathlib
with open(os.path.join(pathlib.Path(__file__).parent.resolve(), 'src', 'dsocli', '.release')) as f:
    __release__ = f.read()
__version__ = '1.0'
