"""
:requires: torch, torchvision
for torch:
cpu: pip install torch
cuda v9 and v9.1:
    pip install torch==1.1.0 torchvision==0.3.0 -f https://download.pytorch.org/whl/cu90/torch_stable.html
"""

try:
    from wizzi_utils.torch.torch_tools import *
except ModuleNotFoundError as e:
    pass

from wizzi_utils.torch import test
