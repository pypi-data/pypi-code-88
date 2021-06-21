import numpy as np
import logging

from .geom import intersect_box
from .log import log_and_raise
from ..material import PEC, PMC
from ..constants import fp_eps

# Constants defining maximum size, etc.
MAX_TIME_STEPS = 1e8
MAX_GRID_CELLS = 20e9
MAX_CELLS_STEPS = 5e15 # max product of grid cells and time steps
MAX_MONITOR_DATA = 10  # in Gb

def check_3D_lists(**kwargs):
    """ Verify that input arguments are lists with three elements """
    for key, val in kwargs.items():
        try:
            if not isinstance(val, list) and not isinstance(val, tuple):
                raise ValueError
            if len(val) != 3:
                raise ValueError
            for v in val:
                if type(v) in [list, tuple, np.ndarray]:
                    raise ValueError
        except:
            log_and_raise (
                f"'{key}' must be array-like with three elements.",
                ValueError
            )

def _check_outside(self, obj, name="Object"):
    """ Check if an object with a ``span`` attribute is completely outside 
    the simulation domain.
    """

    sspan = self.span_sym
    ospan = obj.span
    if np.any(ospan[:, 1] < sspan[:, 0]) or np.any(ospan[:, 0] > sspan[:, 1]):
        logging.warning(f"{name} completely outside simulation domain.")

def _check_size(self):
    """ Check the size of a simulation vs. pre-defined maximum allowed values. 
    """

    if self.Nt > MAX_TIME_STEPS:
        log_and_raise(
            f"Time steps {self.Nt:.2e} exceed current limit "
            f"{MAX_TIME_STEPS:.2e}, reduce 'run_time' or increase the "
            "spatial mesh step.",
            RuntimeError
        )

    if self.Np > MAX_GRID_CELLS:
        log_and_raise(
            f"Total number of grid points {self.Np:.2e} exceeds "
            f"current limit {MAX_GRID_CELLS:.2e}, increase the mesh step "
            "or decrease the size of the simulation domain.",
            RuntimeError
        )

    if self.Np * self.Nt > MAX_CELLS_STEPS:
        log_and_raise(
            f"Product of grid points and time steps {self.Np*self.Nt:.2e} "
            f"exceeds current limit {MAX_CELLS_STEPS:.2e}. Increase the "
            "mesh step and/or decrease the 'run_time' of the simulation.",
            RuntimeError
        )

def _check_monitor_size(self, monitor):
    """ Check if expected monitor data is too big.
    """

    from ..monitor import TimeMonitor, FreqMonitor, ModeMonitor

    # Compute how many grid points there are inside the monitor
    mnt_data = self._mnt_data(monitor)
    span_in = intersect_box(self.span_sym, monitor.span)
    size_in = span_in[:, 1] - span_in[:, 0]
    size_in[size_in == 0] = fp_eps
    if np.any(size_in < 0):
        Np = 0
    else:
        Np = np.prod([np.ceil(s/self.grid.mesh_step[d]) 
                for (d, s) in enumerate(size_in)])

    # Just get contribution from E and H fields
    fs = [s.lower()=='e' or s.lower()=='h' for s in monitor.store]
    nfields = np.sum(fs)

    if isinstance(monitor, TimeMonitor):
        # 4 bytes x N points x N time steps x 3 components x N fields
        memGB = 4*Np*mnt_data.Nt*3*nfields/1e9
        if memGB > MAX_MONITOR_DATA:
            log_and_raise(
                f"Estimated time monitor size {memGB:.2f}GB exceeds "
                f"current limit of {MAX_MONITOR_DATA:.2f}GB per monitor. "
                "Decrease monitor size or the time interval using "
                "'t_start' and 't_stop'.",
                RuntimeError
            )
                
    elif isinstance(monitor, FreqMonitor):
        # 8 bytes x N points x N freqs x 3 components x N fields
        memGB = 8*Np*len(mnt_data.freqs)*3*nfields/1e9
        if isinstance(monitor, ModeMonitor):
            # Account for all the stored eigenmodes
            memGB += memGB * monitor.Nmodes

        if memGB > MAX_MONITOR_DATA:
            log_and_raise(
                f"Estimated frequency monitor size {memGB:.2f}GB exceeds "
                f"current limit of {MAX_MONITOR_DATA:.2f}GB per monitor. " 
                "Decrease monitor size or the number of frequencies.",
                RuntimeError
            )

    return memGB

def _check_modeobj_sym(self):
    """ Check if a ModeSource or a ModeMonitor is crossing a symmetry plane.
    """
    from ..source import VolumeSource, PlaneWave, PlaneSource
    from ..monitor import ModeMonitor
    
    for dim in range(3):
        if self.symmetries[dim] == 0:
            continue

        for source in self.sources:

            if isinstance(source, (VolumeSource, PlaneWave, PlaneSource)):
                continue

            if source.span[dim, 0] < self.span_sym[dim, 0]:
                log_and_raise("Mode source with a symmetry plane not "
                    "yet implemented.", NotImplementedError)

        for monitor in self.monitors:
            if not isinstance(monitor, ModeMonitor):
                continue

            if monitor.span[dim, 0] < self.span_sym[dim, 0]:
                log_and_raise("Mode monitor with a symmetry plane not "
                    "yet implemented.", NotImplementedError)

def check_poles(material, matname, dt):
    """ Check material poles to see if numerical instability will arise.
    """

    if isinstance(material, PEC) or isinstance(material, PMC):
        return
    for ipole, (a, c) in enumerate(material.poles):
        nyquist_factor = 0.5*a.imag*dt
        if nyquist_factor >= 1:
            reduc = 0.99 / nyquist_factor
            # # Commenting out the warning until we figure this out better.
            # logging.warning(
            #     f"Material {matname} contains a high frequency pole (pole "
            #     f"index {ipole}) beyond the Nyquist limit. Recommend "
            #     f"scaling down courant by at least a factor of {reduc:.2f}."
            # )