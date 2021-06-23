##########################################################################
# Track Analyzer - Quantification and visualization of tracking data     #
# Authors: Arthur Michaut                                                #
# Copyright 2016-2019 Harvard Medical School and Brigham and             #
#                          Women's Hospital                              #
# Copyright 2019-2021 Institut Pasteur and CNRS–UMR3738                  #
# See the COPYRIGHT file for details                                     #
#                                                                        #
# This file is part of Track Analyzer package.                           #
#                                                                        #
# Track Analyzer is free software: you can redistribute it and/or modify #
# it under the terms of the GNU General Public License as published by   #
# the Free Software Foundation, either version 3 of the License, or      #
# (at your option) any later version.                                    #
#                                                                        #
# Track Analyzer is distributed in the hope that it will be useful,      #
# but WITHOUT ANY WARRANTY; without even the implied warranty of         #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the           #
# GNU General Public License for more details .                          #
#                                                                        #
# You should have received a copy of the GNU General Public License      #
# along with Track Analyzer (COPYING).                                   #
# If not, see <https://www.gnu.org/licenses/>.                           #
##########################################################################

import os.path as osp

import matplotlib.pyplot as plt
import seaborn as sns

from track_analyzer import prepare as tpr
from track_analyzer import plotting as tpl

# Plotting parameters
color_list = [c['color'] for c in list(plt.rcParams['axes.prop_cycle'])] + sns.color_palette("Set1", n_colors=9,
                                                                                             desat=.5)
plot_param = {'figsize': (5, 5), 'dpi': 300, 'color_list': color_list, 'format': '.png', 'despine': True, 'logx': False,
              'logy': False, 'invert_yaxis': True, 'export_data_pts': False}


def compare_datasets(data_dir, df_list=[], track_df_list=[], MSD_df_list=[], datasets_names=[], plotting_mode='compare',
                     param_couples=None, param_hist=None, param_boxplot=None,
                     param_track_couples=None, param_track_hist=None, param_track_boxplot=None,
                     MSD_plot_param={'logplot_x': True, 'logplot_y': True, 'alpha': 0.2},
                     plot_param=plot_param):
    """Compare different datasets with a list of plotting methods: couples of parameters, histograms, boxplot.
    Each of these three methods (param_couples,param_hist,param_boxplot) are given as dict containing the list of parameters and some specific arguments.
    """

    print("Analyzing datasets: " + ', '.join(datasets_names))

    pool_dir = osp.join(data_dir, 'pooled_datasets')
    tpr.safe_mkdir(pool_dir)

    # plotting option
    if plotting_mode == 'compare':
        hue = 'dataset'
        hue_order = datasets_names
        x_param = 'dataset'
        order = datasets_names
    elif plotting_mode == 'pool':
        hue = None
        hue_order = None
        x_param = None
        order = None

    # merge datasets
    pooled_all_df = tpr.pool_datasets(df_list, datasets_names)
    pooled_track_df = tpr.pool_datasets(track_df_list, datasets_names)
    pooled_MSD_df = tpr.pool_datasets(MSD_df_list, datasets_names)
    names_str = plotting_mode + '_' + '_'.join(datasets_names)

    plot_dir = osp.join(pool_dir, names_str)
    tpr.safe_mkdir(plot_dir)

    pooled_all_df.to_csv(osp.join(plot_dir, 'pooled_all_data.csv'))
    pooled_track_df.to_csv(osp.join(plot_dir, 'pooled_track_data.csv'))
    pooled_MSD_df.to_csv(osp.join(plot_dir, 'pooled_MSD_data.csv'))

    if param_couples is not None:
        if len(param_couples['couples']) > 0:
            print("plotting scatter plots")
        for param_couple in param_couples['couples']:
            tpl.plot_param_vs_param(data_dir, param_couple[0], param_couple[1], df=pooled_all_df, hue=hue,
                                    hue_order=hue_order, set_axis_lim=param_couples['axis_lim'], plot_param=plot_param,
                                    plot_dir=plot_dir, suffix='_' + names_str)

    if param_track_couples is not None:
        if len(param_track_couples['couples']) > 0:
            print("plotting scatter plots")
        for param_couple in param_track_couples['couples']:
            tpl.plot_param_vs_param(data_dir, param_couple[0], param_couple[1], df=pooled_track_df, hue=hue,
                                    hue_order=hue_order, set_axis_lim=param_track_couples['axis_lim'],
                                    plot_param=plot_param, plot_dir=plot_dir, suffix='_' + names_str)

    if param_hist is not None:
        if len(param_hist['param']) > 0:
            print("plotting histograms")
        for param in param_hist['param']:
            tpl.plot_param_hist(data_dir, param, df=pooled_all_df, hue=hue, hue_order=hue_order,
                                hist=param_hist['hist'], kde=param_hist['kde'], rug=param_hist['rug'],
                                plot_param=plot_param, plot_dir=plot_dir, suffix='_' + names_str)

    if param_track_hist is not None:
        if len(param_track_hist['param']) > 0:
            print("plotting histograms")
        for param in param_track_hist['param']:
            tpl.plot_param_hist(data_dir, param, df=pooled_track_df, hue=hue, hue_order=hue_order,
                                hist=param_track_hist['hist'], kde=param_track_hist['kde'], rug=param_track_hist['rug'],
                                plot_param=plot_param, plot_dir=plot_dir, suffix='_' + names_str)

    if param_boxplot is not None:
        if len(param_boxplot['param']) > 0:
            print("plotting boxplots")
        for param in param_boxplot['param']:
            tpl.plot_param_boxplot(data_dir, df=pooled_all_df, x_param=x_param, param=param, order=order,
                                   save_stat=param_boxplot['save_stat'], boxplot=param_boxplot['boxplot'],
                                   swarmplot=param_boxplot['swarmplot'], plot_param=plot_param, plot_dir=plot_dir,
                                   suffix='_' + names_str)

    if param_track_boxplot is not None:
        if len(param_track_boxplot['param']) > 0:
            print("plotting boxplots")
        for param in param_track_boxplot['param']:
            tpl.plot_param_boxplot(data_dir, df=pooled_track_df, x_param=x_param, param=param, order=order,
                                   save_stat=param_track_boxplot['save_stat'], boxplot=param_track_boxplot['boxplot'],
                                   swarmplot=param_track_boxplot['swarmplot'], plot_param=plot_param, plot_dir=plot_dir,
                                   suffix='_' + names_str)

    if MSD_plot_param is not None:
        # add parameters
        print("plotting MSD")
        MSD_plot_param['dim'] = 2
        MSD_plot_param['fitrange'] = False
        MSD_plot_param['plot_all_MSD'] = True
        MSD_plot_param['plot_single_MSD'] = False
        tpl.plot_all_MSD(data_dir, msd_all=pooled_MSD_df, fit_model=None, MSD_parameters=MSD_plot_param, hue=hue,
                         hue_order=hue_order, plot_param=plot_param, plot_dir=plot_dir)

    return pooled_all_df, pooled_track_df


def batch_analysis(dirdata, run_='cell_analysis', refresh=False, invert_yaxis=True):
    dirdata_l = tpr.listdir_nohidden(dirdata)
    dirdata_l_ = []
    for d in dirdata_l:
        dirdata_ = osp.join(dirdata, d)
        if osp.isdir(dirdata_) and d != 'outdata':
            dirdata_l_.append(d)
    for i, d in enumerate(dirdata_l_):
        dirdata_ = osp.join(dirdata, d)
        print("processing directory {} ({}/{})".format(d, i + 1, len(dirdata_l_)))
        if run_ == 'cell_analysis':
            cell_analysis(dirdata_, no_bkg=True, show_axis=True, plot_vel=None, min_traj_len=10, plot_vs_Y=True,
                          dont_plot_cells=True, refresh=refresh, invert_yaxis=invert_yaxis)
            # analysis_func(dirdata_,no_bkg=True,show_axis=True,plot_vel=None,min_traj_len=10,plot_vs_Y=True,dont_plot_cells=True,dont_set_origin=True)
        elif run_ == 'pooled_MSD':
            df, lengthscale, timescale, columns, dim = tpr.get_data(dirdata_)
            plot_pooled_MSD(data_dir, dt=timescale, plot_method='along_Y')
