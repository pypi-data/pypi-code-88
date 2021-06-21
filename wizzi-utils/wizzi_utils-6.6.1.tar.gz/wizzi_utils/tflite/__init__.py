"""
:requires: tflite_runtime
tf_lite install: https://www.tensorflow.org/lite/guide/python#install_tensorflow_lite_for_python
    winOs: pip install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime
"""
try:
    from wizzi_utils.tflite.tflite_tools import *
except ModuleNotFoundError as e:
    pass

from wizzi_utils.tflite import test
