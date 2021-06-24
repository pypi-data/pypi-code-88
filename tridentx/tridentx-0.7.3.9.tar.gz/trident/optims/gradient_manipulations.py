from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import copy

from trident import context

from trident.backend.common import *

_backend =get_backend()
working_directory=context._context().working_directory

if _backend == 'pytorch':
    import torch
    import torch.nn as nn
    from trident.backend.pytorch_backend import *
    from trident.backend.pytorch_ops import *

elif _backend == 'tensorflow':
    import tensorflow as tf
    from trident.backend.tensorflow_backend import *
    from trident.backend.tensorflow_ops import *



def adaptive_clip_grad(p,grad, clip_factor=0.01, eps=1e-3, norm_type=2.0):
    """ Adaptive Gradient Clipping
    Thanks for these great works.
    An impl of AGC, as per (https://arxiv.org/abs/2102.06171):
    @article{brock2021high,
      author={Andrew Brock and Soham De and Samuel L. Smith and Karen Simonyan},
      title={High-Performance Large-Scale Image Recognition Without Normalization},
      journal={arXiv preprint arXiv:},
      year={2021}
    }
    Code references:
      * Official JAX impl (paper authors): https://github.com/deepmind/deepmind-research/tree/master/nfnets
      * Phil Wang's PyTorch gist: https://gist.github.com/lucidrains/0d6560077edac419ab5d3aa29e674d5c
    Hacked together by / Copyright 2021 Ross Wightman

    """
    def unitwise_norm(x, norm_type=2.0):
        if x.ndim <= 1:
            return x.norm(norm_type)
        else:
            # works for nn.ConvNd and nn,Linear where output dim is first in the kernel/weight tensor
            # might need special cases for other weights (possibly MHA) where this may not be true
            return x.norm(norm_type, dim=tuple(range(1, x.ndim)), keepdim=True)

    p_data = p.detach()
    g_data = p.grad.detach()
    max_norm = unitwise_norm(p_data, norm_type=norm_type).clamp_(min=eps).mul_(clip_factor)
    grad_norm = unitwise_norm(g_data, norm_type=norm_type)
    clipped_grad = g_data * (max_norm / grad_norm.clamp(min=1e-6))
    new_grads = where(grad_norm < max_norm, g_data, clipped_grad)
    if get_backend()=='pytorch':
        p.grad.data.copy_(new_grads)

    elif get_backend()=='tensorflow':
        grad=new_grads
    return p, new_grads


def clip_grad_by_norm(paras, norm_value):
    return torch.nn.utils.clip_grad_norm_(paras, norm_value)

#def clip_grad_by_value()