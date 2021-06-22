import pandas as pd
import scipy.stats as stats

import matplotlib.pyplot as plt

from bluebelt.core import graphs

import bluebelt.statistics.hypothesis_testing

import bluebelt.styles

class WeekDay():
    
    """
    Show the data distribution per weekday
    series: pandas.Series
    """

    def __init__(self, series, **kwargs):
        
        self.series = series
        self.name = series.name
        self.calculate()

    def calculate(self):
        
        self.series = pd.Series(index=[self.series.index.weekday, self.series.index.day_name()], data=self.series.values, name=self.series.name).sort_index(level=0).droplevel(0)
        self.data = [pd.Series(self.series[day]).dropna().values for day in self.series.index.unique()] # work around single values
        self.equal_means = bluebelt.statistics.hypothesis_testing.EqualMeans(pd.DataFrame(self.data).T).passed
        self.equal_variance = bluebelt.statistics.hypothesis_testing.EqualVariance(pd.DataFrame(self.data).T).passed
        
        
    def __repr__(self):
        return (f'{self.__class__.__name__}(series={self.name!r}, equal_means={self.equal_means}, equal_variance={self.equal_variance})')

    def plot(self, **kwargs):
        return _datetime_plot(self, title=f'{self.name} week day distribution', **kwargs)
        
class MonthDay():
    
    """
    Show the data distribution per day of the month
    series: pandas.Series
    """

    def __init__(self, series, **kwargs):
        
        self.series = series
        self.name = series.name
        self.calculate()

    def calculate(self):
        
        self.series = pd.Series(index=self.series.index.day, data=self.series.values, name=self.series.name).sort_index()
        self.data = [self.series[day].dropna().values for day in self.series.index.unique()]
        self.equal_means = bluebelt.statistics.hypothesis_testing.EqualMeans(pd.DataFrame(self.data).T).passed
        self.equal_variance = bluebelt.statistics.hypothesis_testing.EqualVariance(pd.DataFrame(self.data).T).passed
                
    def __repr__(self):
        return (f'{self.__class__.__name__}(series={self.name!r}, equal_means={self.equal_means}, equal_variance={self.equal_variance})')

    def plot(self, **kwargs):
        return _datetime_plot(self, title=f'{self.name} month day distribution', **kwargs) 

class Week():
    
    """
    Show the data distribution per weekday
    series: pandas.Series
    """

    def __init__(self, series, **kwargs):
        
        self.series = series
        self.name = series.name
        self.calculate()

    def calculate(self):
        
        self.series = pd.Series(index=self.series.index.isocalendar().week, data=self.series.values, name=self.series.name).sort_index()
        self.data = [self.series[week].dropna().values for week in self.series.index.unique()]
        self.equal_means = bluebelt.statistics.hypothesis_testing.EqualMeans(pd.DataFrame(self.data).T).passed
        self.equal_variance = bluebelt.statistics.hypothesis_testing.EqualVariance(pd.DataFrame(self.data).T).passed

    def __repr__(self):
        return (f'{self.__class__.__name__}(series={self.name!r}, equal_means={self.equal_means}, equal_variance={self.equal_variance})')

    def plot(self, **kwargs):
        return _datetime_plot(self, title=f'{self.name} week distribution', **kwargs)
        
class Month():
    
    """
    Show the data distribution per month
    series: pandas.Series
    """

    def __init__(self, series, **kwargs):
        
        self.series = series
        self.name = series.name
        self.calculate()

    def calculate(self):
        
        self.series = pd.Series(index=self.series.index.month, data=self.series.values, name=self.series.name).sort_index()
        self.data = [self.series[month].dropna().values for month in self.series.index.unique()]
        self.equal_means = bluebelt.statistics.hypothesis_testing.EqualMeans(pd.DataFrame(self.data).T).passed
        self.equal_variance = bluebelt.statistics.hypothesis_testing.EqualVariance(pd.DataFrame(self.data).T).passed
                
    def __repr__(self):
        return (f'{self.__class__.__name__}(series={self.name!r}, equal_means={self.equal_means}, equal_variance={self.equal_variance})')

    def plot(self, **kwargs):
        return _datetime_plot(self, title=f'{self.name} month distribution', **kwargs)
        
class Year():
    
    """
    Show the data distribution per year
    series: pandas.Series
    """

    def __init__(self, series, **kwargs):
        
        self.series = series
        self.name = series.name
        self.calculate()

    def calculate(self):
        
        self.series = pd.Series(index=self.series.index.year, data=self.series.values, name=self.series.name).sort_index()
        self.data = [self.series[year].dropna().values for year in self.series.index.unique()]
        self.equal_means = bluebelt.statistics.hypothesis_testing.EqualMeans(pd.DataFrame(self.data).T).passed
        self.equal_variance = bluebelt.statistics.hypothesis_testing.EqualVariance(pd.DataFrame(self.data).T).passed
                
    def __repr__(self):
        return (f'{self.__class__.__name__}(series={self.name!r}, equal_means={self.equal_means}, equal_variance={self.equal_variance})')

    def plot(self, **kwargs):
        return _datetime_plot(self, title=f'{self.name} year distribution')

def _datetime_plot(plot_obj, **kwargs):
        
    title = kwargs.pop('title', f'{plot_obj.name} datetime distribution')
    style = kwargs.pop('style', bluebelt.styles.paper)
    
    path = kwargs.pop('path', None)        
    
    # prepare figure
    fig, ax = plt.subplots(**kwargs)

    boxplot = ax.boxplot(plot_obj.data)

    for n, box in enumerate(boxplot['boxes']):
        # add style if any is given
        box.set(**style.graphs.boxplot.boxplot.get('boxes', {}))
        
    # title
    ax.set_title(title, **style.graphs.boxplot.title)

    # labels        
    ax.set_xticklabels(plot_obj.series.index.unique())

    plt.gcf().subplots_adjust(right=0.8)

    if path:
        plt.savefig(path)
        plt.close()
    else:
        plt.close()
        return fig