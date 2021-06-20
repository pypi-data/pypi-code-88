import torch
import torch.nn as nn

class ConvModule(nn.Module):

    def __init__(self, in_chs, out_chs, kernel_size, stride=1, groups=1,
            bias=True, padding=None, act_layer=nn.ReLU, act_args=None,
            norm_layer=nn.BatchNorm2d, norm_args=None):
        """
        act_layer: nn.ReLU | nn.PReLU
        act_args: None | {"inplace": True} | {"num_parameters": -1|N}
        """
        super(ConvModule, self).__init__()

        if padding is None:
            padding = (kernel_size - 1) // 2

        self.conv = nn.Conv2d(in_chs, out_chs, kernel_size=kernel_size, stride=stride,
                padding=padding, groups=groups, bias=bias)

        if norm_layer is None:
            self.norm = None
        else:
            # create a deep copy incase of inplace modification
            norm_args_ = dict()
            if norm_args is None:
                if norm_layer == nn.BatchNorm2d:
                    norm_args_["num_features"] = out_chs

            else:
                norm_args_.update(norm_args)
                if norm_args["num_features"] <= 0:
                    norm_args_["num_features"] = out_chs
            self.norm = norm_layer(**norm_args_)

        if act_layer is None:
            self.act = None
        else:
            # create a deep copy incase of inplace modification
            act_args_ = dict() 
            if act_args == None:
                if act_layer == nn.ReLU:
                    act_args_["inplace"] = True

                elif act_layer == nn.PReLU:
                    act_args_["num_parameters"] = out_chs
            else:
                act_args_.update(act_args)
                if act_layer == nn.PReLU:
                    if act_args["num_parameters"] <= 0:
                        act_args_["num_parameters"] = out_chs
            self.act = act_layer(**act_args_)

    def forward(self, x):
        x = self.conv(x)
        if self.norm:
            x = self.norm(x)
        if self.act:
            x = self.act(x)
        return x
