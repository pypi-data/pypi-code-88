import numpy as np
import logging
import torch
from torch.optim.lr_scheduler import LambdaLR
import math
import mautil as mu

logger = logging.getLogger(__name__)

def tensor2device(tensor, device):
    if isinstance(tensor, list):
        return [tensor2device(t, device) for t in tensor]
    elif torch.is_tensor(tensor):
        return tensor.to(device)
    else:
        return tensor


def batch2device(batch, device):
    for k, v in batch.items():
        batch[k] = tensor2device(v, device)


def sequence_mask(lengths, maxlen=None, dtype=torch.bool):
    if maxlen is None:
        maxlen = lengths.max()
    row_vector = torch.arange(0, maxlen, 1, device=lengths.device)
    matrix = torch.unsqueeze(lengths, dim=-1)
    mask = row_vector < matrix
    mask.type(dtype)
    return mask


def get_linear_decay_schedule_with_warmup(optimizer, n_warmup_step, n_decay_step, decay_ratio=0.1, last_epoch=-1):
    """ Create a schedule with a learning rate that decreases following the
    values of the cosine function between 0 and `pi * cycles` after a warmup
    period during which it increases linearly between 0 and 1.
    """

    def lr_lambda(current_step):
        if current_step < n_warmup_step:
            ratio = float(current_step) / float(max(1, n_warmup_step))
        elif current_step<n_decay_step:
            progress = float(min(current_step, n_decay_step) - n_warmup_step) / (n_decay_step - n_warmup_step)

            ratio = 1-(1-decay_ratio)*progress
        else:
            ratio = decay_ratio
        return ratio

    return LambdaLR(optimizer, lr_lambda, last_epoch)


def mesh_reduce_losses(losses):
    reduce_losses = {}
    for k in losses[0]:
        reduce_losses[k] = np.mean([loss[k] for loss in losses])
    return reduce_losses


def mesh_reduce_preds(preds):
    new_preds = {}
    for k in preds[0]:
        if isinstance(preds[0][k], list):
            new_preds[k] = [v for pred in preds for v in pred[k]]
        else:
            new_preds[k] = np.concat([pred[k] for pred in preds], 0)
    return new_preds


def mesh_reduce_outputs(outputs):
    return {k:torch.cat([output[k] for output in outputs], 0) for k in outputs[0]}
