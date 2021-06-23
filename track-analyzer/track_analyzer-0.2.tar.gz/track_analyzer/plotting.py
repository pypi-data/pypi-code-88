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

import sys
import os.path as osp
import datetime
import itertools
import copy

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
from skimage import io
import seaborn as sns
from scipy import stats
from scipy.spatial import voronoi_plot_2d
import napari
import tifffile as tifff

from track_analyzer import calculate as tca
from track_analyzer import prepare as tpr


def make_plot_config(data_dir=None, export_config=False):
    """ Generate config parameters for plotting """

    # Plotting config
    plot_config = {'figsize': (5, 5),
                   'dpi': 300,
                   'color_list': [c['color'] for c in list(plt.rcParams['axes.prop_cycle'])] + sns.color_palette("Set1",
                                                                                                                 n_colors=9,
                                                                                                                 desat=.5),
                   'format': '.png',
                   'despine': True,
                   'logx': False,
                   'logy': False,
                   'invert_yaxis': True,
                   'export_data_pts': True
                   }

    if export_config:
        if data_dir is None:
            raise Exception("ERROR: no data_dir given")
        else:
            config_dir = osp.join(data_dir, 'config')
            tpr.safe_mkdir(config_dir)

        fn = osp.join(config_dir, 'plot_config.csv')
        tpr.write_dict(plot_config, fn)

    return plot_config


def stack_max_proj(image_fn, z_dim, t_dim=None):
    """Perform a maximum projection of a 3D or 4D image. The dimension of z and time are given by z_dim and t_dim. """
    im = io.imread(image_fn)

    if t_dim is None:
        new_im = np.zeros((im.shape[1], im.shape[2]), 'uint8')
        new_im = np.max(im, axis=0)
    else:
        if t_dim == 1 and z_dim == 0:  # if the z dimension is along dimension 0 transpose
            im_ = im.transpose(1, 0, 2, 3)
        new_im = np.zeros((im.shape[0], im.shape[2], im.shape[3]), 'uint8')
        for i in range(im.shape[0]):
            new_im[i] = np.max(im[i], axis=0)
    fn, file_ext = osp.splitext(image_fn)
    out_fn = fn + '_maxproj.tif'
    tifff.imsave(out_fn, new_im)


def plot_cmap(plot_dir, label, cmap, vmin, vmax, plot_config=None):
    """ Plot colormap given by cmap with boundaries vmin and vmax."""

    plot_config = make_plot_config() if plot_config is None else plot_config

    fig = plt.figure(figsize=(8, 3))
    ax = fig.add_axes([0.05, 0.80, 0.9, 0.15])
    norm = plt.Normalize(vmin=vmin, vmax=vmax)
    cb = mpl.colorbar.ColorbarBase(ax, cmap=plt.get_cmap(cmap), norm=norm, orientation='horizontal')
    ax.tick_params(labelsize=16)
    cb.set_label(label=label, size=24)
    filename = osp.join(plot_dir, 'colormap.png')
    fig.savefig(filename, dpi=plot_config['dpi'], bbox_inches='tight')
    plt.close(fig)


def plot_traj(df, frame, data_dir, groups=None, image={'image_fn': None, 't_dim': None, 'z_dim': None}, plot_dir=None,
              show_plot=False, dim=3, plot_config=None,traj_parameters=None):
    """ 
    Plot all trajectories of a given frame on an image if traj_parameters['no_bkg'] is False and an image is given.
    Plots can be color coded z value, by groups, or with random colors (traj_parameters['color_code']='z' or 'group' or 'random' or 'none')
    The trajectory path can be removed to keep only the dots if traj_parameters['traj'] is False.
    It can be plotted in 3D with plot3D, elevation and angle set the 3D view
    """
    sys.stdout.write("\033[K")  # go back to previous line
    print('plotting frame {}'.format(int(frame)), flush=True, end='\r')

    # get config parameters
    plot_config = make_plot_config() if plot_config is None else plot_config
    if traj_parameters is None:
        traj_parameters = {'color_code': 'z',  # color code: 'z', 'ROI', 'random', 'none'
                            'cmap': 'plasma',  # colormap to be used if color_code is 'z'
                            'cmap_lim': None,
                            # pass custom colormap limits (useful for getting coherent boundaries for all frames)
                            'show_tail': True,  # show trajectory tail
                            'hide_labels': True,  # hide trajectory ID
                            'lab_size': 6,  # label size in points if hide_labels is False
                            'no_bkg': False,  # don't show background image if an image is passed
                            'size_factor': 1.,  # to multiply the default size of markers and lines
                            'show_axis': False,  # to show the plot axes (by default just image)
                            'plot3D': False,  # plot in 3D  !! Not supportes anymore !!
                            'elevation': None,  # 3D paramater !! Not supportes anymore !!
                            'angle': None,  # 3D paramater !! Not supportes anymore !!
                            'subset_order': None,  # if color code is ROI, order of ROI in color cycle
                            }


    color_list = plot_config['color_list']
    show_tail = traj_parameters['show_tail']
    color_code = traj_parameters['color_code']
    cmap = traj_parameters['cmap']
    hide_labels = traj_parameters['hide_labels']
    no_bkg = traj_parameters['no_bkg']
    size_factor = traj_parameters['size_factor']
    plot3D = traj_parameters['plot3D']
    cmap_lim = traj_parameters['cmap_lim']
    show_axis = traj_parameters['show_axis']
    elevation = traj_parameters['elevation']
    angle = traj_parameters['angle']
    lab_size = traj_parameters['lab_size']
    invert_yaxis = plot_config['invert_yaxis']


    # get image size
    info = tpr.get_info(data_dir)
    image_size = [info['image_width'], info['image_height']]

    # traj size
    ms_ref = plt.rcParams['lines.markersize']
    ms = ms_ref * size_factor
    lw = ms / 8

    if plot_dir is None:
        plot_dir = osp.join(data_dir, 'traj')
        tpr.safe_mkdir(plot_dir)

    # 3D PLOTTING. not supported anymore
    # if plot3D:
    #     fig = plt.figure()
    #     ax = fig.add_subplot(111, projection='3d')
    #     xmin, xmax, ymin, ymax = ax.axis('off')
    # else:
    # Get background image
    bkgd = tpr.get_background(image=image, frame=frame, df=df, no_bkg=no_bkg,
                        image_size=image_size,axis_on=show_axis, dpi=plot_config['dpi'])
    fig = bkgd['fig']
    ax = bkgd['ax']
    xmin = bkgd['xmin']
    ymin = bkgd['ymin']
    xmax = bkgd['xmax']
    ymax = bkgd['ymax']
    no_bkg = bkgd['no_bkg']

    # get frame dataframe
    groups = df.groupby('frame') if groups is None else groups
    group = groups.get_group(frame).reset_index(drop=True)

    #### plotting positions as dots
    x = group['x'].values
    y = group['y'].values
    z = group['z_scaled'].values if dim == 3 else np.zeros(group.shape[0])
    t = group['t'].values

    ## color code
    if color_code == "z" or color_code == "t":
        if cmap_lim is None:
            if color_code == "z":
                if dim == 3:
                    cmap_lim = [df['z_scaled'].min(), df['z_scaled'].max()]
                else:
                    cmap_lim = [0, 0]
            elif color_code == "t":
                cmap_lim = [df['t'].min(), df['t'].max()]
        if color_code == "z":
            colors = tpr.get_cmap_color(z, cmap, vmin=cmap_lim[0], vmax=cmap_lim[1])
        elif color_code == "t":
            colors = tpr.get_cmap_color(t, cmap, vmin=cmap_lim[0], vmax=cmap_lim[1])

    elif color_code == "ROI":
        # check there are subsets in df
        if 'subset' in group.columns:
            colors = [color_list[i % len(color_list)] for i in group['subset_order'].values] # if too many colors repeat cycle
        else:
            colors = color_list[0]  # if color_coded by group but there's none, use only one color

    elif color_code == "random":
        colors = [color_list[i % len(color_list)] for i in group['track'].values]

    elif color_code == "none":
        colors = color_list[0]

    else:
        colors = color_list[0]

    # plotting labels
    if not hide_labels:
        group['track_lab'] = group['track'].map(lambda num: '{}'.format(int(num)))
        color_ = 'k' if no_bkg else 'w'
        ax.text(x, y, group['track_lab'].values, fontsize=lab_size, color=color_)

    # plot points
    ax.scatter(x, y, s=ms, color=colors)

    #### plotting trajectories as lines
    if show_tail:
        track_list = group['track'].values
        track_groups = df.groupby(['track'])
        for track in track_list:
            traj = tpr.get_traj(track_groups, track, max_frame=frame)
            traj_length = traj.shape[0]
            X = traj['x'].values
            Y = traj['y'].values
            Z = traj['z_scaled'].values if dim == 3 else np.zeros(traj.shape[0])
            t = traj['t'].values

            ## color code
            if color_code == "z":
                colors = tpr.get_cmap_color(Z, cmap, vmin=cmap_lim[0], vmax=cmap_lim[1])
            elif color_code == "t":
                colors = tpr.get_cmap_color(t, cmap, vmin=cmap_lim[0], vmax=cmap_lim[1])
            elif color_code == "ROI":
                if 'subset' in traj.columns:
                    colors = color_list[traj['subset_order'].values[0] % len(color_list)]
                else:
                    colors = color_list[0]  # if color_coded by group but there's none, use only one color
            elif color_code == "random":
                colors = color_list[track % len(color_list)]
            elif color_code == "none":
                colors = color_list[0]
            else:
                colors = color_list[0]

            if traj_length > 1:
                if color_code == "z" or color_code == "t":
                    for j in range(1, traj_length):
                        ax.plot([X[j - 1], X[j]], [Y[j - 1], Y[j]], lw=lw, ls='-', color=colors[j])
                else:
                    ax.plot(X, Y, lw=lw, ls='-', color=colors)

    if invert_yaxis:
        ax.axis([xmin, xmax, ymax, ymin])

    if show_plot:
        fig.show()
        return

    if show_axis:
        fig.tight_layout()

    filename = osp.join(plot_dir, '{:04d}{}'.format(int(frame), plot_config['format']))
    fig.savefig(filename, dpi=plot_config['dpi'])
    plt.close(fig)


def plot_scalar_field(data_dir, df, data, field, frame, image={'image_fn': None, 't_dim': None, 'z_dim': None},
                      map_param={'no_bkg': False, 'vlim': None, 'show_axis': False, 'cmap': 'plasma'},
                      plot_dir=None, plot_config=None, dont_print_count=False, dont_save=False):
    """Plot scalar field as colormap. The data needs to be generated before. """

    if not dont_print_count:
        sys.stdout.write("\033[K")  # go back to previous line
        print('plotting {} {}'.format(field, int(frame)), flush=True, end='\r')

    if plot_dir is None:
        plot_dir = osp.join(data_dir, field)
    tpr.safe_mkdir(plot_dir)

    # misc param

    plot_config = make_plot_config() if plot_config is None else plot_config
    no_bkg = map_param['no_bkg']
    show_axis = map_param['show_axis']
    cmap = map_param['cmap']
    vlim = map_param['vlim']
    info = tpr.get_info(data_dir)
    image_size = [info['image_width'], info['image_height']]
    invert_yaxis = plot_config['invert_yaxis']
    cmap = copy.copy(plt.get_cmap(cmap))  # make a shallow copy of cmap as modifying Matplotlib colormaps is deprecated

    # extract data
    X = data[frame]['X']
    Y = data[frame]['Y']
    val = data[frame][field]

    # #remove edges for div and curl
    # if field=='div' or field=='curl':
    #     X=X[1:-1,1:-1]
    #     Y=Y[1:-1,1:-1]

    if image['image_fn'] is None:
        no_bkg = True

    bkgd = tpr.get_background(image=image, frame=frame, df=df, no_bkg=no_bkg,
                            image_size=image_size, axis_on=show_axis,dpi=plot_config['dpi'])
    fig = bkgd['fig']
    ax = bkgd['ax']
    xmin = bkgd['xmin']
    ymin = bkgd['ymin']
    xmax = bkgd['xmax']
    ymax = bkgd['ymax']
    no_bkg = bkgd['no_bkg']

    val_masked = np.ma.array(val, mask=np.isnan(val))
    [vmin, vmax] = [val_masked.min(), val_masked.max()] if vlim is None else vlim
    cmap.set_bad('w', alpha=0)  # set NAN transparent

    # shading=nearest so color value is centered on grid points
    # for more info on pcolormesh behavior, see https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolormesh_grids.html#sphx-glr-gallery-images-contours-and-fields-pcolormesh-grids-py
    C = ax.pcolormesh(X, Y, val_masked, cmap=cmap, alpha=0.5, vmin=vmin, vmax=vmax, shading='nearest')  

    if show_axis:
        ax.grid(False)
        ax.patch.set_visible(False)
        fig.set_tight_layout(True)

    if invert_yaxis:
        ax.axis([xmin, xmax, ymax, ymin])

    if not dont_save:
        filename = osp.join(plot_dir, field + '_{:04d}.png'.format(int(frame)))
        fig.savefig(filename, dpi=plot_config['dpi'])

    return fig, ax


def plot_vector_field(data_dir, df, data, field, frame, plot_on_field=None, dim=3,
                      image={'image_fn': None, 't_dim': None, 'z_dim': None},
                      map_param={'no_bkg': False, 'vlim': None, 'show_axis': False, 'cmap': 'plasma',
                                 'size_factor': 1},
                      plot_dir=None, plot_config=None, dont_print_count=False):
    """ Plot vector field"""

    if not dont_print_count:
        sys.stdout.write("\033[K")  # go back to previous line
        print('plotting {} {}'.format(field, int(frame)), flush=True, end='\r')

    if plot_dir is None:
        plot_dir = osp.join(data_dir, field)
    tpr.safe_mkdir(plot_dir)

    # misc param
    plot_config = make_plot_config() if plot_config is None else plot_config
    no_bkg = map_param['no_bkg']
    show_axis = map_param['show_axis']
    # cmap=map_param['cmap']
    # vlim=map_param['vlim']
    size_factor = map_param['size_factor']
    info = tpr.get_info(data_dir)
    image_size = [info['image_width'], info['image_height']]
    invert_yaxis = plot_config['invert_yaxis']

    # import image
    if image['image_fn'] is None:
        no_bkg = True

    no_plot_on_field = False
    if plot_on_field is not None:
        if plot_on_field['plot_on'] is not None:
            map_param_ = map_param
            map_param_['cmap'] = plot_on_field['cmap']
            map_param_['vlim'] = plot_on_field['vlim']
            dim = 2  # to ensure that arrows are plotted in black and the z data is not use
            fig, ax = plot_scalar_field(data_dir, df, data, plot_on_field['plot_on'], frame, image=image,
                                        map_param=map_param_, plot_dir=plot_dir, plot_config=None,
                                        dont_print_count=True, dont_save=True)
            invert_yaxis = False  # to ensure it's not inverted a second time
        else:
            no_plot_on_field = True
    else:
        no_plot_on_field = True

    if no_plot_on_field:
        bkgd = tpr.get_background(image=image, frame=frame, df=df, no_bkg=no_bkg,
                                                                     image_size=image_size, axis_on=show_axis,
                                                                     dpi=plot_config['dpi'])
        fig = bkgd['fig']
        ax = bkgd['ax']
        xmin = bkgd['xmin']
        ymin = bkgd['ymin']
        xmax = bkgd['xmax']
        ymax = bkgd['ymax']
        no_bkg = bkgd['no_bkg']

    # extract data
    dimensions = ['x', 'y', 'z'] if dim == 3 else ['x', 'y']
    vdata = [field + d for d in dimensions]  # eg ['vx','vy'] or ['ax','ay','az']
    val = [data[frame]['X'], data[frame]['Y']] + [data[frame][vd] for vd in vdata]  # eg ['X','Y','vx','vy']

    # norm=plt.Normalize(vlim[0],vlim[1]) if vlim is not None else None
    # Q=ax.quiver(*val,units='inches',cmap=cmap,norm=norm,width=0.005)
    Q = ax.quiver(*val, units='inches', width=0.005 * size_factor, angles='xy')

    if show_axis:
        ax.grid(False)
        ax.patch.set_visible(False)
        fig.set_tight_layout(True)

    if invert_yaxis:
        ylim = ax.get_ylim()
        ax.set_ylim(ylim[1], ylim[0])

    filename = osp.join(plot_dir, 'vector_' + field + '_{:04d}.png'.format(int(frame)))
    fig.savefig(filename, dpi=plot_config['dpi'])
    plt.close(fig)


def plot_Voronoi(data_dir, df, frame, data, show_local_area=True,
                 image={'image_fn': None, 't_dim': None, 'z_dim': None},
                 map_param={'no_bkg': False, 'vlim': None, 'show_axis': False, 'cmap': 'plasma', 'size_factor': 1},
                 plot_dir=None, plot_config=None, dont_print_count=False):
    """
    Plot Voronoi tesselation and local area in 2D only.
    :param data_dir:
    :param df:
    :param frame:
    :param data:
    :param show_local_area:
    :param image:
    :param map_param:
    :param plot_dir:
    :param plot_config:
    :param dont_print_count:
    :return:
    """

    if not dont_print_count:
        sys.stdout.write("\033[K")  # go back to previous line
        print('plotting {} {}'.format('voronoi', int(frame)), flush=True, end='\r')

    if plot_dir is None:
        plot_dir = osp.join(data_dir, 'voronoi')
    tpr.safe_mkdir(plot_dir)

    # misc param
    plot_config = make_plot_config() if plot_config is None else plot_config
    no_bkg = map_param['no_bkg']
    show_axis = map_param['show_axis']
    cmap = map_param['cmap']
    vlim = map_param['vlim']
    info = tpr.get_info(data_dir)
    image_size = [info['image_width'], info['image_height']]
    invert_yaxis = plot_config['invert_yaxis']

    # import image
    if image['image_fn'] is None:
        no_bkg = True

    bkgd = tpr.get_background(image=image, frame=frame, df=df, no_bkg=no_bkg,
                            image_size=image_size, axis_on=show_axis, dpi=plot_config['dpi'])
    fig = bkgd['fig']
    ax = bkgd['ax']
    xmin = bkgd['xmin']
    ymin = bkgd['ymin']
    xmax = bkgd['xmax']
    ymax = bkgd['ymax']
    no_bkg = bkgd['no_bkg']

    # plot tesselation
    vor = data[frame]['vor']
    if vor is not None:
        voronoi_plot_2d(vor, show_points=False, show_vertices=False, ax=ax)

        # plot local area on top
        if show_local_area:
            areas = data[frame]['areas']
            if areas is not None:
                for pt_id, reg_num in enumerate(vor.point_region):
                    indices = vor.regions[reg_num]
                    area = areas[pt_id]
                    if not np.isnan(area):
                        color = tpr.get_cmap_color(area, cmap, vmin=vlim[0], vmax=vlim[1])
                        ax.fill(*zip(*vor.vertices[indices]), color=color, alpha=0.5)

    if show_axis:
        ax.grid(False)
        ax.patch.set_visible(False)
        fig.set_tight_layout(True)

    if invert_yaxis:
        ylim = ax.get_ylim()
        ax.set_ylim(ylim[1], ylim[0])

    filename = osp.join(plot_dir, 'voronoi_{:04d}.png'.format(int(frame)))
    fig.savefig(filename, dpi=plot_config['dpi'])
    plt.close(fig)


def plot_hist_persistence_length(data_dir, track_groups, tracks, minimal_traj_length=40, normalize=True, dim=3,
                                 plot_config=None):
    plt.close('all')

    plot_config = make_plot_config() if plot_config is None else plot_config

    pers_length_dict = {}
    for track in tracks:
        traj = tpr.get_traj(track_groups, track)
        traj_length, c = traj.shape
        if traj_length > minimal_traj_length:
            pers_length_dict[track] = tca.get_obj_persistence_length(track_groups, track, traj, dim=dim)

    pers_lengths = pd.Series(pers_length_dict)
    fig, ax = plt.subplots()
    if normalize:
        pers_lengths.plot.hist(weights=np.ones_like(pers_lengths * 100) / len(pers_lengths), ax=ax)
        ax.set_ylabel('trajectories proportion ')
    else:
        pers_lengths.plot.hist(ax=ax)
        ax.set_ylabel('trajectories count')
    ax.set_xlabel(r'persistence length ($\mu m$) ')
    filename = osp.join(data_dir, 'persistence_lenght.svg')
    fig.savefig(filename, dpi=plot_config['dpi'], bbox_inches='tight')


def plot_MSD(data_dir, track, track_groups=None, df=None, df_out=None, fit_model="biased_diff", dim=2, save_plot=True,
             print_traj_info=True, frame_subset=None, fitrange=None, plot_dir=None, plot_config=None, logx=True,
             logy=True):
    """Compute MSD of a trajectory and fit it with a random walk model. If df_out is given, save the output of a fit. If save_plot is False, don't plot the MSD (useful for large number of tracks to analyze)."""

    plot_config = make_plot_config() if plot_config is None else plot_config
    color_list = plot_config['color_list']

    if plot_dir is None:
        plot_dir = osp.join(data_dir, 'MSD')
    tpr.safe_mkdir(plot_dir)

    data = tpr.get_data(data_dir)
    timescale = data['timescale']
    if df is None:
        df = data['df']

    if track_groups is None:
        track_groups = df.groupby(['track'])
    traj = tpr.get_traj(track_groups, track)

    if frame_subset is not None:
        ind = ((traj['frame'] >= frame_subset[0]) & (traj['frame'] <= frame_subset[1]))
        traj = traj[ind]

    if dim == 2:
        dimensions = ['x_scaled', 'y_scaled']
    elif dim == 3:
        dimensions = ['x_scaled', 'y_scaled', 'z_scaled']

    # compute and fit MSD
    msd = tca.compute_msd(traj, timescale, dimensions)
    if fit_model is not None:
        results = tca.fit_msd(msd, mean_vel=traj['v'].mean(), dim=dim, model=fit_model, fitrange=fitrange)
        if df_out is not None and results['success']:
            ind = df_out['track'] == track
            for param in results['param'].keys():
                df_out.loc[ind, param] = results['param'][param]
            df_out.loc[ind, 'redchi'] = results['redchi']

    if save_plot:
        info = tpr.get_info(data_dir)
        D_unit = tpr.make_param_label('D', l_unit=info['length_unit'], t_unit=info['time_unit'], only_unit=True)

        fig, ax = plt.subplots(1, 1, figsize=plot_config['figsize'])
        msd.plot.scatter(x="tau", y="msd", logx=logx, logy=logy, ax=ax)
        if fit_model is not None:
            if results['success']:
                fitted_df = results['fitted_df']
                fitted_df.plot(x="tau", y="fitted", logx=logx, logy=logy, ax=ax)
                if fit_model == 'biased_diff':
                    title_ = r'D={:0.3f} {:}, $\chi^2$={:0.3f}'.format(results['param']['D'], D_unit, results['redchi'])
                elif fit_model == 'PRW':
                    title_ = r'P={:0.3f} {:}, $\chi^2$={:0.3f}'.format(results['param']['P'], info['time_unit'],
                                                                       results['redchi'])
                elif fit_model == 'pure_diff':
                    title_ = r'D={:0.3f} {:}, $\chi^2$={:0.3f}'.format(results['param']['D'], D_unit, results['redchi'])
                ax.set_title(title_)
        ax.set_xlabel('lag time ({})'.format(info['time_unit']))
        ax.set_ylabel(r'MSD ({})'.format(D_unit))
        if plot_config['despine']:
            sns.despine(fig)
        fig.savefig(osp.join(plot_dir, '{}{}'.format(int(track), plot_config['format'])), dpi=plot_config['dpi'],
                    bbox_inches='tight')
        plt.close(fig)

    return msd[['tau', 'msd']]


def plot_param_vs_param(data_dir, x_param, y_param, df=None, hue=None, hue_order=None, set_axis_lim=None,
                        plot_config=None,
                        plot_dir=None, prefix='', suffix=''):
    """Plot a parameter of df (y_param) against another parameter (x_param). Optional: compare datasets with hue as datasets identifier."""

    plot_config = make_plot_config() if plot_config is None else plot_config
    color_list = plot_config['color_list']
    export_data_pts = plot_config['export_data_pts']

    if df is None:
        data = tpr.get_data(data_dir, refresh=refresh, transform_coord=transform_coord)
        df = data['df']

    if plot_dir is None:
        plot_dir = data_dir

    info = tpr.get_info(data_dir)
    x_lab = tpr.make_param_label(x_param, l_unit=info['length_unit'], t_unit=info['time_unit'])
    y_lab = tpr.make_param_label(y_param, l_unit=info['length_unit'], t_unit=info['time_unit'])

    if hue is not None:
        df[hue] = df[hue].astype('category')  # make sure that sns.scatterplot does not use the continuous colormap

    fig, ax = plt.subplots(1, 1, figsize=plot_config['figsize'])
    # sns.scatterplot(x=x_param,y=y_param,ax=ax,facecolors='none',edgecolor=color_list[0],data=df)
    sns.scatterplot(x=x_param, y=y_param, ax=ax, hue=hue, hue_order=hue_order, data=df)
    ax.set_xlabel(x_lab)
    ax.set_ylabel(y_lab)
    if set_axis_lim is not None:
        ax.set_xlim(set_axis_lim[0], set_axis_lim[1])
        ax.set_ylim(set_axis_lim[2], set_axis_lim[3])
    else:  # recalculate because sometimes matplotlib auto limit fails
        xlim_ = [df[x_param].min(), df[x_param].max()]
        ylim_ = [df[y_param].min(), df[y_param].max()]
        xlim_ = [xlim_[0] - 0.05 * (xlim_[1] - xlim_[0]), xlim_[1] + 0.05 * (xlim_[1] - xlim_[0])]
        ylim_ = [ylim_[0] - 0.05 * (ylim_[1] - ylim_[0]), ylim_[1] + 0.05 * (ylim_[1] - ylim_[0])]
        ax.set_xlim(xlim_[0], xlim_[1])
        ax.set_ylim(ylim_[0], ylim_[1])

    if plot_config['despine']:
        sns.despine(fig)

    filename = osp.join(plot_dir, prefix + '{}_vs_{}{}{}'.format(y_param, x_param, suffix, plot_config['format']))
    fig.savefig(filename, dpi=plot_config['dpi'], bbox_inches='tight')
    plt.close(fig)

    if export_data_pts:
        cols = [x_param, y_param, hue] if hue is not None else [x_param, y_param]
        fn = osp.join(plot_dir, prefix + '{}_vs_{}{}{}'.format(y_param, x_param, suffix, '.csv'))
        df[cols].to_csv(fn)


def plot_param_hist(data_dir, param, df=None, hue=None, hue_order=None, hist=True, kde=True,
                    plot_config=None,
                    plot_dir=None, prefix='', suffix=''):
    """Plot a parameter histogram. Optional: compare datasets with hue as datasets identifier."""

    plot_config = make_plot_config() if plot_config is None else plot_config
    color_list = plot_config['color_list']
    figsize = plot_config['figsize']
    export_data_pts = plot_config['export_data_pts']

    if df is None:
        data = tpr.get_data(data_dir)
        df = data['df']

    if plot_dir is None:
        plot_dir = data_dir

    info = tpr.get_info(data_dir)
    param_label = tpr.make_param_label(param, l_unit=info['length_unit'], t_unit=info['time_unit'])

    # make sure data is float and finite
    df[param] = df[param].astype(np.float)
    df = df[np.isfinite(df[param])]

    kind = "hist" if hist else "kde"
    g = sns.displot(data=df, x=param, hue=hue, kind=kind, kde=kde)
    fig = g.fig
    ax = g.ax
    fig.set_size_inches(figsize[0], figsize[1])
    ax.set_xlabel(param_label)

    if plot_config['despine']:
        sns.despine(fig)

    filename = osp.join(plot_dir, prefix + '{}_hist{}{}'.format(param, suffix, plot_config['format']))
    fig.savefig(filename, dpi=plot_config['dpi'], bbox_inches='tight')
    plt.close(fig)

    if export_data_pts:
        cols = [param, hue] if hue is not None else param
        fn = osp.join(plot_dir, prefix + '{}_hist{}{}'.format(param, suffix, '.csv'))
        df[cols].to_csv(fn)


def plot_param_boxplot(data_dir, df, x_param, param, order=None, hue=None, save_stat=False, hue_order=None,
                       boxplot=True, swarmplot=True, plot_config=None, plot_dir=None, prefix='', suffix='',
                       leg_lab=None):
    """Plot boxplot between categories (given by x_param). Sub-categories can be plotted too (given by hue). A ttest can be performed has well"""

    plot_config = make_plot_config() if plot_config is None else plot_config
    color_list = plot_config['color_list']
    figsize = plot_config['figsize']
    export_data_pts = plot_config['export_data_pts']

    if df is None:
        data = tpr.get_data(data_dir)
        df = data['df']

    if plot_dir is None:
        plot_dir = data_dir

    info = tpr.get_info(data_dir)
    param_label = tpr.make_param_label(param, l_unit=info['length_unit'], t_unit=info['time_unit'])

    # plotting
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    if hue is None:
        width = 0.5
        color = color_list[0]
        palette = [(0.25, 0.25, 0.25), (0.25, 0.25, 0.25)]
        lw = 0
    else:
        width = 0.8
        color = None
        palette = color_list
        lw = 1
    if boxplot:
        sns.boxplot(data=df, x=x_param, y=param, ax=ax, order=order, width=width, hue=hue, hue_order=hue_order,
                    color=color)
    if swarmplot:
        sns.swarmplot(data=df, x=x_param, y=param, ax=ax, order=order, size=8, linewidth=lw, dodge=True,
                      palette=palette, hue=hue, hue_order=hue_order)
    if hue is not None:
        handles, labels = ax.get_legend_handles_labels()
        if leg_lab is not None:
            labs = leg_lab
        else:
            labs = labels[0:len(handles) // 2]
        ax.legend(handles[0:len(handles) // 2], labs, frameon=False)
    ax.ticklabel_format(axis='y', style='sci', scilimits=(-2, 3))
    ax.get_yaxis().get_major_formatter().set_useMathText(True)
    ax.set_ylabel(param_label)
    ax.set_xlabel(x_param)

    if plot_config['despine']:
        sns.despine(fig)

    filename_basis = osp.join(plot_dir, prefix + '{}_box{}'.format(param, suffix))
    fig.savefig(filename_basis + plot_config['format'], dpi=plot_config['dpi'], bbox_inches='tight')
    plt.close(fig)

    # stat
    if save_stat and x_param is not None:
        x_list = df[x_param].unique() if order is None else order
        if hue is not None:
            hue_list = df[hue].unique() if hue_order is None else hue_order
            ind = pd.MultiIndex.from_product([x_list, hue_list], names=[x_param, hue])
            df_mean = pd.DataFrame(index=ind, columns=['mean', 'std', 'n'])
            df_pval = pd.DataFrame(index=ind, columns=hue_list)
            for xp in x_list:
                subdf = df[df[x_param] == xp]
                data_dict = {}
                for h in hue_list:
                    sub_nonan = subdf[subdf[hue] == h][param].dropna()
                    data_dict[h] = sub_nonan.values
                    df_mean.loc[(xp, h), :] = [np.mean(data_dict[h]), np.std(data_dict[h]), data_dict[h].shape[0]]
                pairs = list(itertools.combinations(data_dict.keys(), 2))
                for p in pairs:
                    ttest_ = stats.ttest_ind(data_dict[p[0]], data_dict[p[1]], equal_var=False)
                    df_pval.loc[(xp, p[0]), p[1]] = ttest_.pvalue

        else:
            df_mean = pd.DataFrame(index=x_list, columns=['mean', 'std', 'n'])
            df_pval = pd.DataFrame(index=x_list, columns=x_list)
            data_dict = {}
            for xp in x_list:
                sub_nonan = df[df[x_param] == xp][param].dropna()
                data_dict[xp] = sub_nonan.values
                df_mean.loc[xp, :] = [np.mean(data_dict[xp]), np.std(data_dict[xp]), data_dict[xp].shape[0]]

            pairs = list(itertools.combinations(data_dict.keys(), 2))
            for p in pairs:
                ttest_ = stats.ttest_ind(data_dict[p[0]], data_dict[p[1]], equal_var=False)
                df_pval.loc[p[0], p[1]] = ttest_.pvalue

        df_mean.to_csv(filename_basis + '_mean.csv')
        df_pval.to_csv(filename_basis + '_pvalue.csv')

    if export_data_pts:
        cols = [x_param, param, hue] if hue is not None else [x_param, param]
        df[cols].to_csv(filename_basis + '.csv')


#### PLOT_ALL methods

def view_traj(df, image=None, z_step=1):
    """
    View trajectories on a Napari viewer.
    Trajectories can be viewed on the original passed by image
    :param df: dataframe of trajectories
    :type df: pandas.DataFrame
    :param image: image dict returned by prepare.get_image()
    :type image: dict
    :param z_step:
    :type z_step: float or None
    """

    with napari.gui_qt():
        axis_labels = ['t', 'z', 'x', 'y'] if 'z' in df.columns else ['t', 'x', 'y']
        viewer = napari.Viewer(axis_labels=axis_labels)

        # if there is an image to plot on
        if image is not None:
            if image['image_fn'] is not None:
                im = io.imread(image['image_fn'])

                # if 3D data
                if 'z' in df.columns:
                    cols = ['frame', 'z', 'y', 'x']
                    if image['z_dim'] is None:
                        print("WARNING: you have 3D tracking data but your image is not a z-stack, for optimal 3D "
                              "viewing, use a z-stack")
                        viewer.add_image(im, name='image')
                    else:
                        z_step_ = 1 if z_step is None else z_step  # in case z_step not given set it to 1
                        viewer.add_image(im, name='image', scale=(1, z_step_, 1, 1))
                else:
                    cols = ['frame', 'y', 'x']
                    viewer.add_image(im, name='image')
        else:
            cols = ['frame', 'z', 'y', 'x'] if 'z' in df.columns else ['frame', 'y', 'x']

        df = df.sort_values(by=['track', 'frame'])  # napari track layer requires data to be sorted by ID then frame

        points = df[cols].values
        tracks = df[['track'] + cols].values

        properties = {'time': df['t'].values, 'velocity': df['v'].values, 'acceleration': df['a'].values}
        if 'z' in df.columns:
            properties['z'] = df['z'].values

        viewer.add_points(points, name='objects', size=1, opacity=0.3)
        viewer.add_tracks(tracks, properties=properties, name='trajectories')


def plot_all_traj(data_dir, df, image={'image_fn': None, 't_dim': None, 'z_dim': None}, parallelize=False, dim=3,
                  plot_dir=None,
                  traj_parameters={'traj': True, 'color_code': 'z', 'hide_labels': True, 'lab_size': 6, 'no_bkg': False,
                                   'size_factor': 1., 'plot3D': False, 'cmap_lim': None, 'show_axis': False,
                                   'elevation': None, 'angle': None, 'cmap': 'plasma'},
                  plot_config=None):
    """Plot traj for all frames"""

    if plot_dir is None:
        plot_dir = osp.join(data_dir, 'traj')
    else:
        plot_dir = osp.join(plot_dir, 'traj')

    tpr.safe_mkdir(plot_dir)

    info = tpr.get_info(data_dir)
    
    plot_config = make_plot_config() if plot_config is None else plot_config

    # color map
    color_code = traj_parameters['color_code']
    if traj_parameters['cmap_lim'] is None:
        if color_code == "z":
            if dim == 3:
                traj_parameters['cmap_lim'] = [df['z_scaled'].min(), df['z_scaled'].max()]
            else:
                traj_parameters['cmap_lim'] = [0, 0]
        elif color_code == "t":
            traj_parameters['cmap_lim'] = [df['t'].min(), df['t'].max()]

    if color_code == "z" or color_code == "t":
        param = "z_scaled" if color_code == 'z' else color_code
        label = tpr.make_param_label(param, l_unit=info["length_unit"], t_unit=info["time_unit"])
        plot_cmap(plot_dir, label, traj_parameters['cmap'], traj_parameters['cmap_lim'][0],
                  traj_parameters['cmap_lim'][1])
    
    # make a colmuns of indices to be used for color_cylce
    elif color_code == "ROI": 
        subset_order = traj_parameters['subset_order']
        if 'subset' in df.columns:
            # check subset order
            if subset_order is None:
                subset_order = df['subset'].unique()
            else: 
                for sub in df['subset'].unique():
                    if sub not in subset_order: # if missing subset in subset_oder, adding it
                        subset_order.append(sub)
            subset_order = list(subset_order)  # convert to list to use index method
            df['subset_order'] = df['subset'].apply(lambda s: subset_order.index(s))  # column with indices in subset_order

    #    # ensure 'z' is not color code for 2D data
    #    if dim == 2 and traj_parameters['color_code'] == 'z':
    #        traj_parameters['color_code'] == 'random'

    if parallelize:
        num_cores = multiprocessing.cpu_count()
        # Parallel(n_jobs=num_cores)(delayed(plot_cells)(df_list,groups_list,frame,data_dir,plot_traj,z_lim,hide_labels,no_bkg,lengthscale) for frame in df['frame'].unique())
    else:
        groups = df.groupby('frame')
        for frame in df['frame'].unique():
            frame = int(frame)
            plot_traj(df, frame, data_dir, groups=groups, image=image, plot_dir=plot_dir,
                      traj_parameters=traj_parameters,
                      dim=dim, plot_config=plot_config)


def plot_all_scalar_fields(data_dir, df, data, field, image={'image_fn': None, 't_dim': None, 'z_dim': None},
                           map_param={'no_bkg': False, 'vlim': None, 'show_axis': False, 'cmap': 'plasma'},
                           plot_dir=None, plot_config=None, dont_print_count=False):
    """Plot scalar fields as colormap for all frames."""

    if plot_dir is None:
        plot_dir = osp.join(data_dir, field)
    tpr.safe_mkdir(plot_dir)

    info = tpr.get_info(data_dir)

    plot_config = make_plot_config() if plot_config is None else plot_config

    # get vlim
    map_param_ = dict(map_param)
    if map_param_['vlim'] is None:
        vlim = tca.compute_vlim(df, data, field)
        map_param_['vlim'] = vlim
    label = tpr.make_param_label(field, l_unit=info['length_unit'], t_unit=info['time_unit'])
    plot_cmap(plot_dir, label, map_param_['cmap'], vlim[0], vlim[1])

    for frame in df['frame'].unique():
        frame = int(frame)
        fig, ax = plot_scalar_field(data_dir, df, data, field, frame, image=image,
                                    map_param=map_param_, plot_dir=plot_dir, plot_config=plot_config)
        plt.close(fig)


def plot_all_vector_fields(data_dir, df, data, field, plot_on_field=None, dim=3,
                           image={'image_fn': None, 't_dim': None, 'z_dim': None},
                           map_param={'no_bkg': False, 'vlim': None, 'show_axis': False, 'cmap': 'plasma',
                                      'size_factor': 1},
                           plot_dir=None, plot_config=None, dont_print_count=False):
    """Plot vector fields for all frames."""

    if plot_dir is None:
        plot_dir = osp.join(data_dir, field)
    tpr.safe_mkdir(plot_dir)

    info = tpr.get_info(data_dir)

    plot_config = make_plot_config() if plot_config is None else plot_config

    # get vlim
    if plot_on_field is not None:
        if plot_on_field['vlim'] is None:
            vlim = tca.compute_vlim(df, data, plot_on_field['plot_on'])
            plot_on_field['vlim'] = vlim
            label = tpr.make_param_label(plot_on_field['plot_on'], l_unit=info['length_unit'], t_unit=info['time_unit'])
            plot_cmap(plot_dir, label, plot_on_field['cmap'], vlim[0], vlim[1])

    for frame in df['frame'].unique():
        frame = int(frame)
        plot_vector_field(data_dir, df, data, field, frame, plot_on_field=plot_on_field, dim=dim, image=image,
                          map_param=map_param, plot_dir=plot_dir, plot_config=plot_config)


def plot_all_Voronoi(data_dir, df, data, show_local_area=True, df_mean = None,
                     image={'image_fn': None, 't_dim': None, 'z_dim': None},
                     map_param={'no_bkg': False, 'vlim': None, 'show_axis': False, 'cmap': 'plasma', 'size_factor': 1},
                     plot_dir=None, plot_config=None, dont_print_count=False):
    """
    Plot Voronoi for all frames and calculate voronoi cell area.
    """
    if plot_dir is None:
        plot_dir = osp.join(data_dir, 'voronoi')
    tpr.safe_mkdir(plot_dir)

    info = tpr.get_info(data_dir)

    plot_config = make_plot_config() if plot_config is None else plot_config

    # get vlim
    if show_local_area:
        if 'area' in df.columns:
            if map_param['vlim'] is None:
                vlim = [df['area'].min(), df['area'].max()]
                if vlim == [np.nan, np.nan]:
                    show_local_area = False
                else:
                    map_param['vlim'] = vlim
        else:
            show_local_area = False

    if show_local_area:
        label = tpr.make_param_label('area', l_unit=info['length_unit'], t_unit=info['time_unit'])
        plot_cmap(plot_dir, label, map_param['cmap'], map_param['vlim'][0], map_param['vlim'][1])

    for frame in df['frame'].unique():
        frame = int(frame)
        plot_Voronoi(data_dir, df, frame, data, show_local_area=show_local_area, image=image, map_param=map_param,
                     plot_dir=plot_dir, plot_config=plot_config, dont_print_count=dont_print_count)


def plot_all_MSD(data_dir, df=None, df_out=None, fit_model="biased_diff", msd_all=None, refresh=False, hue=None,
                 hue_order=None,
                 MSD_parameters={'dim': 2, 'fitrange': None, 'plot_all_MSD': True, 'plot_single_MSD': False,
                                 'logplot_x': True, 'logplot_y': True},
                 plot_config=None, plot_dir=None):
    """
    Plot all MSD of trajectories given by df (MSD_parameters['plot_all_MSD'] is True). 
    The MSD can be either computed from df or passed with msd_all. If msd_all is None it is computed from df, or it re-computed if refresh is True
    If msd_all contains data from several datasets they can be plotted invidually if with hue (in the order given by hue_order)
    Even with 3D data, the MSD can be computed only along the XY dimensions if MSD_parameters['dim']==2.
    The MSD can be fitted with a random walk model if fit_model is not None. Fit outputs are saved in df_out. 
    Indivual MSD can be plotted too (but it is advised not to do so for large number of trajectories) if MSD_parameters['plot_single_MSD'] is True.
    """

    # unpack parameters
    dim = MSD_parameters['dim']
    fitrange = MSD_parameters['fitrange']
    plot_all_MSD = MSD_parameters['plot_all_MSD']
    plot_single_MSD = MSD_parameters['plot_single_MSD']
    logx = MSD_parameters['logplot_x']
    logy = MSD_parameters['logplot_y']
    alpha = MSD_parameters['alpha']
    xylim = MSD_parameters['xylim'] if 'xylim' in MSD_parameters.keys() else None
    plot_config = make_plot_config() if plot_config is None else plot_config
    color_list = plot_config['color_list']

    # plotting directory
    if plot_dir is None:
        plot_dir = osp.join(data_dir, 'MSD')
    tpr.safe_mkdir(plot_dir)

    # prepare dataframes
    if df is None:
        data = tpr.get_data(data_dir)
        df = data['df']

    if df_out is None and fit_model is not None:  # compute track properties if MSD are to be fitted
        dimensions = ['x', 'y', 'z'] if 'z' in df.columns else ['x', 'y']
        df_out = tca.compute_track_prop(df, dimensions)

    if refresh:  # if refresh erase msd_all
        msd_all = None

    if msd_all is None:
        msd_all = pd.DataFrame()
        refresh = True

    # compute MSD
    if refresh:
        track_groups = df.groupby(['track'])
        track_list = df['track'].unique()
        msd_list = []
        for track in track_list:
            msd = plot_MSD(data_dir, track=track, track_groups=track_groups, df=df, df_out=df_out, fit_model=fit_model,
                           dim=dim, save_plot=plot_single_MSD, fitrange=fitrange, plot_dir=plot_dir,
                           plot_config=plot_config, logx=logx, logy=logy)
            msd['track'] = track

            # get subset if exists
            if 'subset' in df.columns:
                t = track_groups.get_group(track)
                subset = t['subset'].values[0]
                msd['subset'] = subset
            msd_list.append(msd)
        #concatenate
        msd_all = pd.concat(msd_list)

    # plot all
    if plot_all_MSD:
        info = tpr.get_info(data_dir)
        D_unit = tpr.make_param_label('D', l_unit=info['length_unit'], t_unit=info['time_unit'], only_unit=True)

        fig, ax = plt.subplots(1, 1, figsize=plot_config['figsize'])

        if hue is not None:
            if hue_order is None:
                hue_order = msd_all[hue].unique()
            msd_all_list = []
            for h in hue_order:
                msd_all_list.append(msd_all[msd_all[hue] == h])
        else:
            msd_all_list = [msd_all]

        for j, msd_all_ in enumerate(msd_all_list):
            for track in msd_all_['track'].unique():
                msd = msd_all_[msd_all_['track'] == track]
                ax.plot(msd["tau"].values, msd["msd"].values, color=color_list[j], alpha=alpha, label=None)

            # calculate mean
            msd_mean = pd.DataFrame(columns=['tau', 'msd_mean', 'msd_std', 'msd_sem'])
            i = 0
            for t in msd_all_["tau"].unique():
                mean = msd_all_[msd_all_['tau'] == t]['msd'].mean()
                std = msd_all_[msd_all_['tau'] == t]['msd'].std()
                sem = msd_all_[msd_all_['tau'] == t]['msd'].sem()
                msd_mean.loc[i, :] = [t, mean, std, sem]
                i += 1

            lab = 'mean' if hue is None else hue_order[j]
            suffix = '' if hue is None else '_' + hue_order[j]

            msd_mean.plot(x="tau", y="msd_mean", color=color_list[j], ax=ax, label=lab)
            msd_mean.to_csv(osp.join(plot_dir, 'all_MSD_mean' + suffix + '.csv'))
            # calculate exponent
            msd_mean[['tau', 'msd_mean']] = msd_mean[['tau', 'msd_mean']].astype(np.float64)
            msd_mean['log_tau'] = np.log(msd_mean['tau'])
            msd_mean['log_msd'] = np.log(msd_mean['msd_mean'])
            parameters, errors, fitted_, Rsq, success = tca.fit_lin(msd_mean[['log_tau', 'log_msd']].values)
            fit_dict = {'exponent': parameters[0], 'exponent_err': errors[0]}
            # fit MSD with model
            if fit_model is not None:
                msd_mean['msd'] = msd_mean['msd_mean']
                results = tca.fit_msd(msd_mean, mean_vel=df['v'].mean(), dim=dim, model=fit_model, fitrange=fitrange)
                if results['success']:
                    for i, param in enumerate(results['param'].keys()):
                        fit_dict[param] = results['param'][param]
                        fit_dict[param + '_error'] = results['errors'][i]
            tpr.write_dict(fit_dict, osp.join(plot_dir, 'all_MSD_fit' + suffix + '.csv'))

        # handles,labels=ax.get_legend_handles_labels()
        # ax.legend([handles[-1]],[labels[-1]],frameon=False) #show only the mean in the legend, ax.legend() only support lists for handles and labels
        ax.legend(frameon=False)
        ax.set_xlabel('lag time ({})'.format(info['time_unit']))
        ax.set_ylabel(r'MSD ({})'.format(D_unit))

        if logx:
            ax.set_xscale('log')
        if logy:
            ax.set_yscale('log')

        if xylim is not None:
            ax.set_xlim(xylim[0], xylim[1])
            ax.set_ylim(xylim[2], xylim[3])

        if plot_config['despine']:
            sns.despine(fig)
        fig.savefig(osp.join(plot_dir, 'all_MSD{}'.format(plot_config['format'])), dpi=plot_config['dpi'],
                    bbox_inches='tight')
        plt.close(fig)

    msd_all.to_csv(osp.join(plot_dir, 'all_MSD.csv'))

    return df_out


def plot_total_traj(data_dir, df, dim=3, plot_dir=None, plot_fn=None, plot_config=None, specific_config=None):
    """Plot trajectories with common origin. Impose xlim and ylim with set_axis_lim=[xmin,xmax,ymin,ymax]"""

    # Plotting parameters
    plot_config = make_plot_config() if plot_config is None else plot_config
    color_list = plot_config['color_list']
    invert_yaxis = plot_config['invert_yaxis']

    #initialize config if None
    if specific_config is None:
        specific_config = {'dont_center': False,
                           'hide_labels': False,
                           'set_axis_lim': None,
                           'equal_axis': True,
                           'label_size': 6,
                           'color_code': 'random',
                           'cmap': 'plasma',
                           'cmap_lim': None,
                           'subset_order': None,
                           }

    # unpack config
    dont_center = specific_config['dont_center']
    hide_labels = specific_config['hide_labels']
    set_axis_lim = specific_config['set_axis_lim']
    equal_axis = specific_config['equal_axis']
    label_size = specific_config['label_size']
    color_code = specific_config['color_code']
    cmap = specific_config['cmap']
    cmap_lim = specific_config['cmap_lim']
    subset_order = specific_config['subset_order']

    # get info
    info = tpr.get_info(data_dir)

    # saving directory
    if plot_dir is None:
        plot_dir = osp.join(data_dir, 'centered_traj')
        tpr.safe_mkdir(plot_dir)

    # group by tracks
    track_groups = df.groupby(['track'])

    # color code
    if color_code == 'z' and dim == 3:
        if cmap_lim is None:
            cmap_lim = [df['z_scaled'].min(), df['z_scaled'].max()]

        if len(cmap_lim) == 2:
            plot_cmap(plot_dir, tpr.make_param_label('z', l_unit=info["length_unit"]), cmap, cmap_lim[0], cmap_lim[1])

    elif color_code == 't':
        if cmap_lim is None:
            cmap_lim = [df['t'].min(), df['t'].max()]

        if len(cmap_lim) == 2:
            plot_cmap(plot_dir, tpr.make_param_label('t', l_unit=info["time_unit"]), cmap, cmap_lim[0], cmap_lim[1])
    
    elif color_code == 'ROI':
        if 'subset' in df.columns:
            # check subset order
            if subset_order is None:
                subset_order = df['subset'].unique()
            else: 
                for sub in df['subset'].unique():
                    if sub not in subset_order: # if missing subset in subset_oder, adding it
                        subset_order.append(sub)
            subset_order = list(subset_order)  # convert to list to use index method
            df['subset_order'] = df['subset'].apply(lambda s: subset_order.index(s))  # column with indices in subset_order

    # ensure 'z' is not color code for 2D data
    elif dim == 2 and color_code == 'z':
        color_code == 'random'

    fig, ax = plt.subplots(1, 1, figsize=plot_config['figsize'])
    for i, track in enumerate(df['track'].unique()):
        traj = tpr.get_traj(track_groups, track)
        traj_length = traj.shape[0]
        first_frame = traj['frame'].min()
        x0, y0 = traj[traj['frame'] == first_frame][['x_scaled', 'y_scaled']].values[0]
        x = traj['x_scaled'].values
        y = traj['y_scaled'].values
        if dim == 3:
            z = traj['z_scaled'].values
        if not dont_center:
            traj['x_scaled'] -= x0
            traj['y_scaled'] -= y0

        # color
        if color_code == "z" and dim == 3:
            colors = tpr.get_cmap_color(z, cmap, vmin=cmap_lim[0], vmax=cmap_lim[1])
        elif color_code == "random":
            colors = color_list[i % len(color_list)]
        elif color_code == "none":
            colors = color_list[0]
        elif color_code == "ROI":
            if 'subset_order' in df.columns:
                colors = color_list[traj['subset_order'].values[0] % len(color_list)]
            else:
                colors = color_list[0]  # if color_coded by subset but there's none, use only one color
        else:
            colors = color_list[0]

        if color_code == 'z' and dim == 3:
            for j in range(1, traj_length):
                ax.plot([x[j - 1], x[j]], [y[j - 1], y[j]], ls='-', color=colors[j])
            ax.plot(x[-1], y[-1], marker='.', color=colors[-1])
        else:
            ax.plot(x, y, ls='-', color=colors)
            ax.plot(x[-1], y[-1], marker='.', color=colors)

        if hide_labels is False:
            s = '{}'.format(int(track))
            ax.text(traj['x_scaled'].values[-1], traj['y_scaled'].values[-1], s, fontsize=label_size)
        if set_axis_lim is not None:
            ax.set_xlim(set_axis_lim[0], set_axis_lim[1])
            ax.set_ylim(set_axis_lim[2], set_axis_lim[3])
        ax.set_xlabel(r'x ($\mu m$)')
        ax.set_ylabel(r'y ($\mu m$)')

    if equal_axis:
        ax.set_aspect('equal')

    if invert_yaxis:
        ylim = ax.get_ylim()
        ax.set_ylim(ylim[1], ylim[0])

    fig.tight_layout()

    filename = osp.join(plot_dir,'total_traj'+plot_config['format']) if plot_fn is None else plot_fn
    fig.savefig(filename, dpi=plot_config['dpi'])
    plt.close(fig)
