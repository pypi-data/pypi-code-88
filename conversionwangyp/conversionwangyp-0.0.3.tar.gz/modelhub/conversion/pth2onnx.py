import numpy as np

import onnxruntime as ort
import torch


def run_pth2onnx(model, batch_size, onnx_export_path, input_shape):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    batch_size = batch_size
    x = torch.randn(batch_size, *input_shape)
    x = x.to(device)
    model.to(device)
    model.eval()
    torch.onnx.export(model, x, onnx_export_path, verbose=True, export_params=True, opset_version=11)


def load_model_pth2onnx(pth_model_path, batch_size, onnx_export_path, input_shape, network=None):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    batch_size = batch_size
    x = torch.randn(batch_size, *input_shape)
    x = x.to(device)
    if network:
        torch_weight = torch.load(pth_model_path)  # pytorch模型加载
        model = network.to(device)
        model.load_state_dict(torch_weight)
    else:
        model = torch.load(pth_model_path).to(device)
    model.eval()
    torch.onnx.export(model, x, onnx_export_path, verbose=True, export_params=True, opset_version=11)


def do_result_evaluation(batch_size, pth_model_path, onnx_file_path, input_shape, network=None, model=None):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if model:
        model = model
    else:
        if network:
            torch_weight = torch.load(pth_model_path)  # pytorch模型加载
            model = network.to(device)
            model.load_state_dict(torch_weight)
            # model = torchvision.models.alexnet(pretrained=True).cuda()
        else:
            model = torch.load(pth_model_path).to(device)
    model.eval()
    batch_size = batch_size
    x = torch.randn(batch_size, *input_shape).to(device)
    with torch.no_grad():
        predictions = model(x)
    ort_session = ort.InferenceSession(onnx_file_path)
    onnx_outputs = ort_session.run(None, {ort_session.get_inputs()[0].name: x.cpu().numpy().astype(np.float32)})
    print("pth model - onnx model")
    print(predictions.cpu().numpy() - onnx_outputs)
