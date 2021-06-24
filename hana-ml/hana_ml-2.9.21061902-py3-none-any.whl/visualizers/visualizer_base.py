"""
This module represents a visualizer.  Matplotlib is used for all visualizations
"""
#pylint: disable=too-many-lines, line-too-long, too-many-arguments, too-many-locals, too-many-branches

import logging
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.dates import DateFormatter
import pandas as pd
logger = logging.getLogger(__name__) #pylint: disable=invalid-name

class Visualizer(object):
    """
    Base class for all visualizations.
    It stores the axes, size, title and other drawing parameters.

    Parameters
    ----------
    ax : matplotlib.Axes, optional
        The axes to use to plot the figure.
        Default value : Current axes
    size : tuple of integers, optional
        (width, height) of the plot in dpi
        Default value: Current size of the plot
    cmap : plt.cm, optional
        The color map used in the plot.
        Default value: plt.cm.Blues
    title : str, optional
        This plot's title.
        Default value : Empty str

    """

    def __init__(self, ax=None, size=None, cmap=None, title=None): #pylint: disable=invalid-name
        self.set_ax(ax)
        self.set_title(title)
        self.set_cmap(cmap)
        self.set_size(size)

    ##////////////////////////////////////////////////////////////////////
    ## Primary Visualizer Properties
    ##////////////////////////////////////////////////////////////////////
    @property
    def ax(self): #pylint: disable=invalid-name
        """
        Returns the matplotlib Axes where the Visualizer will draw.
        """
        return self._ax

    def set_ax(self, ax):
        """
        Sets the Axes
        """
        if ax is None:
            self._ax = plt.gca()
        else:
            self._ax = ax

    @property
    def size(self):
        """
        Returns the size of the plot in pixels.
        """
        return self._size

    def set_size(self, size):
        """
        Sets the size
        """
        if size is None:
            fig = plt.gcf()
        else:
            fig = plt.gcf()
            width, height = size
            fig.set_size_inches(width / fig.get_dpi(), height / fig.get_dpi())
        self._size = fig.get_size_inches()*fig.dpi

    @property
    def title(self):
        """
        Returns the title of the plot.
        """
        return self._title

    def set_title(self, title):
        """
        Sets the title of the plot
        """
        if title is not None:
            self._title = title
        else:
            self._title = ""

    @property
    def cmap(self):
        """
        Returns the color map being used for the plot.
        """
        return self._cmap

    def set_cmap(self, cmap):
        """
        Sets the colormap
        """
        if cmap is None:
            self._cmap = plt.cm.get_cmap('Blues')

def forecast_line_plot(pred_data, actual_data=None, confidence=None, ax=None, figsize=(15, 12), max_xticklabels=10):
    """
    Plot the prediction data for time series forecast or regression model.

    Parameters
    ----------
    pred_data : DataFrame
        The forecast data to be plotted.
    actual_data : DataFrame, optional
        The actual data to be plotted.
    confidence : tuple of str, optional
        The column names of confidence bound.
    ax : matplotlib.Axes, optional
        The axes to use to plot the figure.
        Default value : Current axes
    figsize : tuple, optional
        (weight, height) of the figure.

        Defaults to (15, 12).
    max_xticklabels : int, optional
        The maximum number of xtick labels.
        Defaults to 10.
    """

    if pred_data.index is None:
        raise ValueError("pred_data has no index. Please set index by set_index().")
    pred_xticks = pred_data.select(pred_data.index).collect()[pred_data.index].to_list()
    xticks = pred_xticks
    if actual_data is not None:
        if actual_data.index is not None:
            actual_xticks = actual_data.select(actual_data.index).collect()[actual_data.index]\
                .to_list()
            xticks = list(set(xticks + actual_xticks))
            xticks.sort()
    if ax is None:
        fig, ax = plt.subplots()
    fig.set_figheight(figsize[1])
    fig.set_figwidth(figsize[0])
    is_timestamp = isinstance(xticks[0], pd.Timestamp)
    if is_timestamp:
        ax.xaxis.set_major_formatter(DateFormatter("%y-%m-%d %H:%M:%S"))
        ax.xaxis_date()
    ax.set_xticks(xticks)
    my_locator = ticker.MaxNLocator(max_xticklabels)
    ax.xaxis.set_major_locator(my_locator)
    if is_timestamp:
        fig.autofmt_xdate()
    pred_columns = pred_data.columns
    pred_columns.remove(pred_data.index)
    if confidence:
        for item in confidence:
            pred_columns.remove(item)
    for col in pred_columns:
        ax.plot(pred_xticks, pred_data.select(col).collect()[col].to_list(), marker='o')
    if confidence:
        ax.fill_between(pred_xticks,
                        pred_data.select(confidence[0]).collect()[confidence[0]].to_list(),
                        pred_data.select(confidence[1]).collect()[confidence[1]].to_list(),
                        alpha=0.2)
        if len(confidence) > 3:
            ax.fill_between(pred_xticks,
                            pred_data.select(confidence[2]).collect()[confidence[2]].to_list(),
                            pred_data.select(confidence[3]).collect()[confidence[3]].to_list(),
                            alpha=0.2)
    if actual_data:
        actual_columns = actual_data.columns
        actual_columns.remove(actual_data.index)
        for col in actual_columns:
            ax.plot(actual_xticks,
                    actual_data.select(col).collect()[col].to_list(),
                    marker='o')
    legend_names = pred_columns
    if actual_data:
        legend_names = legend_names + actual_columns

    ax.legend(legend_names, loc='best', edgecolor='w')
    ax.grid()
    return ax
