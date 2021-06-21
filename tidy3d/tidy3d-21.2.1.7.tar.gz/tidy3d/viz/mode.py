import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from ..utils import listify, log_and_raise 
from ..monitor import ModeMonitor
from ..source import ModeSource
from .field import _plot_field_2D, _plot_field_1D

def _mode_plane(sim, mode_plane, freq_ind=0, mode_inds=None,
                val='abs', cbar=False, eps_alpha=0.3, clim=None):
    """ Plot modes stored in a ModePlane.
    """

    if mode_inds is None:
        mode_inds = np.arange(len(mode_plane.modes[freq_ind]))
    Nmodes = len(mode_inds)

    freq = mode_plane.freqs[freq_ind]
    grid_list = [(1, 2, 0, 'y', 'z'),
                (0, 2, 1, 'x', 'z'),
                (0, 1, 2, 'x', 'y')]

    (d1, d2, dn, x_lab, y_lab) = grid_list[mode_plane.norm_ind]
    N1, N2 = [mode_plane.mesh[0].size, mode_plane.mesh[1].size]

    if eps_alpha<=0:
        eps_r = None
    else:
        eps_r = np.real(mode_plane._get_eps_cent(sim, freq))

    mesh_c1 = mode_plane.mesh[0]
    mesh_c2 = mode_plane.mesh[1]
    extent = [mesh_c1[0], mesh_c1[-1], mesh_c2[0], mesh_c2[-1]]
    yext = extent[3]-extent[2]
    xext = extent[1]-extent[0]
    if xext * yext > 0:
        aspect = yext / xext
        zerodim = np.array([])
    else:
        zerodim = np.nonzero(np.array([xext, yext]) == 0)[0][0]
        nzdim = np.nonzero(np.array([xext, yext]) > 0)[0][0]
        nzlim = (mode_plane.mesh[nzdim][0], mode_plane.mesh[nzdim][-1])
        aspect = 0.8

    fig, axs = plt.subplots(Nmodes, 2, figsize=(8, 4*aspect*Nmodes),
                            constrained_layout=True)
    if Nmodes==1:
        axs = axs.reshape((1, 2))

    for (iax, imode) in enumerate(mode_inds):
        (E, _) = mode_plane.modes[freq_ind][imode].fields_to_center()
        Ec1 = E[0, :, :]
        Ec2 = E[1, :, :]

        _clim = clim
        if clim is None:
            cmax = np.amax(np.abs(np.vstack((Ec1, Ec2))))
            if val=='abs':
                _clim = (0, cmax)
            else:
                _clim = (-cmax, cmax)

        subtitle = "f=%1.2eTHz, "%(mode_plane.freqs[freq_ind]*1e-12)
        subtitle += "n=%1.2f"%mode_plane.modes[freq_ind][imode].neff
        ax_tit_1 = "Mode %d, E%s"%(imode, x_lab) + "\n" + subtitle
        ax_tit_2 = "Mode %d, E%s"%(imode, y_lab) + "\n" + subtitle

        if zerodim.size==0:
            _plot_field_2D(Ec1, eps_r, extent, x_lab, y_lab, ax_tit_1,
                        val=val, ax=axs[iax, 0], cbar=False, clim=_clim,
                        eps_alpha=eps_alpha)
            _plot_field_2D(Ec2, eps_r, extent, x_lab, y_lab, ax_tit_2,
                        val=val, ax=axs[iax, 1], cbar=cbar, clim=_clim,
                        eps_alpha=eps_alpha)
        else:
            slices = [slice(None), slice(None)]
            slices[zerodim] = 0
            nzlab = [x_lab, y_lab][nzdim]
            ylab = "Field amplitude"
            _plot_field_1D(Ec1[tuple(slices)], nzlim, _clim, nzlab,
                            ylab, ax_tit_1, val=val, ax=axs[iax, 0])
            _plot_field_1D(Ec2[tuple(slices)], nzlim, _clim, nzlab,
                            ylab, ax_tit_2, val=val, ax=axs[iax, 1])


    return fig

def viz_modes(self, mode_obj, freq_ind=0, mode_inds=None,
                val='abs', cbar=False, clim=None, eps_alpha=0.3):
    """Plot the field distribution of the 2D eigenmodes of 
    a :class:`.ModeSource` or a :class:`.ModeMonitor` object. Mode data 
    already stored in the object may be used.
    
    Parameters
    ----------
    mode_obj : ModeSource or ModeMonitor
        An object on which :meth:`.Simulation.compute_modes` can be used.
    freq_ind : int, optional
        Frequency index of the stored modes to be plotted.
    mode_inds : array_like or None, optional
        If provided, only visualize the modes with specified indexes.
    val : {'re', 'im', 'abs'}, optional
        Plot the real part (default), or the imaginary or absolute value of 
        the field components.
    cbar : bool, optional
        Add a colorbar to the plot.
    clim : List[float], optional
        Matplotlib color limit to use for plot.
    eps_alpha : float, optional
        If larger than zero, overlay the underlying permittivity distribution, 
        with opacity defined by eps_alpha.
    
    Returns
    -------
    Matplotlib figure object
    
    Note
    ----
    The modes of the ``mode_object`` must have been previously computed with
    :meth:`.compute_modes`.
    """

    if isinstance(mode_obj, ModeSource):
        data = self._src_data(mode_obj)
    elif isinstance(mode_obj, ModeMonitor):
        data = self._mnt_data(mode_obj)
    else:
        log_and_raise(
            "Input 0 must be an instance of ModeSource or ModePlane.",
            ValueError
        )

    mplane = data.mode_plane
    nfreqs = len(mplane.modes)

    # Check if frequency index out of bounds
    if nfreqs < freq_ind:
        log_and_raise(
            f"Frequency index {freq_ind} our of bounds for "
            f"stored modes number of frequencies {nfreqs}.",
            ValueError
        )

    Nmodes = len(mplane.modes[freq_ind])
    if Nmodes==0:
        log_and_raise("Modes must be computed using compute_modes first.",
            RuntimeError
        )
    if mode_inds is not None:
        if np.amax(mode_inds) > Nmodes - 1:
            log_and_raise("Mode index exceeds number of modes found in "
                "mode object.", RuntimeError
            )
    
    fig = _mode_plane(self, mplane, freq_ind,
                val=val, cbar=cbar, clim=clim, eps_alpha=eps_alpha)

    return fig