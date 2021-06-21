import numpy as np
import logging


def emr(predicted, target, **kwargs):
    logging.debug("Evaluating Exact-Match-Ratio(EMR)")
    return np.all(target == predicted, axis=1).mean()


def hamming(predicted, target, **kwargs):
    logging.debug("Evaluating Hamming loss")
    tmp = 0
    for i in range(target.shape[0]):
        tmp += np.size(target[i] == predicted[i]) - np.count_nonzero(target[i] == predicted[i])
    return tmp / (target.shape[0] * target.shape[1])
