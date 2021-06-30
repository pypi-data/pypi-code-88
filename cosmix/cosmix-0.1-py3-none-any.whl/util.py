"""CosmiX model to generate charge by ionization."""
import glob
from bisect import bisect
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import interpolate

PATH = Path(__file__).parent.joinpath('data', 'stepsize')


def get_xvalue_with_interpolation(function_array, y_value):
    """TBW.

    :param function_array:
    :param y_value:
    """
    if y_value <= function_array[0, 1]:
        intpol_x_value = function_array[0, 0]
    elif y_value >= function_array[-1, 1]:
        intpol_x_value = function_array[-1, 0]
    else:
        y_index_bot = bisect(function_array[:, 1], y_value) - 1
        y_index_top = y_index_bot + 1

        y_value_bot = function_array[y_index_bot, 1]
        y_value_top = function_array[y_index_top, 1]
        x_value_bot = function_array[y_index_bot, 0]
        x_value_top = function_array[y_index_top, 0]

        intpol_x_value = x_value_bot + (y_value - y_value_bot) * \
            (x_value_top - x_value_bot) / (y_value_top - y_value_bot)

    return intpol_x_value


def get_yvalue_with_interpolation(function_array, x_value):
    """TBW.

    :param function_array:
    :param x_value:
    """
    if x_value <= function_array[0, 0]:
        intpol_y_value = function_array[0, 1]
    elif x_value >= function_array[-1, 0]:
        intpol_y_value = function_array[-1, 1]
    else:
        x_index_bot = bisect(function_array[:, 0], x_value) - 1
        x_index_top = x_index_bot + 1

        x_value_bot = function_array[x_index_bot, 0]
        x_value_top = function_array[x_index_top, 0]
        y_value_bot = function_array[x_index_bot, 1]
        y_value_top = function_array[x_index_top, 1]

        intpol_y_value = y_value_bot + (x_value - x_value_bot) * \
            (y_value_top - y_value_bot) / (x_value_top - x_value_bot)

    return intpol_y_value


def load_geant4_histogram(file_name, hist_type, skip_rows, read_rows):
    """TBW.

    :param file_name:
    :param hist_type:
    :param skip_rows:
    :param read_rows:
    """
    return pd.read_csv(file_name, delimiter="\t", names=[hist_type, "counts"],
                       usecols=[1, 2], skiprows=skip_rows, nrows=read_rows)


def read_gras_data():
    """TBW."""
    path = Path(__file__).parent.joinpath('data')
    p_df = pd.read_csv(Path(path, 'GRAS_input_spectrum_proton.csv'), index_col=None)
    a_df = pd.read_csv(Path(path, 'GRAS_input_spectrum_alpha.csv'), index_col=None)
    p_spectrum = np.stack((p_df.energy.values, p_df.flux.values), axis=1)
    alpha_spectrum = np.stack((a_df.energy.values, a_df.flux.values), axis=1)
    return np.around(p_spectrum, decimals=10), np.around(alpha_spectrum, decimals=10)


def load_data_into_histogram(array, lim=(None, None), plato=True, regrp=None):
    """TBW.

    :return:
    """
    dist = array[1, 0] - array[0, 0]
    hist_bins = array[:, 0]
    hist = array[:, 1]

    if plato:
        hist_bins -= dist / 2
        z = sorted(np.arange(hist_bins[0]-dist, 0., -1*dist))
        hist_bins = np.append(z, hist_bins)
        hist = np.append(np.zeros(len(z)), hist)

    if lim[0] is not None:
        range1 = np.where(lim[0] <= hist_bins)
        hist_bins = hist_bins[range1]
        hist = hist[range1]
    if lim[1] is not None:
        range2 = np.where(hist_bins <= lim[1])
        hist_bins = hist_bins[range2]
        hist = hist[range2]

    if regrp is not None:
        new_hist = np.array([])
        new_hist_bins = np.array([])
        for i in range(int(len(hist)/regrp)):
            new_hist = np.append(new_hist, np.sum(hist[regrp*i:regrp*(i+1)]))
            new_hist_bins = np.append(new_hist_bins, np.mean(hist_bins[regrp*i:regrp*(i+1)]))
        hist_bins = new_hist_bins
        hist = new_hist

    return np.stack((hist_bins, hist), axis=1)


def read_data(file_name):
    """TBW.

    :param file_name:
    :return:
    """
    return np.loadtxt(file_name, 'float', '#')


def interpolate_data(data):
    """TBW.

    :param data:
    :return:
    """
    return interpolate.interp1d(x=data[:, 0], y=data[:, 1], kind='linear')


# def read_particle_spectrum(file_name, detector_area):
#     """TBW.
#
#     :param file_name: path of the file containing the spectrum
#     :param detector_area: area of detector
#     """
#     spectrum = read_data(file_name)                             # nuc/m2*s*sr*MeV
#     spectrum[:, 1] *= 4 * math.pi * 1.0e-4 * detector_area      # nuc/s*MeV  # area or surface should be used here?
#
#     spectrum_function = interpolate_data(spectrum)
#
#     size = len(spectrum[:, 0])
#     lb = spectrum[0, 0]
#     ub = spectrum[-1, 0]
#     energy_range = np.logspace(start=np.log10(lb), stop=np.log10(ub), num=size)
#
#     cum_sum = np.cumsum(spectrum_function(energy_range))
#     cum_sum /= np.max(cum_sum)
#     spectrum_cdf = np.stack((energy_range, cum_sum), axis=1)
#
#     return spectrum_cdf, spectrum_function(energy_range)


def sampling_distribution(distribution):
    """TBW.

    :param distribution:
    """
    u = np.random.random()
    return get_xvalue_with_interpolation(distribution, u)


def rebin_cdf(cdf, limit, group=10):
    """TBW."""
    y_array = np.array([])
    x_array = np.array([])

    lb = int(np.where(cdf[:, 1] >= limit)[0][0])
    ub = len(cdf[:, 1]) - 1

    for i in range(lb, ub, group):
        y_array = np.append(y_array, np.mean(cdf[i:(i + group), 1]))
        x_array = np.append(x_array, np.mean(cdf[i:(i + group), 0]))

    y_array = np.append(cdf[:lb, 1], y_array)
    x_array = np.append(cdf[:lb, 0], x_array)

    y_array = np.append(y_array, cdf[-1, 1])
    x_array = np.append(x_array, cdf[-1, 0])

    return np.stack((x_array, y_array), axis=1)


def calculate_cdf(dataframe, quantity):
    """TBW."""
    values = dataframe[quantity].values
    if quantity == 'electron':
        values = np.floor(values)

    cum_sum = np.cumsum(dataframe['counts'].values)
    cum_sum /= np.max(cum_sum)

    cdf = np.stack((values, cum_sum), axis=1)
    # cdf = np.around(cdf, decimals=6)
    end = int(np.where(cdf[:, 1] >= 1.)[0][0]) + 1
    cdf = cdf[:end, :]

    # cdf = rebin_cdf(cdf, limit=0.98, group=100)
    # cdf = rebin_cdf(cdf, limit=0.999, group=10)
    # cdf = np.around(cdf, decimals=6)
    # if quantity == 'electron':
    #     cdf[:, 0] = np.rint(cdf[:, 0])

    return cdf


def read_data_library_new():    # todo: material='Silicon', particle='proton'):
    """TBW."""
    return (pd.read_csv(Path(PATH, 'step_data_library.csv')),
            pd.read_csv(Path(PATH, 'elec_data_library.csv')),
            pd.read_csv(Path(PATH, 'edep_data_library.csv')))


def create_data_library_new(thickness='300nm'):
    """TBW."""
    step_data_library = pd.DataFrame(columns=['energy', 'step', 'step_cdf'])
    elec_data_library = pd.DataFrame(columns=['energy', 'electron', 'electron_cdf'])
    edep_data_library = pd.DataFrame(columns=['energy', 'edep', 'edep_cdf'])     # energy deposited over the 10 um track

    file_list = glob.glob(str(PATH.joinpath('stepsize_' + thickness, '*' + thickness + '*.ascii')))
    for g4filepath in file_list:

        loc = g4filepath.rfind('\\')
        if loc == -1:
            g4file = g4filepath[g4filepath.rfind('/') + 1:]
        else:
            g4file = g4filepath[loc + 1:]

        energy = None
        if 'keV' in g4file:
            energy = g4file[:g4file.rfind('keV')]
            energy = float(energy[energy.rfind('_') + 1:])      # keV
            energy /= 1000.                                     # MeV
        elif 'MeV' in g4file:
            energy = g4file[:g4file.rfind('MeV')]
            energy = float(energy[energy.rfind('_') + 1:])      # MeV

        # if 'proton' in g4file:
        #     particle_type = 'proton'
        # elif 'e-' in g4file:
        #     particle_type = 'electron'
        #
        # if 'Silicon' in g4file:
        #     material = 'Silicon'

        x = [10000, 1000, 1000, 2000, 3000, 1000, 10000, 4000]
        # # step size distribution in um
        step_size_dist = load_geant4_histogram(g4filepath, hist_type='step_size', skip_rows=4, read_rows=x[0])
        step_cdf = calculate_cdf(step_size_dist, quantity='step_size')

        # # tertiary electron numbers created by secondary electrons
        elec_number_dist = load_geant4_histogram(g4filepath, hist_type='electron',
                                                 skip_rows=sum(x[:2]) + 4 * 3, read_rows=x[2])
        elec_number_cdf = calculate_cdf(elec_number_dist, quantity='electron')

        # # total energy deposited
        edep_number_dist = load_geant4_histogram(g4filepath, hist_type='edep',
                                                 skip_rows=sum(x[:6])+4*7, read_rows=x[6])
        edep_number_cdf = calculate_cdf(edep_number_dist, quantity='edep')

        size = len(step_cdf[:, 1])
        step_dict = {
            'energy': [energy] * size,
            'step': step_cdf[:, 0],
            'step_cdf': step_cdf[:, 1]
        }
        # 'type': [particle_type] * size,
        # 'material': [material] * size,
        size2 = len(elec_number_cdf[:, 1])
        elec_dict = {
            'energy': [energy] * size2,
            'electron': elec_number_cdf[:, 0],
            'electron_cdf': elec_number_cdf[:, 1]
        }
        size3 = len(edep_number_cdf[:, 1])
        edep_dict = {
            'energy': [energy] * size3,
            'edep': edep_number_cdf[:, 0],
            'edep_cdf': edep_number_cdf[:, 1]
        }

        step_new_df = pd.DataFrame(step_dict)
        elec_new_df = pd.DataFrame(elec_dict)
        edep_new_df = pd.DataFrame(edep_dict)

        step_data_library = pd.concat([step_data_library, step_new_df], ignore_index=True)
        elec_data_library = pd.concat([elec_data_library, elec_new_df], ignore_index=True)
        edep_data_library = pd.concat([edep_data_library, edep_new_df], ignore_index=True)

    step_data_library.to_csv(Path(PATH, 'step_data_library.csv'), index=False, line_terminator='\n')
    elec_data_library.to_csv(Path(PATH, 'elec_data_library.csv'), index=False, line_terminator='\n')
    edep_data_library.to_csv(Path(PATH, 'edep_data_library.csv'), index=False, line_terminator='\n')

    step_data_library.to_pickle(str(Path(PATH, 'step_data_library.pkl')))
    elec_data_library.to_pickle(str(Path(PATH, 'elec_data_library.pkl')))
    edep_data_library.to_pickle(str(Path(PATH, 'edep_data_library.pkl')))


def find_smaller_neighbor(sorted_array, value):
    """TBW.

    :return:
    """
    index = bisect(sorted_array, value) - 1
    if index <= 0:
        return sorted_array[0]
    else:
        return sorted_array[index]


def find_larger_neighbor(sorted_array, value):
    """TBW.

    :return:
    """
    index = bisect(sorted_array, value)
    if index > len(sorted_array) - 1:
        index = len(sorted_array) - 1
    return sorted_array[index]


def find_closest_neighbor(sorted_array, value):
    """TBW.

    :return:
    """
    index_smaller = bisect(sorted_array, value) - 1
    index_larger = bisect(sorted_array, value)

    if index_larger >= len(sorted_array):
        return sorted_array[-1]
    elif (sorted_array[index_larger]-value) < (value-sorted_array[index_smaller]):
        return sorted_array[index_larger]
    else:
        return sorted_array[index_smaller]


def load_cdf(df, p_energy):
    """TBW.

    :param df: CDF dataframe
    :param p_energy: float (MeV)
    :return:
    """
    selected = df[df.energy == p_energy].values[:, 1:]
    return np.around(selected, decimals=6)


# def geant4_validation():
#     """TBW."""
#     material = 'Silicon'
#     particle_type = 'proton'
#     # energy_list = [10, 100, 1000, 10000]
#
#     energy_list = [53, 54, 56, 55, 55, 55]
#     thickness_list = ['15', '15', '15', '15', '17', '20']
#
#     energy_list = [55]
#     thickness_list = ['15']
#
#     path = Path(__file__).parent.joinpath('data', 'validation')
#
#     all_hist = None
#     for energy, thickness in zip(energy_list, thickness_list):
#
#         g4file = Path(path, 'PLATO_irrad_proton_55MeV_10um_Silicon_10000.ascii')
#
#         x = [10000, 1000, 1000, 2000, 3000, 1000, 10000, 4000]
#
#         step_size = load_geant4_histogram(g4file, hist_type='step_size', skip_rows=4, read_rows=x[0])
#         edep_prim = load_geant4_histogram(g4file, hist_type='edep_prim', skip_rows=sum(x[:1])+4*2, read_rows=x[1])
#         electron = load_geant4_histogram(g4file, hist_type='electron', skip_rows=sum(x[:2])+4*3, read_rows=x[2])
#         sec = load_geant4_histogram(g4file, hist_type='sec', skip_rows=sum(x[:3])+4*4, read_rows=x[3])
#         ter = load_geant4_histogram(g4file, hist_type='ter', skip_rows=sum(x[:4])+4*5, read_rows=x[4])
#         edep_sec_ter = load_geant4_histogram(g4file, hist_type='edep_sec_ter',
#                                              skip_rows=sum(x[:5])+4*6, read_rows=x[5])
#         edep_all = load_geant4_histogram(g4file, hist_type='edep_all', skip_rows=sum(x[:6])+4*7, read_rows=x[6])
#         all_elec = load_geant4_histogram(g4file, hist_type='all_elec', skip_rows=sum(x[:7])+4*8, read_rows=x[7])
#
#         # step_hist = load_data_into_histogram(step_size.values, plato=False)
#         # elec_hist = load_data_into_histogram(electron.values, plato=False)
#         # sec_hist = load_data_into_histogram(sec.values, plato=False)
#         # ter_hist = load_data_into_histogram(ter.values, plato=False)
#         all_hist = load_data_into_histogram(all_elec.values, plato=False, lim=(0, 20000))
#
#     # plt.legend()
#
#     return all_hist


# def read_stopping_power():
#     """Stopping Power Unit = keV / micron."""
#     file = Path(__file__).parent.joinpath('data', 'stepsize', 'SRIM_proton_in_silicon.txt')
#     data = pd.read_csv(file, skiprows=23, sep=' ', index_col=False, header=None,  # skipfooter=13,
#                        names=['energy', 'unit_energy',
#                               'LET_EM', 'LET_Nuc',
#                               'range', 'unit_range',
#                               'long_straggling', 'unit_long',
#                               'lat_straggling', 'unit_lat'])
#     units = {
#         'eV':  1.e-6,
#         'keV': 1.e-3,
#         'MeV': 1.e+0,
#         'GeV': 1.e+3
#     }
#     energy = np.array([])
#     for k, v in units.items():
#         energy = np.append(energy, data.energy[data.unit_energy == k].values * v)
#         # data.unit_energy[data.unit_energy == k] = 'MeV'
#     s = data.energy.values.size
#     return np.hstack((energy.reshape(s, 1),
#                       data.LET_EM.values.reshape(s, 1)))
