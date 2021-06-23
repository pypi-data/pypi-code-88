"""Plot tset."""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from logzero import logger

sns.set()


# fmt: off
def plot_tset(
        res,
        xlabel="zh",
        ylabel="en",
        thirdcol="cos",
        xmin=None,
        ymin=None,
        xmax=None,
        ymax=None,
):
    # fmt: on
    """Plot triple set.

    cmat = ren600xzh400
    correlation mat: cmat.shape
            (600, 400)

    yargmax = cmat.argmax(axis=0)
    ymax = cmat.max(axis=0)

    res = [*zip(range(cmat.shape[0]), yargmax, ymax)]

    Args:
        triple set [int, int, flot]

    Returns:
        sns.scatter plot
        fig, ax

    ax.set_xlim(xmin=, ymax=)
    ax.set_ylim(ymin=, ymax=)
    """
    shape = np.array(res).shape
    if len(shape) != 2:
        logger.error("shape length not equal to 2: %s", shape)
        raise Exception("Expect 2-d data")

    fig, ax = plt.subplots()

    if shape[1] == 2:
        # df_res = pd.DataFrame(res, columns=["lang2", "argmax"])
        # sns.relplot(x="lang2", y="argmax", data=df_res, ax=ax)
        df_res = pd.DataFrame(res, columns=[xlabel, ylabel])
        sns.scatterplot(x=xlabel, y=ylabel, data=df_res, ax=ax)

        _ = np.array(res)
        if xmin is None or ymin is None:
            xmin = _[:, 0].min()
            ymin = _[:, 1].min()
            logger.debug("xmin: %s, ymin: %s", xmin, ymin)

        if xmax is None or ymax is None:
            xmax = _[:, 0].max()
            ymax = _[:, 1].max()
            logger.debug("xmax: %s, ymax: %s", xmax, ymax)

        ax.set_xlim(xmin=xmin, xmax=xmax)
        ax.set_ylim(ymin=ymin, ymax=ymax)
        ax.grid()

        if 'get_ipython' not in globals() and 'get_ipython' not in locals():
            logger.info("\n\tKill the plot (ctrl-w or click the cross) to continue.")
            # plt.show(block=True)

        input(" Press ENTER to continue ")

        # return fig, ax
        return None

    if shape[1] == 3:
        # df_res = pd.DataFrame(res, columns=["lang2", "argmax", thirdcol])

        # sns.relplot(x="lang2", y="argmax", size=thirdcol, hue=thirdcol, sizes=(1, 110), data=df_res)

        _ = np.array(res)
        if xmin is None or ymin is None:
            xmin = _[:, 0].min()
            ymin = _[:, 1].min()
            logger.debug("xmin: %s, ymin: %s", xmin, ymin)

        if xmax is None or ymax is None:
            xmax = _[:, 0].max()
            ymax = _[:, 1].max()
            logger.debug("xmax: %s, ymax: %s", xmax, ymax)

        ax.set_xlim(xmin=xmin, xmax=xmax)
        ax.set_ylim(ymin=ymin, ymax=ymax)
        ax.grid()

        df_res = pd.DataFrame(res, columns=[xlabel, ylabel, thirdcol])
        sns.scatterplot(x=xlabel, y=ylabel, size=thirdcol, hue=thirdcol, sizes=(1, 110), data=df_res, ax=ax)

        if 'get_ipython' not in globals() and 'get_ipython' not in locals():
            logger.info("\n\tKill the plot (ctrl-w or click the cross) to continue.")
            # plt.show(block=True)

        input(" Press ENTER to continue ")

        # return fig, ax
        return None
