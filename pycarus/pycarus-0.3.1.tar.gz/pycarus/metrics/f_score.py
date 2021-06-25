from typing import Tuple

import numpy as np
import torch
from pykdtree.kdtree import KDTree  # type: ignore


def fscore(
    prediction: torch.Tensor, groundtruth: torch.Tensor, threshold: float = 0.001
) -> Tuple[float, float, float]:
    """Compute the F1-Score using the treshold as defined in:

    Knapitsch, A., Park, J., Zhou, Q. Y., & Koltun, V. (2017).
    Tanks and temples: Benchmarking large-scale scene reconstruction.
    ACM Transactions on Graphics (ToG), 36(4), 1-13.
    The function uses KdTree to compute the nearest neighbors

    Args:
        prediction: The predicted point cloud with shape (NUM_POINTS, 3).
        groundtruth: The groundtruth point cloud with shape (NUM_POINTS, 3).
        threshold: The euclidean distance treshold to use. Defaults to 0.001.

    Returns:
        A tuple with: the fscore, the precision and the recall.
    """
    pred = prediction.numpy()
    gt = groundtruth.numpy()

    kd_tree = KDTree(gt)
    dist_precision, _ = kd_tree.query(pred, k=1)

    kd_tree = KDTree(pred)
    dist_recall, _ = kd_tree.query(gt, k=1)

    fscore, recall, precision = 0.0, 0.0, 0.0

    if len(dist_precision) and len(dist_recall):
        precision = np.sum(dist_precision < threshold) / len(pred)
        recall = np.sum(dist_recall < threshold) / len(gt)

        if recall + precision > 0:
            fscore = 2 * recall * precision / (recall + precision)

    return fscore, precision, recall
