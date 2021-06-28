import numpy as np
import pydash
import pandas as pd

class Timeseries():

    _data = None
    _num_features_dataset = 0
    _num_inference_features = 0
    _dataset_features = None 
    _time_column = None
    _inference_features = None 
    _resample = True
    _resample_time = None
    _num_previous_measures = 1 
    _num_forecasts = 1
    _timeseries = None

    def __init__(self, data=None, dataset_features:list=None, time_column:str=None, 
                inference_features:list=None, resample=True, resample_time:int=None, 
                num_previous_measures:int=1, num_forecasts:int=1):
        if data is not None: self._data = pd.DataFrame(data)
        self._dataset_features = dataset_features 
        self._time_column = time_column
        self._inference_features = inference_features 
        self._resample = resample
        self._resample_time = resample_time
        self._num_previous_measures = num_previous_measures 
        self._num_forecasts = num_forecasts

    def data_to_supervised_timeseries(self):
        timeseries = self.set_up_timeseries()
        timeseries = self.timeseries_to_supervised(self._num_previous_measures, self._num_forecasts, data=timeseries)
        timeseries = self.clear_timeseries(timeseries)
        self._timeseries = timeseries
        return timeseries

    def split_input_output(self, timeseries=None):
        if timeseries is None:
            timeseries = self._timeseries

        total_columns = timeseries.columns.tolist()
        return timeseries[total_columns[:self._num_previous_measures]], timeseries[total_columns[self._num_previous_measures:]]

    def clear_timeseries(self, data=None):
        if data is None: 
            if self._data is None:
                print("ERROR: You need to specify input data either in the class or as parameter")
                return None
            else:
                data = self._data
        # Removing unnecessary features (input features) from labels columns
        cols_to_remove = []
        for j in range(
                data.shape[1],
                self._num_previous_measures * (self._num_features_dataset + self._num_inference_features),
                -(self._num_features_dataset + self._num_inference_features)):
            for l in range(self._num_features_dataset):
                cols_to_remove.append(j - l - 1)

        # Removing unnecessary features (prediction features) from dataset (input features) columns
        for j in range(self._num_features_dataset, data.shape[1], self._num_features_dataset + self._num_inference_features):
            for l in range(j, j + self._num_inference_features):
                cols_to_remove.append(l)

        data.drop(data.columns[cols_to_remove], axis=1, inplace=True)

        return data

    def timeseries_to_supervised(self, n_in=1, n_out=1, data=None, dropnan=True):
        """
            Convert series to supervised learning (source: 
            https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/)
        """
        if data is None: 
            if self._data is None:
                print("ERROR: You need to specify input data either in the class or as parameter")
                return None
            else:
                data = self._data

        n_vars = 1 if type(data) is list else data.shape[1]
        # n_vars = 1
        df = pd.DataFrame(data)

        cols, names = list(), list()
        # input sequence (t-n, ... t-1)
        for i in range(n_in, 0, -1):
            cols.append(df.shift(i))
            names += [('var%d(t-%d)' % (j + 1, i)) for j in range(n_vars)]
        # forecast sequence (t, t+1, ... t+n)
        for i in range(0, n_out):
            cols.append(df.shift(-i))
            if i == 0:
                names += [('var%d(t)' % (j + 1)) for j in range(n_vars)]
            else:
                names += [('var%d(t+%d)' % (j + 1, i)) for j in range(n_vars)]
        # put it all together
        agg = pd.concat(cols, axis=1)
        agg.columns = names
        # drop rows with NaN values
        if dropnan:
            agg.dropna(inplace=True)
        return agg

    def set_up_timeseries(self, data=None, time_column:str=None, dataset_features:list=None, inference_features:list=None, resample=True, resample_time:int=None):
        """
            Prepares dataframe as a timeseries to be trained selecting the columns from the features 
            configuration/parameters.
            If we have time series data, features to be inferenced are considered for training.
            We use a time index.
        """
        if data is None: 
            if self._data is None:
                print("ERROR: You need to specify input data either in the class or as parameter")
                return None
            else:
                data = self._data

        data = pd.DataFrame(data)

        if time_column is None:
            if self._time_column is None:
                print("ERROR: You need to specify a column with the time either in the class or as parameter")
                return None
            else:
                time_column = self._time_column

        if data.index.name is None:
            data.set_index(time_column)

        self._num_features_dataset = 0
        self._num_inference_features = 0
        
        features = []
        features_df = data.columns.tolist()

        if dataset_features is None:
            if self._dataset_features is None:
                dataset_features = data.drop(data.columns[time_column], axis=1).columns.tolist()
            else:
                dataset_features = self._dataset_features
        
        for dataset_feature in dataset_features:
            if dataset_feature in features_df:
                features = pydash.concat(features, dataset_feature)
                self._num_features_dataset += 1
            else:
                print("Feature '" + str(dataset_feature) + "' was not found in dataset features (" + str(features_df) + "). It will be ignored.")
        
        if self._num_features_dataset == 0:
            print("You must specify at least one feature in 'dataset_features' parameter.")
            return None
        

        if inference_features is None:
            if self._inference_features is None:
                print("You must specify at least one feature in 'inference_features' parameter.")
                return None
            else:
                inference_features = self._inference_features
        
        for inference_feature in inference_features:
            if inference_feature in features_df:
                features = pydash.concat(features, inference_feature)
                self._num_inference_features += 1
            else:
                print("Feature '" + str(inference_feature) + "' was not found in the data features (" + str(features_df) + "). It will be ignored.")
        
        if self._num_inference_features == 0:
            print("You must specify at least one feature in 'inference_features' parameter.")
            return None

        features = pydash.concat(time_column, features)

        data = data[features]
        
        # In modin, next operations throw an error in index is not set
        data = data.set_index(time_column)
        
        # mean delta time between measures in seconds
        t = pd.to_datetime(data.index)
        delta_df = t.to_series().diff().dt.total_seconds()
        delta_df_max = float(delta_df.max())
        delta_df_min = float(delta_df.min())
        if resample_time is None: resample_time = float(delta_df.mean())

        if delta_df_max - delta_df_min > float(resample_time):
            delta_df = int(np.abs(delta_df.mean()))
            delta = resample_time
            if delta is not None and delta != '':
                delta = int(delta)
            else:
                delta = delta_df
            print("\tFound asynchronous data. Delta between measures: " + str(delta))
        else:
            delta = int(delta_df_min)
            print("\tSynchronous data. Delta between measures: " + str(delta))

        data[time_column] = t
        
        try:
            # Remove duplicates
            df_resample = data.drop_duplicates(subset=time_column)
            df_resample = df_resample.set_index(time_column)

            # Resample time series to computed delta time, filling missing values with previous value.
            # We generate, this way, a synchronous time series
            if resample:
                df_resample = df_resample.resample(str(delta)+'S').pad()
                df_resample.dropna(inplace=True)
            
            data = df_resample
        except Exception as e:
            print("Error while trying to resample: " + str(e))
            return data

        return data
