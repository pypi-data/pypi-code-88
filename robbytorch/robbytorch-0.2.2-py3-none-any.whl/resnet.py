import pathlib
from typing import Union
import os
import urllib

import torch
import torch.optim
import torchvision.models

from robustness.imagenet_models import resnet18 as robustness_resnet18
# TODO remove this dependency on robustness.
# It's basically an exact copy of torchvision.models.resnet18, except in the following.
# - The ReLU in the last BasicBlock of the last layer (before pooling) is optionally
#   disabled or replaced with a fake ReLU whose derivative is always 1.
#   It would probably be more elegant to hook torchvision.models.resnet18.
# - It exposes "latent features" (activations just before the last fc layer),
#   by changing the arguments, return values and implementation of `forward`.
#   It would be more elegant to just use: ```
#       latent_dim = resnet.fc.in_features
#       resnet.fc = torch.nn.Identity()
#       model = nn.Sequential(OrderedDict(
#           backbone=resnet,
#           head=torch.nn.Linear(latent_dim, len(CLASSES))
#       )).cuda()
#   ```
#   And then when you actually need both latents and logits, use: ```
#       latents = model.backbone(x)
#       logits = model.head(latents)
#   ```
#   Or `latents = model[:-1](x)` in general.

PathLike = Union[str, os.PathLike]


def get_resnet_from_robustness(
    pretrained=True,
    robust=False,
    device: Union[torch.device, str] = "cuda",
    path: PathLike = "ipython/pretrained-models/"
) -> torch.nn.Module:
    """Get pre-trained resnet18 from robustness library."""
    import dill

    if robust and not pretrained:
        raise ValueError("Cannot get robust and not pretrained model.")

    path = pathlib.Path(path)
    if not robust:
        path = path / "resnet-18-l2-eps0.ckpt"
    else:
        path = path / "resnet-18-l2-eps3.ckpt"
    model = robustness_resnet18()
    if pretrained:
        checkpoint = torch.load(path, pickle_module=dill, map_location=device)
        state_dict = checkpoint["model"]
        prefix = "module.attacker.model."
        state_dict = {k[len(prefix):]: v for k, v in state_dict.items() if k.startswith(prefix)}
        model.load_state_dict(state_dict)
    return model.to(device=device)
