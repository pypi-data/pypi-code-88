from torch import nn


def init(module, weight_init, bias_init, gain=1):
    if gain != 0:
        weight_init(module.weight.data, gain=gain)
    else:
        weight_init(module.weight.data)
    bias_init(module.bias.data)
    return module


class AddBias(nn.Module):
    def __init__(self, bias):
        super(AddBias, self).__init__()
        self._bias = nn.Parameter(bias.unsqueeze(1))

    def forward(self, x):
        if x.dim() == 2:
            bias = self._bias.t().view(1, -1)
        else:
            bias = self._bias.t().view(1, -1, 1, 1)

        return x + bias
