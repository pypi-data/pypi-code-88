"""Module for data preprocessing
Date: 25/May/2020
Author: Li Tang
"""
from __future__ import absolute_import, division, print_function, unicode_literals
from typing import List

import pandas as pd
from sklearn.preprocessing import StandardScaler

__author__ = ['Li Tang']
__copyright__ = 'Li Tang'
__credits__ = ['Li Tang']
__license__ = 'MIT'
__version__ = '0.1.12'
__maintainer__ = ['Li Tang']
__email__ = 'litang1025@gmail.com'
__status__ = 'Production'


class SuiToolboxPreprocessingError(Exception):
    pass


def month_to_int(month: str, unknown: int = None) -> int:
    """transfer a month string into an integer

    Args:
    month: input string of a month
    unknown: an integer to be returned if the month cannot be parsed

    Returns:
        an integer standing for the specific month

    Examples:
        >>> months = ['Apr', 'May', '10', 'December']
        >>> [month_to_int(month=month, unknown=0) for month in months]
        [4, 5, 0, 12]
    """
    month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5,
                  'June': 6, 'July': 7, 'August': 8,
                  'September': 9, 'October': 10, 'November': 11, 'December': 12}

    month_abbr_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5,
                       'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9,
                       'Oct': 10, 'Nov': 11, 'Dec': 12}

    if month in month_dict:
        return month_dict[month]

    elif month in month_abbr_dict:
        return month_abbr_dict[month]

    else:
        if unknown is None:
            raise SuiToolboxPreprocessingError(
                "This input month '{}' cannot be parsed.".format(month))
        else:
            return unknown


def weekday_to_int(weekday: str, unknown: int = None) -> int:
    """transfer a weekday string into an integer

    Args:
    weekday: input string of a weekday
    unknown: an integer to be returned if the weekday cannot be parsed

    Returns:
        an integer standing for the specific weekday

    Examples:
        >>> weekdays = ['Mon', 'Tue', 'Sunday', 'F']
        >>> [weekday_to_int(weekday=day, unknown=0) for day in weekdays]
        [1, 2, 7, 0]
    """
    weekday_dict = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4,
                    'Friday': 5, 'Saturday': 6, 'Sunday': 7}

    weekday_abbr_dict = {'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4, 'Fri': 5,
                         'Sat': 6, 'Sun': 7}

    if weekday in weekday_dict:
        return weekday_dict[weekday]

    elif weekday in weekday_abbr_dict:
        return weekday_abbr_dict[weekday]

    else:
        if unknown is None:
            raise SuiToolboxPreprocessingError(
                "This input weekday '{}' cannot be parsed.".format(weekday))
        else:
            return unknown


def one_hot(X_: pd.DataFrame, categorical_feats: List[str] = []):
    """one-hot function

    Args:
    X_: input pandas dataframe
    categorical_feats: list storing column names for all columns to transfer

    Returns:
        a pandas dataframe concatenated original columns not in categorical_feats and the one-hot result of all columns
        in categorical_feats

    Examples:
        >>> data = {
        ...     'id':['001', '002', '003', '004', '005'],
        ...     'fields': ['pharm', 'tech', 'pharm', 'tech', 'tech'],
        ...     'price': [28.93, 15.92, 83.2, 44.68, 19.22],
        ...     'increase': [1.12, 2.08, 5.79, 8.37, -2.90],
        ...     'country': ['CN', 'CN', 'UK', 'UK', 'UK']
        ... }
        >>> df = pd.DataFrame(data=data)
        >>> df = one_hot(X_=df, categorical_feats=['fields', 'country'])
        >>> pd.set_option("display.max_columns", None)
        >>> df
            id  increase  price  fields_pharm  fields_tech  country_CN  country_UK
        0  001      1.12  28.93             1            0           1           0
        1  002      2.08  15.92             0            1           1           0
        2  003      5.79  83.20             1            0           0           1
        3  004      8.37  44.68             0            1           0           1
        4  005     -2.90  19.22             0            1           0           1

    """
    categorical_feats = X_.columns if len(categorical_feats) == 0 else categorical_feats
    X_categorical = pd.get_dummies(
        X_[categorical_feats].astype('category'))

    return pd.concat([X_[X_.columns.difference(categorical_feats)], X_categorical], axis=1, join='inner')


def standardization(X_, numerical_feats: List[str] = []):
    """standardization

    Args:
    X_:
    numerical_feats:

    Returns:
        a pandas dataframe.

    Examples:
        >>> data = {
        ...     'id':['001', '002', '003', '004', '005'],
        ...     'fields': ['pharm', 'tech', 'trans', 'tech', 'env'],
        ...     'price': [28.93, 15.92, 83.2, 44.68, 19.22],
        ...     'increase': [1.12, 2.08, 5.79, 8.37, -2.90],
        ...     'country': ['CN', 'CN', 'UK', 'US', 'US']
        ... }
        >>> df = pd.DataFrame(data=data)
        >>> df = standardization(X_=df, numerical_feats=['price', 'increase'])
        >>> df
          country fields   id     price  increase
        0      CN  pharm  001 -0.385600 -0.455247
        1      CN   tech  002 -0.915903 -0.208612
        2      UK  trans  003  1.826507  0.744530
        3      US   tech  004  0.256388  1.407362
        4      US    env  005 -0.781391 -1.488032

    """
    numerical_feats = X_.columns if len(numerical_feats) == 0 else numerical_feats
    X_numerical = X_[numerical_feats]
    X_standardization = pd.DataFrame(
        StandardScaler().fit_transform(X_numerical),
        columns=X_numerical.columns)
    X = pd.concat([X_[X_.columns.difference(numerical_feats)], X_standardization], axis=1, join='inner')

    return X
