import os
from importlib.util import find_spec
from typing import Tuple

import torch

from pycarus.geometry.pcd import batchify, unbatchify


def emd(
    prediction: torch.Tensor, groundtruth: torch.Tensor, eps: float, iterations: int
) -> Tuple[torch.Tensor, torch.Tensor]:
    """Compute the Earth Mover's Distance

    This function uses the auction algorithm for approximation, hence the assignment is not
    guranteed to be a bijection.

    Args:
        prediction: The predicted point cloud with shape ([B,] NUM_POINTS, 3). NUM_POINTS should be
        a multiple of 1024.
        groundtruth: The groundtruth point cloud with shape ([B,] NUM_POINTS, 3). NUM_POINTS should
        be a multiple of 1024.
        eps: the balance between the error rate and the speed of convergence.
        iterations: the max number of iterations.
    """
    if find_spec("emd") is None:
        folder = os.path.dirname(os.path.realpath(__file__))
        str_exp = f"EMD not found. Install it running {folder}/external/setup_emd.py"
        raise ModuleNotFoundError(str_exp)
    else:
        from pycarus.metrics.external.emd_module import EMDDistance  # type: ignore

    batched, [pred, gt] = batchify([prediction, groundtruth], 3)
    emd = EMDDistance()

    distance, assignment = emd(pred, gt, eps, iterations)

    if batched:
        [distance, assignment] = unbatchify([distance, assignment])

    return distance, assignment
