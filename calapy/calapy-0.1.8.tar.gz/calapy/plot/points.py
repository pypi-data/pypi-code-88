import numpy as np
from . import plt
from .parameters import my_dpi
from ..combinations import n_conditions_to_combinations as cc_n_conditions_to_combinations
from .. import format as cc_format
from .. import check as cc_check


def single_plot_single_format_single_figure(
        x, y, marker='o', linestyle='-', color='b', linewidth=2, markersize=2, ax=None,
        n_pixels_x=300, n_pixels_y=300, legend=False, label_legend='', tight_layout=True, **kwargs):

    if ax is None:
        figures_existing = plt.get_fignums()
        n_figures_new = 1
        i = 0
        f = 0
        while f < n_figures_new:
            if i in figures_existing:
                pass
            else:
                id_figures = i
                f += 1
            i += 1
        fig = plt.figure(
            id_figures, frameon=False, dpi=my_dpi,
            figsize=(n_pixels_x / my_dpi, n_pixels_y / my_dpi))
        ax = plt.gca()
    else:
        fig = ax.figure

    ax.plot(
        x, y, marker=marker, linestyle=linestyle, color=color,
        linewidth=linewidth, markersize=markersize, label=label_legend)

    if kwargs.get('title') is not None:
        ax.set_title(
            kwargs['title'], fontsize=kwargs.get('fontsize_title'), rotation=kwargs.get('rotation_title'))
    if kwargs.get('label_x') is not None:
        ax.set_xlabel(
            kwargs['label_x'], fontsize=kwargs.get('fontsize_label_x'), rotation=kwargs.get('rotation_label_x'))
    if kwargs.get('label_y') is not None:
        ax.set_ylabel(
            kwargs['label_y'], fontsize=kwargs.get('fontsize_label_y'), rotation=kwargs.get('rotation_label_y'))

    ticks_x_are_applied = False
    if kwargs.get('labels_ticks_x') is None:
        if kwargs.get('ticks_x') is None:
            if kwargs.get('n_ticks_x') is None:
                pass
            else:
                max_x = x.max()
                min_x = x.min()
                n_labels_ticks_x = kwargs['n_ticks_x']
                delta_x = (max_x - min_x) / (n_labels_ticks_x - 1)
                tick_x_lower = min_x
                tick_x_higher = max_x
                kwargs['ticks_x'] = np.arange(tick_x_lower, tick_x_higher + delta_x, delta_x)
                ax.set_xticks(kwargs['ticks_x'])
                ticks_x_are_applied = True
        else:
            ax.set_xticks(kwargs['ticks_x'])
            ticks_x_are_applied = True

        if (kwargs.get('stagger_labels_ticks_x') or
                (kwargs.get('fontsize_labels_ticks_x') is not None) or
                (kwargs.get('rotation_labels_ticks_x') is not None)):
            fig.canvas.draw()
            tmp_labels_ticks_x = ax.get_xticklabels()[1:-1:1]
            n_labels_ticks_x = len(tmp_labels_ticks_x)
            kwargs['labels_ticks_x'] = [None] * n_labels_ticks_x
            for l, label_l in enumerate(tmp_labels_ticks_x):
                kwargs['labels_ticks_x'][l] = label_l.get_text()

    if kwargs.get('labels_ticks_x') is not None:
        if not ticks_x_are_applied:
            if kwargs.get('ticks_x') is None:
                max_x = x.max()
                min_x = x.min()
                n_labels_ticks_x = len(kwargs['labels_ticks_x'])
                delta_x = (max_x - min_x) / (n_labels_ticks_x - 1)
                tick_x_lower = min_x
                tick_x_higher = max_x
                kwargs['ticks_x'] = np.arange(tick_x_lower, tick_x_higher + delta_x, delta_x)

            ax.set_xticks(kwargs['ticks_x'])
        if kwargs.get('stagger_labels_ticks_x'):
            kwargs['labels_ticks_x'] = (
                [l if not i % 2 else '\n' + l for i, l in enumerate(kwargs['labels_ticks_x'])])
        ax.set_xticklabels(
            kwargs['labels_ticks_x'], fontsize=kwargs.get('fontsize_labels_ticks_x'),
            rotation=kwargs.get('rotation_labels_ticks_x'))

    ticks_y_are_applied = False
    if kwargs.get('labels_ticks_y') is None:
        # max_y = data.shape[dict_axes['y']] - 1
        if kwargs.get('ticks_y') is None:
            if kwargs.get('n_ticks_y') is None:
                pass
            else:
                max_y = y.max()
                min_y = y.min()
                n_labels_ticks_y = kwargs['n_ticks_y']
                delta_y = (max_y - min_y) / (n_labels_ticks_y - 1)
                tick_y_lower = min_y
                tick_y_higher = max_y
                kwargs['ticks_y'] = np.arange(tick_y_lower, tick_y_higher + delta_y, delta_y)
                ax.set_yticks(kwargs['ticks_y'])
                ticks_y_are_applied = True

        else:
            ax.set_yticks(kwargs['ticks_y'])
            ticks_y_are_applied = True

        if (kwargs.get('stagger_labels_ticks_y') or
                (kwargs.get('fontsize_labels_ticks_y') is not None) or
                (kwargs.get('rotation_labels_ticks_y') is not None)):
            fig.canvas.draw()
            tmp_labels_ticks_y = ax.get_yticklabels()[1:-1:1]
            n_labels_ticks_y = len(tmp_labels_ticks_y)
            kwargs['labels_ticks_y'] = [None] * n_labels_ticks_y
            for l, label_l in enumerate(tmp_labels_ticks_y):
                kwargs['labels_ticks_y'][l] = label_l.get_text()

    if kwargs.get('labels_ticks_y') is not None:
        if not ticks_y_are_applied:
            if kwargs.get('ticks_y') is None:
                max_y = y.max()
                min_y = y.min()
                n_labels_ticks_y = len(kwargs['labels_ticks_y'])
                delta_y = (max_y - min_y) / (n_labels_ticks_y - 1)
                tick_y_lower = min_y
                tick_y_higher = max_y
                kwargs['ticks_y'] = np.arange(tick_y_lower, tick_y_higher + delta_y, delta_y)

            ax.set_yticks(kwargs['ticks_y'])
        if kwargs.get('stagger_labels_ticks_y'):
            kwargs['labels_ticks_y'] = (
                [l if not i % 2 else '\n' + l for i, l in enumerate(kwargs['labels_ticks_y'])])
        ax.set_yticklabels(
            kwargs['labels_ticks_y'], fontsize=kwargs.get('fontsize_labels_ticks_y'),
            rotation=kwargs.get('rotation_labels_ticks_y'))

    if legend:
        ax.legend()

    if tight_layout:
        plt.tight_layout()


def multi_plots_single_format_single_figure(
        x, y, axes,
        id_figure=None, sharex=False, sharey=False,
        hspace=None, wspace=None, add_letters_to_titles=True,
        n_pixels_x_per_plot=300, n_pixels_y_per_plot=300, tight_layout=True, **kwargs):

    """

    Parameters
    ----------
    x
    y
    axes
    id_figure
    sharex
    sharey
    hspace
    wspace
    add_letters_to_titles
    n_pixels_x_per_plot
    n_pixels_y_per_plot
    tight_layout
    kwargs

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

    shape_x = np.asarray(x.shape, dtype=int)
    n_dim_x = shape_x.size
    shape_y = np.asarray(y.shape, dtype=int)
    n_dim_y = shape_y.size

    keys_axes_expected = np.asarray(['rows', 'columns', 'points'], dtype=str)

    axes_subplots = np.asarray([axes['rows'], axes['columns']], dtype=int)
    n_axes_subplots = axes_subplots.size

    if n_dim_y == 3:

        values_axes_expected = np.arange(n_dim_y)
        if not isinstance(axes, dict):
            raise TypeError('The type of "axes" has to be dict')
        else:
            keys_axes, axes_y = cc_format.dict_to_key_array_and_value_array(axes)
            axes_negative = axes_y < 0
            axes_y[axes_negative] += n_dim_y
            for k in keys_axes[axes_negative]:
                axes[k] += n_dim_y

        cc_check.keys_necessary_known_and_values_necessary_known_exist_and_other_keys_and_values_do_not_exist(
            axes, keys_axes_expected, values_axes_expected, name_dictionary='axes')
        cc_check.values_are_not_repeated(axes, name_dictionary='axes')

        n_rows, n_columns = shape_y[axes_subplots]
        axes_subplots_sort = np.sort(axes_subplots)
        shape_subplots = shape_y[axes_subplots_sort]
        n_subplots_per_fig = n_rows * n_columns
        axis_combinations = 0
        axis_variables = int(axis_combinations == 0)
        subplots_combinations = cc_n_conditions_to_combinations(
            shape_subplots, order_variables='lr', axis_combinations=axis_combinations)

        n_axes_combinations = len(subplots_combinations.shape)
        indexes_subplots_combinations = np.empty(n_axes_combinations, dtype=object)
        if axes['rows'] < axes['columns']:
            indexes_subplots_combinations[axis_variables] = slice(0, n_axes_subplots, 1)
        elif axes['rows'] > axes['columns']:
            indexes_subplots_combinations[axis_variables] = slice(n_axes_subplots, None, -1)
    elif n_dim_x == 3:

        values_axes_expected = np.arange(n_dim_x)
        if not isinstance(axes, dict):
            raise TypeError('The type of "axes" has to be dict')
        else:
            keys_axes, axes_x = cc_format.dict_to_key_array_and_value_array(axes)
            axes_negative = axes_x < 0
            axes_x[axes_negative] += n_dim_x
            for k in keys_axes[axes_negative]:
                axes[k] += n_dim_x

        cc_check.keys_necessary_known_and_values_necessary_known_exist_and_other_keys_and_values_do_not_exist(
            axes, keys_axes_expected, values_axes_expected, name_dictionary='axes')
        cc_check.values_are_not_repeated(axes, name_dictionary='axes')

        n_rows, n_columns = shape_x[axes_subplots]
        axes_subplots_sort = np.sort(axes_subplots)
        shape_subplots = shape_x[axes_subplots_sort]
        n_subplots_per_fig = n_rows * n_columns
        axis_combinations = 0
        axis_variables = int(axis_combinations == 0)
        subplots_combinations = cc_n_conditions_to_combinations(
            shape_subplots, order_variables='lr', axis_combinations=axis_combinations)

        n_axes_combinations = len(subplots_combinations.shape)
        indexes_subplots_combinations = np.empty(n_axes_combinations, dtype=object)
        if axes['rows'] < axes['columns']:
            indexes_subplots_combinations[axis_variables] = slice(0, n_axes_subplots, 1)
        elif axes['rows'] > axes['columns']:
            indexes_subplots_combinations[axis_variables] = slice(n_axes_subplots, None, -1)
    elif (n_dim_x == 1) and (n_dim_y == 1):
        n_rows = n_columns = 1
        shape_subplots = np.asarray([1, 1], dtype=int)
    else:
        raise ValueError('n_dim_x or n_dim_y has to be 1 or 3')

    if add_letters_to_titles:
        a_num = ord('a')
        addition = '*) '
        # len_addition = len(addition)
        if kwargs.get('title') is None:
            kwargs['title'] = addition
        elif isinstance(kwargs['title'], str):
            kwargs['title'] = addition + kwargs['title']
        elif (isinstance(kwargs['title'], np.ndarray) or
              isinstance(kwargs['title'], list) or
              isinstance(kwargs['title'], tuple)):

            if (isinstance(kwargs['title'], list) or
                    isinstance(kwargs['title'], tuple)):
                kwargs['title'] = np.asarray(kwargs['title'], dtype=str)

            if kwargs['title'].dtype.char != 'U':
                idx = np.empty(n_axes_subplots, dtype=int)
                idx[:] = 0
                if kwargs['title'][tuple(idx)] is None:
                    kwargs['title'] = addition
                else:
                    kwargs['title'] = np.char.add(addition, kwargs['title'].astype(str))

            else:
                kwargs['title'] = np.char.add(addition, kwargs['title'])
            # try:
            #     kwargs['title'] = np.char.add(addition, kwargs['title'])
            # except TypeError:
            #     kwargs['title'] = addition

        else:
            kwargs['title'] = np.char.add(
                addition, np.asarray(kwargs['title'], dtype=str))

    n_kwargs = len(kwargs)
    if n_kwargs > 0:
        kwargs = cc_format.format_shape_arguments(kwargs, shape_subplots)
        index_kwargs = np.empty(n_axes_subplots, dtype=object)
        index_kwargs[:] = slice(None)

    # plt.figure(
    #     id_figure, frameon=False, dpi=my_dpi,
    #     figsize=((n_pixels_x_per_plot * n_columns) / my_dpi,
    #              (n_pixels_y_per_plot * n_rows) / my_dpi))

    fig, ax = plt.subplots(
        n_rows, n_columns, sharex=sharex, sharey=sharey, squeeze=False,
        num=id_figure, frameon=False, dpi=my_dpi,
        figsize=((n_pixels_x_per_plot * n_columns) / my_dpi, (n_pixels_y_per_plot * n_rows) / my_dpi))
    # ax = np.asarray(ax, dtype=object)

    keys = kwargs.keys()

    if n_dim_y == 3:
        indexes = np.empty(n_dim_y, dtype=object)
        indexes[axes['points']] = slice(0, None, 1)
        if n_dim_x == n_dim_y:
            for s in range(n_subplots_per_fig):
                indexes_subplots_combinations[axis_combinations] = s
                ax[tuple(subplots_combinations[tuple(indexes_subplots_combinations)])].tick_params(
                    axis='both', labelbottom=True, labelleft=True)

                if n_kwargs > 0:
                    index_kwargs[slice(0, n_axes_subplots)] = subplots_combinations[s]
                    if add_letters_to_titles:
                        kwargs['title'][tuple(index_kwargs)] = (
                                chr(a_num + s) + kwargs['title'][tuple(index_kwargs)][slice(1, None, 1)])

                indexes[axes_subplots_sort] = subplots_combinations[s]
                single_plot_single_format_single_figure(
                    x[tuple(indexes)], y[tuple(indexes)],
                    ax=ax[tuple(subplots_combinations[tuple(indexes_subplots_combinations)])],
                    tight_layout=False,
                    **dict(zip(keys, [value[tuple(index_kwargs)] for value in kwargs.values()])))

        elif n_dim_x == 1:
            for s in range(n_subplots_per_fig):
                indexes_subplots_combinations[axis_combinations] = s
                ax[tuple(subplots_combinations[tuple(indexes_subplots_combinations)])].tick_params(
                    axis='both', labelbottom=True, labelleft=True)
                if n_kwargs > 0:
                    index_kwargs[slice(0, n_axes_subplots)] = subplots_combinations[s]
                    if add_letters_to_titles:
                        kwargs['title'][tuple(index_kwargs)] = (
                                chr(a_num + s) + kwargs['title'][tuple(index_kwargs)][slice(1, None, 1)])
                indexes[axes_subplots_sort] = subplots_combinations[s]
                single_plot_single_format_single_figure(
                    x, y[tuple(indexes)],
                    ax=ax[tuple(subplots_combinations[tuple(indexes_subplots_combinations)])],
                    tight_layout=False, **dict(zip(keys, [value[tuple(index_kwargs)] for value in kwargs.values()])))
        else:
            raise ValueError('x has to be a 1d or 3d array')

    elif n_dim_y == 1:
        if n_dim_x == 3:

            indexes = np.empty(n_dim_x, dtype=object)
            indexes[axes['points']] = slice(0, None, 1)
            for s in range(n_subplots_per_fig):
                indexes_subplots_combinations[axis_combinations] = s
                ax[tuple(subplots_combinations[tuple(indexes_subplots_combinations)])].tick_params(
                    axis='both', labelbottom=True, labelleft=True)
                if n_kwargs > 0:
                    index_kwargs[slice(0, n_axes_subplots)] = subplots_combinations[s]
                    if add_letters_to_titles:
                        kwargs['title'][tuple(index_kwargs)] = (
                                chr(a_num + s) + kwargs['title'][tuple(index_kwargs)][slice(1, None, 1)])
                indexes[axes_subplots_sort] = subplots_combinations[s]
                single_plot_single_format_single_figure(
                    x[tuple(indexes)], y,
                    ax=ax[tuple(subplots_combinations[tuple(indexes_subplots_combinations)])],
                    tight_layout=False, **dict(zip(keys, [value[tuple(index_kwargs)] for value in kwargs.values()])))
        elif n_dim_x == 1:

            if add_letters_to_titles:
                kwargs['title'][0, 0] = chr(a_num) + kwargs['title'][0, 0][slice(1, None, 1)]
            single_plot_single_format_single_figure(
                x, y, ax=ax[0, 0], tight_layout=False,
                **dict(zip(keys, [value[0, 0] for value in kwargs.values()])))
        else:
            raise ValueError('x has to be a 1d or 3d array')
    else:
        raise ValueError('y has to be a 1d or 3d array')

    if tight_layout:
        plt.tight_layout()
    if any([hspace is not None, wspace is not None]):
        plt.subplots_adjust(hspace=hspace, wspace=wspace)


def single_plot_multi_formats_single_figure(
        x_raw, y_raw, axes,
        marker='o', linestyle='-', color='b', linewidth=2, markersize=2,
        ax=None, n_pixels_x=300, n_pixels_y=300, legend=False, label_legend='', tight_layout=True, **kwargs):

    if ax is None:
        figures_existing = plt.get_fignums()
        n_figures_new = 1
        i = 0
        f = 0
        while f < n_figures_new:
            if i in figures_existing:
                pass
            else:
                id_figures = i
                f += 1
            i += 1
        fig = plt.figure(
            id_figures, frameon=False, dpi=my_dpi,
            figsize=(n_pixels_x / my_dpi, n_pixels_y / my_dpi))
        ax = plt.gca()
    else:
        fig = ax.figure

    if isinstance(x_raw, (list, tuple, range)):
        x = np.asarray(x_raw)
    else:
        x = x_raw

    if isinstance(y_raw, (list, tuple, range)):
        y = np.asarray(y_raw)
    else:
        y = y_raw

    shape_x = np.asarray(x.shape, dtype=int)
    n_dim_x = shape_x.size
    shape_y = np.asarray(y.shape, dtype=int)
    n_dim_y = shape_y.size

    if n_dim_y == 2:
        ####
        if axes.get('formats') is None:
            axes['formats'] = int(axes['points'] == 0)
        elif axes.get('points') is None:
            axes['points'] = int(axes['formats'] == 0)

        n_formats = shape_y[axes['formats']]
        if (not isinstance(marker, list) and
                not isinstance(marker, tuple) and
                not isinstance(marker, np.ndarray)):
            marker = [marker] * n_formats

        if (not isinstance(linestyle, list) and
                not isinstance(linestyle, tuple) and
                not isinstance(linestyle, np.ndarray)):
            linestyle = [linestyle] * n_formats

        if (not isinstance(color, list) and
                not isinstance(color, tuple) and
                not isinstance(color, np.ndarray)):
            color = [color] * n_formats

        if (not isinstance(linewidth, list) and
                not isinstance(linewidth, tuple) and
                not isinstance(linewidth, np.ndarray)):
            linewidth = [linewidth] * n_formats

        if (not isinstance(markersize, list) and
                not isinstance(markersize, tuple) and
                not isinstance(markersize, np.ndarray)):
            markersize = [markersize] * n_formats


        if (not isinstance(label_legend, list) and
                not isinstance(label_legend, tuple) and
                not isinstance(label_legend, np.ndarray)):
            label_legend = [label_legend] * n_formats

        indexes = np.empty(n_dim_y, dtype=object)
        indexes[axes['points']] = slice(0, None, 1)
        if n_dim_x == 2:
            for c in range(n_formats):
                indexes[axes['formats']] = c
                single_plot_single_format_single_figure(
                    x[tuple(indexes)], y[tuple(indexes)],
                    marker=marker[c], linestyle=linestyle[c], color=color[c],
                    linewidth=linewidth[c], markersize=markersize[c], legend=legend, label_legend=label_legend[c],
                    ax=ax, n_pixels_x=n_pixels_x, n_pixels_y=n_pixels_y, tight_layout=False)
        elif n_dim_x == 1:
            for c in range(n_formats):
                indexes[axes['formats']] = c
                single_plot_single_format_single_figure(
                    x, y[tuple(indexes)],
                    marker=marker[c], linestyle=linestyle[c], color=color[c],
                    linewidth=linewidth[c], markersize=markersize[c], legend=legend, label_legend=label_legend[c],
                    ax=ax, n_pixels_x=n_pixels_x, n_pixels_y=n_pixels_y, tight_layout=False)
        else:
            raise ValueError('x has to be a 1d or 2d array')

    elif n_dim_y == 1:
        if n_dim_x == 2:
            if axes.get('formats') is None:
                axes['formats'] = int(axes['points'] == 0)
            elif axes.get('points') is None:
                axes['points'] = int(axes['formats'] == 0)

            n_formats = shape_x[axes['formats']]
            if (not isinstance(marker, list) and
                    not isinstance(marker, tuple) and
                    not isinstance(marker, np.ndarray)):
                marker = [marker] * n_formats

            if (not isinstance(linestyle, list) and
                    not isinstance(linestyle, tuple) and
                    not isinstance(linestyle, np.ndarray)):
                linestyle = [linestyle] * n_formats

            if (not isinstance(color, list) and
                    not isinstance(color, tuple) and
                    not isinstance(color, np.ndarray)):
                color = [color] * n_formats

            if (not isinstance(linewidth, list) and
                    not isinstance(linewidth, tuple) and
                    not isinstance(linewidth, np.ndarray)):
                linewidth = [linewidth] * n_formats

            if (not isinstance(markersize, list) and
                    not isinstance(markersize, tuple) and
                    not isinstance(markersize, np.ndarray)):
                markersize = [markersize] * n_formats

            if (not isinstance(label_legend, list) and
                    not isinstance(label_legend, tuple) and
                    not isinstance(label_legend, np.ndarray)):
                label_legend = [label_legend] * n_formats

            indexes = np.empty(n_dim_x, dtype=object)
            indexes[axes['points']] = slice(0, None, 1)
            for c in range(n_formats):
                indexes[axes['formats']] = c
                single_plot_single_format_single_figure(
                    x[tuple(indexes)], y,
                    marker=marker[c], linestyle=linestyle[c], color=color[c],
                    linewidth=linewidth[c], markersize=markersize[c], legend=legend, label_legend=label_legend[c],
                    ax=ax, n_pixels_x=n_pixels_x, n_pixels_y=n_pixels_y, tight_layout=False)

        elif n_dim_x == 1:
            if (isinstance(marker, list) or
                    isinstance(marker, tuple) or
                    isinstance(marker, np.ndarray)):
                marker = marker[0]

            if (isinstance(linestyle, list) or
                    isinstance(linestyle, tuple) or
                    isinstance(linestyle, np.ndarray)):
                linestyle = linestyle[0]

            if (isinstance(color, list) or
                    isinstance(color, tuple) or
                    isinstance(color, np.ndarray)):
                color = color[0]

            if (isinstance(linewidth, list) or
                    isinstance(linewidth, tuple) or
                    isinstance(linewidth, np.ndarray)):
                linewidth = linewidth[0]

            if (isinstance(markersize, list) or
                    isinstance(markersize, tuple) or
                    isinstance(markersize, np.ndarray)):
                markersize = markersize[0]

            if (isinstance(label_legend, list) or
                    isinstance(label_legend, tuple) or
                    isinstance(label_legend, np.ndarray)):
                label_legend = label_legend[0]

            single_plot_single_format_single_figure(
                x, y,
                marker=marker, linestyle=linestyle, color=color,
                linewidth=linewidth, markersize=markersize,
                ax=ax, n_pixels_x=n_pixels_x, n_pixels_y=n_pixels_y,
                legend=legend, label_legend=label_legend, tight_layout=False)
        else:
            raise ValueError('x has to be a 1d or 2d array')
    else:
        raise ValueError('y has to be a 1d or 2d array')

    if kwargs.get('title') is not None:
        ax.set_title(
            kwargs['title'], fontsize=kwargs.get('fontsize_title'), rotation=kwargs.get('rotation_title'))
    if kwargs.get('label_x') is not None:
        ax.set_xlabel(
            kwargs['label_x'], fontsize=kwargs.get('fontsize_label_x'), rotation=kwargs.get('rotation_label_x'))
    if kwargs.get('label_y') is not None:
        ax.set_ylabel(
            kwargs['label_y'], fontsize=kwargs.get('fontsize_label_y'), rotation=kwargs.get('rotation_label_y'))

    ticks_x_are_applied = False
    if kwargs.get('labels_ticks_x') is None:
        # max_x = data.shape[dict_axes['x']] - 1
        if kwargs.get('ticks_x') is None:
            if kwargs.get('n_ticks_x') is None:
                pass
            else:
                max_x = x.max()
                min_x = x.min()
                n_labels_ticks_x = kwargs['n_ticks_x']
                delta_x = (max_x - min_x) / (n_labels_ticks_x - 1)
                tick_x_lower = min_x
                tick_x_higher = max_x
                kwargs['ticks_x'] = np.arange(tick_x_lower, tick_x_higher + delta_x, delta_x)
                ax.set_xticks(kwargs['ticks_x'])
                ticks_x_are_applied = True
        else:
            ax.set_xticks(kwargs['ticks_x'])
            ticks_x_are_applied = True

        if (kwargs.get('stagger_labels_ticks_x') or
                (kwargs.get('fontsize_labels_ticks_x') is not None) or
                (kwargs.get('rotation_labels_ticks_x') is not None)):
            fig.canvas.draw()
            tmp_labels_ticks_x = ax.get_xticklabels()[1:-1:1]
            n_labels_ticks_x = len(tmp_labels_ticks_x)
            kwargs['labels_ticks_x'] = [None] * n_labels_ticks_x
            for l, label_l in enumerate(tmp_labels_ticks_x):
                kwargs['labels_ticks_x'][l] = label_l.get_text()

    if kwargs.get('labels_ticks_x') is not None:
        if not ticks_x_are_applied:
            if kwargs.get('ticks_x') is None:
                max_x = x.max()
                min_x = x.min()
                n_labels_ticks_x = len(kwargs['labels_ticks_x'])
                delta_x = (max_x - min_x) / (n_labels_ticks_x - 1)
                tick_x_lower = min_x
                tick_x_higher = max_x
                kwargs['ticks_x'] = np.arange(tick_x_lower, tick_x_higher + delta_x, delta_x)

            ax.set_xticks(kwargs['ticks_x'])
        if kwargs.get('stagger_labels_ticks_x'):
            kwargs['labels_ticks_x'] = (
                [str(l) if not i % 2 else '\n' + str(l) for i, l in enumerate(kwargs['labels_ticks_x'])])
        ax.set_xticklabels(
            kwargs['labels_ticks_x'], fontsize=kwargs.get('fontsize_labels_ticks_x'),
            rotation=kwargs.get('rotation_labels_ticks_x'))

    ticks_y_are_applied = False
    if kwargs.get('labels_ticks_y') is None:
        # max_y = data.shape[dict_axes['y']] - 1
        if kwargs.get('ticks_y') is None:
            if kwargs.get('n_ticks_y') is None:
                pass
            else:
                max_y = y.max()
                min_y = y.min()
                n_labels_ticks_y = kwargs['n_ticks_y']
                delta_y = (max_y - min_y) / (n_labels_ticks_y - 1)
                tick_y_lower = min_y
                tick_y_higher = max_y
                kwargs['ticks_y'] = np.arange(tick_y_lower, tick_y_higher + delta_y, delta_y)
                ax.set_yticks(kwargs['ticks_y'])
                ticks_y_are_applied = True

        else:
            ax.set_yticks(kwargs['ticks_y'])
            ticks_y_are_applied = True

        if (kwargs.get('stagger_labels_ticks_y') or
                (kwargs.get('fontsize_labels_ticks_y') is not None) or
                (kwargs.get('rotation_labels_ticks_y') is not None)):
            fig.canvas.draw()
            tmp_labels_ticks_y = ax.get_yticklabels()[1:-1:1]
            n_labels_ticks_y = len(tmp_labels_ticks_y)
            kwargs['labels_ticks_y'] = [None] * n_labels_ticks_y
            for l, label_l in enumerate(tmp_labels_ticks_y):
                kwargs['labels_ticks_y'][l] = label_l.get_text()

    if kwargs.get('labels_ticks_y') is not None:
        if not ticks_y_are_applied:
            if kwargs.get('ticks_y') is None:
                max_y = y.max()
                min_y = y.min()
                n_labels_ticks_y = len(kwargs['labels_ticks_y'])
                delta_y = (max_y - min_y) / (n_labels_ticks_y - 1)
                tick_y_lower = min_y
                tick_y_higher = max_y
                kwargs['ticks_y'] = np.arange(tick_y_lower, tick_y_higher + delta_y, delta_y)

            ax.set_yticks(kwargs['ticks_y'])
        if kwargs.get('stagger_labels_ticks_y'):
            kwargs['labels_ticks_y'] = (
                [l if not i % 2 else '\n' + l for i, l in enumerate(kwargs['labels_ticks_y'])])
        ax.set_yticklabels(
            kwargs['labels_ticks_y'], fontsize=kwargs.get('fontsize_labels_ticks_y'),
            rotation=kwargs.get('rotation_labels_ticks_y'))

    if legend:
        ax.legend()

    if tight_layout:
        plt.tight_layout()
