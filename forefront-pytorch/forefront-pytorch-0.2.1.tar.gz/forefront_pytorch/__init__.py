import torch
from typing import Any, NoReturn, Optional


def convert_pytorch_model_to_onnx(model: Any, sample_input_data: Any, path: Optional[str] = './model.onnx') -> NoReturn:
    torch.onnx.export(model, sample_input_data, path, output_names=['output'], input_names=['input'])