from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from util import load_data_into_histogram, load_geant4_histogram  # , sampling_distribution, read_data


def analysis():
    """Main function."""

    # mct_materials()

    plot_plato_hists()
    # plot_geant4_hists()
    compare_different_thicknesses()
    compare_different_energies()

    # plot_3d_tracks()
    plt.show()


def plot_geant4_hists(g4file, label):
    """TBW."""
    x = [10000, 1000, 1000, 2000, 3000, 1000, 10000, 4000]

    plt.figure()
    h0 = load_geant4_histogram(g4file, hist_type='step_size', skip_rows=4, read_rows=x[0])
    h0 = load_data_into_histogram(h0.values, plato=False)
    plt.title('step size'+label)
    plt.hist(h0[:, 0], bins=h0[:, 0], weights=h0[:, 1], histtype='stepfilled', density=True)

    # plt.figure()
    # h1 = load_geant4_histogram(g4file, hist_type='edep_prim', skip_rows=sum(x[:1]) + 4 * 2, read_rows=x[1])
    # h1 = load_data_into_histogram(h1.values, plato=False)
    # plt.title('E dep by prim'+label)
    # plt.hist(h1[:, 0], bins=h1[:, 0], weights=h1[:, 1], histtype='stepfilled', density=True)
    #
    # plt.figure()
    # h2 = load_geant4_histogram(g4file, hist_type='edep_sec_ter', skip_rows=sum(x[:5]) + 4 * 6, read_rows=x[5])
    # h2 = load_data_into_histogram(h2.values, plato=False)
    # plt.title('E dep by sec&ter'+label)
    # plt.hist(h2[:, 0], bins=h2[:, 0], weights=h2[:, 1], histtype='stepfilled', density=True)

    plt.figure()
    h3 = load_geant4_histogram(g4file, hist_type='edep_all', skip_rows=sum(x[:6]) + 4 * 7, read_rows=x[6])
    h3 = load_data_into_histogram(h3.values, plato=False)
    plt.title('E dep all'+label)
    plt.hist(h3[:, 0], bins=h3[:, 0], weights=h3[:, 1], histtype='stepfilled', density=True)

    plt.figure()
    h4 = load_geant4_histogram(g4file, hist_type='all_elec', skip_rows=sum(x[:7]) + 4 * 8, read_rows=x[7])
    h4 = load_data_into_histogram(h4.values, plato=False)
    plt.title('all e-'+label)
    plt.hist(h4[:, 0], bins=h4[:, 0], weights=h4[:, 1], histtype='stepfilled', density=True)

    plt.figure()
    h5 = load_geant4_histogram(g4file, hist_type='electron', skip_rows=sum(x[:2]) + 4 * 3, read_rows=x[2])
    h5 = load_data_into_histogram(h5.values, plato=False, lim=(0, 500))
    plt.title('cluster sizes'+label)
    plt.hist(h5[:, 0], bins=h5[:, 0], weights=h5[:, 1], histtype='stepfilled', density=True, log=True)

    # plt.figure()
    # h6 = load_geant4_histogram(g4file, hist_type='sec', skip_rows=sum(x[:3]) + 4 * 4, read_rows=x[3])
    # h6 = load_data_into_histogram(h6.values, plato=False)
    # plt.title('sec e-'+label)
    # plt.hist(h6[:, 0], bins=h6[:, 0], weights=h6[:, 1], histtype='stepfilled', density=True)
    #
    # plt.figure()
    # h7 = load_geant4_histogram(g4file, hist_type='ter', skip_rows=sum(x[:4]) + 4 * 5, read_rows=x[4])
    # h7 = load_data_into_histogram(h7.values, plato=False)
    # plt.title('ter e-'+label)
    # plt.hist(h7[:, 0], bins=h7[:, 0], weights=h7[:, 1], histtype='stepfilled', density=True)


def compare_different_thicknesses():
    """TBW."""
    x = [10000, 1000, 1000, 2000, 3000, 1000, 10000, 4000]
    # path = Path(__file__).parent.joinpath('data', 'different_thicknesses')
    path = Path(__file__).parent.joinpath('data', 'diff_thick_new')
    g4file_dict = {
        # '10 nm': Path(path, 'stepsize_proton_55MeV_10nm_Silicon_10000_MicroElec.ascii'),
        # '30 nm': Path(path, 'stepsize_proton_55MeV_30nm_Silicon_10000_MicroElec.ascii'),
        # '50 nm': Path(path, 'stepsize_proton_55MeV_50nm_Silicon_10000_MicroElec.ascii'),
        # '100 nm': Path(path, 'stepsize_proton_55MeV_100nm_Silicon_10000_MicroElec.ascii'),
        # '200 nm': Path(path, 'stepsize_proton_55MeV_200nm_Silicon_10000_MicroElec.ascii'),
        '300 nm': Path(path, 'stepsize_proton_55MeV_300nm_Silicon_10000_MicroElec.ascii'),
        # '400 nm': Path(path, 'stepsize_proton_55MeV_400nm_Silicon_10000_MicroElec.ascii'),
        '600 nm': Path(path, 'stepsize_proton_55MeV_600nm_Silicon_10000_MicroElec.ascii'),
        # '800 nm': Path(path, 'stepsize_proton_55MeV_800nm_Silicon_10000_MicroElec.ascii'),
        '1 um': Path(path, 'stepsize_proton_55MeV_1um_Silicon_10000_MicroElec.ascii'),
        '2 um': Path(path, 'stepsize_proton_55MeV_2um_Silicon_10000_MicroElec.ascii'),
        '4 um': Path(path, 'stepsize_proton_55MeV_4um_Silicon_10000_MicroElec.ascii'),
        '10 um': Path(path, 'stepsize_proton_55MeV_10um_Silicon_10000_MicroElec.ascii'),
        '15 um': Path(path, 'stepsize_proton_55MeV_15um_Silicon_10000_MicroElec.ascii')
    }

    plt.figure()
    for lab, g4file in g4file_dict.items():

        geant4_all_edep = load_geant4_histogram(g4file, hist_type='all_edep',
                                                skip_rows=sum(x[:6]) + 4 * 7, read_rows=x[6])

        title = 'total energy deposited per event'
        geant4_all_edep = load_data_into_histogram(geant4_all_edep.values, plato=False, regrp=10)

        # hbins = geant4_all_edep.shape[0]
        plt.hist(geant4_all_edep[:, 0] * 1000, bins=geant4_all_edep[:, 0] * 1000, weights=geant4_all_edep[:, 1],
                 density=True, histtype='step', label='G4 ' + lab)
        # plt.hist(tars.edep_per_event, bins=hbins, range=hrange, histtype='step', label='edep_per_event', density=True)
        plt.title(title)
        plt.xlabel('energy (keV)')
        plt.ylabel('counts')
        plt.legend()

    plt.figure()
    for lab, g4file in g4file_dict.items():

        geant4_all_elec = load_geant4_histogram(g4file, hist_type='all_elec', skip_rows=sum(x[:7]) + 4 * 8,
                                                read_rows=x[7])
        hrange = (0, 20000)
        # hbins = 200
        title = 'electrons per event'
        geant4_all_elec = load_data_into_histogram(geant4_all_elec.values, plato=False, lim=hrange)

        # if sel in lab:
        #     geant4_all_elec[:, 0] *= factor
        #     lab = sel + ' * ' + str(factor)

        # hbins = geant4_all_elec.shape[0]
        plt.hist(geant4_all_elec[:, 0], bins=geant4_all_elec[:, 0], weights=geant4_all_elec[:, 1], density=True,
                 histtype='step', label='G4 ' + lab)
        plt.title(title)
        plt.xlabel('electrons')
        plt.ylabel('counts')
        plt.legend()

    plt.figure()
    for lab, g4file in g4file_dict.items():
        geant4_step_size = load_geant4_histogram(g4file, hist_type='step_size', skip_rows=4, read_rows=x[0])

        plt.title('Proton step size per step')
        plt.xlabel('step (um)')
        plt.ylabel('Counts')
        geant4_step_size = load_data_into_histogram(geant4_step_size.values, plato=False)
        hist_bins = np.linspace(-8, 1, 1000)
        # geant4_step_size[:, 0] is in mm not in um, therefore we need to add 3 order of magnitude to it !!!
        plt.hist(geant4_step_size[:, 0] + 3., bins=hist_bins, weights=geant4_step_size[:, 1],
                 histtype='step', density=True, label='G4 ' + lab)
        # plt.hist(np.log10(tars.step_size_lst_per_step), bins=hist_bins,
        #          histtype='step', density=True, label='cosmix')
        plt.legend()

    # plt.figure()
    # for lab, g4file in g4file_dict.items():
    #     geant4_cluster_size = load_geant4_histogram(g4file, hist_type='electron', skip_rows=sum(x[:2]) + 4 * 3,
    #                                                 read_rows=x[2])
    #
    #     plt.title('Electron cluster size per step')
    #     plt.xlabel('electron')
    #     plt.ylabel('Counts')
    #     hrange = (0, 500)
    #     geant4_cluster_size = load_data_into_histogram(geant4_cluster_size.values, plato=False, lim=hrange)
    #     plt.hist(geant4_cluster_size[:, 0], bins=geant4_cluster_size[:, 0], weights=geant4_cluster_size[:, 1],
    #              histtype='step', density=True, log=True, label='G4 ' + lab)
    #     # plt.hist(tars.electron_lst_per_step, log=True, density=True, bins=hrange[1],
    #     #          histtype='step', range=hrange, label='cosmix')
    #     plt.legend()


def compare_different_energies():
    """TBW."""
    import matplotlib
    font = {'size': 14}
    matplotlib.rc('font', **font)

    x = [10000, 1000, 1000, 2000, 3000, 1000, 10000, 4000]
    path = Path(__file__).parent.joinpath('data', 'result_plot')
    g4file_dict = {
        # '10 MeV': Path(path, 'stepsize_proton_10MeV_15um_Silicon_10000_MicroElec.ascii'),
        # '53 MeV': Path(path, 'stepsize_proton_53MeV_15um_Silicon_10000_MicroElec.ascii'),
        # '54 MeV': Path(path, 'stepsize_proton_54MeV_15um_Silicon_10000_MicroElec.ascii'),

        r'$55\,MeV$': Path(path, 'stepsize_proton_55MeV_15um_Silicon_10000_MicroElec.ascii'),
        r'$100\,MeV$': Path(path, 'stepsize_proton_100MeV_15um_Silicon_10000_MicroElec.ascii'),
        r'$1\,GeV$': Path(path, 'stepsize_proton_1000MeV_15um_Silicon_10000_MicroElec.ascii'),

        # r'$55\,MeV 2$': Path(path, 'stepsize_proton_55000keV_300nm_Silicon_10000_MicroElec.ascii'),
        # r'$100\,MeV 2$': Path(path, 'stepsize_proton_100MeV_300nm_Silicon_10000_MicroElec.ascii'),
        # r'$1\,GeV 2$': Path(path, 'stepsize_proton_1000MeV_300nm_Silicon_10000_MicroElec.ascii'),
    }

    result_path = Path(__file__).parent.joinpath('data', 'results', 'tars_1GeV_10k_2um')
    # tars_result_all_elec_1gev = np.load(Path(result_path, 'tars_electron_per_event.npy'))
    tars_result_all_edep_1gev = np.load(Path(result_path, 'tars_edep_per_event.npy'))
    tars_result_step_1gev = np.load(Path(result_path, 'tars_step_size_lst_per_step.npy'))

    result_path = Path(__file__).parent.joinpath('data', 'results', 'tars_100MeV_10k_2um')
    # tars_result_all_elec_100mev = np.load(Path(result_path, 'tars_electron_per_event.npy'))
    tars_result_all_edep_100mev = np.load(Path(result_path, 'tars_edep_per_event.npy'))
    tars_result_step_100mev = np.load(Path(result_path, 'tars_step_size_lst_per_step.npy'))

    result_path = Path(__file__).parent.joinpath('data', 'results', 'tars_55MeV_10k_2um')
    # tars_result_all_elec_55mev = np.load(Path(result_path, 'tars_electron_per_event.npy'))
    tars_result_all_edep_55mev = np.load(Path(result_path, 'tars_edep_per_event.npy'))
    tars_result_step_55mev = np.load(Path(result_path, 'tars_step_size_lst_per_step.npy'))

    title = r'Total energy deposited per event, $15\,\mu m$'

    fig = plt.figure(figsize=(8, 4))
    hbins = 120

    for lab, g4file in g4file_dict.items():

        geant4_all_edep = load_geant4_histogram(g4file, hist_type='all_edep',
                                                skip_rows=sum(x[:6]) + 4 * 7, read_rows=x[6])

        geant4_all_edep = load_data_into_histogram(geant4_all_edep.values, plato=False, regrp=40)

        plt.hist(geant4_all_edep[:, 0] * 1000, bins=geant4_all_edep[:, 0] * 1000, weights=geant4_all_edep[:, 1],
                 density=True, histtype='step', label='G4, ' + lab)

    plt.hist(tars_result_all_edep_55mev, bins=hbins, histtype='step',
             label=r'model, $55\,MeV$', density=True)    # l_{ch}=2\,\mu m$
    plt.hist(tars_result_all_edep_100mev, bins=hbins, histtype='step',
             label=r'model, $100\,MeV$', density=True)
    plt.hist(tars_result_all_edep_1gev, bins=hbins, histtype='step',
             label=r'model, $1\,GeV$', density=True)

    plt.xlim([0, 60])
    plt.title(title)
    plt.xlabel('energy (keV)')
    plt.ylabel('normalized counts')
    plt.legend()
    fig.tight_layout()
    fig.savefig('data/plots/cosmix-energy.png')

    fig = plt.figure(figsize=(8, 4))
    hist_bins = np.linspace(-6, 1, 160)
    for lab, g4file in g4file_dict.items():
        geant4_step_size = load_geant4_histogram(g4file, hist_type='step_size', skip_rows=4, read_rows=x[0])
        geant4_step_size = load_data_into_histogram(geant4_step_size.values, plato=False)  # , regrp=2)
        # geant4_step_size[:, 0] is in mm not in um, therefore we need to add 3 order of magnitude to it !!!
        plt.hist(geant4_step_size[:, 0] + 3., bins=hist_bins, weights=geant4_step_size[:, 1],
                 histtype='step', density=True, label='G4, ' + lab)

    plt.hist(np.log10(tars_result_step_55mev), bins=hist_bins, histtype='step', label=r'model, $55\,MeV$',
             density=True)  # l_{ch}=2\,\mu m$
    plt.hist(np.log10(tars_result_step_100mev), bins=hist_bins, histtype='step', label=r'model, $100\,MeV$',
             density=True)
    plt.hist(np.log10(tars_result_step_1gev), bins=hist_bins, histtype='step', label=r'model, $1\,GeV$',
             density=True)

    plt.title(r'Proton step size distribution, $15\,\mu m$')
    plt.xlabel(r'log$_{10}$(d$_{step}^i$)')
    plt.ylabel('normalized counts')
    plt.legend(loc='upper left')
    fig.tight_layout()
    fig.savefig('data/plots/cosmix-stepsize.png')

    # plt.figure()
    # for lab, g4file in g4file_dict.items():
    #
    #     geant4_all_elec = load_geant4_histogram(g4file, hist_type='all_elec', skip_rows=sum(x[:7]) + 4 * 8,
    #                                             read_rows=x[7])
    #     hrange = (0, 20000)
    #     # hbins = 200
    #     title = 'electrons per event'
    #     geant4_all_elec = load_data_into_histogram(geant4_all_elec.values, plato=False, lim=hrange, regrp=10)
    #
    #     # if sel in lab:
    #     #     geant4_all_elec[:, 0] *= factor
    #     #     lab = sel + ' * ' + str(factor)
    #
    #     # hbins = geant4_all_elec.shape[0]
    #     plt.hist(geant4_all_elec[:, 0], bins=geant4_all_elec[:, 0], weights=geant4_all_elec[:, 1], density=True,
    #              histtype='step', label='G4, ' + lab)
    #     plt.title(title)
    #     plt.xlabel('electrons')
    #     plt.ylabel('counts')
    #     plt.legend()


def plot_plato_hists():
    """TBW."""
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

    array = np.loadtxt(Path(__file__).parent.joinpath('data', 'validation', 'CosmicsStatsplato-cold-irrad-protons.txt'))

    # result_path = Path(__file__).parent.joinpath('data', 'results', 'tars_spectrum_10k')
    # tars_result_all_elec = np.load(Path(result_path, 'tars_electron_per_event.npy'))
    # tars_result_all_edep = np.load(Path(result_path, 'tars_edep_per_event.npy'))

    result_path = Path(__file__).parent.joinpath('data', 'results', 'tars_55MeV_10k_2um')
    tars_result_all_elec_2 = np.load(Path(result_path, 'tars_electron_per_event.npy'))
    tars_result_all_edep_2 = np.load(Path(result_path, 'tars_edep_per_event.npy'))

    x = [10000, 1000, 1000, 2000, 3000, 1000, 10000, 4000]
    g4file = Path(path, 'PLATO_irrad_proton_spectrum_15um_Silicon_10000_MicroElec.ascii')
    spectrum_p_uelec_all_elec = load_geant4_histogram(g4file, hist_type='all_elec', skip_rows=sum(x[:7]) + 4 * 8,
                                                      read_rows=x[7])
    x = [10000, 1000, 1000, 2000, 3000, 1000, 1000, 4000]
    g4file = Path(path, 'PLATO_irrad_e-_spectrum_15um_Silicon_10000_MicroElec.ascii')
    spectrum_e_uelec_all_elec = load_geant4_histogram(g4file, hist_type='all_elec', skip_rows=sum(x[:7]) + 4 * 8,
                                                      read_rows=x[7])

    import matplotlib
    font = {'size': 14}
    matplotlib.rc('font', **font)

    fig = plt.figure(figsize=(8, 6))
    hrange = (0, 100)  # keV
    title = 'Total energy deposited per event'
    geant4_all_edep = load_data_into_histogram(geant4_all_edep.values, plato=False, lim=hrange, regrp=20)
    plato_spectrum_all_edep = load_data_into_histogram(plato_spectrum_all_edep.values, plato=False, lim=hrange,
                                                       regrp=20)

    plt.hist(geant4_all_edep[:, 0] * 1000, bins=geant4_all_edep[:, 0] * 1000, weights=geant4_all_edep[:, 1],
             density=True, histtype='step', label=r'G4, p$^{+}$, $55\,MeV, 15\,\mu m$', alpha=1.)
    plt.hist(plato_spectrum_all_edep[:, 0] * 1000, bins=plato_spectrum_all_edep[:, 0] * 1000,
             weights=plato_spectrum_all_edep[:, 1], density=True, histtype='step',
             label=r'G4, p$^{+}$, spectrum, $15\,\mu m$', alpha=1.)

    hbins = 100

    plt.hist(tars_result_all_edep_2, bins=hbins, range=hrange, histtype='step',
             label=r'model, p$^{+}$, $55\,MeV, l_{ch}=2\,\mu m$', density=True)

    plt.title(title)
    plt.xlabel('energy (keV)')
    plt.ylabel('normalized counts')
    plt.legend()
    fig.tight_layout()
    fig.savefig('data/plots/plato-validation-energy.png')
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    fig = plt.figure(figsize=(8, 6))
    hrange = (0, 20000)
    title = 'Number of electrons per event'
    density = True

    geant4_all_elec = load_data_into_histogram(geant4_all_elec.values, plato=False, lim=hrange, regrp=10)
    plato_spectrum_all_elec = load_data_into_histogram(plato_spectrum_all_elec.values, plato=False, lim=hrange,
                                                       regrp=10)
    plato_data = load_data_into_histogram(array, plato=True, lim=hrange)

    plt.hist(plato_data[:, 0], bins=plato_data[:, 0], weights=plato_data[:, 1], histtype='stepfilled', density=density,
             linewidth=2, color='blue', label='PLATO irrad. data', alpha=0.2)

    plt.hist(geant4_all_elec[:, 0], bins=geant4_all_elec[:, 0], weights=geant4_all_elec[:, 1], density=density,
             histtype='step', label=r'G4, p$^{+}$, $55\,MeV, 15\,\mu m$', alpha=1.)
    plt.hist(plato_spectrum_all_elec[:, 0], bins=plato_spectrum_all_elec[:, 0], weights=plato_spectrum_all_elec[:, 1],
             density=density, histtype='step', label=r'G4, p$^{+}$, spectrum, $15\,\mu m$', alpha=1.)

    proton_factor = 9.942500e+00
    electron_factor = 6.162000e-01
    #
    all_hist_21 = load_data_into_histogram(spectrum_p_uelec_all_elec.values, plato=False, regrp=20, lim=hrange)
    # plt.hist(all_hist_21[:, 0], bins=all_hist_21[:, 0], weights=all_hist_21[:, 1], histtype='step', density=True,
    #          label='G4 MicroElec, spectrum, proton', alpha=1)
    # plt.hist(all_hist_21[:, 0], bins=all_hist_21[:, 0], weights=all_hist_21[:, 1], histtype='step', density=True,
    #          label='G4 MicroElec, spectrum, only protons', alpha=1)
    all_hist_22 = load_data_into_histogram(spectrum_e_uelec_all_elec.values, plato=False, regrp=20, lim=hrange)
    # plt.hist(all_hist_22[:, 0], bins=all_hist_22[:, 0], weights=all_hist_22[:, 1], histtype='step', density=True,
    #          label='G4 MicroElec, spectrum, electron', alpha=1)
    all_hist_23 = all_hist_21
    all_hist_23[:, 1] = all_hist_21[:, 1] * proton_factor + all_hist_22[:, 1] * electron_factor
    plt.hist(all_hist_23[:, 0], bins=all_hist_23[:, 0], weights=all_hist_23[:, 1], histtype='step', density=density,
             label=r'G4, p$^{+}$ + e$^{-}$, spectrum, $15\,\mu m$', alpha=1)

    hbins = 100

    plt.hist(tars_result_all_elec_2, bins=hbins, range=hrange, histtype='step',
             label=r'model, p$^{+}$, $55\,MeV, l_{ch}=2\mu m$', density=True)

    plt.title(title)
    plt.xlabel('electrons (e-)')
    plt.ylabel('normalized counts')
    plt.legend()
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 1))
    fig.tight_layout()
    fig.savefig('data/plots/plato-data-validation-electrons.png')

    # g4stepmean = np.average(geant4_step_size_53[:, 0] + 3., weights=geant4_step_size_53[:, 1])
    # cosmixstepmean = np.log10(tars_result_step_size_53).mean()
    # print('G4 53MeV stepsize dist.:')
    # print('  mean:     ', g4stepmean)
    # print('cosmix 53MeV stepsize dist.:')
    # print('  mean:     ', cosmixstepmean)
    # print('  st.dev:   ', np.log10(tars_result_step_size_53).std())
    # print('difference: ', g4stepmean - cosmixstepmean)
    # print('ratio 1:    ', g4stepmean / cosmixstepmean)
    # print('ratio 2:    ', cosmixstepmean / g4stepmean)
    # print('-----')

    # detector.charge.frame.hist(column='position_ver', bins=200)
    # detector.charge.frame.hist(column='position_hor', bins=200)
    # detector.charge.frame.hist(column='position_z', bins=200)
    # detector.charge.frame.hist(column='number', bins=400)

    # plt.figure()
    # plt.title('Proton spectrum by cosmix')
    # plt.xlabel('Energy (MeV)')
    # plt.ylabel('Counts')
    # hist_bins = np.logspace(np.log10(0.1), np.log10(100), 250)
    # plt.hist(tars.p_init_energy_lst_per_event, bins=hist_bins, label='init')
    # # plt.hist(tars.p_final_energy_lst_per_event, bins=hist_bins, label='final')
    # # plt.gca().set_xscale("log")
    # plt.legend()


def plot_3d_tracks():
    """TBW."""
    from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

    # np.save('outputs/cosmix_direction_lst_per_event', tars.direction_lst_per_event)
    # np.save('outputs/cosmix_trajectory_lst_per_event', tars.trajectory_lst_per_event)

    plt.figure()
    plt.title('Angle distribution')
    polar_angle_dist('outputs/cosmix_angle_alpha_lst_per_event.npy', label=r'$\alpha$')
    polar_angle_dist('outputs/cosmix_angle_beta_lst_per_event.npy', label=r'$\beta$')

    charge_num = np.load('outputs/cosmix_charge_num.npy')
    charge_v_pos = np.load('outputs/cosmix_charge_v_pos.npy')
    charge_h_pos = np.load('outputs/cosmix_charge_h_pos.npy')
    charge_z_pos = np.load('outputs/cosmix_charge_z_pos.npy')

    direction_per_event = np.load('outputs/cosmix_direction_lst_per_event.npy')
    starting_pos_per_event = np.load('outputs/cosmix_starting_pos_lst_per_event.npy')
    first_pos_per_event = np.load('outputs/cosmix_first_pos_lst_per_event.npy')
    last_pos_per_event = np.load('outputs/cosmix_last_pos_lst_per_event.npy')

    # plot_det_geo_3d(geo=detector.geometry)
    plot_tracks_3d(first_pos=first_pos_per_event, last_pos=last_pos_per_event,
                   start_pos=starting_pos_per_event, dir=direction_per_event)
    plot_charges_3d(x=charge_v_pos,
                    y=charge_h_pos,
                    z=charge_z_pos,
                    size=charge_num)


def polar_angle_dist(theta, label=None):
    """TBW."""
    if isinstance(theta, str):
        if theta.endswith('.npy'):
            theta = np.load(theta)
    fig = plt.gcf()
    fig.add_subplot(111, polar=True)
    plt.hist(theta, bins=360, histtype='step', label=label)
    if label:
        plt.legend()


def plot_det_geo_3d(geo):
    """TBW."""
    # fig = plt.figure(figsize=plt.figaspect(0.5))
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    point1 = np.array([0, 0, 0])
    point2 = np.array([0, 0, -1 * geo.total_thickness])
    normal = np.array([0, 0, 1])
    d1 = -point1.dot(normal)
    d2 = -point2.dot(normal)
    xx, yy = np.meshgrid(np.linspace(0, geo.vert_dimension, 10), np.linspace(0, geo.horz_dimension, 10))
    z1 = (-normal[0] * xx - normal[1] * yy - d1) * 1. / normal[2]
    z2 = (-normal[0] * xx - normal[1] * yy - d2) * 1. / normal[2]
    ax.plot_surface(xx, yy, z1, alpha=0.2, color=(0, 0, 1))
    ax.plot_surface(xx, yy, z2, alpha=0.2, color=(0, 0, 1))
    ax.set_xlim(0, geo.vert_dimension)
    ax.set_ylim(0, geo.horz_dimension)
    ax.set_zlim(-1 * geo.total_thickness - 5, 5)
    ax.set_xlabel(r'vertical ($\mu$m)')
    ax.set_ylabel(r'horizontal ($\mu$m)')
    ax.set_zlabel(r'z ($\mu$m)')


def plot_tracks_3d(first_pos, last_pos, start_pos, dir):
    """TBW."""
    ax = plt.gca()

    # ax.scatter(start_pos[:, 0], start_pos[:, 1], start_pos[:, 2], marker='*')
    # ax.scatter(first_pos[:, 0], first_pos[:, 1], first_pos[:, 2], marker='x')
    # ax.scatter(last_pos[:, 0], last_pos[:, 1], last_pos[:, 2], marker='o')

    # for i in range(len(first_pos)):
    #     ax.plot([start_pos[i, 0], first_pos[i, 0], last_pos[i, 0]],
    #             [start_pos[i, 1], first_pos[i, 1], last_pos[i, 1]],
    #             [start_pos[i, 2], first_pos[i, 2], last_pos[i, 2]],
    #             'x-', c='r')

    for i in range(len(first_pos)):
        ax.plot([first_pos[i, 0], last_pos[i, 0]],
                [first_pos[i, 1], last_pos[i, 1]],
                [first_pos[i, 2], last_pos[i, 2]],
                'x-', c='r')


def plot_charges_3d(x, y, z, size):
    """TBW."""
    # dx, dy, dz, dr = [], [], [], []

    ax = plt.gca()
    for i in range(len(size)):
        cluster_sizes = [k / 10. for k in size[i]]
        ax.scatter(x[i], y[i], z[i], c='b', marker='.', s=cluster_sizes)

    #     for j in range(len(x[i])-1):
    #         dx += [abs(x[i][j+1]-x[i][j])]
    #         dy += [abs(y[i][j+1]-y[i][j])]
    #         dz += [abs(z[i][j+1]-z[i][j])]
    #         dr += [np.sqrt((x[i][j+1]-x[i][j])**2 + (y[i][j+1]-y[i][j])**2 + (z[i][j+1]-z[i][j])**2)]
    #
    # plt.figure()
    # hbins = 200
    # plt.hist(dx, bins=hbins, histtype='step', label='x')
    # plt.hist(dy, bins=hbins, histtype='step', label='y')
    # plt.hist(dz, bins=hbins, histtype='step', label='z')
    # plt.hist(dr, bins=hbins, histtype='step', label='r')
    # plt.legend()
    pass


if __name__ == '__main__':
    analysis()
