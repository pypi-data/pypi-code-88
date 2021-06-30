import inspect
import os
import sys

__version__ = "0.1.1"
__all__ = ['kakaopy']

real_path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")
sys.path.append(real_path)