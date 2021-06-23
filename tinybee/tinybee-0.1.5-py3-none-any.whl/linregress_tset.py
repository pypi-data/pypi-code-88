"""Find linregress of tset."""
from typing import List, Tuple, Union
import numpy as np
from scipy.stats import linregress

TwoTupleList = List[Tuple[float, float]]
ThreeTupleList = List[Tuple[float, float, float]]


def linregress_tset(tset: Union[TwoTupleList, ThreeTupleList, List[float]]) -> Tuple[float, float, float]:
    """Calculate slope, rvalue, stderr for linregress tset.

    Args
        tset: triple set
    the three-tuple (slope, rvalue, stderr) linregress of tset (list of 2-tuples or 3-tuples.
    """
    arr = np.array(tset)
    assert arr.shape[1] > 1, f"Minimum two columns, current: {arr.shape} "

    lr_ = linregress(arr[:, 0], arr[:, 1])
    linregress_tset.lr = lr_

    return float(lr_.slope), float(lr_.rvalue), float(lr_.stderr)
