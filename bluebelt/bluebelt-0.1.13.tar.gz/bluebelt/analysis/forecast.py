import pandas as pd
import numpy as np


import matplotlib.pyplot as plt
import seaborn as sns

import bluebelt.core.decorators
import bluebelt.core.helpers

import bluebelt.styles.paper

@bluebelt.core.decorators.class_methods
class MAPE():

    def __init__(self, frame, forecast=None, actuals=None, **kwargs):
        
        self.frame = frame
        self.forecast = forecast
        self.actuals = actuals
        self.calculate()

    def calculate(self):

        if isinstance(self.frame, pd.Series):
            if isinstance(self.forecast, pd.Series):
                forecast = self.forecast
                actuals = self.frame
            elif isinstance(self.actuals, pd.Series):
                forecast = self.frame
                actuals = self.actuals
            else:
                forecast = None
                actuals = None
        elif isinstance(self.frame, pd.DataFrame):
            if isinstance(self.forecast, str):
                forecast = self.frame[self.forecast]
            else:
                forecast = None

            if isinstance(self.actuals, str):
                actuals = self.frame[self.actuals]
            else:
                actuals = None

        if forecast is not None and actuals is not None:
            self.result = (np.abs((actuals - forecast)/actuals).sum()) / len(forecast)
            self.values = np.abs((actuals - forecast)/actuals)
        else:
            self.result = None
            self.values = None

    def __repr__(self):
        return (f'{self.__class__.__name__}(n={self.frame.shape[0]:1.0f}, result={self.result:1.4f})')
    
    def plot(self, **kwargs):
        return _forecast_plot(self, **kwargs)

@bluebelt.core.decorators.class_methods
class SMAPE():

    def __init__(self, frame, forecast=None, actuals=None, **kwargs):
        
        self.frame = frame
        self.forecast = forecast
        self.actuals = actuals
        self.calculate()

    def calculate(self):

        if isinstance(self.frame, pd.Series):
            if isinstance(self.forecast, pd.Series):
                forecast = self.forecast
                actuals = self.frame
            elif isinstance(self.actuals, pd.Series):
                forecast = self.frame
                actuals = self.actuals
            else:
                forecast = None
                actuals = None
        elif isinstance(self.frame, pd.DataFrame):
            if isinstance(self.forecast, str):
                forecast = self.frame[self.forecast]
            else:
                forecast = None

            if isinstance(self.actuals, str):
                actuals = self.frame[self.actuals]
            else:
                actuals = None

        if forecast is not None and actuals is not None:
            self.result = (np.abs(actuals - forecast) / ((np.abs(actuals) + np.abs(forecast)) / 2) ).sum() / len(forecast)
            self.values = np.abs(actuals - forecast) / ((np.abs(actuals) + np.abs(forecast)) / 2)
        else:
            self.result = None
            self.values = None

    def __repr__(self):
        return (f'{self.__class__.__name__}(n={self.frame.shape[0]:1.0f}, result={self.result:1.4f})')
    
    def plot(self, **kwargs):
        return _forecast_plot(self, **kwargs)

@bluebelt.core.decorators.class_methods
class MDA():

    def __init__(self, frame, forecast=None, actuals=None, **kwargs):
        
        self.frame = frame
        self.forecast = forecast
        self.actuals = actuals
        self.calculate()

    def calculate(self):

        if isinstance(self.frame, pd.Series):
            if isinstance(self.forecast, pd.Series):
                forecast = self.forecast
                actuals = self.frame
            elif isinstance(self.actuals, pd.Series):
                forecast = self.frame
                actuals = self.actuals
            else:
                forecast = None
                actuals = None
        elif isinstance(self.frame, pd.DataFrame):
            if isinstance(self.forecast, str):
                forecast = self.frame[self.forecast]
            else:
                forecast = None

            if isinstance(self.actuals, str):
                actuals = self.frame[self.actuals]
            else:
                actuals = None

        if forecast is not None and actuals is not None:
            self.result = (((forecast < forecast.shift(-1)).iloc[:-1] == (actuals < actuals.shift(-1)).iloc[:-1]) * 1).sum() / (len(forecast) - 1)
            self.values = (((forecast < forecast.shift(-1)).iloc[:-1] == (actuals < actuals.shift(-1)).iloc[:-1]) * 1)
        else:
            self.result = None
            self.values = None

    def __repr__(self):
        return (f'{self.__class__.__name__}(n={self.frame.shape[0]:1.0f}, result={self.result:1.4f})')
    
    def plot(self, **kwargs):
        return _forecast_plot(self, **kwargs)

@bluebelt.core.decorators.class_methods
class MPE():

    def __init__(self, frame, forecast=None, actuals=None, **kwargs):
        
        self.frame = frame
        self.forecast = forecast
        self.actuals = actuals
        self.calculate()

    def calculate(self):

        if isinstance(self.frame, pd.Series):
            if isinstance(self.forecast, pd.Series):
                forecast = self.forecast
                actuals = self.frame
            elif isinstance(self.actuals, pd.Series):
                forecast = self.frame
                actuals = self.actuals
            else:
                forecast = None
                actuals = None
        elif isinstance(self.frame, pd.DataFrame):
            if isinstance(self.forecast, str):
                forecast = self.frame[self.forecast]
            else:
                forecast = None

            if isinstance(self.actuals, str):
                actuals = self.frame[self.actuals]
            else:
                actuals = None

        if forecast is not None and actuals is not None:
            self.result = ((actuals - forecast)/actuals).sum() / len(forecast)
            self.values = (actuals - forecast)/actuals
        else:
            self.result = None
            self.values = None

    def __repr__(self):
        return (f'{self.__class__.__name__}(n={self.frame.shape[0]:1.0f}, result={self.result:1.4f})')
    
    def plot(self, **kwargs):
        return _forecast_plot(self, **kwargs)

def _forecast_plot(plot_obj, **kwargs):

    style = kwargs.pop('style', bluebelt.styles.paper)
    path = kwargs.pop('path', None)
    min_bins = kwargs.pop('min_bins', 10)
    max_bins = kwargs.pop('max_bins', 20)
    
    xlim = kwargs.pop('xlim', (None, None))
    ylim = kwargs.pop('ylim', (None, None))
    
    fig, axes = plt.subplots(nrows=1, ncols=1, gridspec_kw={'wspace': 0, 'hspace': 0}, **kwargs)

    # get bins
    histogram_points = [plot_obj.values.min(), plot_obj.values.max()]
    bins = bluebelt.core.helpers._bins(series=plot_obj.values, points=histogram_points, min_bins=min_bins, max_bins=max_bins)
    
    # plot
    axes.hist(plot_obj.values, bins=bins, **style.forecast.histogram)
    #axes.set_yticks([])

    # format x axis
    if any(val < 0 for val in plot_obj.values):
        axes.set_xlim(-1,1) 
    else:
        axes.set_xlim(0,1)
    axes.set_xticks(axes.get_xticks())
    axes.set_xticklabels([f'{x:1.0%}' for x in axes.get_xticks()])

    # title
    axes.set_title(f'{plot_obj.__class__.__name__}', **style.forecast.title)

    axes.set_xlim(xlim)
    axes.set_ylim(ylim)
    
    if path:
        plt.savefig(path)
        plt.close()
    else:
        plt.close()
        return fig