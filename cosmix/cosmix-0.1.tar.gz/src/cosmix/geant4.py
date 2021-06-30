"""Run a geant4 application."""
import numpy as np
import subprocess
import time
from operator import add
import pandas as pd


# def geant4_new():
#     """Generate distributions via runnnig the geant4 app directly.
#
#     :return:
#     """
#     start_time = time.time()
#
#     step_df = pd.DataFrame(columns=['edep', 'step_size', 'hist'])
#     elec_df = pd.DataFrame(columns=['edep', 'cluster_size', 'hist'])
#     # edep_df = pd.DataFrame(columns=['edep', 'edep_step', 'hist'])
#
#     material = 'Silicon'
#     particle_type = 'proton'            # 'e-' , 'alpha'
#     track_length = '1 um'             # 300 nm
#     particle_number = '1'
#     physics_list = 'MicroElec'
#     # physics_list = 'EMopt4'
#
#     events = 10
#
#     energy_list = ['100 MeV']
#
#     for particle_energy in energy_list:
#
#         for _ in range(events):
#
#             # print('particle_energy: %s' % particle_energy)
#             print('/home/dlucsanyi/LET-Geant4/build/cosmics',
#                   material,
#                   particle_type,
#                   particle_energy,
#                   track_length,
#                   particle_number,
#                   physics_list)
#
#             subprocess.call([
#                 '/home/dlucsanyi/LET-Geant4/build/cosmics',
#                 material,
#                 particle_type,
#                 particle_energy,
#                 track_length,
#                 particle_number,
#                 physics_list
#             ], stdout=subprocess.DEVNULL)
#
#             data_energy_length = np.loadtxt('edep.data', delimiter='\t', usecols=[0, 1], dtype=np.str)
#             data_edep = np.loadtxt('edep.data', delimiter='\t', usecols=[2, 3, 4])
#
#             try:
#                 last_primary_energy = data_energy_length[-1, 0]
#                 last_track_length = data_energy_length[-1, 1]
#                 last_total_edep = data_edep[-1, 0] * 1.e3          # in keV
#                 # last_prim_edep = data_edep[-1, 1] * 1.e3
#                 # last_sec_edep = data_edep[-1, 2] * 1.e3
#             except IndexError:
#                 last_primary_energy = data_energy_length[0]
#                 last_track_length = data_energy_length[1]
#                 last_total_edep = data_edep[0] * 1.e3  # in keV
#                 # last_prim_edep = data_edep[1] * 1.e3
#                 # last_sec_edep = data_edep[2] * 1.e3
#
#             filename = 'stepsize_' + particle_type + '_' + last_primary_energy + '_' \
#                        + last_track_length + '_' + material + '_' + particle_number + '_' + physics_list + '.ascii'
#
#             x = [10000, 1000, 1000, 2000, 3000, 1000, 10000, 4000]
#             # # step size distribution in um
#             step_size_hist = load_geant4_histogram(filename, hist_type='step_size', skip_rows=4, read_rows=x[0])
#
#             # # tertiary electron numbers created by secondary electrons
#             elec_number_hist = load_geant4_histogram(filename, hist_type='electron', skip_rows=sum(x[:2]) + 4 * 3,
#                                                      read_rows=x[2])
#             # # # energy deposited per step TODO
#             # edep_per_step_hist = load_geant4_histogram(filename, hist_type='edep_step',
#             #                      TODO                                 skip_rows=sum(x[:6]) + 4 * 7, read_rows=x[6])
#
#             size = len(step_size_hist.values[:, 1])
#             step_dict = {'edep': [last_total_edep] * size,
#                          'step_size': step_size_hist.values[:, 0],
#                          'hist': step_size_hist.values[:, 1]}
#
#             size2 = len(elec_number_hist.values[:, 1])
#             elec_dict = {'edep': [last_total_edep] * size2,
#                          'cluster_size': elec_number_hist.values[:, 0],
#                          'hist': elec_number_hist.values[:, 1]}
#
#             # size3 = len(edep_per_step_hist.values[:, 1])
#             # edep_dict = {'edep': [last_total_edep] * size3,
#             #              'edep_step': edep_per_step_hist[:, 0],
#             #              'hist': edep_per_step_hist[:, 1]}
#
#             step_new_df = pd.DataFrame(step_dict)
#             elec_new_df = pd.DataFrame(elec_dict)
#             # edep_new_df = pd.DataFrame(edep_dict)
#
#             step_df = pd.concat([step_df, step_new_df], ignore_index=True)
#             elec_df = pd.concat([elec_df, elec_new_df], ignore_index=True)
#             # edep_df = pd.concat([edep_df, edep_new_df], ignore_index=True)
#
#             step_df.to_csv('data/geant4/' + 'step_df.csv', index=False, line_terminator='\n')
#             elec_df.to_csv('data/geant4/' + 'elec_df.csv', index=False, line_terminator='\n')
#             # edep_df.to_csv('data/geant4/' + 'edep_df.csv', index=False, line_terminator='\n')
#
#     print('\n\nRunning time: %.3f min' % ((time.time() - start_time)/60.))


def geant4():
    """Generate distributions via runnnig the geant4 app directly.

    :return:
    """
    start_time = time.time()

    material = 'Silicon'
    particle_type = 'proton'            # 'e-' , 'alpha'
    track_length = '300 nm'             # 300 nm
    particle_number = '10000'
    physics_list = 'MicroElec'
    # physics_list = 'EMopt4'

    # elowlim = 100       # keV
    # ehighlim = 9999     # keV
    # energy_list_kev = np.unique(np.logspace(start=np.log10(elowlim), stop=np.log10(ehighlim), num=100, dtype=int))
    # energy_list_kev = list(map(str, energy_list_kev))
    # energy_list_kev = list(map(add, energy_list_kev, len(energy_list_kev)*[' keV']))
    #
    # elowlim = 10        # MeV
    # ehighlim = 65       # MeV
    # energy_list_mev = np.unique(np.logspace(start=np.log10(elowlim), stop=np.log10(ehighlim), num=100, dtype=int))
    # energy_list_mev = list(map(str, energy_list_mev))
    # energy_list_mev = list(map(add, energy_list_mev, len(energy_list_mev)*[' MeV']))

    # energy_list = np.append(energy_list_kev, energy_list_mev)

    elowlim = 52000    # keV
    ehighlim = 56000     # keV
    step = 10        # keV
    energy_list_kev = list(range(elowlim, ehighlim, step))
    energy_list_kev = list(map(str, energy_list_kev))
    energy_list_kev = list(map(add, energy_list_kev, len(energy_list_kev) * [' keV']))
    energy_list = energy_list_kev

    for particle_energy in energy_list:

        print('particle_energy: %s' % particle_energy)
        print('/home/dlucsanyi/LET-Geant4/build/cosmics',
              material,
              particle_type,
              particle_energy,
              track_length,
              particle_number,
              physics_list)

        subprocess.call([
            '/home/lucsi/LET-Geant4/build_new/cosmics',
            material,
            particle_type,
            particle_energy,
            track_length,
            particle_number,
            physics_list
        ], stdout=subprocess.DEVNULL)

    print('\n\nRunning time: %.3f min' % ((time.time() - start_time)/60.))


def read_pd_csv(file='data/geant4/elec_df_copy.csv', column='cluster_size', rebin=None):
    """TBW."""
    df = pd.read_csv(file)

    df_nonzero = df[df.histo.values != 0.]
    unics = np.unique(df_nonzero[column].values)
    minimum = min(unics)
    maximum = max(unics)
    length = len(unics)

    if rebin is not None:
        unics = np.linspace(minimum, maximum, num=rebin)

    new_hist = None
    for i in range(len(unics)-1):
        # value = np.sum(df_nonzero[df_nonzero[column].values == key].histo.values)

        value = np.sum(df_nonzero[(df_nonzero[column].values >= unics[i]) &
                                  (df_nonzero[column].values < unics[i+1])].histo.values)
        v = np.stack((unics[i], value))
        # v = np.stack((np.mean((unics[i], unics[i+1])), value))
        if new_hist is None:
            new_hist = v
        else:
            new_hist = np.vstack((new_hist, v))

    import matplotlib.pyplot as plt
    plt.figure()
    plt.hist(new_hist[:, 0], bins=new_hist[:, 0], weights=new_hist[:, 1],
             density=False, histtype='step', label='')
    plt.show()


def read_pd_csv_edep(file='data/geant4/elec_df_copy.csv', column='cluster_size'):
    """TBW."""
    df = pd.read_csv(file)

    df_nonzero = df[df.histo.values != 0.]
    eee = np.unique(df_nonzero['edep'].values)
    edep_minimum = min(eee)
    edep_maximum = max(eee)
    print('edep_minimum: ', edep_minimum)
    print('edep_maximum: ', edep_maximum)

    lowlim = 0.4  # keV
    highlim = 0.8   # keV

    selected_edep = df_nonzero[(df_nonzero['edep'].values >= lowlim) & (df_nonzero['edep'].values < highlim)]

    unics = np.unique(selected_edep[column].values)

    bins = np.linspace(min(df_nonzero[column].values), max(df_nonzero[column].values), num=200)

    import matplotlib.pyplot as plt
    plt.figure()
    plt.hist(df_nonzero[column].values, bins=bins, weights=df_nonzero['histo'].values, density=True, histtype='step',
             label='all edep between 0.4 & 32.0 keV')

    new_hist = None
    for i in range(len(unics) - 1):

        value = np.sum(selected_edep[(selected_edep[column].values >= unics[i]) & (selected_edep[column].values < unics[i + 1])].histo.values)

        v = np.stack((unics[i], value))
        if new_hist is None:
            new_hist = v
        else:
            new_hist = np.vstack((new_hist, v))
    plt.hist(new_hist[:, 0], bins=bins, weights=new_hist[:, 1], density=True, histtype='step',
             label='edep between ' + str(lowlim) + ' & ' + str(highlim) + ' keV')

    lowlim = 16.  # keV
    highlim = 32.  # keV

    selected_edep = df_nonzero[(df_nonzero['edep'].values >= lowlim) & (df_nonzero['edep'].values < highlim)]

    unics = np.unique(selected_edep[column].values)

    new_hist = None
    for i in range(len(unics) - 1):

        value = np.sum(selected_edep[(selected_edep[column].values >= unics[i]) & (
                    selected_edep[column].values < unics[i + 1])].histo.values)

        v = np.stack((unics[i], value))
        if new_hist is None:
            new_hist = v
        else:
            new_hist = np.vstack((new_hist, v))
    plt.hist(new_hist[:, 0], bins=bins, weights=new_hist[:, 1], density=True, histtype='step',
             label='edep between ' + str(lowlim) + ' & ' + str(highlim) + ' keV')

    plt.legend()
    plt.title(column)
    plt.show()


def load_geant4_histogram(file_name, hist_type, skip_rows, read_rows):
    """TBW.

    :param file_name:
    :param hist_type:
    :param skip_rows:
    :param read_rows:
    """
    return pd.read_csv(file_name, delimiter="\t", names=[hist_type, "counts"],
                       usecols=[1, 2], skiprows=skip_rows, nrows=read_rows)


if __name__ == "__main__":
    geant4()
    # geant4_new()

    # read_pd_csv(file='data/geant4/elec_df_copy.csv', column='cluster_size', rebin=200)
    # read_pd_csv(file='data/geant4/step_df.csv', column='step_size', rebin=200)

    # read_pd_csv_edep(file='data/geant4/elec_df_copy.csv', column='cluster_size')
    # read_pd_csv_edep(file='data/geant4/step_df.csv', column='step_size')

