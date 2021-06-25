
# Copyright (c) 2021, Eva Laplace e.c.laplace@uva.nl

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import matplotlib.pyplot as plt
import mesaPlot as mp
import numpy as np
from os import makedirs, path
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.colors import ListedColormap
from matplotlib.patches import Wedge, Patch
from matplotlib.colors import Normalize, LogNorm
from tqdm.notebook import tqdm
import astropy.units as u
from imageio_ffmpeg import get_ffmpeg_exe
import re
import cmasher as cmr

# Use ffmpeg executable from imageio_ffmpeg to avoid installation issues
plt.rcParams['animation.ffmpeg_path'] = get_ffmpeg_exe()

from matplotlib.animation import FuncAnimation


from . import colormodels
from . import blackbody



# Define global constants
ELEM_BASE = ['h1', 'he3', 'he4', 'c12', 'n14', 'o16', 'ne20', 'mg24', 'si28', 's32', 'ar36', 'ca40', 'ti44', 'cr48',
             'cr56', 'fe52', 'fe54', 'fe56', 'ni56']
ELEM_EXTENDED = ['s32','s33', 's34', 'cl35', 'ar36','ar38', 'k39', 'ca40', 'ca42', 'ti46', 'ti47', 'ti48', 'v49', 'v50',
                 'v51', 'cr48', 'cr49', 'cr50', 'cr51', 'cr52', 'cr53', 'cr54', 'cr55', 'cr56', 'cr57', 'mn51', 'mn52',
                 'mn53', 'mn54', 'mn55', 'mn56', 'fe52', 'fe53', 'fe54', 'fe55', 'fe56', 'fe57', 'fe58', 'co55', 'co56',
                 'co57', 'co58', 'co59', 'co60', 'ni56', 'ni57', 'ni58', 'ni59', 'ni60', 'ni61', 'cu59', 'cu61', 'cu62']
ABUN_ELEM_M127 = np.hstack([ELEM_BASE[:9], ELEM_EXTENDED])
# Custom colormap
CMAP_BASE = ListedColormap([ "#40C4FF",     # dark blue - h1
                             "#64B5F6",     # lighter dark blue - he3
                             "#2962FF",     # light blue - he4
                             "#C6FF00",     # lime - c12
                             "#18FFFF",     # cyan - n14
                             "#00C853",     # dark green - o16
                             "#69F0AE",     # light green - ne20
                             "#8D6E63",     # light brown - mg24
                             "#5D4037",     # brown - si28
                             "#BDBDBD",     # grey - s32
                             "#2f0596",     # ar36
                             "#4903a0",     # ca40
                             "#6100a7",     # ti47
                             "#8707a6",     # cr48
                             "#ba3388",     # cr56
                             "#de6164",     # fe52
                             "#e66c5c",     # fe54
                             "#ed7953",     # fe56
                             "#feb72d",     # ni56
                             ])
CMAP_DEFAULT = cmr.get_sub_cmap("cmr.pride", 0, 0.8)
CMAP_HEAVY = cmap = plt.get_cmap("plasma", len(ELEM_EXTENDED))
CMAP_M127 = ListedColormap(np.vstack([CMAP_BASE(np.linspace(0, 0.5, 10)),
                                      CMAP_HEAVY(np.linspace(0, 1, len(ELEM_EXTENDED)))]))
p = mp.plot(rcparams_fixed=False)
ROBS_CMAP_ENERGY = p.mergeCmaps([plt.cm.Purples_r, plt.cm.hot_r], [[0.0, 0.5], [0.5, 1.0]])
# Default values for percentages and fraction annotations
PERCENTAGE_LIST = [0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]
FRACTION_LIST = [0.25, 0.5, 0.75, 1.0]
# Mixing types
MIX_TYPES = ["No mixing", "Convection", "Softened convection", "Overshooting", "Semi-convection", "Thermohaline mixing",
             "Rotational mixing", "Rayleigh-Taylor mixing", "Minimum", "Anonymous"]
MIX_HATCHES = ['',      # no mixing
               'o',     # convective
               '.',     # softened convective
               'x',     # overshoot
               'O',     # semi-convective
               '\\',    # thermohaline
               '/',     # rotation
               '+',      # Rayleigh-Taylor
               '',      # minimum
               ''       # anonymous
               ]


def perceived_color(m, time_ind=-1, raxis="log_R", fps=10, fig=None, ax=None, show_time_label=True, time_label_loc=(),
                    time_unit="Myr", fig_size=(5.5, 4), axis_lim=-99, axis_label="", theta1=0, theta2=360,
                    hrd_inset=True, show_hrd_ticks_and_labels=False, show_total_mass=True, show_surface=True,
                    output_fname="perceived_color", anim_fmt=".mp4",
                    time_scale_type="model_number"):

    r""" Create perceived color diagram of a stellar model.
    
    Represent the model of a stellar object as circle with radius `raxis`. The color of the circle corresponds to its
    color as perceived by the human eye by assuming black body radiation at a certain effective temperature.
    Requires a MESA history file.
    
    Parameters
    ----------
    m : mesaPlot object
        Already loaded a history file.
    time_ind : int or tuple (start_index, end_index, step=1) or (start_index, end_index, step)
        If int: create the plot at the index `time_ind`. If tuple: create an animation from start index to end index with intervals of step.
    raxis : str
        Default axis to use as radius of the circle.
    fps : int
        Number of frames per second for the animation.
    fig : Figure object
        If set, plot on existing figure.
    ax : Axes object
        If set, plot on provided axis.
    show_time_label : boolean
        If set, insert a label that gives the age of the stellar object (in Myr).
    time_label_loc : tuple
        Location of the time label on the plot as fraction of the maximal size.
    time_unit : str
        Valid astropy time unit.
    fig_size : tuple
        Size of the figure in inches.
    axis_lim : float
        Value to set for the maximum limit of the x and y axis.
    axis_label : str
        Label of the x and y axis.
    theta1: int or float
        Start angle for the wedge.
    theta2 : int or float
        End angle for the wedge.
    hrd_inset : boolean
        If set, add an inset HRD where the location of the current model is indicated with a circle.
    show_hrd_ticks_and_labels : Boolean
        If set, display the axis ticks and labels of the inset HRD
    show_total_mass : boolean
        If set, display the value of the total mass of the model in the bottom right corner.
    show_surface : boolean,
        If set, show the outer boundary of the stellar object.
    output_fname : str
        Name of the output file.
    anim_fmt : str
        Format to use for saving an animation.
    time_scale_type : str
        One of `model_number`, `linear`, or `log_to_end`. For `model_number`, the time follows the moment when a new MESA model was saved. For `linear`, the time follows linear steps in star_age. For `log_to_end`, the time axis is tau = log10(t_final - t), where t_final is the final star_age of the model.
    
    Returns
    -------
    fig, ax
    """
    if fig is None:
        fig = plt.figure()
        fig.set_size_inches(fig_size)
    if ax is None:
        ax = plt.gca()

    start_ind, end_ind, ind_step = check_time_indeces(time_ind, m.hist.star_age)

    r = m.hist.data[raxis]

    # Set axis limits
    if axis_lim == -99:
        axis_lim = 1.1 * r.max()
    elif raxis[:3] == "log":
        axis_lim = np.log10(axis_lim)

    # replace smallest values with constant ratio
    smallest_radius_ratio = 0.01
    too_small = (r / axis_lim < smallest_radius_ratio)
    if np.any(too_small):
        r[too_small] = axis_lim * smallest_radius_ratio

    # Plot star as circle with color derived from Teff
    color = teff2rgb([10 ** m.hist.log_Teff[start_ind]])[0]

    lw = 0
    if show_surface:
        lw = 1.1
    circle = Wedge((0, 0), r[start_ind], theta1=theta1, theta2=theta2, facecolor=color, edgecolor='k',
                   lw=lw)
    ax.add_artist(circle)

    # Add time label
    if show_time_label:
        time = m.hist.star_age[start_ind]
        text = add_time_label(time, ax, time_label_loc=time_label_loc, time_unit=time_unit)

    # Set axis for plotting correctly sized circles
    ax.set_xlim([-axis_lim, axis_lim])
    ax.set_ylim([-axis_lim, axis_lim])
    ax.set_aspect('equal', adjustable='box')

    set_axis_ticks_and_labels(ax, raxis=raxis, axis_label=axis_label)

    if hrd_inset:
        axins, point = add_inset_hrd(m, ax=ax, time_index=start_ind,
                                     show_hrd_ticks_and_labels=show_hrd_ticks_and_labels)

    # Add mass label
    if show_total_mass:
        mass_text = ax.text(0.87, 0.05, "{}".format(round(m.hist.star_mass[start_ind], 1)) +
                            "$\,\\rm{M}_{\odot}$", transform=ax.transAxes, ha="center", va="center")

    # Create animation
    if end_ind != start_ind:
        # Create animation
        indices = range(start_ind, end_ind, ind_step)
        indices = rescale_time(indices, m, time_scale_type=time_scale_type)
        r = r[indices]
        t = m.hist.star_age[indices]
        log_teff = m.hist.log_Teff[indices]
        log_l = m.hist.log_L[indices]
        star_mass = m.hist.star_mass[indices]
        colors_ary = teff2rgb(10 ** log_teff)

        frames = len(indices)
        fps = fps
        bar = tqdm(total=frames)

        def init():
            circle.radius = r[0]
            circle.set_facecolor(colors_ary[0])
            ax.add_patch(circle)
            time = (t[0] * u.yr).to(time_unit)
            text.set_text("t = " + time.round(3).to_string())
            return circle, point

        def animate(ind):
            bar.update()
            time = (t[ind] * u.yr).to(time_unit)
            r_cur = r[ind]
            color = colors_ary[ind]
            circle.set_radius(r_cur)
            circle.set_facecolor(color)

            # Add time location
            if show_time_label:
                text.set_text("t = " + time.round(3).to_string())

            if hrd_inset:
                point.set_data(log_teff[ind], log_l[ind])

            if show_total_mass:
                mass_text.set_text("{}".format(round(star_mass[ind], 1)) + "$\,\\rm{M}_{\odot}$")

            return circle, point

        print("Creating animation")

        ani = FuncAnimation(fig, animate, init_func=init, frames=frames, interval=1000 / fps, blit=False, repeat=False)
        plt.subplots_adjust(top=0.99, left=0.12, right=0.89, hspace=0, wspace=0, bottom=0.1)

        # Save animation
        ani.save(output_fname + anim_fmt, writer="ffmpeg", extra_args=['-vcodec', 'libx264'])

    return fig, ax


def energy_and_mixing(m, time_ind=-1, show_mix=False, show_mix_legend=True, raxis="star_mass", fps=10, fig=None, ax=None,
                      show_time_label=True, time_label_loc=(), time_unit="Myr", fig_size=(5.5, 4), axis_lim=-99,
                      axis_label="", axis_units="", show_colorbar=True, cmap=ROBS_CMAP_ENERGY, cmin=-10,
                      cmax=10, cbar_label="", theta1=0, theta2=360, hrd_inset=True, show_hrd_ticks_and_labels=False,
                      show_total_mass=False, show_surface=True, show_grid=False, output_fname="energy_and_mixing",
                      anim_fmt=".mp4", time_scale_type="model_number"):
    """Create energy and mixing diagram.
    
    Represent the model of a stellar object as circle with radius raxis. The circle is divided into rings whose color
    reflect how much energy is generated or lost from the star. Optionally, hashed areas representing mixing regions
    can be added. This corresponds to a "2D Kippenhahn plot".
    Requires MESA history files that contain burning_regions and optionally mixing_regions.
    
    Parameters
    ----------
    m : mesaPlot object
        Already loaded a history file.
    time_ind : int or tuple (start_index, end_index, step=1) or (start_index, end_index, step)
        If int: create the plot at the index time_ind. If tuple: create an animation from start index to end index with
    intervals of step.
    show_mix: boolean
        If set, add hatches for convection and overshooting zones in the star.
    show_mix_legend: boolean
        If set, show a legend for the mixing types.
    raxis : str
        Default axis to use as radius of the circle.
    fps: int
        Number of frames per second for the animation
    fig : Figure object
        If set, plot on existing figure.
    ax : Axes object
        If set, plot on provided axis.
    show_time_label : boolean
        If set, insert a label that gives the age of the stellar object.
    time_label_loc : tuple
        Location of the time label on the plot as fraction of the maximal size.
    time_unit : str
        Valid astropy time unit, default Myr.
    fig_size : tuple
        Size of the figure in inches.
    axis_lim : float
        Value to set for the maximum limit of the x and y axis.
    axis_label : str
        Label of the x and y axis.
    axis_units : str
        Astropy unit for the x and y axis.
    show_colorbar : boolean
        If set, add a colorbar corresponding to the property shown.
    cmap : str or matplotlib.colors.ListedColormap
        Colormap to use for the property
    cmin : float
        Minimum value to set for the colorbar.
    cmax : float
        Maximum value to set for the colorbar, if smaller or equal to cmin, use the minimum and maximum values of property_name instead.
    cbar_label : str
        Label to set for the colorbar.
    theta1 : int or float
        Start angle for the wedge.
    theta2: int or float
        End angle for the wedge.
    hrd_inset : boolean
        If set, add an inset HRD where the location of the current model is indicated with a circle.
    show_hrd_ticks_and_labels : Boolean
        If set, display the axis ticks and labels of the inset HRD
    show_total_mass : boolean
        Default False, display the value of the total mass of the model below the circle.
    show_surface : boolean
        Default True, if set, show the outer boundary of the stellar object.
    show_grid: boolean
        Default False, if set, add additional axes in crosshair form.
    output_fname : str
        Name of the output file.
    anim_fmt : str
        Format to use for saving an animation.
    time_scale_type : str
        One of `model_number`, `linear`, or `log_to_end`. For `model_number`, the time follows the moment when a new MESA model was saved. For `linear`, the time follows linear steps in star_age. For `log_to_end`, the time axis is tau = log10(t_final - t), where t_final is the final star_age of the model.
    
    Returns
    -------
    fig, ax
    """
    if fig is None:
        fig = plt.figure()
        fig.set_size_inches(fig_size)
    if ax is None:
        ax = plt.gca()

    start_ind, end_ind, ind_step = check_time_indeces(time_ind, m.hist.star_age)

    r = m.hist.data[raxis]

    # Set axis limits
    if axis_lim == -99:
        axis_lim = 1.1 * r.max()

    # replace smallest values with constant ratio
    smallest_radius_ratio = 0.01
    too_small = (r / axis_lim < smallest_radius_ratio)
    if np.any(too_small):
        r[too_small] = axis_lim * smallest_radius_ratio

    # Show energy and mixing regions
    burn_wedges_list = []
    mix_wedges_list = []

    qtop = "burn_qtop_"
    qtype = "burn_type_"
    try:
        m.hist.data[qtop + "1"]
    except ValueError:
        raise KeyError(
            "No field " + qtop + "* found, add mixing_regions 40 and burning_regions 40 to your history_columns.list")
    if type(cmap) == str:
        cmap = plt.get_cmap(cmap, len(m.hist.data[qtype + "1"]))
    # Automatic colorbar limits
    if cmin == cmax:
        cmin = m.hist.data[qtop + "1"].min()
        cmax = m.hist.data[qtop + "1"].max()

    # Plot energy production / loss zones
    num_burn_zones = int([xx.split('_')[2] for xx in m.hist.data.dtype.names if qtop in xx][-1])
    width = 0
    sm = m.hist.star_mass
    norm = Normalize(vmin=cmin, vmax=cmax)
    for region in range(1, num_burn_zones + 1):
        # Plot burning regions
        radius = np.abs(m.hist.data[qtop + str(region)][start_ind] * sm[start_ind])
        burn = m.hist.data[qtype + str(region)][start_ind]
        # Width = current radius - previous radius
        width += radius
        color = cmap(norm(burn))
        # Center zone should be a circle, not a ring
        if region == 1:
            width = None
        wedge = Wedge((0, 0), radius, width=width, zorder=-region, color=color, theta1=theta1,
                      theta2=theta2)
        ax.add_artist(wedge)
        burn_wedges_list.append(wedge)
        width = -1 * radius

    # Plot mixing
    if show_mix:
        mix_qtop = "mix_qtop_"
        mix_qtype = "mix_type_"
        try:
            m.hist.data[qtop + "1"]
        except ValueError:
            raise KeyError(
                "No field " + qtop + "* found, add mixing_regions 40 and burning_regions 40 to your history_columns.list")

        num_mix_zones = int([xx.split('_')[2] for xx in m.hist.data.dtype.names if mix_qtop in xx][-1])
        width = 0
        sm = m.hist.star_mass
        norm = Normalize(vmin=cmin, vmax=cmax)

        legend_elements = []
        legend_names = []
        for region in range(1, num_mix_zones + 1):
            # Plot mixing regions
            radius = np.abs(m.hist.data[mix_qtop + str(region)][start_ind] * sm[start_ind])
            mix = m.hist.data[mix_qtype + str(region)][start_ind]
            # Width = current radius - previous radius
            width += radius
            hatch = MIX_HATCHES[int(mix)]
            # Center zone should be a circle, not a ring
            if region == 1:
                width = None
            wedge = Wedge((0, 0), radius, width=width, zorder=-region, hatch=hatch,
                          color="grey", alpha=0.8, lw=1, fill=False, theta1=theta1, theta2=theta2)
            ax.add_artist(wedge)
            mix_wedges_list.append(wedge)
            width = -1 * radius
            # Show legend
            if show_mix_legend:
                if mix > 0 and MIX_TYPES[int(mix)] not in legend_names:
                    legend_elements.append(
                        Patch(facecolor=None, hatch=hatch, edgecolor="grey", alpha=0.8, fill=False))
                    legend_names.append(MIX_TYPES[int(mix)])
        if show_mix_legend:
            ax.legend(legend_elements, legend_names, loc="upper right")

    # Add time label
    if show_time_label:
        time = m.hist.star_age[start_ind]
        text = add_time_label(time, ax, time_label_loc=time_label_loc, time_unit=time_unit)

    # Add crosshair
    if show_grid:
        #TODO: add grid
        pass

    if hrd_inset:
        axins, point = add_inset_hrd(m, ax=ax, time_index=start_ind,
                                     show_hrd_ticks_and_labels=show_hrd_ticks_and_labels)

    # Add mass label in lower right corner
    if show_total_mass:
        mass_text = ax.text(0.87, 0.05, "{}".format(round(m.hist.star_mass[start_ind], 1)) +
                            "$\,\\rm{M}_{\odot}$", transform=ax.transAxes, ha="center", va="center")

    # Add color-bar
    if show_colorbar:
        sm_colorbar = plt.cm.ScalarMappable(cmap=cmap, norm=Normalize(vmin=cmin, vmax=cmax))
        # fake up the array of the scalar mappable
        sm_colorbar.set_array(m.hist.data[qtype + '1'])
        cb, div = colorbar(sm_colorbar, ax=ax)
        cb.set_label(cbar_label)
        if cbar_label == "":
            cb.set_label('$\\log_{10} $``energy generation/loss rate"')

    if show_surface:
        surface = Wedge((0, 0), r[start_ind], theta1=theta1, theta2=theta2, fill=False, facecolor="#FFFDE7",
                        edgecolor='k', lw=1.1)
        ax.add_artist(surface)

    # Set axis for plotting correctly sized circles
    ax.set_xlim([-axis_lim, axis_lim])
    ax.set_ylim([-axis_lim, axis_lim])
    ax.set_aspect('equal', adjustable='box')

    # Set axis and tick labels
    set_axis_ticks_and_labels(ax, raxis="star_mass", axis_label=axis_label)

    # Create animation
    if end_ind != start_ind:
        # Create animation
        indices = range(start_ind, end_ind, ind_step)
        indices = rescale_time(indices, m, time_scale_type=time_scale_type)
        r = r[indices]
        t = m.hist.star_age[indices]

        frames = len(indices)
        fps = fps
        bar = tqdm(total=frames)

        def init():
            wedge.radius = r[0]
            time = (t[0] * u.yr).to(time_unit)
            text.set_text("t = " + time.round(3).to_string())
            for artist in burn_wedges_list:
                ax.add_patch(artist)
            if show_mix:
                for artist in mix_wedges_list:
                    ax.add_patch(artist)
            return wedge, point, burn_wedges_list, mix_wedges_list

        def animate(ind):
            bar.update()
            time = (t[ind] * u.yr).to(time_unit)
            r_cur = r[ind]
            wedge.radius = r_cur
            log_teff = m.hist.log_Teff[indices]
            log_l = m.hist.log_L[indices]
            star_mass = m.hist.star_mass[indices]

            # Add burning
            width = 0
            for artist, region in zip(burn_wedges_list, range(1, num_burn_zones + 1)):
                # Plot burning regions
                radius = np.abs(m.hist.data[qtop + str(region)][indices][ind] * r_cur)
                burn = m.hist.data[qtype + str(region)][indices][ind]
                # Width = current radius - previous radius
                width += radius
                # Center zone should be a circle, not a ring
                if region == 1:
                    width = None
                color = cmap(norm(burn))

                # Change current artist
                artist.set_radius(radius)
                artist.set_color(color)
                artist.set_width(width)

                # Width = current radius - previous radius
                width = -1 * radius

            # Add mixing
            if show_mix:
                for mix_artist, region in zip(mix_wedges_list, range(1, num_mix_zones + 1)):
                    # Plot mixing regions
                    radius = np.abs(m.hist.data[mix_qtop + str(region)][ind] * r_cur)
                    mix = m.hist.data[mix_qtype + str(region)][indices][ind]
                    # Width = current radius - previous radius
                    width += radius
                    hatch = MIX_HATCHES[int(mix)]
                    # Center zone should be a circle, not a ring
                    if region == 1:
                        width = None

                    # Change current artist
                    mix_artist.set_radius(radius)
                    mix_artist.set_hatch(hatch)
                    mix_artist.set_width(width)
                    width = -1 * radius

            # Add time location
            text.set_text("t = " + time.round(1).to_string())

            if hrd_inset:
                point.set_data(log_teff[ind], log_l[ind])

            if show_total_mass:
                mass_text.set_text("{}".format(round(star_mass[ind], 1)) + "$\,\\rm{M}_{\odot}$")

            if show_surface:
                surface.set_radius(r_cur)

            return wedge, point, burn_wedges_list, mix_wedges_list

        print("Creating movie...")
        ani = FuncAnimation(fig, animate, init_func=init, frames=frames, interval=1000 / fps, blit=False, repeat=False)
        # Save animation
        ani.save(output_fname + anim_fmt, writer="ffmpeg", extra_args=['-vcodec', 'libx264'])
    return fig, ax


def property_profile(m, time_ind=-1, property_name="logRho", num_rings=-1, raxis="mass", log=False, log_low_lim=1e-20,
                     fps=10, fig=None, ax=None, show_time_label=True, time_label_loc=(), time_unit="Myr",
                     fig_size=(5.5, 4), axis_lim=-99, axis_label="", show_colorbar=True, cmap="plasma",
                     cmin=0, cmax=0, cbar_label="", theta1=0, theta2=360, hrd_inset=True,
                     show_hrd_ticks_and_labels=False, show_total_mass=True,
                     show_surface=True, show_grid=False, output_fname="property_profile", anim_fmt=".mp4"):

    """ Create property profile diagram. 
    
    Represent the model of a stellar object as circle with radius raxis. The circle is divided into rings whose color
    reflect the values of a physical property of the model.
    Requires MESA profile files that contain this property and the corresponding MESA history file.
    
    Parameters
    ----------
    m : mesaPlot object
        Already loaded a history file
    time_ind : int or tuple (start_index, end_index, step=1) or (start_index, end_index, step)
        If int: create the plot at the index time_ind. If tuple: create an animation from start index to end index with intervals of step.
    property_name : string
        Property of a MESA profile to be shown as colors.
    num_rings : int
        Default -1, if greater than -1, limit the number of rings to this number.
    raxis : str
        Default axis to use as radius of the circle.
    log : boolean
        If set, show the natural logarithm of the property.
    log_low_lim : float
        Value to replace zero and negative values in a property with
    fps : int
        Number of frames per second for the animation.
    fig : Figure object
        If set, plot on existing figure.
    ax : Axes object
        If set, plot on provided axis.
    show_time_label : boolean
        If set, insert a label that gives the age of the stellar object (in Myr).
    time_label_loc : tuple
        Location of the time label on the plot as fraction of the maximal size.
    time_unit : str
        Valid astropy time unit, default Myr.
    fig_size : tuple
        Size of the figure in inches.
    axis_lim : float
        Value to set for the maximum limit of the x and y axis.
    axis_label : str
        Label of the x and y axis.
    show_colorbar : boolean
        If set, add a colorbar corresponding to the property shown.
    cmin : float
        Minimum value to set for the colorbar.
    cmax : float
        Maximum value to set for the colorbar, if smaller or equal to cmin, use the minimum and maximum values of property_name instead.
    cmap : str or matplotlib.colors.ListedColormap
        Colormap to use for the property
    cbar_label : str
        Label to set for the colorbar.
    theta1 : int or float
        Start angle for the wedge.
    theta2 : int or float
        End angle for the wedge.
    hrd_inset : boolean
        If set, add an inset HRD where the location of the current model is indicated with a circle.
    show_hrd_ticks_and_labels : Boolean
        If set, display the axis ticks and labels of the inset HRD
    show_total_mass: boolean
        Default False, display the value of the total mass of the model below the circle
    show_surface : boolean
        Default True, if set, show the outer boundary of the stellar object.
    show_grid : boolean
        Default False, if set, add additional axes in crosshair form.
    output_fname : str
        Name of the output file.
    anim_fmt : str
        Format to use for saving an animation.
        
    Returns
    -------
    fig, ax
    """
    if fig is None:
        fig = plt.figure()
        fig.set_size_inches(fig_size)
    if ax is None:
        ax = plt.gca()

    start_ind, end_ind, ind_step = check_time_indeces(time_ind, m.hist.star_age)
    prof = find_profile(m, time_ind=start_ind)
    r = prof.data[raxis]
    prop = prof.data[property_name][:]

    automatic_limits = False
    # Set axis limits
    if axis_lim == -99:
        axis_lim = 1.1 * r.max()
        automatic_limits = True

    if log:
        # Replace zero and negative values with fill value
        prop[prop <= 0] = log_low_lim
    # Automatic colorbar limits
    if cmin == cmax:
        if log:
            cmin = np.log10(prop.min())
            cmax = np.log10(prop.max())
        else:
            cmin = prop.min()
            cmax = prop.max()

    if type(cmap) == str:
        cmap = plt.get_cmap(cmap, len(prop))
    # Plot a quantity as colored rings inside a stellar structure
    wedges_list = make_property_plot(ax, prof, property_name, raxis, log=log, cmin=cmin, cmax=cmax, num_rings=num_rings,
                                     theta1=theta1, theta2=theta2, cmap=cmap, log_low_lim=log_low_lim)

    # Add time label
    if show_time_label:
        time = prof.star_age
        text = add_time_label(time, ax, time_label_loc=time_label_loc, time_unit=time_unit)

    # Set axis for plotting correctly sized circles
    ax.set_xlim([-axis_lim, axis_lim])
    ax.set_ylim([-axis_lim, axis_lim])
    ax.set_aspect('equal', adjustable='box')

    # Add axis label
    set_axis_ticks_and_labels(ax, raxis=raxis, axis_label=axis_label)

    # Add annotations
    # add_ring_annotations(ax, rmax=prof.star_mass, show_percentage=True, show_fraction_labels=False)

    # Add crosshair
    if show_grid:
        #TODO: add grid
        pass

    if hrd_inset:
        axins, point = add_inset_hrd(m, ax=ax, time_index=start_ind,
                                     show_hrd_ticks_and_labels=show_hrd_ticks_and_labels)

    # Add mass label
    if show_total_mass:
        mass_text = ax.text(0.87, 0.05, "{}".format(round(prof.star_mass, 1)) +
                            "$\,\\rm{M}_{\odot}$", transform=ax.transAxes, ha="center", va="center")

    # Add colorbar
    if show_colorbar:
        if num_rings > -1:
            selec = [int(i) for i in np.linspace(0, len(prof.mass) - 1, num_rings)]
            prop = prop[selec]
        norm = Normalize(vmin=cmin, vmax=cmax)
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=Normalize(vmin=cmin, vmax=cmax))
        # fake up the array of the scalar mappable
        sm.set_array(prof.data[property_name])
        bar, div = colorbar(sm, ax=ax)
        if cbar_label == "":
            cbar_label = property_name.replace("_", "")
            if log:
                cbar_label = "log " + cbar_label
        bar.set_label(cbar_label)

    if show_surface:
        surface = Wedge((0, 0), r.max(), theta1=theta1, theta2=theta2, fill=False, facecolor="#FFFDE7",
                        edgecolor='k', lw=1.1)
        ax.add_artist(surface)

    # Create animation
    if end_ind != start_ind:
        def init():
            for w in wedges_list:
                ax.add_patch(w)
            if show_time_label:
                time = (prof.star_age * u.yr).to(time_unit)
                text.set_text("t = " + time.round(1).to_string())
            if show_total_mass:
                mass_text.set_text("".format(round(prof.star_mass, 1)) + "$\,\\rm{M}_{\odot}$")
            if show_surface:
                surface.set_radius(r.max())
                ax.add_artist(surface)
            return wedges_list

        def animate(i):
            bar.update()
            prof = prof_list[i]
            r = prof.data[raxis][:]
            reversed = False
            if raxis != "mass" and raxis != "radius":
                if not reversed:
                    r = r[::-1]
                    reversed = True
            prop = prof.data[property_name][:]
            if num_rings > -1:
                selec = [int(i) for i in np.linspace(0, len(prof.mass) - 1, num_rings)]
                r = r[selec]
                prop = prop[selec]
            if log:
                prop = np.log10(prop)
            width = 0
            for ind, w in enumerate(wedges_list):
                radius = r[ind]
                w.set_radius(radius)
                # Plot rings
                value = prop[ind]
                # Width = current radius - previous radius
                width += radius
                # Center zone should be a circle, not a ring
                if ind == 0:
                    width = None
                w.set_width(width)
                w.set_color(cmap(norm(value)))
                width = -1 * radius
            # Update time label
            if show_time_label:
                time = (prof.star_age * u.yr).to(time_unit)
                text.set_text("t = " + time.round(1).to_string())

            if show_total_mass:
                mass_text.set_text("{}".format(round(prof.star_mass, 1)) + "$\,\\rm{M}_{\odot}$")

            if hrd_inset:
                point.set_data(np.log10(prof.Teff), np.log10(prof.luminosity[0]))
            if show_surface:
                surface.set_radius(r.max())
            if automatic_limits:
                # Update axis size to follow changes in radius
                axis_lim = 1.1 * r.max()
                ax.set_xlim([-axis_lim, axis_lim])
                ax.set_ylim([-axis_lim, axis_lim])
                ax.set_aspect('equal', adjustable='box')
        # Create animation
        ip = m.iterateProfiles(rng=[m.hist.model_number[start_ind], m.hist.model_number[end_ind]], step=ind_step)
        count = 0
        prof_list = []
        print("Loading profiles, this may take some time...")
        bar0 = tqdm()

        for i in ip:
            prof_list.append(m.prof)
            count += 1
            bar0.update()

        bar = tqdm()
        print("Creating movie...")
        ani = FuncAnimation(fig, animate, init_func=init, frames=count, interval=1000 / fps, blit=False, repeat=False)

        # Save animation
        # Fix issues with directory name
        ani.save(output_fname + anim_fmt, writer="ffmpeg", extra_args=['-vcodec', 'libx264'])

    return fig, ax


def chemical_profile(m, time_ind=-1, isotope_list=None, num_rings=-1, scale=-1, width=0.03, raxis="mass",
                     show_ring_annotations=True, fps=10, fig=None, ax=None, show_time_label=True, time_label_loc=(),
                     time_unit="Myr", fig_size=(5.5, 4), axis_lim=1.05, axis_label="", show_colorbar=True,
                     cmap=CMAP_DEFAULT, min_cbar_elem=5, max_cbar_elem=25, show_legend=False,
                     counterclock=True, startangle=90, hrd_inset=True,
                     show_hrd_ticks_and_labels=False, show_total_mass=True, show_surface=False,
                     output_fname="chemical_profile", anim_fmt=".mp4"):
    """Creates chemical profile diagram. 
    
    Represent the model of a stellar object as a circle with radius raxis. The circle contains nested pie charts that
    show the composition of the star at a certain mass or radius coordinate.
    Requires MESA profile files that contain the profiles of certain isotopes, such as "h1" and the corresponding MESA
    history file.
    
    Parameters
    ----------
    m : mesaPlot object
        Already loaded a history file
    time_ind : int or tuple (start_index, end_index, step=1) or (start_index, end_index, step)
        If int: create the plot at the index time_ind. If tuple: create an animation from start index to end index with intervals of step.
    isotope_list : None or list or np.array of str 
        Containing the names of isotopes to be included.
    num_rings : int
        Default -1, if greater than -1, limit the number of nested pie charts to this number
    scale : float
        Value to scale the circle to. If negative, use the maximum value of the raxis.
    width : float
        Minimum width of a nested pie chart ring.
    raxis : str
        Default axis to use as radius of the circle.
    show_ring_annotations: boolean
        If set, add concentric rings on top of the nested pie charts.
    fps : int
        Number of frames per second for the animation.
    fig: Figure object
        If set, plot on existing figure.
    ax : Axes object
        If set, plot on provided axis.
    show_time_label : boolean
        If set, insert a label that gives the age of the stellar object (in Myr).
    time_label_loc : tuple
        Location of the time label on the plot as fraction of the maximal size.
    time_unit : str
        Valid astropy time unit, default Myr.
    fig_size : tuple
        Size of the figure in inches.
    axis_lim : float
        Value to set for the maximum limit of the x and y axis.
    axis_label : str
        Label of the x and y axis.
    show_colorbar : boolean
        If set, add a colorbar that gives the isotopes and corresponding colors.
    cmap : str or matplotlib.colors.ListedColormap
        colormap to use for the isotopes
    min_cbar_elem : int
        Minimum number of isotopes in a colorbar
    max_cbar_elem : int
        Maximum number of isotopes per colorbar
    counterclock : boolean
        If set, plot the isotopes counterclockwise.
    startangle : int or float
        Angle in degrees from the horizontal line at which to start plotting the isotopes.
    hrd_inset : boolean
        If set, add an inset HRD where the location of the current model is indicated with a circle.
    show_hrd_ticks_and_labels : Boolean
        If set, display the axis ticks and labels of the inset HRD
    show_total_mass : boolean
        Default False, display the value of the total mass of the model below the circle.
    show_surface : boolean
        Default True, if set, show the outer boundary of the stellar object.
    show_grid : boolean
        Default False, if set, add additional axes in crosshair form.
    output_fname : str
        Name of the output file.
    anim_fmt : str
        Format to use for saving an animation.
        
    Returns
    -------
    fig, ax
    """
    if fig is None:
        fig = plt.figure()
        fig.set_size_inches(fig_size)
    if ax is None:
        ax = plt.gca()

    start_ind, end_ind, ind_step = check_time_indeces(time_ind, m.hist.star_age)
    prof = find_profile(m, time_ind=start_ind)
    r = prof.data[raxis]
    if scale < 0:
        # Set automatic value for the scale
        scale = r.max()

    # Create nested pie charts of isotopes
    isotope_list, artist_list = make_pie_composition_plot(ax, prof, startangle=startangle, raxis=raxis,
                                                          isotope_list=isotope_list, cmap=cmap, show_colorbar=show_colorbar,
                                                          min_cbar_elem=min_cbar_elem, max_cbar_elem=max_cbar_elem,
                                                          counterclock=counterclock, num_rings=num_rings,
                                                          scale=scale, width=width)
    # Add annotations
    rmax = np.sqrt(r.max()) / np.sqrt(scale)
    if show_ring_annotations:
        c_list, fll, r_list, pll = add_ring_annotations(ax, rmax=rmax, show_percentage=True, show_fraction_labels=False,
                                                        startangle=startangle)

    # Add time label
    if show_time_label:
        time = prof.star_age
        text = add_time_label(time, ax, time_label_loc=time_label_loc, time_unit=time_unit)

    # Set axis for plotting correctly sized circles
    ax.set_xlim([-axis_lim, axis_lim])
    ax.set_ylim([-axis_lim, axis_lim])
    ax.set_aspect('equal', adjustable='box')

    # Add axis label - no default values for axis label
    ax.set_xlabel(axis_label)
    ax.set_ylabel(axis_label)

    # Make sure to show the axis frame
    ax.set(frame_on=True)

    if hrd_inset:
        axins, point = add_inset_hrd(m, ax=ax, time_index=start_ind,
                                     show_hrd_ticks_and_labels=show_hrd_ticks_and_labels)

    # Add mass label
    if show_total_mass:
        mass_text = ax.text(0.87, 0.05, "{}".format(round(prof.star_mass, 1)) +
                            "$\,\\rm{M}_{\odot}$", transform=ax.transAxes, ha="center", va="center")


    if show_surface:
        surface = Wedge((0, 0), rmax, theta1=0, theta2=360, fill=False, facecolor="#FFFDE7",
                        edgecolor='k', lw=1.1, zorder=600)
        ax.add_artist(surface)

    # Create animation
    if end_ind != start_ind:
        def init():
            if show_time_label:
                time = (prof.star_age * u.yr).to(time_unit)
                text.set_text("t = " + time.round(1).to_string())
            for pie in artist_list:
                for w in pie:
                    ax.add_patch(w)
            if show_total_mass:
                mass_text.set_text("".format(round(prof.star_mass, 1)) + "$\,\\rm{M}_{\odot}$")
            if show_surface:
                surface.set_radius(r.max())
            return artist_list

        def animate(i):
            bar.update()
            prof = prof_list[i]
            selec = [int(x) for x in np.linspace(0, len(prof.mass) - 1, num_rings)]
            data = prof.data[selec]
            masses = prof.data[raxis][selec]

            # Update pie charts
            radius = np.sqrt(masses) / np.sqrt(scale)
            if raxis[:3] == "log":
                shift = masses.min() + 1e-7
                radius = np.sqrt(np.abs(masses - shift)) / np.sqrt(np.abs(scale - shift))
            for ind, r_i in enumerate(radius):
                factor = 1
                if ind == len(masses) - 1:
                    factor *= -1
                theta1 = factor * startangle / 360.0

                for elem, w in zip(isotope_list, artist_list[ind]):
                    frac = data[elem][ind]
                    theta2 = (theta1 + frac) if counterclock else (theta1 - frac)
                    w.set_theta1(360. * min(theta1, theta2))
                    w.set_theta2(360. * max(theta1, theta2))
                    w.set_radius(r_i)
                    theta1 = theta2
            # Update time label
            if show_time_label:
                time = (prof.star_age * u.yr).to(time_unit)
                text.set_text("t = " + time.round(1).to_string())

            # Update annotations
            rmax = np.sqrt(masses.max()) / np.sqrt(scale)
            if show_ring_annotations:
                for ind, c in enumerate(c_list):
                    f = FRACTION_LIST[ind]
                    c.set_radius(f * rmax)
                for ind, rad in enumerate(r_list):
                    p = PERCENTAGE_LIST[ind]
                    x = rmax * np.sin(-p * 2 * np.pi)
                    y = rmax * np.cos(-p * 2 * np.pi)
                    rad.set_data([0, x], [0, y])

            if show_total_mass:
                mass_text.set_text("{}".format(round(prof.star_mass, 1)) + "$\,\\rm{M}_{\odot}$")

            if hrd_inset:
                point.set_data(np.log10(prof.Teff), np.log10(prof.luminosity[0]))

            if show_surface:
                surface.set_radius(rmax)

        # Create animation
        ip = m.iterateProfiles(rng=[m.hist.model_number[start_ind], m.hist.model_number[end_ind]], step=ind_step)
        count = 0
        prof_list = []
        print("Loading profiles, this may take some time...")
        bar0 = tqdm()

        for i in ip:
            prof_list.append(m.prof)
            count += 1
            bar0.update()

        bar = tqdm()
        print("Creating movie...")
        ani = FuncAnimation(fig, animate, init_func=init, frames=count, interval=1000 / fps, blit=False, repeat=False)

        # Save animation
        # Fix issues with directory name
        ani.save(output_fname + anim_fmt, writer="ffmpeg", extra_args=['-vcodec', 'libx264'])

    return fig, ax


def animated_hist_comp_test(m1, m2, fig=None, ax=None, raxis="log_R", label1="", label2="", time_index1=0,
                            time_index2=0, hrd_inset=True):
    """ Plot two models together. 
    
    Plot two MESA models at the same time as half-circles with radius r over the same evolutionary time.
    
    Parameters
    ----------
    label2 :
    label1 :
    time_index2 :
    m1 : mesaPlot object
        Already loaded a history file.
    m2 : second mesaPlot object
        Already loaded a history file.
    fig : Figure object
        If set, plot on existing figure.
    ax : Axes object 
        If set, plot on provided axis.
    raxis: str
        Valid column name for a MESA history file. This sets the outer radius of the star.
    time_label_loc : tuple
        Location of the time label on the plot as fraction of the maximal size.
    time_index : int
        Contains time index of moment to plot.
    hrd_inset : boolean
        If set, add an inset HRD that indicates the current time index to each plot.
        
    Returns
    -------
    fig, ax
    """
    if fig is None:
        fig = plt.figure()
        fig.set_size_inches(11, 9)
    if ax is None:
        ax = plt.gca()

    # Normalize the radius from something small but still visible to something large
    # that still fits inside the plot
    r1 = m1.hist.data[raxis][:]   # Create a copy of the array to prevent changes to data
    t1 = m1.hist.star_age
    r2 = m2.hist.data[raxis][:]  # Create a copy of the array to prevent changes to data
    t2 = m2.hist.star_age
    lim = 1.1 * np.max([r1.max(), r2.max()])     # Adapt upper limit maximal radius
    # replace smallest values with constant ratio of 0.003
    smallest_radius_ratio = 0.01
    too_small1 = (r1/lim < smallest_radius_ratio)
    too_small2 = (r2 / lim < smallest_radius_ratio)
    if np.any(too_small2):
        r1[too_small1] = lim * smallest_radius_ratio
        r2[too_small2] = lim * smallest_radius_ratio

    # Add center circle, color is given by T_eff
    colors_ary1 = teff2rgb(10 ** m1.hist.log_Teff)
    colors_ary2 = teff2rgb(10 ** m2.hist.log_Teff)
    color1 = colors_ary1[time_index1]
    color2 = colors_ary2[time_index2]
    wedge1 = Wedge((0, 0), r1[time_index1], 90, 270, width=None, facecolor=color1,
                   edgecolor="k")
    ax.add_artist(wedge1)
    wedge2 = Wedge((0, 0), r2[time_index2], 270, 90, width=None, facecolor=color2,
                   edgecolor="k")
    ax.add_artist(wedge2)

    # Add dashed line to separate both models
    ax.plot([0, 0], [-lim, lim], ls='-', color='grey')

    # Add labels for both models
    ax.text(-lim / 2., 0.88 * lim, label1)
    ax.text(lim / 2., 0.88 * lim, label2)

    # Set axis for plotting correctly sized circles
    ax.set_xlim([-lim, lim])
    ax.set_ylim([-lim, lim])
    ax.set_aspect('equal', adjustable='box')

    set_axis_ticks_and_labels(ax, raxis=raxis)

    if hrd_inset:
        add_inset_hrd(m1, ax=ax, time_index=time_index1)
        add_inset_hrd(m2, ax=ax, time_index=time_index1, loc=4)
    return fig, ax


def animated_hist_comp(m1, m2, raxis="log_R", label1="", label2="", time_index_start1=0, time_index_start2=0,
                       time_index_end1=-1, time_index_end2=-1, time_indices=None, frames=200, fps=10,
                       plot_name_base="mesarings_comp_", plot_dir=".", hrd_inset=True,
                       fig_size=(11, 9)):
    # TODO: find out how to compute same indices. Make sure they have the same size
    # Idea: Scale model number from 0 to 1 and use same fractional time
    # TODO: Accept negative indices
    indices1 = np.linspace(time_index_start1, time_index_end1, frames, dtype=int)
    indices2 = np.linspace(time_index_start2, time_index_end2, frames, dtype=int)

    # Normalize the radius from something small but still visible to something large
    # that still fits inside the plot
    r1 = m1.hist.data[raxis][indices1]   # Create a copy of the array to prevent changes to data
    log_teff1 = m1.hist.log_Teff[indices1]
    log_l1 = m1.hist.log_L[indices1]
    # Second half
    r2 = m2.hist.data[raxis][indices2]  # Create a copy of the array to prevent changes to data
    log_teff2 = m2.hist.log_Teff[indices2]
    log_l2 = m2.hist.log_L[indices2]
    lim = 1.1 * np.max([r1.max(), r2.max()])     # Adapt upper limit maximal radius
    colors_ary1 = teff2rgb(10 ** log_teff1)
    colors_ary2 = teff2rgb(10 ** log_teff2)
    # replace smallest values with constant ratio of 0.003
    # TODO: Fix smallest radius
    smallest_radius_ratio = 0.08
    too_small1 = (r1 / lim < smallest_radius_ratio)
    too_small2 = (r2 / lim < smallest_radius_ratio)
    if np.any(too_small2):
        r1[too_small1] = lim * smallest_radius_ratio
        r2[too_small2] = lim * smallest_radius_ratio

    # Check if directory exists already, otherwise create a new one
    if not path.exists(plot_dir):
        makedirs(plot_dir)

    # Create initial figure
    fig = plt.figure(figsize=fig_size)
    ax = plt.gca()

    # Set axis for plotting correctly sized circles
    ax.set_xlim([-lim, lim])
    ax.set_ylim([-lim, lim])
    ax.set_aspect('equal', adjustable='box')

    set_axis_ticks_and_labels(ax, raxis=raxis)

    # Initial half-stars
    wedge1 = Wedge((0, 0), r1[0], 90, 270, width=None, facecolor=colors_ary1[0],
                   edgecolor="k")
    wedge2 = Wedge((0, 0), r2[0], 270, 90, width=None, facecolor=colors_ary2[0],
                   edgecolor="k")
    # Add inset
    axins1, axins2, point1, point2 = None, None, None, None  # intialize
    if hrd_inset:
        axins1, point1 = add_inset_hrd(m1, ax=ax, time_index=0, indices=indices1)
        axins2, point2 = add_inset_hrd(m2, ax=ax, time_index=0, indices=indices2, loc=4)

    # Add dashed line to separate both models
    ax.plot([0, 0], [-lim, lim], ls='-', color='grey')

    # Add labels for both models
    ax.text(-lim / 2., 0.88 * lim, label1)
    ax.text(lim / 2., 0.88 * lim, label2)

    def init():
        wedge1.set_radius(r1[0])
        wedge2.set_radius(r2[0])
        wedge1.set_facecolor(colors_ary1[0])
        wedge2.set_facecolor(colors_ary2[0])
        ax.add_patch(wedge1)
        ax.add_patch(wedge2)
        return wedge1, wedge2, point1, point2

    def animate(ind):
        bar.update()
        wedge1.set_radius(r1[ind])
        wedge2.set_radius(r2[ind])
        wedge1.set_facecolor(colors_ary1[ind])
        wedge2.set_facecolor(colors_ary2[ind])

        if hrd_inset:
            point1.set_data(log_teff1[ind], log_l1[ind])
            point2.set_data(log_teff2[ind], log_l2[ind])

        return wedge1, wedge2, point1, point2

    # Create animation
    bar = tqdm(total=frames)

    # TODO: Fix frames to match length of arrays
    ani = FuncAnimation(fig, animate, init_func=init, frames=frames, interval=1000 / fps, blit=False, repeat=False)
    # Save animation
    # Fix issues with directory name
    if plot_dir[-1] != '/':
        plot_dir += '/'
    # Fix issue with plot name
    if plot_name_base[-1] != '_':
        plot_name_base += '_'
    ani.save(plot_dir + plot_name_base + "movie.mp4", writer="ffmpeg", extra_args=['-vcodec', 'libx264'])

# ----------- Helper functions ----------------------


def find_profile(m, time_ind=0):
    """Load closest MESA profile.
    
    Loads the MESA profil closest to the time_ind given.
    
    Parameters
    ----------
    m : object
        mesaPlot object
    
    time_ind: int
        index of mesaPlot history
    
    Returns
    -------
    m.prof : profile
        MESA profile
    """
    model_number = m.hist.model_number[time_ind]
    m.loadProfile(num=model_number)
    return m.prof

def find_closest(ary, value):
    return np.abs(ary - value).argmin()

def set_axis_ticks_and_labels(ax, raxis="star_mass", axis_label=""):
    """ Format axis ticks.
    
    Format the axis ticks such that no negative values are shown.
    
    Parameters
    ----------
    ax : matplotlib axis object
    raxis: str
        Valid column name for a MESA history file. This sets the value used for the outer radius of the star.
    axis_label : str
        User defined axis label.
        
    Returns
    -------
    None
    """
    # Set axis properties
    label = axis_label

    if label == "":
        label = raxis
        if raxis == "log_R" or raxis == "radius":
            label = "Radius" + "$ \,[\\rm{R}_\odot]$"
        elif raxis == "star_mass" or raxis == "mass":
            label = "Mass" + "$\,[\\rm{M}_\odot]$"
        elif "_" in label:
            label = label.replace("_", " ")
    ax.set_xlabel(label)
    ax.set_ylabel(label)
    # Change number of ticks to avoid excessive number
    plt.locator_params(nbins=6)
    ax.xaxis.set_major_locator(plt.MaxNLocator(6))
    ax.yaxis.set_major_locator(plt.MaxNLocator(6))
    # Change y tick labels
    if raxis[:3] == "log":
        ticks = ax.get_yticks()
        new_ticks = []
        for t in ticks:
            if abs(t) < 1:
                new = '{:.2g}'.format(abs(np.sign(t)) * 10 ** abs(t))
            else:
                new = '{:.0f}'.format(abs(np.sign(t)) * 10 ** abs(t))
            new_ticks.append(new)
        ax.set_xticks(ticks)
        ax.set_yticks(ticks)
        ax.set_yticklabels(new_ticks)
        ax.set_xticklabels(new_ticks)
    else:
        ticks = ax.get_yticks()
        min_tick = abs(ax.get_xticks().min())
        new_ticks = ['{:.1f}'.format(abs(t)) for t in ticks]
        if min_tick < 1:
            new_ticks = ['{:.2g}'.format(abs(t)) for t in ticks]
        ax.set_xticks(ticks)
        ax.set_yticks(ticks)
        ax.set_yticklabels(new_ticks)
        ax.set_xticklabels(new_ticks)


def add_inset_hrd(m, time_index=100, ax=None, axins=None, fraction="20%", indices=None,
                  loc="lower left", bbox_to_anchor=None, show_hrd_ticks_and_labels=False):
    """ Add inset HRD.
    
    Add an inset HRD to a plot that highlights the current time-step.
    
    Parameters
    ----------
    m : mesaPlot object
    ax : axis object
    indices : None, list or ndarray
        Selected indices for plotting
    fraction : string
        Fraction of the parent axis used for setting the size of the inset
    axins : None or Axes
        If provided, inset axis to use.
    time_index : int
        Time index to highlight on inset plot.
    loc : str or int
        Matplotlib location to put the inset axis on the parent axis.
    bbox_to_anchor : tuple (x, y, width, height)
        Bounding box for the axis
    show_hrd_ticks_and_labels : Boolean
        If set, display the axis ticks and labels of the inset HRD
    Returns
    -------
    (axins, point): Axes
        Created inset axis, and the point moving on the plot.
    """
    # TODO: adapt to only show chosen range of time_ind
    if ax is None:
        ax = plt.gca()
    if indices is None:
        indices = np.arange(len(m.hist.log_Teff))

    if axins is None:
        axins = inset_axes(ax,
                           width=fraction,  # width = % of parent_bbox
                           height=fraction,  # height : 1 inch
                           loc=loc,
                           bbox_to_anchor=bbox_to_anchor
                           )
        axins.invert_xaxis()
        # move axis ticks
        axins.tick_params(axis='y', which='both', labelright=True, labelleft=False, direction='in')
        axins.tick_params(axis='x', which='both', labeltop=True, labelbottom=False, direction='in')
        axins.yaxis.set_ticks_position('right')
        axins.xaxis.set_ticks_position('top')

        # Add labels
        if show_hrd_ticks_and_labels:
            axins.set_xlabel("$\log_{10}(T_{\\rm{eff}}/\\mathrm{K})$",
                             fontsize=int(0.45 * plt.rcParams.get("font.size")))
            axins.set_ylabel("$\log_{10}(L/\\mathrm{L}_{\\odot})$", rotation=90,
                             fontsize=int(0.45 * plt.rcParams.get("font.size")))
            axins.yaxis.set_label_position('right')
            axins.xaxis.set_label_position('top')
            plt.setp(axins.get_xticklabels(),
                     fontsize=int(0.36 * plt.rcParams.get("font.size")))
            plt.setp(axins.get_yticklabels(),
                     fontsize=int(0.36 * plt.rcParams.get("font.size")))
            # fix the number of ticks on the inset axes
            axins.yaxis.get_major_locator().set_params(nbins=3)
            axins.xaxis.get_major_locator().set_params(nbins=3)
        else:
            axins.xaxis.set_ticks([])
            axins.yaxis.set_ticks([])
        # For better output, use all the models within the range selected for the background evolution on the HRD
        axins.plot(m.hist.log_Teff[indices[0]:indices[-1] + 1], m.hist.log_L[indices[0]:indices[-1] + 1], "b", lw=1.25)

    # Add marker for current location
    point, = axins.plot([m.hist.log_Teff[indices][time_index]], [m.hist.log_L[indices][time_index]], ls=None,
                        marker="o", color="yellow", mec="k", mew=1, alpha=0.6)
    return axins, point


def teff2rgb(t_ary):
    """Convert effective temperature to rgb colors.
    
    Convert effective temperature to rgb colors using colorpy.
    
    Parameters
    ----------
    t_ary : array
        Temperature array in K.
    
    Returns
    -------
    rgb_list: array
        Array with rgb colors. 
    """
    rgb_list = []
    for t in t_ary:
        rgb_list.append(colormodels.irgb_string_from_xyz(blackbody.blackbody_color(t)))
    return rgb_list


def colorbar(mappable, ax=None, size=None, pad=None, cax=None, orientation="vertical", **kwargs):
    # Trick from Joseph Long
    if ax is None:
        ax = mappable.axes
    fig = ax.figure
    divider = None
    if cax == None:
        divider = make_axes_locatable(ax)
        if orientation == "horizontal":
            if size is None:
                size = "20%"
            if pad is None:
                pad = 0.4
            cax = divider.append_axes("bottom", size=size, pad=pad)
        elif orientation == "vertical":
            if size is None:
                size = "10%"
            if pad is None:
                pad = 0.05
            cax = divider.append_axes("right", size=size, pad=pad)
        else:
            raise ValueError("Wrong value of orientation")
    return fig.colorbar(mappable, cax=cax, orientation=orientation, **kwargs), divider


def make_pie_composition_plot(ax, prof, num_rings=0, scale=11.0, width=0.01, startangle=90,
                              isotope_list=None, cmap=None, show_colorbar=True, min_cbar_elem=5, max_cbar_elem=25,
                              counterclock=True, raxis="mass", boundary=0, log_low_lim=-2.1):
    """ Create composition plot. 
    
    Create a composition plot showing the percentage of composition for each element in each layer of the star.
    
    Parameters
    ----------
    ax : axis object
    prof: mesaPlot profile object
    num_rings : int
        Number of rings to plot. 
    scale : float
        Value to scale the plot to.
    width : float
        Width of each nested piechart.
    startangle : float
        Value of the angle to start with for the piecharts.
    isotope_list : None or list
        List of isotopes to take into account.
    counterclock : bool, optional
        Default: True, specify fractions direction, clockwise or counterclockwise.
    show_colorbar : boolean
        If set, add a colorbar that gives the isotopes and corresponding colors.
    cmap : str or matplotlib.colors.ListedColormap
        colormap to use for the isotopes
    min_cbar_elem : int
        Minimum number of isotopes in a colorbar
    max_cbar_elem : int
        Maximum number of isotopes per colorbar
    Returns
    -------
    elem_list, artists
    """
    if isotope_list is None:
        isotope_list = get_isotopes_from_prof(prof)
    if cmap is None:
        if len(isotope_list) == 19:
           cmap = CMAP_BASE
        elif len(isotope_list) == 89:
            cmap = CMAP_HEAVY
        else:
            cmap = plt.get_cmap(CMAP_DEFAULT, len(isotope_list))
    elif type(cmap) == str:
        cmap = plt.get_cmap(cmap, len(isotope_list))
    elif type(cmap) is not ListedColormap:
        raise ValueError("cmap must be a valid colormap string or a matplotlib colormap")
    cmap_list = cmap(np.linspace(0, 1, len(isotope_list)))
    masses = prof.data[raxis]

    # Set limits of radial axis
    lim = 0
    if boundary > 0:
        lim = np.where(masses <= boundary)[0][0]
    low_lim = len(masses)
    if raxis[:3] == "log":
        low_lim = np.where(masses <= log_low_lim)[0][0]

    if num_rings > 0:
        selec = [int(i) for i in np.linspace(lim, low_lim - 1, num_rings)]
        data = prof.data[selec]
        masses = masses[selec]
    else:
        data = prof.data[lim:low_lim]
        masses = masses[lim:low_lim]
    artists = []
    radius = np.sqrt(np.abs(masses)) / np.sqrt(np.abs(scale))
    if raxis[:3] == "log":
        shift = masses.min() + 1e-7
        radius = np.sqrt(np.abs(masses - shift)) / np.sqrt(np.abs(scale - shift))
    for ind, r in enumerate(radius):
        vals = []
        for elem in isotope_list:
            vals.append(data[elem][ind])
        # Fix problem with center zone
        if ind == len(masses) - 1:
            startangle *= -1
        pie = ax.pie(vals, radius=r, colors=cmap_list, startangle=startangle,
                     wedgeprops=dict(width=width, antialiased=True, linestyle="None"),
                     counterclock=counterclock, normalize=True)
        artists.append(pie[0])    # return Wedges only
    ax.set(aspect="equal")

    # Add color bar or legend for isotopes
    if show_colorbar:
        create_elem_colorbars(isotope_list, ax, cmap=cmap, min_cbar_elem=min_cbar_elem, max_cbar_elem=max_cbar_elem)

    return isotope_list, artists


def make_property_plot(ax, prof, property_name="logRho", raxis="mass", num_rings=-1, cmin=-5, cmax=10, log=False,
                       cmap="plasma", theta1=0, theta2=360, log_low_lim=1e-20):
    """ Create property plot.
    
    Plot a circle containing concentric rings with a color that corresponds to the evolution of a property.
    
    Parameters
    ----------
    ax : axis object
    prof: mesaPlot profile object
    property_name: string
        Default logRho, existing quantity in the MESA profile.
    raxis : string
        Default axis to use as radius representation. Any linear property can be used instead (for example radius). 
    num_rings : int
        Default -1, if greater than -1, limit the number of rings to this number.
    theta1 : int or float
        Start angle for the wedge (in degrees).
    theta2 : int or float
        End angle for the wedge (in degrees).
    cmap : str or matplotlib.colors.ListedColormap
        Colormap to use for the property
    cmin : float
        Minimum value to set for the colorbar.
    cmax : float
        Maximum value to set for the colorbar, if smaller or equal to cmin, use the minimum and maximum values of property_name instead.
    log : boolean
        If set, show the natural logarithm of the property.
    log_low_lim : float
        Value to replace zero and negative values in a property with
    Returns
    -------
    List of artists created in the plot
    """
    r = prof.data[raxis][:]
    if raxis != "mass" and raxis != "radius":
        r = r[::-1]

    prop = prof.data[property_name][:]
    if num_rings > -1:
        selec = [int(i) for i in np.linspace(0, len(prof.mass) - 1, num_rings)]
        r = r[selec]
        prop = prop[selec]
    if log:
        # Replace zero and negative values with fill value
        prop[prop <= 0] = log_low_lim
        prop = np.log10(prop)

    if type(cmap) == str:
        cmap = plt.get_cmap(cmap, len(prop))
    norm = Normalize(vmin=cmin, vmax=cmax)
    artist_list = []
    width = 0
    for ind, r_ind in enumerate(r):
        # Plot burning regions
        radius = r_ind
        value = prop[ind]
        # Width = current radius - previous radius
        width += radius
        color = cmap(norm(value))
        # Center zone should be a circle, not a ring
        if ind == 0:
            width = None
        wedge = Wedge((0, 0), radius, theta1=theta1, theta2=theta2, width=width, color=color)
        ax.add_artist(wedge)
        artist_list.append(wedge)
        width = -1 * radius

    return artist_list


def add_ring_annotations(ax, rmax, fraction_list=None, show_fraction=True, show_fraction_labels=True,
                         use_actual_mass_fraction=True, percentage_list=None, show_percentage=False,
                         show_percentage_labels=False,
                         startangle=90, counterclock=True, loc=1.25, **kwargs):
    """ Add concentric circles. 
    
    Add concentric circles on an axis that indicate the fraction of the maximum radius given. Optionally,
    indications of percentages can also be given.
    
    Parameters
    ----------
    ax : matplotlib axis object
    rmax : float
        Value of the maximum radius of the circle to compare to as a reference
    fraction_list: list
        Default None, list of floats giving the fractions of the total mass.
    show_fraction : boolean
        Default True, whether or not to plot circles that have radii of a fraction of the reference circle radius.
    show_fraction_labels: boolean
        Default True, whether or not to add labels indication the fractions.
    use_actual_mass_fraction: boolean
        Default True, whether or not to locate the fraction circles at the location where a circle contains this mass or at a fraction of `rmax`.
    percentage_list : list
        Default None, list of floats giving the percentages to add.
    show_percentage : boolean
        Default False, whether to plot radial lines indicating a certain percentage.
    show_percentage_labels : boolean
        Default False, whether or not to add labels indicating percentages.
    startangle : float
        Value of the angle to start with for the percentages.
    counterclock: bool, optional
        Default: True, specify percentage direction, clockwise or counterclockwise.
    loc: float
        Default 1.25, location of percentage labels in units of fraction of `rmax`.
        
    Returns
    -------
    List of matplotlib artists created
    """
    circle_list = []
    fraction_label_list = []
    rays_list = []
    percentage_label_list = []
    if show_fraction:
        # Plot 4 rings by default
        if fraction_list is None:
            fraction_list = FRACTION_LIST
        for f in fraction_list:
            factor = np.sqrt(f)
            if not use_actual_mass_fraction:
                factor = f
            a = plt.Circle((0, 0), factor * rmax, fill=False, ec="0.7", linewidth=1.2, zorder=500)
            ax.add_artist(a)
            circle_list.append(a)
        if show_fraction_labels:
            for f in fraction_list:
                t = ax.text(0.7 * factor * rmax, 0.7 * np.sqrt(f) * rmax, str(f), color="k",
                            fontsize=10, ha="left", va="bottom", **kwargs)
                fraction_label_list.append(t)
    if show_percentage:
        # TODO: add startangle and counterclock option
        if percentage_list is None:
            percentage_list = PERCENTAGE_LIST
        for p in percentage_list:
            x = rmax * np.sin(-p * 2 * np.pi)
            y = rmax * np.cos(-p * 2 * np.pi)
            l, = ax.plot([0, x], [0, y], "0.7", lw=1.2, zorder=500)
            rays_list.append(l)
            if show_percentage_labels:
                t = ax.text(loc * x, loc * y, str(p * 100) + "\%", fontsize=10, color="0.8", ha='center',
                            va="center", **kwargs)
                percentage_label_list.append(t)
    artist_list = [circle_list, fraction_label_list, rays_list, percentage_label_list]
    return artist_list


def add_time_label(age, ax, time_label_loc=None, time_unit="Myr"):
    """ Add time label.
    
    Add a time label in the upper left corner of a diagram.
    
    Parameters
    ----------
    age : float
        Age of the stellar object.
    ax : matplotlib Axes object
    time_label_loc : None or tuple 
        Default None, the custom location of the time label in units of the Axes coordinate; (0, 0) is bottom left of the axes, and (1, 1) is top right of the axes
    time_unit: str
        Unit of the time. 
    
    Returns
    -------
    matplotlib Artist object
    """
    # If location not specified, place it in the upper left corner
    if len(time_label_loc) == 0:
        time_label_loc = (0.05, 0.95)

    time = (age * u.yr).to(time_unit)
    text = ax.text(time_label_loc[0], time_label_loc[1], "t = " + time.round(1).to_string(),
                   transform=ax.transAxes)
    return text


def check_time_indeces(time_ind, star_age):
    """Check time indices.
    
    Check if time indices are correctly set and define start_ind and end_ind.
    
    Parameters
    ----------
    time_ind: int or tuple (start_index, end_index, step=1) or (start_index, end_index, step)
        If int: create the plot at the index `time_ind`.
    star_age: array
        Ages of star from MESA history file
    
    Returns
    -------
    start_ind, end_ind, ind_step
    """
    if type(time_ind) is not tuple and type(time_ind) is not list and type(time_ind) is not np.ndarray:
        start_ind = int(time_ind)
        if start_ind < 0:
            start_ind += len(star_age)
        end_ind = start_ind
        ind_step = 1
    elif len(time_ind) == 2 or len(time_ind) == 3:
        start_ind = int(time_ind[0])
        end_ind = int(time_ind[1])

        # Make sure all indices are positive
        if start_ind < 0:
            start_ind += len(star_age)
        if end_ind < 0:
            end_ind += len(star_age)

        if start_ind == end_ind:
            # Issue warning when same values for start and end index
            raise Warning("No animation will be created because the start and end index have the same value")

        ind_step = 1
        if len(time_ind) == 3:
            ind_step = int(time_ind[2])
            if ind_step <= 0:
                raise ValueError("ind_step must be an integer larger than 0")
    else:
        raise TypeError("time_index must be an integer or a tuple of integers (start_ind, end_ind, step=1)")

    return start_ind, end_ind, ind_step


def rescale_time(indices, m, time_scale_type="model_number"):
    """Rescale the time.
    
    Rescale time indices depending on the time_type.
    
    Parameters
    ----------    
    indices : np.array or list of int
        Containing selected indices.
    m : mesa Object
    time_scale_type : str
        One of `model_number`, `linear`, or `log_to_end`. For `model_number`, the time follows the moment when a new MESA model was saved. For `linear`, the time follows linear steps in star_age. For `log_to_end`, the time axis is tau = log10(t_final - t), where t_final is the final star_age of the model.
    
    Returns
    -------
    ind_select : list
        New list of indices that reflect the rescaling in time.
    """
    age = m.hist.star_age
    if time_scale_type == "model_number":
        return indices
    elif time_scale_type == "linear":
        val_select = np.linspace(age[indices[0]], age[indices[-1]], len(indices))
        ind_select = [find_closest(val, age) for val in val_select]
        return ind_select
    elif time_scale_type == "log_to_end":
        time_diff = (age[-1] - age)
        # Avoid invalid values for log
        time_diff[time_diff <= 0] = 1e-5
        logtime = np.log10(time_diff)
        # Find indices
        val_select = np.linspace(logtime[indices[0]], logtime[indices[-1]], len(indices))
        ind_select = [find_closest(val, logtime) for val in val_select]
        return ind_select
    else:
        raise ValueError('Invalid time_type. Choose one of "model_number", "linear", or "log_to_end"')


def too_dark(color_ary):
    """Check if text too dark

    Check whether dark text can be overlayed on colors in an array of RGBA colors.

    Parameters
    ----------
    color_ary : np.array or list of RGBA color arrays

    Returns
    -------
    final_ary : list
        New list of Booleans.
    """
    final_ary = []
    for c in color_ary:
        r, g, b = c[0], c[1], c[2]
        luma = 0.2126 * r + 0.7152 * g + 0.0722 * b;  # per ITU-R BT.709 https://stackoverflow.com/questions/12043187/how-to-check-if-hex-color-is-too-black
        if luma < 0.55:
            final_ary.append(True)
        else:
            final_ary.append(False)
    return final_ary


def chem_elem_notation(elem_list):
    """Make LateX formatted elements

    Change list of isotopes into LateX formatted list of isotopes

    Parameters
    ----------
    elem_list : np.array or list of RGBA color arrays

    Returns
    -------
    new_list : list
        New list of str that are laTeX formatted.
    """
    new_list = []
    for elem in elem_list:
        name = re.search(r'^[a-zA-Z]+', elem).group().capitalize()
        num = re.search(r'\d+', elem).group()
        new_list.append("$^{{{0}}}\mathrm{{{1}}}$".format(num, name))
    return new_list


def num_cbar_elem(num_elems, min_cbar_elem=5, max_cbar_elem=25):
    """Calculate number of colorbars

    Based on the maximum and minum number of elements per colorbar,
    compute the number of colorbars and elements per colorbar that will be displayed

    Parameters
    ----------
    num_elems : int
        Number of isotopes to add to the colorbar
    min_cbar_elem : int
        Minimum number of isotopes in a colorbar
    max_cbar_elem : int
        Maximum number of isotopes per colorbar

    Returns
    -------
    num_cbar : int
        Number of colorbars needed
    elem_per_cbar : list
        List of the number of isotopes per colorbar
    """
    if type(num_elems) is not int or type(max_cbar_elem) is not int or type(min_cbar_elem) is not int:
        raise ValueError("Entries must be positive integers")
    if num_elems <= 0 or max_cbar_elem <= 0 or min_cbar_elem <= 0:
        raise ValueError("Entries must be positive integers")
    num_cbar = 0
    elem_per_cbar = []
    if num_elems <= max_cbar_elem:
        num_cbar = 1
        elem_per_cbar.append(num_elems)
    else:
        # Fill colorbars with elements until a last max_cbar_elements + rest is left
        num_cbar += num_elems // max_cbar_elem - 1
        elem_per_cbar = [max_cbar_elem for i in range(num_cbar)]
        # Add rest
        mod = num_elems % max_cbar_elem
        if mod == 0:
            num_cbar += 1
            elem_per_cbar.append(max_cbar_elem)
        elif mod >= min_cbar_elem:
            num_cbar += 2
            elem_per_cbar.append(max_cbar_elem)
            elem_per_cbar.append(mod)
        elif mod < min_cbar_elem:
            num_cbar += 2
            elem_cbar1 = (max_cbar_elem + mod) // 2
            elem_cbar2 = max_cbar_elem + mod - elem_cbar1
            elem_per_cbar.append(elem_cbar1)
            elem_per_cbar.append(elem_cbar2)
    assert len(elem_per_cbar) == num_cbar
    assert np.sum(elem_per_cbar) == num_elems
    return num_cbar, elem_per_cbar


def create_elem_colorbars(isotope_list, ax, cmap=CMAP_DEFAULT, min_cbar_elem=5, max_cbar_elem=25, orientation="vertical"):
    """Create colorbar for isotopes

    Create colorbars containing labels of isotopes for chemical_profile plots

    Parameters
    ----------
    isotope_list : list
        List of isotopes to plot
    ax : matplotlib.Axes object
        The current axis to plot on
    cmap : str or matplotlib.colors.ListedColormap
        colormap to use for the isotopes
    min_cbar_elem : int
        Minimum number of isotopes in a colorbar
    max_cbar_elem : int
        Maximum number of isotopes per colorbar

    Returns
    -------
    cbar_list : list
       List of colorbar objects
    """
    num_elem = len(isotope_list)
    num_cbar, elem_per_cbar = num_cbar_elem(num_elem, min_cbar_elem=min_cbar_elem, max_cbar_elem=max_cbar_elem)
    cbar_list = []
    divider = None
    cax = None
    start_elem = 0
    norm = Normalize(0, len(isotope_list))
    for ind in range(num_cbar):
        cur_num_elem = elem_per_cbar[ind]
        end_elem = start_elem + cur_num_elem
        # Use a subset of the colormap
        cmap_cur = cmr.get_sub_cmap(cmap, norm(start_elem), norm(end_elem), N=cur_num_elem)
        cmap_list = cmap_cur(np.linspace(0, 1, cur_num_elem))
        sm = plt.cm.ScalarMappable(norm=norm, cmap=cmap_cur)
        if ind == 0:
            cbar, divider = colorbar(sm, ax=ax, cax=cax, orientation=orientation)
        else:
            if orientation == "vertical":
                cax = divider.append_axes("right", size="10%", pad=0.05)
            elif orientation == "horizontal":
                cax = divider.append_axes("bottom", size="20%", pad=0.05)
            cbar, div2 = colorbar(sm, ax=ax, cax=cax, orientation=orientation)
        cbar.ax.get_yaxis().set_ticks([])
        cbar.ax.get_xaxis().set_ticks([])
        # Display element labels on top of the corresponding color
        h = 1. / cur_num_elem
        formated_elems = chem_elem_notation(isotope_list[start_elem:end_elem + 1])
        for ind, elem, istoodark in zip(range(cur_num_elem), formated_elems, too_dark(cmap_list)):
            if orientation == "vertical":
                y = h / 2. + ind * h
                x = 0.5
            elif orientation == "horizontal":
                x = h / 2. + ind * h
                y = 0.5
            else:
                raise ValueError("Invalid value for orientation")
            text_color = "k"
            if istoodark:
                text_color = "w"
            cbar.ax.text(x, y, elem, ha='center', va='center', color=text_color,
                         transform=cbar.ax.transAxes, fontsize=int(0.45 * plt.rcParams.get("font.size")))
        cbar_list.append(cbar)
        start_elem = end_elem
    return cbar_list


def get_isotopes(m):
    """Get list of isotopes

    Get the complete list of isotopes in a MESA model. Requires MESA profiles to be available.

    Parameters
    ----------
    m: mesaPlot object
        The current MESA model

    """
    prof = m.prof
    # Check if profile already loaded
    if not hasattr(prof, "initial_mass"):
        prof = find_profile(m, time_ind=0)
    return get_isotopes_from_prof(prof)


def get_isotopes_from_prof(prof):
    """Get list of isotopes

    Get the complete list of isotopes in a MESA model. Requires MESA profiles to be available.

    Parameters
    ----------
    prof: mesaPlot.prof object
        The current MESA profile

    """
    elem_list = p._listAbun(prof)
    # Remove "neut", "prot", and ionized hydrogen from the list of isotopes
    if "neut" in elem_list:
        elem_list.remove("neut")
    if "prot" in elem_list:
        elem_list.remove("prot")
    if "h1_1" in elem_list:
        elem_list.remove("h1_1")
    return elem_list
