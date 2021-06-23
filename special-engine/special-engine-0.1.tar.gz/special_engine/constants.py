import os.path
import sys

__all__ = []
_module = sys.modules[__name__]

def _add_constants(enum, prefix):
    for name, value in enum.__members__.items():
        setattr(_module, prefix + name, value)
        __all__.append(prefix + name)

if __name__ == '__main__':
    __name__ = 'hyperscan.constants'
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    print('from . import capi')
    def _add_constants(enum, prefix):
        for name, value in enum.__members__.items():
            print(f"{prefix}{name}: capi.{enum.__name__} = ...")

from . import capi

_constants = {
    capi.HsError: 'HS_',
    capi.HsExtFlag: 'HS_EXT_FLAG_',
    capi.HsFlag: 'HS_FLAG_',
    capi.HsMode: 'HS_MODE_',
    capi.HsCpuFeatures: 'HS_CPU_FEATURE_',
    capi.HsTune: 'HS_TUNE_',
}

for enum, prefix in _constants.items():
    for name, value in enum.__members__.items():
        setattr(_module, prefix + name, value)
        __all__.append(prefix + name)
