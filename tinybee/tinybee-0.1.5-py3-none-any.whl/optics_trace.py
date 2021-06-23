r"""optics_trace.py in tinybee-aligner/tinybee, pypi\tinybee-aligner\wuch3_pad.py."""
from typing import Any, List, Tuple, Union

import webbrowser
# import os
# import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import OPTICS

from logzero import logger

# pylint: disable=invalid-name
colors = "bgrcmykw"
colors = "bgrcmyk"
colors = "bgrcmy"  # k (black) for outliers
colors = "bgr"  # k (black) for outliers
colors = "b"  # k (black) for outliers
colors = "gbk"  # r for outliers
markers = ".,ov^<>1234sp*hH+xDd|_"
markers = ".,v^<>1234sp*hH+xDd|_"  # exclude o (will be used for outliers)
markers = ".v^<>1234sp*hH+xDd|_"  # exclude , (pixel, too small)
style = ["-", "--", "-.", ":"]

c_m = [c + m for m in markers for c in colors]
c_m_s = [c + m + s for s in [""] + style for m in markers for c in colors]
# In [953]: c_m[:10]  # len(c_m) 132
# Out[953]: ['b.', 'g.', 'r.', 'c.', 'm.', 'y.', 'b,', 'g,', 'r,', 'c,']


# fmt: off
def optics_trace(
        tset: List,
        min_samples: Union[float, int] = 5,
        xi: float = 0.05,
        label="",
        plot=False,
        xmin: float = 0,
        xmax: float = None,
        ymin: float = 0,
        ymax: float = None,
) -> Tuple[Any, int, int]:
    # fmt: on
    """Find and plot optics trace for a given list of triple or tuple.

    Args:
        tset:
        min_samples: refer to sklearn.cluster.OPTICS
        xi: refer to sklearn.cluster.OPTICS

    Returns:
        OPTICS

    paras_zh = Path("data/wu_ch3_zh.txt").read_text("utf8").splitlines()
    paras_en = Path("data/wu_ch3_en.txt").read_text("utf8").splitlines()
    paras_w4w = [bingmdx_tr(elm) for elm in paras_en]
    lmat_w4w = light_scores(paras_w4w, paras_zh)
    ltset_w4w = cmat2tset(lmat_w4w)

    _ = optics_trace(ltset_w4w)
    _ = optics_trace(ltset_w4w[:,:2])  # this looks good

    the bigger min_samples, the more outlier
    the smaller xi, the fewer outlier

    tset[opt_w4w.lablels_ > -1]: projectd trace
        can be used in gen_iset: iset
        iset with test: aset

    """
    ltset_w4w = tset

    opt_w4w = OPTICS(min_samples=min_samples, xi=xi).fit(ltset_w4w)
    n_clusters = set(elm for elm in opt_w4w.labels_ if elm > -1).__len__()
    # n_picked = sum([1 for elm in opt_w4w.labels_ if elm > -1])
    n_outliers = sum([1 for elm in opt_w4w.labels_ if elm == -1])

    if plot:
        figw4w = plt.figure(figsize=(10, 7))
        axw4w = figw4w.subplots()


        # Xk = ltset_w4w[opt_w4w.labels_ > -1]
        # axw4w.plot(Xk[:, 0], Xk[:, 1], "g.", alpha=0.8)
        for klass, color_mark in zip(range(n_clusters), c_m):
            Xk = ltset_w4w[opt_w4w.labels_ == klass]
            # axw4w.plot(Xk[:, 0], Xk[:, 1], color_mark, alpha=0.8)
            axw4w.plot(Xk[:, 0], Xk[:, 1], color_mark, alpha=1.0)
            logger.debug("klass: %s, collor: %s, %s", klass, color_mark, Xk)

        # outliers
        # axw4w.plot(ltset_w4w[opt_w4w.labels_ == -1, 0], ltset_w4w[opt_w4w.labels_ == -1, 1], 'ko', alpha=1)
        axw4w.plot(ltset_w4w[opt_w4w.labels_ == -1, 0], ltset_w4w[opt_w4w.labels_ == -1, 1], "ro", alpha=1)  # type: ignore
        axw4w.set_xlim(xmin=xmin, xmax=xmax)
        axw4w.set_ylim(ymin=ymin, ymax=ymax)
        axw4w.set_title(
            f"{label + '-- ' if label else ''}min_samples: {min_samples}, xi: {xi}, no. of outliers: {n_outliers}"
        )

        # to show plot in non-ipython session
        if "get_ipython" in locals():
            plt.ion()
            plt.show()
        else:
            # plt.show(block=True)
            plt.savefig("tmp111.png")
            plt.close()
            try:
                # os.startfile("tmp111.png")
                webbrowser.open("tmp111.png")
                logger.info("Opened tmp111.png in default app")
            except Exception as e:
                logger.error(e)
    # return ltset_w4w[opt_w4w.labels_ > -1], n_picked, n_outliers
    return opt_w4w.labels_