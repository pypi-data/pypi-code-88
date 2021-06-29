#!/usr/bin/env python
# coding: utf-8

import logging
import os, re, shlex, sys
from typing import Iterator

logging.root.setLevel(logging.DEBUG)
logger = logging.getLogger("air")


def log(msg, *args, **kwargs):
    text = msg
    try:
        text = msg.format(*args, **kwargs)
    except:
        try:
            text = msg % args
        except:
            text = ", ".join([msg, *args, *kwargs.items()])
    logger.log(logging.WARN, text)


# In[1]:
def install_packages(*packages):
    extra_options = []
    if "EXTRA_PIP_OPTIONS" in os.environ:
        extra_options = shlex.split(os.environ["EXTRA_PIP_OPTIONS"])
        log("Adding extra pip options: {}", extra_options)

    log("Installing packages: {}", packages)
    import sys
    __oldexit = sys.exit
    try:
        sys.exit = lambda *args: exec(
            "raise BaseException(\x27\x27.join(map(str,args)))")
        import pip._internal.commands.install
        c = pip._internal.commands.install.InstallCommand("install", "");
        ctx: Iterator[None] = c.main_context()
        runner = ctx(lambda: c._main([
            "--progress-bar", "off", "--no-input", "--pre",
            "--no-build-isolation", "--ignore-requires-python",
            "--prefer-binary", *extra_options, *packages
        ]))
        return runner()
    finally:
        sys.exit = __oldexit


log("Importing modules")
try:
    import numpy as np  # linear algebra
    # data processing, CSV file I/O (e.g. pd.read_csv)
    import pandas as pd
    import statsmodels

except ImportError:
    install_packages("statsmodels", "numpy", "pandas")
    import numpy as np  # linear algebra
    # data processing, CSV file I/O (e.g. pd.read_csv)
    import pandas as pd
    import statsmodels

dataset_csv = "pollution_us_2000_2016.csv"
GROUP_BY = ['NO2 AQI', 'O3 AQI', 'SO2 AQI', 'CO AQI']
USE_LIMITED_DATASET = False

if USE_LIMITED_DATASET:
    log("Using limited dataset")
    dataset_csv_path = os.environ["USE_LIMITED_DATASET"]
    if os.path.exists(dataset_csv_path):
        dataset_csv = dataset_csv_path
    else:
        dataset_csv = "pollution_Washington_CO_2000_2016.csv"
    GROUP_BY = ['CO AQI']
else:
    log("Using full dataset")
    GROUP_BY = ['CO AQI']

if not os.path.exists(dataset_csv):
    raise Exception("Dataset file does not exist: %s" % dataset_csv)

from statsmodels.tsa.arima.model import ARIMA

log("Reading dataset into DataFrame from %s" % dataset_csv)
df = pd.read_csv(dataset_csv)

# compute mean AQI for each city for each date
mean_aqi = df.groupby(['City', 'Date Local'])[GROUP_BY].mean()

# reset index mean_aqi
mean_aqi = mean_aqi.reset_index()
ELEMENTS = ["NO2", "O3", "SO2", "CO"]
PERIODS = 200


class UsageException(BaseException):
    def __init__(self, *args):
        super(UsageException, self).__init__(*args)


class ForecastService(object):
    def __init__(self, pollutant):
        if pollutant not in ELEMENTS:
            raise UsageException(
                "Invalid pollutant '%s'; valid choices are: %s" % (
                    pollutant, ", ".join(ELEMENTS)
                )
            )
        self.pollutant = pollutant

    def predict(self, location="Washington"):
        """
        Select one single city for analysis and
        for developing proof of concept.
        """
        log("predict({}) called", location)
        city = location
        # select one column for analysis and
        # for developing proof of concepts
        col = "%s AQI" % self.pollutant
        log("col = {}", col)
        # create subset of dataset to include only city
        # and column selected for analysis
        log("Create new_df using mean_aqi for City={}, col={}", city, col)
        new_df = mean_aqi.loc[mean_aqi['City'] == city, ['Date Local', col]]

        columns = {
            col: "y"
        }
        log("Renaming columns in new_df to columns={}", columns)
        new_df = new_df.rename(columns=columns)

        # resample time series to Daily Frequency
        # resample ensures that all dates from begining to end of
        # the start series are present
        # use ffill  forward fill to handle missing valye
        # filling the missing value from the previous day
        log("Filling new_df={}", new_df)
        new_df = new_df.ffill()
        # visualize dataframe
        # new_df.plot(x ='ds', y='y', kind = 'line', figsize=(12,8))
        log("Creating prophet_model")

        import itertools
        observations = list(filter(None, itertools.starmap(
            lambda city, date, aqi: (date, aqi) if city == 'Washington' else None,
            zip(mean_aqi['City'], mean_aqi['Date Local'], mean_aqi['CO AQI'])
        )))

        import pandas
        new_df = pandas.DataFrame(observations, columns=['Date Local', 'CO AQI'])

        arr = new_df.values
        d = dict()
        [d.__setitem__(*a[0:2]) for a in arr]
        time_sorted = sorted(d.items())
        time_sorted_dict = dict(time_sorted)
        import numpy
        data = numpy.array([*time_sorted_dict.values()])
        import pandas;
        new_df2 = pandas.DataFrame(data, columns=["CO AQI"])

        log("Generate ARIMA using new_df2={}", new_df2)
        model = ARIMA(new_df2, order=(0, 1, 0))

        log("Fit prophet_model={} using new_df2={}", model, new_df2)
        model_fit = model.fit(new_df2)

        # the parameter 'periods' represents the number of
        # days you want to predict
        # log("Creating future df using prophet_model, periods={}", PERIODS)

        # seasonal_order = (0,0,0,PERIODS)
        # future = ARIMA(new_df2, seasonal_order=seasonal_order)

        # future = model_fit.make_future_dataframe(periods=PERIODS)
        # log("Created future={}", future)

        # range pf fitted data
        bounds = (model_fit.data.row_labels.start, model_fit.data.row_labels.stop)
        new_bounds = (model_fit.data.row_labels.start, model_fit.data.row_labels.stop + PERIODS)

        start, stop = model_fit.data.row_labels.start, model_fit.data.row_labels.stop
        start, newstop = start, stop + (stop - start)

        log("Generating prediction (as 'z') from model_fit.predict()")
        z = model_fit.predict(*new_bounds)

        log("Generating forecast")
        f = statsmodels.tsa.arima.model.ARIMA(list(z.values)[0:stop + 1], exog=list(z.keys())[0:stop + 1]).fit()
        new_exog = list(range(stop, newstop))
        predictedmean = f.get_prediction(stop, newstop, exog=new_exog).predicted_mean
        #predicted = f.predict(stop, newstop, exog=new_exog)
        #forecast = list(zip(new_exog, predicted.prediction_results))
        #log("Result: forecast={}", forecast)
        #log("Returning forecast: {}", forecast)
        return predictedmean
        #forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
        #output = prophet_model.plot(forecast)
        #return json(output)
