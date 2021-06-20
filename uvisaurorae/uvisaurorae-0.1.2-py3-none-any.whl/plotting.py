from typing import Tuple

import matplotlib
import matplotlib.colors as mcolors
import matplotlib.patheffects as mpatheffects
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("Agg")


def plot_auroral_image(
    plot_data: np.ndarray,
    hemisphere: str,
    kr_min: float = 0.5,
    kr_max: float = 30,
    r_min: float = 0,
    r_max: float = 30,
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Generate a preview plot of a projection. Color scale is logarithmic.

    :param plot_data: Projection array to plot, shape (# longitude px, # latitude px)
    :param hemisphere: Hemisphere to plot.
    :param kr_min: Minimum intensity value.
    :param kr_max: Maximum intensity value.
    :param r_min: Minimum radius (colatitude) limit.
    :param r_max: Maximum radius (colatitude) limit.
    :return: Matplotlib figure and axes.
    """
    plot_data[plot_data < kr_min] = kr_min

    lon_bins = np.linspace(0, 360, num=plot_data.shape[0] + 1)
    colat_bins = np.linspace(0, 30, num=int(30 / 180 * plot_data.shape[0]) + 1)

    if hemisphere == "North":
        tmp = np.flip(plot_data, axis=1)
    else:
        tmp = np.copy(plot_data)
    crop_img = tmp[:, : int(30 / 180 * plot_data.shape[0])]

    fig = plt.figure(figsize=(8, 7))
    ax = plt.subplot(projection="polar")

    quad = ax.pcolormesh(np.radians(lon_bins), colat_bins, crop_img.T, cmap="inferno")
    quad.set_clim(0, kr_max)
    quad.set_norm(mcolors.LogNorm(kr_min, kr_max))

    cbar = plt.colorbar(quad, ax=ax, extend="both")
    cbar.set_label(
        "Intensity (kR)", labelpad=10 if kr_max < 50 else 14, rotation=270, fontsize=14
    )
    cbar.set_ticks(
        np.append(
            np.append(np.arange(kr_min, 1, 0.1), np.arange(1, 10, 1)),
            np.arange(10, kr_max + 1, 10),
        )
    )
    cbar.ax.tick_params(labelsize=12)

    ticks = [0, 1 / 2 * np.pi, np.pi, 3 / 2 * np.pi, 2 * np.pi]
    tick_labels = ["00", "06", "12", "18"]
    for iii in range(len(tick_labels)):
        txt = ax.text(
            ticks[iii],
            r_max - 4,
            tick_labels[iii],
            color="w",
            fontsize=15,
            fontweight="bold",
            ha="center",
            va="center",
            zorder=5,
        )
        txt.set_path_effects([mpatheffects.withStroke(linewidth=4, foreground="k")])
    ax.set_xticks(ticks)
    ax.set_xticks(np.linspace(0, 2 * np.pi, 25), minor=True)
    ax.set_xticklabels([])
    ax.set_yticks([10, 20, 30])
    ax.set_yticks([5, 15, 25], minor=True)
    ax.set_yticklabels([])
    ax.grid("on", color="0.8", linewidth=1, which="major")
    ax.grid("on", color="0.8", linewidth=0.5, linestyle="--", which="minor")

    ax.set_rorigin(0)
    ax.set_rmax(r_max)
    ax.set_rmin(r_min)
    ax.set_theta_zero_location("N")
    ax.set_facecolor("0.25")

    return fig, ax
