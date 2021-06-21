try:
    from .qiwi import Qiwi
except ImportError:
    pass
try:
    from .yoomoney import YooMoney
except ImportError:
    pass

from .coinbase.bitcoin import Bitcoin
