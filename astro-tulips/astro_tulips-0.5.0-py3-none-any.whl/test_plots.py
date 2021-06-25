# Copyright (c) 2021, Eva Laplace e.c.laplace@uva.nl

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from tulips import *

# # Use LaTeX in the plots
from matplotlib import rc

fsize = 30
SMALL_SIZE = 25
MEDIUM_SIZE = 25
BIGGER_SIZE = 30
rc('font', **{'family': 'DejaVu Sans', 'serif': ['Times'], 'size': fsize})
rc('text', usetex=True)
plt.rc('font', size=MEDIUM_SIZE)  # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)  # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

BASE_DIR = '/home/laplace/Documents/Amsterdam/phd/year1/stripped_stars/'
DATA_DIR = "/MESA_DIR_EXAMPLE"
STRIPPED_LOWZ_DIR = BASE_DIR + 'mesa_models_stripped_binaries/example_binary_model10.48Msun/M10.48_Zlow_v2/'
OUT_DIR = "/home/laplace/Documents/Amsterdam/Documents/API/travels/2019/Kyoto_7-11October_2019/Poster_talk/"
STRIPPED_ZSUN_DIR = BASE_DIR + 'mesa_models_stripped_binaries/example_binary_model10.48Msun/M10.48_Zsun_v2/'
# Run tests
if __name__ == "__main__":
    m = mp.MESA()
    m.loadHistory(DATA_DIR)
    tulips.perceived_color(m,time_ind=0)
    #
    # # # Test plot of radius over time
    # animated_hist_test(m, time_index=0)
    # plt.show()
    #
    # # Test plot of star_mass over time
    # multiplots_hist_test(m, raxis="star_mass", time_index=-1)
    # plt.show()

    # # Test movie
    # stop_ind = int(np.where((m.hist.center_o16 > 0.1) & (m.hist.center_c12 < 1e-4))[0][0])
    # print(stop_ind)
    # animated_hist(m, plot_name_base="single_M10.5", plot_dir=OUT_DIR, raxis="log_R", time_index_end=stop_ind,
    #               time_index_step=20, fps=15)
    #
    # # Test interior plot
    # animated_hist_interior_test(m, time_index=2000)
    # plt.show()
    #
    # # Test interior animation
    # # stop_ind = np.where(m.hist.star_age > 1.50406e7)[0][0]
    # animated_hist_interior(m, plot_name_base="single_M10.5_interior_", plot_dir=OUT_DIR, time_index_end=stop_ind,
    #                        time_index_step=20, fps=15, cmin=-8, cmax=8)

    # Zlow stripped star
    m1 = mp.MESA()
    m1.loadHistory(filename_in=STRIPPED_LOWZ_DIR + 'history_new.data')
    # animated_hist_interior_test(m, time_index=-1)
    # plt.show()
    #
    # # Radius movie
    # stop_ind = int(np.where((m.hist.center_o16 > 0.1) & (m.hist.center_c12 < 1e-4))[0][0])
    # animated_hist(m, plot_name_base="stripped_M10.5", plot_dir=OUT_DIR, raxis="log_R", time_index_end=stop_ind,
    #               time_index_step=20, fps=15)
    #
    # # Interior movie
    # # stop_ind = np.where(m.hist.star_age > 1.50406e7)[0][0]
    # animated_hist_interior(m, plot_name_base="stripped_M15_interior_", plot_dir=OUT_DIR, time_index_end=stop_ind,
    #                        time_index_step=20, fps=15, cmin=-10, cmax=10)

    # Zsun stripped star
    m2 = mp.MESA()
    m2.loadHistory(filename_in=STRIPPED_ZSUN_DIR + 'history_new.data')
    # animated_hist_test(m2, time_index=-1)
    # plt.show()
    #
    # # Radius movie
    # stop_ind = int(np.where((m2.hist.center_o16 > 0.1) & (m2.hist.center_c12 < 1e-4))[0][0])
    # print(stop_ind)
    # animated_hist(m2, plot_name_base="new_stripped_M10.5_Zsun", plot_dir=OUT_DIR, raxis="log_R", time_index_end=stop_ind,
    #               time_index_step=20, fps=15)
    #
    # # Interior movie
    # # stop_ind = np.where(m.hist.star_age > 1.50406e7)[0][0]
    # animated_hist_interior(m, plot_name_base="stripped_M10.5_Zsun_interior_", plot_dir=OUT_DIR, time_index_end=stop_ind,
    #                        time_index_step=20, fps=15, cmin=-10, cmax=10)


    # Test comparison plots
    stop_ind1 = int(np.where((m2.hist.center_o16 > 0.1) & (m2.hist.center_c12 < 1e-4))[0][0])
    stop_ind2 = int(np.where((m1.hist.center_o16 > 0.1) & (m1.hist.center_c12 < 1e-4))[0][0])
    animated_hist_comp_test(m2, m1, label1="$Z_{\odot}$", label2="Z_{\\rm{low}", time_index1=stop_ind1,
                            time_index2=stop_ind2)
    plt.show()

    # Test comparison animation
    stop_ind1 = int(np.where((m2.hist.center_o16 > 0.1) & (m2.hist.center_c12 < 1e-4))[0][0])
    stop_ind2 = int(np.where((m1.hist.center_o16 > 0.1) & (m1.hist.center_c12 < 1e-4))[0][0])
    animated_hist_comp(m2, m1, label1="$Z_{\odot}$", label2="Z_{\\rm{low}", plot_name_base="test_comp_Zsun_Zlow",
                       time_index_end1=stop_ind1, time_index_end2=stop_ind2)

