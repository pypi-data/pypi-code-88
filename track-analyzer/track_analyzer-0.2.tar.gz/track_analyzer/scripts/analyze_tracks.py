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
import sys
import argparse

from track_analyzer import prepare as tpr
from track_analyzer import plotting as tpl
from track_analyzer import calculate as tca


def traj_analysis(data_dir, data=None, image=None, refresh=False, parallelize=False, filters=None, plot_config=None,
                  traj_config=None, data_config=None):
    """Container method to run analysis related to cell trajectories."""

    traj_dir = osp.join(data_dir, 'traj_analysis')
    tpr.safe_mkdir(traj_dir)

    # Get image
    image = tpr.get_image(data_dir) if image is None else image

    # Get data
    data_config = tpr.make_data_config(data_dir=data_dir, export_config=False) if data_config is None else data_config
    if data is None: 
        data = tpr.get_data(data_dir, refresh=refresh, split_traj=data_config["split_traj"], set_origin_=data_config["set_origin_"], 
                            image=image, reset_dim=data_config["reset_dim"], invert_axes=data_config["invert_axes"])

    df = data['df']
    dim = data['dim']
    dimensions = data['dimensions']

    # Get config
    plot_config = tpl.make_plot_config(data_dir=data_dir, export_config=False) if plot_config is None else plot_config

    traj_config_default = tpr.make_traj_config(data_dir=data_dir, export_config=False)
    traj_config = traj_config_default if traj_config is None else traj_config

    # check that all configs are in traj_confign, if not load default
    for key in ["traj_config_", "MSD_config", "scatter_config", "hist_config", "total_traj_config", "voronoi_config"]:
        if key not in traj_config.keys():
            traj_config[key] = traj_config_default[key]

    traj_config_ = traj_config["traj_config_"]
    MSD_config = traj_config["MSD_config"]
    scatter_config = traj_config["scatter_config"]
    hist_config = traj_config["hist_config"]
    total_traj_config = traj_config["total_traj_config"]
    voronoi_config = traj_config["voronoi_config"]

    # Filter data
    filters = tpr.init_filters(data_dir=data_dir, export_to_config=False) if filters is None else filters
    subset_analysis = filters['subset']  # how to deal with subsets
    filters_ = filters['filters_list']
    df = tpr.select_sub_data(df, filters=filters_)
    if subset_analysis == 'together':
        df_list = [df]  # a single df is kept
        # force color coding trajectory plotting
        traj_config_['color_code'] = 'ROI'
        total_traj_config['color_code'] = 'ROI'
    elif subset_analysis == 'separately':
        df_list = [df[df['subset'] == sub] for sub in df['subset'].unique()]  # a list of df filtered by subset

    # Run analysis
    for i, df in enumerate(df_list):
        # name subset directory
        dir_name = ''
        if subset_analysis == 'separately':
            subset_name = df['subset'].values[0]
            dir_name = '_' + subset_name if subset_name != '' else ''
        dir_name_ = '{}{}'.format(len(tpr.listdir_nohidden(traj_dir)) + 1, dir_name)

        print(r"Analyzing subset #{}, named: {}".format(i + 1, dir_name_))
        sub_dir = osp.join(traj_dir, dir_name_)
        sub_dir = sub_dir + '_1' if osp.exists(sub_dir) else sub_dir  # dont overwrite existing dir
        tpr.safe_mkdir(sub_dir)

        # export data
        csv_fn = osp.join(sub_dir, 'all_data.csv')
        df.to_csv(csv_fn)

        # save pipeline parameters
        config_dir = osp.join(sub_dir, 'config')
        tpr.safe_mkdir(config_dir)
        fn = osp.join(config_dir, 'filters.csv')
        tpr.write_dict(filters_[i], fn)
        for key in traj_config.keys():
            fn = osp.join(config_dir, key + '.csv')
            tpr.write_dict(traj_config[key], fn)
        #        if filters[i]['ROI'] is not None:
        #            filters[i]['ROI']['coord'] = ROI_list[i]
        #        params_d = [filters[i], traj_config_, MSD_config, plot_config]
        #        params_n = ['filters', 'traj parameters', 'MSD parameters', 'plotting parameters']
        #        tpr.write_dict(params_d, filename, dict_names=params_n)

        # compute mean track properties
        mean_fn = osp.join(sub_dir, 'track_prop.csv')
        df_prop = tca.compute_track_prop(df, dimensions)
        df_prop.to_csv(mean_fn)

        # analysis and plotting
        if subset_analysis == 'together':
            hue = 'subset'
            hue_order = df['subset'].unique() if filters['subset_order'] is None else filters['subset_order']
            traj_config_['subset_order'] = hue_order
        else:
            hue = None
            hue_order = None


        # plot trajectories
        if traj_config_['run']:
            print("Plotting trajectories...")
            tpl.plot_all_traj(data_dir, df, image=image, traj_parameters=traj_config_, parallelize=parallelize,
                              dim=dim, plot_dir=sub_dir, plot_config=plot_config)

        if total_traj_config['run']:
            print("Plotting total trajectories")
            tpl.plot_total_traj(data_dir, df, dim=dim, plot_dir=sub_dir, plot_config=plot_config,
                                specific_config=total_traj_config)

        # MSD analysis
        if MSD_config['run']:
            print("MSD analysis...")
            MSD_dir = tpr.safe_mkdir(osp.join(sub_dir, 'MSD'))
            df_prop = tpl.plot_all_MSD(data_dir, df, df_out=df_prop, fit_model=MSD_config['MSD_model'],
                                       MSD_parameters=MSD_config, plot_config=plot_config, plot_dir=MSD_dir, hue=hue,
                                       hue_order=hue_order)
            df_prop.to_csv(mean_fn)

        # Voronoi analysis
        if voronoi_config['run']:
            vor_data = tca.compute_all_Voronoi(data_dir, df, outdir=sub_dir,compute_local_area=voronoi_config['compute_local_area'],
                                            area_threshold=voronoi_config['area_threshold'],df_mean=df_prop)
            df_prop.to_csv(mean_fn)
            
            if voronoi_config['plot']:
                plot_dir = osp.join(sub_dir, 'voronoi')
                tpr.safe_mkdir(plot_dir)
                tpl.plot_all_Voronoi(data_dir, df, vor_data, show_local_area=voronoi_config['show_local_area'], image=image,
                                     map_param=voronoi_config, plot_dir=plot_dir, plot_config=plot_config, dont_print_count=False)

        if hist_config['run']:
            if len(hist_config['var_list']) > 0:
                print("Plotting parameters histograms...")
            for p in hist_config['var_list']:
                tpl.plot_param_hist(data_dir, p, df, plot_config=plot_config, plot_dir=sub_dir, hue=hue,
                                    hue_order=hue_order)

            if len(hist_config['mean_var_list']) > 0:
                print("Plotting whole-track histograms...")
            for p in hist_config['mean_var_list']:
                tpl.plot_param_hist(data_dir, p, df_prop, plot_config=plot_config, plot_dir=sub_dir, prefix='track_',
                                    hue=hue, hue_order=hue_order)

        if scatter_config['run']:
            if len(scatter_config['couple_list']) > 0:
                print("Plotting couples of parameters...")
            for param_vs_param in scatter_config['couple_list']:
                x_param, y_param = param_vs_param
                tpl.plot_param_vs_param(data_dir, x_param, y_param, df, plot_dir=sub_dir, plot_config=plot_config,
                                        hue=hue, hue_order=hue_order)

            if len(scatter_config['mean_couple_list']) > 0:
                print("Plotting couples of whole-track parameters...")
            for param_vs_param in scatter_config['mean_couple_list']:
                x_param, y_param = param_vs_param
                tpl.plot_param_vs_param(data_dir, x_param, y_param, df_prop, plot_dir=sub_dir, plot_config=plot_config,
                                        prefix='track_', hue=hue, hue_order=hue_order)

    return df_list


def parse_args(args=None):
    """
    parse arguments for main()
    """

    #    description = """Analyze trajectories
    #                Argument :
    #                -
    #                """

    #    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=description)
    parser = argparse.ArgumentParser()

    parser.add_argument('data_dir',
                        help='path of the data directory')

    parser.add_argument('-r', '--refresh',
                        action="store_true",
                        default=False,
                        help='refresh database')

    parser.add_argument('-p', '--parallelize',
                        action="store_true",
                        default=False,
                        help=argparse.SUPPRESS)

    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Increase verbosity of output')

    parsed_args = parser.parse_args(args)

    return parsed_args


def main(args=None):
    """ main function to run traj_analysis from command line"""

    args = sys.argv[1:] if args is None else args
    parsed_args = parse_args(args)

    data_dir = osp.realpath(parsed_args.data_dir)
    refresh = parsed_args.refresh
    parallelize = parsed_args.parallelize

    if not osp.exists(data_dir):
        raise Exception("ERROR: the passed data directory does not exist. Aborting...")

    if not osp.isdir(data_dir):
        raise Exception("ERROR: the passed data directory is not a directory. Aborting...")

    # Load config
    config = tpr.load_config(data_dir, verbose=parsed_args.verbose)

    # Check config
    mandatory_config = ["filters", "plot_config", "data_config"]
    for key in mandatory_config:
        if key not in config.keys():
            config[key] = None  # make them None, so they are initialize in traj_analysis

    # get traj_config
    traj_config = {}
    for key in ["traj_config_", "MSD_config", "scatter_config", "hist_config", "total_traj_config", "voronoi_config"]:
        if key in config.keys():
            traj_config[key] = config[key]

    # run analysis
    traj_analysis(data_dir,
                  refresh=refresh,
                  parallelize=parallelize,
                  filters=config["filters"],
                  plot_config=config["plot_config"],
                  traj_config=traj_config,
                  data_config=config["data_config"])


if __name__ == '__main__':
    main()
