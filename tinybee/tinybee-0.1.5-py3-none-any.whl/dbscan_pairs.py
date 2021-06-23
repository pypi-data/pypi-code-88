"""Gen pairs based on dbscan clustering.

Modified from lowess_pairs.
"""
# pylint: disable=broad-except, too-many-locals, duplicate-code

from typing import List, Optional, Tuple, Union

import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

from logzero import logger


# fmt: off
# def lowess_pairs(
def dbscan_pairs(
        arr1: Union[List[float], np.ndarray],
        eps: float = None, min_samples: float = None,
        plot: bool = False,
) -> List[Tuple[int, int, float]]:
    # fmt: on
    """Gen pairs via dbscan clustering.

    Args:
        arr1: correlation matrix
        src_len, tgt_len = arr1.shape
        eps:    .5% * src_len
        min_samples: float,  .5 * tgt_len
        plot: to plot or not
        https://colab.research.google.com/drive/17dBcLZ9gZyJV51GP0Q1PEVRyXJb--RnY#scrollTo=NZDxVnLxercQ&uniqifier=9
    def dbscan(X, eps, min_samples):
        '''https://medium.com/@plog397/functions-to-plot-kmeans-hierarchical-and-dbscan-clustering-c4146ed69744'''
        # ss = StandardScaler()
        # X = ss.fit_transform(X)
        db = DBSCAN(eps=eps, min_samples=min_samples)  # .5%？ 50， 5 for 10000 1000
        db.fit(X)
        y_pred = db.fit_predict(X)
        plt.scatter(X[:,0], X[:,1], c=y_pred, cmap='Paired')
        # display(y_pred)
        plt.title("DBSCAN")

        import joblib
        from tinybee.cos_matrix2 import cos_matrix2

        cmat = joblib.load("data/cmat.lzma")
        arr = cmat.copy()

        hlm_ch1_en_emb = joblib.load("data/hlm_ch1_en_emb.lzma")
        hlm_ch1_zh_emb = joblib.load("data/hlm_ch1_zh_emb.lzma")
        cmat_hlmch1 = cos_matrix2(hlm_ch1_en_emb, hlm_ch1_zh_emb)
        arr = cmat_hlmch1.copy()

        tset = dbscan_pairs(cmat_hlmch1)

        fig = plt.figure(figsize=(8, 6))
        ax1 = fig.add_subplot(111)

        df = pd.DataFrame(tset, columns=['y', 'yargmax', 'ymax'])
        sns.scatterplot(data=df, x="y", y="yargmax", size="ymax", sizes=(1, 110))  # legend='auto'

        corr1000x1100 = joblib.load("data/corr1000x1100.lzma")
        tset1000x1100 = dbscan_pairs(corr1000x1100, plot=1)
        df1000x1100 = pd.DataFrame(tset1000x1100, columns=['y', 'yargmax', 'ymax'])
        fig = plt.figure(figsize=(8, 6))
        ax1 = fig.add_subplot(111)
        sns.scatterplot(data=df1000x1100, x="y", y="yargmax", size="ymax", sizes=(1, 50))

        ---
        import matplotlib a mpl
        mpl.rcParams['lines.markersize'] = 6
        size: mpl.rcParams['lines.markersize']**2
    """
    if isinstance(arr1, list):
        try:
            arr = np.array(arr1)
        except Exception as exc:
            logger.debug(exc)
            raise SystemExit(1) from exc
    else:
        arr = arr1.copy()

    src_len, tgt_len = arr.shape  # _ = src_len (leny)

    if eps is None:
        eps = src_len * .01
        if eps < 3:
            eps = 3
    if min_samples is None:
        min_samples = tgt_len / 100 * 0.5
        if min_samples < 3:
            min_samples = 3

    logger.debug("eps: %s", eps)
    logger.debug("min_samples: %s", min_samples)

    x = np.arange(tgt_len)  # pylint: disable=invalid-name
    yargmax = np.array(arr).argmax(axis=0)
    ymax = np.array(arr).max(axis=0)

    assert tgt_len == yargmax.shape[0]

    _ = zip(x, yargmax, ymax)  # type: ignore
    tset = np.array([*_])

    db = DBSCAN(eps=eps, min_samples=min_samples)
    db.fit(tset)
    y_pred = db.fit_predict(tset)

    dbscan_pairs.y_pred = y_pred
    # logger.debug(" y_pred: %s", y_pred)

    xcl = []
    ycl = []
    val = []
    for idx, elm in enumerate(y_pred):
        if elm > -1:  # not noise
            xcl.append(idx)
            ycl.append(tset[idx, 1])
            val.append(tset[idx, 2])
    if plot:
        # plt.scatter(tset[:,0], tset[:,1], c=y_pred, cmap='Paired')
        fig = plt.figure(figsize=(8, 6))
        ax1 = fig.add_subplot(111)
        plt.scatter(tset[:,0], tset[:,1], cmap='Paired')  # , s=4
        plt.scatter(xcl, ycl, s=10)

    res = []
    for idx, idy, val in zip(xcl, ycl, val):
        res.append((idx, idy, val,))

    return res

    # return y_pred
    # return [(0, 0, 0.0,)]
    # return y_pred
