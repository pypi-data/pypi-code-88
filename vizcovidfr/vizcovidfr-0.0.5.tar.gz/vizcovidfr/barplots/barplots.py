# ---------- requirements ----------
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
import os
import plotly.express as px
import plotly.graph_objects as go


# local reqs
from vizcovidfr.loads import load_datasets
from vizcovidfr.loads.load_datasets import Load_posquotfr
from vizcovidfr.loads.load_datasets import Load_posquotreg
from vizcovidfr.loads.load_datasets import Load_poshebreg
from vizcovidfr.loads.load_datasets import Load_poshebfr
from vizcovidfr.loads.load_datasets import Load_incquotreg
from vizcovidfr.loads.load_datasets import Load_incquotfr
from vizcovidfr.loads.load_datasets import Load_inchebreg
from vizcovidfr.loads.load_datasets import Load_inchebfr

from vizcovidfr.preprocesses.preprocess_positivity import ignoreage
from vizcovidfr.preprocesses.preprocess_positivity import granupositivity
from vizcovidfr.preprocesses import preprocess_classe_age as pca


def bar_age(num_var, num_reg, save=False):
    """
    Display the bar plot of the given variable in the given region by age
    group today. Each variable and region have a special code that you can
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

    :return: Bar plot of one of the Covid variable in a specific region
        of France grouped by age.
    :rtype: plotly.graph_objects.bar.

    :Example:

    **Bar plot of hospitalization in Guadeloupe by age group today**

    >>> bar_age(1, 1)

    **Bar plot of hospitalization in Corse by age group today**

    >>> bar_age(1, 94)

    **Bar plot of deaths in Guadeloupe by age group today**

    >>> bar_age(7, 1)

    """
    # Testing execution time
    start = time.time()
    # Loading dataframe
    T = load_datasets.Load_classe_age().save_as_df()
    # Dropping rows where cl_age90 = 0
    T2 = pca.drop0(T)
    # Come back home and deaths are cumulative numbers, so we preprocess
    # them in another dataframe
    # Extracting 10 last rows of the given region (useful for variable 6 or 7)
    # dataframe
    T_rad_dc = pca.reg(num_reg, T2).tail(10)
    # Renaming columns
    T_rad_dc = pca.rename_cl(T_rad_dc)
    # Extracting the given region dataframe (1 to 5)
    data_reg = pca.reg(num_reg, T2)
    # Creating dictionnary
    dico_col = pca.dico_column(data_reg)
    data_reg_age = data_reg.groupby(by='cl_age90').sum()
    data_reg_age['cl_age90'] = data_reg_age.index
    data_reg_age = pca.rename_cl(data_reg_age)
    dico_file = pca.dico_file()
    dico_var = pca.dico_var()
    dico_reg = pca.dico_reg()
    # Plotting figure, condition depending of the variable
    if (num_var == 6 or num_var == 7):
        fig = px.bar(T_rad_dc, x='cl_age90', y=dico_col[num_var],
                     hover_data=[dico_col[num_var]],
                     color=dico_col[num_var],
                     labels={dico_col[num_var]: dico_var[dico_col[num_var]], 'cl_age90':'Age'},
                     height=400,
                     title="Bar plot of" + " " + dico_var[dico_col[num_var]] + " in " + dico_reg[num_reg] + " by age group today")
        fig.show()
    else:
        fig = px.bar(data_reg_age, x='cl_age90', y=dico_col[num_var],
                     hover_data=[dico_col[num_var]],
                     color=dico_col[num_var],
                     labels={dico_col[num_var]: dico_var[dico_col[num_var]], 'cl_age90':'Age'},
                     height=400,
                     title="Bar plot of" + " " + dico_var[dico_col[num_var]] + " in " + dico_reg[num_reg] + " by age group today")
        fig.show()
    # Saving pdf file
    if save:
        fig.write_image(f"bar_age_{dico_file[num_var]}_{dico_reg[num_reg]}.pdf")
    end = time.time()
    print("Time to execute: {0:.5f} s.".format(end - start))


def bar_reg(num_var, save=False):
    """
    Display the bar plot of the given variable by region group today.
    Each variable and region have a special code that you can see in
    function parameters for details.

    Parameters
    ----------

    :param num_var: code of the variable you want to display.
        Codes are in the following dictionary.
    :type num_var: int
    :param save: True if you want to save the graph in pdf file,
        False otherwise.
    :type save: bool, optional, default = False

    - Variable dictionary :

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


    - Region codes (official INSAA) :


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

    :return: Bar plot of one of the Covid variable by region group.
    :rtype: plotly.graph_objects.bar.

    :Example:

    **Bar plot of hospitalization in Guadeloupe by age group today**

    >>> bar_reg(1)

    **Bar plot of hospitalization in Corse by age group today**

    >>> bar_reg(7)

    """
    # Testing execution time
    start = time.time()
    # Loading dataframe
    T = load_datasets.Load_classe_age().save_as_df()
    # Drop rows where cl_age90 = 0
    T2 = pca.drop0(T)
    # Come back home and deaths are cumulative numbers, so we preprocess them in another dataframe
    # Extracting 18 last rows (useful for variable 6 or 7) dataframe
    T_rad_dc = pca.rad_dc(T)
    # Grouping by region
    data_day = T2.groupby(by='reg').sum()
    # Creating dictionnaries
    dico_file = pca.dico_file()
    dico_col = pca.dico_column(T2)
    dico_var = pca.dico_var()
    dico_reg = pca.dico_reg()
    # Come back home and deaths are cumulative numbers, so we take the value
    # of the last day recorded
    # Plotting figures
    if num_var == 6 or num_var == 7:
        fig = px.bar(T_rad_dc, x=T_rad_dc['reg'],
                     y=dico_col[num_var], color=dico_col[num_var],
                     labels={
                        dico_col[num_var]: dico_var[dico_col[num_var]],
                        'reg': 'Region in France'},
                     height=400,
                     title="Bar plot of" + " " + dico_var[dico_col[num_var]] + " by region group today")
        fig.update_xaxes(type='category')
        fig.show()
    else:
        fig = px.bar(data_day, x=data_day.index,
                     y=dico_col[num_var], color=dico_col[num_var],
                     labels={
                        dico_col[num_var]: dico_var[dico_col[num_var]],
                        'reg': 'Region in France'},
                     height=400,
                     title="Bar plot of" + " " + dico_var[dico_col[num_var]] + " by region group today")
        fig.update_xaxes(type='category')
        fig.show()
    # Saving file
    if save:
        fig.write_image(f"bar_reg_{dico_file[num_var]}.pdf")
    end = time.time()
    print("Time to execute: {0:.5f} s.".format(end - start))


def compareMF(date, criterion='incidence', granularity='France', num_reg=None,
              cumulative=False):
    """
    Make a comparative barplot between males and females for a chosen
    criterion.

    Parameters
    ----------
    :param date:
        a day on the format 'YYYY-MM-DD' or a week on the format 'YYYY-SWW'
    :type date: str
    :param criterion:
        'positivity': positivity rate (1/100)
        'P': positive cases
        'T': tests done
        'incidence': incidence rate (1/100000)
    :type criterion: str, optional, default='incidence'
    :param granularity: the granularity we want the heatmap to be based on.
        Should be either 'region' or 'France'.
    :type granularity: str, optional, default='France'
    :param num_reg: code of the region you want to display.
        Codes are the official INSAA code region and are given in the
        dictionary below.
    :type num_reg: int, optional (useful only if granularity='region'),
        default=Guadeloupe

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

    :param cumulative:
        if True: cumulative number since the beginning of the records of
            the criterion of interest until the chosen date
        if False: number for the given date
    :type cumulative: bool

    Returns
    -------
    :return: A comparative barplot between males and females for a chosen
        criterion
    :rtype: matplotlib.pyplot.bar

    :Examples:
    >>> compareMF(date="2021-04-12", criterion='incidence',
    ...           granularity='region', num_reg=1, cumulative=True)

    >>> compareMF(date='2020-11-12', criterion='P', granularity='France')
    """
    start = time.time()
    if (criterion == 'P'):
        legend = 'positive cases'
    elif (criterion == 'T'):
        legend = 'tests done'
    elif (criterion == 'positivity'):
        legend = 'positivity rate'
    else:
        legend = 'incidence rate'
    if (granularity == 'region'):
        dico_reg = pca.dico_reg()
        where = dico_reg[num_reg]
    else:
        where = 'France'
    if cumulative:
        cum = 'cumulated'
    else:
        cum = ''
    if criterion in ["P", "T", "positivity"]:
        if (granularity == "France"):
            if (len(date) > 8):
                df = ignoreage(Load_posquotfr().save_as_df())
            else:
                df = ignoreage(Load_poshebfr().save_as_df())
        elif (granularity == "region"):
            if (len(date) > 8):
                df = ignoreage(Load_posquotreg().save_as_df())
            else:
                df = ignoreage(Load_poshebreg().save_as_df())
        if (granularity == "region"):
            gra = 'reg'
            df = granupositivity(df, num_reg, gra)
    if (criterion == "incidence"):
        if (granularity == "France"):
            if (len(date) > 8):
                df = ignoreage(Load_incquotfr().save_as_df())
            else:
                df = ignoreage(Load_inchebfr().save_as_df())
        elif (granularity == "region"):
            if (len(date) > 8):
                df = ignoreage(Load_incquotreg().save_as_df())
            else:
                df = ignoreage(Load_inchebreg().save_as_df())
        if (granularity == "region"):
            gra = 'reg'
            df = granupositivity(df, num_reg, gra)
    fig, ax = plt.subplots()
    sex = ['male', 'female']
    if cumulative:
        df = df.cumsum()
    if criterion in ["P", "T"]:
        positive = [df.loc[date, ][criterion + "_h"],
                    df.loc[date, ][criterion + "_f"]]
    if (criterion == "positivity"):
        positive = [df.loc[date, ]["P_h"]/df.loc[date, ]["T_h"],
                    df.loc[date, ]["P_f"]/df.loc[date, ]["T_f"]]
    if (criterion == "incidence"):
        positive = [df.loc[date, ]["P_h"]*100000/df.loc[date, ]["pop_h"],
                    df.loc[date, ]["P_f"]*100000/df.loc[date, ]["pop_f"]]
    ax.bar(sex, positive)
    plt.title(f'Sex comparison of {cum} {legend} in {where}')
    plt.xlabel('Sex')
    plt.ylabel(f'{cum} {legend}')
    end = time.time()
    print("Time to execute: {0:.5f} s.".format(end - start))
    plt.show()
