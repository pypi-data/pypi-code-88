from typing import Collection, Optional

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scanpy as sc


def expr_colormap():
    """\
    Gray-to-blue colormap for expression data
    """
    cdict = {
        'red':   [
            (0.0, 220/256, 220/256),
            (0.5, 42/256, 42/256),
            (1.0, 6/256, 6/256)
        ],

        'green': [
            (0.0, 220/256, 220/256),
            (0.5, 145/256, 145/256),
            (1.0, 37/256, 27/256)
        ],

        'blue':  [
            (0.0, 220/256, 220/256),
            (0.5, 174/256, 174/256),
            (1.0, 170/256, 170/256)
        ]
    }
    return mpl.colors.LinearSegmentedColormap('exprCmap', segmentdata=cdict, N=256)


def feature_plot(
    adata: sc.AnnData,
    feature: str,
    gridsize: tuple = (180, 70),
    linewidths: float = 0.15,
    figsize: Optional[float] = None
) -> mpl.figure.Figure:
    """\
    Plot expression of gene or feature in hexbin

    Plots numeric feature value, commonly gene expression, on UMAP
    coordinates using hexbin. Feature is taken from ``adata.obs`` if it is
    found there, otherwise from ``adata.raw``.

    Parameters
    ----------
    adata
        Annotated data matrix
    feature
        Name of the feature to plot
    gridsize
        Tuple of hexbin dimentions, larger numbers produce smaller hexbins
    linewidths
        Width of the lines to draw around each hexbin
    figsize
        Optional, make figure of this size

    Returns
    -------
    Matplotlib figure with colorbar added.
    """
    if feature in adata.obs.columns:
        values = adata.obs_vector(feature)
    else:
        values = adata.raw.obs_vector(feature)

    kwargs = {}
    if figsize is not None:
        kwargs["figsize"] = figsize
    fig, ax = plt.subplots(**kwargs)
    hb = ax.hexbin(
        adata.obsm["X_umap"][:, 0],
        adata.obsm["X_umap"][:, 1],
        C=values,
        cmap=expr_colormap(),
        gridsize=gridsize,
        linewidths=linewidths
    )
    cax = fig.add_axes((0.92, 0.8, 0.02, 0.15))
    fig.colorbar(hb, cax=cax, fraction=0.05, pad=0.02, aspect=40)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"{feature}")
    ax.set_xlabel("UMAP1")
    ax.set_ylabel("UMAP2")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    return fig


def plot_composition(
    adata: sc.AnnData,
    group_by: str,
    color: str,
    relative: bool = False,
    palette: Optional[Collection] = None,
    plot_numbers: bool = False
) -> mpl.axes.Axes:
    """\
    Plot composition of clusters or other metadata

    Groups cells by one metadata field and plots stacked barplot
    colored by another metadata field. Common use case is to see which
    samples contribute to which clusters. Plots horizontally.

    Parameters
    ----------
    adata
        Annotated data matrix
    group_by
        Name of the field to group by on y axis
    color
        Name of the field to color by
    relative
        Plot percentage for each cluster if ``True`` or absolute counts if ``False``
    palette
        Optional, pass your own palette
    plot_numbers
        If ``True``, plot number of cells next to the bars

    Returns
    -------
    Matplotlib axes with the plot.
    """
    left = np.zeros(len(adata.obs[group_by].unique()))
    total = None
    if relative:
        total = adata.obs[group_by].value_counts().sort_index(ascending=False)
    fig, ax = plt.subplots()
    num_colors = adata.obs[color].unique().size
    # TODO: adjust
    if palette is not None:
        colors = palette
    elif num_colors <= 10:
        colors = mpl.cm.tab10
    elif num_colors <= 20:
        colors = mpl.cm.tab20
    elif num_colors <= 28:
        colors = sc.pl.palettes.default_28
    else:
        colors = sc.pl.palettes.default_102
    for i, s in enumerate(adata.obs[color].cat.categories):
        cnt = adata.obs[group_by][adata.obs[color] == s].value_counts().sort_index(ascending=False)
        if relative:
            cnt = cnt / total * 100
        c = isinstance(colors, list) and colors[i] or colors(i)
        ax.barh(cnt.index, cnt, left=left, label=s, color=c)
        left += cnt
    if plot_numbers:
        for i, count in enumerate(total):
            ax.text(left[i] + 2, i, str(count), va="center")
    ax.legend(title=color.capitalize())
    ax.set_title(f"{group_by.capitalize()} by {color}")
    return ax
