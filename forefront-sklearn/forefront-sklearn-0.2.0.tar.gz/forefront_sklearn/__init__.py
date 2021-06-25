import sklearn
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
from typing import Any, NoReturn, Optional, Tuple, Union, List


def convert_sklearn_model_to_onnx(model: Any, input_shape: List[Union[int, None]] = None,
                                  path: Optional[str] = './model.onnx') -> NoReturn:

    initial_type = [('float_input', FloatTensorType(input_shape))]
    onx = convert_sklearn(model, initial_types=initial_type)
    with open(path, 'wb') as f:
        f.write(onx.SerializeToString())
