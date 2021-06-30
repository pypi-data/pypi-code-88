import numpy as np
from . import plt
from .parameters import my_dpi
from .. import combinations as cc_combinations
from .. import format as cc_format
from .. import check as cc_check


def single_plot_single_format_single_figure(
        x, y, width=0.6, bottom=None, align='center', color='b', color_edge=None, width_edge=None,
        error_bars_x=None, error_bars_y=None, color_error_bars=None, size_caps=5, log=False,
        title=None, fontsize_title=None, rotation_title=None,
        label_x=None, fontsize_label_x=None, rotation_label_x=None,
        label_y=None, fontsize_label_y=None, rotation_label_y=None,
        labels_ticks_x=None, ticks_x=None, n_ticks_x=None,
        stagger_labels_ticks_x=False, fontsize_labels_ticks_x=None, rotation_labels_ticks_x=None,
        labels_ticks_y=None, ticks_y=None, n_ticks_y=None,
        stagger_labels_ticks_y=False, fontsize_labels_ticks_y=None, rotation_labels_ticks_y=None,
        ax=None, n_pixels_x=300, n_pixels_y=300, legend=False, label_legend='', location_legend='best',
        tight_layout=True):

    """

    Parameters
    ----------
    x
    y
    width
    bottom
    align
    color
    color_edge
    width_edge
    error_bars_x
    error_bars_y
    color_error_bars
    size_caps
    log
    title
    fontsize_title
    rotation_title
    label_x
    fontsize_label_x
    rotation_label_x
    label_y
    fontsize_label_y
    rotation_label_y
    labels_ticks_x
    ticks_x
    n_ticks_x
    stagger_labels_ticks_x
    fontsize_labels_ticks_x
    rotation_labels_ticks_x
    labels_ticks_y
    ticks_y
    n_ticks_y
    stagger_labels_ticks_y
    fontsize_labels_ticks_y
    rotation_labels_ticks_y
    ax
    n_pixels_x
    n_pixels_y
    legend
    label_legend
    location_legend
    tight_layout

    Returns
    -------

    """

    if ax is None:
        figures_existing = plt.get_fignums()
        n_figures_new = 1
        i = 0
        f = 0
        while f < n_figures_new:
            if i in figures_existing:
                pass
            else:
                id_figure = i
                f += 1
            i += 1
        fig = plt.figure(
            id_figure, frameon=False, dpi=my_dpi,
            figsize=(n_pixels_x / my_dpi, n_pixels_y / my_dpi))
        ax = plt.gca()
    else:
        fig = ax.figure

    ax.bar(
        x, y, width=width, bottom=bottom, align=align, color=color, edgecolor=color_edge, linewidth=width_edge,
        xerr=error_bars_x, yerr=error_bars_y, ecolor=color_error_bars, capsize=size_caps,
        log=log, label=label_legend)

    if title is not None:
        ax.set_title(title, fontsize=fontsize_title, rotation=rotation_title)
    if label_x is not None:
        ax.set_xlabel(label_x, fontsize=fontsize_label_x, rotation=rotation_label_x)
    if label_y is not None:
        ax.set_ylabel(label_y, fontsize=fontsize_label_y, rotation=rotation_label_y)

    ticks_x_are_applied = False
    if labels_ticks_x is None:
        # max_x = data.shape[dict_axes['x']] - 1
        if ticks_x is None:
            if n_ticks_x is None:
                pass
            else:
                max_x = x.max()
                min_x = x.min()
                n_labels_ticks_x = n_ticks_x
                delta_x = (max_x - min_x) / (n_labels_ticks_x - 1)
                tick_x_lower = min_x
                tick_x_higher = max_x
                ticks_x = np.arange(tick_x_lower, tick_x_higher + delta_x, delta_x)
                ax.set_xticks(ticks_x)
                ticks_x_are_applied = True
        else:
            ax.set_xticks(ticks_x)
            ticks_x_are_applied = True

        if stagger_labels_ticks_x or (fontsize_labels_ticks_x is not None) or (rotation_labels_ticks_x is not None):
            fig.canvas.draw()
            tmp_labels_ticks_x = ax.get_xticklabels()[1:-1:1]
            n_labels_ticks_x = len(tmp_labels_ticks_x)
            labels_ticks_x = [None] * n_labels_ticks_x
            for l, label_l in enumerate(tmp_labels_ticks_x):
                labels_ticks_x[l] = label_l.get_text()

    if labels_ticks_x is not None:
        if not ticks_x_are_applied:
            if ticks_x is None:
                max_x = x.max()
                min_x = x.min()
                n_labels_ticks_x = len(labels_ticks_x)
                delta_x = (max_x - min_x) / (n_labels_ticks_x - 1)
                tick_x_lower = min_x
                tick_x_higher = max_x
                ticks_x = np.arange(tick_x_lower, tick_x_higher + delta_x, delta_x)

            ax.set_xticks(ticks_x)
        if stagger_labels_ticks_x:
            labels_ticks_x = (
                [l if not i % 2 else '\n' + l for i, l in enumerate(labels_ticks_x)])
        ax.set_xticklabels(
            labels_ticks_x, fontsize=fontsize_labels_ticks_x,
            rotation=rotation_labels_ticks_x)

    ticks_y_are_applied = False
    if labels_ticks_y is None:
        # max_y = data.shape[dict_axes['y']] - 1
        if ticks_y is None:
            if n_ticks_y is None:
                pass
            else:
                max_y = y.max()
                min_y = y.min()
                n_labels_ticks_y = n_ticks_y
                delta_y = (max_y - min_y) / (n_labels_ticks_y - 1)
                tick_y_lower = min_y
                tick_y_higher = max_y
                ticks_y = np.arange(tick_y_lower, tick_y_higher + delta_y, delta_y)
                ax.set_yticks(ticks_y)
                ticks_y_are_applied = True

        else:
            ax.set_yticks(ticks_y)
            ticks_y_are_applied = True

        if stagger_labels_ticks_y or (fontsize_labels_ticks_y is not None) or (rotation_labels_ticks_y is not None):
            fig.canvas.draw()
            tmp_labels_ticks_y = ax.get_yticklabels()[1:-1:1]
            n_labels_ticks_y = len(tmp_labels_ticks_y)
            labels_ticks_y = [None] * n_labels_ticks_y
            for l, label_l in enumerate(tmp_labels_ticks_y):
                labels_ticks_y[l] = label_l.get_text()

    if labels_ticks_y is not None:
        if not ticks_y_are_applied:
            if ticks_y is None:
                max_y = y.max()
                min_y = y.min()
                n_labels_ticks_y = len(labels_ticks_y)
                delta_y = (max_y - min_y) / (n_labels_ticks_y - 1)
                tick_y_lower = min_y
                tick_y_higher = max_y
                ticks_y = np.arange(tick_y_lower, tick_y_higher + delta_y, delta_y)

            ax.set_yticks(ticks_y)
        if stagger_labels_ticks_y:
            labels_ticks_y = (
                [l if not i % 2 else '\n' + l for i, l in enumerate(labels_ticks_y)])
        ax.set_yticklabels(
            labels_ticks_y, fontsize=fontsize_labels_ticks_y,
            rotation=rotation_labels_ticks_y)

    if legend:
        if isinstance(location_legend, np.ndarray):
            ax.legend(loc=location_legend.tolist())
        else:
            ax.legend(loc=location_legend)

    if tight_layout:
        plt.tight_layout()


def single_plot_multi_formats_single_figure(
        x, y, axes,
        widths=None, width=0.8, delta_x_formats=0.1,
        bottom=None, align='center', colors='b', colors_edges=None, widths_edges=None,
        error_bars_x=None, error_bars_y=None, colors_error_bars=None, sizes_caps=5, log=False,
        title=None, fontsize_title=None, rotation_title=None,
        label_x=None, fontsize_label_x=None, rotation_label_x=None,
        label_y=None, fontsize_label_y=None, rotation_label_y=None,
        labels_ticks_x=None, ticks_x=None, n_ticks_x=None,
        stagger_labels_ticks_x=False, fontsize_labels_ticks_x=None, rotation_labels_ticks_x=None,
        labels_ticks_y=None, ticks_y=None, n_ticks_y=None,
        stagger_labels_ticks_y=False, fontsize_labels_ticks_y=None, rotation_labels_ticks_y=None,
        ax=None, n_pixels_x=300, n_pixels_y=300,
        legend=False, labels_legend='', location_legend='best', tight_layout=True):

    # raise NotImplementedError

    # format axes
    keys_axes_expected = np.asarray(['formats', 'bars'], dtype=str)
    values_axes_expected = np.arange(2)
    if not isinstance(axes, dict):
        raise TypeError('The type of "axes" has to be dict')
    else:
        keys_axes, values_axes = cc_format.dict_to_key_array_and_value_array(axes)
        axes_negative = values_axes < 0
        values_axes[axes_negative] += 2
        for k in keys_axes[axes_negative]:
            axes[k] += 2

    cc_check.keys_necessary_known_and_values_necessary_known_exist_and_other_keys_and_values_do_not_exist(
        axes, keys_axes_expected, values_axes_expected, name_dictionary='axes')
    cc_check.values_are_not_repeated(axes, name_dictionary='axes')

    if axes.get('formats') is None:
        if axes.get('bars') in values_axes_expected:
            axes['formats'] = int(axes['bars'] == 0)
        else:
            raise ValueError('axes')
    elif axes.get('bars') is None:
        if axes.get('formats') in values_axes_expected:
            axes['bars'] = int(axes['formats'] == 0)
        else:
            raise ValueError('axes')

    # format x and y

    if isinstance(x, np.ndarray):
        x = x
    else:
        x = np.asarray(x)

    if isinstance(y, np.ndarray):
        y = y
    else:
        y = np.asarray(y)

    shape_x = np.asarray(x.shape, dtype='i')
    n_dim_x = shape_x.size
    shape_y = np.asarray(y.shape, dtype='i')
    n_dim_y = shape_y.size

    indexes = np.empty(2, dtype='O')

    if n_dim_y == 2:
        n_formats = shape_y[axes['formats']]

        if n_dim_x == 2:
            pass
        elif n_dim_x == 1:
            x = np.expand_dims(x, axis=axes['formats'])
            shape_x = np.asarray(x.shape, dtype='i')
            n_dim_x = shape_x.size
            if not np.all(shape_x == shape_y):
                for i in range(n_dim_y):
                    indexes[i] = slice(0, shape_y[i], 1)
                x_tmp = x
                x = np.empty(shape=shape_y, dtype=x.dtype)
                x[tuple(indexes)] = x_tmp
                shape_x = np.asarray(x.shape, dtype='i')
        else:
            raise ValueError('x has to be a 1d or 2d array')

    elif n_dim_y == 1:

        if n_dim_x == 2:
            n_formats = shape_x[axes['formats']]
            y = np.expand_dims(y, axis=axes['formats'])
            shape_y = np.asarray(y.shape, dtype='i')
            n_dim_y = shape_y.size
            if not np.all(shape_x == shape_y):
                for i in range(n_dim_x):
                    indexes[i] = slice(0, shape_x[i], 1)
                y_tmp = y
                y = np.empty(shape=shape_x, dtype=y.dtype)
                y[tuple(indexes)] = y_tmp
                shape_y = np.asarray(y.shape, dtype='i')

        elif n_dim_x == 1:
            n_formats = 1
            y = np.expand_dims(y, axis=axes['formats'])
            shape_y = np.asarray(y.shape, dtype='i')
            n_dim_y = shape_y.size
            x = np.expand_dims(x, axis=axes['formats'])
            shape_x = np.asarray(x.shape, dtype='i')
            n_dim_x = shape_x.size
        else:
            raise ValueError('x has to be a 1d or 2d array')
    else:
        raise ValueError('y has to be a 1d or 2d array')

    # format error_bars_x
    if error_bars_x is None:
        symmetric_error_bars_x = True
        indexes_error_bars_x = None

    elif not np.iterable(error_bars_x):
        symmetric_error_bars_x = True
        indexes_error_bars_x = None
        error_bars_x = [error_bars_x] * shape_y[axes['bars']]

    else:

        if not isinstance(error_bars_x, np.ndarray):
            error_bars_x = np.asarray(error_bars_x)

        shape_error_bars_x_tmp = np.asarray(error_bars_x.shape, dtype='i')
        n_dim_error_bars_x = shape_error_bars_x_tmp.size
        indexes_error_bars_x = np.empty(n_dim_error_bars_x, dtype='O')

        if n_dim_error_bars_x == 2:
            symmetric_error_bars_x = True
            shape_error_bars_x = shape_y

        elif n_dim_error_bars_x == 3:
            symmetric_error_bars_x = False
            shape_error_bars_x = np.append([2], shape_y, axis=0)

        else:
            raise ValueError('error_bars_x')

        for i in range(n_dim_error_bars_x):
            indexes_error_bars_x[i] = slice(0, shape_error_bars_x[i], 1)

        if not np.all(shape_error_bars_x_tmp == shape_error_bars_x):
            error_bars_x_tmp = error_bars_x
            error_bars_x = np.empty(shape=shape_error_bars_x, dtype=error_bars_x.dtype)
            error_bars_x[tuple(indexes_error_bars_x)] = error_bars_x_tmp

    # format error_bars_y
    if error_bars_y is None:
        symmetric_error_bars_y = True
        indexes_error_bars_y = None

    elif not np.iterable(error_bars_y):
        symmetric_error_bars_y = True
        indexes_error_bars_y = None
        error_bars_y = [error_bars_y] * shape_y[axes['bars']]

    else:

        if not isinstance(error_bars_y, np.ndarray):
            error_bars_y = np.asarray(error_bars_y)

        shape_error_bars_y_tmp = np.asarray(error_bars_y.shape, dtype='i')
        n_dim_error_bars_y = shape_error_bars_y_tmp.size
        indexes_error_bars_y = np.empty(n_dim_error_bars_y, dtype='O')

        if n_dim_error_bars_y == 2:
            symmetric_error_bars_y = True
            shape_error_bars_y = shape_y

        elif n_dim_error_bars_y == 3:
            symmetric_error_bars_y = False
            shape_error_bars_y = np.append([2], shape_y, axis=0)

        else:
            raise ValueError('error_bars_y')

        for i in range(n_dim_error_bars_y):
            indexes_error_bars_y[i] = slice(0, shape_error_bars_y[i], 1)

        if not np.all(shape_error_bars_y_tmp == shape_error_bars_y):
            error_bars_y_tmp = error_bars_y
            error_bars_y = np.empty(shape=shape_error_bars_y, dtype=error_bars_y.dtype)
            error_bars_y[tuple(indexes_error_bars_y)] = error_bars_y_tmp

    # find id_figure
    if ax is None:
        figures_existing = plt.get_fignums()
        n_figures_new = 1
        i = 0
        f = 0
        while f < n_figures_new:
            if i in figures_existing:
                pass
            else:
                id_figure = i
                f += 1
            i += 1
        fig = plt.figure(
            id_figure, frameon=False, dpi=my_dpi,
            figsize=(n_pixels_x / my_dpi, n_pixels_y / my_dpi))
        ax = plt.gca()
    else:
        fig = ax.figure


    if widths is None:
        widths = np.empty(n_formats, dtype='f')
        widths[slice(0, n_formats, 1)] = (width / n_formats) - ((delta_x_formats * (n_formats - 1)) / n_formats)
    else:
        width = sum(widths) + (delta_x_formats * (n_formats - 1))

    x_formats = np.empty(n_formats, dtype='f')
    x_formats[0] = 0
    for c in range(1, n_formats, 1):
        x_formats[c] = widths[slice(0, c, 1)].sum() + (delta_x_formats * c)

    if align == 'center':
        x_formats = x_formats - x_formats.mean(axis=0)

    # if not isinstance(colors, (list, tuple, np.ndarray)):
    #     colors = [colors] * n_formats
    #
    # if not isinstance(colors_edges, (list, tuple, np.ndarray)):
    #     colors_edges = [colors_edges] * n_formats
    #
    # if not isinstance(widths_edges, (list, tuple, np.ndarray)):
    #     widths_edges = [widths_edges] * n_formats
    #
    # if not isinstance(colors_error_bars, (list, tuple, np.ndarray)):
    #     colors_error_bars = [colors_error_bars] * n_formats
    #
    # if not isinstance(sizes_caps, (list, tuple, np.ndarray)):
    #     sizes_caps = [sizes_caps] * n_formats
    #
    # if not isinstance(labels_legend, (list, tuple, np.ndarray)):
    #     labels_legend = [labels_legend] * n_formats
    #
    # if not isinstance(location_legend, (list, tuple, np.ndarray)):
    #     location_legend = [location_legend] * n_formats

    dict_parameters = dict(
        colors=colors, colors_edges=colors_edges,
        widths_edges=widths_edges, colors_error_bars=colors_error_bars, sizes_caps=sizes_caps,
        labels_legend=labels_legend, location_legend=location_legend)

    dict_parameters = cc_format.format_shape_arguments(dict_parameters, n_formats)

    colors = dict_parameters['colors']
    colors_edges = dict_parameters['colors_edges']
    widths_edges = dict_parameters['widths_edges']
    colors_error_bars = dict_parameters['colors_error_bars']
    sizes_caps = dict_parameters['sizes_caps']
    labels_legend = dict_parameters['labels_legend']

    indexes[axes['bars']] = slice(0, shape_y[axes['bars']], 1)

    for c in range(n_formats):
        indexes[axes['formats']] = c

        if indexes_error_bars_x is None:
            error_bars_x_c = error_bars_x
        else:
            if symmetric_error_bars_x:
                indexes_error_bars_x[axes['formats']] = c
            else:
                indexes_error_bars_x[axes['formats'] + 1] = c
            error_bars_x_c = error_bars_x[tuple(indexes_error_bars_x)]

        if indexes_error_bars_y is None:
            error_bars_y_c = error_bars_y
        else:
            if symmetric_error_bars_y:
                indexes_error_bars_y[axes['formats']] = c
            else:
                indexes_error_bars_y[axes['formats'] + 1] = c
            error_bars_y_c = error_bars_y[tuple(indexes_error_bars_y)]

        ax.bar(
            x[tuple(indexes)] + x_formats[c], y[tuple(indexes)],
            width=widths[c], bottom=bottom, align=align, color=colors[c],
            edgecolor=colors_edges[c], linewidth=widths_edges[c],
            xerr=error_bars_x_c, yerr=error_bars_y_c,
            ecolor=colors_error_bars[c], capsize=sizes_caps[c],
            log=log, label=labels_legend[c])

    if title is not None:
        ax.set_title(title, fontsize=fontsize_title, rotation=rotation_title)
    if label_x is not None:
        ax.set_xlabel(label_x, fontsize=fontsize_label_x, rotation=rotation_label_x)
    if label_y is not None:
        ax.set_ylabel(label_y, fontsize=fontsize_label_y, rotation=rotation_label_y)

    #plt.show()
    ticks_x_are_applied = False
    if labels_ticks_x is None:
        # max_x = data.shape[dict_axes['x']] - 1
        if ticks_x is None:
            if n_ticks_x is None:
                pass
            else:
                max_x = x.max()
                min_x = x.min()
                n_labels_ticks_x = n_ticks_x
                delta_x = (max_x - min_x) / (n_labels_ticks_x - 1)
                tick_x_lower = min_x
                tick_x_higher = max_x
                ticks_x = np.arange(tick_x_lower, tick_x_higher + delta_x, delta_x)
                ax.set_xticks(ticks_x)
                ticks_x_are_applied = True
        else:
            ax.set_xticks(ticks_x)
            ticks_x_are_applied = True

        if (stagger_labels_ticks_x or
                (fontsize_labels_ticks_x is not None) or
                (rotation_labels_ticks_x is not None)):
            fig.canvas.draw()
            tmp_labels_ticks_x = ax.get_xticklabels()[1:-1:1]
            n_labels_ticks_x = len(tmp_labels_ticks_x)
            labels_ticks_x = [None] * n_labels_ticks_x
            for l, label_l in enumerate(tmp_labels_ticks_x):
                labels_ticks_x[l] = label_l.get_text()

    if labels_ticks_x is not None:
        if not ticks_x_are_applied:
            if ticks_x is None:
                max_x = x.max()
                min_x = x.min()
                n_labels_ticks_x = len(labels_ticks_x)
                delta_x = (max_x - min_x) / (n_labels_ticks_x - 1)
                tick_x_lower = min_x
                tick_x_higher = max_x
                ticks_x = np.arange(tick_x_lower, tick_x_higher + delta_x, delta_x)

            ax.set_xticks(ticks_x)
        if stagger_labels_ticks_x:
            labels_ticks_x = (
                [str(l) if not i % 2 else '\n' + str(l) for i, l in enumerate(labels_ticks_x)])
        ax.set_xticklabels(
            labels_ticks_x, fontsize=fontsize_labels_ticks_x,
            rotation=rotation_labels_ticks_x)

    ticks_y_are_applied = False
    if labels_ticks_y is None:
        # max_y = data.shape[dict_axes['y']] - 1
        if ticks_y is None:
            if n_ticks_y is None:
                pass
            else:
                max_y = y.max()
                min_y = y.min()
                n_labels_ticks_y = n_ticks_y
                delta_y = (max_y - min_y) / (n_labels_ticks_y - 1)
                tick_y_lower = min_y
                tick_y_higher = max_y
                ticks_y = np.arange(tick_y_lower, tick_y_higher + delta_y, delta_y)
                ax.set_yticks(ticks_y)
                ticks_y_are_applied = True

        else:
            ax.set_yticks(ticks_y)
            ticks_y_are_applied = True

        if (stagger_labels_ticks_y or
                (fontsize_labels_ticks_y is not None) or
                (rotation_labels_ticks_y is not None)):
            fig.canvas.draw()
            tmp_labels_ticks_y = ax.get_yticklabels()[1:-1:1]
            n_labels_ticks_y = len(tmp_labels_ticks_y)
            labels_ticks_y = [None] * n_labels_ticks_y
            for l, label_l in enumerate(tmp_labels_ticks_y):
                labels_ticks_y[l] = label_l.get_text()

    if labels_ticks_y is not None:
        if not ticks_y_are_applied:
            if ticks_y is None:
                max_y = y.max()
                min_y = y.min()
                n_labels_ticks_y = len(labels_ticks_y)
                delta_y = (max_y - min_y) / (n_labels_ticks_y - 1)
                tick_y_lower = min_y
                tick_y_higher = max_y
                ticks_y = np.arange(tick_y_lower, tick_y_higher + delta_y, delta_y)

            ax.set_yticks(ticks_y)
        if stagger_labels_ticks_y:
            labels_ticks_y = (
                [l if not i % 2 else '\n' + l for i, l in enumerate(labels_ticks_y)])
        ax.set_yticklabels(
            labels_ticks_y, fontsize=fontsize_labels_ticks_y,
            rotation=rotation_labels_ticks_y)

    if legend:
        if isinstance(location_legend, np.ndarray):
            ax.legend(loc=location_legend.tolist())
        else:
            ax.legend(loc=location_legend)

    if tight_layout:
        plt.tight_layout()


def multi_plots_single_format_single_figure(
        x, y, axes,
        widths=0.6, bottoms=None, aligns='center', colors='b', colors_edges=None, widths_edges=None,
        error_bars_x=None, error_bars_y=None, colors_error_bars=None, sizes_caps=5, logs=False,
        titles=None, fontsizes_titles=None, rotations_titles=None,
        labels_x=None, fontsizes_labels_x=None, rotations_labels_x=None,
        labels_y=None, fontsizes_labels_y=None, rotations_labels_y=None,
        labels_ticks_x=None, ticks_x=None, n_ticks_x=None,
        stagger_labels_ticks_x=False, fontsizes_labels_ticks_x=None, rotations_labels_ticks_x=None,
        labels_ticks_y=None, ticks_y=None, n_ticks_y=None,
        stagger_labels_ticks_y=False, fontsizes_labels_ticks_y=None, rotations_labels_ticks_y=None,
        legends=False, labels_legends='', locations_legends='best',
        id_figure=None, sharex=False, sharey=False,
        hspace=None, wspace=None, add_letters_to_titles=True,
        n_pixels_x=300, n_pixels_y=300, tight_layout=True):

    """

    Parameters
    ----------
    x
    y
    axes
    widths
    bottoms
    aligns
    colors
    colors_edges
    widths_edges
    error_bars_x
    error_bars_y
    colors_error_bars
    sizes_caps
    logs
    titles
    fontsizes_titles
    rotations_titles
    labels_x
    fontsizes_labels_x
    rotations_labels_x
    labels_y
    fontsizes_labels_y
    rotations_labels_y
    labels_ticks_x
    ticks_x
    n_ticks_x
    stagger_labels_ticks_x
    fontsizes_labels_ticks_x
    rotations_labels_ticks_x
    labels_ticks_y
    ticks_y
    n_ticks_y
    stagger_labels_ticks_y
    fontsizes_labels_ticks_y
    rotations_labels_ticks_y
    legends
    labels_legends
    locations_legends
    id_figure
    sharex
    sharey
    hspace
    wspace
    add_letters_to_titles
    n_pixels_x
    n_pixels_y
    tight_layout

    Returns
    -------

    """

    figures_existing = plt.get_fignums()
    # n_figures_existing = len(figures_existing)
    if id_figure is None:
        i = 0
        while id_figure is None:
            if i in figures_existing:
                pass
            else:
                id_figure = i
            i += 1
    else:
        if id_figure in figures_existing:
            print('Warning: overwriting figure {}.'.format(id_figure))

    # format axes
    keys_axes_expected = np.asarray(['rows', 'columns', 'bars'], dtype='U')
    values_axes_expected = np.arange(3)
    if not isinstance(axes, dict):
        raise TypeError('The type of "axes" has to be dict')
    else:
        keys_axes, values_axes = cc_format.dict_to_key_array_and_value_array(axes)
        axes_negative = values_axes < 0
        values_axes[axes_negative] += 3
        for k in keys_axes[axes_negative]:
            axes[k] += 3

    cc_check.keys_necessary_known_and_values_necessary_known_exist_and_other_keys_and_values_do_not_exist(
        axes, keys_axes_expected, values_axes_expected, name_dictionary='axes')
    cc_check.values_are_not_repeated(axes, name_dictionary='axes')

    axes_subplots = np.asarray([axes['rows'], axes['columns']], dtype='i')
    n_axes_subplots = axes_subplots.size
    axes_subplots_sort = np.sort(axes_subplots)

    if isinstance(x, np.ndarray):
        x = x
    else:
        x = np.asarray(x)

    if isinstance(y, np.ndarray):
        y = y
    else:
        y = np.asarray(y)

    shape_x = np.asarray(x.shape, dtype='i')
    n_dim_x = shape_x.size
    shape_y = np.asarray(y.shape, dtype='i')
    n_dim_y = shape_y.size

    indexes = np.empty(3, dtype='O')

    if n_dim_y == 3:
        n_rows, n_columns = shape_y[axes_subplots]
        shape_subplots = shape_y[axes_subplots_sort]

        if n_dim_x == 3:
            pass
        elif n_dim_x == 1:
            x = np.expand_dims(x, axis=axes_subplots_sort.tolist())
            shape_x = np.asarray(x.shape, dtype='i')
            n_dim_x = shape_x.size
            if not np.all(shape_x == shape_y):
                for i in range(n_dim_y):
                    indexes[i] = slice(0, shape_y[i], 1)
                x_tmp = x
                x = np.empty(shape=shape_y, dtype=x.dtype)
                x[tuple(indexes)] = x_tmp
                shape_x = np.asarray(x.shape, dtype='i')
        else:
            raise ValueError('x has to be a 1d or 3d array')

    elif n_dim_y == 1:

        if n_dim_x == 3:
            n_rows, n_columns = shape_x[axes_subplots]
            shape_subplots = shape_x[axes_subplots_sort]

            y = np.expand_dims(y, axis=axes_subplots_sort.tolist())
            shape_y = np.asarray(y.shape, dtype='i')
            n_dim_y = shape_y.size
            if not np.all(shape_x == shape_y):
                for i in range(n_dim_x):
                    indexes[i] = slice(0, shape_x[i], 1)
                y_tmp = y
                y = np.empty(shape=shape_x, dtype=y.dtype)
                y[tuple(indexes)] = y_tmp
                shape_y = np.asarray(y.shape, dtype='i')

        elif n_dim_x == 1:
            n_rows = n_columns = 1
            shape_subplots = np.asarray([1, 1], dtype='i')

            y = np.expand_dims(y, axis=axes_subplots_sort.tolist())
            shape_y = np.asarray(y.shape, dtype='i')
            n_dim_y = shape_y.size
            x = np.expand_dims(x, axis=axes_subplots_sort.tolist())
            shape_x = np.asarray(x.shape, dtype='i')
            n_dim_x = shape_x.size
        else:
            raise ValueError('x has to be a 1d or 3d array')
    else:
        raise ValueError('y has to be a 1d or 3d array')

    n_subplots = n_rows * n_columns

    # format error_bars_x
    if error_bars_x is None:
        symmetric_error_bars_x = True
        indexes_error_bars_x = None

    elif not np.iterable(error_bars_x):
        symmetric_error_bars_x = True
        indexes_error_bars_x = None
        error_bars_x = [error_bars_x] * shape_y[axes['bars']]

    else:

        if not isinstance(error_bars_x, np.ndarray):
            error_bars_x = np.asarray(error_bars_x)

        shape_error_bars_x_tmp = np.asarray(error_bars_x.shape, dtype='i')
        n_dim_error_bars_x = shape_error_bars_x_tmp.size
        indexes_error_bars_x = np.empty(n_dim_error_bars_x, dtype='O')

        if n_dim_error_bars_x == 3:
            symmetric_error_bars_x = True
            shape_error_bars_x = shape_y

        elif n_dim_error_bars_x == 4:
            symmetric_error_bars_x = False
            shape_error_bars_x = np.append([2], shape_y, axis=0)

        else:
            raise ValueError('error_bars_x')

        for i in range(n_dim_error_bars_x):
            indexes_error_bars_x[i] = slice(0, shape_error_bars_x[i], 1)

        if not np.all(shape_error_bars_x_tmp == shape_error_bars_x):
            error_bars_x_tmp = error_bars_x
            error_bars_x = np.empty(shape=shape_error_bars_x, dtype=error_bars_x.dtype)
            error_bars_x[tuple(indexes_error_bars_x)] = error_bars_x_tmp

    # format error_bars_y
    if error_bars_y is None:
        symmetric_error_bars_y = True
        indexes_error_bars_y = None

    elif not np.iterable(error_bars_y):
        symmetric_error_bars_y = True
        indexes_error_bars_y = None
        error_bars_y = [error_bars_y] * shape_y[axes['bars']]

    else:

        if not isinstance(error_bars_y, np.ndarray):
            error_bars_y = np.asarray(error_bars_y)

        shape_error_bars_y_tmp = np.asarray(error_bars_y.shape, dtype='i')
        n_dim_error_bars_y = shape_error_bars_y_tmp.size
        indexes_error_bars_y = np.empty(n_dim_error_bars_y, dtype='O')

        if n_dim_error_bars_y == 3:
            symmetric_error_bars_y = True
            shape_error_bars_y = shape_y

        elif n_dim_error_bars_y == 4:
            symmetric_error_bars_y = False
            shape_error_bars_y = np.append([2], shape_y, axis=0)

        else:
            raise ValueError('error_bars_y')

        for i in range(n_dim_error_bars_y):
            indexes_error_bars_y[i] = slice(0, shape_error_bars_y[i], 1)

        if not np.all(shape_error_bars_y_tmp == shape_error_bars_y):
            error_bars_y_tmp = error_bars_y
            error_bars_y = np.empty(shape=shape_error_bars_y, dtype=error_bars_y.dtype)
            error_bars_y[tuple(indexes_error_bars_y)] = error_bars_y_tmp

    a_num = 0
    if add_letters_to_titles:
        a_num = ord('a')
        addition = '*) '
        # len_addition = len(addition)
        if titles is None:
            titles = addition
        elif isinstance(titles, str):
            titles = addition + titles
        elif isinstance(titles, (np.ndarray, list, tuple)):

            if isinstance(titles, (list, tuple)):
                titles = np.asarray(titles, dtype='U')

            if titles.dtype.char != 'U':
                idx = np.empty(n_axes_subplots, dtype='i')
                idx[:] = 0
                if titles[tuple(idx)] is None:
                    titles = addition
                else:
                    titles = np.char.add(addition, titles.astype('U'))

            else:
                titles = np.char.add(addition, titles)
        else:
            titles = np.char.add(addition, np.asarray(titles, dtype='U'))

    dict_parameters = dict(
        widths=widths, bottoms=bottoms, aligns=aligns, colors=colors, colors_edges=colors_edges,
        widths_edges=widths_edges, colors_error_bars=colors_error_bars, sizes_caps=sizes_caps, logs=logs,
        titles=titles, fontsizes_titles=fontsizes_titles, rotations_titles=rotations_titles,
        labels_x=labels_x, fontsizes_labels_x=fontsizes_labels_x, rotations_labels_x=rotations_labels_x,
        labels_y=labels_y, fontsizes_labels_y=fontsizes_labels_y, rotations_labels_y=rotations_labels_y,
        labels_ticks_x=labels_ticks_x, ticks_x=ticks_x, n_ticks_x=n_ticks_x,
        stagger_labels_ticks_x=stagger_labels_ticks_x, fontsizes_labels_ticks_x=fontsizes_labels_ticks_x,
        rotations_labels_ticks_x=rotations_labels_ticks_x,
        labels_ticks_y=labels_ticks_y, ticks_y=ticks_y, n_ticks_y=n_ticks_y,
        stagger_labels_ticks_y=stagger_labels_ticks_y, fontsizes_labels_ticks_y=fontsizes_labels_ticks_y,
        rotations_labels_ticks_y=rotations_labels_ticks_y,
        legends=legends, labels_legends=labels_legends, locations_legends=locations_legends)

    dict_parameters = cc_format.format_shape_arguments(dict_parameters, shape_subplots)

    widths = dict_parameters['widths']
    bottoms = dict_parameters['bottoms']
    aligns = dict_parameters['aligns']
    colors = dict_parameters['colors']
    colors_edges = dict_parameters['colors_edges']
    widths_edges = dict_parameters['widths_edges']
    colors_error_bars = dict_parameters['colors_error_bars']
    sizes_caps = dict_parameters['sizes_caps']
    logs = dict_parameters['logs']
    titles = dict_parameters['titles']
    fontsizes_titles = dict_parameters['fontsizes_titles']
    rotations_titles = dict_parameters['rotations_titles']
    labels_x = dict_parameters['labels_x']
    fontsizes_labels_x = dict_parameters['fontsizes_labels_x']
    rotations_labels_x = dict_parameters['rotations_labels_x']
    labels_y = dict_parameters['labels_y']
    fontsizes_labels_y = dict_parameters['fontsizes_labels_y']
    rotations_labels_y = dict_parameters['rotations_labels_y']
    labels_ticks_x = dict_parameters['labels_ticks_x']
    ticks_x = dict_parameters['ticks_x']
    n_ticks_x = dict_parameters['n_ticks_x']
    stagger_labels_ticks_x = dict_parameters['stagger_labels_ticks_x']
    fontsizes_labels_ticks_x = dict_parameters['fontsizes_labels_ticks_x']
    rotations_labels_ticks_x = dict_parameters['rotations_labels_ticks_x']
    labels_ticks_y = dict_parameters['labels_ticks_y']
    ticks_y = dict_parameters['ticks_y']
    n_ticks_y = dict_parameters['n_ticks_y']
    stagger_labels_ticks_y = dict_parameters['stagger_labels_ticks_y']
    fontsizes_labels_ticks_y = dict_parameters['fontsizes_labels_ticks_y']
    rotations_labels_ticks_y = dict_parameters['rotations_labels_ticks_y']
    legends = dict_parameters['legends']
    labels_legends = dict_parameters['labels_legends']
    locations_legends = dict_parameters['locations_legends']

    fig, ax = plt.subplots(
        n_rows, n_columns, sharex=sharex, sharey=sharey, squeeze=False,
        num=id_figure, frameon=False, dpi=my_dpi,
        figsize=((n_pixels_x * n_columns) / my_dpi, (n_pixels_y * n_rows) / my_dpi))
    # ax = np.asarray(ax, dtype=object)

    indexes[axes['bars']] = slice(0, None, 1)

    indexes_parameters = np.empty(n_axes_subplots, dtype=object)
    indexes_parameters[:] = slice(None)

    if axes['rows'] < axes['columns']:
        indexes_combinations = slice(0, n_axes_subplots, 1)
    elif axes['rows'] > axes['columns']:
        indexes_combinations = slice(-1, -(n_axes_subplots + 1), -1)
    else:
        raise ValueError('axes')

    i = 0
    for comb_i in cc_combinations.n_conditions_to_combinations_on_the_fly(shape_subplots):

        ax[tuple(comb_i[indexes_combinations])].tick_params(axis='both', labelbottom=True, labelleft=True)

        if indexes_error_bars_x is None:
            error_bars_x_i = error_bars_x
        else:
            if symmetric_error_bars_x:
                indexes_error_bars_x[axes_subplots_sort] = comb_i
            else:
                indexes_error_bars_x[axes_subplots_sort + 1] = comb_i
            error_bars_x_i = error_bars_x[tuple(indexes_error_bars_x)]

        if indexes_error_bars_y is None:
            error_bars_y_i = error_bars_y
        else:
            if symmetric_error_bars_y:
                indexes_error_bars_y[axes_subplots_sort] = comb_i
            else:
                indexes_error_bars_y[axes_subplots_sort + 1] = comb_i
            error_bars_y_i = error_bars_y[tuple(indexes_error_bars_y)]

        indexes_parameters[slice(0, n_axes_subplots)] = comb_i
        tuple_idx_parms = tuple(indexes_parameters)
        if add_letters_to_titles:
            titles[tuple_idx_parms] = (
                    chr(a_num + i) + titles[tuple_idx_parms][slice(1, None, 1)])

        indexes[axes_subplots_sort] = comb_i

        single_plot_single_format_single_figure(
            x[tuple(indexes)], y[tuple(indexes)],
            ax=ax[tuple(comb_i[indexes_combinations])], tight_layout=False,
            width=widths[tuple_idx_parms], bottom=bottoms[tuple_idx_parms],
            align=aligns[tuple_idx_parms], color=colors[tuple_idx_parms],
            color_edge=colors_edges[tuple_idx_parms], width_edge=widths_edges[tuple_idx_parms],
            error_bars_x=error_bars_x_i,
            error_bars_y=error_bars_y_i,
            color_error_bars=colors_error_bars[tuple_idx_parms],
            size_caps=sizes_caps[tuple_idx_parms], log=logs[tuple_idx_parms],
            title=titles[tuple_idx_parms], fontsize_title=fontsizes_titles[tuple_idx_parms],
            rotation_title=rotations_titles[tuple_idx_parms],
            label_x=labels_x[tuple_idx_parms], fontsize_label_x=fontsizes_labels_x[tuple_idx_parms],
            rotation_label_x=rotations_labels_x[tuple_idx_parms],
            label_y=labels_y[tuple_idx_parms], fontsize_label_y=fontsizes_labels_y[tuple_idx_parms],
            rotation_label_y=rotations_labels_y[tuple_idx_parms],
            labels_ticks_x=labels_ticks_x[tuple_idx_parms], ticks_x=ticks_x[tuple_idx_parms],
            n_ticks_x=n_ticks_x[tuple_idx_parms],
            stagger_labels_ticks_x=stagger_labels_ticks_x[tuple_idx_parms],
            fontsize_labels_ticks_x=fontsizes_labels_ticks_x[tuple_idx_parms],
            rotation_labels_ticks_x=rotations_labels_ticks_x[tuple_idx_parms],
            labels_ticks_y=labels_ticks_y[tuple_idx_parms], ticks_y=ticks_y[tuple_idx_parms],
            n_ticks_y=n_ticks_y[tuple_idx_parms],
            stagger_labels_ticks_y=stagger_labels_ticks_y[tuple_idx_parms],
            fontsize_labels_ticks_y=fontsizes_labels_ticks_y[tuple_idx_parms],
            rotation_labels_ticks_y=rotations_labels_ticks_y[tuple_idx_parms],
            legend=legends[tuple_idx_parms], label_legend=labels_legends[tuple_idx_parms],
            location_legend=locations_legends[tuple_idx_parms])

        i += 1
    # plt.show()
    if tight_layout:
        plt.tight_layout()
    if any([hspace is not None, wspace is not None]):
        plt.subplots_adjust(hspace=hspace, wspace=wspace)


def single_plot_single_format_multi_figures(
        x, y, axes,
        widths=0.6, bottoms=None, aligns='center', colors='b', colors_edges=None, widths_edges=None,
        error_bars_x=None, error_bars_y=None, colors_error_bars=None, sizes_caps=5, logs=False,
        titles=None, fontsizes_titles=None, rotations_titles=None,
        labels_x=None, fontsizes_labels_x=None, rotations_labels_x=None,
        labels_y=None, fontsizes_labels_y=None, rotations_labels_y=None,
        labels_ticks_x=None, ticks_x=None, n_ticks_x=None,
        stagger_labels_ticks_x=False, fontsizes_labels_ticks_x=None, rotations_labels_ticks_x=None,
        labels_ticks_y=None, ticks_y=None, n_ticks_y=None,
        stagger_labels_ticks_y=False, fontsizes_labels_ticks_y=None, rotations_labels_ticks_y=None,
        legends=False, labels_legends='', locations_legends='best',
        id_figures=None, n_pixels_x=500, n_pixels_y=500, tight_layouts=True):

    """

    Parameters
    ----------
    x
    y
    axes
    widths
    bottoms
    aligns
    colors
    colors_edges
    widths_edges
    error_bars_x
    error_bars_y
    colors_error_bars
    sizes_caps
    logs
    titles
    fontsizes_titles
    rotations_titles
    labels_x
    fontsizes_labels_x
    rotations_labels_x
    labels_y
    fontsizes_labels_y
    rotations_labels_y
    labels_ticks_x
    ticks_x
    n_ticks_x
    stagger_labels_ticks_x
    fontsizes_labels_ticks_x
    rotations_labels_ticks_x
    labels_ticks_y
    ticks_y
    n_ticks_y
    stagger_labels_ticks_y
    fontsizes_labels_ticks_y
    rotations_labels_ticks_y
    legends
    labels_legends
    locations_legends
    id_figures
    n_pixels_x
    n_pixels_y
    tight_layouts

    Returns
    -------

    """

    # format axes
    keys_axes_expected = np.asarray(['figures', 'bars'], dtype=str)
    values_axes_expected = np.arange(2)
    if not isinstance(axes, dict):
        raise TypeError('The type of "axes" has to be dict')
    else:
        keys_axes, values_axes = cc_format.dict_to_key_array_and_value_array(axes)
        axes_negative = values_axes < 0
        values_axes[axes_negative] += 2
        for k in keys_axes[axes_negative]:
            axes[k] += 2

    cc_check.keys_necessary_known_and_values_necessary_known_exist_and_other_keys_and_values_do_not_exist(
        axes, keys_axes_expected, values_axes_expected, name_dictionary='axes')
    cc_check.values_are_not_repeated(axes, name_dictionary='axes')

    if isinstance(x, np.ndarray):
        x = x
    else:
        x = np.asarray(x)

    if isinstance(y, np.ndarray):
        y = y
    else:
        y = np.asarray(y)

    shape_x = np.asarray(x.shape, dtype='i')
    n_dim_x = shape_x.size
    shape_y = np.asarray(y.shape, dtype='i')
    n_dim_y = shape_y.size

    indexes = np.empty(2, dtype='O')

    if n_dim_y == 2:
        n_figures = shape_y[axes['figures']]

        if n_dim_x == 2:
            pass
        elif n_dim_x == 1:
            x = np.expand_dims(x, axis=axes['figures'])
            shape_x = np.asarray(x.shape, dtype='i')
            n_dim_x = shape_x.size
            if not np.all(shape_x == shape_y):
                for i in range(n_dim_y):
                    indexes[i] = slice(0, shape_y[i], 1)
                x_tmp = x
                x = np.empty(shape=shape_y, dtype=x.dtype)
                x[tuple(indexes)] = x_tmp
                shape_x = np.asarray(x.shape, dtype='i')
        else:
            raise ValueError('x has to be a 1d or 2d array')

    elif n_dim_y == 1:

        if n_dim_x == 2:
            n_figures = shape_x[axes['figures']]
            y = np.expand_dims(y, axis=axes['figures'])
            shape_y = np.asarray(y.shape, dtype='i')
            n_dim_y = shape_y.size
            if not np.all(shape_x == shape_y):
                for i in range(n_dim_x):
                    indexes[i] = slice(0, shape_x[i], 1)
                y_tmp = y
                y = np.empty(shape=shape_x, dtype=y.dtype)
                y[tuple(indexes)] = y_tmp
                shape_y = np.asarray(y.shape, dtype='i')

        elif n_dim_x == 1:
            n_figures = 1
            y = np.expand_dims(y, axis=axes['figures'])
            shape_y = np.asarray(y.shape, dtype='i')
            n_dim_y = shape_y.size
            x = np.expand_dims(x, axis=axes['figures'])
            shape_x = np.asarray(x.shape, dtype='i')
            n_dim_x = shape_x.size
        else:
            raise ValueError('x has to be a 1d or 2d array')
    else:
        raise ValueError('y has to be a 1d or 2d array')

    # format error_bars_x
    if error_bars_x is None:
        symmetric_error_bars_x = True
        indexes_error_bars_x = None

    elif not np.iterable(error_bars_x):
        symmetric_error_bars_x = True
        indexes_error_bars_x = None
        error_bars_x = [error_bars_x] * shape_y[axes['bars']]

    else:

        if not isinstance(error_bars_x, np.ndarray):
            error_bars_x = np.asarray(error_bars_x)

        shape_error_bars_x_tmp = np.asarray(error_bars_x.shape, dtype='i')
        n_dim_error_bars_x = shape_error_bars_x_tmp.size
        indexes_error_bars_x = np.empty(n_dim_error_bars_x, dtype='O')

        if n_dim_error_bars_x == 2:
            symmetric_error_bars_x = True
            shape_error_bars_x = shape_y

        elif n_dim_error_bars_x == 3:
            symmetric_error_bars_x = False
            shape_error_bars_x = np.append([2], shape_y, axis=0)

        else:
            raise ValueError('error_bars_x')

        for i in range(n_dim_error_bars_x):
            indexes_error_bars_x[i] = slice(0, shape_error_bars_x[i], 1)

        if not np.all(shape_error_bars_x_tmp == shape_error_bars_x):
            error_bars_x_tmp = error_bars_x
            error_bars_x = np.empty(shape=shape_error_bars_x, dtype=error_bars_x.dtype)
            error_bars_x[tuple(indexes_error_bars_x)] = error_bars_x_tmp

    # format error_bars_y
    if error_bars_y is None:
        symmetric_error_bars_y = True
        indexes_error_bars_y = None

    elif not np.iterable(error_bars_y):
        symmetric_error_bars_y = True
        indexes_error_bars_y = None
        error_bars_y = [error_bars_y] * shape_y[axes['bars']]

    else:

        if not isinstance(error_bars_y, np.ndarray):
            error_bars_y = np.asarray(error_bars_y)

        shape_error_bars_y_tmp = np.asarray(error_bars_y.shape, dtype='i')
        n_dim_error_bars_y = shape_error_bars_y_tmp.size
        indexes_error_bars_y = np.empty(n_dim_error_bars_y, dtype='O')

        if n_dim_error_bars_y == 2:
            symmetric_error_bars_y = True
            shape_error_bars_y = shape_y

        elif n_dim_error_bars_y == 3:
            symmetric_error_bars_y = False
            shape_error_bars_y = np.append([2], shape_y, axis=0)

        else:
            raise ValueError('error_bars_y')

        for i in range(n_dim_error_bars_y):
            indexes_error_bars_y[i] = slice(0, shape_error_bars_y[i], 1)

        if not np.all(shape_error_bars_y_tmp == shape_error_bars_y):
            error_bars_y_tmp = error_bars_y
            error_bars_y = np.empty(shape=shape_error_bars_y, dtype=error_bars_y.dtype)
            error_bars_y[tuple(indexes_error_bars_y)] = error_bars_y_tmp

    figures_existing = plt.get_fignums()
    # n_figures_existing = len(figures_existing)
    if id_figures is None:
        id_figures = [None] * n_figures  # type: list
        i = 0
        f = 0
        while f < n_figures:
            if i in figures_existing:
                pass
            else:
                id_figures[f] = i
                f += 1
            i += 1
    else:
        for f in id_figures:
            if f in figures_existing:
                print('Warning: overwriting figure {}.'.format(f))

    dict_parameters = dict(
        widths=widths, bottoms=bottoms, aligns=aligns, colors=colors, colors_edges=colors_edges,
        widths_edges=widths_edges, colors_error_bars=colors_error_bars, sizes_caps=sizes_caps, logs=logs,
        titles=titles, fontsizes_titles=fontsizes_titles, rotations_titles=rotations_titles,
        labels_x=labels_x, fontsizes_labels_x=fontsizes_labels_x, rotations_labels_x=rotations_labels_x,
        labels_y=labels_y, fontsizes_labels_y=fontsizes_labels_y, rotations_labels_y=rotations_labels_y,
        labels_ticks_x=labels_ticks_x, ticks_x=ticks_x, n_ticks_x=n_ticks_x,
        stagger_labels_ticks_x=stagger_labels_ticks_x, fontsizes_labels_ticks_x=fontsizes_labels_ticks_x,
        rotations_labels_ticks_x=rotations_labels_ticks_x,
        labels_ticks_y=labels_ticks_y, ticks_y=ticks_y, n_ticks_y=n_ticks_y,
        stagger_labels_ticks_y=stagger_labels_ticks_y, fontsizes_labels_ticks_y=fontsizes_labels_ticks_y,
        rotations_labels_ticks_y=rotations_labels_ticks_y,
        legends=legends, labels_legends=labels_legends, locations_legends=locations_legends,
        n_pixels_x=n_pixels_x, n_pixels_y=n_pixels_y, tight_layouts=tight_layouts)

    dict_parameters = cc_format.format_shape_arguments(dict_parameters, n_figures)

    widths = dict_parameters['widths']
    bottoms = dict_parameters['bottoms']
    aligns = dict_parameters['aligns']
    colors = dict_parameters['colors']
    colors_edges = dict_parameters['colors_edges']
    widths_edges = dict_parameters['widths_edges']
    colors_error_bars = dict_parameters['colors_error_bars']
    sizes_caps = dict_parameters['sizes_caps']
    logs = dict_parameters['logs']
    titles = dict_parameters['titles']
    fontsizes_titles = dict_parameters['fontsizes_titles']
    rotations_titles = dict_parameters['rotations_titles']
    labels_x = dict_parameters['labels_x']
    fontsizes_labels_x = dict_parameters['fontsizes_labels_x']
    rotations_labels_x = dict_parameters['rotations_labels_x']
    labels_y = dict_parameters['labels_y']
    fontsizes_labels_y = dict_parameters['fontsizes_labels_y']
    rotations_labels_y = dict_parameters['rotations_labels_y']
    labels_ticks_x = dict_parameters['labels_ticks_x']
    ticks_x = dict_parameters['ticks_x']
    n_ticks_x = dict_parameters['n_ticks_x']
    stagger_labels_ticks_x = dict_parameters['stagger_labels_ticks_x']
    fontsizes_labels_ticks_x = dict_parameters['fontsizes_labels_ticks_x']
    rotations_labels_ticks_x = dict_parameters['rotations_labels_ticks_x']
    labels_ticks_y = dict_parameters['labels_ticks_y']
    ticks_y = dict_parameters['ticks_y']
    n_ticks_y = dict_parameters['n_ticks_y']
    stagger_labels_ticks_y = dict_parameters['stagger_labels_ticks_y']
    fontsizes_labels_ticks_y = dict_parameters['fontsizes_labels_ticks_y']
    rotations_labels_ticks_y = dict_parameters['rotations_labels_ticks_y']
    legends = dict_parameters['legends']
    labels_legends = dict_parameters['labels_legends']
    locations_legends = dict_parameters['locations_legends']
    n_pixels_x = dict_parameters['n_pixels_x']
    n_pixels_y = dict_parameters['n_pixels_y']
    tight_layouts = dict_parameters['tight_layouts']

    indexes[axes['bars']] = slice(0, shape_y[axes['bars']], 1)

    for f in range(n_figures):

        fig_f = plt.figure(
            num=id_figures[f], frameon=False, dpi=my_dpi,
            figsize=(n_pixels_x[f] / my_dpi, n_pixels_y[f] / my_dpi))

        ax_f = plt.subplot(1, 1, 1)

        # ax_f.tick_params(axis='both', labelbottom=True, labelleft=True)

        indexes[axes['figures']] = f

        if indexes_error_bars_x is None:
            error_bars_x_f = error_bars_x
        else:
            if symmetric_error_bars_x:
                indexes_error_bars_x[axes['figures']] = f
            else:
                indexes_error_bars_x[axes['figures'] + 1] = f
            error_bars_x_f = error_bars_x[tuple(indexes_error_bars_x)]

        if indexes_error_bars_y is None:
            error_bars_y_f = error_bars_y
        else:
            if symmetric_error_bars_y:
                indexes_error_bars_y[axes['figures']] = f
            else:
                indexes_error_bars_y[axes['figures'] + 1] = f
            error_bars_y_f = error_bars_y[tuple(indexes_error_bars_y)]

        single_plot_single_format_single_figure(
            x[tuple(indexes)], y[tuple(indexes)],
            ax=ax_f, width=widths[f], bottom=bottoms[f], align=aligns[f],
            color=colors[f], color_edge=colors_edges[f], width_edge=widths_edges[f],
            error_bars_x=error_bars_x_f, error_bars_y=error_bars_y_f, color_error_bars=colors_error_bars[f],
            size_caps=sizes_caps[f], log=logs[f],
            title=titles[f], fontsize_title=fontsizes_titles[f], rotation_title=rotations_titles[f],
            label_x=labels_x[f], fontsize_label_x=fontsizes_labels_x[f], rotation_label_x=rotations_labels_x[f],
            label_y=labels_y[f], fontsize_label_y=fontsizes_labels_y[f], rotation_label_y=rotations_labels_y[f],
            labels_ticks_x=labels_ticks_x[f], ticks_x=ticks_x[f], n_ticks_x=n_ticks_x[f],
            stagger_labels_ticks_x=stagger_labels_ticks_x[f], fontsize_labels_ticks_x=fontsizes_labels_ticks_x[f],
            rotation_labels_ticks_x=rotations_labels_ticks_x[f],
            labels_ticks_y=labels_ticks_y[f], ticks_y=ticks_y[f], n_ticks_y=n_ticks_y[f],
            stagger_labels_ticks_y=stagger_labels_ticks_y[f], fontsize_labels_ticks_y=fontsizes_labels_ticks_y[f],
            rotation_labels_ticks_y=rotations_labels_ticks_y[f],
            legend=legends[f], label_legend=labels_legends[f], location_legend=locations_legends[f],
            tight_layout=tight_layouts[f])

