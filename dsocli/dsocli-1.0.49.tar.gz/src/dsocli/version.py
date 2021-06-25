import os
import pathlib
__version__ = '1.0'

if __name__ == '__main__':
    path = os.path.join(pathlib.Path(__file__).parent.resolve(), 'src', 'dsocli', '.release')
else:
    path = os.path.join(pathlib.Path(__file__).parent.resolve(), '.release')
with open(path, 'r') as f:
    __release__ = f.read().strip()
