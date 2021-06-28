import slai
import torch


class ModelHandler(slai.BaseModelHandler):
    def model_inputs(self):
        return {"input_1": slai.inputs.Float(), "input_2": slai.inputs.Float()}

    def input(self, **inputs):
        x = torch.tensor([inputs["input_1"], inputs["input_2"]])
        return x

    def output(self, model_output):
        processed_output = model_output.detach().numpy().tolist()
        return processed_output
