import pandas as pd
import numpy as np
import scipy.stats as stats


import bluebelt.datetime.dt

import bluebelt.statistics.std

import bluebelt.analysis.ci
import bluebelt.statistics.hypothesis_testing
import bluebelt.analysis.patterns
import bluebelt.analysis.datetime
import bluebelt.analysis.graphs
import bluebelt.analysis.ppa

import bluebelt.core.decorators

@bluebelt.core.decorators.class_methods
@pd.api.extensions.register_series_accessor('blue')
class SeriesToolkit():
    def __init__(self, pandas_obj):
        self._obj = pandas_obj
        self.std = self.std(self._obj)
        self.patterns = self.patterns(self._obj)
        self.datetime = self.datetime(self._obj)
        self.data = self.data(self._obj)
        self.graphs = self.graphs(self._obj)
        self.statistics = self.statistics(self._obj)
        self.test = self.test(self._obj)
        self.ppa = self.ppa(self._obj)
    
    @bluebelt.core.decorators.class_methods
    class std():

        def __init__(self, pandas_obj):
            self._obj = pandas_obj
                
        # standard deviation
        def std_within(self, how=None, observations=2, **kwargs):
            """
            Calculate the standard deviation within subgroups.
                arguments
                frame: pandas.DataFrame or pandas.Series
                columns: list
                    a list of column names
                    if not provided all columns will be treated as subgroups
                    if frame is a Pandas Series only the first column will be used
                    default value: None
                how: str
                    the method of estimating std_within
                    options when subgroup size == 1 (default when frame is a Pandas Series):
                    - 'amr' or 'average_moving_range'
                        optional argument: observations=2
                    - 'mmr' or 'median_moving_range'
                        optional argument: observations=2
                    - 'mssd' or 'sqrt_of_mssd'
                    default value: 'amr'

                    options when subgroup size > 1:
                    - 'pooled_std'
                    - 'r_bar'
                    - 's_bar'
                    default value: 'pooled_std'

                observations: int
                    used for average moving range and median moving range estimation
                    default value: 2
            """
            return bluebelt.statistics.std.StdWithin(self._obj, how=how, observations=observations, **kwargs)        

    @bluebelt.core.decorators.class_methods
    class patterns():

        def __init__(self, pandas_obj):
            self._obj = pandas_obj
                
        # patterns
        def polynomial(self, **kwargs):
            """
            Find the polynomial of a series and project a bandwidth
                arguments
                series: pandas.Series
                shape: int or tuple
                    when an int is provided the polynomial is provided as n-th degree polynomial
                    when a tuple is provided the function will find an optimised polynomial between first and second value of the tuple
                    default value: (0, 6)
                validation: string
                    validation type for shape tuple
                    p_val: test for normal distribution of the residuals
                    rsq: check for improvement of the rsq value
                    default value: p_val
                threshold: float
                    the threshold for normal distribution test or rsq improvement
                    default value: 0.05
                confidence: float
                    the bound confidence
                    default value: 0.8
                outlier_sigma: float
                    outliers are datapoints outside the outlier_sigma fraction
                    default value: 2
                adjust: boolean
                    adjust polynomial for outliers
                    default value: True
            """
            return bluebelt.analysis.patterns.Polynomial(self._obj, **kwargs)

        def periodical(self, **kwargs):
            """
            Find the periodical pattern of a series and project a bandwidth
                series: pandas.Series
                rule: period representation used for resampling the series
                    default value: "1W"
                how: define how the period must be evaluated
                    options are "mean", "min", "max" and "std"
                    default value: "mean"
                resolution: define the resolution of the pattern
                    the pattern is rounded to fit the resolution
                    default value: None
                confidence: float
                    the bandwidth confidence
                    default value: 0.8
                outlier_sigma: float
                    outliers are datapoints outside the outlier_sigma fraction
                    default value: 2    
            """
            return bluebelt.analysis.patterns.Periodical(self._obj, **kwargs)
    
    @bluebelt.core.decorators.class_methods
    class datetime():
        def __init__(self, pandas_obj):
            self._obj = pandas_obj

        # week day
        def week_day(self, **kwargs):
            """
            Compare the distribution of data between week days
                arguments
                series: pandas.Series
                    the Series must have a pandas.DatetimeIndex
                
                properties
                .series
                    the transformed pandas.Series with week day index
                .data
                    the data
                .equal_means
                    the result of bluebelt.statistics.hypothesis_testing.EqualMeans().passed
                .equal_variance
                    the result of bluebelt.statistics.hypothesis_testing.EqualVariance().passed

                methods
                .plot()
                    plot the results as a boxplot
            """
            return bluebelt.analysis.datetime.WeekDay(self._obj, **kwargs)

        weekday = week_day

        # day of the month
        def month_day(self, **kwargs):
            """
            Compare the distribution of data between month days
                arguments
                series: pandas.Series
                    the Series must have a pandas.DatetimeIndex
                
                properties
                .series
                    the transformed pandas.Series with month day index
                .data
                    the data
                .equal_means
                    the result of bluebelt.statistics.hypothesis_testing.EqualMeans().passed
                .equal_variance
                    the result of bluebelt.statistics.hypothesis_testing.EqualVariance().passed

                methods
                .plot()
                    plot the results as a boxplot
            """
            return bluebelt.analysis.datetime.MonthDay(self._obj, **kwargs)

        day = month_day

        # week of the year
        def week(self, **kwargs):
            """
            Compare the distribution of data between weeks
                arguments
                series: pandas.Series
                    the Series must have a pandas.DatetimeIndex
                
                properties
                .series
                    the transformed pandas.Series with week number index
                .data
                    the data
                .equal_means
                    the result of bluebelt.statistics.hypothesis_testing.EqualMeans().passed
                .equal_variance
                    the result of bluebelt.statistics.hypothesis_testing.EqualVariance().passed

                methods
                .plot()
                    plot the results as a boxplot
            """
            return bluebelt.analysis.datetime.Week(self._obj, **kwargs)

        # month of the year
        def month(self, **kwargs):
            """
            Compare the distribution of data between months
                arguments
                series: pandas.Series
                    the Series must have a pandas.DatetimeIndex
                
                properties
                .series
                    the transformed pandas.Series with month index
                .data
                    the data
                .equal_means
                    the result of bluebelt.statistics.hypothesis_testing.EqualMeans().passed
                .equal_variance
                    the result of bluebelt.statistics.hypothesis_testing.EqualVariance().passed

                methods
                .plot()
                    plot the results as a boxplot
            """
            return bluebelt.analysis.datetime.Month(self._obj, **kwargs)

        # year
        def year(self, **kwargs):
            """
            Compare the distribution of data between years
                arguments
                series: pandas.Series
                    the Series must have a pandas.DatetimeIndex
                
                properties
                .series
                    the transformed pandas.Series with year index
                .data
                    the data
                .equal_means
                    the result of bluebelt.statistics.hypothesis_testing.EqualMeans().passed
                .equal_variance
                    the result of bluebelt.statistics.hypothesis_testing.EqualVariance().passed

                methods
                .plot()
                    plot the results as a boxplot
            """
            return bluebelt.analysis.datetime.Year(self._obj, **kwargs) 

    @bluebelt.core.decorators.class_methods
    class data():

        def __init__(self, pandas_obj):
            self._obj = pandas_obj
                
        def resample(self, **kwargs):
            """
            Resample as series and apply a specific function.
                arguments
                series: pandas.Series
                rule: str
                    the resampling rule
                any pandas.Series.resample argunment

                Apply one of the following functions:
                    .sum()
                    .mean()
                    .min()
                    .max()
                    .std()
                    .value_range()
                    .count()
                    .subsize_count()
                    .subseries_count()

                e.g. series.blue.data.resample(rule="1W").sum()
            """
            return bluebelt.data.resolution.Resample(self._obj, **kwargs)
        
        def group_index(self, **kwargs):
            """
            Group a series by DateTime index and apply a specific function.
                arguments
                series: pandas.Series
                index: str
                    a string with date-time keywords that can be parsed to group the index
                    keywords:
                        weekday_name -> %a  # abbreviated weekday name
                        week_day -> %u      # weekday as a number (1 to 7), Monday=1. Warning: In Sun Solaris Sunday=1
                        weekday -> %u       # weekday as a number (1 to 7), Monday=1. Warning: In Sun Solaris Sunday=1
                        iso_week -> %V      # The ISO 8601 week number of the current year (01 to 53), where week 1 is the first week that has at least 4 days in the current year, and with Monday as the first day of the week
                        isoweek -> %V       # The ISO 8601 week number of the current year (01 to 53), where week 1 is the first week that has at least 4 days in the current year, and with Monday as the first day of the week
                        monthname -> %b     # abbreviated month name
                        month_name -> %b    # abbreviated month name
                        monthday -> %d      # day of the month (01 to 31)
                        month_day -> %d     # day of the month (01 to 31)
                        isoyear -> %G       # 4-digit year corresponding to the ISO week number (see %V).
                        iso_year -> %G      # 4-digit year corresponding to the ISO week number (see %V).
                        yearday -> %j       # day of the year (001 to 366)
                        year_day -> %j      # day of the year (001 to 366)
                        year -> %Y          # year including the century
                        month -> %m         # month (01 to 12)
                        week -> %W          # week number of the current year, starting with the first Monday as the first day of the first week
                        day -> %d           # day of the month (01 to 31)
                        hour -> %H          # hour, using a 24-hour clock (00 to 23)
                        minute -> %M        # minute
                        second -> %S        # second
                        time -> %T          # current time, equal to %H:%M:%S
                    
                    default value "iso_year-iso_week"

                    e.g. "iso_year-Wiso_week" will parse to "%G-W%V" which will print "2021-W01" for the first week of 2021

                Apply one of the following functions:
                    .sum()
                    .mean()
                    .min()
                    .max()
                    .std()
                    .value_range()
                    .count()
                    .subsize_count()
                    .subseries_count()

                e.g. series.blue.data.group_index(index="iso_year-iso_week").sum()
                
            """
            return bluebelt.data.resolution.GroupByDatetimeIndex(self._obj, **kwargs)
        
    @bluebelt.core.decorators.class_methods
    class graphs():
        def __init__(self, pandas_obj):
            self._obj = pandas_obj
        
        # rolling std
        def rolling_std(self, **kwargs):
            return bluebelt.analysis.graphs.RollingStd(self._obj, **kwargs)

    @bluebelt.core.decorators.class_methods
    class statistics():
        def __init__(self, pandas_obj):
            self._obj = pandas_obj
    
    @bluebelt.core.decorators.class_methods
    class test():
        def __init__(self, pandas_obj):
            self._obj = pandas_obj

        # index
        @property
        def index(self):
            return bluebelt.statistics.hypothesis_testing.index()

        # hypothesis testing
        def normal_distribution(self, alpha=0.05, **kwargs):
            return bluebelt.statistics.hypothesis_testing.NormalDistribution(self._obj, alpha=alpha)
        
        def dagostino_pearson(self, alpha=0.05, **kwargs):
            return bluebelt.statistics.hypothesis_testing.DAgostinoPearson(self._obj, alpha=alpha)
        
        def anderson_darling(self, alpha=0.05, **kwargs):
            return bluebelt.statistics.hypothesis_testing.AndersonDarling(self._obj, alpha=alpha)
                
        def one_sample_t(self, popmean=None, confidence=0.95, alpha=0.05, **kwargs):
            return bluebelt.statistics.hypothesis_testing.OneSampleT(self._obj, popmean=popmean, confidence=confidence, alpha=alpha, **kwargs)

        def wilcoxon(self, alpha=0.05, **kwargs):
            return bluebelt.statistics.hypothesis_testing.Wilcoxon(self._obj, alpha=alpha, **kwargs)
        
    @bluebelt.core.decorators.class_methods
    class ppa():
        def __init__(self, pandas_obj):
            self._obj = pandas_obj

        def summary(self, **kwargs):
            return bluebelt.analysis.ppa.Summary(self._obj, **kwargs)
        
        def control_chart(self, **kwargs):
            return bluebelt.analysis.ppa.ControlChart(self._obj, **kwargs)
            
        def run_chart(self, alpha=0.05, **kwargs):
            return bluebelt.analysis.ppa.RunChart(self._obj, alpha=alpha, **kwargs)

        def process_capability(self, **kwargs):
            '''
            Calculate and display the process capability
                
                arguments
                target: float
                    target value for the process
                    default value: None
                usl: float
                    upper specification limit (usl and ub cannot be specified both)
                    default value: None
                ub: float
                    upper bound (usl and ub cannot be specified both)
                    default value: None
                lsl: float
                    lower specification limit
                    default value: None
                lb: float
                    lower bound (lsl and lb cannot be specified both)
                    default value: None
                tolerance: float
                    sigma tolerance of the process
                    default value: 6.0

                methods
                .md()
                    show the process capability as markdown
                .df()
                    show the process capability in a pandas.DataFrame
                .plot()
                    plot the process capability
                    
                properties
                @ observed performance
                .observed_lt_lsl
                .observed_gt_usl
                .observed_performance

                @ expected performance
                .expected_lt_lsl_within
                .expected_gt_usl_within
                .expected_performance_within

                .expected_lt_lsl_overall
                .expected_gt_usl_overall
                .expected_performance_overall
                
                @ within capability
                .cp
                .cpl
                .cpu
                .cpk
                .ccpk
                
                @ overall capability
                .pp
                .ppl
                .ppu
                .ppk
                .cpm
            '''
            return bluebelt.analysis.ppa.ProcessCapability(self._obj, **kwargs)
        
        