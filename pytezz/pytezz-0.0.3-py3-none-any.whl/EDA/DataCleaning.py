#####################################       Data Cleaning         ##############################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
import seaborn as sns


class PrepareDataset:

    def __init__(self):
        pass

    def handle_missing_data(self, df: pd.DataFrame):
        """
          This function will remove all the rows which have missing labels.
          This function will get rid of all the missing values in both categorical as well as numerical columns.
          It will replace the missing categorical values by the mod of the column.
          It will replace the missing numeric values by the mean of the column.
          It will drop any column which has more than 50% null values.
        """

        df.dropna(subset=[df.columns.to_list()[
                  len(df.columns.to_list())-1]], axis=0, inplace=True)

        features = df[df.columns.to_list()[0:len(df.columns.to_list())-1]]
        labels = df[df.columns.to_list()[len(df.columns.to_list())-1]]

        for column in features.columns.to_list():

            if (features[column].isna().sum() >= (0.5*len(features[column]))):
                features.drop(column, axis=1, inplace=True)

            elif (features[column].dtype == 'O'):
                features[column].fillna(
                    features[column].mode()[0], inplace=True)

            elif (features[column].dtype == 'float64' or features[column].dtype == 'int64'):
                features[column].fillna(features[column].mean(), inplace=True)

        df = pd.concat([features, labels], axis=1)

        return df

    def extract_features(self, features: pd.DataFrame, nfeatures: int):
        """
          This function reduces the dimensions of the dataset to the limit specified by user.
          The specified dimensions are returned as Principal components.
        """
        pca_obj = PCA(n_components=nfeatures, random_state=10)
        reduced_features = pca_obj.fit_transform(features)
        column_list = []
        for i in range(reduced_features.shape[1]):
            column_list.append('PC'+str(i+1))

        reduced_features = pd.DataFrame(reduced_features, columns=column_list)
        return reduced_features

    def scale_dataset(self, features: pd.DataFrame):
        """
          This function takes in the list of all the features of type int() and scales them using
          z-score standardization
        """

        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(features)
        scaled_data = pd.DataFrame(
            scaled_data, columns=features.columns.to_list())
        return scaled_data

    def encode_dataset(self, df: pd.DataFrame, column_list: list):
        """
          Takes in a dataframe as input along with the categorical columns to be encoded.
          Will perform label encoding on each of the categorical variables and add them as a separate column.
        """

        for column in column_list:
            df[column+'_dummy'] = LabelEncoder().fit_transform(df[column])

        return df

    def drop_columns(self, df: pd.DataFrame, col_list: list):
        """
          Takes in a list of columns as input and drops them from the dataset
        """

        return df.drop(col_list, axis=1)
