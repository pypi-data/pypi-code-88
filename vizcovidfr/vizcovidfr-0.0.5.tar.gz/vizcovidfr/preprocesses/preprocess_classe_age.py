# ---------- requirements ----------
import pandas as pd
import numpy as np
import operator

from vizcovidfr.loads import load_datasets
from sklearn.linear_model import LinearRegression

from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
model = LinearRegression()

T = load_datasets.Load_classe_age().save_as_df()


def drop0(T):
    '''
    Delete lines where cl_age90 is 0 in the 'classe_age' dataset.
    :param T: dataframe where one of the column is 'cl_age90'.
    :type T: Pandas dataframe
    :return: sub-dataframe of 'classe_age'
    :rtype: Pandas dataframe
    '''
    T = T.drop(T[T['cl_age90'] == 0].index)
    return T


def date_time(df):
    '''
    Convert date column to datetime format.
    :param df: dataframe where one of the column is 'jour'.
    :type df: Pandas dataframe
    :return: sub-dataframe of 'classe_age'
    :rtype: Pandas dataframe
    '''
    df['jour'] = pd.to_datetime(df['jour'])
    return df


def reg(x, T):
    '''
    Extract from 'classe_age' the dataframe of the region x.
    :param x: number of the region.
        Region codes are available in the documentation.
    :type x: int
    :param T: classe_age dataframe
    :type T: Pandas dataframe
    :return: sub-dataframe of 'classe_age'
    :rtype: Pandas dataframe
    '''
    A = T[T['reg'] == x]
    return A


def covid_day_fct(T):
    '''
    Groupby the dataframe by day, summing others columns and add column
        from index.
    :param T: classe_age dataframe.
    :type T: Pandas dataframe
    :return: sub-dataframe of 'classe_age'
    :rtype: Pandas dataframe
    '''
    A = T.groupby(by=['jour']).sum()
    A['jour'] = A.index
    return A


def rad_dc(T):
    '''
    Function for variable 6 and 7 to get their total today.
    :param T: classe_age dataframe
    :type T: Pandas dataframe
    :return: sub-dataframe of 'classe_age'
    :rtype: Pandas dataframe
    '''
    T1 = T[T['cl_age90'] == 0]
    X = T1.tail(18)
    return X


def rename_cl(T):
    '''
    Rename cl_age90 clumn.
    :param T: classe_age dataframe.
    :type T: Pandas dataframe
    :return: sub-dataframe of 'classe_age'
    :rtype: Pandas dataframe
    '''
    T['cl_age90'] = ['0-9', '10-19', '20-29', '30-39', '40-49',
                     '50-59', '60-69', '70-79', '80-89', '+90']
    return T


# Creation of some dictionaries
def dico_column(T):
    '''
    Create dictionary of variables with column of T.
    :param T: classe_age dataframe.
    :type T: Pandas dataframe
    :return: dictionary of variables
    :rtype: dict
    '''
    dico_col = {}
    for i in np.arange(1, T.shape[1]-2):
        dico_col[i] = T.columns[i+2]
    return dico_col


def dico_day(T):
    '''
    Create dictionary of days with rows of T.
    :param T: classe_age dataframe.
    :type T: Pandas dataframe
    :return: dictionary of days
    :rtype: dict
    '''
    dico_day = {}
    for i in np.arange(0, T.shape[0]):
        dico_day[i] = T.iloc[i, 9]
    return dico_day


def dico_var():
    '''
    Create dictionary for title.
    :return: dictionary
    :rtype: dict
    '''
    dico_var = {'hosp': 'Hospitalization', 'rea': 'Reanimation',
                'cl_age90': 'Age', 'HospConv': 'Conventional hospitalization',
                'SSR_USLD': 'SSR and USLD', 'autres': 'Others',
                'rad': 'Come back home', 'dc': 'Deaths'}
    return dico_var


def dico_reg():
    '''
    Create dictionary for region.
    :return: dictionary of region
    :rtype: dict
    '''
    dico_reg = {1: 'Guadeloupe', 2: 'Martinique', 3: 'Guyane', 4: 'La Reunion',
                6: 'Mayotte', 11: 'Île-de-France', 24: 'Centre-Val de Loire',
                27: 'Bourgogne-Franche-Comte', 28: 'Normmandie',
                32: 'Hauts-de-France', 44: 'Grand Est', 52: 'Pays de la Loire',
                53: 'Bretagne', 75: 'Nouvelle-Aquitaine', 76: 'Occitanie',
                84: 'Auvergne-Rhône-Alpes', 93: "Provence-Alpes Côte d'Azur",
                94: 'Corse'}
    return dico_reg


def dico_file():
    '''
    Create dictionary for saving file.
    :return: dictionary
    :rtype: dict
    '''
    dico_file = {1: 'hospitalization', 2: 'reanimation', 3: 'hosp_conv',
                 4: 'SSR_USLD', 5: 'others', 6: 'back_home', 7: 'deaths'}
    return dico_file


# Function which list the mean squared error and predict y
def degreeChoice(x, y, degree):
    '''
    Give the mean squared error, x predicted and y predicted.
    :param x: abscissa of points we want to predict
    :type x: list
    :param y: ordonate of points we want to predict
    :type y: list
    :param degree: degree of the regression polynom
    :type degree: int
    :return: mean squared error, x predicted and y predicted
    :rtype: float, float, float
    '''
    # Generate a new feature matrix consisting of all polynomial combinations
    # of the features with degree less than or equal to the specified degree.
    polynomial_features = PolynomialFeatures(degree=degree)
    # Scaling and fitting
    x_poly = polynomial_features.fit_transform(x)
    model = LinearRegression()
    model.fit(x_poly, y)
    # Prediction of y
    y_poly_pred = model.predict(x_poly)
    # Root of mean squared error (RMSE)
    rmse = np.sqrt(mean_squared_error(y, y_poly_pred))
    sort_axis = operator.itemgetter(0)
    sorted_zip = sorted(zip(x, y_poly_pred), key=sort_axis)
    x_p, y_poly_pred_P = zip(*sorted_zip)
    return rmse, x_p, y_poly_pred_P


def rmse_list(x, y):
    '''
    Give the list of mean squared error, x predicted and y predicted
    depending of polynom degree.
    :param x: abscissa of points we want to predict
    :type x: list
    :param y: ordonate of points we want to predict
    :type y: list
    :return: list of mean squared error, x predicted and y predicted
    :rtype: list, list, list
    '''
    rmselist = np.zeros(100)
    x_p_list = [None]*100
    y_poly_pred_P_list = [None]*100
    for i in np.arange(1, 101):
        rmselist[i-1], x_p_list[i-1], y_poly_pred_P_list[i-1] = degreeChoice(x, y, i)
    return rmselist, x_p_list, y_poly_pred_P_list
