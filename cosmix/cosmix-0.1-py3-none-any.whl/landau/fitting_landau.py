from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from landau import landau
from util import load_data_into_histogram, load_geant4_histogram  # , sampling_distribution, read_data


def fitting_landau():
    """Main function."""

    # fit_landau_to_edep()
    # plot_fitted_params()

    landau.plot_landau()
    landau.simple_fit()
    landau.plot_landau_with_fwhm()
    landau.landau_gauss_crosscheck()
    landau.integrate_landau()

    plt.show()


def plot_fitted_params():
    """TBW."""
    path = Path(__file__).parent.joinpath('data', 'stepsize', 'stepsize_2um')
    # df = pd.read_csv(Path(path, 'fitting_df.csv'))
    df = pd.read_csv(Path(path, 'fitting_df_test.csv'))

    plt.figure()
    plt.title(r'Landau*Gauss most probable value')
    plt.loglog(df.energy.values, df.mpv.values, '.-', label='mpv')
    plt.xlabel('E (MeV)')
    plt.legend()

    plt.figure()
    plt.title(r'Landau*Gauss $\eta$ and $\sigma$ parameters')
    plt.loglog(df.energy.values, df.eta.values, '.-', label=r'$\eta$')
    plt.loglog(df.energy.values, df.sigma.values, '.', label=r'$\sigma$')
    plt.loglog(df.energy.values, df.sigma.values * df.scale.values, '.', label=r'$\sigma * scale$')
    plt.ylim([1e-3, 1e+1])
    plt.xlabel('E (MeV)')
    plt.legend()

    plt.figure()
    plt.title(r'Landau*Gauss amplitude')
    plt.loglog(df.energy.values, df.amp.values, '.-', label='amp')
    plt.xlabel('E (MeV)')
    plt.legend()

    plt.show()


def fit_landau_to_edep():
    """TBW."""
    x = [10000, 1000, 1000, 2000, 3000, 1000, 10000, 4000]
    path = Path(__file__).parent.joinpath('data', 'stepsize', 'stepsize_2um')
    g4file_dict = {
        # # energy in MeV, filename
        # '5': Path(path, 'stepsize_proton_5MeV_2um_Silicon_10000_MicroElec.ascii'),
        # '7': Path(path, 'stepsize_proton_7MeV_2um_Silicon_10000_MicroElec.ascii'),
        # '10': Path(path, 'stepsize_proton_10MeV_2um_Silicon_10000_MicroElec.ascii'),
        # '20': Path(path, 'stepsize_proton_20MeV_2um_Silicon_10000_MicroElec.ascii'),
        '30': Path(path, 'stepsize_proton_30MeV_2um_Silicon_10000_MicroElec.ascii'),
        '55': Path(path, 'stepsize_proton_55MeV_2um_Silicon_10000_MicroElec.ascii'),  # ######
        '100': Path(path, 'stepsize_proton_100MeV_2um_Silicon_10000_MicroElec.ascii'),
        '200': Path(path, 'stepsize_proton_200MeV_2um_Silicon_10000_MicroElec.ascii'),
        '300': Path(path, 'stepsize_proton_300MeV_2um_Silicon_10000_MicroElec.ascii'),
        '500': Path(path, 'stepsize_proton_500MeV_2um_Silicon_10000_MicroElec.ascii'),
        '600': Path(path, 'stepsize_proton_600MeV_2um_Silicon_10000_MicroElec.ascii'),
        '700': Path(path, 'stepsize_proton_700MeV_2um_Silicon_10000_MicroElec.ascii'),
        # '800': Path(path, 'stepsize_proton_800MeV_2um_Silicon_10000_MicroElec.ascii'),
        '900': Path(path, 'stepsize_proton_900MeV_2um_Silicon_10000_MicroElec.ascii'),
        '1000': Path(path, 'stepsize_proton_1000MeV_2um_Silicon_10000_MicroElec.ascii'),
        '2000': Path(path, 'stepsize_proton_2000MeV_2um_Silicon_10000_MicroElec.ascii'),
        '3000': Path(path, 'stepsize_proton_3000MeV_2um_Silicon_10000_MicroElec.ascii'),
        '4000': Path(path, 'stepsize_proton_4000MeV_2um_Silicon_10000_MicroElec.ascii'),
        '5000': Path(path, 'stepsize_proton_5000MeV_2um_Silicon_10000_MicroElec.ascii'),
        '6000': Path(path, 'stepsize_proton_6000MeV_2um_Silicon_10000_MicroElec.ascii'),
        '7000': Path(path, 'stepsize_proton_7000MeV_2um_Silicon_10000_MicroElec.ascii'),
        # '8000': Path(path, 'stepsize_proton_8000MeV_2um_Silicon_10000_MicroElec.ascii'),
        '9000': Path(path, 'stepsize_proton_9000MeV_2um_Silicon_10000_MicroElec.ascii'),
        '9990': Path(path, 'stepsize_proton_9990MeV_2um_Silicon_10000_MicroElec.ascii'),
        # # # # 10000 MeV data is not good, models used are not valid any more...
    }

    df = pd.DataFrame(columns=['energy', 'thickness', 'mpv', 'eta', 'sigma', 'amp', 'scale'])

    grp_val = None       # 2 or None
    thickness = 2           # um

    plt.figure()
    plt.title(r'Landau*Gauss dist. fitted to G4 E$_{dep}(E, l=2\mu m)$ data')
    scale = 1.
    for energy, g4file in g4file_dict.items():

        if float(energy) < 100.:
            grp_val = 2

        g4data = load_geant4_histogram(g4file, hist_type='edep', skip_rows=sum(x[:6]) + 4 * 7, read_rows=x[6])
        g4data = load_data_into_histogram(g4data.values, plato=False, regrp=grp_val)

        mpv, eta, sigma, amp, scale = landau.simple_fit_to_data(g4data, energy, scale)
        if grp_val is not None:
            amp /= grp_val
        mpv /= scale
        eta /= scale
        sigma /= scale
        print('energy: %1.1e    mpv: %1.3f   eta: %1.3e   sigma: %1.3e   amp: %1.3f   scale: %1.1f' %
              (float(energy), mpv, eta, sigma, amp, scale))

        df_dict = {
            'energy': energy,
            'thickness': thickness,
            'mpv': mpv,
            'eta': eta,
            'sigma': sigma,
            'amp': amp,
            'scale': scale
        }
        df_new = pd.DataFrame(df_dict, index=[0])
        df = pd.concat([df, df_new], ignore_index=True)
        pass

    plt.xlim([-10, 60])
    plt.xlabel('edep')
    plt.legend()

    df.to_csv(Path(path, 'fitting_df_test.csv'), index=False, line_terminator='\n')


def normalize(data):
    return np.stack((data[:, 0], data[:, 1]/np.sum(data[:, 1])), axis=1)


if __name__ == '__main__':
    fitting_landau()
