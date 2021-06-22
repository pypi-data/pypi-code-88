import pandas as pd
import scipy.stats as stats

import matplotlib.pyplot as plt

from bluebelt.core import graphs
import bluebelt.core.helpers

import bluebelt.styles

class RollingStd():
    
    """
    Show the rolling standard deviation of a pandas series
    series: pandas.Series
    window: int
        the window size
        default value: 7
    center: boolean
        center the labels
        default value: True
    accepts all arguments for pd.Series.Rolling
    """

    def __init__(self, series, window=7, center=True, **kwargs):
        
        self.series = series
        self.confidence = kwargs.pop('confidence', None)
        self.window = window
        self.center = center
        self.win_type = kwargs.get('win_type', None)
        self.calculate(**kwargs)

    def calculate(self, **kwargs):
        if self.confidence:
            sigma_level = stats.norm.ppf(1-(1-self.confidence)/2) * 2
        else:
            sigma_level = 1
        self.rolling = self.series.dropna().rename(f'{self.series.name} rolling std').rolling(window=self.window, center=self.center, **kwargs).std() * sigma_level
        

    def plot(self, **kwargs):
        
        title = kwargs.pop('title', f'{self.series.name} rolling standard deviation')
        style = kwargs.pop('style', bluebelt.styles.paper)
        
        path = kwargs.pop('path', None)        
        
        # prepare figure
        fig, ax = plt.subplots(**kwargs)
        
        # area plot
        ax.stackplot(self.series.index, self.series.values, **style.graphs.area.stackplot)
        ax.plot(self.series, **style.graphs.area.plot)
        
        # labels
        ax.set_title(title, **style.graphs.area.title)
        
        # set x axis locator
        bluebelt.core.helpers._axisformat(ax, self.series)
        ax.set_ylim(0,)

        if path:
            plt.savefig(path)
            plt.close()
        else:
            plt.close()
            return fig