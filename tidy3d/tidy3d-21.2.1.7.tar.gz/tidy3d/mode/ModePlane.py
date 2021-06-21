import numpy as np
import h5py

from ..constants import float_
from ..utils import inside_box_coords, listify, log_and_raise, subprocess_cmd
from ..utils.log import Tidy3DError
from .solver import compute_modes as get_modes
from .dot_product import dot_product

class ModePlane(object):
    """2D plane for computation of modes used in ModeSource and ModeMonitor.
    The coordinate system with respect to which meshes and fields are defined 
    here is always such that the z-axis is normal to the plane.
    """
    def __init__(self, span, norm_ind):
        """Construct.
        
        Parameters
        ----------
        span : np.ndarray of shape (3, 2)
            (micron) Defines (xmin, xmax), (ymin, ymax), (zmin, zmax) of the 
            mode plane.
        norm_ind : int
            Specifies the normal direction. We must then also have 
            ``span[mode_ind, 0] = span[mode_ind, 1]``.
        """
        self.span = span
        self.norm_ind = norm_ind
        
        """ Everything is stored in axes oriented as 
        (in_plane1, in_plane2, normal). Array self.new_ax defines how to do the
        switching between simulation axes and ModePlane axes:
            sim_axes[self.new_ax] -> ModePlane axes
            mpl_axes[self.new_ax[a] for a in self.new_ax] -> simulation axes
        """
        self.new_ax = [0, 1, 2]
        self.new_ax.pop(self.norm_ind)
        self.new_ax.append(self.norm_ind)
        self.old_ax = np.argsort(self.new_ax).tolist()

        """Variables below to be set after based on the Simulation object to 
        which the ModePlane is added. """

        # Permittivity and mesh at the center of the Yee cell.
        self.mesh = None
        self.eps = None
        # Permittivity and mesh for field components along the two 
        # cross-section directions and the normal direction
        self.mesh_e1 = None
        self.eps_e1 = None
        self.mesh_e2 = None
        self.eps_e2 = None
        self.mesh_en = None
        self.eps_en = None

        """List of modes, set by a call to ``compute_modes()``. The first list 
        dimension is equal to the number of sampling frequencies, while the 
        second dimension is the number of computed modes. Each mode is given by 
        a dictionary with the fields and propagation constants."""
        self.modes = [[]]
        self.freqs = []

    def _set_sim(self, sim, freqs):
        """ Set the mesh of the ModePlane based on a global simulation mesh, 
        and the indexing of that mesh w.r.t. the simulation grid.
        Also set the ModePlane frequencies and the ``modes`` attribute as a
        list of Nfreqs empty lists.
        """
        self.freqs = listify(freqs)
        self.modes = [[] for i in range(len(self.freqs))]
        indsx, indsy, indsz = inside_box_coords(self.span, sim.grid.coords)
        if np.any([inds[0]==inds[1] for inds in (indsx, indsy, indsz)]):
            raise Tidy3DError(
                "Mode plane position is outside simulation domain."
            )

        """Array of shape (3, 2) of int defining the starting and stopping 
        index in the global simulation grid of the ModePlane span."""
        self.span_inds = np.array([[inds[0], inds[1]] 
                                    for inds in (indsx, indsy, indsz)])

        # Space and time resolution from global grid.
        self.mesh_step = [sim.grid.mesh_step[a] for a in self.new_ax]
        self.time_step = sim.grid.dt

        # Lists to store variables at Yee grid center and at the E-field 
        # polarization locations in the new axes
        meshes = []
        sim_ms = [sim.grid.mesh]
        sim_ms += [sim.grid.mesh_ex, sim.grid.mesh_ey, sim.grid.mesh_ez]

        for im, mesh in enumerate(sim_ms):
            # Average the edges for the Yee grid coordinates, otherwise 
            # include them in eps (used for plotting)
            plane_mesh = (mesh[0][indsx[0]:indsx[1]],
                          mesh[1][indsy[0]:indsy[1]],
                          mesh[2][indsz[0]:indsz[1]])
            meshes.append([plane_mesh[a] for a in self.new_ax])

        self.mesh = meshes[0]
        self.mesh_e1 = meshes[1 + self.new_ax[0]]
        self.mesh_e2 = meshes[1 + self.new_ax[1]]
        self.mesh_en = meshes[1 + self.norm_ind]


    def _get_eps_cent(self, sim, freq):
        """Get the (non-averaged) permittivity at the center of the Yee cells,
        in ModePlane axes, at a given frequency. Used for plotting.
        """

        plane_mesh = (
            sim.grid.mesh[0][self.span_inds[0, 0]:self.span_inds[0, 1]],
            sim.grid.mesh[1][self.span_inds[1, 0]:self.span_inds[1, 1]],
            sim.grid.mesh[2][self.span_inds[2, 0]:self.span_inds[2, 1]]
        )

        eps = sim._get_eps(plane_mesh, edges='in', freq=freq)
        eps = np.squeeze(eps, axis=self.norm_ind)

        # Return as shape (N_cross_ind1, N_cross_ind2)
        return eps


    def _set_eps_yee(self, sim, file_in, file_out, dset_name):
        """Set the permittivity at the Yee locations using a call to the C++
        solver that applies subpixel averaging as in the time stepping."""

        mfile = h5py.File(file_in, "w")
        grp = mfile.create_group(dset_name)
        grp.create_dataset("span_inds", data=self.span_inds)
        grp.create_dataset("freqs", data=np.array([self.freqs]))

        # # Compute eps_yee from python if needed
        # self._set_yee_sim(sim)
        # # Change to simulation axes
        # eps_mpl = [self.eps_e1, self.eps_e2, self.eps_en]
        # eps_sim = np.stack(
        #     [np.moveaxis(eps_mpl[self.new_ax[a]][:, :, :, None],
        #     [1, 2, 3], 1 + np.array(self.new_ax)) for a in self.new_ax],
        #     axis=1)
        # grp.create_dataset("eps_python", data=eps_sim)
        
        mfile.close()

        gencoeffs_args = f"{sim.fjson} {file_in} {file_out}"
        subprocess_cmd(f"{sim.fdtd_path}/solver/gencoeffs {gencoeffs_args}")

        mfile = h5py.File(file_out, "r")
        eps_sub = np.array(mfile[dset_name]['eps'])
        self._set_yee_arr(eps_sub)
        mfile.close()


    def _set_yee_sim(self, sim):
        """ Return the permittivity at the Yee grid positions by passing the 
        simulation in which the mode plane is embedded.
        """

        epses = []
        meshes = [self.mesh_e1, self.mesh_e2, self.mesh_en]

        for im, mesh in enumerate(meshes):
            eps_freqs = []
            # Mesh rotated back in simulation axis
            sim_mesh = [mesh[a] for a in self.old_ax]

            for freq in self.freqs:
                eps = sim._get_eps(sim_mesh, edges='average', freq=freq)
                eps = np.squeeze(eps, axis=self.norm_ind)
                eps_freqs.append(eps)

            epses.append(np.stack(eps_freqs, axis=0))

        [self.eps_e1, self.eps_e2, self.eps_en] = epses


    def _set_yee_arr(self, eps_yee):
        """ Return the permittivity at the Yee grid positions by passing an 
        array of shape (Nfreqs, Nx, Ny, Nz, 3) (as computed from C++ solver).
        """

        eps_new = np.moveaxis(eps_yee, 1 + np.array(self.new_ax), [1, 2, 3])
        self.eps_e1 = eps_new[:, :, :, 0, self.new_ax[0]]
        self.eps_e2 = eps_new[:, :, :, 0, self.new_ax[1]]
        self.eps_en = eps_new[:, :, :, 0, self.new_ax[2]]


    def compute_modes(self, Nmodes, target_neff=None, pml_layers=[0, 0]):
        """ Compute the ``Nmodes`` eigenmodes in decreasing order of 
        propagation constant at every frequency in the list ``freqs``.
        """

        for (ifreq, freq) in enumerate(self.freqs):
            modes = self._compute_modes_ifreq(
                ifreq, Nmodes, target_neff, pml_layers)
            self.modes[ifreq] = modes 

    def _compute_modes_ifreq(self, ifreq, Nmodes, target_neff=None,
            pml_layers=[0, 0]):
        """ Compute the ``Nmodes`` eigenmodes in decreasing order of 
        propagation constant for frequency index ``ifreq``.
        """

        if self.mesh is None:
            raise Tidy3DError(
                "Mode plane has not been added to a simulation yet."
            )

        freq = self.freqs[ifreq]
        # Get permittivity. Slightly break the c1-c2 symmetry to avoid 
        # complex-valued degenerate modes.
        epses = [self.eps_e1[ifreq],
                 self.eps_e2[ifreq] + 1e-6,
                 self.eps_en[ifreq]]

        # Get modes
        modes = get_modes(
            epses,
            freq,
            mesh_step=self.mesh_step,
            pml_layers=pml_layers,
            num_modes=Nmodes,
            target_neff=target_neff)
        
        for mode in modes:
            # Normalize to unit power flux
            fields_cent = mode.fields_to_center()
            flux = dot_product(fields_cent, fields_cent, self.mesh_step)
            mode.E /= np.sqrt(flux)
            mode.H /= np.sqrt(flux)
            # Make largest E-component real
            mode.fix_efield_phase()

        return modes