#####################################       Data Visualization         ##############################################


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
import seaborn as sns


class VisualizeData:

    def __init__(self):
        pass

    def individual_lineplots(self, df: pd.DataFrame, col_list: list):
        """
          This function takes a Dataframe and a list of tuples containing the column names whose line plots are to be printed.
        """
        count = 1
        num_cols = len(col_list)
        plt.subplots(figsize=(20, 5))
        for col_tuple in col_list:
            plt.tight_layout(pad=5.0)
            plt.subplot(1, num_cols, count)
            sns.lineplot(df[col_tuple[0]], df[col_tuple[1]])
            count += 1

        plt.show()

    def combined_lineplot(self, df: pd.DataFrame, x_col: str, y_col: str, hue: str):
        """
          This function takes a Dataframe, its x-axis and y-axis column and a hue.
        """
        sns.lineplot(x=df[x_col], y=df[y_col], hue=df[hue])

    def individual_areaplots(self, df: pd.DataFrame, col_list: list):
        """
          This function takes a Dataframe and a list of tuples containing the column names whose area are to be printed.
        """
        num_cols = len(col_list)
        fig, axes = plt.subplots(nrows=1, ncols=num_cols, figsize=(20, 5))

        count = 0
        for col_tuple in col_list:
            plt.tight_layout(pad=5.0)
            df.plot.area(x=col_tuple[0], y=col_tuple[1], ax=axes.flat[count])
            count = count+1

    def combined_areaplot(self, df: pd.DataFrame, x_col: str, y_cols: list, stacked: bool, alpha: float = 0.25):
        """
          This function takes a Dataframe, its x-axis and a list of columns for the y-axis, stacked option and a value for the transparency
          of the figure(alpha).
        """
        df.plot.area(x=x_col, y=y_cols, stacked=stacked, alpha=alpha)

    def histogram(self, df: pd.DataFrame, col_dict: dict):
        """
          This function takes a Dataframe and a dictionary containing the column names as keys and their bins as values.
        """
        count = 1
        num_cols = len(col_dict)
        plt.subplots(nrows=1, ncols=num_cols, figsize=(20, 5))
        plt.tight_layout(pad=5.0)

        for key in col_dict:
            plt.subplot(1, num_cols, count)
            sns.histplot(df, x=key, bins=col_dict[key])
            count += 1

        plt.show()

    def individual_barplots(self, df: pd.DataFrame, col_list: list):
        """
          This function takes a Dataframe, and a list of tuples containing the column names whose bar plots are to be printed.
        """
        count = 1
        num_cols = len(col_list)
        plt.subplots(nrows=1, ncols=num_cols, figsize=(20, 5))
        plt.tight_layout(pad=5.0)

        for col_tuple in col_list:
            plt.subplot(1, num_cols, count)
            sns.barplot(data=df, x=col_tuple[0], y=col_tuple[1])
            count += 1

        plt.show()

    def piechart(self, df, col_list):
        """
          This function takes a Dataframe, an index value and a list of tuples containing the column names whose pie charts are to be printed.
        """
        num_cols = len(col_list)
        fig, axes = plt.subplots(nrows=1, ncols=num_cols, figsize=(15, 5))

        count = 0
        for col_tuple in col_list:
            plt.tight_layout(pad=5.0)
            df.groupby([col_tuple[0]]).sum().plot(
                kind='pie', y=col_tuple[1], ax=axes.flat[count])
            count = count+1

    def individual_boxplots(self, df: pd.DataFrame, col_list: list):
        """
          This function takes a Dataframe, and a list of tuples containing the column names whose box plots are to be printed.
        """
        count = 1
        num_cols = len(col_list)
        plt.subplots(nrows=1, ncols=num_cols, figsize=(10, 5))
        plt.tight_layout(pad=5.0)

        for column in col_list:
            plt.subplot(1, num_cols, count)
            sns.boxplot(y=df[column])
            count += 1

        plt.show()

    def combined_boxplot(self, df: pd.DataFrame, x_val: str, y_val: str):
        """
          This function takes a Dataframe, its x-axis and y-axis.
        """
        sns.boxplot(x=df[x_val], y=df[y_val])

    def visualize_labels(self, df: pd.DataFrame):
        """
          This function will visualize the labels variables so that user can get to know the distribution of the values
          of the labels
        """
        label_name = df.columns.to_list()[len(df.columns.to_list())-1]
        labels = df[label_name]
        targets = pd.DataFrame(data=labels, columns=[label_name])

        # creating a box plot in case of categorical data
        if (targets[label_name].dtype == 'O'):
            sns.catplot(x=label_name, kind="count",
                        palette="ch:.25", data=targets)

        # creating a histogram in case of numeric data
        elif (targets[label_name].dtype == 'float64' or targets[label_name].dtype == 'int64'):
            sns.histplot(targets, x=label_name)

        else:
            pass
