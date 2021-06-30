"""CosmiX model to generate charge by ionization."""
from pathlib import Path
import numpy as np
try:
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
except ImportError:
    # raise Warning('Matplotlib cannot be imported')
    plt = None
from cosmix.util import load_data_into_histogram, load_geant4_histogram


class Plotting:
    """Plotting class for CosmiX."""

    def __init__(self,
                 show_plots: bool = True,
                 output_dir: str = 'outputs',
                 geometry: dict = None
                 ) -> None:
        """TBW.

        :param show_plots:
        :param output_dir:
        """
        self.show_plots = show_plots
        self.output_dir = output_dir
        self.geometry = geometry

    def save_and_draw(self, fig_name: str):
        """TBW.

        :param fig_name:
        """
        plt.savefig(self.output_dir + '/' + fig_name + '.png')
        if self.show_plots:
            plt.draw()

    def show(self):
        """TBW."""
        if self.show_plots:
            plt.show()

    # def plot_cdf(self, cdf, title: str = 'CDF', label=None, xlabel='', log=True):
    #     """TBW."""
    #     if isinstance(cdf, str) or isinstance(cdf, Path):
    #         cdf = np.load(cdf)
    #     plt.title(title)
    #     plt.xlabel(xlabel)
    #     if log:
    #         plt.semilogx(cdf[:, 0], cdf[:, 1], '.', label=label, markersize=2.)
    #     else:
    #         plt.plot(cdf[:, 0], cdf[:, 1], '.', label=label, markersize=2.)
    #     if label:
    #         plt.legend()
    #     self.save_and_draw('tars_plot_'+title.replace(' ', '_'))
    #
    # def plot_spectrum_cdf(self):
    #     """TBW."""
    #     plt.figure()
    #     plt.semilogx(self.tars.spectrum_cdf[:, 0], self.tars.spectrum_cdf[:, 1], '.')
    #     plt.title('Spectrum CDF')
    #     plt.xlabel('Energy (MeV)')
    #     self.save_and_draw('tars_plot_spectrum_cdf')
    #
    # def plot_flux_spectrum(self, energy, flux, label=None):
    #     """TBW."""
    #     # plt.figure()
    #     plt.title('Proton flux spectrum by tars')
    #     plt.xlabel('Energy (MeV)')
    #     plt.ylabel('Flux (1/(s*MeV))')
    #     plt.loglog(energy, flux, '.', label=label, markersize=2)
    #     if label:
    #         plt.legend()
    #     self.save_and_draw('tars_plot_flux_spectrum')
    #
    # def plot_spectrum_hist(self, data):
    #     """TBW."""
    #     plt.figure()
    #     plt.title('Proton flux spectrum sampled by TARS')
    #     plt.xlabel('Energy (MeV)')
    #     plt.ylabel('Counts')
    #     # plt.ylabel('Flux (1/(s*MeV))')
    #     # plt.loglog(lin_energy_range, flux_dist)
    #
    #     if isinstance(data, str):
    #         if data.endswith('.npy'):
    #             data = np.load(data)
    #
    #     hist_bins = 250
    #     # hist_range = (1e-1, 1e5)
    #     # col = (0, 1, 1, 1)
    #     plt.hist(data, bins=np.logspace(np.log10(0.1), np.log10(1e5), hist_bins))
    #     plt.gca().set_xscale("log")
    #     # plt.legend(loc='upper right')
    #     self.save_and_draw('tars_spectrum')
    #
    # def plot_spectra(self, log=False):
    #     """TBW."""
    #     plt.figure()
    #     plt.title('Proton spectra')
    #     plt.xlabel('Energy (MeV)')
    #     plt.ylabel('Counts')
    #     hist_range = (1e-1, 1e5)
    #     hist_bins = 400
    #     hist_bins = np.logspace(np.log10(hist_range[0]), np.log10(hist_range[1]), hist_bins)
    #     # plt.axis([hist_range[0], hist_range[1], 1., 1.e+3])
    #     plt.ylim([0., 300])
    #
    #     hist_names = {
    #         # # with old TARS G4 app (using MicroElec)
    #         # 'E$_{init?}$, TARS (G4app), interpol., lin. sampl.':
    #         #     Path(r'C:\dev\work\tars-old-validation\validation' +
    #         #          r'\G4_app_results_20180425\tars-p_energy_lst_per_event.npy'),
    #         # 10k
    #         r'E$_{init}$, TARS (stepsize), no interpol.':
    #             Path(r'C:\dev\work\pyxel\tars_p_init_energy_lst_per_event_10k_v7.npy'),
    #         # 10k
    #         r'E$_{final}$, TARS (stepsize), no interpol.':
    #             Path(r'C:\dev\work\pyxel\tars_p_final_energy_lst_per_event_10k_v7.npy'),
    #
    #         # latest
    #         r'E$_{init}$, TARS (stepsize) latest':
    #             Path(r'C:\dev\work\pyxel\tars_p_init_energy_lst_per_event.npy'),
    #         # latest
    #         r'E$_{final}$, TARS (stepsize) latest':
    #             Path(r'C:\dev\work\pyxel\tars_p_final_energy_lst_per_event.npy')
    #     }
    #     for label, filename in hist_names.items():
    #         histogram_data = np.load(filename)
    #         col = None
    #         plt.hist(histogram_data, bins=hist_bins, range=hist_range, log=log,
    #                  histtype='step', label=label, color=col)
    #     plt.gca().set_xscale("log")
    #     plt.legend(loc='upper right')
    #     self.save_and_draw('tars_hist_initial_final_proton_spectra')

    def event_polar_angle_dist(self, alpha, beta):
        """TBW."""
        if isinstance(alpha, str):
            if alpha.endswith('.npy'):
                alpha = np.load(alpha)
        if isinstance(beta, str):
            if beta.endswith('.npy'):
                beta = np.load(beta)
        fig = plt.figure()
        fig.add_subplot(111, polar=True)
        plt.hist(alpha, bins=360, histtype='step', label='alpha')
        plt.hist(beta, bins=360, histtype='step', label='beta')
        plt.legend()
        plt.title('Incident angle distributions')
        plt.xlabel('')
        plt.ylabel('')
        self.save_and_draw('event_angles')

    def cluster_charge_number(self, chg_num):
        """TBW."""
        if isinstance(chg_num, str):
            if chg_num.endswith('.npy'):
                chg_num = np.load(chg_num, allow_pickle=True)
        all_charge_cluster = []
        for chg_list in chg_num:
            all_charge_cluster += list(chg_list)
        plt.figure()
        plt.hist(all_charge_cluster, bins=100, histtype='step')
        plt.title('Charge number per cluster')
        plt.xlabel('[e-]')
        plt.ylabel('')
        self.save_and_draw('cluster_charge_number')

    def cluster_positions(self, chg_v_pos, chg_h_pos, chg_z_pos):
        """TBW."""
        if isinstance(chg_v_pos, str):
            if chg_v_pos.endswith('.npy'):
                chg_v_pos = np.load(chg_v_pos, allow_pickle=True)
        if isinstance(chg_h_pos, str):
            if chg_h_pos.endswith('.npy'):
                chg_h_pos = np.load(chg_h_pos, allow_pickle=True)
        if isinstance(chg_z_pos, str):
            if chg_z_pos.endswith('.npy'):
                chg_z_pos = np.load(chg_z_pos, allow_pickle=True)
        all_cluster_v_pos = []
        all_cluster_h_pos = []
        all_cluster_z_pos = []
        for v, h, z in zip(chg_v_pos, chg_h_pos, chg_z_pos):
            all_cluster_v_pos += list(v)
            all_cluster_h_pos += list(h)
            all_cluster_z_pos += list(z)
        plt.figure()
        plt.hist(all_cluster_v_pos, bins=100, histtype='step', label='vertical')
        plt.hist(all_cluster_h_pos, bins=100, histtype='step', label='horizontal')
        plt.legend()
        plt.title('Cluster positions')
        plt.xlabel('v, h [um]')
        plt.ylabel('')
        self.save_and_draw('cluster_positions_yx')
        plt.figure()
        plt.hist(all_cluster_z_pos, bins=100, color='g', histtype='step', label='z')
        plt.legend()
        plt.title('Cluster positions')
        plt.xlabel('z [um]')
        plt.ylabel('')
        self.save_and_draw('cluster_positions_z')

    def event_direction_hist(self, direction):
        """TBW."""
        if isinstance(direction, str):
            if direction.endswith('.npy'):
                direction = np.load(direction)
        plt.figure()
        plt.hist(direction[:, 0], bins=100, histtype='step', label='vert')
        plt.hist(direction[:, 1], bins=100, histtype='step', label='horz')
        plt.hist(direction[:, 2], bins=100, histtype='step', label='z')
        plt.legend()
        plt.title('Direction per event')
        plt.xlabel('')
        plt.ylabel('')
        self.save_and_draw('event_direction')

    def geometry_3d(self, margin=1):
        """TBW."""
        fig = plt.figure(figsize=plt.figaspect(1.))
        # fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1, projection='3d')
        point1 = np.array([0, 0, 0])
        point2 = np.array([0, 0, -1 * self.geometry['det_total_thickness']])
        normal = np.array([0, 0, 1])
        d1 = -point1.dot(normal)
        d2 = -point2.dot(normal)
        xx, yy = np.meshgrid(np.linspace(0, self.geometry['det_vert_dimension'], 10),
                             np.linspace(0, self.geometry['det_horz_dimension'], 10))
        z1 = (-normal[0] * xx - normal[1] * yy - d1) * 1. / normal[2]
        z2 = (-normal[0] * xx - normal[1] * yy - d2) * 1. / normal[2]
        ax.plot_surface(xx, yy, z1, alpha=0.2, color=(0, 0, 1))
        ax.plot_surface(xx, yy, z2, alpha=0.2, color=(0, 0, 1))
        ax.set_xlim(-1 * margin, self.geometry['det_vert_dimension'] + margin)
        ax.set_ylim(-1 * margin, self.geometry['det_horz_dimension'] + margin)
        ax.set_zlim(-1 * self.geometry['det_total_thickness'] - margin, margin)
        ax.set_xlabel(r'vertical [$\mu$m]')
        ax.set_ylabel(r'horizontal [$\mu$m]')
        ax.set_zlabel(r'z [$\mu$m]')

    def event_tracks_3d(self, first_pos, last_pos):
        """TBW."""
        if isinstance(first_pos, str):
            if first_pos.endswith('.npy'):
                first_pos = np.load(first_pos)
        if isinstance(last_pos, str):
            if last_pos.endswith('.npy'):
                last_pos = np.load(last_pos)
        self.geometry_3d()
        ax = plt.gca()
        for first, last in zip(first_pos, last_pos):
            ax.plot([first[0], last[0]],
                    [first[1], last[1]],
                    [first[2], last[2]],
                    'x-', c='r')
        plt.title('Event tracks')
        self.save_and_draw('event_tracks_3d')

    def cluster_charges_3d(self, chg_v_pos, chg_h_pos, chg_z_pos, chg_num):
        """TBW."""
        if isinstance(chg_v_pos, str):
            if chg_v_pos.endswith('.npy'):
                chg_v_pos = np.load(chg_v_pos, allow_pickle=True)
        if isinstance(chg_h_pos, str):
            if chg_h_pos.endswith('.npy'):
                chg_h_pos = np.load(chg_h_pos, allow_pickle=True)
        if isinstance(chg_z_pos, str):
            if chg_z_pos.endswith('.npy'):
                chg_z_pos = np.load(chg_z_pos, allow_pickle=True)
        if isinstance(chg_num, str):
            if chg_num.endswith('.npy'):
                chg_num = np.load(chg_num, allow_pickle=True)
        self.geometry_3d()
        ax = plt.gca()
        for v, h, z, s in zip(chg_v_pos, chg_h_pos, chg_z_pos, chg_num):
            cluster_sizes = [k / 10. for k in s]
            ax.scatter(v, h, z, c='b', marker='.', s=cluster_sizes)
        plt.title('Cluster positions and sizes in 3d')
        self.save_and_draw('cluster_charges_3d')

    def event_energy_deposited(self, edep):
        """TBW."""
        if isinstance(edep, str):
            if edep.endswith('.npy'):
                edep = np.load(edep)
        plt.figure()
        plt.hist(edep, bins=100, histtype='step', label='edep')
        plt.legend()
        plt.title('Energy deposited per event')
        plt.xlabel('[keV]')
        plt.ylabel('')
        self.save_and_draw('event_energy_deposited')

    def event_electrons_deposited(self, elec):
        """TBW."""
        if isinstance(elec, str):
            if elec.endswith('.npy'):
                elec = np.load(elec)
        plt.figure()
        plt.hist(elec, bins=100, histtype='step', label='elec')
        plt.legend()
        plt.title('Electrons deposited per event')
        plt.xlabel('[e-]')
        plt.ylabel('')
        self.save_and_draw('event_electrons_deposited')

    def event_proton_spectra(self, init, final):
        """TBW."""
        if isinstance(init, str):
            if init.endswith('.npy'):
                init = np.load(init)
        if isinstance(final, str):
            if final.endswith('.npy'):
                final = np.load(final)
        plt.figure()
        plt.hist(init, bins=100, histtype='step', label='initial')
        plt.hist(final, bins=100, histtype='step', label='final')
        plt.legend()
        plt.title('Proton spectra')
        plt.xlabel('energy [MeV]')
        plt.ylabel('')
        self.save_and_draw('event_proton_spectra')

    def event_starting_position(self, start_pos):
        """TBW."""
        if isinstance(start_pos, str):
            if start_pos.endswith('.npy'):
                start_pos = np.load(start_pos)
        self.geometry_3d(margin=5)
        ax = plt.gca()
        ax.scatter(start_pos[:, 0], start_pos[:, 1], start_pos[:, 2], marker='*')
        plt.title('Proton starting position')
        self.save_and_draw('event_starting_position')

    def event_track_length(self, track):
        """TBW."""
        if isinstance(track, str):
            if track.endswith('.npy'):
                track = np.load(track)
        plt.figure()
        plt.hist(track, bins=100, histtype='step', label='track')
        plt.legend()
        plt.title('Track length per event')
        plt.xlabel(r'[$\mu$m]')
        plt.ylabel('')
        self.save_and_draw('event_track_length')

    def cluster_step_size(self, step_size):
        """TBW."""
        if isinstance(step_size, str):
            if step_size.endswith('.npy'):
                step_size = np.load(step_size)
        plt.figure()
        plt.hist(step_size,
                 bins=np.logspace(np.log10(np.min(step_size)), np.log10(np.max(step_size)), 100),
                 histtype='step', label='step size')
        plt.gca().set_xscale("log")
        plt.legend()
        plt.title('Step size per cluster')
        plt.xlabel(r'[$\mu$m]')
        plt.ylabel('')
        self.save_and_draw('cluster_step_size')

    def plot_plato_hists(self, edep, elec):
        """TBW."""
        cosmix_edep = None
        if isinstance(edep, str):
            if edep.endswith('.npy'):
                cosmix_edep = np.load(edep)
        cosmix_elec = None
        if isinstance(elec, str):
            if elec.endswith('.npy'):
                cosmix_elec = np.load(elec)

        x = [10000, 1000, 1000, 2000, 3000, 1000, 10000, 4000]
        path = Path(__file__).parent.joinpath('data', 'validation')
        g4file = Path(path, 'PLATO_irrad_proton_spectrum_15um_Silicon_10000_MicroElec.ascii')
        # plato_spectrum_step_size = load_geant4_histogram(g4file, hist_type='step_size', skip_rows=4, read_rows=x[0])
        plato_spectrum_all_elec = load_geant4_histogram(g4file, hist_type='elec', skip_rows=sum(x[:7]) + 4 * 8,
                                                        read_rows=x[7])
        plato_spectrum_all_edep = load_geant4_histogram(g4file, hist_type='edep', skip_rows=sum(x[:6]) + 4 * 7,
                                                        read_rows=x[6])

        g4file = Path(__file__).parent.joinpath('data', 'diff_thick_new',
                                                'stepsize_proton_55MeV_15um_Silicon_10000_MicroElec.ascii')
        # geant4_step_size = load_geant4_histogram(g4file, hist_type='step_size', skip_rows=4, read_rows=x[0])
        geant4_all_elec = load_geant4_histogram(g4file, hist_type='elec', skip_rows=sum(x[:7]) + 4 * 8, read_rows=x[7])
        geant4_all_edep = load_geant4_histogram(g4file, hist_type='edep', skip_rows=sum(x[:6]) + 4 * 7, read_rows=x[6])

        plato_data_array = np.loadtxt(str(
            Path(__file__).parent.joinpath('data', 'validation', 'CosmicsStatsplato-cold-irrad-protons.txt')))

        # x = [10000, 1000, 1000, 2000, 3000, 1000, 10000, 4000]
        # g4file = Path(path, 'PLATO_irrad_proton_spectrum_15um_Silicon_10000_MicroElec.ascii')
        # spectrum_p_uelec_all_elec = load_geant4_histogram(g4file, hist_type='all_elec', skip_rows=sum(x[:7]) + 4 * 8,
        #                                                   read_rows=x[7])
        # x = [10000, 1000, 1000, 2000, 3000, 1000, 1000, 4000]
        # g4file = Path(path, 'PLATO_irrad_e-_spectrum_15um_Silicon_10000_MicroElec.ascii')
        # spectrum_e_uelec_all_elec = load_geant4_histogram(g4file, hist_type='all_elec', skip_rows=sum(x[:7]) + 4 * 8,
        #                                                   read_rows=x[7])

        import matplotlib
        font = {'size': 14}
        matplotlib.rc('font', **font)

        fig = plt.figure(figsize=(8, 6))
        hrange = (0, 100)  # keV
        title = 'Total energy deposited per event'
        density = True

        geant4_all_edep = load_data_into_histogram(geant4_all_edep.values, plato=False, lim=hrange, regrp=20)
        plato_spectrum_all_edep = load_data_into_histogram(plato_spectrum_all_edep.values, plato=False, lim=hrange,
                                                           regrp=20)

        hbins_edep = plato_spectrum_all_edep[:, 0] * 1000  # same as geant4_all_edep[:, 0] * 1000

        plt.hist(geant4_all_edep[:, 0] * 1000, bins=hbins_edep, weights=geant4_all_edep[:, 1],
                 density=density, histtype='step', label=r'G4, p$^{+}$, $55\,MeV, 15\,\mu m$', alpha=1.)
        plt.hist(plato_spectrum_all_edep[:, 0] * 1000, bins=hbins_edep, weights=plato_spectrum_all_edep[:, 1],
                 density=density, histtype='step', label=r'G4, p$^{+}$, spectrum, $15\,\mu m$', alpha=1.)
        plt.hist(cosmix_edep, bins=hbins_edep, range=hrange,
                 density=density, histtype='step', label=r'model, p$^{+}$, $55\,MeV, l_{ch}=2\,\mu m$')

        plt.title(title)
        plt.xlabel('energy (keV)')
        if density:
            plt.ylabel('normalized counts')
        else:
            plt.ylabel('counts')
        plt.legend()
        fig.tight_layout()
        self.save_and_draw('plato-data-validation-energy')

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        fig = plt.figure(figsize=(8, 6))
        hrange = (0, 20000)
        title = 'Number of electrons per event'
        density = True

        geant4_all_elec = load_data_into_histogram(geant4_all_elec.values, plato=False, lim=hrange, regrp=10)
        plato_spectrum_all_elec = load_data_into_histogram(plato_spectrum_all_elec.values, plato=False, lim=hrange,
                                                           regrp=10)
        plato_data = load_data_into_histogram(plato_data_array, plato=True, lim=hrange)

        plt.hist(plato_data[:, 0], bins=plato_data[:, 0], weights=plato_data[:, 1], histtype='stepfilled',
                 density=density, linewidth=2, color='blue', label='PLATO irrad. data', alpha=0.2)

        hbins_elec = plato_spectrum_all_elec[:, 0]   # same as geant4_all_elec[:, 0]

        plt.hist(geant4_all_elec[:, 0], bins=hbins_elec, weights=geant4_all_elec[:, 1],
                 density=density, histtype='step', label=r'G4, p$^{+}$, $55\,MeV, 15\,\mu m$', alpha=1.)
        plt.hist(plato_spectrum_all_elec[:, 0], bins=hbins_elec, weights=plato_spectrum_all_elec[:, 1],
                 density=density, histtype='step', label=r'G4, p$^{+}$, spectrum, $15\,\mu m$', alpha=1.)
        plt.hist(cosmix_elec, bins=hbins_elec, range=hrange,
                 density=density, histtype='step', label=r'model, p$^{+}$, $55\,MeV, l_{ch}=2\mu m$')

        # proton_factor = 9.942500e+00
        # electron_factor = 6.162000e-01
        # #
        # all_hist_21 = load_data_into_histogram(spectrum_p_uelec_all_elec.values, plato=False, regrp=20, lim=hrange)
        # # plt.hist(all_hist_21[:, 0], bins=all_hist_21[:, 0], weights=all_hist_21[:, 1], histtype='step',
        # #          density=True, label='G4 MicroElec, spectrum, proton', alpha=1)
        # # plt.hist(all_hist_21[:, 0], bins=all_hist_21[:, 0], weights=all_hist_21[:, 1], histtype='step',
        # #          density=True, label='G4 MicroElec, spectrum, only protons', alpha=1)
        # all_hist_22 = load_data_into_histogram(spectrum_e_uelec_all_elec.values, plato=False, regrp=20, lim=hrange)
        # # plt.hist(all_hist_22[:, 0], bins=all_hist_22[:, 0], weights=all_hist_22[:, 1], histtype='step',
        # #          density=True, label='G4 MicroElec, spectrum, electron', alpha=1)
        # all_hist_23 = all_hist_21
        # all_hist_23[:, 1] = all_hist_21[:, 1] * proton_factor + all_hist_22[:, 1] * electron_factor
        # plt.hist(all_hist_23[:, 0], bins=all_hist_23[:, 0], weights=all_hist_23[:, 1], histtype='step',
        #          density=density, label=r'G4, p$^{+}$ + e$^{-}$, spectrum, $15\,\mu m$', alpha=1)

        plt.title(title)
        plt.xlabel('electrons (e-)')
        if density:
            plt.ylabel('normalized counts')
        else:
            plt.ylabel('counts')
        plt.legend()
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 1))
        fig.tight_layout()
        self.save_and_draw('plato-data-validation-electrons')
