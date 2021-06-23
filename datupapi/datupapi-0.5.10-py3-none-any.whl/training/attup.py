import boto3
import datetime
import itertools
import numpy as np
import openpyxl
import os
import pandas as pd
import tensorflow as tf
import tensorflow.keras.backend as K
import time

from datetime import datetime
from datetime import date, timedelta
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.utils import plot_model
from tensorflow.keras.layers import LSTM, Dense, RepeatVector, TimeDistributed, Input, BatchNormalization
from tensorflow.keras.layers import multiply, concatenate, Flatten, Activation, dot, Dropout
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.optimizers import Adam, Nadam
from tensorflow.keras.activations import softmax
from tensorflow.keras.losses import categorical_crossentropy, logcosh

from datupapi.configure.config import Config

tf.compat.v1.disable_eager_execution()

class Attup(Config):

    def __init__(self, config_file, logfile, log_path, *args, **kwargs):
        Config.__init__(self, config_file=config_file, logfile=logfile)
        self.log_path = log_path


    def transform_with_loc_to_matrix(self, df):
        """
        Returns a dataframe in matrix form in order to be trained by the attention model

        :param df: Dataframe with columns: timestamp, item_id, demand and location
        :return df_out: Output dataframe with each item as a column
        >>> df =
                Date        item_id  Demand  Location
                2021-16-05     sku1      23     1
                2021-16-05     sku2     543     2
                2021-16-05     sku3     123     3
        >>> df = transform_to_matrix(df)
        >>> df =
                      Date           sku1    sku2     sku3 ......... skuN
                idx1  2021-16-05      23      543      123 ......... 234
        """
        n_features_list = []
        frames = []
        locations = df.location.unique()
        for i in range(len(locations)):
            data_aux = df[df['location'] == locations[i]].iloc[:, :3].sort_values(by='timestamp')
            n_features_list.append(len(data_aux.item_id.unique()))
            data_aux = data_aux.pivot(index='timestamp', columns='item_id', values='demand')
            frames.append(data_aux)
        df_out = pd.concat(frames, axis=1).fillna(0).reset_index()
        df_out = df_out.rename(columns={'index': 'Date'})

        for_loc = []
        for i in range(len(locations)):
            aux_for = np.repeat(locations[i], n_features_list[i] * self.n_steps_out)
            for_loc.append(aux_for)
        for_loc = np.concatenate(for_loc)

        return df_out, for_loc


    def transform_to_matrix(self, df):
        """
        Returns a dataframe in matrix form in order to be trained by the attention model

        :param df: Dataframe with columns: timestamp, item_id and demand
        :return df_out: Output dataframe with each item as a column
        >>> df =
                Date        item_id  Demand
                2021-16-05     sku1      23
                2021-16-05     sku2     543
                2021-16-05     sku3     123
        >>> df = transform_to_matrix(df)
        >>> df =
                      Date           sku1    sku2     sku3 ......... skuN
                idx1  2021-16-05      23      543      123 ......... 234
        """
        df_out = df.sort_values(by='timestamp')
        df_out = df_out.reset_index()
        df_out = df_out.iloc[:, 1:]
        df_out = df_out.pivot(index='timestamp', columns='item_id', values='demand').reset_index()
        df_out = df_out.fillna(0)
        df_out = df_out.rename(columns={'timestamp': 'Date'})

        for_loc = []
        return df_out, for_loc


    def fill_dates(self, df, freq='W', value=None, method=None):
        """
        Returns a dataframe in matrix form with a row for each week between the start and end date
        defined in the df input dataframe. The NaN values are filled by the value.

        :param df: Dataframe in matrix form with the data as first column and each SKU as the next columns.
        :param freq: Aggregation type for time dimension. Default W.
        :param value: Value to fill incomplete records.
        :param method: Filling method for incomplete intermediate records.
        :return df: Output dataframe with each week between the start and end date as a row.
        >>> df =
                        Date           sku1    sku2 ......... skuN
                idx1    2021-16-05     543      123 ......... 234
                idx2    2021-30-05     250      140 ......... 200
        >>> df =fill_dates(df)
        >>> df =
                        Date           sku1    sku2 ......... skuN
                idx1    2021-16-05     543      123 ......... 234
                idx2    2021-23-05      0        0  ......... 0
                idx3    2021-30-05     250      140 ......... 200
        """
        df = df.sort_values(by='Date', ascending=True)
        sdate = datetime.strptime(df['Date'].iloc[0], '%Y-%m-%d').date()
        # start date
        edate = datetime.strptime(df['Date'].iloc[len(df) - 1], '%Y-%m-%d').date()
        # sdate = date(2017,1,2)   # start date
        # edate = date(2021,5,12)   # end date
        dates = pd.date_range(sdate, edate, freq='d')
        if freq == 'W':
            dates = dates[::7]
        dates = dates.strftime("%Y-%m-%d")
        dates_df = df.sort_values(by='Date').Date.values

        n_dates = []
        for j in range(len(dates)):
            if np.isin(dates[j], dates_df) == False:
                n_dates.append(dates[j])

        if n_dates:
            df2 = pd.DataFrame(n_dates)
            df2.columns = ['Date']
            df = df.append(df2, ignore_index=True)
            df['Date'] = pd.to_datetime(df.Date, format='%Y-%m-%d')

            df = df.sort_values(by='Date', ascending=True)
            df = df.reset_index().iloc[:, 1:]
            df = df.fillna(value=value, method=method)
            return df
        else:
            df['Date'] = pd.to_datetime(df.Date, format='%Y-%m-%d')
            return df


    def concatenate_exodata(self, df, exo, value=None, method=None, date_col=None):
        """
        Returns a dataframe in matrix form with both the endogen data (df) and the exo data
        concatenated for each week between the start and end date defined in the df input dataframe.
        The NaN values in the exo data are filled by the next not NaN value.

        :param df: Dataframe in matrix form with the data as first columnd and each SKU of the endogen data as the next columns.
        :param exo: Dataframe in matrix form with the exogen data.
        :param value: Value used to fill the NaN values after the concatenation.
        :param method: Method used to fill the NaN values after the concatenation.
        :param date_col: Name of the column that contains the dates.

        :return df_out: Output dataframe with the endogen and exogen data concatenated with the same date column.

        """
        if date_col == "Fecha":
            exo = exo.rename(columns={'Fecha': 'Date'})
        exo = exo.drop(columns='Pais')
        exo.drop_duplicates(keep="first", inplace=True)
        exo = self.fill_dates(exo, method='ffill')
        dates_df = df.sort_values(by='Date').Date.values
        dates_exo = exo.sort_values(by='Date').Date.values
        n_dates = []
        for j in range(len(dates_exo)):
            if np.isin(dates_exo[j], dates_df) == True:
                n_dates.append(dates_exo[j])

        df_out = pd.DataFrame()
        for date in n_dates:
            df_out = df_out.append(exo[exo['Date'] == date], ignore_index=True)
        df_out['Date'] = pd.to_datetime(df_out.Date, format='%Y-%m-%d')
        df_out = df_out.sort_values(by='Date', ascending=True)
        df_out = df_out.reset_index().iloc[:, 1:]
        df_out = df_out.fillna(value=value, method=method)
        df_out = pd.concat([df.set_index('Date'), df_out.set_index('Date')], axis=1)
        df_out = df_out.fillna(value=value, method=method)
        df_out = df_out.reset_index()
        return df_out


    def get_training_data(self, df, df_exo=None, method=None, value=None, date_col="Fecha"):
        """
        Returns a dataframe in matrix form using the atributes exo and location to know if the model is going to be trained
        with exo data or if there is a location column in the data.

        :param df: Qprep dataframe with the columns Date, item_id, demand and location if it exists.
        :param df_exo: Dataframe in matrix form with the exogen data.
        :param value: Value used to fill the NaN values after the concatenation of the exodata.
        :param method: Method used to fill the NaN values after the concatenation of the exodata.
        :param date_col: Name of the column that contains the dates.

        :return df_out: Output dataframe with the endogen and exogen data concatenated with the same date column.

        """
        data_date, for_loc = self.transform_with_loc_to_matrix(
            df) if self.location == True else self.transform_to_matrix(df)
        data_date = self.fill_dates(data_date, value=0)
        # data_date = data_date if exo == True else data_date
        n_features = len(data_date.columns) - 1
        if self.exo == True:
            data_date = self.concatenate_exodata(df_exo, data_date, method=method, value=value, date_col=date_col)

        return data_date, n_features, for_loc


    def add_dates(self, data_date, data, predict, n_features, for_loc):
        """
        Add the timestamp, backtesting intervals and target to the predictions dataframe based on each rows index and Qprep.

        :param data_date (df): Original Qprep dataframe.
        :param data (df): training data without dates.
        :param predict (df): Dataframe with the neural network output.
        :param n_features (int): Number of features or items that were predicted.
        :param n_backtests (int): Number of backtests. 5 by default.
        :param n_steps_out (int): Number of weeks predicted. 4 by default

        :return predict (df): Prediction dataframe with the target values, timestamp and backtesting intervals.
        """

        # Take the start date of the data
        startdate = data_date['Date'].iloc[0]
        # startdate=datetime.datetime.strptime(startdate, '%Y-%m-%d').date()
        # Define a list with all the dates by week between the startdate and the enddate
        listaDates = list(data_date['Date'].unique())
        dates = [startdate + timedelta(weeks=i) for i in range(0, len(listaDates) + self.n_steps_out + 1)]

        size = len(data.index)
        target = {}
        # Take the target column from the data dataframe and add it to the Predict dataframe.
        for i in range(1, self.n_backtests + 1):
            target[i] = data.iloc[size - i * self.n_steps_out:size - (i - 1) * self.n_steps_out].to_numpy()
            target[i] = np.reshape(target[i], (n_features * self.n_steps_out, 1), order='F')
            predict[i].insert(3, "target_value", target[i], allow_duplicates=False)

        # Add the dates column to the forecast dataframe based on the respective time_idx of each row and drop the time_idx column.
        timestamp = []
        for i in range(len(predict[0].index)):
            timestamp.append(dates[predict[0]['time_idx'].iloc[i]])
        predict[0].insert(2, column='date', value=timestamp)
        predict[0] = predict[0].drop(columns='time_idx')

        # Reorder the forecast columns according to the order defined in datupapi.
        column_names = ["item_id", "date", "p5", "p20", "p40", "p50", "p60", "p80", "p95"]
        predict[0] = predict[0].reindex(columns=column_names)

        ##Add the dates, backtest start time and backtest end time column to each backtest dataframe based on the respective time_idx of each row
        for j in range(1, self.n_backtests + 1):
            timestamp = []
            startdate = []
            enddate = []
            for i in range(len(predict[j].index)):
                timestamp.append(dates[predict[j]['time_idx'].iloc[i]])

            for i in range(len(predict[j].index)):
                startdate.append(timestamp[0])
                enddate.append(timestamp[3])

            predict[j].insert(2, column='timestamp', value=timestamp)
            predict[j].insert(3, column='backtestwindow_start_time', value=startdate)
            predict[j].insert(4, column='backtestwindow_end_time', value=enddate)
            predict[j] = predict[j].drop(columns='time_idx')

            # Reorder the backtest columns according to the order defined in datupapi.
            column_names = ["item_id", "timestamp", "target_value", "backtestwindow_start_time",
                            "backtestwindow_end_time", "p5", "p20", "p40", "p50", "p60", "p80", "p95"]
            predict[j] = predict[j].reindex(columns=column_names)

        if self.location == True:
            for i in range(self.n_backtests + 1):
                predict[i].insert(1, "Location", for_loc, allow_duplicates=False)

        return predict


    def clean_negatives(self, df):
        """
        Replace negative values with zeros.

        :param noneg (df): Dataframe with the negative values to be replaces.
        :param n_backtests (int): Number of backtests. 5 by default.

        :return noneg (df): Dataframe without negative values.
        """
        inter = ["p95", "p5", "p60", "p40", "p80", "p20", "p50"]
        for i in range(1, self.n_backtests + 1):
            df[i]['target_value'] = df[i]['target_value'].map(lambda x: 0 if x < 0 else x)

        for i in inter:
            for j in range(self.n_backtests + 1):
                df[j][i] = df[j][i].map(lambda x: 0 if x < 0 else x)

        return df


    def split_sequences(self, sequences, n_steps_in, n_steps_out):
        """
        Split a multivariate sequence into samples to use the sequences as a supervised learning model.

        :param sequences(df): Dataframe use to train the model in matrix form.
        :param n_steps_out (int): Number of weeks  to be predicted. 4 by default.
        :param n_steps_in (int): Input window size. Number of weeks used to make the prediction.

        :return X (numpy_array): Input values for training the model.
        :return y (numpy_array): Output values for training the model.
        """
        X, y = list(), list()
        for i in range(len(sequences)):
            # find the end of this pattern
            end_ix = i + n_steps_in
            out_end_ix = end_ix + n_steps_out
            # check if we are beyond the dataset
            if out_end_ix > len(sequences):
                break
            # gather input and output parts of the pattern
            seq_x, seq_y = sequences[i:end_ix, :], sequences[end_ix:out_end_ix, :]
            X.append(seq_x)
            y.append(seq_y)
        return array(X), array(y)


    def predict_with_uncertainty(self, f, x, n_iter, n_steps_out, n_features):
        predictions = []
        for i in range(n_iter):
            predictions.append(f([x, 1]))
            # prediction = result.mean(axis=0)
        predictions = np.array(predictions).reshape(n_iter, n_steps_out * n_features).T
        # uncertainty = result.std(axis=0)
        return predictions


    def prediction(self, data_m, n_features):
        """
        Train models and make predictions for backtesting and forecasting.

        :param data_m (df): Dataframe with the forecasted values for the next n_steps_out weeks.
        :param n_features (int): Number of features or items to be predicted.
        :return predict (list(df)): Dataframe with the forecasted values of n_steps_out for each item in n_features.
        :return (list(models)): List with the (n_backtests+1) models trained for backtesting and forecasting.
        :return intervals (list(arrays)): List with arrays of the predictions using dropout in order to find the confidence intervales.
                                Each array has a size of (n_iter, n_steps_out*n_features).
        """
        models = [None] * (self.n_backtests + 1)
        intervals = {}
        predict = {}
        # Train and predict forecast and backtests models
        for i in range(self.n_backtests + 1):
            scalers = {}
            data_train = pd.DataFrame()
            data_train = data_m.copy()
            size = len(data_m.index)
            data_train = data_train.head(size - (i) * self.n_steps_out)

            # -------------------------------scaler----------------------------------
            if self.normalization:
                for j in data_train.columns:
                    scaler = MinMaxScaler(feature_range=(-1, 1))
                    s_s = scaler.fit_transform(data_train[j].values.reshape(-1, 1))
                    s_s = np.reshape(s_s, len(s_s))
                    scalers['scaler_' + str(j)] = scaler
                    data_train[j] = s_s
            # -----------------------------------------------------------

            # convert into input/output
            X, y = self.split_sequences(data_train.to_numpy(), self.n_steps_in, self.n_steps_out)
            y = y[:, :, 0:n_features]
            # Xval,yval=split_sequences(dfvaln, n_steps_in, n_steps_out)
            # the dataset knows the number of features, e.g. 2
            n_features = y.shape[2]

            # ------------------------------Define the model---------------------------------------------------
            n_hidden = self.units
            input_train = Input(shape=(X.shape[1], X.shape[2]))
            output_train = Input(shape=(y.shape[1], y.shape[2]))

            encoder_stack_h, encoder_last_h, encoder_last_c = LSTM(n_hidden, activation='elu',
                                                                   dropout=self.dropout_train,
                                                                   recurrent_dropout=self.dropout_train,
                                                                   return_state=True, return_sequences=True)(input_train)

            encoder_last_h = BatchNormalization(momentum=self.momentum)(encoder_last_h)
            encoder_last_c = BatchNormalization(momentum=self.momentum)(encoder_last_c)
            decoder_input = RepeatVector(y.shape[1])(encoder_last_h)
            decoder_stack_h = LSTM(n_hidden, activation='elu', return_state=False, return_sequences=True)(decoder_input, initial_state=[encoder_last_h, encoder_last_c])
            attention = dot([decoder_stack_h, encoder_stack_h], axes=[2, 2])
            attention = Activation('softmax')(attention)
            context = dot([attention, encoder_stack_h], axes=[2, 1])
            context = BatchNormalization(momentum=self.momentum)(context)
            decoder_combined_context = concatenate([context, decoder_stack_h])
            out = TimeDistributed(Dense(y.shape[2]))(decoder_combined_context)
            model = Model(inputs=input_train, outputs=out)
            # ---------------------------------------------------------------------------------
            model.summary()
            lr = self.lr
            adam = Adam(lr)
            # Compile model
            model.compile(optimizer=adam, loss='mse', metrics=['accuracy'])
            # fit model
            history = model.fit(X, y, epochs=self.epochs, verbose=2, batch_size=self.batch_size)
            print(history.history.keys())

            # Plot the model accuracy and loss
            plt.plot(history.history['accuracy'])
            plt.title('model accuracy')
            plt.ylabel('accuracy')
            plt.xlabel('epoch')
            plt.legend(['train'], loc='upper left')
            plt.show()

            plt.plot(history.history['loss'])
            plt.title('model loss')
            plt.ylabel('loss')
            plt.xlabel('epoch')
            plt.legend(['train'], loc='upper left')
            plt.show()

            models[i] = model
            # ------------------------------------------------------------------------------------------------------
            lista = []
            lista = list(data_train.columns)[0:n_features]
            listan = list(itertools.chain.from_iterable(itertools.repeat(x, self.n_steps_out) for x in lista))
            size = len(data_m)
            predict_input = data_train.tail(self.n_steps_in)
            predict_input = predict_input.to_numpy()[0:self.n_steps_in]

            # -------Add dropout to the model used during training to make the predictions---------------------------

            dropout = self.dropout
            n_iter = self.n_iter
            conf = model.get_config()
            # Add the specified dropout to all layers
            print(conf)

            for layer in conf['layers']:
                # Dropout layers
                if layer["class_name"] == "Dropout":
                    layer["config"]["rate"] = dropout
                # Recurrent layers with dropout
                elif "dropout" in layer["config"].keys():
                    layer["config"]["dropout"] = dropout
            print(conf)
            # Create a new model with specified dropout
            if type(model) == Sequential:
                # Sequential
                model_dropout = Sequential.from_config(conf)
            else:
                # Functional
                model_dropout = Model.from_config(conf)
            model_dropout.set_weights(model.get_weights())
            print(model_dropout)

            # Define the new model with dropout
            predict_with_dropout = K.function([model_dropout.layers[0].input, K.learning_phase()],
                                              [model_dropout.layers[-1].output])

            input_data = predict_input.copy()
            input_data = input_data[None, ...]
            num_samples = input_data.shape[0]
            # fill the intervals list with the n_iter outputs for each point.
            intervals[i] = self.predict_with_uncertainty(f=predict_with_dropout, x=input_data, n_iter=self.n_iter,
                                                         n_steps_out=self.n_steps_out, n_features=n_features)
            # -----------------------------------------------------------------------------------
            # Make predictions without dropout to compare the results
            predict_input = predict_input.reshape((1, self.n_steps_in, len(data_train.columns)))
            predict_out = model.predict(predict_input, verbose=0)

            # ---------------------Invert normalization----------------------------
            if self.normalization:
                for index, k in enumerate(data_train.iloc[:, :n_features].columns):
                    scaler = scalers['scaler_' + str(k)]
                    predict_out[:, :, index] = scaler.inverse_transform(predict_out[:, :, index])
                    intervals[i][0 * n_features + index, :] = scaler.inverse_transform(
                        intervals[i][0 * n_features + index, :].reshape(-1, 1))[:, 0]
                    intervals[i][1 * n_features + index, :] = scaler.inverse_transform(
                        intervals[i][1 * n_features + index, :].reshape(-1, 1))[:, 0]
                    intervals[i][2 * n_features + index, :] = scaler.inverse_transform(
                        intervals[i][2 * n_features + index, :].reshape(-1, 1))[:, 0]
                    intervals[i][3 * n_features + index, :] = scaler.inverse_transform(
                        intervals[i][3 * n_features + index, :].reshape(-1, 1))[:, 0]
            # ------------------------inverse transform-----------------------

            # Reshape predictions
            predict_out = np.reshape(predict_out, (n_features * self.n_steps_out, 1), order='F')
            predict[i] = pd.DataFrame(predict_out)
            idxa = np.arange(size - i * self.n_steps_out, size - (i - 1) * self.n_steps_out)
            idx = idxa
            for k in range(n_features - 1):
                idx = np.append(idx, idxa)
            predict[i].insert(0, "item_id", np.array(listan), True)
            predict[i].insert(0, "time_idx", idx.T, True)

        return predict, models, intervals


    def intervals(self, data, predict, predictions, n_features):
        """
        Define confidence intervals using the ['p50','p95','p5','p60','p40','p80','p20'] percentils with the predictions data
        found using dropout and simulation path during the prediction.

        :param data (df): Qprep data in matrix form.
        :param predict (df): Dataframe with the predicted values during prediction.
        :param predictions (df): predictions using dropout with size (n_iter, n_steps_out*n_features).
        :param n_features (int): Number of features or items to be predicted.

        :return predict (df): Dataframe with the confidence intervals for each product in each of the backtests and forecast.
        """
        interv = ['p50', 'p95', 'p5', 'p60', 'p40', 'p80', 'p20']
        columns = ["time_idx", "item_id"]
        size = len(data)
        # n_features_old=10
        for i in range(self.n_backtests + 1):
            predict[i] = predict[i].iloc[:, :2]
            p = np.zeros((self.n_steps_out * n_features, len(interv)))
            predict[i].columns = columns
            for j in range(n_features):
                for k in range(self.n_steps_out):
                    ci = 0
                    p[j * self.n_steps_out + k][0] = np.quantile(predictions[i][n_features * k + j, :], 0.5)
                    ci = 0.95
                    p[j * self.n_steps_out + k][1] = np.quantile(predictions[i][n_features * k + j, :],
                                                                 0.5 + ci / 2) * (4 * 1.96)
                    p[j * self.n_steps_out + k][2] = np.quantile(predictions[i][n_features * k + j, :],
                                                                 0.5 - ci / 2) / (4 * 1.96)
                    ci = 0.6
                    p[j * self.n_steps_out + k][3] = np.quantile(predictions[i][n_features * k + j, :],
                                                                 0.5 + ci / 2) * (3 * 0.84)
                    p[j * self.n_steps_out + k][4] = np.quantile(predictions[i][n_features * k + j, :],
                                                                 0.5 - ci / 2) / (3 * 0.84)
                    ci = 0.8
                    p[j * self.n_steps_out + k][5] = np.quantile(predictions[i][n_features * k + j, :],
                                                                 0.5 + ci / 2) * (4 * 1.28)
                    p[j * self.n_steps_out + k][6] = np.quantile(predictions[i][n_features * k + j, :],
                                                                 0.5 - ci / 2) / (4 * 1.28)
            predict[i].insert(2, "p50", p[:, 0], allow_duplicates=False)
            predict[i].insert(3, "p95", p[:, 1], allow_duplicates=False)
            predict[i].insert(4, "p5", p[:, 2], allow_duplicates=False)
            predict[i].insert(5, "p60", p[:, 3], allow_duplicates=False)
            predict[i].insert(6, "p40", p[:, 4], allow_duplicates=False)
            predict[i].insert(7, "p80", p[:, 5], allow_duplicates=False)
            predict[i].insert(8, "p20", p[:, 6], allow_duplicates=False)
        return predict

