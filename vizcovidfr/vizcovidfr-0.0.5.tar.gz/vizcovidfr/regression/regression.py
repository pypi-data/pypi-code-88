# ---------- requirements ----------
import time
import numpy as np
import pandas as pd
import plotly.express as px

import matplotlib.pyplot as plt
import matplotlib.lines as mlines

from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

# local reqs
from vizcovidfr.loads import load_datasets
from vizcovidfr.preprocesses import preprocess_classe_age as pca

# add python option to avoid "false positive" warning:
pd.options.mode.chained_assignment = None  # default='warn'

# scikitlearn model
model = LinearRegression()


def scatter_reg(num_var, num_reg, save=False):
    """
    Display the scatter plot of the evolution of the given variable in the
    given region. Each variable and region have a special code that you can
    see in function parameters for details.

    Parameters
    ----------

    :param num_var: code of the variable you want to display.
        Codes are in the following dictionary.
    :type num_var: int
    :param num_reg: code of the region you want to display.
        Codes are the official INSAA code region and are given in the
        dictionary below.
    :type num_reg: int
    :param save: True if you want to save the graph in pdf file,
        False otherwise.
    :type save: bool, optional, default = False

    Variable dictionary :

        1 : Hospitalization

        2 : Reanimation

        3 : Conventional hospitalization

        4 : SSR and USLD

        5 : Others

        6 : Come back home

        7 : Deaths

    - Hospitalization :
        number of hospitalized patients.

    - Reanimation :
        number of people currently in intensive care.

    - Conventional hospitalization :
        number of people currently in conventional hospitalization.

    - SSR and USLD :
        number of people currently in Aftercare and Rehabilitation
        (SSR in french) or Long-Term Care Units (USLD in french).

    - Others :
        number of people currently hospitalized in another type of service.

    - Come back home :
        cumulative number of people who returned home.

    - Deaths :
        cumulative number of deceased persons.


    Region dictionary :

        1 : Guadeloupe

        2 : Martinique

        3 : Guyane

        4 : La Reunion

        6 : Mayotte

        11 : Île-de-France

        24 : Centre-Val de Loire

        27 : Bourgogne-Franche-Comte

        28 : Normandie

        32 : Hauts-de-France

        44 : Grand Est

        52 : Pays de la Loire

        53 : Bretagne

        75 : Nouvelle-Aquitaine

        76 : Occitanie

        84 : Auvergne-Rhône-Alpes

        93 : Provence-Alpes Côte d'Azur

        94 : Corse

    Returns
    ----------

    :return: Scatter plot of one of the Covid variable in a specific
        region of France.
    :rtype: Figure

    :Example:

    **Scatter plot of hospitalization in Île-de-France**

    >>> scatter_reg(1, 11)

    """
    # Test execution time
    start = time.time()
    # Loading dataframe
    T = load_datasets.Load_classe_age().save_as_df()
    # Extracting chosen region
    T2 = pca.reg(num_reg, T)
    # Converting to datetime format
    T2 = pca.date_time(T2)
    # Creating dictionnary with columns
    dico_col = pca.dico_column(T2)
    # Grouping by day
    covid_day = pca.covid_day_fct(T2)
    # Creating dictionaries
    dico_file = pca.dico_file()
    dico_reg = pca.dico_reg()
    dico_var = pca.dico_var()
    # Scatter plot
    fig = px.scatter(
                covid_day,
                x=covid_day.index,
                y=dico_col[num_var],
                opacity=0.65,
                trendline_color_override='darkblue',
                labels={
                    dico_col[num_var]: dico_var[dico_col[num_var]],
                    'index': 'Date'},
                title="Scatter plot of the evolution of" +
                      " " +
                      dico_var[dico_col[num_var]] +
                      " in " +
                      dico_reg[num_reg])
    if (save):
        fig.write_image(
                f'scatter_{dico_file[num_var]}_{dico_reg[num_reg]}.pdf')
    end = time.time()
    print("Time to execute: {0:.5f} s.".format(end - start))
    fig.show()


def poly_fit(num_var, num_reg, save=False):
    """
    Display the scatter plot of the evolution of the given variable in the
    given region with a polynomial regression. Each variable and region have
    a special code that you can see in function parameters for details.
    Degree of polynom is chosen by minimizing the mean squared error
    and is displayed as well.

    Parameters
    ----------

    :param num_var: code of the variable you want to display.
        Codes are in the following dictionary.
    :type num_var: int
    :param num_reg: code of the region you want to display.
        Codes are the official INSAA code region and are given in the
        dictionary below.
    :type num_reg: int
    :param save: True if you want to save the graph in pdf file,
        False otherwise.
    :type save: bool, optional, default=False

    Variable dictionary :

        1 : Hospitalization

        2 : Reanimation

        3 : Conventional hospitalization

        4 : SSR and USLD

        5 : Others

        6 : Come back home

        7 : Deaths

    - Hospitalization :
        number of hospitalized patients.

    - Reanimation :
        number of people currently in intensive care.

    - Conventional hospitalization :
        number of people currently in conventional hospitalization.

    - SSR and USLD :
        number of people currently in Aftercare and Rehabilitation
        (SSR in french) or Long-Term Care Units (USLD in french).

    - Others :
        number of people currently hospitalized in another type of service.

    - Come back home :
        cumulative number of people who returned home.

    - Deaths :
        cumulative number of deceased persons.


    Region dictionary :

        1 : Guadeloupe

        2 : Martinique

        3 : Guyane

        4 : La Reunion

        6 : Mayotte

        11 : Île-de-France

        24 : Centre-Val de Loire

        27 : Bourgogne-Franche-Comte

        28 : Normandie

        32 : Hauts-de-France

        44 : Grand Est

        52 : Pays de la Loire

        53 : Bretagne

        75 : Nouvelle-Aquitaine

        76 : Occitanie

        84 : Auvergne-Rhône-Alpes

        93 : Provence-Alpes Côte d'Azur

        94 : Corse

    Returns
    ----------

    :return: Scatter plot of one of the Covid variable in a specific region
        of France with the regression curve.
    :rtype: Figure

    :Example:

    **Polynomial regression of hospitalization in Île-de-France**

    >>> poly_fit(1, 11)

    **Polynomial regression of hospitalization in Provence**

    >>> poly_fit(1, 93)

    """
    # Testing execution time
    start = time.time()
    # Loading dataframe
    T = load_datasets.Load_classe_age().save_as_df()
    # Extracting chosen region
    R = pca.reg(num_reg, T)
    # Converting to datetime format
    R = pca.date_time(R)
    # Creating dictionnary with columns
    dico_col = pca.dico_column(R)
    # Grouping by day
    covid_day = pca.covid_day_fct(R)
    # Defining x and y
    x = np.arange(0, covid_day.shape[0])
    y = covid_day[dico_col[num_var]]
    x = x[:, np.newaxis]
    y = y[:, np.newaxis]
    # Creating dictionnaries
    dico_days = pca.dico_day(covid_day)
    dico_file = pca.dico_file()
    dico_var = pca.dico_var()
    dico_reg = pca.dico_reg()
    # Reseting index
    covid_day = covid_day.reset_index(drop=True)
    # Creating root of mean squared error (RMSE), x_p and y_predict list
    rmselist, x_p_list, y_poly_pred_P_list = pca.rmse_list(x, y)
    # Choosing degree which mimnimize RMSE
    deg = list(rmselist).index(rmselist.min())
    # Plotting figure
    fig = plt.scatter(dico_days.values(), y)
    plt.plot(dico_days.values(),
             y_poly_pred_P_list[deg],
             color='r')
    plt.suptitle("Polynomial regression of" +
                 " " +
                 dico_var[dico_col[num_var]] +
                 " in " +
                 dico_reg[num_reg]).set_fontsize(15)
    blue_line = mlines.Line2D(
                          [], [], color='blue',
                          markersize=15,
                          marker='.', label=dico_var[dico_col[num_var]])
    red_line = mlines.Line2D(
                          [], [], color='red',
                          markersize=15, label='Regression curve')
    plt.legend(handles=[blue_line, red_line])
    plt.title(f'Degree of polynomial regression : {deg+1}', fontsize=10)
    # Saving pdf file
    if (save):
        plt.savefig(f"regression_" +
                    dico_file[num_var] +
                    "_" + dico_reg[num_reg] +
                    ".pdf", dpi=1200)
    end = time.time()
    print("Time to execute: {0:.5f} s.".format(end - start))
    plt.show()


def R2(num_var, num_reg):
    """
    Display the R2 of the polynomial regression made by poly_fit function.

    Parameters
    ----------

    :param num_var: code of the variable you want to display.
        Codes are in the following dictionary.
    :type num_var: int
    :param num_reg: code of the region you want to display.
        Codes are the official INSAA code region and are given in the
        dictionary below.
    :type num_reg: int

    Variable dictionary :

        1 : Hospitalization

        2 : Reanimation

        3 : Conventional hospitalization

        4 : SSR and USLD

        5 : Others

        6 : Come back home

        7 : Deaths

    - Hospitalization :
        number of hospitalized patients.

    - Reanimation :
        number of people currently in intensive care.

    - Conventional hospitalization :
        number of people currently in conventional hospitalization.

    - SSR and USLD :
        number of people currently in Aftercare and Rehabilitation
        (SSR in french) or Long-Term Care Units (USLD in french).

    - Others :
        number of people currently hospitalized in another type of service.

    - Come back home :
        cumulative number of people who returned home.

    - Deaths :
        cumulative number of deceased persons.


    Region dictionary :

        1 : Guadeloupe

        2 : Martinique

        3 : Guyane

        4 : La Reunion

        6 : Mayotte

        11 : Île-de-France

        24 : Centre-Val de Loire

        27 : Bourgogne-Franche-Comte

        28 : Normandie

        32 : Hauts-de-France

        44 : Grand Est

        52 : Pays de la Loire

        53 : Bretagne

        75 : Nouvelle-Aquitaine

        76 : Occitanie

        84 : Auvergne-Rhône-Alpes

        93 : Provence-Alpes Côte d'Azur

        94 : Corse

    Returns
    ----------

    :return: R2 of the polynomial regression of one of the Covid variable in
        a specific region of France.
    :rtype: float

    :Example:

    **R2 of polynomial regression of hospitalization in Île-de-France**

    >>> R2(1, 11)

    """
    # Testing execution time
    start = time.time()
    # Loading dataframe
    T = load_datasets.Load_classe_age().save_as_df()
    # Extracting chosen region
    R = pca.reg(num_reg, T)
    # Converting to format datetime
    R = pca.date_time(R)
    # Creating dictionnary with columns
    dico_col = pca.dico_column(R)
    # Grouping by day
    covid_day = pca.covid_day_fct(R)
    # Defining x and y
    x = np.arange(0, covid_day.shape[0])
    y = covid_day[dico_col[num_var]]
    x = x[:, np.newaxis]
    y = y[:, np.newaxis]
    # Creating dictionnaries
    dico_var = pca.dico_var()
    dico_reg = pca.dico_reg()
    # Reseting index
    covid_day = covid_day.reset_index(drop=True)
    # Creating root of mean squared error (RMSE), x_p and y_predict list
    rmselist, x_p_list, y_poly_pred_P_list = pca.rmse_list(x, y)
    # Choosing degree which minimize RMSE
    deg = list(rmselist).index(rmselist.min())
    # Calculating R2
    res = 'R2 of polynomial regression of ' + dico_var[dico_col[num_var]] + \
          ' in ' + dico_reg[num_reg] + \
         f' is : {r2_score(y,y_poly_pred_P_list[deg])}.'
    end = time.time()
    print("Time to execute: {0:.5f} s.".format(end - start))
    return res
