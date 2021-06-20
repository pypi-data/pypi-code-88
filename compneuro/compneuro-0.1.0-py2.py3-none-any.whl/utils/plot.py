"""
Plotting functions.

Largely taken from Neural_

Provides the following methods:

- :func:`plot_spikes`: Plot 2D array of binary spike mask
- :func:`plot_mat`: Plot matrix data using :py:func:`matplotlib.pyplot.pcolormesh`
- :func:`yyaxis`: compute PSTH from a set of spike sequences.

.. _Neural: https://github.com/chungheng/neural/blob/master/neural/plot.py
"""
import typing as tp
import matplotlib.pyplot as plt
import numpy as np
from .. import errors as err


def plot_spikes(
    spikes: np.ndarray,
    dt: float = None,
    t: np.ndarray = None,
    ax: plt.Axes = None,
    markersize: int = None,
    color: tp.Union[str, tp.Any] = "k",
) -> plt.Axes:
    """
    Plot Spikes in raster format

    Arguments:
        spikes: the spike states in binary format, where 1 stands for a spike.
            The shape of the spikes should either be (N_times, ) or (N_trials, N_times)
        dt: time resolution of the time axis.
        t: time axes for the spikes, use arange if not provided
        ax: which axis to plot into, create one if not provided
        markersize: size of raster
        color: color for the raster. Any acceptable type of `matplotlib.pyplot.plot`'s
            color argument is accepted.

    .. note::

            If `t` is specified, it is assumed to have the same
            length as `mat.shape[1]`, which is used to find the x coordinate of
            the spiking values of the data. If `t` is
            not specified, the time-axis is formated by resolution `dt`.
            `dt` is assumed to be 1 if not specified.

    Returns:
        The axis that the raster is plotted into
    """
    spikes = np.atleast_2d(spikes)
    if spikes.ndim != 2:
        raise err.CompNeuroPlotError(
            f"matrix need to be of ndim 2, (channels x time), got ndim={spikes.ndim}"
        )

    if t is not None:
        if len(t) != spikes.shape[1]:
            raise err.CompNeuroPlotError(
                "Time vector 't' does not have the same shape as the matrix."
                f" Expected length {spikes.shape[1]} but got {len(t)}"
            )
    else:
        if dt is None:
            dt = 1.0
        else:
            if not np.isscalar(dt):
                raise err.CompNeuroPlotError("dt must be a scalar value.")
        t = np.arange(spikes.shape[1]) * dt

    if ax is None:
        fig = plt.gcf()
        ax = fig.gca()

    neu_idx, t_idx = np.nonzero(spikes)

    try:
        ax.plot(t[t_idx], neu_idx, "|", c=color, markersize=markersize)
    except ValueError as e:
        raise err.CompNeuroPlotError(
            "Raster plot failed, likely an issue with color or markersize setting"
        ) from e
    except IndexError as e:
        raise err.CompNeuroPlotError(
            "Raster plot failed, likely an issue with spikes and time vector mismatch"
        ) from e
    except Exception as e:
        raise err.CompNeuroPlotError("Raster plot failed due to unknown error") from e
    ax.set_xlim([t.min(), t.max()])
    return ax


def plot_mat(
    mat: np.ndarray,
    dt: float = None,
    dy: float = None,
    t: np.ndarray = None,
    y: np.ndarray = None,
    ax: plt.Axes = None,
    cax=None,
    vmin: float = None,
    vmax: float = None,
    cbar_kw: dict = None,
    cmap: tp.Any = None,
    shading: str = "nearest",
) -> tp.Union[tp.Tuple[plt.Axes, tp.Any], plt.Axes]:
    """
    Plot Matrix with formatted time axes

    Arguments:
        mat: the matrix to be plotted, it should of shape (N, Time)
        dt: time resolution of the time axis.
        dy: resolution of the Y-axis
        t: time axes for the matrix, use arange if not provided.
        y: spatial axes of the matrix, use arange if not provided.


        ax: which axis to plot into, create one if not provided
        cax: which axis to plot colorbar into
            - if instance of axis, plot into that axis
            - if is True, steal axis from `ax`
        vmin: minimum value for the imshow
        vmax: maximum value for the imshow
        cbar_kw: keyword arguments to be passed into the colorbar creation
        cmap: colormap to use
        shading: optional, argument to be passed to `matplotlib.pyplot.pcolormesh`

    .. note::

        If `t` is specified, it is assumed to have the same
        length as `mat.shape[1]`. Consequently, the x-axis will be formatted
        to take the corresponding values from `t` based on index. If `t` is
        not specified, the time-axis is formated by resolution `dt`.
        If neither are specified, `dt` is assumed to be 1.


    .. note::

        If `y` is specified, it is assumed to have the same
        length as `mat.shape[0]`. Consequently, the y-axis will be formatted
        to take the corresponding values from `y` based on index. If `y` is
        not specified, the time-axis is formated by resolution `dy`.
        If neither are specified, `dy` is assumed to be 1.

    Returns:
        A 2-tuple of

            1. the axis that the raster is plotted into
            2. colorbar object, only returned if cax is `True` or a `plt.Axes` instance
    """
    mat = np.atleast_2d(mat)
    if mat.ndim != 2:
        raise err.CompNeuroPlotError(
            "matrix need to be of ndim 1 (N_time),or ndim 2 (N_trials x N_times),"
            f" got ndim={mat.ndim}"
        )
    if t is not None:
        if len(t) != mat.shape[1]:
            raise err.CompNeuroPlotError(
                "Time vector 't' does not have the same shape as the matrix."
                f" Expected length {mat.shape[1]} but got {len(t)}"
            )
    else:
        if dt is None:
            dt = 1
        t = np.arange(mat.shape[1]) * dt

    if y is not None:
        if len(y) != mat.shape[0]:
            raise err.CompNeuroPlotError(
                "Spatial vector 'y' does not have the same shape as the matrix."
                f" Expected length {mat.shape[0]} but got {len(y)}"
            )
    else:
        if dy is None:
            dy = 1
        y = np.arange(mat.shape[0]) * dy

    if ax is None:
        fig = plt.gcf()
        ax = fig.gca()

    cim = ax.pcolormesh(t, y, mat, vmin=vmin, vmax=vmax, cmap=cmap, shading=shading)

    if cax:
        if cbar_kw is None:
            cbar_kw = {}
        if not isinstance(cax, plt.Axes):
            cbar = plt.colorbar(cim, ax=ax, **cbar_kw)
        else:
            cbar = plt.colorbar(cim, cax, **cbar_kw)
        return ax, cbar
    return (ax,)


def yyaxis(ax: plt.Axes, c: tp.Any = "red") -> plt.Axes:
    """
    Create a second colored axis

    Arguments:
        ax: the main axis to generate a twinx from
        c: color of the twinx, see matplotlib\'s colors_

    Returns:
        The new axis object

    .. note::

        This method will only make the twinx look like the color in
        MATLAB's :code:`yyaxis` function. However, unlike in MATLAB,
        it will not set the linestyle and linecolor of the lines that
        are plotted after twinx creation.

    .. _colors: https://matplotlib.org/stable/gallery/color/color_demo.html
    """
    ax2 = ax.twinx()
    ax2.spines["right"].set_color(c)
    ax2.tick_params(axis="y", colors=c, which="both")
    ax2.yaxis.label.set_color(c)
    return ax2
