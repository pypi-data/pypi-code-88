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


def map_analysis(data_dir, data=None, image=None, refresh=False, parallelize=False, filters=None,
                 plot_config=None, map_config=None, data_config=None):
    """Container method to plot a series of maps given by field_values. Manual vlim to colormap can be passed."""

    map_dir = osp.join(data_dir, 'map_analysis')
    tpr.safe_mkdir(map_dir)

    # Get image
    image = tpr.get_image(data_dir) if image is None else image

    # Get data
    data_config = tpr.make_data_config(data_dir=data_dir, export_config=False) if data_config is None else data_config
    if data is None: 
        data = tpr.get_data(data_dir, refresh=refresh, split_traj=data_config["split_traj"], set_origin_=data_config["set_origin_"], 
                            image=image, reset_dim=data_config["reset_dim"], invert_axes=data_config["invert_axes"])

    df = data['df']
    dimensions = data['dimensions']
    lengthscale = data['lengthscale']

    # Get config
    plot_config = tpl.make_plot_config(data_dir=data_dir, export_config=False) if plot_config is None else plot_config

    map_config_default = tpr.make_map_config(data_dir=data_dir, export_config=False)
    map_config = map_config_default if map_config is None else map_config

    # check that all configs are in map_config, if not load default
    for key in ["grid_param", "map_param", "scalar_fields", "vector_fields", "vector_mean"]:
        if key not in map_config.keys():
            map_config[key] = map_config_default[key]

    grid_param = map_config["grid_param"]
    map_param = map_config["map_param"]
    scalar_fields = map_config["scalar_fields"]
    vector_fields = map_config["vector_fields"]
    vector_mean = map_config["vector_mean"]

    # Filter data
    filters = tpr.init_filters(data_dir=data_dir, export_to_config=True) if filters is None else filters
    subset_analysis = filters['subset']  # how to deal with subsets
    filters_ = filters['filters_list']
    df = tpr.select_sub_data(df, filters=filters_)
    if subset_analysis == 'together':
        print("WARNING: subsets won't be plotted in different colors in maps if plotted together")
        df_list = [df]  # a single df is kept
    elif subset_analysis == 'separately':
        df_list = [df[df['subset'] == sub] for sub in df['subset'].unique()]  # a list of df filtered by subset

    # Make grid
    image_size = [image['image_size'][1], image['image_size'][0]]  # image width,image height in px
    grids = tpr.make_grid(image_size,
                          x_num=grid_param['x_num'],
                          y_num=grid_param['y_num'],
                          cell_size=grid_param['cell_size'],
                          scaled=grid_param['scaled'],
                          lengthscale=lengthscale,
                          origin=grid_param['origin'],
                          plot_grid=grid_param['plot_grid'],
                          save_plot_fn=osp.join(map_dir, 'grids{}'.format(plot_config['format'])))

    # Compute fields
    for i, df in enumerate(df_list):
        # name subset directory
        dir_name = ''
        if subset_analysis == 'separately':
            subset_name = df['subset'].values[0]
            dir_name = '_' + subset_name if subset_name != '' else ''
        dir_name_ = '{}{}'.format(len(tpr.listdir_nohidden(map_dir)) + 1, dir_name)

        print(r"Analyzing subset {}  ".format(i + 1, dir_name_))
        sub_dir = osp.join(map_dir, dir_name_)
        sub_dir = sub_dir + '_1' if osp.exists(sub_dir) else sub_dir  # dont overwrite existing dir
        tpr.safe_mkdir(sub_dir)
        
        # export data
        csv_fn = osp.join(sub_dir, 'all_data.csv')
        df.to_csv(csv_fn)
        config_dir = osp.join(sub_dir, 'config')
        tpr.safe_mkdir(config_dir)
        fn = osp.join(config_dir, 'filters.csv')
        tpr.write_dict(filters_[i], fn)
        for key in map_config.keys():
            fn = osp.join(config_dir, key + '.csv')
            tpr.write_dict(map_config[key], fn)

        # list required fields to interpolate
        all_fields = list(set(list(scalar_fields.keys()) + list(vector_fields.keys()) + list(vector_mean.keys())))
        interp_fields = [f for f in all_fields if f not in ['div', 'curl', 'v_mean', 'a_mean']]  # fields to interpolate
        vel_fields = ['v' + d for d in dimensions]
        acc_fields = ['a' + d for d in dimensions]

        if 'div' in all_fields or 'curl' in all_fields or 'v_mean' in all_fields or 'v' in vector_fields.keys():  # add all velocity fields
            for vf in vel_fields:
                if vf not in interp_fields:
                    interp_fields.append(vf)
        if 'a_mean' in all_fields or 'a' in vector_fields.keys():  # add all acceleration fields
            for af in acc_fields:
                if af not in interp_fields:
                    interp_fields.append(af)

        # compute data
        field_data = tca.interpolate_all_fields(data_dir, df, grids, field_values=interp_fields,
                                                temporal_average=map_param['temporal_average'],
                                                export_field=map_param['export_field'], outdir=sub_dir)
        if 'div' in all_fields or 'curl' in all_fields:
            field_data = tca.compute_all_div_curl(data_dir, df, field_data, lengthscale,
                                                  export_field=map_param['export_field'], outdir=sub_dir)
        for mf in ['v_mean', 'a_mean']:
            if mf in all_fields:
                field_data = tca.compute_all_vector_mean(data_dir, df, field_data, mf,
                                                         dimensions=vector_mean[mf]['dimensions'],
                                                         export_field=map_param['export_field'], outdir=sub_dir)

        # plot data
        scalar_fields_ = {**scalar_fields, **vector_mean}  # merge scalar data in one single dict
        for field in scalar_fields_.keys():
            plot_dir = osp.join(sub_dir, field)
            tpr.safe_mkdir(plot_dir)
            map_param_ = dict(map_param)
            map_param_['vlim'] = scalar_fields_[field]['vlim']
            map_param_['cmap'] = scalar_fields_[field]['cmap']
            tpl.plot_all_scalar_fields(data_dir, df, field_data, field, image=image, map_param=map_param_,
                                       plot_dir=plot_dir, plot_config=plot_config, dont_print_count=False)
        for field in vector_fields.keys():
            plot_dir = osp.join(sub_dir, field)
            tpr.safe_mkdir(plot_dir)
            map_param_ = dict(map_param)
            map_param_['vlim'] = vector_fields[field]['vlim']
            tpl.plot_all_vector_fields(data_dir, df, field_data, field, image=image, plot_on_field=vector_fields[field],
                                       dim=3, map_param=map_param_, plot_dir=plot_dir, plot_config=plot_config,
                                       dont_print_count=False)

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
            config[key] = None

    # get map_config
    map_config = {}
    for key in ["grid_param", "map_param", "scalar_fields", "vector_fields", "vector_mean"]:
        if key in config.keys():
            map_config[key] = config[key]

    # run analysis
    map_analysis(data_dir,
                 refresh=refresh,
                 parallelize=parallelize,
                 filters=config["filters"],
                 plot_config=config["plot_config"],
                 map_config=map_config,
                 data_config=config["data_config"])


if __name__ == '__main__':
    main()
