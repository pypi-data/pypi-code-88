from . import torch

__all__ = ['set_device']


def set_device(tensor, device):

    # if isinstance(tensor, torch.Tensor):
    if isinstance(tensor, (torch.nn.Module, torch.Tensor)):
        if device is None:
            return tensor
        elif isinstance(device, (str, torch.device)):
            tensor = tensor.to(device)
            return tensor
        else:
            raise TypeError('device')
    else:
        raise TypeError('tensor')
