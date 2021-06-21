# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Defines a criterion for loss functions"""
from torch import nn


def _get_criterion(multilabel=False, class_weights=None):
    """Get torch criterion.

    :param multilabel: flag indicating if it is a multilabel problem or not.
    :type multilabel: bool
    :param class_weights: class-level rescaling weights
    :type class_weights: torch.Tensor
    :return: torch criterion
    :rtype: object from one of torch.nn criterion classes
    """
    if multilabel:
        # https://pytorch.org/docs/stable/generated/torch.nn.BCEWithLogitsLoss.html#torch.nn.BCEWithLogitsLoss
        criterion = nn.BCEWithLogitsLoss(pos_weight=class_weights)
    else:
        criterion = nn.CrossEntropyLoss(weight=class_weights)
    return criterion
