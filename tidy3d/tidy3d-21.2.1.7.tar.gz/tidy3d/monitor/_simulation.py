import numpy as np
import logging

from ..constants import int_, float_, complex_, fp_eps, xyz_dict, xyz_list
from ..utils.em import poynting_insta, poynting_avg
from ..utils.log import log_and_raise, MonitorError
from ..utils import axes_handed
from ..mode import dot_product

from .Monitor import ModeMonitor, FreqMonitor, TimeMonitor

def _compute_modes_monitor(self, monitor, Nmodes, target_neff=None):
    """Compute the eigenmodes of the 2D cross-section of a ModeMonitor object.
    """   

    # Set the Yee permittivity if not yet set
    mplane = self._mnt_data(monitor).mode_plane
    if mplane.eps_e1 is None:
        mplane._set_yee_sim(self)
    # Compute the mode plane modes
    mplane.compute_modes(Nmodes, target_neff=target_neff)

def _mnt_data(self, monitor):
    """Get the monitor data object from a monitor, if it is in the simulation.
    """
    try:
        mnt_data = self._monitor_ids[id(monitor)]
        return mnt_data
    except KeyError:
        log_and_raise(
            "Monitor has not been added to Simulation!",
            MonitorError
        )

def data(self, monitor):
    """Return a dictionary with all the stored data in a :class:`.Monitor`.
    
    Parameters
    ----------
    monitor : Monitor
        The queried monitor.
    
    Returns
    -------
    monitor_data : dict
        Dictonary with all the data currently in the monitor. For example, in 
        a frequency monitor, after a simulation run, ``monitor_data['E']`` and 
        ``monitor_data['H']`` are 5D arrays of shape ``(3, Nx, Ny, Nz, Nf)`` 
        The first index is the vector component of the field, the next three 
        dimensions index the x, y, z, position in space, and the last index
        is the frequency index at which the data was stored.

        Returned data is organized as follows

        * ``'xmesh'``: (micron) Positions along x where the fields are stored.
        * ``'ymesh'``: (micron) Positions along y where the fields are stored.
        * ``'zmesh'``: (micron) Positions along z where the fields are stored.
        * ``'tmesh'``: (s) Time points at which the fields are stored. Empty 
          array for a frequency monitor.
        * ``'freqs'``: (Hz) Frequencies at which the fields are stored. Empty 
          array for a time monitor.
        * ``'E'``: (V/micron) E-field array (empty if ``'E' not in 
          Monitor.store``).
        * ``'H'``: (A/micron) H-field array (empty if ``'H' not in 
          Monitor.store``).
        * ``'flux'``: (W) flux array with size equal to the size of ``tmesh``
          for a :class:`TimeMonitor` and to the size of ``freqs`` for a
          :class:`FreqMonitor`. Only returned if ``'flux' in Monitor.store``.
        * ``'S'``: (W/micron\\ :sup:`2`) Poynting vector (power flux density) 
          if it has been computed with :meth:`Simulation.poynting`.
        * ``'mode_amps'`` (W\\ :sup:`1/2`) For a :class:`ModeMonitor`,
          the decomposition coefficients into the different modes, in units of
          power amplitude. The shape of the array is ``(2, Nf, Nmodes)``, where
          ``mode_amps[0, :, :]`` are the coefficients for forward-propagating
          modes, and ``mode_amps[1, :, :]`` - for backward-propagating modes.
        * ``'modes'`` For a :class:`ModeMonitor`, a list of length ``Nf`` of
          lists of length ``Nmodes`` of ``Mode`` objects which store the ``E``
          and ``H`` fields of each mode as well as the real and imaginary part
          of the effective index, ``neff`` and ``keff``. The fields are
          oriented in the mode plane axes, such that they are arrays of shape
          (3, Np1, Np2) where ``Np1`` and ``Np2`` are the two in-plane
          directions. The three components are also oriented in-plane as
          ``(parallel_1, parallel_2, normal)``.
    """

    mnt_data = self._mnt_data(monitor)
    return_dict = {
        'xmesh': mnt_data.xmesh,
        'ymesh': mnt_data.ymesh,
        'zmesh': mnt_data.zmesh,
        'tmesh': mnt_data.tmesh,
        'freqs': mnt_data.freqs,
    }

    if isinstance(mnt_data.monitor, ModeMonitor):
        return_dict.update({'modes': mnt_data.mode_plane.modes})

    if mnt_data.data is False:
        return return_dict

    return_dict.update({
        'E': mnt_data.E,
        'H': mnt_data.H,
    })

    if mnt_data.flux.size > 0:
        return_dict.update({'flux': mnt_data.flux})
    if mnt_data.S.size > 0:
        return_dict.update({'S': mnt_data.S})
    if mnt_data.mode_amps.size > 0:
        return_dict.update({'mode_amps': mnt_data.mode_amps})

    return return_dict

def poynting(self, monitor):
    """Compute the Poynting vector at every point recorded by a 
    :class:`.Monitor`. Returns the instantaneous power flux per unit area at 
    every time for a :class:`.TimeMonitor`, and the time-averaged power flux 
    per unit area at every frequency for a :class:`.FreqMonitor`.
     
    Returns
    -------
    np.ndarray
        (Watt/micron\\ :sup:`2`) The Poynting vector, i.e. the directed power 
        flux per unit area, at every sampling point of the monitor. Same shape 
        as the ``E`` and ``H`` fields stored in the monitor.
    """

    mnt_data = self._mnt_data(monitor)

    if mnt_data.E.size==0:
        log_and_raise(
            "No electric field stored in the monitor.",
            ValueError
        )
    if mnt_data.H.size==0:
        log_and_raise(
            "No magnetic field stored in the monitor.",
            ValueError
        )

    if isinstance(monitor, TimeMonitor):
        mnt_data._S = poynting_insta(mnt_data.E, mnt_data.H)
    elif isinstance(monitor, FreqMonitor):
        mnt_data._S = poynting_avg(mnt_data.E, mnt_data.H)

    return mnt_data._S

def flux(self, monitor, normal=None):
    """Compute the area-integrated Poynting flux in a given direction. 
    This is the total power flowing through a plane orthogonal to the 
    ``normal`` direction. If the monitor is larger than one in that 
    direction, the flux at every pixel is returned. Returns the instantaneous 
    power flux at every time for a :class:`.TimeMonitor`, and the 
    time-averaged power flux at every frequency for a :class:`.FreqMonitor`.
    
    Parameters
    ----------
    normal : {'x', 'y', 'z'}, or None
        If ``None``, normal is set to the first dimension along which the 
        Monitor spans a single pixel.
    
    Returns
    -------
    np.ndarray
        (Watt) The Poynting flux, an array of shape ``(Nsample, Np)``, where 
        ``Np`` are the number of points in the monitor volume along the 
        normal direction, while ``Nsample`` is the number of time steps 
        or frequencies in the monitor. If ``Np==1``, the return shape is just
        ``(Nsample, )``.
    """

    mnt_data = self._mnt_data(monitor)

    if normal is None:
        dmin = np.argmin(mnt_data.inds_end - mnt_data.inds_beg)
        normal = xyz_list[dmin]
    try:
        norm_ind = xyz_dict[normal]
    except:
        log_and_raise("'normal' must be one of 'x', 'y', or 'z'.", ValueError)

    cross_inds = [0, 1, 2]
    cross_inds.pop(norm_ind)

    if mnt_data.S.size==0:
        self.poynting(monitor)

    # Compute numerical integral.
    fl = np.prod(mnt_data.mesh_step[cross_inds]) * \
            np.sum(mnt_data.S[norm_ind, :, :, :, :],
                axis=(cross_inds[0], cross_inds[1])).astype(float_)

    # Transpose so that time/frequency index comes first
    fl = fl.T

    return fl

def decompose(self, mode_monitor):
    """Compute the decomposition of the fields recorded in a 
    :class:`.ModeMonitor` into the eigenmodes in the monitor plane.  

    Parameters
    ----------
    mode_monitor : ModeMonitor
        ModeMonitor object to compute the decomposition for.
    
    Returns
    -------
    np.ndarray
        A tuple of two arrays giving the overlap coefficients of the mode 
        fields with the forward- and backward-propagating eigenmodes, 
        respectively. Each array has shape ``(Nfreqs, Nmodes)``, where 
        ``Nfreqs`` is the number of frequencies in the monitor.
    """

    if not isinstance(mode_monitor, ModeMonitor):
        log_and_raise("'ModeMonitor' instance expected.", TypeError)

    mnt_data = self._mnt_data(mode_monitor)
    Nmodes = mnt_data.Nmodes
    target_neff = mnt_data.target_neff
    mplane = mnt_data.mode_plane

    if Nmodes > len(mplane.modes[0]):
        self.compute_modes(mode_monitor, Nmodes, target_neff)

    if mnt_data.data is False:
        log_and_raise("No data loaded in monitor.", RuntimeError)

    Nfreqs = len(mnt_data.freqs)
    positive_coeff = np.zeros((Nfreqs, Nmodes), dtype=complex_)
    negative_coeff = np.zeros((Nfreqs, Nmodes), dtype=complex_)

    for ifreq in range(Nfreqs):
        # Need to get the monitor field of shape (3, Ncross1, Ncross2)
        E = mnt_data.E[mplane.new_ax[0:2], :, :, :, ifreq]
        H = mnt_data.H[mplane.new_ax[0:2], :, :, :, ifreq]
        # +/-1 factor on H due to axes change
        H *= axes_handed(mplane.new_ax)
        fields_monitor = (np.squeeze(E, axis=1 + mnt_data.norm_ind),
                        np.squeeze(H, axis=1 + mnt_data.norm_ind))

        for imode, mode in enumerate(mplane.modes[ifreq]):
            # Fields of the mode snapped to Yee grid centers
            (Em, Hm) = mode.fields_to_center()
            # Overlap with positive-direction mode
            positive_coeff[ifreq, imode] = dot_product(
                                    (Em, Hm), fields_monitor,
                                    mplane.mesh_step)
            # Overlap with negative-direction mode.
            # Note: the sign of the fields is correct only for the tangential 
            # components, but those are the only ones entering the dot product.
            negative_coeff[ifreq, imode] = dot_product(
                                    (np.conj(Em), -np.conj(Hm)), 
                                    fields_monitor,
                                    mplane.mesh_step)

    return positive_coeff, negative_coeff

def set_monitor_modes(self, monitor, Nmodes=None, target_neff=None):
    """Set the number ``Nmodes`` of modes with effective index closest
    to ``target_neff`` to be used in the modal decomposition in the monitor.
    
    Parameters
    ----------
    monitor : ModeMonitor
        A mode monitor in the simulation.
    Nmodes : None or int, optional
        Number of modes to compute. If ``None``, uses ``monitor.Nmodes``.
    target_neff : None or float, optional
        Look for modes with effective index closest to ``target_neff``. If
        ``None``, the modes are computed in order of decreasing index.
    """

    mnt_data = self._mnt_data(monitor)
    mplane = mnt_data.mode_plane

    if isinstance(monitor, ModeMonitor):

        if Nmodes is not None:
            mnt_data.Nmodes = Nmodes
        mnt_data.target_neff = target_neff

    else:
        log_and_raise(
            "Input 0 must be an instance of a ModeMonitor.", MonitorError
        )