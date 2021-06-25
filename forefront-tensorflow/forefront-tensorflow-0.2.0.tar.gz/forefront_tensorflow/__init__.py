import tf2onnx
from typing import Any, NoReturn, Optional


def convert_tensorflow_model_to_onnx(model: Any, path: Optional[str] = './model.onnx') -> NoReturn:
    tf2onnx.convert.from_keras(model, output_path=path)